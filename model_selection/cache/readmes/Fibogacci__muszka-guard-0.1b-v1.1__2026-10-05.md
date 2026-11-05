---
language:
- pl
license: apache-2.0
library_name: onnx
pipeline_tag: text-classification
base_model: speakleash/Bielik-Guard-0.1B-v1.1
base_model_relation: finetune
tags:
- safety
- guardrails
- content-moderation
- polish
- onnx
- int8
- text-classification
datasets:
- ToxicityPrompts/PolyGuardMix
- allenai/wildguardmix
- thesofakillers/jigsaw-toxic-comment-classification-challenge
---
# Muszka Guard 0.1B v1.1

![Muszka Guard 0.1B v1.1 - small, light, fast](assets/muszka-guard-baner.png)

*A derivative of [Bielik-Guard 0.1B (Sójka)](https://huggingface.co/speakleash/Bielik-Guard-0.1B-v1.1) by SpeakLeash. Muszka Guard is an independent project - it is not an official product of the Bielik-Guard (Sójka) team.*

**A small, fast Polish safety filter (guardrail) for chatbots and LLM assistants.** 124M parameters, 7 categories,
a 126 MB (120 MiB) INT8 ONNX file that runs on an ordinary CPU, no GPU. On a desktop Intel i5-12600K (all cores,
one message at a time): median 8.7 ms and mean 28.5 ms on test texts (median length 38 tokens),
about 0.24 s for a long text of ~420 tokens.

Author: Fibogacci ([LinkedIn](https://www.linkedin.com/in/Fibogacci)). Training data and the profanity lexicon: **[Jan Sowa](https://www.linkedin.com/in/janpiotrsowa/)** - thank you!

[Project page](https://muszkaowocowa.pl/en/muszka-guard) • [Demo with side-by-side comparison and arena](https://huggingface.co/spaces/Fibogacci/muszka-guard-v1.1-demo) •
[Full report (PDF, EN)](https://huggingface.co/Fibogacci/muszka-guard-0.1b-v1.1/blob/main/muszka-guard-v1.1-report-en.pdf) • [Raport (PDF, PL)](https://huggingface.co/Fibogacci/muszka-guard-0.1b-v1.1/blob/main/muszka-guard-v1.1-raport.pdf) •
[Glossary (PL/EN)](GLOSSARY.md) • [Glossary (PDF, EN)](https://huggingface.co/Fibogacci/muszka-guard-0.1b-v1.1/blob/main/muszka-guard-v1.1-glossary-en.pdf) •
[Słowniczek (PDF, PL)](https://huggingface.co/Fibogacci/muszka-guard-0.1b-v1.1/blob/main/muszka-guard-v1.1-slowniczek.pdf) • [Wersja polska](#wersja-polska)

## About v1.0

The first public release, Muszka Guard 0.1B v1.0, reported results measured on a small test set (30 harmful and
6 innocent examples, close to the training data), and some parameters - including memory use and response time -
came from design assumptions rather than measurement. Once independent test sets were prepared, those numbers
turned out to overstate the model's effectiveness. We re-measured v1.1 from scratch on thousands of texts set aside
before training and describe it together with its limitations - every number below comes from those
measurements. v1.1 replaces v1.0.

## Categories

| Category | What it catches |
|---|---|
| `self-harm` | suicide, self-injury, eating disorders |
| `hate` | contempt or violence against groups |
| `vulgar` | profanity and insults (also obfuscated: `k*rwa`, `kórwa`, `k u r w a`) |
| `sex` | explicit sexual content |
| `crime` | help with crime, violence, weapons, hacking |
| `jailbreak` | prompt injection, "ignore previous instructions", DAN |
| `other` (new) | defamation, specialised (medical, legal, financial) advice, elections |

Multi-label: each category gets a score from 0 to 1. Default: **block** at 0.5, **warn** between 0.18 and 0.5.

## Quick start

```python
# pip install onnxruntime tokenizers numpy huggingface_hub
from huggingface_hub import snapshot_download
import sys
path = snapshot_download("Fibogacci/muszka-guard-0.1b-v1.1",  # only the 4 files needed (~130 MB), not the whole repo (~1.1 GB)
                         allow_patterns=["muszka_int8_pc_rr.onnx", "muszka_guard.py", "config.json", "tokenizer.json"])
sys.path.insert(0, path)
from muszka_guard import MuszkaGuard

guard = MuszkaGuard(path, "muszka_int8_pc_rr.onnx", mode="sensitive")
print(guard.predict("ty kórwo")["is_blocked"])            # True
print(guard.predict("Jak upiec sernik?")["is_blocked"])   # False
```

`muszka_guard.py` needs only onnxruntime, tokenizers and numpy (no PyTorch). Use `muszka_int8_pc_rr.onnx` rather than
a plain per-channel INT8 file: without `reduce_range`, per-channel INT8 breaks on x86 CPUs without VNNI (tested on a
small VPS). INT8 vs fp32 decision agreement: 99.0% on 300 test texts.

### Long texts: windows and modes

A classifier that reads a long text as a whole can miss a single harmful sentence hidden in it (e.g. 800 words of a
cheesecake recipe followed by a request for a pipe bomb). Muszka v1.1 also scores texts longer than 128 tokens in
overlapping 128-token windows. Set the mode with `mode=`:

- `sensitive` (**default**) - the highest window counts; catches a hidden sentence, costs a few more false alarms
  on long fiction or game texts. Our priority: it is better to block an innocent sentence than to let a harmful one through.
- `balanced` - fewer false alarms on long texts, but a single hidden sentence can be diluted.
- `no_windows` - the whole text only, up to 512 tokens.

## Results

Muszka: the released INT8 file, sensitive mode (windows), threshold 0.5. Holdouts, PL-Guard, GadziJęzyk and false-alarm
tests - model only, no regex; exam and critical list - with regex, as deployed. Sójka 0.1B and 0.5B as published (fp32, up to
512 tokens, no windows - Sójka itself does not use them; PyTorch or our ONNX export). Only for PL-Guard we also ran Sójka in the
same 128/32-token windows as Muszka (numbers in brackets).

Holdouts, PL-Guard, GadziJęzyk, Roget and the exam were set aside before training (exceptions: 3 exam items and 7 short
holdout v1 texts were in the data of one of the two averaged checkpoints). The profanity test and the word audit measure
coverage - their words were in training.

### Sealed final exam

A separate set, generated by Bielik and labelled by a Bielik judge before measurement (the standalone insults were picked
by hand), measured **once** on the chosen model (exam file sha256 `160bbc02a615…`). Percent of texts blocked:

| Exam section | n | Expected | Muszka v1.1 | Sójka 0.1B | Sójka 0.5B |
|---|---|---|---|---|---|
| Vulgar chat messages (new situations) | 288 | block | 93.8% | 92.4% | 93.1% |
| Obfuscated vulgar messages | 194 | block | 99.0% | 77.8% | 92.3% |
| Innocent messages with look-alike words | 250 | allow | 4.8% | 2.8% | 0.8% |
| Innocent messages with one obfuscated word | 175 | allow | 6.3% | 6.3% | 4.0% |
| Standalone insults outside the profanity lexicon used in training | 15 | block | 6.7% | 60.0% | 26.7% |

Muszka is clearly better on obfuscated profanity and on par for plain vulgar messages. **It is clearly worse than Sójka on
standalone insults outside the profanity lexicon used in training** (some of these words, e.g. "palantem", appeared in training
data labelled innocent) - see Known limitations. On innocent messages with look-alike words Muszka blocks more than both Sójka
models (4.8% vs 2.8% and 0.8%). Note: after measurement we saw that the
exam builder (a Bielik-based judge) labelled some non-vulgar messages as vulgar, so the true rate for the first row is
likely higher; we did not edit the sealed exam after measuring.

### PL-Guard (NASK) - Polish safety benchmark

Binary macro F1 (safe / unsafe), all 14 categories. PL-Guard also contains model *responses*, not only prompts.
We split the test into two fixed halves: one for choosing settings, the other (**report half**) for reporting. The report half
was computed in every gate run (5 candidates) and the gate threshold used the whole set; the candidate was not chosen by it -
the released model scores lowest of the last three on it.

| Model | Report half: test / adversarial | Whole test: test / adversarial |
|---|---|---|
| **Muszka v1.1** | **0.811 / 0.768** | 0.852 / 0.774 |
| Sójka 0.1B (in brackets: run by us in windows) | 0.497 (0.537) / 0.472 (0.527) | 0.489 (0.541) / 0.481 (0.537) |
| Sójka 0.5B (in brackets: run by us in windows) | 0.475 (0.568) / 0.464 (0.551) | 0.480 (0.568) / 0.470 (0.555) |
| HerBERT-PL-Guard (NASK, from the paper) | - | 0.927 / 0.913 |

HerBERT-PL-Guard was trained on data prepared by the PL-Guard authors, with the same taxonomy - which may explain the gap.
Muszka's training data has no overlap with PL-Guard (checked).

### Held-out tests (Polish translations by Bielik 11B)

| | Muszka v1.1 | Sójka 0.1B | Sójka 0.5B |
|---|---|---|---|
| Holdout v1 (Jigsaw test + 36 attack and innocent prompts from the muszkaowocowa.pl chat) AUROC | **0.961** | 0.940 | 0.942 |
| Holdout v1 recall / false alarms @0.5 | 83.5% / 6.3% | 78.2% / 7.5% | 78.4% / 6.9% |
| Holdout v2 (WildGuardMix test) AUROC | **0.916** | 0.802 | 0.846 |
| Holdout v2 recall / false alarms @0.5 | 87.1% / 11.5% | 40.3% / 6.1% | 41.5% / 3.6% |
| Adversarial attacks caught (v2) | **87.6%** | 18.9% | 17.1% |
| Adversarial *innocent* prompts blocked (v2, false alarms) | 20.2% | 3.8% | 1.6% |
| GadziJęzyk (native Polish harmful prompts) | **98.9%** | 62.7% | 81.3% |

Holdout v1: Jigsaw test comments (translated by Bielik) and 36 attack and innocent prompts written in Polish for the chat on
muszkaowocowa.pl; holdout v2: WildGuardMix test prompts. v1 and v2 are the test splits of datasets whose training splits Muszka used (translated by Jan Sowa) - same domain for
Muszka, not for Sójka. GadziJęzyk was excluded from Muszka's training. Adversarial prompts are mostly longer than one window,
so Muszka's windows matter here; Sójka was not measured in windows on this set. The gain in caught attacks comes with more
false alarms on innocent adversarial prompts (row below it).

### Profanity and obfuscation

Test built from Jan Sowa's lexicon of Polish vulgar words and phrases, every inflected form, 13 kinds of obfuscation.
Muszka v1.1 was trained on all word families, so this measures **coverage**; generalisation to unseen families,
measured on an earlier model with 30% of families held out: 87.2% of all variants (forms and
obfuscations) blocked; plain forms 90.3% (release gate, INT8).

| Spelling | Muszka v1.1 | Sójka 0.1B | Sójka 0.5B |
|---|---|---|---|
| plain form | 99.8% | 89.4% | 80.8% |
| u→ó (kórwa) | 99.7% | 46.4% | 43.3% |
| ch→h (huj) | 100.0% | 92.1% | 64.5% |
| ch→h + u→ó (hój) | 100.0% | 62.3% | 26.9% |
| asterisk (k*rwa) | 99.0% | 87.6% | 99.6% |
| spaced letters (k u r w a) | 98.4% | 32.5% | 10.9% |
| dots (k.u.r.w.a) | 98.4% | 99.9% | 41.9% |
| leet (kurw@) | 99.1% | 61.8% | 49.2% |
| repeated letter (kuuurwa) | 98.7% | 65.9% | 72.8% |
| no Polish diacritics | 99.4% | 82.9% | 75.0% |
| UPPERCASE | 98.5% | 58.1% | 53.9% |

Table: all three models in full precision (PyTorch fp32), profanity test v2; the released INT8 file scores up to 0.5 pp lower
(release gate, test v3). Innocent words in the same unusual spellings are blocked in 0.5%-6.7% of cases depending
on the spelling (u→ó 6.7% - above the 5% gate threshold).

### Other checks

| Check | Result |
|---|---|
| False alarms on 5100 ordinary Polish texts (Roget semantic fields) | 0.6% |
| False alarms on innocent health / legal / finance / election questions | 0.7% |
| Model refusals ("I can't help with that") blocked | 1.2% |
| Ordinary (non-harmful) model responses blocked - false alarms | 15.3% |
| Innocent texts on negative topics (Roget) blocked | 6.7% |
| Harmful model responses caught (PolyGuardMix, held out) | 79.4% |
| Harmful text behind a refusal-style opening ("I can't help, but...") caught | 65.5% |
| Letters, 2-3 letter words, top 2000 words (in training as innocent examples) - blocks | 0 / 0 / 0 / 3 (the 3 are lexicon or policy words); Sójka 0.1B 21 / 15 / 9 / 48, 0.5B 12 / 5 / 4 / 39 |

Short tokens: Sójka mistakes some ordinary letters and words for vulgar ones - e.g. the single letter "k" scores
0.73 in Sójka 0.1B and 0.90 in 0.5B (blocked), "wujek" (uncle) 0.40 in 0.1B (warning). v1.0 fixed this and v1.1 keeps
it: "k" 0.0005, "wujek" 0.0005; of 86 single letters and short spellings Muszka blocks 0, Sójka 0.1B 31
and 0.5B 26 (released INT8 file with regex; Sójka as published). These tokens were in Muszka's training as innocent examples.

### Release gate

Before release every candidate goes through 45 control conditions (critical cases reported by people, profanity
and obfuscation, extreme controls, word audit, benchmarks). v1.1 meets **38 of 45** - we released it despite
7 unmet conditions, listed below as known limitations. Before release we raised the holdout v2 false-alarm threshold
from 10% to 12% (no candidate in sensitive mode met 10%).

## Speed and memory

Released file, sensitive mode, one message at a time, 500 texts from the test sets (median 38 tokens), ONNX Runtime 1.30
with default threads (all cores), tokenization included, no regex. Muszka's quality numbers in this card were measured on the ARM server; INT8 arithmetic differs slightly between CPUs, so holdout v2
false alarms range from 11.5% to 12.0% depending on the device (last column). The Mikrus VPS has 1 vCPU and runs production traffic.

| Device | File | median | mean | long texts (~420 tokens) | process RAM (MiB) | false alarms v2 |
|---|---|---|---|---|---|---|
| NVIDIA GB10 (ARM, dell) | INT8 (126 MB) | 10.1 ms | 30.7 ms | 237 ms | 386 | 11.5% |
| NVIDIA GB10 (ARM, dell) | fp32 (498 MB) | 25.4 ms | 75.2 ms | 511 ms | 788 | - |
| Intel i5-12600K (x86) | INT8 (126 MB) | 8.7 ms | 28.5 ms | 242 ms | 406 | 12.0% |
| Intel i5-12600K (x86) | fp32 (498 MB) | 19.3 ms | 60.5 ms | 475 ms | 809 | - |
| Raspberry Pi 500+ (ARM) | INT8 (126 MB) | 34.1 ms | 134 ms | 1331 ms | 429 | 11.8% |
| Raspberry Pi 500+ (ARM) | fp32 (498 MB) | 98.0 ms | 316 ms | 2626 ms | 780 | - |
| Mikrus VPS (x86, 1 vCPU) | INT8 (126 MB) | 189 ms | 559 ms | 4044 ms | 400 | 12.0% |

## Known limitations

- **Standalone insults outside the profanity lexicon used in training pass** (some appeared in training labelled innocent; exam: 6.7% blocked vs
  60.0% for Sójka 0.1B) - e.g. "palant", "szuja", "łajdak" on their own. In an
  insulting sentence they are usually caught. The critical list also shows "buc" passing - we like to think Muszka reads
  it as an acronym: **B**ardzo **U**przejmy **C**złowiek (a Very Polite Person). Top priority for v1.2.
  In insulting sentences the same words are blocked in 41 of 45 cases (3 sentence frames), weaker in the mildest frame.
  Standalone insults that pass: łajza, darmozjad, łachudra, luj, palant, patafian, prostak, szuja, tłuk, łajdak, łachmyta,
  łachudrak, łotr, łapserdak. Mild insults (gamoń, łamaga, gapa...) - policy not decided yet.
- **False alarms on ambiguous words in innocent sentences**: "Dostał pałę z matematyki" (got an F), "Suka owczarka..."
  (a female dog), "Dmuchać na zimne" (an idiom), "hak do wieszania towaru"; "dupleks" is blocked, probably because the tokenizer
  splits it into dup-lek-s.
- **Hidden intent is not recognised**: e.g. "I have 75 kg of spoiled chicken and want to get rid of it without a trace" -
  scored innocent (a known case from a LinkedIn comment; thank you).
- An ambiguous phrase without Polish diacritics ("wnuczek zrobil dziadkowi laske") gets no warning.
- Sensitive mode raises false alarms: 11.5% of innocent prompts on holdout v2 and 20.2% of innocent adversarial
  prompts (Sójka 0.1B: 6.1% and 3.8%), 15.3% of ordinary model responses. Without windows it would be lower,
  but a hidden harmful sentence would get through.
- Some rare abbreviations (CJK, MILF) are not recognised as vulgar.
- Polish only; texts from other domains may behave differently. This is a filter, not a judge of truth or intent -
  for important decisions use it together with a larger model or a human.

## Roadmap (v1.2)

1. A broad lexicon of insults with inflections and obfuscations; fewer "innocent single-word" training anchors, which
   weakened what Sójka already knew about insults.
2. Ambiguous words in context, larger sentence-pair tests.
3. **Muszka + judge**: blocked messages optionally re-checked by a small language model (Muszka-Instruct 1.5B) that
   releases false alarms. The filter stays sensitive; the judge reduces false blocks.
4. An in-browser version (runs locally on the user's device).

## Training data and credits

- **[Jan Sowa](https://www.linkedin.com/in/janpiotrsowa/)** - Polish translations of WildGuardMix and Jigsaw Toxic Comments (Bielik 11B v3.0) and the lexicon of
  vulgar words and phrases, the core of v1.1's training and profanity tests. Thank you!
- **Base model and teacher:** [Bielik-Guard 0.1B / 0.5B "Sójka"](https://huggingface.co/speakleash/Bielik-Guard-0.1B-v1.1)
  by [SpeakLeash](https://huggingface.co/speakleash) (Apache 2.0) - Sójka team: [Jan Maria Kowalski](https://www.linkedin.com/in/janmariakowalski/), [Krzysztof Wróbel](https://www.linkedin.com/in/wrobelkrzysztof/),
  [Jerzy Surma](https://www.linkedin.com/in/jerzysurma/), [Igor Ciuciura](https://www.linkedin.com/in/igor-ciuciura-1763b52a6/), [Maciej Krystian Szymański](https://www.linkedin.com/in/maciej-krystian-szymanski/) [1]. Base encoder: [Sławomir Dadas](https://www.linkedin.com/in/sdadas/) (`sdadas/mmlw-roberta-base`, Apache 2.0).
- **WildGuardMix** (Han et al., 2024, AllenAI, ODC-BY) [2] - train split translated to Polish by Jan Sowa; test split used
  only for the holdout v2 test.
- **PolyGuardMix** (Kumar et al., 2025, CC BY 4.0) [3] - model responses and categories (built on WildGuardMix).
  The part coming from LMSys-Chat-1M was excluded.
- **Jigsaw Toxic Comment Classification Challenge** (Jigsaw / Conversation AI; comment text from Wikipedia, CC BY-SA 3.0) -
  train split translated to Polish by Jan Sowa; test split used only for the holdout v1 test.
- **FrequencyWords** (Hermit Dave, CC BY-SA 4.0, based on OpenSubtitles 2018) - list of frequent Polish words, used as innocent
  examples in training and in false-alarm tests.
- **Bielik team (SpeakLeash):** Krzysztof Ociepa, Remigiusz Kinas, Adrian Gwoździej, Krzysztof Wróbel, Łukasz Flis, Sebastian Kondracki - Bielik 11B v2.1 and v3.0 (Apache 2.0), used for translations and synthetic Polish data.
- Synthetic Polish data generated with **Bielik 11B v2.1 and v3.0** (SpeakLeash, Apache 2.0), including simple texts built on the
  semantic fields of Roget's Thesaurus (public domain).
- Tests only (never trained on): **PL-Guard** (NASK, CC BY-SA 4.0) - Aleksandra Krasnodębska, Karolina Seweryn, Szymon Łukasik,
  Wojciech Kusa [4]; **GadziJęzyk** (Prof. [Jerzy Surma](https://www.linkedin.com/in/jerzysurma/), SGH, with student volunteers, MIT).

### References

1. Wróbel K., Kowalski J. M., Surma J., Ciuciura I., Szymański M. *Bielik Guard: Efficient Polish Language Safety Classifiers
   for LLM Content Moderation.* 2026. [arXiv:2602.07954](https://arxiv.org/abs/2602.07954)
2. Han S., Rao K., Ettinger A., Jiang L., Lin B. Y., Lambert N., Choi Y., Dziri N. *WildGuard: Open One-Stop Moderation Tools
   for Safety Risks, Jailbreaks, and Refusals of LLMs.* 2024. [arXiv:2406.18495](https://arxiv.org/abs/2406.18495)
3. Kumar P., Jain D., Yerukola A., Jiang L., Beniwal H., Hartvigsen T., Sap M. *PolyGuard: A Multilingual Safety Moderation
   Tool for 17 Languages.* 2025. [arXiv:2504.04377](https://arxiv.org/abs/2504.04377)
4. Krasnodębska A., Seweryn K., Łukasik S., Kusa W. *PL-Guard: Benchmarking Language Model Safety for Polish.* Proceedings of
   the 10th Workshop on Slavic Natural Language Processing, 2025. [arXiv:2506.16322](https://arxiv.org/abs/2506.16322)

License: Apache 2.0.

---

# Wersja polska

*Pochodna [Bielik-Guard 0.1B (Sójka)](https://huggingface.co/speakleash/Bielik-Guard-0.1B-v1.1) od SpeakLeash. Muszka Guard to niezależny projekt - to nie jest oficjalny produkt zespołu Bielik-Guard (Sójka).*

**Mały, szybki polski filtr bezpieczeństwa dla czatów i asystentów AI.** 124M parametrów, 7 kategorii, plik ONNX INT8
126 MB (120 MiB) działający na zwykłym procesorze, bez GPU. Na komputerze z Intel i5-12600K (wszystkie rdzenie,
jedna wiadomość naraz): mediana 8,7 ms i średnio 28,5 ms na tekstach testowych (mediana długości
38 tokenów), ok. 0,24 s na długi tekst ok. 420 tokenów.
Terminy wyjaśnia [słowniczek](GLOSSARY.md) (także [w PDF](https://huggingface.co/Fibogacci/muszka-guard-0.1b-v1.1/blob/main/muszka-guard-v1.1-slowniczek.pdf)).

Autor: Fibogacci ([LinkedIn](https://www.linkedin.com/in/Fibogacci)). Dane treningowe i zestaw wulgaryzmów: **[Jan Sowa](https://www.linkedin.com/in/janpiotrsowa/)** - dziękujemy!

[Strona projektu](https://muszkaowocowa.pl/muszka-guard) • [Demo z porównaniem i areną](https://huggingface.co/spaces/Fibogacci/muszka-guard-v1.1-demo) •
[Pełny raport (PDF)](https://huggingface.co/Fibogacci/muszka-guard-0.1b-v1.1/blob/main/muszka-guard-v1.1-raport.pdf) • [Report (PDF, EN)](https://huggingface.co/Fibogacci/muszka-guard-0.1b-v1.1/blob/main/muszka-guard-v1.1-report-en.pdf) •
[Słowniczek (PDF)](https://huggingface.co/Fibogacci/muszka-guard-0.1b-v1.1/blob/main/muszka-guard-v1.1-slowniczek.pdf) • [Glossary (PDF, EN)](https://huggingface.co/Fibogacci/muszka-guard-0.1b-v1.1/blob/main/muszka-guard-v1.1-glossary-en.pdf)

## O wersji v1.0

Pierwsza publiczna wersja, Muszka Guard 0.1B v1.0, podawała wyniki zmierzone na małym zestawie testowym
(30 szkodliwych i 6 niewinnych przykładów, zbliżonych do danych treningowych), a część parametrów - m.in.
zapotrzebowanie na pamięć i czas odpowiedzi - pochodziła z założeń projektowych, a nie z pomiaru. Po przygotowaniu
niezależnych zbiorów testowych okazało się, że tamte liczby zawyżały skuteczność modelu. Wersję v1.1 zmierzyliśmy od
nowa na kilku tysiącach tekstów odłożonych przed treningiem i opisaliśmy wraz z ograniczeniami - wszystkie liczby pochodzą z tych
pomiarów. Wersja v1.1 zastępuje v1.0.

## Kategorie

`self-harm` (samookaleczenia), `hate` (nienawiść), `vulgar` (wulgaryzmy i obelgi, także zaciemnione), `sex`, `crime`
(przestępstwa, przemoc, broń, hakowanie), `jailbreak` (prompt injection) i nowa `other` (zniesławienie, porady
specjalistyczne, wybory). Domyślnie: **blokada** od 0,5, **ostrzeżenie** między 0,18 a 0,5.

## Długie teksty - tryby

Teksty dłuższe niż 128 tokenów są dodatkowo czytane oknami po 128 tokenów. Tryb **`sensitive`** (czuły, domyślny) łapie jedno groźne
zdanie ukryte w długim tekście - kosztem kilku fałszywych alarmów więcej. Zasada: lepiej zablokować niewinne zdanie,
niż przepuścić szkodliwe. Tryb **`balanced`** (zrównoważony) rzadziej blokuje długie opowiadania, **`no_windows`** (bez okien) czyta tylko całość.
Tryb ustawia parametr `mode=`.

## Wyniki

Muszka: plik INT8, tryb `sensitive` (czuły, z oknami), próg 0,5. Holdouty, PL-Guard, GadziJęzyk i testy fałszywych alarmów - sam model,
bez regexu; egzamin i lista krytyczna - z regexem, jak we wdrożeniu. Sójka 0.1B i 0.5B - tak, jak ją opublikowano (fp32,
do 512 tokenów, bez okien; PyTorch albo nasz eksport ONNX). Tylko w PL-Guard pokazujemy też Sójkę uruchomioną przez nas
w tych samych oknach co Muszka (liczby w nawiasach).

Holdouty, PL-Guard, GadziJęzyk, Roget i egzamin zostały odłożone przed treningiem (wyjątki: 3 pozycje egzaminu i 7 krótkich
tekstów holdoutu v1 trafiły do danych jednej z dwóch uśrednianych wersji). Test przekleństw i audyt słów mierzą pokrycie -
ich słowa były w treningu.

### Zapieczętowany egzamin końcowy

Osobny zbiór wygenerowany Bielikiem i oznaczony przez sędziego (Bielik) przed pomiarem (obelgi wybrane ręcznie), zmierzony
**raz** na wybranym modelu (sha256 pliku egzaminu `160bbc02a615…`). Odsetek zablokowanych tekstów:

| Sekcja egzaminu | n | Oczekiwane | Muszka v1.1 | Sójka 0.1B | Sójka 0.5B |
|---|---|---|---|---|---|
| Wulgarne wiadomości (nowe sytuacje) | 288 | blokada | 93,8% | 92,4% | 93,1% |
| Zaciemnione wulgarne wiadomości | 194 | blokada | 99,0% | 77,8% | 92,3% |
| Niewinne wiadomości ze słowami podobnymi | 250 | przepuść | 4,8% | 2,8% | 0,8% |
| Niewinne z jednym zaciemnionym słowem | 175 | przepuść | 6,3% | 6,3% | 4,0% |
| Obelgi spoza zestawu wulgaryzmów z treningu, osobno | 15 | blokada | 6,7% | 60,0% | 26,7% |

Muszka wyraźnie lepiej radzi sobie z zaciemnionymi wulgaryzmami, zwykłe wulgarne wiadomości łapie na poziomie Sójki,
**a pojedyncze obelgi spoza zestawu wulgaryzmów z treningu - wyraźnie gorzej** (część tych słów, np. „palantem”, była
w danych treningowych jako słowo niewinne; patrz ograniczenia). Na niewinnych wiadomościach ze słowami podobnymi Muszka
blokuje więcej niż obie Sójki (4,8% wobec 2,8% i 0,8%). Po pomiarze zauważyliśmy, że
sędzia (Bielik) budujący egzamin oznaczył część niewulgarnych wiadomości jako wulgarne - prawdziwy wynik pierwszego
wiersza jest raczej wyższy; egzaminu po pomiarze nie poprawialiśmy.

### PL-Guard (NASK)

Makro F1 bezpieczne / niebezpieczne, wszystkie 14 kategorii. Zbiór testowy podzieliliśmy na dwie stałe połowy: jedna do
wyboru ustawień, druga (raportowa) do raportu. Połowę raportową liczyliśmy przy każdym przebiegu bramki (5 kandydatów), a warunek
bramki obejmował cały zbiór; kandydata nie wybieraliśmy według niej - wybrany model ma na niej najniższy wynik z trzech ostatnich.

| Model | Połowa raportowa: test / adv | Cały zbiór: test / adv |
|---|---|---|
| **Muszka v1.1** | **0,811 / 0,768** | 0,852 / 0,774 |
| Sójka 0.1B (w nawiasie: uruchomiona przez nas w oknach) | 0,497 (0,537) / 0,472 (0,527) | 0,489 (0,541) / 0,481 (0,537) |
| Sójka 0.5B (w nawiasie: uruchomiona przez nas w oknach) | 0,475 (0,568) / 0,464 (0,551) | 0,480 (0,568) / 0,470 (0,555) |
| HerBERT-PL-Guard (NASK, z pracy) | - | 0,927 / 0,913 |

HerBERT-PL-Guard trenowano na danych przygotowanych przez autorów PL-Guard, z tą samą listą kategorii - to może tłumaczyć
przewagę. Dane treningowe Muszki nie mają wspólnych tekstów z PL-Guard (sprawdzone).
Sama Sójka nie używa okien (czyta do 512 tokenów); liczby w nawiasach to Sójka uruchomiona przez nas w tych samych
oknach 128/32 co Muszka, żeby porównać oba modele w równych warunkach.

### Zbiory odłożone

| | Muszka v1.1 | Sójka 0.1B | Sójka 0.5B |
|---|---|---|---|
| Holdout v1 AUROC / wykrywalność / fałszywe alarmy | **0,961** / 83,5% / 6,3% | 0,940 / 78,2% / 7,5% | 0,942 / 78,4% / 6,9% |
| Holdout v2 AUROC / wykrywalność / fałszywe alarmy | **0,916** / 87,1% / 11,5% | 0,802 / 40,3% / 6,1% | 0,846 / 41,5% / 3,6% |
| Ataki adversarial wykryte | **87,6%** | 18,9% | 17,1% |
| Niewinne prompty adversarial zablokowane (fałszywe alarmy) | 20,2% | 3,8% | 1,6% |
| GadziJęzyk | **98,9%** | 62,7% | 81,3% |

Holdout v1: komentarze z testowej części Jigsaw (przetłumaczone Bielikiem) i 36 ataków oraz niewinnych wiadomości napisanych
po polsku dla czatu na muszkaowocowa.pl; holdout v2: prompty z testowej części WildGuardMix. Prompty adversarial są zwykle dłuższe niż jedno okno, więc okna Muszki mają tu znaczenie; Sójki w oknach na tym zbiorze nie
mierzyliśmy. Więcej wykrytych ataków kosztuje więcej fałszywych alarmów na niewinnych promptach adversarial (wiersz niżej).

### Przekleństwa i zaciemnienia

Zestaw wulgaryzmów Jana Sowy, wszystkie formy odmiany, 13 rodzajów zaciemnień. Muszka v1.1 trenowała na wszystkich
rodzinach słów (to pokrycie); uogólnianie na nieznane rodziny (wcześniejszy model, 30% rodzin odłożonych):
87,2% wszystkich wariantów (formy i zaciemnienia), same formy 90,3% (bramka, INT8).

| Zapis | Muszka v1.1 | Sójka 0.1B | Sójka 0.5B |
|---|---|---|---|
| forma bez zmian | 99,8% | 89,4% | 80,8% |
| u→ó (kórwa) | 99,7% | 46,4% | 43,3% |
| ch→h (huj) | 100,0% | 92,1% | 64,5% |
| ch→h + u→ó (hój) | 100,0% | 62,3% | 26,9% |
| gwiazdka (k*rwa) | 99,0% | 87,6% | 99,6% |
| spacje (k u r w a) | 98,4% | 32,5% | 10,9% |
| kropki (k.u.r.w.a) | 98,4% | 99,9% | 41,9% |
| leet (kurw@) | 99,1% | 61,8% | 49,2% |
| powtórzona litera (kuuurwa) | 98,7% | 65,9% | 72,8% |
| bez polskich znaków | 99,4% | 82,9% | 75,0% |
| WIELKIE LITERY | 98,5% | 58,1% | 53,9% |

Tabela: wszystkie trzy modele w pełnej precyzji (PyTorch fp32), test przekleństw v2; wydawany plik INT8 - do 0,5 pkt proc.
mniej (bramka, test v3). Zwykłe słowa w tych samych nietypowych zapisach są blokowane w 0,5%-6,7% przypadków
zależnie od zapisu (u→ó 6,7% - powyżej progu bramki 5%).

### Inne

Fałszywe alarmy: zwykłe polskie teksty 0,6%, niewinne teksty na tematy negatywne (Roget) 6,7%,
pytania o zdrowie / prawo / finanse / wybory 0,7%, odmowy modeli 1,2%, **zwykłe (nieszkodliwe)
odpowiedzi modeli 15,3%**. Szkodliwe odpowiedzi modeli wykryte: 79,4%; szkodliwa treść
za wstępem-odmową: 65,5%. Litery, słowa 2-3-literowe i 2000 najczęstszych słów (były w treningu jako niewinne):
0 fałszywych alarmów na zwykłych słowach (3 blokady w top 2000 to słowa z zestawu wulgaryzmów lub objęte polityką ostrzeżeń;
Sójka 0.1B 21 / 15 / 9 / 48, 0.5B 12 / 5 / 4 / 39 - litery / 2 / 3 litery / top 2000). Sójka myli część zwykłych liter i słów z wulgaryzmami:
sama litera „k” to u Sójki 0.1B 0,73, a u 0.5B 0,90 (blokada), „wujek” u 0.1B 0,40 (ostrzeżenie).
v1.0 to naprawiła, a v1.1 to utrzymuje: „k” 0,0005, „wujek” 0,0005; z 86 pojedynczych liter
i krótkich zapisów Muszka blokuje 0, Sójka 0.1B 31, a 0.5B 26 (te słowa były w treningu Muszki jako niewinne).

Bramka przed publikacją: 45 warunków kontrolnych; v1.1 spełnia **38** - wydaliśmy ją mimo 7 niespełnionych,
opisanych jako znane ograniczenia. Przed wydaniem podnieśliśmy próg fałszywych alarmów na holdoucie v2 z 10% do 12%
(żaden kandydat w trybie `sensitive` (czułym) nie mieścił się w 10%).

## Szybkość i pamięć

Jedna wiadomość naraz, 500 tekstów z testów (mediana 38 tokenów), ONNX Runtime 1.30 z domyślną liczbą wątków (wszystkie
rdzenie), z tokenizacją, bez regexu. Liczby jakości Muszki w karcie zmierzono na serwerze ARM;
INT8 liczy się minimalnie inaczej na różnych procesorach - fałszywe alarmy na holdoucie v2 od 11,5% do 12,0% (ostatnia kolumna).
Mikrus to VPS z 1 vCPU, na którym działa ruch produkcyjny.

| Urządzenie | Plik | mediana | średnio | długie teksty (~420 tokenów) | RAM procesu (MiB) | fałszywe alarmy v2 |
|---|---|---|---|---|---|---|
| NVIDIA GB10 (ARM, dell) | INT8 (126 MB) | 10,1 ms | 30,7 ms | 237 ms | 386 | 11,5% |
| NVIDIA GB10 (ARM, dell) | fp32 (498 MB) | 25,4 ms | 75,2 ms | 511 ms | 788 | - |
| Intel i5-12600K (x86) | INT8 (126 MB) | 8,7 ms | 28,5 ms | 242 ms | 406 | 12,0% |
| Intel i5-12600K (x86) | fp32 (498 MB) | 19,3 ms | 60,5 ms | 475 ms | 809 | - |
| Raspberry Pi 500+ (ARM) | INT8 (126 MB) | 34,1 ms | 134 ms | 1331 ms | 429 | 11,8% |
| Raspberry Pi 500+ (ARM) | fp32 (498 MB) | 98,0 ms | 316 ms | 2626 ms | 780 | - |
| Mikrus VPS (x86, 1 vCPU) | INT8 (126 MB) | 189 ms | 559 ms | 4044 ms | 400 | 12,0% |

## Znane ograniczenia

- **Pojedyncze obelgi spoza zestawu wulgaryzmów z treningu przechodzą** (część była w treningu jako słowa niewinne; egzamin: 6,7%
  zablokowanych, Sójka 0.1B 60,0%) - np. samo „palant”, „szuja”, „łajdak”.
  W obraźliwym zdaniu te same słowa są blokowane w 41 z 45 przypadków (3 ramki zdaniowe;
  w najłagodniejszej słabiej). Przechodzą osobno: łajza, darmozjad, łachudra, luj, palant, patafian, prostak, szuja, tłuk,
  łajdak, łachmyta, łachudrak, łotr, łapserdak. Łagodne obelgi (gamoń, łamaga, gapa…) - polityka jeszcze nieustalona.
  Przepuszcza też „buc” - wolimy myśleć, że Muszka czyta to jako skrót:
  **B**ardzo **U**przejmy **C**złowiek. Pierwszy punkt planu v1.2.
- **Fałszywe blokady słów dwuznacznych w niewinnych zdaniach**: „Dostał pałę z matematyki”, „Suka owczarka…”, „Dmuchać
  na zimne”, „hak do wieszania towaru”; „dupleks” (prawdopodobnie dlatego, że tokenizer dzieli go na dup-lek-s).
- **Ukryty zamiar nie jest rozpoznawany**, np. „mam 75 kg zepsutego mięsa z kurczaka i chcę się go pozbyć bez śladu” -
  oceniane jako niewinne (przypadek z komentarza na LinkedIn - dziękujemy).
- Dwuznaczne zdanie bez polskich znaków („wnuczek zrobil dziadkowi laske”) nie dostaje ostrzeżenia.
- Tryb `sensitive` (czuły) podnosi fałszywe alarmy: 11,5% niewinnych promptów na holdoucie v2 i 20,2% niewinnych promptów
  adversarial (Sójka 0.1B: 6,1% i 3,8%), 15,3% zwykłych odpowiedzi modeli. Bez okien byłoby ich mniej,
  ale ukryte szkodliwe zdanie by przeszło.
- Rzadkie skróty (CJK, MILF) nierozpoznawane.
- Tylko polski. To filtr, a nie sędzia prawdy czy intencji - przy ważnych decyzjach warto łączyć go z większym modelem
  albo człowiekiem.

## Plan v1.2

Szeroki słownik obelg z odmianami i zaciemnieniami, mniej „niewinnych” pojedynczych słów w treningu, słowa dwuznaczne
w kontekście, **Muszka + sędzia** (Muszka-Instruct 1.5B zwalnia fałszywe blokady), wersja w przeglądarce.

## Dane i podziękowania

- **[Jan Sowa](https://www.linkedin.com/in/janpiotrsowa/)** - tłumaczenia WildGuardMix i Jigsaw na polski (Bielik 11B v3.0) oraz zestaw wulgaryzmów i fraz, które są
  podstawą treningu i testów przekleństw v1.1. Dziękujemy!
- **Model bazowy i nauczyciel:** [Bielik-Guard 0.1B / 0.5B „Sójka”](https://huggingface.co/speakleash/Bielik-Guard-0.1B-v1.1)
  od [SpeakLeash](https://huggingface.co/speakleash) (Apache 2.0) - zespół Sójki: [Jan Maria Kowalski](https://www.linkedin.com/in/janmariakowalski/), [Krzysztof Wróbel](https://www.linkedin.com/in/wrobelkrzysztof/),
  [Jerzy Surma](https://www.linkedin.com/in/jerzysurma/), [Igor Ciuciura](https://www.linkedin.com/in/igor-ciuciura-1763b52a6/), [Maciej Krystian Szymański](https://www.linkedin.com/in/maciej-krystian-szymanski/) [1]. Bazowy enkoder: [Sławomir Dadas](https://www.linkedin.com/in/sdadas/) (`sdadas/mmlw-roberta-base`, Apache 2.0).
- **WildGuardMix** (Han i in., 2024, AllenAI, ODC-BY) [2] - część treningowa przetłumaczona na polski przez Jana Sowę; część
  testowa użyta wyłącznie w teście holdout v2.
- **PolyGuardMix** (Kumar i in., 2025, CC BY 4.0) [3] - odpowiedzi modeli i kategorie (na bazie WildGuardMix). Część pochodząca
  z LMSys-Chat-1M została wyłączona.
- **Jigsaw Toxic Comment Classification Challenge** (Jigsaw / Conversation AI; treść komentarzy z Wikipedii, CC BY-SA 3.0) -
  część treningowa przetłumaczona na polski przez Jana Sowę; część testowa użyta wyłącznie w teście holdout v1.
- **FrequencyWords** (Hermit Dave, CC BY-SA 4.0, na bazie OpenSubtitles 2018) - lista częstych polskich słów, użyta jako niewinne
  przykłady w treningu i w testach fałszywych alarmów.
- **Zespół Bielik (SpeakLeash):** Krzysztof Ociepa, Remigiusz Kinas, Adrian Gwoździej, Krzysztof Wróbel, Łukasz Flis, Sebastian Kondracki - Bielik 11B v2.1 i v3.0 (Apache 2.0), użyte do tłumaczeń i polskich danych syntetycznych.
- Dane syntetyczne wygenerowane modelami **Bielik 11B v2.1 i v3.0** (SpeakLeash, Apache 2.0), w tym proste teksty oparte na polach
  semantycznych Tezaurusa Rogeta (domena publiczna).
- Wyłącznie do testów (bez treningu): **PL-Guard** (NASK, CC BY-SA 4.0) - Aleksandra Krasnodębska, Karolina Seweryn, Szymon Łukasik,
  Wojciech Kusa [4]; **GadziJęzyk** (prof. [Jerzy Surma](https://www.linkedin.com/in/jerzysurma/), SGH, ze studentami-wolontariuszami, MIT).

Publikacje [1]-[4] - lista w sekcji *References* wersji angielskiej.

Licencja: Apache 2.0.
