---
language: en
license: mit
tags:
- mental-health
- sentiment-analysis
- pytorch
- transformers
- distilbert
datasets:
- custom-mental-health-dataset
pipeline_tag: text-classification
widget:
- text: I am feeling great today and everything is going well!
  example_title: Positive Mental State
- text: I don't see the point in anything anymore, everything feels hopeless
  example_title: Mental Health Risk
- text: Just having a regular day at work, nothing special
  example_title: Neutral State
model-index:
- name: MindTrack Mental Health Analyzer
  results:
  - task:
      type: text-classification
      name: Mental Health Risk Detection
    metrics:
    - type: Accuracy
      value: 97.13%
      name: Accuracy
    - type: f1
      value: 97.13%
      name: F1 Score
metrics:
- f1
- accuracy
base_model:
- distilbert/distilbert-base-uncased
---

# MindTrack: Mental Health Sentiment Analyzer 🧠

## Model Description

MindTrack is a fine-tuned DistilBERT model specifically trained for mental health sentiment analysis and risk detection in text content. The model can classify text into two categories:

- **Normal**: Indicates healthy mental state or neutral content
- **Risk Detected**: Indicates potential mental health concerns that may require attention

## Model Details

- **Model Type**: DistilBERT for Sequence Classification
- **Training Data**: Curated mental health dataset with balanced samples
- **Languages**: English
- **License**: MIT

## Performance

The model achieves the following performance on the validation set:

- **Overall Accuracy**: 97.13%
- **Overall F1-Score**: 97.13%
- **Normal Class F1**: 97.16%
- **Risk Class F1**: 97.10%

## Dataset

The model was trained on a perfectly balanced dataset.

- **Total Samples**: 50,000
- **Training Samples**: 40,000 (80%)
- **Validation Samples**: 10,000 (20%)
- **Class Balance**: 50/50
  
## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model_id = "techhy/mindtrack-mental-health-analyzer"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id)

# Example usage
text = "I am feeling great today!"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)

with torch.no_grad():
    outputs = model(**inputs)
    probabilities = torch.softmax(outputs.logits, dim=-1)
    predicted_class = torch.argmax(probabilities, dim=-1).item()
    confidence = probabilities[0][predicted_class].item()

labels = {0: "Normal", 1: "Risk Detected"}
print(f"Prediction: {labels[predicted_class]} (Confidence: {confidence:.2%})")
```

## Intended Use

This model is designed to assist in identifying potential mental health concerns in text content. **Important**: This tool should not replace professional medical advice or diagnosis. Always consult qualified healthcare professionals for mental health issues.

## Limitations

- Trained primarily on English text
- May not capture cultural nuances in mental health expression
- Performance may vary on text significantly different from training data
- Should be used as a screening tool, not for final diagnosis

## Training Data

The model was trained on a carefully curated dataset of mental health-related text, including:
- Social media posts (anonymized)
- Mental health support forum discussions
- Clinical text samples (anonymized)
- Balanced representation of risk and normal states

## Ethical Considerations

- **Privacy**: No personal information was used in training
- **Bias**: Efforts were made to reduce bias, but some may remain
- **Responsible Use**: Should be used to help people, not to discriminate
- **Professional Guidance**: Always recommend professional help for mental health concerns

## Citation

If you use this model in your research or applications, please cite:

```
@misc{mindtrack2024,
  title={MindTrack: Mental Health Sentiment Analyzer},
  author={Soham},
  year={2024},
  url={https://huggingface.co/techhy/mindtrack-mental-health-analyzer}
}
```

## Contact

For questions or issues, please open an issue on the [GitHub repository](https://github.com/Soham-droid-pixel/Mind_Track_Project).