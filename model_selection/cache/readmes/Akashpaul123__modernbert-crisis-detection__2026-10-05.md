---
language: en
tags:
- mental-health
- crisis-detection
- modernbert
- healthcare
- nlp
- pytorch
- text-classification
library_name: transformers
pipeline_tag: text-classification
datasets:
- synthetic-mental-health-crisis
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: modernbert-crisis-detection
  results:
  - task:
      type: text-classification
      name: Crisis Detection
    dataset:
      type: synthetic-mental-health-crisis
      name: Mental Health Crisis Detection
    metrics:
    - type: accuracy
      value: 1.0000
      name: Accuracy
    - type: precision
      value: 1.0000
      name: Precision
    - type: recall
      value: 1.0000
      name: Recall (Crisis Detection Rate)
    - type: f1
      value: 1.0000
      name: F1-Score
    - type: false_positive_rate
      value: 0.0000
      name: False Positive Rate
---

# ModernBERT Crisis Detection

## Model Description

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) specifically optimized for **mental health crisis detection**. It achieves **perfect performance** on synthetic crisis detection data with 100% accuracy while maintaining zero false positives.

## Key Features

- ✅ **100% Crisis Detection Rate** (Target: ≥95%)
- ✅ **0% False Positive Rate** (Target: <10%)
- ✅ **8,192 token context window** (full ModernBERT capacity)
- ✅ **Real-time inference** optimized for production use
- ✅ **Clinical-grade metrics** for healthcare applications



### Quick Start

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("Akashpaul123/modernbert-crisis-detection")
model = AutoModelForSequenceClassification.from_pretrained(
    "Akashpaul123/modernbert-crisis-detection",
    torch_dtype=torch.bfloat16,
    attn_implementation="eager"  # For compatibility
)

# Example usage
def detect_crisis(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=8192)
    
    # Remove token_type_ids (ModernBERT doesn't use them)
    if 'token_type_ids' in inputs:
        del inputs['token_type_ids']
    
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.softmax(outputs.logits, dim=-1)
        crisis_prob = probs[0][1].item()
    
    return {
        'crisis_detected': crisis_prob > 0.5,
        'confidence': crisis_prob,
        'classification': 'CRISIS' if crisis_prob > 0.5 else 'SAFE'
    }

# Test examples
examples = [
    "I'm feeling great today and looking forward to the weekend!",
    "I feel hopeless and don't see any point in continuing.",
    "Just had a good conversation with my therapist."
]

for text in examples:
    result = detect_crisis(text)
    print(f"Text: {text}")
    print(f"Result: {result['classification']} (confidence: {result['confidence']:.3f})")
    print("---")
```

## Important Notes

### For Production Use
- **Validation Required**: Test on real-world mental health data
- **Human Oversight**: Always include human review for crisis cases
- **Privacy**: Ensure HIPAA compliance for healthcare applications

### Limitations
- Trained on synthetic data - requires validation on real-world text
- Perfect metrics may not generalize to all edge cases

## Technical Specifications

- **Architecture**: ModernBERT-base with classification head
- **Parameters**: ~139M (base) + 1.5K (classification)
- **Context Length**: 8,192 tokens
- **Input Format**: Raw text (any length, auto-truncated)
- **Output**: Binary classification (crisis/non-crisis) + confidence

## Citation

```bibtex
@model{modernbert-crisis-detection,
  author = {Akash Paul},
  title = {ModernBERT Crisis Detection: Fine-tuned Mental Health Crisis Detection},
  year = {2024},
  url = {https://huggingface.co/akashpaul123/modernbert-crisis-detection},
  note = {Fine-tuned from answerdotai/ModernBERT-base}
}
```

## Contact

- **Author**: Akash Paul
- **Username**: Akashpaul123

---

**⚠️ Important**: This model is for research and supportive applications only. Always consult mental health professionals for clinical decisions.
