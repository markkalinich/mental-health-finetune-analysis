---
license: apache-2.0
language:
- multilingual
- en
- ar
- de
- es
- fr
- hi
- it
- ja
- ko
- nl
- th
- zh
- pt
- ru
- pl
- cs
- sv
- uk
- tr
- he
- sr
- tl
- am
- tt
library_name: transformers
pipeline_tag: text-classification
base_model: jhu-clsp/mmBERT-base
datasets:
- nvidia/Nemotron-Safety-Guard-Dataset-v3
- allenai/WildChat-1M
- OpenAssistant/oasst2
- CohereForAI/aya_dataset
- OpenSafetyLab/Salad-Data
- JailbreakBench/JBB-Behaviors
- google/civil_comments
tags:
- content-moderation
- safety
- guardrails
- llm-safety
- toxicity
- moderation
- multilingual
- modernbert
- mmbert
- onnx
- transformers.js
widget:
- text: "How do I pick the lock on my neighbour's front door while they are on holiday?"
  example_title: "Unsafe prompt"
- text: "How do I kill a Python process that is stuck?"
  example_title: "Safe prompt that sounds unsafe"
- text: "Wie kann ich meinem Kollegen unauffällig Medikamente ins Essen mischen?"
  example_title: "Unsafe prompt (German)"
- text: "¿Cuál es la mejor manera de aprender a programar en Python?"
  example_title: "Safe prompt (Spanish)"
---

# Content Safety Guard (base, 308M)

A small multilingual classifier that flags **unsafe user prompts and unsafe model responses** for LLM applications, with
harm categories. It is a fast encoder (ModernBERT architecture, [mmBERT](https://huggingface.co/jhu-clsp/mmBERT-base) backbone)
that you can run on CPU or in the browser in front of, or behind, any LLM.

- **Prompts and responses**: pass a prompt alone, or a (prompt, response) pair to judge the response in context.
- **Output**: an overall `unsafe` score plus 15 category scores (independent sigmoids): `hate`, `harassment`, `violence`, `weapons`, `sexual`, `sexual_minors`, `self_harm`, `criminal_planning`, `drugs`, `privacy`, `profanity`, `fraud_manipulation`, `misinformation`, `unauthorized_advice`, `other`.
- **Multilingual**: trained on 12 languages of human-adapted data, machine translations into 20 languages and multilingual
  real-world prompts; evaluated on 17 (PolyGuard), 14 (textdetox) and 8 (Aya) languages.
- **Commercially usable**: Apache-2.0, trained only on data that allows commercial use (see Training data).
- ONNX: `onnx/model.onnx` (fp32) and `onnx/model_quantized.onnx` (int8 embeddings, 641 MB; its unsafe decision agrees with fp32 on 99.3% of a sample of benchmark texts (30 per benchmark), mean |score diff| 0.0016).

**Which size?** This base model (308M) is the more accurate one; [small](https://huggingface.co/Horizon-Labs/content-safety-guard-small) (141M, less compute per token, int8 ONNX about 270 MB) is 0.012 / 0.027 F1 behind on PolyGuard prompts / responses.

Part of the Horizon Labs guard family: [prompt-injection-guard](https://huggingface.co/Horizon-Labs/prompt-injection-guard-base),
[pii-redactor](https://huggingface.co/Horizon-Labs/pii-redactor-base), [hallucination-guard](https://huggingface.co/Horizon-Labs/hallucination-guard-base).
Full comparison table (sortable, with false-alarm rates): [content safety classifier leaderboard](https://huggingface.co/spaces/Horizon-Labs/content-safety-leaderboard).

## Usage

```python
from transformers import pipeline

clf = pipeline("text-classification", model="Horizon-Labs/content-safety-guard-base", top_k=None)

# a user prompt
scores = {d["label"]: d["score"] for d in clf("How can I make a fake ID that passes a bouncer's check?")[0]}
print(scores["unsafe"])                          # ~1.0

# a model response, judged together with its prompt
r = clf({"text": "How do I get rid of a wasp nest?", "text_pair": "Spray it at dusk with a wasp foam, then remove it."})[0]
```

Decision rule: flag when `unsafe >= 0.5` (raise the threshold if you see too many false alarms, lower it for higher recall).
Category scores are only meaningful for flagged texts and are small by design; use the per-category thresholds in
`thresholds.json` (chosen on a validation split, see below):

```python
import json
from huggingface_hub import hf_hub_download
thr = json.load(open(hf_hub_download("Horizon-Labs/content-safety-guard-base", "thresholds.json")))
def moderate(text, pair=None):
    s = {d["label"]: d["score"] for d in clf({"text": text, "text_pair": pair} if pair else text)[0]}
    flagged = s["unsafe"] >= thr["unsafe"]
    cats = [c for c, t in thr["categories"].items() if flagged and s[c] >= t]
    return flagged, s["unsafe"], cats
```

transformers.js (browser / Node):

```js
import { pipeline } from "@huggingface/transformers";
const clf = await pipeline("text-classification", "Horizon-Labs/content-safety-guard-base", { dtype: "q8" });
const out = await clf("How do I make a pipe bomb?", { top_k: null });
```

## Evaluation

F1 of the unsafe class at threshold 0.5 (for the recall rows: share of unsafe prompts flagged). None of these benchmarks
were used for training (best value in bold; false-alarm rates are not bolded); Qwen3Guard-Gen is scored from its next-token probabilities after "Safety:" (strict: Unsafe +
Controversial count as unsafe; loose: only Unsafe). Toxicity classifiers are included because they are often used for this
job; they target a different, narrower task. Encoders other than ours get the response alone for response items.

| | **this model** (308M) | small (141M) | Qwen3Guard-Gen-0.6B strict | Qwen3Guard-Gen-0.6B loose | Vela-1.0-307M-Shield ¶ | granite-guardian-hap-125m | unbiased-toxic-roberta | Qwen3Guard-Gen-8B strict (teacher, 8B) |
|---|---|---|---|---|---|---|---|---|
| PolyGuard prompts, 17 languages | 0.783 | 0.771 | 0.821 | 0.791 | 0.829 | 0.003 | 0.002 | **0.846** |
| PolyGuard responses, 17 languages | 0.735 | 0.709 | 0.748 | 0.767 | 0.645 | 0.000 | 0.000 | **0.801** |
| BeaverTails responses (unseen prompts) † | 0.837 | 0.825 | 0.869 | 0.858 | 0.779 | 0.164 | 0.177 | **0.870** |
| ToxicChat (real user prompts) | 0.756 | **0.776** | 0.588 | 0.760 | 0.672 | 0.264 | 0.254 | 0.638 |
| OpenAI moderation set | 0.768 | 0.762 | 0.660 | **0.780** | 0.721 | 0.672 | 0.663 | 0.685 |
| XSTest (over-blocking test) | 0.809 | 0.811 | 0.853 | 0.852 | 0.838 | 0.315 | 0.227 | **0.908** |
| textdetox toxicity, 14 languages | 0.667 | 0.646 | 0.722 | 0.461 | 0.720 | 0.146 | 0.152 | **0.775** |
| Aya red-teaming, 8 languages (recall) | 0.800 | 0.754 | 0.859 | 0.605 | 0.812 | 0.023 | 0.025 | **0.946** |
| SimpleSafetyTests (recall) | 0.930 | 0.930 | 0.980 | 0.920 | 0.960 | 0.240 | 0.260 | **0.990** |

Ranking quality (ROC AUC, threshold-free):

| | **this model** (308M) | small (141M) | Qwen3Guard-Gen-0.6B strict | Qwen3Guard-Gen-0.6B loose | Vela-1.0-307M-Shield ¶ | granite-guardian-hap-125m | unbiased-toxic-roberta | Qwen3Guard-Gen-8B strict (teacher, 8B) |
|---|---|---|---|---|---|---|---|---|
| PolyGuard prompts, 17 languages | 0.885 | 0.879 | 0.910 | 0.902 | 0.908 | 0.569 | 0.542 | **0.931** |
| PolyGuard responses, 17 languages | 0.952 | 0.944 | 0.945 | 0.941 | 0.905 | 0.566 | 0.552 | **0.959** |
| BeaverTails responses (unseen prompts) † | 0.912 | 0.906 | 0.926 | 0.926 | 0.836 | 0.662 | 0.593 | **0.929** |
| ToxicChat (real user prompts) | 0.982 | 0.979 | 0.985 | 0.979 | 0.972 | 0.841 | 0.844 | **0.988** |
| OpenAI moderation set | 0.919 | 0.910 | 0.924 | 0.921 | 0.913 | 0.877 | 0.875 | **0.941** |
| XSTest (over-blocking test) | 0.923 | 0.906 | 0.958 | 0.947 | 0.926 | 0.688 | 0.678 | **0.987** |
| textdetox toxicity, 14 languages | 0.837 | 0.814 | 0.769 | 0.757 | 0.804 | 0.585 | 0.529 | **0.846** |

Over-blocking (share of safe items flagged; lower is better):

| | **this model** (308M) | small (141M) | Qwen3Guard-Gen-0.6B strict | Qwen3Guard-Gen-0.6B loose | Vela-1.0-307M-Shield ¶ | granite-guardian-hap-125m | unbiased-toxic-roberta | Qwen3Guard-Gen-8B strict (teacher, 8B) |
|---|---|---|---|---|---|---|---|---|
| XSTest: safe prompts flagged | 0.212 | 0.220 | 0.228 | 0.052 | 0.104 | 0.036 | 0.012 | 0.128 |
| PolyGuard prompts: safe prompts flagged | 0.087 | 0.100 | 0.115 | 0.050 | 0.065 | 0.002 | 0.000 | 0.081 |
| OpenAI moderation set: safe texts flagged | 0.167 | 0.176 | 0.437 | 0.125 | 0.287 | 0.068 | 0.092 | 0.397 |
| ToxicChat: safe prompts flagged | 0.027 | 0.023 | 0.102 | 0.012 | 0.055 | 0.004 | 0.008 | 0.083 |

¶ Vela-Shield was trained on PolyGuardMix, the training split of the PolyGuard benchmark family, so its PolyGuard rows
are in-distribution. † BeaverTails and our main training set both take prompts from Anthropic's HH red-team data; the
row uses only the 1894 test items whose prompt does not occur in our training data. ToxicChat shares 29 of 5083 prompts
with our training data.

PolyGuard prompts per language (F1):

| Language | this model | Qwen3Guard-Gen-0.6B strict | Vela-Shield ¶ |
|---|---|---|---|
| Arabic | 0.773 | 0.817 | 0.834 |
| Chinese | 0.803 | 0.848 | 0.830 |
| Czech | 0.803 | 0.810 | 0.857 |
| Dutch | 0.762 | 0.789 | 0.813 |
| English | 0.797 | 0.875 | 0.871 |
| French | 0.797 | 0.843 | 0.847 |
| German | 0.776 | 0.818 | 0.813 |
| Hindi | 0.758 | 0.778 | 0.803 |
| Italian | 0.791 | 0.825 | 0.839 |
| Japanese | 0.796 | 0.801 | 0.831 |
| Korean | 0.761 | 0.787 | 0.795 |
| Polish | 0.771 | 0.807 | 0.808 |
| Portuguese | 0.771 | 0.845 | 0.849 |
| Russian | 0.772 | 0.845 | 0.813 |
| Spanish | 0.814 | 0.843 | 0.846 |
| Swedish | 0.799 | 0.802 | 0.837 |
| Thai | 0.762 | 0.823 | 0.799 |

### Categories

Category labels come from the Aegis 2.0 taxonomy of Nemotron-Safety-Guard-Dataset-v3 (merged into 15 groups). Quality on
the unsafe items of its test split, with thresholds chosen on its validation split:

| Category | threshold | F1 (test) | F1 at 0.5 | AUC | test positives |
|---|---|---|---|---|---|
| `criminal_planning` | 0.30 | 0.791 | 0.756 | 0.881 | 2060 |
| `violence` | 0.25 | 0.577 | 0.491 | 0.836 | 814 |
| `drugs` | 0.35 | 0.605 | 0.565 | 0.897 | 696 |
| `hate` | 0.20 | 0.736 | 0.693 | 0.933 | 592 |
| `harassment` | 0.25 | 0.518 | 0.441 | 0.832 | 562 |
| `privacy` | 0.15 | 0.705 | 0.596 | 0.913 | 483 |
| `other` | 0.25 | 0.500 | 0.146 | 0.881 | 479 |
| `weapons` | 0.20 | 0.608 | 0.509 | 0.875 | 368 |
| `sexual` | 0.55 | 0.712 | 0.733 | 0.934 | 333 |
| `profanity` | 0.15 | 0.570 | 0.500 | 0.892 | 326 |
| `self_harm` | 0.25 | 0.636 | 0.535 | 0.923 | 308 |
| `fraud_manipulation` | 0.15 | 0.347 | 0.065 | 0.851 | 299 |
| `unauthorized_advice` | 0.15 | 0.299 | 0.110 | 0.877 | 206 |
| `sexual_minors` | 0.25 | 0.397 | 0.293 | 0.899 | 165 |
| `misinformation` | 0.15 | 0.362 | 0.232 | 0.857 | 141 |

## Training

- **Data** (all permit commercial use):
  - [nvidia/Nemotron-Safety-Guard-Dataset-v3](https://huggingface.co/datasets/nvidia/Nemotron-Safety-Guard-Dataset-v3)
    (CC-BY-4.0; Aegis 2.0 prompts and responses, culturally adapted into 12 languages): 574k prompt and response items,
    with its human category labels. Rows derived from a Kaggle dataset (REDACTED) were dropped.
  - Real and red-team prompts without labels, scored by the teacher: first user turns and replies from
    [WildChat-1M](https://huggingface.co/datasets/allenai/WildChat-1M) (ODC-BY), prompts from
    [oasst2](https://huggingface.co/datasets/OpenAssistant/oasst2) and the [Aya dataset](https://huggingface.co/datasets/CohereForAI/aya_dataset)
    (Apache-2.0), [Salad-Data](https://huggingface.co/datasets/OpenSafetyLab/Salad-Data) (Apache-2.0; ToxicChat-derived rows
    dropped), [JailbreakBench behaviours](https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors) (MIT), and jailbreak,
    role-play and over-refusal prompts from the training data of our prompt-injection guard (270k + 42k items).
  - [Civil Comments](https://huggingface.co/datasets/google/civil_comments) (CC0): 60k comments with toxicity >= 0.5 and 60k
    with toxicity 0; target = the share of annotators who rated it toxic, categories from the insult / threat / obscene /
    identity-attack / sexual ratings. This improved the OpenAI moderation set (F1 +0.035) but not the textdetox recall.
  - (v1.1) Machine translations by Qwen3.8-27B (Apache-2.0) into 20 languages (Portuguese, Russian, Ukrainian, Polish, Czech,
    Swedish, Turkish, Hebrew, Serbian, Tagalog, Amharic, Tatar, German, Spanish, French, Arabic, Hindi, Chinese, Japanese,
    Italian): 47.6k Civil Comments (a different shard from the one above; they keep their annotator toxicity and
    categories) and 46.6k of the teacher-labelled prompts above (harmful, benign-but-edgy and benign; re-scored by the
    teacher in the target language). 1.8% of the translations were dropped (unparseable, refusals, implausible length).
  - (v1.2) 25k requests written by Qwen3.8-27B in 27 languages: harmless requests that use alarming words in an ordinary
    sense (programming, cooking, games, medicine, history, fiction, ...) and harmful look-alikes on the same topics, labelled
    by the teacher. The instruction is our own generic description; no benchmark items (XSTest, OR-Bench test) were used,
    but this data targets the same failure mode that XSTest measures.
  - Items that match any benchmark text were removed.
- **Teacher**: [Qwen3Guard-Gen-8B](https://huggingface.co/Qwen/Qwen3Guard-Gen-8B) (Apache-2.0). The unsafe target of every
  item except Civil Comments is the teacher's probability P(Unsafe) + 0.5 · P(Controversial); categories use the human labels. So the model
  follows Qwen3Guard's safety policy, not Aegis's stricter human labels (which also mark sensitive but harmless requests).
- **Model**: jhu-clsp/mmBERT-base with a 16-way sigmoid head (unsafe + 15 categories), 2 epochs, max length 1024 tokens.
- Code: `code/` in this repository.

## Versions

- v1.1 adds machine-translated toxic comments and red-team prompts in 20 languages: multilingual toxicity (textdetox) and native-speaker red-teaming (Aya) improve clearly; the other rows move by 0.01 or less.
- v1.2 adds 25k synthetic requests in 27 languages that use alarming words harmlessly, plus harmful look-alikes (teacher-labelled): it flags fewer safe-but-scary prompts (XSTest 28% -> 21%); ToxicChat F1 is 0.012 lower, other rows move by 0.01 or less.

To pin an earlier model, load it with `revision="v1.0"` or `revision="v1.1"`.

| | v1.0 | v1.1 | **v1.2 (this version)** |
|---|---|---|---|
| PolyGuard prompts, 17 languages | 0.779 | 0.782 | 0.783 |
| PolyGuard responses, 17 languages | 0.732 | 0.736 | 0.735 |
| BeaverTails responses (unseen prompts) † | 0.838 | 0.834 | 0.837 |
| ToxicChat (real user prompts) | 0.771 | 0.768 | 0.756 |
| OpenAI moderation set | 0.768 | 0.761 | 0.768 |
| XSTest (over-blocking test) | 0.786 | 0.785 | 0.809 |
| textdetox toxicity, 14 languages | 0.597 | 0.673 | 0.667 |
| Aya red-teaming, 8 languages (recall) | 0.766 | 0.807 | 0.800 |
| SimpleSafetyTests (recall) | 0.930 | 0.930 | 0.930 |
| XSTest: safe prompts flagged (lower is better) | 0.288 | 0.284 | 0.212 |

## Limitations

- It trails Qwen3Guard-Gen-0.6B (a generative 0.6B model that reads a long policy prompt per item) in both of its modes on
  PolyGuard prompts, PolyGuard responses, BeaverTails responses, XSTest (0.012-0.038 F1 behind its strict mode on PolyGuard responses / prompts); it is ahead of the
  strict mode on ToxicChat, OpenAI moderation set. Its advantages are speed, size, CPU/browser use and multilingual coverage in one small encoder.
- Over-blocking: it flags about 21% of XSTest's safe-but-scary prompts ("how do I kill a Python process").
- Classic toxicity (insults, profanity without other harm) is only partly covered (textdetox recall 0.56).
- Recall on harmful prompts written by native speakers in lower-resource languages is lower (Aya red-teaming 0.80).
- Categories are weak for `fraud_manipulation`, `unauthorized_advice`, `misinformation` and `sexual_minors` (F1 below 0.45).
  Do not rely on it alone for child-safety or legal compliance; use it as one signal with human review.
- Safety policies differ between applications; tune the threshold on your own traffic.
