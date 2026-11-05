---
language: en
license: mit
tags:
- biomedical
- relation-extraction
- pubmedbert
- named-entity-recognition
datasets:
- chemprot
- bc5cdr
- gad
- biored
- ddi
metrics:
- f1
- precision
- recall
model-index:
- name: PubMedBERT Relation Extraction
  results:
  - task:
      type: relation-extraction
      name: Biomedical Relation Extraction
    metrics:
    - type: f1
      value: 0.7347
      name: F1 Macro
---

# PubMedBERT for Biomedical Relation Extraction

Fine-tuned [PubMedBERT](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract) for multi-class relation extraction in biomedical text.

## Model Description

This model extracts semantic relations between biomedical entities (chemicals, diseases, genes, proteins) from scientific literature.

**Base Model:** `microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract`

**Training Data:** chemprot, bc5cdr, gad, biored, ddi

**Relation Types (9):**
- `activates`
- `inhibits`
- `converts`
- `causes`
- `treats`
- `associated_with`
- `interacts_with`
- `located_in`
- `NO_RELATION`

## Performance

| Metric | Value |
|--------|------:|
| F1 Macro | 0.7347 |
| Accuracy | 75.3% |

### Per-Class F1 Scores

| Relation | F1 | Support |
|----------|---:|--------:|
| interacts_with | 0.85 | 1,304 |
| inhibits | 0.84 | 2,704 |
| activates | 0.83 | 3,412 |
| converts | 0.82 | 884 |
| associated_with | 0.81 | 1,769 |
| causes | 0.81 | 6,760 |
| NO_RELATION | 0.63 | 6,760 |
| treats | 0.28 | 678 |

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model_name = "your-username/pubmedbert-relation-extraction"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Add entity markers
special_tokens = {"additional_special_tokens": ["[E1]", "[/E1]", "[E2]", "[/E2]"]}
tokenizer.add_special_tokens(special_tokens)
model.resize_token_embeddings(len(tokenizer))

# Example: Extract relation between aspirin and pain
text = "[E1]Aspirin[/E1] reduces [E2]pain[/E2] in patients."

inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=256)
outputs = model(**inputs)
probs = torch.softmax(outputs.logits, dim=-1)
predicted_class = torch.argmax(probs, dim=-1).item()

print(f"Predicted relation: {model.config.id2label[predicted_class]}")
print(f"Confidence: {probs[0][predicted_class].item():.3f}")
```

## Input Format

Text must contain entity markers `[E1]`, `[/E1]`, `[E2]`, `[/E2]` around the two entities:

```
[E1]Entity1[/E1] ... context ... [E2]Entity2[/E2]
```

## Training Details

- **Optimizer:** AdamW
- **Learning Rate:** 2e-5
- **Batch Size:** 16
- **Epochs:** 15 (early stopping)
- **Max Length:** 256 tokens
- **Loss:** Weighted CrossEntropy

## Limitations

- `treats` relation has low F1 (0.28) due to limited training data
- Best performance on Chemical↔Gene/Protein and Disease relations
- Requires entity markers in input text
- Trained on English biomedical abstracts

## Citation

```bibtex
@misc{pubmedbert-relation-extraction,
  author = {Your Name},
  title = {PubMedBERT for Biomedical Relation Extraction},
  year = {2026},
  publisher = {HuggingFace},
  howpublished = {\url{https://huggingface.co/your-username/pubmedbert-relation-extraction}}
}
```

## Acknowledgments

- Base model: [PubMedBERT](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract)
- Datasets: ChemProt, BC5CDR, GAD, BioRED, DDI Corpus
