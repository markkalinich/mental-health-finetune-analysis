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

# RooseBERT-scr-uncased

**RooseBERT** is a domain-specific BERT-based language model pre-trained on English political debates and parliamentary speeches. It is designed to capture the distinctive features of political discourse, including domain-specific terminology, implicit argumentation, and strategic communication patterns.

This variant — **scr-uncased** — was trained **from scratch** (SCR) with a **custom uncased WordPiece tokenizer** built from the political debate corpus, giving it a vocabulary better suited to political language than standard BERT. The uncased variant lowercases all input text before tokenization, making it more robust to capitalisation variation across debate transcripts.

> 📄 **Paper:** [RooseBERT: A New Deal For Political Language Modelling](https://arxiv.org/abs/2508.03250)  
> 💻 **GitHub:** [https://github.com/deborahdore/RooseBERT](https://github.com/deborahdore/RooseBERT)

---

## Model Details

| Property | Value |
|---|---|
| Architecture | BERT-base (encoder-only) |
| Training approach | From scratch (SCR) |
| Vocabulary | Custom uncased WordPiece (30,522 tokens) |
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

The SCR approach trains BERT entirely from scratch on domain-specific data, using a custom tokenizer. This allows political terms like *deterrent*, *endorse*, *bureaucrat*, *statutorily*, and *consequential* to be represented as single tokens — whereas standard BERT would split them into multiple sub-tokens. The custom vocabulary shares only ~56% of its tokens with `bert-base-uncased`.

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

The uncased variant is recommended when capitalisation is inconsistent across your data, or when your task does not rely on case distinctions (e.g., proper nouns vs. common nouns).

---

## How to Use

```python
from transformers import AutoTokenizer, AutoModelForMaskedLM

tokenizer = AutoTokenizer.from_pretrained("ddore14/RooseBERT-scr-uncased")
model = AutoModelForMaskedLM.from_pretrained("ddore14/RooseBERT-scr-uncased")
```

For fine-tuning on a downstream classification task:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("ddore14/RooseBERT-scr-uncased")
model = AutoModelForSequenceClassification.from_pretrained(
    "ddore14/RooseBERT-scr-uncased",
    num_labels=2
)

# Recommended fine-tuning hyperparameters (from paper):
# learning_rate ∈ {2e-5, 3e-5, 5e-5}
# batch_size ∈ {8, 16, 32}
# epochs ∈ {2, 3, 4}
```

> **Note:** This model uses an uncased tokenizer. Make sure **not** to pass `do_lower_case=False` when loading — lowercasing is applied automatically.

---

## Evaluation Results

RooseBERT was evaluated across 10 datasets covering 6 downstream tasks. Results below are for **RooseBERT-scr-uncased** (Macro F1 unless noted).

| Task | Dataset | Metric | RooseBERT-scr-uncased | BERT-base-uncased |
|---|---|---|---|---|
| Sentiment Analysis | ParlVote | Accuracy | 0.78 | 0.67 |
| Sentiment Analysis | HanDeSeT | Accuracy | 0.69 | 0.66 |
| Stance Detection | ConVote | Accuracy | 0.75 | 0.73 |
| Stance Detection | AusHansard | Accuracy | 0.59 | 0.55 |
| Arg. Component Det. & Class. | ElecDeb60to20 | Macro F1 | 0.63 | 0.61 |
| Arg. Component Det. & Class. | ArgUNSC | Macro F1 | 0.61 | 0.60 |
| Arg. Relation Pred. & Class. | ElecDeb60to20 | Macro F1 | 0.62 | 0.58 |
| Arg. Relation Pred. & Class. | ArgUNSC | Macro F1 | 0.65 | 0.64 |
| Motion Policy Classification | ParlVote+ | Macro F1 | 0.58 | 0.55 |
| NER | NEREx | Macro F1 | 0.88 | 0.90 |

RooseBERT-scr-uncased outperforms BERT-base-uncased on 8 out of 10 tasks. Results are averaged over 5 runs with different random seeds. For tasks where capitalisation carries semantic weight (e.g., proper noun-heavy NER), the cased variant may perform better.

**Perplexity on held-out political debate data:**

| Model | Perplexity (uncased) |
|---|---|
| BERT-base-uncased | 9.60 |
| ConfliBERT-cont-uncased | 5.00 |
| ConfliBERT-scr-uncased | 4.68 |
| RooseBERT-cont-uncased | **2.71** |
| RooseBERT-scr-uncased | 3.09 |

---

## Available Variants

| Model | Training | Casing | HuggingFace ID |
|---|---|---|---|
| RooseBERT-cont-cased | Continued pre-training | Cased | `ddore14/RooseBERT-cont-cased` |
| RooseBERT-cont-uncased | Continued pre-training | Uncased | `ddore14/RooseBERT-cont-uncased` |
| RooseBERT-scr-cased | From scratch | Cased | `ddore14/RooseBERT-scr-cased` |
| RooseBERT-scr-uncased (this model) | From scratch | Uncased | `ddore14/RooseBERT-scr-uncased` |

**SCR (from scratch)** models use a custom political vocabulary; **CONT (continued pre-training)** models are initialised from the original BERT weights and vocabulary. **Cased** models preserve capitalisation; **uncased** models lowercase all input.

---

## Limitations

- RooseBERT is trained exclusively on **English** political debates. Cross-lingual use is not supported.
- The model may reflect biases present in official political speech, including over-representation of certain geopolitical perspectives.
- Performance on NER tasks does not benefit from domain-specific pre-training when entity categories are general rather than politically specific.
- As an uncased model, it loses information from capitalisation, which may matter for tasks involving proper nouns or acronyms.
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