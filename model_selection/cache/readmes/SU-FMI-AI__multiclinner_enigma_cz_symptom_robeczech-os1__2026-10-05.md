---
license: apache-2.0
language:
- cs
library_name: transformers
pipeline_tag: token-classification
base_model: ufal/robeczech-base
tags:
- token-classification
- named-entity-recognition
- ner
- clinical
- biomedical
- medical
- czech
- multiclinai
- iberlef
datasets:
- MultiClinAI
metrics:
- precision
- recall
- f1
model-index:
- name: multiclinner_enigma_cz_symptom_robeczech-os1
  results:
  - task:
      type: token-classification
      name: Named Entity Recognition
    dataset:
      name: MultiClinAI Czech (SYMPTOM)
      type: MultiClinAI
    metrics:
    - type: precision
      name: Strict Precision
      value: 0.6242
    - type: recall
      name: Strict Recall
      value: 0.5908
    - type: f1
      name: Strict F1
      value: 0.6070
    - type: precision
      name: Char-level Precision
      value: 0.7482
    - type: recall
      name: Char-level Recall
      value: 0.7083
    - type: f1
      name: Char-level F1
      value: 0.7277
---

# multiclinner_enigma_cz_symptom_robeczech-os1

Czech clinical Named Entity Recognition model for the **SYMPTOM** entity
type, fine-tuned from [`ufal/robeczech-base`](https://huggingface.co/ufal/robeczech-base) on the
Czech portion of the [MultiClinAI 2026 IberLEF shared task](https://temu.bsc.es/MultiClinAI/).
Developed by **Team Enigma** at the Faculty of Mathematics and Informatics,
Sofia University.

## Summary

| | |
|---|---|
| Task | Token classification (BIO), single entity type |
| Entity type | `SYMPTOM` (patient symptoms and clinical findings) |
| Language | Czech (`cs`) |
| Base model | [`ufal/robeczech-base`](https://huggingface.co/ufal/robeczech-base) |
| Architecture | Transformer (softmax) |
| Augmentation | Morphological synonyms + 1x oversample of entity-bearing docs |
| Training data | MultiClinAI Czech `train + dev` combined (1,258 documents) plus augmentation |
| Test F1 (strict) | **0.6070** (char F1 **0.7277**) |

## Quick start

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

repo = "SU-FMI-AI/multiclinner_enigma_cz_symptom_robeczech-os1"

tokenizer = AutoTokenizer.from_pretrained(repo)
model = AutoModelForTokenClassification.from_pretrained(repo)

ner = pipeline(
    "token-classification",
    model=model,
    tokenizer=tokenizer,
    aggregation_strategy="simple",
)

text = "Pacient byl přijat s hypertenzí a podstoupil koronarografii."
for span in ner(text):
    print(span)
```

Each predicted span is a dictionary with keys `entity_group`,
`score`, `word`, `start`, `end`.


## Label set

The model predicts a single entity type using the BIO tagging scheme:

| ID | Label | Meaning |
|---:|---|---|
| 0 | `O` | outside any entity |
| 1 | `B-SYMPTOM` | beginning of a `SYMPTOM` mention |
| 2 | `I-SYMPTOM` | inside a `SYMPTOM` mention |

## Intended use

- Extracting `SYMPTOM` mentions from **Czech clinical text** (discharge
  summaries, case reports, medical records).
- Building block for ensembles (this model was deployed as part of an
  ensemble in the original submission).
- A starting point for further fine-tuning on related Czech biomedical
  corpora.

## Out-of-scope use

- Other languages. Although the XLM-RoBERTa based variants share a
  multilingual encoder, the classification head was only trained on Czech.
- Other domains. The model was not exposed to non-clinical text, social
  media or layperson descriptions.
- Clinical decision making. This is a research artifact. **Do not** use it
  as the sole input to any clinical decision.

## Training data

- **Source.** [MultiClinAI Czech NER](https://zenodo.org/records/19334278): 1,006 train documents
  and 252 dev documents per entity type in BRAT standoff format, derived
  from the DisTEMIST, SympTEMIST and MedProcNER corpora translated and
  annotation-projected to Czech. For the final submission models the gold
  `train + dev` sets are merged into a single training partition (no
  held-out validation).
- **Augmentation.** **Morphological synonym replacement + oversampling.** Morphological augmentation as described above, with one additional copy of every training document that contains at least one entity annotation, added before the augmented documents are appended. This increases the relative weight of gold supervision over the synthetic data.
- **Tokenisation.** SentencePiece tokenizer inherited from the base model.

## Training procedure

| Hyperparameter | Value |
|---|---|
| Base model | `ufal/robeczech-base` |
| Head | SOFTMAX |
| Optimiser | AdamW |
| Learning rate | 2e-5 |
| Batch size | 64 |
| Epochs | 10 |
| Max sequence length | 512 |
| Input granularity | Sentence-level |
| Warmup ratio | 0.1 |
| Weight decay | 0.01 |
| Seed | 42 |
| Mixed precision | fp16 (CUDA) |

Token classification head: backbone hidden states are projected through a linear layer to BIO logits and decoded greedily (argmax per token).

## Evaluation

### Held-out development set

Best dev-set entity-level F1 observed during development: **0.669**.

### MultiClinAI Czech, official blind test set

Run name in the official MultiClinAI ranking: `robeczech-os1_cz_symptom`.

| Metric | Strict | Character-level |
|---|---:|---:|
| Precision | 0.6242 | 0.7482 |
| Recall    | 0.5908 | 0.7083 |
| F1        | **0.6070** | **0.7277** |


Strict matching requires the predicted span to exactly match a gold span
(same start, end, and type). Character-level matching gives partial credit
for overlapping spans.

## Related models

Other models for the same entity type:

- [`SU-FMI-AI/multiclinner_enigma_cz_symptom_xlmr-crf`](https://huggingface.co/SU-FMI-AI/multiclinner_enigma_cz_symptom_xlmr-crf): xlm-roberta-base, Morphological synonyms (curated + Wikidata), CRF head, test F1 = 0.5960.
- [`SU-FMI-AI/multiclinner_enigma_cz_symptom_xlmr-os1`](https://huggingface.co/SU-FMI-AI/multiclinner_enigma_cz_symptom_xlmr-os1): xlm-roberta-base, Morphological synonyms + 1x oversample of entity-bearing docs, SOFTMAX head, test F1 = 0.5815.


## License

Released under the [apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)
license. Base-model and dataset licenses apply to their respective
artifacts.

## Code and resources

Training code, augmentation pipeline, ablation log and evaluation scripts
are available in the project's GitHub repository: <https://github.com/TeogopK/MultiClinAI-Czech>.
