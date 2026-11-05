---
language: en
license: mit
library_name: transformers
tags:
- text-classification
- psychology
- abuse-detection
- darvo
- manipulation-detection
- mental-health
- relationship-analysis
- tether-pro
datasets:
- custom
metrics:
- mse
- mae
- accuracy
- auc
model-index:
- name: tether-darvo-regressor-v1
  results:
  - task:
      type: text-classification
      name: DARVO Detection
    metrics:
    - type: mse
      value: 0.043
    - type: mae  
      value: 0.171
    - type: accuracy
      value: 0.842
    - type: auc
      value: 0.881
---

# Tether Pro DARVO Regressor v2

## Model Description

This model detects DARVO (Deny, Attack, Reverse Victim & Offender) manipulation tactics in text communication. DARVO is a psychological manipulation strategy where an abuser:

1. **Denies** the abuse ever happened
2. **Attacks** the victim for bringing it up  
3. **Reverses** the roles to claim they are the victim

## Key Features

🎯 **Role-Aware Detection**: Distinguishes between genuine accountability and manipulation tactics
🔬 **Research-Grade Accuracy**: 84% accuracy with 0.88 AUC
⚡ **Real-Time Analysis**: Optimized for fast inference
🛡️ **Professional Use**: Designed for therapists, legal professionals, and safety applications

## Performance Metrics

| Metric | Score |
|--------|-------|
| **R²** | 0.665 |
| **MAE** | 0.171 |
| **MSE** | 0.043 |
| **Accuracy** | 84.2% |
| **AUC** | 88.1% |

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("SamanthaStorm/tether-darvo-regressor-v1")
model = AutoModelForSequenceClassification.from_pretrained("SamanthaStorm/tether-darvo-regressor-v1")

# Example usage
text = "You're the one being abusive to me right now"

# Tokenize and predict
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
with torch.no_grad():
    outputs = model(**inputs)
    darvo_score = outputs.logits.item()

print(f"DARVO Score: {darvo_score:.3f}")  # Higher scores = more DARVO tactics
```

## Score Interpretation

- **0.0 - 0.3**: Genuine accountability, healthy communication
- **0.3 - 0.6**: Some defensive patterns, mild deflection  
- **0.6 - 0.8**: Moderate DARVO tactics, concerning patterns
- **0.8 - 1.0**: Strong DARVO tactics, victim reversal

## Example Predictions

| Text | DARVO Score | Interpretation |
|------|-------------|----------------|
| "You're the one being abusive to me right now" | 0.870 | High DARVO - victim reversal |
| "I don't remember saying that" | 0.224 | Low DARVO - simple denial |
| "I take full responsibility for my actions" | 0.205 | Very low DARVO - accountability |

## Training Data

Trained on 285 carefully curated examples including:
- **High DARVO**: Explicit victim reversal tactics
- **Medium DARVO**: Deflection and minimization patterns  
- **Low DARVO**: Genuine accountability and healthy communication
- **Contrast Examples**: Non-apologies vs real apologies

## Applications

### 🏥 Clinical Therapy
- Help therapists identify manipulation patterns in client relationships
- Assist in couples counseling to recognize unhealthy dynamics
- Support trauma therapy by validating victim experiences

### ⚖️ Legal Documentation  
- Analyze communication patterns in domestic violence cases
- Provide objective evidence of psychological manipulation
- Support legal professionals in building abuse cases

### 🏢 Workplace Safety
- Identify harassment patterns in workplace communications
- Support HR investigations with objective analysis
- Create safer work environments through pattern recognition

## Ethical Considerations

⚠️ **Important**: This model is designed to assist professionals and should not be used as the sole basis for serious decisions about relationships or safety.

- **Professional Use**: Best used by trained therapists, counselors, and legal professionals
- **Context Matters**: Consider cultural, situational, and individual factors
- **Not Diagnostic**: Does not diagnose psychological conditions
- **Privacy**: Ensure consent when analyzing personal communications

## Technical Details

- **Base Model**: DistilBERT (distilbert-base-uncased)
- **Architecture**: Custom regression head with 4-layer neural network
- **Training**: 8 epochs with cosine learning rate scheduling
- **Optimization**: Mixed precision training (FP16)
- **Max Length**: 256 tokens for efficiency

## Model Architecture

```
DistilBERT Base
    ↓
Linear(768 → 768) + GELU + Dropout
    ↓  
Linear(768 → 384) + GELU + Dropout
    ↓
Linear(384 → 192) + GELU + Dropout
    ↓
Linear(192 → 1) + Sigmoid
    ↓
DARVO Score (0.0 - 1.0)
```

## Version History

### v2 (Current)
- ✅ Enhanced training dataset (285 examples)
- ✅ Improved architecture with deeper regression head
- ✅ Better score calibration for accountability detection
- ✅ Added contrast examples (fake vs real apologies)
- ✅ 84% accuracy (up from 40%)

### v1 (Previous)  
- Basic DARVO detection capability
- Limited training data
- Lower accuracy performance

## Citation

If you use this model in research or professional practice, please cite:

```bibtex
@misc{tether-darvo-regressor-v1,
  title={Tether Pro DARVO Regressor: Role-Aware Detection of Manipulation Tactics},
  author={SamanthaStorm},
  year={2024},
  howpublished={\url{https://huggingface.co/SamanthaStorm/tether-darvo-regressor-v1}},
}
```

## Contact & Support

For questions about integration, licensing, or professional applications:
- 📧 Enterprise: enterprise@tether.ai
- 🌐 Documentation: docs.tether.ai
- 📅 Consultation: calendly.com/tether-pro

## Related Models

Part of the **Tether Pro AI Suite**:
- 🛡️ **Boundary Health Detector**: `SamanthaStorm/healthy-boundary-predictor`
- 🎯 **Abuse Pattern Detector**: `SamanthaStorm/tether-multilabel-v6`  
- 🎭 **Sentiment Analyzer**: `SamanthaStorm/tether-sentiment-v3`
- 🧩 **Fallacy Detector**: `SamanthaStorm/fallacy-detector` (coming soon)
- 🎯 **Intent Classifier**: `SamanthaStorm/intent-detector` (coming soon)

---

*Built with ❤️ for safer communication analysis*
