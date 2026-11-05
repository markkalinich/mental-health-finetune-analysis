---
base_model:
- pritamdeka/S-PubMedBert-MS-MARCO
---
# Healthcare Interoperability Domain-Adapted PubMedBERT

This model is a fine-tuned version of `pritamdeka/S-PubMedBert-MS-MARCO` that has been domain-adapted for healthcare interoperability concepts and terminology.

## Model Details
- **Base model:** PubMedBERT-MS-MARCO
- **Task:** Domain adaptation via masked language modeling (MLM)
- **Training data:** Healthcare interoperability literature corpus
- **Focus areas:** FHIR, HL7, medical terminologies, health information exchange

## Domain-Specific Knowledge

This model has been fine-tuned to better understand healthcare interoperability concepts including:

- Health data exchange standards (FHIR, HL7, DICOM, CCD)
- Terminology systems (SNOMED CT, LOINC, ICD, RxNorm)
- Interoperability frameworks and architectures
- Electronic Health Records (EHR) systems and implementations

## Evaluation Results

Our domain-adapted model shows significant improvements in understanding healthcare interoperability terminology as demonstrated in these fill-mask examples:

| Prompt | Top Predictions |
|--------|----------------|
| "FHIR is a standard for health [MASK] exchange." | "information" (91.3%), "data" (5.6%) |
| "Health information [MASK] is critical for coordinated care." | "exchange" (58.7%), "sharing" (4.6%) |
| "Blockchain technology can improve data [MASK] in healthcare." | "exchange" (21.2%), "quality" (6.0%) |
| "Electronic Health Records require [MASK] standards for sharing information." | "common" (10.1%), "international" (8.0%) |

## Usage

```python
from transformers import AutoModelForMaskedLM, AutoTokenizer

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("adamleeit/pubmedbert-interop-mlm")
model = AutoModelForMaskedLM.from_pretrained("adamleeit/pubmedbert-interop-mlm")

# Example usage
text = "FHIR enables healthcare [MASK] exchange between systems."
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)
token_id = inputs.input_ids[0].tolist().index(tokenizer.mask_token_id)
probs = outputs.logits[0, token_id].softmax(dim=0)
top_tokens = torch.topk(probs, k=5)

for i, (score, token_id) in enumerate(zip(top_tokens.values, top_tokens.indices)):
    print(f"{i+1}. {tokenizer.decode([token_id])}: {score.item():.3f}")
```

## For Embeddings/Sentence Transformers

For generating document embeddings (e.g., for topic modeling), use our sentence-transformer version:

```python
from sentence_transformers import SentenceTransformer

# Load the model
model = SentenceTransformer("adamleeit/pubmedbert-interop-sentence")

# Generate embeddings
embeddings = model.encode(["FHIR enables healthcare information exchange between systems."])
```

## Citation

If you use this model in your research, please cite:
```
@misc{pubmedbert-interop-mlm,
  author = {Lee AM},
  title = {Healthcare Interoperability Domain-Adapted PubMedBERT},
  year = {2025},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/adamleeit/pubmedbert-interop-mlm}}
}
```