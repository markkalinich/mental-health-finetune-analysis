---
language:
  - en
  - zh
license: apache-2.0
library_name: transformers
tags:
  - sentiment-analysis
  - text-classification
  - xlm-roberta
  - webnovel
  - cross-lingual
  - reader-response
  - digital-humanities
  - computational-literary-studies
datasets:
  - custom
base_model: cardiffnlp/twitter-xlm-roberta-base-sentiment
pipeline_tag: text-classification
model-index:
  - name: sentiment-webnovel-comments-xlmr-en-zh
    results:
      - task:
          type: text-classification
          name: Sentiment Analysis
        metrics:
          - name: Accuracy
            type: accuracy
            value: 0.7481
            verified: false
          - name: F1 Macro
            type: f1
            value: 0.7329
            verified: false
          - name: Cohen's Quadratic Kappa
            type: cohen_kappa
            value: 0.6339
            verified: false
          - name: Spearman rho (valence)
            type: spearmanr
            value: 0.665
            verified: false
---

# sentiment-webnovel-comments-xlmr-en-zh

A bilingual (English + Chinese) sentiment classifier for webnovel reader comments (sourced from Qidian and WebNovel and manually annotated), finetuned from [cardiffnlp/twitter-xlm-roberta-base-sentiment](https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment).

Classifies comments into three categories (**negative**, **neutral**, **positive**) and produces continuous valence scores via softmax probabilities: `valence = p(positive) - p(negative)`, yielding a score in [-1, +1].

## Intended Use

This model was developed for a computational literary studies project investigating emotional links between story content and reader responses in bilingual (EN-ZH) webnovel corpora. It is designed to score millions of reader comments with a continuous sentiment valence, which serves as a dependent variable in a Generalized Additive Mixed Model (GAMM) predicting comment sentiment from story paragraph sentiment (see the article https://doi.org/10.26083/tuda-7994).

**Primary use case:** Batch inference on informal reader comments from platforms like Goodreads, Qidian, and Webnovel.com.

**Why a single bilingual model?** Using the same model for both languages ensures measurement invariance, i.e. systematic differences in valence scores reflect genuine cross-lingual sentiment differences rather than model-specific biases. This is critical for the downstream GAMM, where language is a factor.

### Out-of-Scope Uses

- General-purpose sentiment analysis (the model is tuned for informal reader commentary, not product reviews, news, or social media)
- Languages other than English and Chinese
- High-stakes decision-making (moderation, content filtering, etc.)

## Training Details

### Data

1,580 manually annotated bilingual webnovel comments (779 EN, 801 ZH) sampled from Qidian and Webnovel.com. Comments were independently annotated by two annotators into three sentiment categories, who later discussed to reach a final curated version of the annotations.

| Class | EN | ZH | Total |
|---|---|---|---|
| Negative | 373 | 395 | 768 |
| Neutral | 216 | 241 | 457 |
| Positive | 190 | 165 | 355 |
| **Total** | **779** | **801** | **1,580** |

Preprocessing: stripped `[fn=N]` footnote markers, removed 4 duplicate texts.

Source: Yu, Z., Pianzola, F., & Tatar, E. (2024). *Qidian-Webnovel Corpus 110 (Version V2)* [dataset]. DataverseNL. https://doi.org/10.34894/GQXX3K

### Procedure

- **Base model:** `cardiffnlp/twitter-xlm-roberta-base-sentiment` -- an XLM-RoBERTa model pretrained on ~198M multilingual tweets with sentiment labels. Selected because it won a multi-model comparison on both paragraph-level and comment-level sentiment tasks (see [Model Selection](#model-selection--overall-5-fold-cv) below).
- **Cross-validation:** 5-fold stratified CV (stratified by `language x label` to preserve proportions). Each fold trains on 1,264 comments and evaluates on 316.
- **Early stopping:** Patience = 3 on `eval_macro_f1`, with `load_best_model_at_end=True`. Best epochs per fold: [4, 4, 3, 3, 4]; median = 4.
- **Final model:** Trained on all 1,580 comments for 4 epochs (the median best epoch from CV), with no evaluation set.
- **Loss:** Class-weighted cross-entropy (`sklearn.utils.class_weight.compute_class_weight("balanced")`), compensating for class imbalance.

### Hyperparameters

| Parameter | Value |
|---|---|
| Learning rate | 3e-5 |
| Batch size | 32 |
| Max sequence length | 256 tokens |
| Weight decay | 0.01 |
| Warmup ratio | 0.1 |
| Precision | fp16 |
| Optimizer | AdamW |
| Seed | 42 |
| Training epochs (final) | 4 |

### Infrastructure

Trained on the [Habrok HPC cluster](https://wiki.hpc.rug.nl/habrok/) at the University of Groningen (1x NVIDIA A100 GPU). Total training time for the final model: ~17 seconds.

## Evaluation

### Metrics

- **Accuracy / F1 macro / F1 weighted:** Standard classification metrics on the three-class task.
- **Cohen's quadratic weighted kappa (kappa_q):** Ordinal agreement between gold and predicted labels. Penalises distant misclassifications (negative <-> positive) more heavily than adjacent ones (negative <-> neutral).
- **Spearman rho (valence-label):** Rank correlation between the continuous valence score `p(pos) - p(neg)` and ordinal gold labels (negative = -1, neutral = 0, positive = +1). This is the primary evaluation metric for the downstream GAMM, where continuous valence (not discrete class) is used as the dependent variable.

### Model Selection -- Overall (5-Fold CV)

Three XLM-RoBERTa base models were compared, each with human-only training data and with synthetic data augmentation (+1,580 resampled LLM-generated comments added to training folds; evaluation always on held-out human annotations). All used the same CV protocol. These selection runs used lr=2e-5, maxlen=128, and checkpoint selection by `eval_loss`; the final published model uses tuned hyperparameters (see [Hyperparameter Tuning](#hyperparameter-tuning) below).

| Model | Base | Data | Acc | F1m | kappa_q | rho |
|---|---|---|---|---|---|---|
| xlmr_multi | twitter-xlm-roberta-base-sentiment-multilingual | human | .710 | .700 | .588 | .631 |
| xlmr_multi | | +synth | .690 | .684 | .584 | .637 |
| **xlmr_en** | **twitter-xlm-roberta-base-sentiment** | **human** | **.723** | **.714** | **.603** | **.646** |
| xlmr_en | | +synth | .694 | .687 | .582 | .655 |
| xlmr_base | xlm-roberta-base | human | .702 | .691 | .552 | .577 |
| xlmr_base | | +synth | .692 | .682 | .565 | .590 |

### Model Selection -- English (5-Fold CV)

| Model | Data | Acc | F1m | kappa_q | rho |
|---|---|---|---|---|---|
| xlmr_multi | human | .732 | .726 | .668 | .692 |
| xlmr_multi | +synth | .702 | .702 | .642 | .696 |
| **xlmr_en** | **human** | **.745** | **.739** | **.675** | **.706** |
| xlmr_en | +synth | .716 | .714 | .646 | .717 |
| xlmr_base | human | .692 | .686 | .562 | .578 |
| xlmr_base | +synth | .693 | .689 | .584 | .602 |

### Model Selection -- Chinese (5-Fold CV)

| Model | Data | Acc | F1m | kappa_q | rho |
|---|---|---|---|---|---|
| xlmr_multi | human | .689 | .670 | .502 | .562 |
| xlmr_multi | +synth | .678 | .654 | .514 | .574 |
| **xlmr_en** | **human** | **.702** | **.686** | **.526** | **.579** |
| xlmr_en | +synth | .672 | .651 | .506 | .590 |
| xlmr_base | human | .712 | .693 | .541 | .577 |
| xlmr_base | +synth | .690 | .669 | .541 | .582 |

`xlmr_en` (human only) was selected as the base model. It leads on accuracy, F1, and kappa_q overall and for both languages, and on rho overall. Synthetic data augmentation yielded marginal rho improvements (+.006 to +.013) at the cost of consistent accuracy and F1 losses (-.010 to -.029). These rho gains fall within fold-level SD, making them statistically indistinguishable from noise. The human-only model was therefore preferred.

### Hyperparameter Tuning

After model selection, hyperparameters were tuned by comparing the original configuration (lr=2e-5, maxlen=128, checkpoint selection by `eval_loss`) against an alternative (lr=3e-5, maxlen=256, checkpoint selection by `eval_macro_f1`). Both configurations used the same 5-fold CV protocol on the 1,580 cleaned comments.

| Config | lr | maxlen | Selection | F1m | kappa_q | rho | EN rho | ZH rho |
|---|---|---|---|---|---|---|---|---|
| Initial | 2e-5 | 128 | eval_loss | .714 | .603 | .646 | .706 | .579 |
| **Tuned** | **3e-5** | **256** | **macro_f1** | **.733** | **.634** | **.665** | **.723** | **.603** |
| Delta | | | | +.019 | +.031 | +.019 | +.017 | +.024 |

The improvement is consistent across all metrics and both languages. The maxlen increase from 128 to 256 tokens likely accounts for most of the gain: some webnovel comments exceed 128 tokens and were being truncated. Note that the checkpoint selection metric also changed (eval_loss -> macro_f1), so the gain is not attributable to lr/maxlen alone. Dropout was kept at the model default (~0.1); increasing it to 0.2 was tested but yielded no meaningful improvement.

### Detailed Results (xlmr_en, tuned hyperparameters, 5-Fold CV)

Metrics computed on concatenated held-out predictions across all folds (i.e., every sample is scored exactly once by a model that never saw it during training).

| Subset | N | Acc | F1m | kappa_q | rho |
|---|---|---|---|---|---|
| **Overall** | **1,580** | **.748** | **.733** | **.634** | **.665** |
| English | 779 | .775 | .767 | .715 | .723 |
| Chinese | 801 | .722 | .691 | .541 | .603 |
| *Zero-shot baseline* | *1,580* | *.679* | *.646* | *.541* | *.614* |
| *  English* | *779* | *.675* | *.653* | *.602* | *.664* |
| *  Chinese* | *801* | *.683* | *.633* | *.473* | *.565* |
| *Majority baseline* | *1,580* | *.486* | *--* | *--* | *--* |

**Per-class F1:**

| Class | N | F1 | EN F1 | ZH F1 |
|---|---|---|---|---|
| Negative | 768 | .800 | .815 | .787 |
| Neutral | 457 | .689 | .690 | .688 |
| Positive | 355 | .710 | .796 | .597 |

**Fold-level means +- SD:**

| Metric | Mean +- SD |
|---|---|
| Accuracy | .748 +- .023 |
| F1 macro | .732 +- .024 |
| F1 weighted | .747 +- .023 |
| Cohen kappa_q | .633 +- .041 |
| Spearman rho | .670 +- .029 |

**Improvement over zero-shot:** Delta Acc = +.069, Delta F1m = +.087, Delta kappa_q = +.093, Delta rho = +.051.

### Synthetic Data Augmentation

To test whether additional training data could improve performance, 1,580 synthetic comments were generated by an LLM and resampled to match the human annotation class distribution (negative: 768, neutral: 457, positive: 355). Neutral was oversampled with replacement (385 available synthetic neutrals -> 457); negative and positive were downsampled. Synthetic data was added to training folds only; evaluation was always on held-out human annotations.

Result: synthetic augmentation consistently improved rho by small margins (+.006 to +.013) but degraded accuracy (-.010 to -.029) and F1 macro (-.009 to -.027) across all three base models. The rho gains fall within fold-level variability and are not statistically significant. The classification degradation suggests the synthetic data introduces noise into the decision boundary.

### Known Limitations

- **ZH-EN gap:** Chinese rho (.603) is consistently lower than English rho (.723), reflecting the base model's EN-centric pretraining. This gap (~.12) persists across all evaluated models and hyperparameter configurations and is not bridged by synthetic data augmentation.
- **Small training set:** 1,580 samples limits what finetuning can achieve; the modest improvement over zero-shot (+.051 rho) suggests diminishing returns without more data. Synthetic augmentation with 1,580 LLM-generated comments did not meaningfully close this gap.
- **Domain specificity:** Trained on webnovel reader comments only. Performance on other comment types (e.g., academic reviews, product reviews) is untested.

## How to Use

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "fpianz/sentiment-webnovel-comments-xlmr-en-zh"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
model.eval()

texts = [
    "This chapter was absolutely incredible, I cried at the end",
    "meh, nothing really happened",
    "This was a decent chapter but I expected more from the protagonist",
]

inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True, max_length=256)

with torch.no_grad():
    outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=-1)

# Discrete labels
labels = ["negative", "neutral", "positive"]
predictions = [labels[p] for p in probs.argmax(dim=-1)]

# Continuous valence: p(positive) - p(negative), range [-1, +1]
valence = (probs[:, 2] - probs[:, 0]).tolist()

for text, pred, val in zip(texts, predictions, valence):
    print(f"{pred:>8s} (valence={val:+.3f})  {text[:60]}")
```

**Note:** Use `use_fast=False` for the tokenizer to avoid potential tiktoken conversion issues with XLM-RoBERTa.

## Label Mapping

| ID | Label |
|---|---|
| 0 | negative |
| 1 | neutral |
| 2 | positive |

## Training Code

The training script (`finetune_comments_cv.py`) and SLURM runner (`run_finetune_comments.sh`) are available in the project repository. Key implementation details:

- Custom `WeightedTrainer` extending HuggingFace `Trainer` with class-weighted cross-entropy loss
- Stratified k-fold CV with `language x label` stratification key
- Early stopping via `EarlyStoppingCallback(patience=3)` monitoring `eval_macro_f1`
- Final model epoch count determined by median best epoch across CV folds

## Citation

If you use this model, please cite:

```bibtex
@misc{pianzla2026webnovel-comments,
  title={sentiment-webnovel-comments-xlmr-en-zh: A Bilingual Sentiment Classifier for Webnovel Reader Comments},
  author={Pianzola, Federico, and Yu, Ze},
  year={2026},
  url={https://huggingface.co/fpianz/sentiment-webnovel-comments-xlmr-en-zh}
}
```

## Acknowledgements

Computational resources provided by the [Center for Information Technology](https://www.rug.nl/society-business/centre-for-information-technology/) of the University of Groningen (Habrok HPC cluster).
