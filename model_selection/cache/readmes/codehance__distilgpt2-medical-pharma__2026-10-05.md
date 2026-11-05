---
language: en
license: mit
tags:
- medical
- pharmaceutical
- autocomplete
- distillation
- gpt2
datasets:
- medmcqa
metrics:
- perplexity
model-index:
- name: codehance/distilgpt2-medical-pharma
  results:
  - task:
      type: text-generation
    dataset:
      name: Medical Q&A
      type: medmcqa
    metrics:
    - name: Perplexity
      type: perplexity
      value: 44.07
---

# DistilGPT-2 Medical Pharmaceutical Autocomplete

## Model Description

This is a distilled GPT-2 model fine-tuned for pharmaceutical autocomplete. It suggests drug names and medical terminology based on clinical context.

**Key Features:**
- 34% smaller than base fine-tuned model (81,912,576 parameters)
- 45% faster inference (347.9ms per generation)
- Specialized in pharmaceutical vocabulary

## Training Process

### Stage 1: Fine-Tuning
- Base model: GPT-2 (124M parameters)
- Dataset: Medical Q&A (medmcqa) - 4,500 training examples
- Training: 3 epochs
- Final perplexity: 23.61

### Stage 2: Knowledge Distillation
- Teacher: Fine-tuned GPT-2
- Student: DistilGPT-2
- Training: 2 epochs
- Compression: 34.2% size reduction

## Performance

| Metric | Value |
|--------|-------|
| Parameters | 81,912,576 |
| Perplexity | 44.07 |
| Inference Speed | 347.9ms |
| Quality Retained | 53.6% |

## Usage
```python
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load model and tokenizer
model = GPT2LMHeadModel.from_pretrained("codehance/distilgpt2-medical-pharma")
tokenizer = GPT2Tokenizer.from_pretrained("codehance/distilgpt2-medical-pharma")

# Generate pharmaceutical suggestions
prompt = "The patient should take"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_length=30, num_return_sequences=3)

for output in outputs:
    print(tokenizer.decode(output, skip_special_tokens=True))
```

## Intended Use

**Primary Use Cases:**
- Pharmaceutical autocomplete systems
- Medical documentation assistance
- Clinical note-taking tools
- Drug name suggestion

**Limitations:**
- Not a substitute for medical advice
- May suggest incorrect drugs - always verify with qualified professionals
- Trained on medical exam questions, not real prescriptions
- English language only

## Training Data

- **Source:** MedMCQA dataset (Indian medical entrance exam questions)
- **Size:** 4,500 training examples
- **Content:** Medical questions with pharmaceutical terminology

## Ethical Considerations

⚠️ **Important:** This model is for autocomplete assistance only. It should NOT be used as the sole basis for medical decisions. Always verify suggestions with qualified healthcare professionals.

## Model Card Authors

Created as part of a pharmaceutical autocomplete system tutorial demonstrating transfer learning, fine-tuning, and knowledge distillation.

## Citation
```bibtex
@misc{distilgpt2-medical-pharma,
  author = {codehance},
  title = {DistilGPT-2 Medical Pharmaceutical Autocomplete},
  year = {2025},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/codehance/distilgpt2-medical-pharma}}
}
```
