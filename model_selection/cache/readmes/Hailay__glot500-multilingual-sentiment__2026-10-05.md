---
license: apache-2.0
base_model: cis-lmu/glot500-base
language: multilingual
library_name: transformers
pipeline_tag: text-classification
tags:
  - sentiment-analysis
  - text-classification
  - xlm-roberta
  - multilingual
  - social-media
metrics:
  - accuracy
  - f1
model-index:
  - name: glot500-multilingual-sentiment
    results:
      - task:
          type: text-classification
          name: Sentiment Analysis
        dataset:
          name: VEXMLM multilingual tweet sentiment (custom, 3-class)
          type: custom
        metrics:
          - type: accuracy
            value: 0.6624
            name: Test Accuracy
          - type: f1
            value: 0.6620
            name: Test F1 (weighted)
---

# glot500-multilingual-sentiment (VEXMLM)

A 3-class (positive / negative / neutral) sentiment classifier fine-tuned from
[`cis-lmu/glot500-base`](https://huggingface.co/cis-lmu/glot500-base) on a multilingual
collection of short social-media posts.

## Motivation

Sentiment analysis resources are concentrated in a handful of high-resource languages.
This model targets the gap for **lower-resource and typologically diverse languages**
that appear in the training data (see *Dataset* below) by starting from Glot500 — an
XLM-RoBERTa model pretrained on ~500 languages — and fine-tuning it on a multilingual
sentiment-labeled tweet corpus, so a single model can be applied across languages rather
than requiring one model per language.

## Supported task

- **Task**: single-label text classification (sentiment analysis)
- **Labels**: `positive`, `negative`, `neutral`
- **Input**: short, informal social-media text (tweets), up to 512 subword tokens
- **Languages**: multilingual, inherited from the Glot500 pretraining coverage (~500
  languages). The fine-tuning corpus itself does not carry an explicit per-example
  language tag. A Unicode-script analysis over all 107,549 rows (train+dev+test) found:
  Latin script in 88.18% of rows, Ethiopic/Ge'ez script in 8.81%, Arabic script in
  7.91% (rows can contain more than one script if code-mixed; a general-purpose
  language detector, `langdetect`, was also tried but proved unreliable on this short,
  code-mixed text and is not reported). Manual inspection of samples additionally
  suggests: English / Nigerian Pidgin, Swahili, Portuguese, Yoruba, Igbo, and Twi within
  the Latin-script majority; Arabic (incl. Moroccan Darija) within the Arabic-script
  rows; and Amharic within the Ethiopic-script rows (Tigrinya was not clearly identified
  in the samples checked, despite sharing the same script as Amharic). Treat this as a
  lower bound, not an exhaustive or verified list.

## Base model & fine-tuning approach

- **Base model**: [`cis-lmu/glot500-base`](https://huggingface.co/cis-lmu/glot500-base)
  (XLM-RoBERTa architecture, 12 layers, hidden size 768, ~395M backbone params,
  401,145-token SentencePiece vocabulary, pretrained on the
  [Glot500](https://arxiv.org/abs/2305.12182) corpus).
- **Approach**: standard supervised fine-tuning of a sequence-classification head
  (`XLMRobertaForSequenceClassification`, 3-way softmax) on top of the pretrained
  encoder, using the Hugging Face `Trainer`.

## Training details

**Dataset** (custom, not currently published on the Hub):

| Split | Examples | File |
|---|---|---|
| Train | 63,685 | `multilingual_train.tsv` |
| Validation | 13,653 | `multilingual_dev.tsv` |
| Test | 30,211 | `multilingual_test.tsv` |

Each row has three columns: `ID`, `tweet` (input text), `label` (`positive` /
`negative` / `neutral`).

**Source / provenance**: not documented. These files carry no accompanying README,
citation, or license in the project, and were intentionally excluded from git version
control (kept as local, gitignored data), so no commit history records where they came
from. The only trace of origin is a one-off `scp` transfer of a local directory
(`EXLM_R`) onto this cluster — i.e. the corpus was assembled/curated elsewhere before
arriving in this project. **If you know the original source of this corpus, please
update this section with the correct citation/link** — the language mix and 3-class
labeling scheme resemble the shape of published African-language multilingual sentiment
benchmarks, but that has not been confirmed and should not be assumed.

**Script composition** (Unicode-range analysis over all 107,549 rows, train+dev+test
combined; a row can contain more than one script):

| Script | Rows | % of dataset |
|---|---|---|
| Latin | 94,842 | 88.18% |
| Ethiopic / Ge'ez (Amharic / Tigrinya) | 9,478 | 8.81% |
| Arabic | 8,502 | 7.91% |
| Cyrillic, CJK, Devanagari | 8 total | ~0.00% (noise) |

**Configuration**:

| Hyperparameter | Value |
|---|---|
| Learning rate | 2e-5 |
| Batch size (per device) | 16 |
| Epochs | 3 |
| Max sequence length | 512 (padded/truncated) |
| Weight decay | 0.01 |
| Optimizer / schedule | HF `Trainer` default (AdamW, linear decay) |
| Model selection | best checkpoint by weighted F1 on the validation split |

**Steps**: 11,943 total optimization steps for the final training segment (3 epochs ×
3,981 steps/epoch at batch size 16).

**Hardware / environment**: SLURM-managed GPU cluster; final training segment ran on a
single NVIDIA A100 80GB GPU. `transformers==4.53.2`, `torch==2.5.1+cu121`.

**Reproducibility note**: this run was preempted partway through on a shared/preemptible
queue and resumed from an intermediate checkpoint (~2 epochs into an earlier 3×A100 run
of the same configuration). Because the installed `torch` version blocks deserializing
legacy optimizer checkpoints (`torch.load` restriction, CVE-2025-32434), only the model
weights were restored from that checkpoint (via `safetensors`) — optimizer/scheduler
state and the LR schedule were **not** preserved across the resume, i.e. the final 3
epochs reported above were trained fresh on top of warm-started weights rather than
being a bit-exact continuation.

## Evaluation

**Methodology**: the fine-tuned model was evaluated on the held-out `multilingual_test.tsv`
split (30,211 examples) through **two independent pipelines**:

1. `trainer.evaluate()` invoked automatically at the end of the training script
   (`finetune_M_model.py`).
2. A standalone batched-inference script (`evaluation.py`) that reloads the saved model
   from disk and scores it independently.

Both pipelines produced matching results (accuracy 0.6624 in both cases), which cross-
validates that the saved checkpoint, tokenizer, and label mapping (`id2label`) are
internally consistent.

**Test results**:

| Metric | Weighted | Macro |
|---|---|---|
| Accuracy | **66.24%** | — |
| Precision | 66.20% | 66.25% |
| Recall | 66.24% | 66.30% |
| F1 | 66.20% | 66.25% |

## Usage

### Installation

```bash
pip install transformers torch safetensors
```

### Loading the model

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "Hailay/glot500-multilingual-sentiment"  # update after upload
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
```

### Example inference

```python
import torch

texts = [
    "I love this, it made my day!",
    "This is the worst experience I've ever had.",
]

inputs = tokenizer(texts, padding=True, truncation=True, max_length=512, return_tensors="pt")
with torch.no_grad():
    logits = model(**inputs).logits

probs = torch.softmax(logits, dim=-1)
preds = torch.argmax(probs, dim=-1)

for text, pred, prob in zip(texts, preds, probs):
    label = model.config.id2label[pred.item()]
    print(f"{text!r} -> {label} (confidence {prob[pred].item():.2f})")
```

## Repository structure

This model card ships inside the Hugging Face model repo alongside the model weights.
The broader training project (VEXMLM) that produced this model is organized as:

```
VEXMLM/
├── finetune_M_model.py       # training script
├── evaluation.py             # standalone evaluation script (2nd, independent eval path)
├── fm.sh / eval.sh           # SLURM job scripts (training / evaluation)
├── multilingual_{train,dev,test}.tsv   # dataset splits (not part of the HF upload)
├── glot500finetuned_v2/      # <- this directory is what gets uploaded to the Hub
│   ├── config.json
│   ├── model.safetensors
│   ├── tokenizer.json
│   ├── sentencepiece.bpe.model
│   ├── tokenizer_config.json
│   ├── special_tokens_map.json
│   └── README.md             # this file
└── eval_results/
    └── scores.txt            # raw evaluation output (local artifact, not uploaded)
```

## Limitations & future improvements

- **Moderate accuracy (66%)**: 3-class sentiment on informal, code-mixed, multilingual
  social-media text is a hard task; there is a visible gap between validation accuracy
  (~73%) and held-out test accuracy (66%), suggesting some distribution shift between
  the validation and test splits worth investigating further.
- **No verified per-example language labels**: language coverage is inferred, not
  measured — per-language breakdown of accuracy is not currently available.
- **Weak on Tigrinya specifically**: ad hoc testing found a clearly negative Tigrinya
  sentence misclassified as positive with high confidence. This is consistent with the
  Ethiopic-script portion of the fine-tuning data appearing to be predominantly Amharic
  rather than Tigrinya (see the Dataset section above) — treat Tigrinya predictions as
  unreliable pending further evaluation.
- **Optimizer-state resume gap**: as noted above, the released checkpoint's final
  training segment did not have access to the prior segment's optimizer/scheduler
  state; a from-scratch, uninterrupted run (or an environment with `torch>=2.6`) may
  produce different results.
- **Future work**: per-language evaluation breakdown, hyperparameter tuning
  (learning-rate schedule, longer training), and augmenting the training set for
  underrepresented languages.

## Citation

This model was produced as part of the following work. **If you use this model,
please cite:**

> **Expanding the Lexicon of Ge'ez Based African Languages: A Comparative Study of Amharic and Tigrinya**
> Hailay Kidu Teklehaymanot†, Debela Desalegn Yadeta‡, Wolfgang Nejdl†
> † L3S Research Center, Leibniz University Hannover, Germany — {teklehaymanot, nejdl}@l3s.de
> ‡ Addis Ababa University, Ethiopia — debela.desalegn@aau.edu.et
> Accepted at **LM4UC @ IJCAI 2026**.

```bibtex
@inproceedings{teklehaymanot2026geez,
  title     = {Expanding the Lexicon of Ge'ez Based African Languages: A Comparative Study of Amharic and Tigrinya},
  author    = {Teklehaymanot, Hailay Kidu and Yadeta, Debela Desalegn and Nejdl, Wolfgang},
  booktitle = {Proceedings of LM4UC @ IJCAI 2026},
  year      = {2026},
  note      = {To appear}
}
```

### Base model acknowledgement

This model fine-tunes Glot500 and would not exist without it. Please also credit:

```bibtex
@inproceedings{imanigooghari2023glot500,
  title     = {Glot500: Scaling Multilingual Corpora and Language Models to 500 Languages},
  author    = {ImaniGooghari, Ayyoob and Lin, Peiqin and Kargaran, Amir Hossein and Severini, Silvia and Jalili Sabet, Masoud and Kassner, Nora and Ma, Chunlan and Schmid, Helmut and Martins, Andr{\'e} F. T. and Yvon, Fran{\c{c}}ois and Sch{\"u}tze, Hinrich},
  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},
  year      = {2023},
  url       = {https://arxiv.org/abs/2305.12182}
}
```
