---
language: en
tags:
- suicide-detection
- mental-health
- bert
- text-classification
- pytorch
- safetensors
license: mit
datasets:
- suicide-watch
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: BERT Suicide Risk Detection
  results:
  - task:
      type: text-classification
      name: Suicide Risk Detection
    dataset:
      type: suicide-watch
      name: Suicide Detection Dataset
    metrics:
    - type: accuracy
      value: 0.9772
      name: Accuracy
    - type: f1
      value: 0.9772
      name: F1 Score
    - type: precision
      value: 0.9773
      name: Precision
    - type: recall
      value: 0.9772
      name: Recall
---

# BERT Suicide Risk Detection Model

## Model Description

This is a fine-tuned BERT model for suicide risk detection in text. The model can classify text as either "suicide" (indicating potential suicide risk) or "non-suicide" (indicating no immediate risk).

## Model Performance

- **Accuracy**: 97.72%
- **F1 Score**: 97.72%
- **Precision**: 97.73%
- **Recall**: 97.72%

## Intended Use

This model is designed to assist mental health professionals and support systems in identifying potentially at-risk individuals. It should **NOT** be used as a standalone diagnostic tool.

## Usage

```python
from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Load model and tokenizer
model_name = "Akashpaul123/bert-suicide-detection"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)

# Example usage
text = "I'm feeling really down and don't know if I can keep going."
inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True, padding=True)

with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    
suicide_prob = predictions[0][1].item()
non_suicide_prob = predictions[0][0].item()

print(f"Suicide probability: {suicide_prob:.4f}")
print(f"Non-suicide probability: {non_suicide_prob:.4f}")
```

## Training Data

The model was trained on the Suicide Detection dataset containing 232,074 samples with balanced classes (50% suicide, 50% non-suicide).

## Training Details

- **Model**: bert-base-uncased
- **Epochs**: 5
- **Batch Size**: 32
- **Learning Rate**: 2e-5
- **Max Length**: 512
- **Optimizer**: AdamW
- **Hardware**: A100 GPU

## Ethical Considerations

⚠️ **Important Notice**: This model is a tool to assist in suicide risk assessment and should not replace professional mental health evaluation. Always consult with qualified mental health professionals for proper assessment and intervention.

### Limitations

- The model may produce false positives or false negatives
- It should be used as part of a comprehensive mental health assessment system
- Regular monitoring and validation are recommended
- The model's performance may vary across different populations and contexts

## License

This model is released under the MIT License.

## Citation

If you use this model in your research, please cite:

```bibtex
@model{akashpaul2024bert-suicide-detection,
  title={BERT Suicide Risk Detection Model},
  author={Akash Paul},
  year={2024},
  url={https://huggingface.co/Akashpaul123/bert-suicide-detection}
}
```

## Contact

For questions or issues, please contact through the Hugging Face model page.
