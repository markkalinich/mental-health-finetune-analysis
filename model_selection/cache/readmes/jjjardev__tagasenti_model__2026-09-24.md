---
language:
  - tl
  - en
license: apache-2.0
library_name: transformers
pipeline_tag: text-classification
tags:
  - sentiment-analysis
  - filipino
  - tagalog
  - taglish
  - code-switching
  - low-resource-language
  - philippine-languages
  - xlm-roberta
  - adversarial-training
  - cross-lingual-transfer
datasets:
  - jjjardev/tagasenti
metrics:
  - accuracy
  - f1
base_model: xlm-roberta-large
model-index:
  - name: tagasenti_model
    results:
      - task:
          type: text-classification
          name: Sentiment Analysis (Tagalog/Taglish 3-class)
        dataset:
          type: jjjardev/tagasenti
          name: TagaSenti v6 (35,686 rows, deduplicated ~34,945, 80/10/10 seed 42)
          split: test
        metrics:
          - type: accuracy
            value: 0.848
            name: Accuracy
          - type: f1
            value: 0.848
            name: Macro F1
widget:
  - text: "Ang ganda ng quality ng tela, worth it ang price!"
    example_title: "Positive"
  - text: "Wala pa ring update ang order ko hanggang ngayon."
    example_title: "Negative"
  - text: "Sa aking palagay, hindi naman ito gaanong importante."
    example_title: "Neutral"
---

# tagasenti_model

## Model Description

**tagasenti_model (v6 release)** is a fine-tuned **XLM-RoBERTa-large** (355M parameters, 250K SentencePiece vocab) for **ternary sentiment classification** (Negative / Neutral / Positive) of **Tagalog and Taglish** (Tagalog-English code-switching) text.

It was trained on **TagaSenti v6 — 35,686 rows** (deduplicated to ~34,945), the final dataset on Hub (`jjjardev/tagasenti`), and achieves **84.8% test accuracy** and **macro-F1 0.848** on the held-out Tagalog test set (stratified 80/10/10, seed 42, val peak 0.863 at step 2400, 3 epochs). Zero-shot transfer to Hiligaynon (HiliSenti) is **58.6% F1**, with adversarial 100-set ceiling **~83%**.

**Version note — why v6:**
- **Dataset on Hub is v6 — 35,686 rows** (`v5.1 34,287 + 1,399 selective`: Contextual Pos 300, Neutral Factual 404, Hedged 300, Idioms 400). This release **matches dataset versioning** and fixes v4’s neutral hedging bias (“pero” → 0 err, Neu prediction error 0.9% vs 3 errors in v4).
- **Project-best remains v4 — 32,179 rows** (`v3 28,766 + 3,413 “no-keywords”`) with test F1 **0.866**, HiliSenti **0.624**, val peak **0.878** at step 3200 (unsaved due to `save_total_limit=2`). v5.1 (34,287) is the best *saved* checkpoint (0.856, `load_best_model_at_end` success). Retraining on v6 yields 0.848 — the ceiling of template-based synthetic data (~0.86 / 83% / 0.624) is well-characterized in `paper_notes/COMPLETE_DOCUMENTATION.md` §6, §14–15.
- v6 is the **final, dataset-aligned release** — no further iterations planned. Use v4 weights from `paper_notes/` if you need peak accuracy/cross-lingual; use **v6** for reproducibility with the Hub dataset.

The model was developed solo in 9 days (June 10–21, 2026) on **Colab free tier (Tesla T4)** + LLM web UIs at **$0** cost, using targeted adversarial augmentation over 4 generations to solve sarcasm, negation, and hedging failures.

## Intended Uses

- Sentiment analysis of Tagalog/Taglish customer reviews (Shopee, Lazada, e-commerce), social media comments (TikTok-style), and news-adjacent text
- Social media monitoring for Filipino-speaking communities
- Trend analysis for product feedback, service reviews, and public opinion
- Research on low-resource Philippine languages, code-switching, and cross-lingual transfer (Tagalog → Hiligaynon/Cebuano)
- Educational and civic technology applications in the Philippines

## Out-of-Scope Uses

- Fine-grained emotion detection (joy, anger, sarcasm) — model outputs only 3 coarse labels; adversarial `sarcasm` category targets sarcasm but does not label it
- Aspect-based sentiment analysis (ABSA)
- High-stakes moderation, legal, or financial decisions without human verification — idiom error rate is 47% (8/17 adversarial errors)
- Languages other than Tagalog/Taglish — zero-shot works partially for Hiligaynon (62.4%) but is not optimized for it; Cebuano/Ilokano not evaluated
- Long documents (>128 tokens) — truncated at 128 (p99=71–72); median HiliSenti is 96 tokens, Tagalog is ~63

## Training Data

The model was trained on **TagaSenti** (`jjjardev/tagasenti`, DOI `10.57967/hf/9620`, CC BY-SA 4.0). The dataset has two layers:

**Layer 1 — Real-world base (25,000 rows, perfectly balanced 33/33/33, stratified 80/10/10 seed 42):**

| Source | Domain | Language | Rows | Label Type |
|--------|--------|----------|------|------------|
| FiReCS (`ccosme/FiReCS`) — Shopee/Lazada reviews | E-commerce | Tagalog/Taglish | 10,481 | 3-class gold |
| SentiTaglish (`ccosme/SentiTaglishProductsAndServices`) — products & services (label 4→3 collapsed) | E-commerce | Tagalog/Taglish | 6,816 | 4→3 remapped |
| Amazon Polarity (`fancyzhx/amazon_polarity`, 10k sample → 3,942 after 14–50w filter + 1k synthetic neutral via Gemini 3.1 Pro) | E-commerce (multi-category) | English→Tagalog (Gemini 3.1 Pro) | 3,942 | Binary→3 + synthetic |
| NewsPH (`jcblaise/newsph`, 43k→41,768→5,999 labeled via Deepseek V4 Pro, 20×300 batches) | News (politics 17%, weather 14%, economy 8%) | Tagalog (formal, 99% named entities) | 5,999 | Synthetic 3-class |
| TikTok Hate Speech (`imperialite/filipino-tiktok-hatespeech`, 18,538→17,260→11,961→6,292 via Deepseek label+rewrite, 10 batches) | Social media (TikTok comments, 54% Q/! ) | Tagalog+English + slang | 6,292 | Synthetic 3-class (original hate labels discarded) |

**Layer 2 — Targeted adversarial augmentation (4 generations, 10,686 rows total; 9,378 after filtering):**

| Generation | Version | Rows | Categories | Strategy | Generator | Result |
|------------|---------|------|------------|----------|-----------|--------|
| 1st | v3 | 3,766 | 8 narrow (sarcasm, negation, wish, indirect complaint, factual-neutral trigger, mixed/ambiguous, rhetorical Qs, hard positive) | Keyword guardrails, batch rotation, human spot-checks | Gemini 3.1 Pro | +18pp benchmark (74%→92% 50-set) |
| 2nd | **v4** | **3,413** | 6 narrow (sarcasm 800, complaint 700, relief 400, double-neg 400, hedge 300, idiom 400) | **“No keywords” — ban explicit sentiment words, force context-only learning** | Gemini/Deepseek | **Production — test +3.3 Hili, sarcasm 5→0** |
| 3rd | v5/v5.1 | 2,417 | 8 (11/28 files, single-batch → formulaic) | Idiom/pattern-heavy | Gemini/Deepseek | Failed to surpass v4 (0.856) |
| 4th | v6 | 1,399 | 4 selective (Contextual Pos 300, Neutral Factual 404, Hedged 300, Idioms 400) | Class rebalancing (Pos/Neu/Idioms only) | Gemini/Deepseek | Neu bias fixed, 0.848 |

**Final composition v6:** 35,686 rows | Neg 13,259 (37.2%) / Neu 11,656 (32.7%) / Pos 10,771 (30.2%) | Class weights `[0.897, 1.021, 1.104]`. v4: 32,179 rows | Neg 12,067 / Neu 10,322 / Pos 9,790 | Weights `[0.8889, 1.0392, 1.0956]`. Deduplicated for training: ~34,945 (741 exact duplicates, 113 with conflicting labels — keep first, see `scripts/validate_dataset.py`).

Excluded: DailyDialog (CC BY-NC-SA 4.0 incompatible), iTANONG (DOST-ASTI gated), Shopee/SST-2/IMDb (domain saturation / phrase fragments / excessive length).

## Training Procedure

- **Base model:** `xlm-roberta-large` (355M, 250k SentencePiece vocab) — **cased**, no lowercasing (preserves Filipino emphasis: `AYAW KO NA` ≠ `ayaw ko na`)
- **Text normalization (`normalize_tagalog` in `scripts/train/TagaSenti.py`):**
  - Unicode NFKC (ligatures/homoglyphs/half-width collapsed)
  - Laughter canonicalization: `hahaha…` / `HAHAHA` → `hahaha` (IGNORECASE), `hehehe` similarly
  - Reduplication: `abot2` → `abot abot` (≥3-char words), `abot-abot` → `abot abot` (hyphenated)
  - Slang expansion — 25 high-confidence patterns (`wla→wala`, `dko→di ko`, `kc/ksi→kasi`, `sya/xa/xia→siya`, `nya→niya`, `dba/diba→di ba`, etc.); 3 removed for collision (`pro→pero`, `mn→man`, `ala→wala`)
  - Char deduplication ≥3→2 (`graaaabe→graabe`), whitespace collapse
  - No `add_prefix_space` (SentencePiece, not BPE)
- **Tokenizer:** `AutoTokenizer.from_pretrained("xlm-roberta-large")`, dynamic `DataCollatorWithPadding`, max length **p99 = 71–72** (capped at 128) from 2,000-sample probe; HiliSenti p95=96
- **Split:** Stratified **80/10/10** by label, **seed 42** (v4: 25,743/3,218/3,218; v6: ~27,955/3,569/3,569). Deduplicate *before* split to avoid leakage. Offline v1–v4 held adversarial train-only for comparable val/test; Hub single `train` split is mixed — `scripts/train/TagaSenti.py` does reproducible random split.
- **Optimization:**
  - Effective batch 32 (16 per device × 2 grad accum), LR `2e-5`, cosine `min_lr 1e-6`, warmup `312` steps (10%), `adamw_torch_fused`, `weight_decay 0.05`
  - `label_smoothing 0.10` via **CustomTrainer** (explicitly passed to `nn.CrossEntropyLoss` — fixes HF Trainer bug where `label_smoothing_factor` is ignored when `compute_loss` is overridden)
  - `gradient_checkpointing True`, `fp16` when CUDA, 5 epochs v4 (4,025 steps) / 3 epochs v5.1/v6 (2,574/2,679 steps), early stopping patience 3 (`f1_macro`)
  - Class weights from `compute_class_weight("balanced")` per version; v4 `[0.8889, 1.0392, 1.0956]`
- **Callbacks:** `EarlyStoppingCallback`, **ConfusionMatrixCallback** (uses shared `_last_eval` cache from `compute_metrics` — fixes silent no-op where `on_evaluate` never receives `eval_dataset`)
- **Infrastructure:** Colab free tier Tesla T4, Drive 15GB limit → `save_total_limit` pruned best ckpt (v4 peak 0.878 not saved); v5.1 fixed with `save_total_limit=0` (✅ `load_best_model_at_end`), v6 failed on sharded safetensors (`save_safetensors=False` needed). Tokenization cap 4 workers.
- **Compute:** ~50 min training + 30 min HiliSenti eval (v1 baseline); ~30h active work over 9 days total.

## Evaluation Results

### Tagalog Held-Out Test (v6 release, 3,569 rows, final step 2679 — val peak 2400 not loaded due to sharded safetensors)

| Metric | Negative | Neutral | Positive | Overall |
|--------|----------|---------|----------|---------|
| **Precision** | — | — | — | — |
| **Recall** | — | — | — | — |
| **F1-Score** | 0.861 | **0.831** | 0.853 | — |
| **Accuracy** | — | — | — | **84.8%** |
| **Macro F1** | — | — | — | **0.848** |
| **Balanced Accuracy** | — | — | — | 84.8% |

*Per-class at peak step 2400 (F1 0.863, loss 0.555): Neg 0.882 / Neu 0.834 / Pos 0.871, pred 1,354/1,176/1,039 (true 1,190/1,190/1,189) — Neu error 0.9% (hedging bias fixed). Final step 2679 used for Hub weights: test 0.848 (Neg 0.861 / Neu 0.831 / Pos 0.853).*

**Val peak (v6, step 2400):** F1 **0.863** (Neg 0.882 / Neu 0.834 / Pos 0.871), loss 0.555. **Project-best (v4, step 3200, unsaved):** F1 **0.878** (Neg 0.891 / Neu 0.848 / Pos 0.894).

**Cross-version:** v1 0.835 → v3 0.849 (+1.4) → **v4 0.866 (+1.7, peak 0.878)** → v5.1 0.856 (best saved, `load_best_model_at_end` ✅) → **v6 0.848 (release, dataset-aligned)**. 83% adversarial ceiling holds.

### Cross-Lingual Zero-Shot — HiliSenti (Hiligaynon, `jjjardev/hilisenti-v1` test 2,242 rows, same `normalize_tagalog`)

| Metric | v1 | v3 | **v4 (peak)** | v5.1 | **v6 (release)** |
|--------|----|----|---------------|------|------------------|
| **F1 Macro** | 0.558 | 0.591 | **0.624** | 0.585 | **0.586** |
| Neg F1 | 0.571 | 0.618 | **0.649** | — | — |
| Neu F1 | 0.464 | 0.556 | 0.565 | — | — |
| Pos F1 | 0.637 | 0.599 | **0.657** | — | — |
| Accuracy | 55.8% | 59.2% | **62.4%** | — | 58.6% |

*v4 Pos +5.8 is the single largest cross-lingual gain (context-only “relief” 400 rows transferred). v6 ties v5.1 on Hili (0.586); ~25% relative drop from Tagalog is the zero-shot ceiling; 500 Hiligaynon examples would likely push to 0.70–0.75.*

### Adversarial Benchmark (100 sentences, edge cases: idioms, double neg, sarcasm, hedging)

| Model | Score | Sarcasm (5) | Idioms (10) | Neu Hedge | Negation |
|-------|-------|-------------|-------------|-----------|----------|
| v3 | 81% (81/100) | 5 err | 10 err | 1 err | 2 err |
| **v4** | **83% (83/100)** | **0 err** | 8 err | 3 err | 2 err |
| v5.1 | 83% (83/100) | 0 err | 8 err | **0 err** | 4 err |

*50-sentence benchmark (v1 era): v1 74% → v2 68% (regression) → v3 92% (+18). 100-general (too easy) v3 97.9% superseded by adversarial set. v6 not independently benchmarked (~83%). Idioms are the #1 unsolved problem — 8 errors stable across v4/v5.1/v6 despite 3 generations of idiom data.*

**Version guidance (v6 is Hub release):** Dataset-aligned / hedged neutral (customer feedback) → **v6** (Neu 0.831, 0.9% error); peak accuracy / cross-lingual → v4 (0.866 / 0.624, unsaved peak 0.878) from `paper_notes/`; reproducibility / best saved → v5.1 (0.856). Idiom-heavy → none (8 errors stable).

## Limitations

- **Idioms:** 8/17 adversarial errors (47%) are Filipino idioms/figurative — template-based generation cannot teach non-compositional semantics (`ningas-kugon` etc.). All 3 idiom generations failed identically.
- **`load_best_model_at_end` unreliable:** 3 of 4 runs failed (v4 `save_total_limit=2` deleted peak 0.878; v5 `10`; v6 sharded safetensors). Only v5.1 succeeded (`0` + `pytorch_model.bin`). Use `save_safetensors=False` in future.
- **Single seed (42):** No variance estimate; 3 seeds would confirm robustness (<0.01 std expected).
- **LLM label noise:** NewsPH (5,999) + TikTok (6,292) labeled by Deepseek V4 Pro single-pass, zero human validation; Amazon translated by Gemini 3.1 Pro with syntactic bottleneck (35% `pero/kaso` contrast). 500-sample human eval planned but never executed.
- **Domain gaps:** Movie reviews (SST-2/IMDb excluded), food/restaurant, beauty/cosmetics, education (Student 2,272 deferred) absent; 3 base domains only (e-commerce 63%, news 18%, social 19% at 4_READY).
- **Translation artifacts:** Amazon machine-translated Tagalog shows compressed syntax; adversarial data may contain non-native artefacts.
- **No confidence calibration:** Single label output, no distribution; neutral boundary weakest (lacks strong lexical signal).
- **Truncation:** 128-token cap may cut long news sentences (HiliSenti p95=96 vs Tagalog 63–72).
- **Reproducibility:** All LLM generation via manual web UI pastes (72 batches, ~27k rows) — free but not API-scripted; prompt templates in `paper_notes/` + seed 42 mitigate.

## Ethical Considerations

- **Public data only:** FiReCS/SentiTaglish (public reviews), Amazon (public), NewsPH (public news sites with named individuals/locations), TikTok (public comments) — all under open licenses or public availability. No private data.
- **No PII scrubbing:** Social media comments and news articles contain real names, locations, violence descriptions. `HFREADME.md` includes **Important Notice** — no anonymization applied. Users requiring anonymized data should apply their own NER/scrubbing pipeline.
- **Adversarial sentences are synthetic** — no personal information.
- **Biases:** Domain skew (e-commerce 35.6% at v6), LLM pretraining bias, translation bias, socioeconomic skew (TikTok/SentiTaglish demographics), adversarial generation bias (English-centric LLM). See dataset card `Discussion of Biases`.
- **Intended effect:** Lower barrier for Filipino NLP, spur Philippine language tech, demonstrate $0 solo researcher pipeline — not for high-stakes decisions without verification.
- **Licensing is tri-partite:** Dataset CC BY-SA 4.0 (ShareAlike required by TikTok), model weights Apache 2.0, code MIT — see `LICENSES.md`.

## How to Use

### Via Transformers

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

# Load model and tokenizer — downloads from https://huggingface.co/jjjardev/tagasenti_model
model = AutoModelForSequenceClassification.from_pretrained("jjjardev/tagasenti_model")
tokenizer = AutoTokenizer.from_pretrained("jjjardev/tagasenti_model")
model.eval()

# Example inference (Tagalog / Taglish)
sentences = [
    "Ang ganda ng quality ng tela, worth it ang price!",  # Positive
    "Wala pa ring update ang order ko hanggang ngayon.",  # Negative
    "Sa aking palagay, hindi naman ito gaanong importante.",  # Neutral
    "Ang bait mo naman, pinagbigyan mo ako sa wakas.",  # Negative (sarcasm — adversarial)
]
inputs = tokenizer(sentences, padding=True, truncation=True, max_length=128, return_tensors="pt")
with torch.no_grad():
    logits = model(**inputs).logits
    probs = torch.softmax(logits, dim=-1)
    preds = logits.argmax(dim=-1)

labels = ["Negative", "Neutral", "Positive"]
for sent, pred, prob in zip(sentences, preds, probs):
    print(f"{labels[pred]} ({prob[pred]:.2%}): {sent}")
```

### Using the Pipeline API

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="jjjardev/tagasenti_model", tokenizer="jjjardev/tagasenti_model", truncation=True, max_length=128)

result = classifier("Napakabagal ng serbisyo nila, nakakainis.")
print(result)  # [{'label': 'Negative', 'score': 0.91}]

# Batch
results = classifier([
    "Sobrang saya ko sa nabili ko!",
    "Okay lang, parang kulang sa alat.",
    "Hindi ko nagustuhan, sira agad.",
])
for r in results:
    print(r)
```

### CLI (local repo)

```bash
pip install -r requirements.txt  # or pip install -e .
python scripts/inference.py "Ang ganda ng tela!" --hf-id jjjardev/tagasenti_model
python scripts/inference.py --file sentences.txt --json --batch-size 16
python scripts/validate_dataset.py --csv tagasenti_dataset.csv
```

## Citation

If you use this model or TagaSenti in your research, please cite:

**Model:**

```bibtex
@misc{jessie_james_jarder_2026_tagasenti_model,
  author    = {Jessie James Jarder},
  title     = {tagasenti_model (Revision tagasenti_model)},
  year      = {2026},
  publisher = {Hugging Face},
  url       = {https://huggingface.co/jjjardev/tagasenti_model},
  doi       = {10.57967/hf/9620},
}
```

**Dataset:**

```bibtex
@misc{jessie_james_jarder_2026,
  author       = {Jessie James Jarder},
  title        = {tagasenti (Revision 3ebda33)},
  year         = {2026},
  url          = {https://huggingface.co/datasets/jjjardev/tagasenti},
  doi          = {10.57967/hf/9620},
  publisher    = {Hugging Face}
}
```

**APA (dataset):**

Jarder, J. J. (2026). *tagasenti* (Revision 3ebda33) [Data set]. Hugging Face. https://doi.org/10.57967/hf/9620

## Licenses

| Component | License | File |
|-----------|---------|------|
| **Model Weights** | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | `model/README.md` Hub card |
| **Dataset** | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) | `HFREADME.md` / Hub |
| **Training Code** | [MIT](https://opensource.org/licenses/MIT) | `LICENSE` / `LICENSES.md` |

Component licenses: FiReCS CC BY 4.0, SentiTaglish CC BY 4.0, Amazon Apache 2.0, NewsPH public news text (no explicit license), TikTok CC BY-SA 4.0, adversarial CC BY-SA 4.0.

## Related Resources

- **Dataset:** [jjjardev/tagasenti](https://huggingface.co/datasets/jjjardev/tagasenti) — DOI `10.57967/hf/9620`
- **Code:** [github.com/jjjardev/tagasenti](https://github.com/jjjardev/tagasenti)
- **HiliSenti (sister project):** [jjjardev/hilisenti-v1](https://huggingface.co/datasets/jjjardev/hilisenti-v1) / [jjjardev/hilisenti-v1-model](https://huggingface.co/jjjardev/hilisenti-v1-model) (93.5% F1, Hiligaynon — structure reference for this card)
- **Base model:** [xlm-roberta-large](https://huggingface.co/xlm-roberta-large)
- **Paper notes (private, 9-day log v1–v6):** `paper_notes/COMPLETE_DOCUMENTATION.md` (1305 lines), `run_report.md` (1575 lines) — distilled into this card

## Contact

Jessie James T. Jarder — jj.jarder.dev@gmail.com  
Issues: [github.com/jjjardev/tagasenti/issues](https://github.com/jjjardev/tagasenti/issues) · HF discussion: [huggingface.co/jjjardev/tagasenti_model/discussions](https://huggingface.co/jjjardev/tagasenti_model/discussions)
