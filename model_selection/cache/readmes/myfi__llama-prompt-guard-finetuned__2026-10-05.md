---
language:
- en
license: mit
tags:
- prompt-injection
- security
- classification
- fine-tuned
- myfi
datasets:
- custom
metrics:
- accuracy
- precision
- recall
- f1
- auc
---

# Fine-tuned Llama-Prompt-Guard-2-86M

This is a fine-tuned version of the Meta Llama-Prompt-Guard-2-86M model for prompt injection detection, developed by the MyFi team.

## Model Description

- **Base Model**: meta-llama/Llama-Prompt-Guard-2-86M
- **Task**: Binary classification (benign vs malicious prompts)
- **Architecture**: mDeBERTa-base with custom classifier head
- **Fine-tuning**: Custom dataset with balanced benign/malicious samples
- **Organization**: MyFi

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model_name = "myfi/llama-prompt-guard-finetuned"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Classify text
text = "How do I hack a computer?"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
outputs = model(**inputs)

# Apply temperature scaling (recommended: 3.0)
temperature = 3.0
scaled_logits = outputs.logits / temperature
probabilities = torch.softmax(scaled_logits, dim=-1)

# Get prediction
benign_prob = probabilities[0][0].item()
malicious_prob = probabilities[0][1].item()
prediction_result = "MALICIOUS" if malicious_prob > 0.5 else "BENIGN"

print(f"Prediction: {prediction_result}")
print(f"Benign Probability: {benign_prob:.4f}")
print(f"Malicious Probability: {malicious_prob:.4f}")
```

## Training Details

- **Dataset**: Custom dataset with balanced benign/malicious samples
- **Training Method**: Fine-tuning with custom loss function
- **Temperature Scaling**: Recommended temperature = 3.0
- **Classification Threshold**: Default = 0.5
- **Organization**: MyFi

## Performance

The model is designed to detect prompt injection attempts and malicious queries while allowing legitimate requests to pass through.

## Limitations

- May have false positives/negatives on edge cases
- Performance depends on the quality and distribution of training data
- Should be used as part of a broader security strategy

## License

This model is licensed under the MIT License.

## Organization

This model is maintained by [MyFi](https://huggingface.co/myfi) - a company focused on AI & ML solutions.

## Citation

If you use this model, please cite the original Llama-Prompt-Guard-2-86M paper and mention that this is a fine-tuned version by MyFi.
