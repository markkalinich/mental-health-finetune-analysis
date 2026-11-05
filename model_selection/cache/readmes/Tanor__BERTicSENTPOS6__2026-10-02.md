---
base_model: classla/bcms-bertic
tags:
- serbian
- sentiment-analysis
- wordnet
- sentiwordnet
- lexicon-induction
metrics:
- f1
model-index:
- name: BERTicSENTPOS6
  results: []
language:
- sr
library_name: transformers
pipeline_tag: text-classification
base_model_relation: finetune
widget:
- text: koji oseća radost i zadovoljstvo
  example_title: Illustrative Serbian gloss
license: apache-2.0
---

# BERTicSENTPOS6

This is a **positive-polarity classifier for Serbian WordNet synset glosses**, fine-tuned from the BERTić model family. It is a component of the **S5 sentiment-lexicon construction method** described in:

Saša Petalinkar, Ranka M. Stanković, and Milica Ikonić Nešić (2025). **Comparative analysis of methods for creating a sentiment lexicon of the Serbian WordNet.** *The Electronic Library*, 43(4), 547–577. [Paper and DOI](https://doi.org/10.1108/EL-08-2024-0253).

[Companion code and sentiment lexicons](https://github.com/sasa5linkar/Serbian-WordNet-Sentiment-Lexicon-Analysis) · [Paired classifier](https://huggingface.co/Tanor/BERTicSENTNEG6) · [Original base model](https://huggingface.co/classla/bcms-bertic)

## Model identity and task

| Field | Value |
|---|---|
| Model ID | `Tanor/BERTicSENTPOS6` |
| Architecture | `ElectraForSequenceClassification` |
| Original base model | [`classla/bcms-bertic`](https://huggingface.co/classla/bcms-bertic) |
| Input | A Serbian synset gloss, representing one lexical meaning |
| Target | Positive vs non-positive polarity |
| Dataset expansion iteration | **6** (`T6`) |
| Label 0 | `NON-POSITIVE` |
| Label 1 | `POSITIVE` |
| Derived lexicon family | **S5** |
| Paired classifier, same iteration | [`Tanor/BERTicSENTNEG6`](https://huggingface.co/Tanor/BERTicSENTNEG6) |

The preparation notebook initializes the BERTić family from `classla/bcms-bertic`. The linked training script can resume from the corresponding `Tanor/BERTicSENT*` repository. The metadata identifies the original base model; it does not imply that every run started from that base checkpoint.

A non-positive label is the complement of the target class. It does not by itself mean that the gloss has the opposite polarity. A separate classifier handles that polarity.

## Training data and construction method

The paper constructs polarity-labeled synsets from Serbian WordNet, starting from curated positive, negative, and objective seed sets and expanding through semantic relations. The initial sets reported in the paper contain 149 positive, 219 negative, and 19,475 objective synsets. Polarity-preserving relations expand the corresponding set; antonymy contributes to the opposite polarity. The selected datasets are `T0`, `T2`, `T4`, and `T6`, after zero, two, four, and six expansion iterations.

This checkpoint is associated with **T6 and the POS classification task**. Its numerical suffix is a dataset-expansion iteration, not an epoch count or a lexicon identifier.

The [training script](https://github.com/sasa5linkar/Serbian-WordNet-Sentiment-Lexicon-Analysis/blob/833582dbbf561a902fc5b872248db12bf529b3d9/trainBERTic.py) reads `Sysnet` from `X_train_UPPOS6.csv` and the target `POS` from `y_train_UPPOS6.csv`, replaces missing text with an empty string, and creates a stratified validation subset of **10% of that training CSV**, with `random_state=42`. The `UP` inputs are the non-lemmatized gloss variant in the [dataset-generation script](https://github.com/sasa5linkar/Serbian-WordNet-Sentiment-Lexicon-Analysis/blob/833582dbbf561a902fc5b872248db12bf529b3d9/create_sets.py).

The paper and code snapshot have different split descriptions: the paper describes an 80/10/10 split for neural models, while the scripts split existing training CSV files and `create_sets.py` leaves the initial split size at the library default. Exact checkpoint-specific sample assignments are not supplied in the public revision. The `train_sets/` files referenced by the scripts are absent from that revision. Reconstructing the experiment requires the relevant lexical resources and saved preparation/split information; the paper's proportions alone do not establish this checkpoint's split.

## Use in sentiment lexicon S5

For each iteration, the POS model estimates positive-class probability `p_pos` and the NEG model estimates negative-class probability `p_neg`. The [lexicon-building code](https://github.com/sasa5linkar/Serbian-WordNet-Sentiment-Lexicon-Analysis/blob/833582dbbf561a902fc5b872248db12bf529b3d9/sentiwordnet_calculator.py) combines them as:

```text
POS = p_pos * (1 - p_neg)
NEG = p_neg * (1 - p_pos)
OBJ = 1 - POS - NEG
```

It averages each score across the four iteration-specific pairs. A single checkpoint is one component of this construction; its two class probabilities are not the final three lexicon scores.

| Iteration | POS classifier | NEG classifier |
|---|---|---|
| 0 | [BERTicSENTPOS0](https://huggingface.co/Tanor/BERTicSENTPOS0) | [BERTicSENTNEG0](https://huggingface.co/Tanor/BERTicSENTNEG0) |
| 2 | [BERTicSENTPOS2](https://huggingface.co/Tanor/BERTicSENTPOS2) | [BERTicSENTNEG2](https://huggingface.co/Tanor/BERTicSENTNEG2) |
| 4 | [BERTicSENTPOS4](https://huggingface.co/Tanor/BERTicSENTPOS4) | [BERTicSENTNEG4](https://huggingface.co/Tanor/BERTicSENTNEG4) |
| 6 | [BERTicSENTPOS6](https://huggingface.co/Tanor/BERTicSENTPOS6) | [BERTicSENTNEG6](https://huggingface.co/Tanor/BERTicSENTNEG6) |

## Usage

This example reads one gloss and returns both class probabilities. It pins the model to the weights revision present before the documentation update.

```python
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

MODEL_ID = "Tanor/BERTicSENTPOS6"
WEIGHTS_REVISION = "3cddd4da67b409e888c0e06b58c2b9d6c86db2ef"
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, revision=WEIGHTS_REVISION)
model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_ID, revision=WEIGHTS_REVISION
)
model.eval()

# An illustrative gloss, not a benchmark item or a claimed prediction.
inputs = tokenizer(
    "koji oseća radost i zadovoljstvo",
    return_tensors="pt", truncation=True, max_length=300,
)
with torch.inference_mode():
    probabilities = model(**inputs).logits.softmax(dim=-1)[0]
scores = {model.config.id2label[i]: float(p) for i, p in enumerate(probabilities)}
print(scores)
```

The model uses standard PyTorch/Transformers sequence-classification classes, without custom remote code. The example requires PyTorch and Transformers. Where a Trainer record is available below, it includes software versions from the original run. No example prediction or benchmark score was generated for this documentation update.

## Evaluation and provenance

### Archived test report

The companion repository contains an [evaluation report for BERTic, POS, T6](https://github.com/sasa5linkar/Serbian-WordNet-Sentiment-Lexicon-Analysis/blob/833582dbbf561a902fc5b872248db12bf529b3d9/reports/BERTic2/report_UPPOS6.csv.txt). It is preserved below, with class 0 = `NON-POSITIVE` and class 1 = `POSITIVE`. Metric values retain the source's rounding; support values are sample counts. The confusion matrix uses that class order.

```text
[[4432    6]
 [  49   24]]

              precision    recall  f1-score   support

           0       0.99      1.00      0.99      4438
           1       0.80      0.33      0.47        73

    accuracy                           0.99      4511
   macro avg       0.89      0.66      0.73      4511
weighted avg       0.99      0.99      0.99      4511
```

This is an archived experiment artifact, not a new evaluation. The report does not record a model-weight SHA, so its exact correspondence to the currently hosted weights has not been independently re-established. These binary-classification metrics are separate from evaluation of the derived lexicon and from sentiment evaluation of full sentences.

### Preserved Trainer record

The following validation summary and training log are retained from the [previous model card](https://huggingface.co/Tanor/BERTicSENTPOS6/blob/3cddd4da67b409e888c0e06b58c2b9d6c86db2ef/README.md), without recomputing them. The recorded F1 is a training-validation metric, separate from the archived test report above and from lexicon or sentence-level sentiment evaluation. The source training code uses binary F1 for target label 1 when `eval="f1"` is selected.

- Loss: 0.0839
- F1: 0.375

#### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 64
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 32

#### Training results

| Training Loss | Epoch  | Step | Validation Loss | F1     |
|:-------------:|:------:|:----:|:---------------:|:------:|
| No log        | 0.9843 | 47   | 0.0589          | 0.4068 |
| No log        | 1.9895 | 95   | 0.0592          | 0.3590 |
| No log        | 2.9948 | 143  | 0.0663          | 0.4783 |
| No log        | 4.0    | 191  | 0.0839          | 0.375  |


#### Framework versions

- Transformers 4.40.1
- Pytorch 2.2.2
- Datasets 2.19.0
- Tokenizers 0.19.1

The Trainer record and the linked source script are separate provenance sources. In particular, the recorded optimizer may differ from the script's `adafactor` setting; the historical record is retained without asserting that the linked script reproduces that exact run.

## Settings in the archived training source

These settings describe the linked code revision, not a replacement for the per-run Trainer record.

| Setting | Source-code value |
|---|---|
| Maximum tokenized input length | 300 |
| Learning rate | 2e-5 |
| Training batch size per device | 64 |
| Evaluation batch size per device | 16 |
| Gradient accumulation | 4 steps |
| Optimizer | Adafactor |
| Weight decay | 0.01 |
| Validation split seed | 42 |
| Evaluation and saving | Each epoch |
| Early stopping patience | 3 evaluation calls |
| Epoch budget in experiment notebooks | Up to 32 |

The paper reports early-stopping patience of 3. The linked family script also uses 3.

## Intended use and limitations

- Intended for research on polarity of Serbian WordNet meanings and construction or analysis of Serbian sentiment lexicons.
- Training inputs are glosses. Performance on reviews, news, social media, and documents requires separate evaluation; this checkpoint is not documented as a general sentence-sentiment benchmark model.
- Class imbalance is visible in the archived report. Read accuracy and weighted averages alongside target-class precision, recall, F1, and support.
- Labels depend on seed selection and semantic-relation expansion. Polysemy, domain-specific polarity, and propagation errors can affect predictions. English-to-Serbian alignment alone does not establish polarity in Serbian.
- Softmax outputs are model scores; probability calibration is not established by this card.
- The model performs no sense selection for a word in context. Applying the lexicon to text requires a separate choice or aggregation of meanings.

## License

This fine-tuned model is distributed under **Apache License 2.0** (`apache-2.0`), matching the license declared for its original base model, [classla/bcms-bertic](https://huggingface.co/classla/bcms-bertic/blob/5db9755d6152ec6403c0201223e4848bd1b98a48/README.md). Read the full [LICENSE](LICENSE) and [NOTICE](NOTICE) for attribution and the description of the fine-tuning changes.

The license permits use, modification, and distribution, including commercial use, subject to its terms. When redistributing, include the license, retain applicable attribution and notices, and mark modifications. It does not require every derivative work to use the same license.

### Scope and training-resource permissions

The model license covers the model distribution and accompanying documentation within the rights the licensors can grant. External lexical resources, training datasets, and companion code retain their own terms.

An earlier description of Serbian WordNet reports **CC BY-NC** terms for the downloadable resource ([Developing and Maintaining a WordNet: Procedures and Tools, 2014](https://aclanthology.org/W14-0108.pdf)). The terms of the exact SrpWN release used for this fine-tuning, and any separate permission covering it, have not been verified in this documentation update. That historical statement alone does not determine the license of the trained weights. This model-license declaration does not grant rights to redistribute SrpWN or establish that every third-party permission for a particular use has been cleared. The remaining check is to identify the training release and record the applicable permission from its rights holders. See also [Creative Commons guidance on AI training](https://creativecommons.org/faq/#artificial-intelligence-and-cc-licenses).

### License declaration history

The `apache-2.0` declaration, full license text, and attribution were added on 23 September 2026.

## Citation

When using this model family or the resulting lexicon-construction method, cite the paper and record the model ID and revision used.

```bibtex
@article{petalinkar2025sentimentlexicon,
  author = {Petalinkar, Saša and Stanković, Ranka M. and Ikonić Nešić, Milica},
  title = {Comparative analysis of methods for creating a sentiment lexicon of the Serbian WordNet},
  journal = {The Electronic Library},
  year = {2025},
  volume = {43},
  number = {4},
  pages = {547--577},
  doi = {10.1108/EL-08-2024-0253},
  url = {https://doi.org/10.1108/EL-08-2024-0253}
}
```

## Version and documentation sources

- Weights/configuration revision documented here: [`3cddd4da67b409e888c0e06b58c2b9d6c86db2ef`](https://huggingface.co/Tanor/BERTicSENTPOS6/tree/3cddd4da67b409e888c0e06b58c2b9d6c86db2ef). This pins the hosted checkpoint; it does not prove which weights produced every table in the paper.
- Companion code revision: [`833582dbbf561a902fc5b872248db12bf529b3d9`](https://github.com/sasa5linkar/Serbian-WordNet-Sentiment-Lexicon-Analysis/tree/833582dbbf561a902fc5b872248db12bf529b3d9).
- BERTić initialization is recorded in [Prepare and load models.ipynb](https://github.com/sasa5linkar/Serbian-WordNet-Sentiment-Lexicon-Analysis/blob/833582dbbf561a902fc5b872248db12bf529b3d9/Prepare%20and%20load%20models.ipynb); GPT2-Orao and Jerteh-355 initialization is recorded in their training scripts.
- Documentation expanded on 23 September 2026 using the paper, model configuration, repository source, archived evaluation report, and any pre-existing Trainer record. Weights, tokenizer files, and model configuration were not changed by this documentation update.
