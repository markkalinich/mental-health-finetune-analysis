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

# RooseBERT-cont-uncased

**RooseBERT** is a domain-specific BERT-based language model pre-trained on English political debates and parliamentary speeches. It is designed to capture the distinctive features of political discourse, including domain-specific terminology, implicit argumentation, and strategic communication patterns.

This variant — **cont-uncased** — was trained via **continued pre-training** (CONT) of `bert-base-uncased`, initialising from its original weights and vocabulary and training for additional steps on the political debate corpus. This allows the model to leverage BERT's general language understanding while adapting its representations to the political domain. The uncased variant lowercases all input text before tokenization, making it more robust to capitalisation variation across debate transcripts.

> 📄 **Paper:** [RooseBERT: A New Deal For Political Language Modelling](https://arxiv.org/abs/2508.03250)  
> 💻 **GitHub:** [https://github.com/deborahdore/RooseBERT](https://github.com/deborahdore/RooseBERT)

---

## Model Details

| Property | Value |
|---|---|
| Architecture | BERT-base (encoder-only) |
| Training approach | Continued pre-training (CONT) from `bert-base-uncased` |
| Vocabulary | BERT standard uncased WordPiece (30,523 tokens) |
| Hidden size | 768 |
| Attention heads | 12 |
| Hidden layers | 12 |
| Max position embeddings | 512 |
| Training steps | 150K |
| Batch size | 2048 |
| Learning rate | 3e-4 (linear warmup + decay) |
| Warmup steps | 10,000 |
| Weight decay | 0.01 |
| Training objective | Masked Language Modelling (MLM, 15% mask rate) |
| Hardware | 8× NVIDIA A100 GPUs |
| Training time | ~24 hours |
| Frameworks | HuggingFace Transformers, DeepSpeed ZeRO-2, FP16 |

The CONT approach initialises from `bert-base-uncased`'s pre-trained weights and continues training on the political debate corpus, retaining BERT's standard vocabulary. This means the model benefits from BERT's broad linguistic knowledge while adapting its contextual representations to the political domain — without the overhead of training a new tokenizer or initialising weights from random. CONT models require fewer training steps (150K vs. 250K for SCR) and can be trained in approximately 24 hours on 8× A100 GPUs.

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

The CONT-uncased variant is a good default choice when compatibility with the standard BERT vocabulary is important (e.g., when using pre-trained task-specific heads or embeddings), or when capitalisation distinctions are not critical for your task. It achieves the best overall perplexity among all uncased RooseBERT variants.

---

## How to Use

```python
from transformers import AutoTokenizer, AutoModelForMaskedLM

tokenizer = AutoTokenizer.from_pretrained("ddore14/RooseBERT-cont-uncased")
model = AutoModelForMaskedLM.from_pretrained("ddore14/RooseBERT-cont-uncased")
```

For fine-tuning on a downstream classification task:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("ddore14/RooseBERT-cont-uncased")
model = AutoModelForSequenceClassification.from_pretrained(
    "ddore14/RooseBERT-cont-uncased",
    num_labels=2
)

# Recommended fine-tuning hyperparameters (from paper):
# learning_rate ∈ {2e-5, 3e-5, 5e-5}
# batch_size ∈ {8, 16, 32}
# epochs ∈ {2, 3, 4}
```

> **Note:** This model uses an uncased tokenizer. Lowercasing is applied automatically — do not pass `do_lower_case=False`.

---

## Evaluation Results

RooseBERT was evaluated across 10 datasets covering 6 downstream tasks. Results below are for **RooseBERT-cont-uncased** (Macro F1 unless noted).

| Task | Dataset | Metric | RooseBERT-cont-uncased | BERT-base-uncased |
|---|---|---|---|---|
| Sentiment Analysis | ParlVote | Accuracy | 0.80 | 0.67 |
| Sentiment Analysis | HanDeSeT | Accuracy | 0.71 | 0.66 |
| Stance Detection | ConVote | Accuracy | 0.77 | 0.73 |
| Stance Detection | AusHansard | Accuracy | 0.60 | 0.55 |
| Arg. Component Det. & Class. | ElecDeb60to20 | Macro F1 | 0.62 | 0.61 |
| Arg. Component Det. & Class. | ArgUNSC | Macro F1 | 0.61 | 0.60 |
| Arg. Relation Pred. & Class. | ElecDeb60to20 | Macro F1 | 0.61 | 0.58 |
| Arg. Relation Pred. & Class. | ArgUNSC | Macro F1 | 0.70 | 0.64 |
| Motion Policy Classification | ParlVote+ | Macro F1 | 0.63 | 0.55 |
| NER | NEREx | Macro F1 | 0.90 | 0.90 |

RooseBERT-cont-uncased outperforms BERT-base-uncased on 9 out of 10 tasks, with the strongest gains on sentiment analysis (+13% on ParlVote) and motion policy classification (+8%). Results are averaged over 5 runs with different random seeds.

**Perplexity on held-out political debate data:**

| Model | Perplexity (uncased) |
|---|---|
| BERT-base-uncased | 9.60 |
| ConfliBERT-cont-uncased | 5.00 |
| ConfliBERT-scr-uncased | 4.68 |
| RooseBERT-scr-uncased | 3.09 |
| RooseBERT-cont-uncased | **2.71** |

RooseBERT-cont-uncased achieves the lowest perplexity of all uncased models, indicating the strongest adaptation to the political debate domain.

---

## Available Variants

| Model | Training | Casing | HuggingFace ID |
|---|---|---|---|
| RooseBERT-cont-cased | Continued pre-training | Cased | `ddore14/RooseBERT-cont-cased` |
| RooseBERT-cont-uncased (this model) | Continued pre-training | Uncased | `ddore14/RooseBERT-cont-uncased` |
| RooseBERT-scr-cased | From scratch | Cased | `ddore14/RooseBERT-scr-cased` |
| RooseBERT-scr-uncased | From scratch | Uncased | `ddore14/RooseBERT-scr-uncased` |

**CONT (continued pre-training)** models inherit BERT's standard vocabulary and pre-trained weights, requiring fewer training steps. **SCR (from scratch)** models use a custom political vocabulary that encodes domain-specific terms as single tokens. **Cased** models preserve capitalisation; **uncased** models lowercase all input.

---

## Limitations

- RooseBERT is trained exclusively on **English** political debates. Cross-lingual use is not supported.
- The model may reflect biases present in official political speech, including over-representation of certain geopolitical perspectives.
- Because CONT models retain BERT's standard vocabulary, domain-specific political terms may still be split into sub-tokens (e.g., *deterrent* → `['de', '##ter', '##rent']`). For richer domain vocabulary encoding, consider the SCR variants.
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