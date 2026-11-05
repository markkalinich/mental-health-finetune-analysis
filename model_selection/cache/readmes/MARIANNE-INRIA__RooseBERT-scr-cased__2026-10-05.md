---
language:
  - en
license: apache-2.0
tags:
  - bert
  - political-nlp
  - domain-adaptation
  - argument-mining
  - sentiment-analysis
  - stance-detection
  - named-entity-recognition
  - political-debates
library_name: transformers
pipeline_tag: fill-mask
---

# RooseBERT-scr-cased

**RooseBERT** is a domain-specific BERT-based language model pre-trained on English political debates and parliamentary speeches. It is designed to capture the distinctive features of political discourse, including domain-specific terminology, implicit argumentation, and strategic communication patterns.

This variant — **scr-cased** — was trained **from scratch** (SCR) with a **custom cased WordPiece tokenizer** built from the political debate corpus, giving it a vocabulary better suited to political language than standard BERT.

> 📄 **Paper:** [RooseBERT: A New Deal For Political Language Modelling](https://arxiv.org/abs/2508.03250)  
> 💻 **GitHub:** [https://github.com/deborahdore/RooseBERT](https://github.com/deborahdore/RooseBERT)

---

## Model Details

| Property | Value |
|---|---|
| Architecture | BERT-base (encoder-only) |
| Training approach | From scratch (SCR) |
| Vocabulary | Custom cased WordPiece (28,996 tokens) |
| Hidden size | 768 |
| Attention heads | 12 |
| Hidden layers | 12 |
| Max position embeddings | 512 |
| Training steps | 250K |
| Batch size | 2048 |
| Learning rate | 3e-4 (linear warmup + decay) |
| Training objective | Masked Language Modelling (MLM, 15% mask rate) |
| Hardware | 8× NVIDIA A100 GPUs |
| Frameworks | HuggingFace Transformers, DeepSpeed ZeRO-2, FP16 |

The SCR approach trains BERT entirely from scratch on domain-specific data, using a custom tokenizer. This allows political terms like *deterrent*, *endorse*, *bureaucrat*, *statutorily*, and *consequential* to be represented as single tokens — whereas standard BERT would split them into multiple sub-tokens. The custom vocabulary shares only ~56% of its tokens with `bert-base-cased`.

---

## Training Data

RooseBERT was pre-trained on **11GB** of English political debate transcripts spanning 1919–2025, drawn from:

| Source | Coverage | Size |
|---|---|---|
| African Parliamentary Debates (Ghana & South Africa) | 1999–2024 | 573 MB |
| Australian Parliamentary Debates | 1998–2025 | 1 GB |
| Canadian Parliamentary Debates | 1994–2025 | 1.1 GB |
| European Parliamentary Debates (EUSpeech) | 2007–2015 | 110 MB |
| Irish Parliamentary Debates | 1919–2019 | ~3.4 GB |
| New Zealand Parliamentary Debates (ParlSpeech) | 1987–2019 | 791 MB |
| Scottish Parliamentary Debates (ParlScot) | –2021 | 443 MB |
| UK House of Commons Debates | 1979–2019 | 2.6 GB |
| UN General Debate Corpus (UNGDC) | 1946–2023 | 186 MB |
| UN Security Council Debates (UNSC) | 1992–2023 | 387 MB |
| US Presidential & Primary Debates | 1960–2024 | 16 MB |

All datasets were sourced from authoritative, official political settings. Pre-processing removed hyperlinks, markup tags, and collapsed whitespace.

---

## Intended Use

RooseBERT is intended as a **base model for fine-tuning** on downstream NLP tasks related to political discourse analysis. It is especially well-suited for:

- **Sentiment Analysis** of parliamentary speeches and debates
- **Stance Detection** (support/oppose classification)
- **Argument Component Detection and Classification** (claims and premises)
- **Argument Relation Prediction and Classification** (support/attack/no-relation)
- **Motion Policy Classification**
- **Named Entity Recognition** in political texts

---

## How to Use

```python
from transformers import AutoTokenizer, AutoModelForMaskedLM

tokenizer = AutoTokenizer.from_pretrained("ddore14/RooseBERT-scr-cased")
model = AutoModelForMaskedLM.from_pretrained("ddore14/RooseBERT-scr-cased")
```

For fine-tuning on a downstream classification task:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer

tokenizer = AutoTokenizer.from_pretrained("ddore14/RooseBERT-scr-cased")
model = AutoModelForSequenceClassification.from_pretrained(
    "ddore14/RooseBERT-scr-cased",
    num_labels=2
)

# Recommended fine-tuning hyperparameters (from paper):
# learning_rate ∈ {2e-5, 3e-5, 5e-5}
# batch_size ∈ {8, 16, 32}
# epochs ∈ {2, 3, 4}
```

---

## Evaluation Results

RooseBERT was evaluated across 10 datasets covering 6 downstream tasks. Results below are for **RooseBERT-scr-cased** (Macro F1 unless noted).

| Task | Dataset | Metric | RooseBERT-scr-cased | BERT-base-cased |
|---|---|---|---|---|
| Sentiment Analysis | ParlVote | Accuracy | 0.79 | 0.69 |
| Sentiment Analysis | HanDeSeT | Accuracy | 0.71 | 0.67 |
| Stance Detection | ConVote | Accuracy | 0.75 | 0.72 |
| Stance Detection | AusHansard | Accuracy | 0.60 | 0.54 |
| Arg. Component Det. & Class. | ElecDeb60to20 | Macro F1 | 0.63 | 0.61 |
| Arg. Component Det. & Class. | ArgUNSC | Macro F1 | 0.61 | 0.61 |
| Arg. Relation Pred. & Class. | ElecDeb60to20 | Macro F1 | 0.63 | 0.58 |
| Arg. Relation Pred. & Class. | ArgUNSC | Macro F1 | 0.72 | 0.57 |
| Motion Policy Classification | ParlVote+ | Macro F1 | 0.62 | 0.54 |
| NER | NEREx | Macro F1 | 0.88 | 0.92 |

RooseBERT outperforms BERT on 9 out of 10 tasks, with improvements ranging from **4% to 15%** on classification tasks. NER performance is comparable, as the NEREx dataset uses general (non-political) entity categories. Results are averaged over 5 runs with different random seeds.

**Perplexity on held-out political debate data:**

| Model | Perplexity (cased) |
|---|---|
| BERT-base-cased | 22.11 |
| ConfliBERT-cont-cased | 4.37 |
| RooseBERT-cont-cased | **2.61** |
| RooseBERT-scr-cased | 2.80 |

---

## Available Variants

| Model | HuggingFace ID |
|---|---|
| RooseBERT-scr-cased (this model) | `ddore14/RooseBERT-scr-cased` |
| RooseBERT-scr-uncased | `ddore14/RooseBERT-scr-uncased` |
| RooseBERT-cont-cased | `ddore14/RooseBERT-cont-cased` |
| RooseBERT-cont-uncased | `ddore14/RooseBERT-cont-uncased` |

**SCR (from scratch)** models use a custom political vocabulary; **CONT (continued pre-training)** models are initialised from the original BERT weights and vocabulary.

---

## Limitations

- RooseBERT is trained exclusively on **English** political debates. Cross-lingual use is not supported.
- The model may reflect biases present in official political speech, including over-representation of certain geopolitical perspectives.
- Performance on NER tasks does not benefit from domain-specific pre-training when entity categories are general rather than politically specific.
- As with all encoder-only models, RooseBERT is best suited to classification and labelling tasks rather than generation.

---

## Citation

If you use RooseBERT in your research, please cite:

```bibtex
@article{dore2025roosebert,
  title={RooseBERT: A New Deal For Political Language Modelling},
  author={Dore, Deborah and Cabrio, Elena and Villata, Serena},
  journal={arXiv preprint arXiv:2508.03250},
  year={2025}
}
```

---

## Acknowledgements

This work was supported by the French government through the **3IA Côte d'Azur** programme (ANR-23-IACL-0001). Computing resources were provided by **GENCI at IDRIS** (grant 2026-AD011016047R1) on the Jean Zay supercomputer.