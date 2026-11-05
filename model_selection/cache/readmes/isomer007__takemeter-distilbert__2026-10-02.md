---
library_name: transformers
tags:
  - text-classification
  - distilbert
  - crypto
  - sentiment
  - fine-tuned
pipeline_tag: text-classification
---

# Model Card: `isomer007/takemeter-distilbert`

## Model Details

### Model Description

`isomer007/takemeter-distilbert` is a 3-class text classifier fine-tuned from [`distilbert-base-uncased`](https://huggingface.co/distilbert-base-uncased) on 153 hand-labeled r/CryptoCurrency posts. It sorts crypto-community posts by the **quality of the take** — not by whether a post is bullish or bearish, but by whether its claim is backed by load-bearing, checkable evidence.

The fine-tuned model is the center of the [AlphaSift](https://github.com/isomer04/alphasift) project, which also includes a zero-shot `llama-3.3-70b-versatile` baseline and a Gradio demo. The complete writeup — taxonomy, label definitions, error analysis, and a side-by-side comparison with the baseline — lives in the [project README](https://github.com/isomer04/alphasift#readme).

**The headline finding from the project evaluation is that this fine-tuned model *loses* to a zero-shot `llama-3.3-70b-versatile` baseline on the locked 23-post test set** (0.522 vs 0.783 accuracy, a 0.261 gap). The cause is a data-quantity failure on 107 training examples, not a pipeline bug — see the [Evaluation](#evaluation) section below. The model is published because (a) the failure mode is itself a useful finding, and (b) `classifier.py` and `app.py` in the repo load it cleanly so the result is reproducible.

- **Developed by:** [isomer007](https://huggingface.co/isomer007)
- **Funded by:** N/A (independent project)
- **Shared by:** [isomer007](https://huggingface.co/isomer007)
- **Model type:** `DistilBertForSequenceClassification` (3-class single-label classification)
- **Language(s) (NLP):** English (lowercased via the DistilBERT uncased tokenizer)
- **License:** Apache 2.0 (inherited from `distilbert-base-uncased`)
- **Finetuned from model:** [`distilbert-base-uncased`](https://huggingface.co/distilbert-base-uncased)

### Model Sources

- **Repository:** [github.com/isomer04/alphasift](https://github.com/isomer04/alphasift)
- **Demo:** runnable locally with `python app.py` (Gradio) — see the [project README](https://github.com/isomer04/alphasift#run-it-locally)
- **Base model:** [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased)
- **Loom walkthrough:** [b1a6d49f7665437db84418751f383359](https://www.loom.com/share/b1a6d49f7665437db84418751f383359)

## Uses

### Direct Use

The model's intended use is **classifying a single short Reddit-style post (≤256 tokens) as one of three labels**:

| Label | Definition |
|---|---|
| `signal` | Claim backed by load-bearing, verifiable evidence — on-chain data, a named mechanism, a concrete historical comparison. Direction (bullish or bearish) does not matter. |
| `hype` | Bullish claim with no real evidence — bare price targets, FOMO, "to the moon." |
| `panic` | Bearish claim with no real evidence — doom, "scam," nothing behind it. (The community's native term for this is "FUD.") |

It is a research / educational artifact that demonstrates the failure mode of fine-tuning a small encoder on a tiny hand-labeled dataset, and the value of comparing against a strong zero-shot baseline.

### Downstream Use

- **Component in a larger crypto-content pipeline.** A downstream user could treat the model's `signal` probability as a "quality score" attached to each post and aggregate it across a feed.
- **Comparison baseline.** Anyone fine-tuning a small text classifier on a domain-specific taxonomy can compare against this model to see what 107 training examples buys you (and what it doesn't).
- **Discussion-quality moderation signal.** Could be used as one input among several for surfacing "reasoned" vs. "emotional" posts in a community feed — but **not** as a single decision-maker, for the reasons in the next section.

### Out-of-Scope Use

- **Financial advice or trading signal generation.** The model classifies *discourse quality*, not market direction. It does not predict prices, sentiment polarity, or trade outcomes. Any system that wires this model's output directly into a trading decision is misusing it.
- **Posts outside the r/CryptoCurrency distribution.** Trained on a single subreddit's idiom (informal, US-English, crypto-native vocabulary, lots of slang like "FUD", "hopium", "rug", "LFG", "GM", emoji-heavy). Performance will degrade on more formal financial writing, non-English text, or posts about adjacent domains (general finance, NFTs without the trading angle, pure tech discussion of blockchain protocols).
- **Posts with no stance.** The 3-class taxonomy is gated: a post with no take at all (news links, neutral questions, memes) is supposed to be filtered out upstream and is *not* one of the model's three classes. Routing `filter`-like content to this model will produce a forced 3-way prediction that should be ignored.
- **High-stakes content moderation.** A 0.522 accuracy on a 23-post test set is below random-oracle quality for any moderation decision with real consequences.
- **Inference on text longer than 256 tokens.** Posts are truncated to `max_length=256` at inference time; longer posts will have their tail silently cut off.

## Bias, Risks, and Limitations

### Known limitations of this model

- **Below the zero-shot baseline on the project's locked test set.** 0.522 vs 0.783 accuracy for `llama-3.3-70b-versatile` zero-shot on the same 23 posts. The fine-tuned model is **not** the recommended classifier in the AlphaSift project; the baseline is.
- **Confidence is at chance level on every prediction.** In the reported evaluation run, every prediction (right or wrong) had a softmax confidence in the 0.34–0.35 band, essentially indistinguishable from the 0.333 a uniform 3-way guess would produce. The model is not confidently right *or* confidently wrong; it sits near the decision boundary between all three classes. **Do not treat the confidence number as a reliable signal.**
- **Instability across training runs.** Re-running the same training notebook on the same data with the same seed produced a *different* model with a *different* "broken" class. The model's behavior is not a stable function of the training pipeline.
- **Data-quantity failure.** 107 training examples spread across 3 classes (as few as 24 for `hype`) is well below the threshold at which a 6-layer transformer can pin down a reproducible decision boundary. The model has learned weak proxies — see the [Reflection section in the project README](https://github.com/isomer04/alphasift#reflection--what-the-model-learned-vs-what-i-intended) — not the intended rule.
- **Small test set.** All reported numbers are on 23 posts; the smallest per-class support is 5 (`hype`), so a single flipped prediction moves that class's F1 by ~0.10–0.15. Per-class numbers should be read as directional, not precise.
- **Sentiment proxies.** The model partially recovers a sentiment axis (positive ↔ negative language) it was never asked to learn, and uses it as a shortcut. The "FTX/Anthropic stake breakdown" example in the project README — rigorous bearish-evidence content — is misread as `panic` because of negative-coded vocabulary.
- **Numeric-density proxy.** The model uses "contains numbers" as a shortcut for `signal`. The "buying at 60k, betting on 200k" post — dense with price targets but no mechanism — is misread as `signal` instead of `hype`. This is the one error pattern that recurred identically across both training runs.

### Known biases of the training data

- **Single-subreddit source.** All 206 labeled rows are r/CryptoCurrency posts. Crypto-Twitter, crypto-Discord, and other subreddits will have different discourse norms.
- **Hand-pick survivorship bias.** The 250 candidates handed to the labeling pipeline were pre-selected by browsing the sub; stanceless content was already under-collected upstream of the labeling pass. The dataset is clean and taxonomy-consistent, not a representative sample.
- **Pre-label anchoring.** An LLM (Claude) pre-labeled candidates before hand-review; 16/206 labels (7.8%) were corrected on review, but the prelabel may have anchored the reviewer on the rest. A v2 protocol would blind the reviewer to the prelabel on a sample to measure anchoring directly.
- **Sentiment imbalance in `signal`.** The dataset has more bullish-evidence posts than bearish-evidence posts, both because bullish-evidence content is more common on r/CryptoCurrency and because rigorous bearish analysis is harder to find. This contributes to the `signal` → `panic` error pattern.
- **Length imbalance.** The training set is dominated by longer, citation-heavy posts in each class. Short, terse `signal` posts (e.g. "It is actually more profitable now to rent out GPU time to AI than it is to mine w/ ASICs") are underrepresented and frequently misread.

### Recommendations

Users (both direct and downstream) should be made aware of the risks, biases, and limitations of the model. More specific recommendations:

- **Do not deploy this model as a standalone classifier.** Use the [`llama-3.3-70b-versatile`](https://console.groq.com/) zero-shot baseline from the same project, which outperforms it on the project's own test set.
- **If you must use this model**, treat its output as a weak signal and the confidence number as uninformative (it sits at chance). Apply it only on posts that are already known to express a stance (`filter` has been removed upstream), and only on short Reddit-style English text.
- **For any decision with consequences**, re-evaluate on a larger, balanced test set, or fall back to the zero-shot baseline.
- **A v2 of this model** would need (a) ≥10× the training data per class, (b) targeted counter-examples to break the sentiment- and density-proxy heuristics (short terse `signal` posts, number-dense `hype` posts, balanced-sentiment `signal` posts), and (c) bootstrap confidence intervals on every reported metric, not point estimates on n=23.

## How to Get Started with the Model

Use the code below to get started with the model. The `transformers` pipeline is the lightest path; the project's own `classifier.py` wraps the same call with the AlphaSift label order and a 256-token truncation.

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="isomer007/takemeter-distilbert",
    top_k=None,           # return probabilities for all 3 classes
    truncation=True,
    max_length=256,
)

result = classifier("9 UMA whale wallets control 53.1% of voting power. "
                    "Same wallets fund $12.5M Polymarket side-bets on "
                    "markets they resolve. The oracle is mathematically "
                    "incentivized to lie.")
# Returns: [[{'label': 'signal', 'score': ~0.34},
#            {'label': 'panic',  'score': ~0.33},
#            {'label': 'hype',   'score': ~0.33}]]
# Note: the project evaluates this exact post as correctly labeled 'signal',
# but the model's confidence is at chance — see the Limitations section.

# Or, for a single top label and confidence:
top = classifier("SOL is so back. This is the floor, screenshot this. LFG 🚀🚀")
print(top[0][0])  # {'label': 'hype', 'score': ~0.34}
```

For the full project — including the Groq baseline, evaluation, and Gradio demo — clone the repo and use the included `classifier.py` and `app.py`:

```bash
git clone https://github.com/isomer04/alphasift
cd alphasift
pip install -r requirements.txt
python app.py          # Gradio demo at http://localhost:7860
python evaluate.py     # reproduces the locked 23-post test-set evaluation
```

## Training Details

### Training Data

- **153 labeled examples** used for training (after dropping `filter` rows and stratified-splitting 70/15/15), drawn from a hand-collected pool of ~250 r/CryptoCurrency posts.
- **206 total rows** in the full labeled dataset, with a `filter` rate of 25.7% (53/206). The remaining 153 are split:
  - `signal`: 65 rows (42.5% of usable)
  - `panic`: 54 rows (35.3% of usable)
  - `hype`: 34 rows (22.2% of usable)
- **No class exceeds 70% of the usable set; every quality class is at or above the 20% floor.**
- The full dataset is committed to the [project repo](https://github.com/isomer04/alphasift) at `data/alphasift_dataset.csv` (with `[REVIEWED]` flags in the `notes` column showing which rows were hand-corrected from the AI prelabel).
- The label taxonomy (definitions, decision tree, edge-case rules) is at [`data/taxonomy.md`](https://github.com/isomer04/alphasift/blob/main/data/taxonomy.md) in the project repo.
- **Licensing:** The posts are public Reddit comments; they inherit Reddit's user-content license. They are not redistributed as a standalone dataset; they are part of the AlphaSift project repo.

#### Labeling process

1. **AI-assisted cleaning pass.** Claude filtered out stanceless content (news links, questions, memes, sponsored posts) from the 250 hand-collected candidates. Kept posts were re-read to confirm nothing load-bearing was dropped.
2. **AI pre-labeling.** Claude pre-labeled the remaining candidates (flagged as `prelabeled` in the `notes` column).
3. **Hand-review pass.** Every one of the 206 final rows was then read and hand-reviewed against the taxonomy's decision rule. 16 of 206 rows (7.8%) had their label corrected on review; all 206 rows are now marked `[REVIEWED]` in `notes`, with the original prelabel preserved in the note text where it was overridden along with the reasoning for the change.

### Training Procedure

- **Base model:** [`distilbert-base-uncased`](https://huggingface.co/distilbert-base-uncased) (6 layers, 768 hidden dim, 12 attention heads, 30522 vocab, tied input/output embeddings).
- **Head:** 3-class sequence-classification head; `id2label = {0: "hype", 1: "panic", 2: "signal"}`, taken from `config.py` so the head's label order matches the rest of the repo.
- **Preprocessing:** Posts are tokenized with the DistilBERT uncased tokenizer, truncated to `max_length=256`, and padded. `filter` rows are dropped before training, so the model only ever sees `signal` / `hype` / `panic`.
- **Trainer:** HuggingFace `Trainer` with the following hyperparameters:

| Hyperparameter | Value |
|---|---|
| Epochs | 3 |
| Learning rate | 2e-5 |
| Train batch size | 16 |
| Weight decay | 0.01 |
| Warmup steps | 50 |
| Max sequence length | 256 |
| Best-model selection | highest validation accuracy (`load_best_model_at_end`) |
| Random seed | 42 |

- **Data split:** stratified 70/15/15 on the 153 usable rows → 107 train / 23 validation / 23 test. The split is seeded (`random_state=42`) so the test set is reproducible locally via `evaluate.py`.

#### Training Hyperparameters

- **Training regime:** fp32 (full precision; no mixed precision was used). The model is small enough (~67M parameters) that fp32 fits comfortably on a free Colab GPU.

#### Speeds, Sizes, Times

- **Training time:** single-digit minutes per run on a free Colab GPU (T4); the notebook ran end-to-end in well under the 90-minute Colab free-tier cutoff.
- **Checkpoint size:** ~255 MB (the standard DistilBERT float32 size on disk).
- **Inference latency:** low single-digit milliseconds per post on a modern CPU; the Gradio demo runs comfortably on the HF Spaces free CPU tier.

## Evaluation

All numbers below are on the **same locked 23-post test set** (the 15% test split from the stratified split above). The full per-class breakdown, confusion matrix, and per-post error analysis are in the [project README's Evaluation report section](https://github.com/isomer04/alphasift#evaluation-report).

### Testing Data, Factors & Metrics

#### Testing Data

- 23 posts held out from the same hand-labeled r/CryptoCurrency pool used for training, stratified across the three quality classes:
  - `signal`: 10 posts
  - `panic`: 8 posts
  - `hype`: 5 posts
- Tokenized with the same DistilBERT uncased tokenizer at `max_length=256`.
- Labeled by the same hand-review process as the training data (see [Training Data](#training-data) above).
- The full test set is reproducible locally: `python evaluate.py` regenerates the exact 23 posts from the locked seed and re-runs both models.

#### Factors

The evaluation is disaggregated by:
- **True class** (`signal` / `panic` / `hype`) — reported as per-class precision, recall, F1, and support, plus a confusion matrix.
- **Sentiment direction** of the post (bullish vs. bearish) — relevant because the dominant error is `signal` → `panic` for bearish-evidence posts (the model uses negative-sounding vocabulary as a proxy for `panic`).
- **Post length and numeric density** — relevant because the model uses length and numeric density as proxies for `signal`.

The evaluation is **not** disaggregated by subreddit, language, or time period (all 23 posts are r/CryptoCurrency, English, contemporaneous with the training data).

#### Metrics

- **Accuracy** — overall fraction of correct top-1 predictions.
- **Per-class precision, recall, F1, support** — standard `classification_report` output.
- **Macro and weighted F1** — to summarize across the imbalanced class distribution.
- **Confusion matrix** — to make the dominant error pattern (`signal` → `panic`, 6 of 10 true `signal` posts) visible at a glance.
- **Confidence calibration** — the softmax probability of the predicted class on every test post, reported in the project README. *All* predictions in the reported run fall in the 0.34–0.35 band.

### Results

#### Fine-tuned model (this model)

| Class | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| `hype` | 0.67 | 0.40 | 0.50 | 5 |
| `panic` | 0.43 | 0.75 | 0.55 | 8 |
| `signal` | 0.67 | 0.40 | 0.50 | 10 |
| **macro avg** | 0.59 | 0.52 | 0.52 | 23 |
| **weighted avg** | 0.58 | 0.52 | 0.52 | 23 |

**Overall accuracy: 0.522**

Confusion matrix (rows = true, columns = predicted):

| True ↓ \ Pred → | `hype` | `panic` | `signal` | Total |
|---|---|---|---|---|
| **`hype`** | 2 | 2 | 1 | 5 |
| **`panic`** | 1 | 6 | 1 | 8 |
| **`signal`** | 0 | 6 | 4 | 10 |
| **Total predicted** | 3 | 14 | 6 | 23 |

#### Zero-shot baseline (`llama-3.3-70b-versatile` via Groq, no fine-tuning)

For context — the baseline that beat this model on the same test set:

| Class | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| `hype` | 0.67 | 0.80 | 0.73 | 5 |
| `panic` | 0.78 | 0.88 | 0.82 | 8 |
| `signal` | 0.88 | 0.70 | 0.78 | 10 |
| **macro avg** | 0.77 | 0.79 | 0.78 | 23 |
| **weighted avg** | 0.80 | 0.78 | 0.78 | 23 |

**Overall accuracy: 0.783**

The zero-shot baseline wins on every class: `hype` 0.73 vs 0.50 F1, `panic` 0.82 vs 0.55 F1, `signal` 0.78 vs 0.50 F1. It never saw a single training example and still outperforms this model, because it brings pretrained world knowledge of what each kind of take sounds like — knowledge that 107 examples can't replace.

#### Summary

| Model | Test accuracy |
|---|---|
| **Zero-shot baseline (`llama-3.3-70b-versatile`)** | **0.783** |
| **Fine-tuned DistilBERT (this model)** | **0.522** |
| **Difference** | **−0.261 (this model regresses vs. baseline)** |

The dominant error pattern is **`signal` → `panic`** (6 of 10 true `signal` posts). The model is not learning the intended evidence-quality rule; it is learning two cheaper proxies — *negative-sounding words ⇒ `panic`* and *numeric density ⇒ `signal`/non-`panic`*. The full per-post error analysis is in the [project README's "Wrong predictions, analyzed" section](https://github.com/isomer04/alphasift#wrong-predictions-analyzed).

The model also exhibits **run-to-run instability**: re-running the same training notebook on the same data with the same seed produced a different model where `hype` collapsed to 0% recall instead of `signal`. The specific failure mode is not stable; the underlying problem (data quantity) is.

## Model Examination

The model's learned behavior was examined qualitatively via per-post error analysis on the locked test set, not via internal interpretability work (attention probing, probing classifiers, etc.). Three findings:

1. **Sentiment proxy.** The model treats negative-coded vocabulary as evidence of `panic`, even when the post is rigorously evidence-backed (the FTX/Anthropic stake breakdown is the clearest example). This is consistent with the model having recovered a sentiment axis it was never asked to learn.
2. **Numeric-density proxy.** The model treats the *presence of numbers* as evidence of `signal`, even when the numbers are bare price targets with no mechanism (the "buying at 60k, betting on 200k" post). This proxy is the one error pattern that recurred identically across both training runs.
3. **Chance-level confidence on every prediction.** Every prediction in the reported run has a softmax confidence in the 0.34–0.35 band — indistinguishable from uniform 3-way chance. The model is near the decision boundary between all three classes on essentially every input, which is consistent with a model that has not pinned down a stable decision boundary at all (data-quantity failure, not mislearned-rule failure).

No formal probing, attention visualization, or embedding-space analysis has been performed; these would be reasonable follow-ups but are out of scope for the v1.

## Environmental Impact

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).

- **Hardware Type:** NVIDIA T4 (Google Colab free tier)
- **Hours used:** single-digit minutes per training run; the model was fine-tuned only a small number of times during development
- **Cloud Provider:** Google Cloud (via Colab)
- **Compute Region:** US (Colab default)
- **Carbon Emitted:** **Negligible** for this scale of fine-tuning. A single Colab T4 run of a 67M-parameter model for a few minutes is in the low single-digit grams of CO₂eq range, well under the threshold worth reporting precisely. The bigger environmental cost in the project is the **zero-shot baseline** (the `llama-3.3-70b-versatile` calls via Groq), which is the recommended classifier and is not done with this model at all.

## Technical Specifications

### Model Architecture and Objective

- **Architecture:** `DistilBertForSequenceClassification` — a 6-layer DistilBERT encoder with a 3-class linear classification head on top of the [CLS] pooled output. `seq_classif_dropout=0.2` on the pooled output before the head.
- **Objective:** Cross-entropy loss on a 3-way single-label classification (`problem_type: "single_label_classification"`).
- **Input:** A single r/CryptoCurrency-style post, tokenized with the DistilBERT uncased tokenizer, truncated to 256 tokens, padded to the longest in-batch sequence.
- **Output:** A 3-way softmax over `{hype, panic, signal}`. The head's `id2label` is `{0: "hype", 1: "panic", 2: "signal"}` and `label2id` is `{hype: 0, panic: 1, signal: 2}`. **Note:** the project repo's `config.py` `LABEL_MAP` matches this order exactly; `classifier.py` verifies the loaded model's `id2label` matches `config.ID_TO_LABEL` at load time and raises if not.
- **Total parameters:** ~67M (standard DistilBERT-base size; 6 layers, 768 hidden dim, 12 attention heads).

### Compute Infrastructure

#### Hardware

- **Training:** Google Colab free tier (NVIDIA T4, 16 GB VRAM)
- **Inference:** CPU is sufficient (the Gradio demo runs on the HF Spaces free CPU tier)

#### Software

- **Python:** 3.10+
- **PyTorch:** 2.x
- **Transformers:** 4.x / 5.x (model was pushed with `transformers_version: 5.10.2` in `config.json`)
- **Other dependencies:** `gradio`, `scikit-learn`, `pandas`, `numpy` — see [`requirements.txt`](https://github.com/isomer04/alphasift/blob/main/requirements.txt) in the project repo

## Citation

If you use this model, please cite the AlphaSift project:

**APA:**

```
isomer007. (2026). AlphaSift: A fine-tuned DistilBERT text classifier for
crypto-community take-quality. Hugging Face Model ID: isomer007/takemeter-distilbert.
https://huggingface.co/isomer007/takemeter-distilbert
```

**BibTeX:**

```bibtex
@misc{alphasift2026takemeter,
  author       = {isomer007},
  title        = {AlphaSift: a fine-tuned DistilBERT text classifier for
                  crypto-community take-quality},
  year         = {2026},
  howpublished = {\url{https://huggingface.co/isomer007/takemeter-distilbert}},
  note         = {Model card. Fine-tuned from \texttt{distilbert-base-uncased}
                  on 153 hand-labeled r/CryptoCurrency posts. Evaluated against
                  a zero-shot \texttt{llama-3.3-70b-versatile} baseline; the
                  baseline outperforms the fine-tuned model on the project's
                  locked 23-post test set (0.783 vs 0.522 accuracy). Project
                  repository: \url{https://github.com/isomer04/alphasift}.}
}
```

**Base model citation (DistilBERT):**

```bibtex
@inproceedings{sanh2019distilbert,
  title  = {DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter},
  author = {Sanh, Victor and Debut, Lysandre and Chaumond, Julien and Wolf, Thomas},
  booktitle = {EMC2 NLP Workshop at NeurIPS 2019},
  year   = {2019}
}
```

## Glossary

- **`signal`** — a post whose claim is backed by load-bearing, checkable evidence (on-chain data, a named mechanism, a concrete historical comparison). Direction (bullish or bearish) does not matter.
- **`hype`** — a bullish post with no real evidence. The community's native term for the equivalent bearish case is "FUD"; this project calls that `panic` for symmetry.
- **`panic`** — a bearish post with no real evidence.
- **`filter`** — a post with no stance at all (news links, neutral questions, memes). Excluded from the 3-way taxonomy. **Not a class of this model**; the model is trained only on `signal` / `hype` / `panic`.
- **FUD** — community shorthand for "fear, uncertainty, and doubt"; maps to `panic` in this taxonomy.
- **Hopium** — community shorthand for groundless bullishness; maps to `hype`.
- **Zero-shot baseline** — the comparison classifier that classifies a post with no task-specific training, using only a system prompt that defines the labels. In this project, the baseline is `llama-3.3-70b-versatile` via the Groq API.
- **Locked test set** — the 23-post stratified test split, seeded with `random_state=42`, reproducible locally via `python evaluate.py`. The "locked" framing is to emphasize that all reported numbers in the project are on the same posts.
- **Run-to-run instability** — the project's finding that re-running the same training notebook on the same data with the same seed produces a different fine-tuned model with a different "broken" class. Symptom of insufficient data per class.

## More Information

- **Project repository (full writeup, code, data, evaluation):** [github.com/isomer04/alphasift](https://github.com/isomer04/alphasift)
- **Project README (recommended starting point — this model card is a summary):** [github.com/isomer04/alphasift#readme](https://github.com/isomer04/alphasift#readme)
- **Label taxonomy:** [`data/taxonomy.md`](https://github.com/isomer04/alphasift/blob/main/data/taxonomy.md)
- **Annotation cheat sheet:** [`docs/collecting.md`](https://github.com/isomer04/alphasift/blob/main/docs/collecting.md)
- **Design rationale:** [`docs/planning.md`](https://github.com/isomer04/alphasift/blob/main/docs/planning.md)
- **Confusion matrix image:** [`results/confusion_matrix.png`](https://github.com/isomer04/alphasift/blob/main/results/confusion_matrix.png)
- **Video walkthrough:** [Loom](https://www.loom.com/share/b1a6d49f7665437db84418751f383359)

## Model Card Authors

isomer007

## Model Card Contact

[isomer007 on Hugging Face](https://huggingface.co/isomer007) — open an issue on the [AlphaSift project repo](https://github.com/isomer04/alphasift/issues) for the fastest response.
