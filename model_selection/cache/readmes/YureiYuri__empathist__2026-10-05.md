---
license: apache-2.0
language:
- en
pipeline_tag: text-classification
tags:
- medical
- code
- mental_health
- classifier
library_name: transformers
---

# CBT Cognitive Distortion Classifier

A fine-tuned DistilBERT model for detecting cognitive distortions in text, based on Cognitive Behavioral Therapy (CBT) principles.

## Model Description

This model identifies 5 common cognitive distortions in conversational text:

- **Overgeneralization**: Using "always", "never", "everyone", "nobody"
- **Catastrophizing**: Using "terrible", "awful", "worst", "disaster"
- **Black and White Thinking**: All-or-nothing, either/or patterns
- **Self-Blame**: "My fault", "blame myself", "guilty"
- **Mind Reading**: "They think", "must think", "probably think"

## Model Details

- **Base Model**: `distilbert-base-uncased`
- **Task**: Multi-label classification
- **Number of Labels**: 5
- **Training Data**: 231 samples from mental health conversational data
- **Training Split**: 196 train / 35 test
- **Framework**: HuggingFace Transformers

## Training Performance

| Epoch | Training Loss | Validation Loss |
|-------|--------------|-----------------|
| 1     | 0.1200       | 0.0857          |
| 2     | 0.0322       | 0.0258          |
| 3     | 0.0165       | 0.0129          |
| 4     | 0.0335       | 0.0084          |
| 5     | 0.0079       | 0.0067          |
| 6     | 0.0066       | 0.0056          |
| 7     | 0.0311       | 0.0048          |
| 8     | 0.0523       | 0.0045          |
| 9     | 0.0051       | 0.0044          |
| 10    | 0.0278       | 0.0043          |

**Final Validation Loss**: 0.0043

## Training Configuration

```python
- Epochs: 10
- Batch Size: 8
- Evaluation Strategy: Per epoch
- Optimizer: AdamW (default)
- Max Sequence Length: 128
- Device: GPU (Tesla T4)
```

## Usage

### Loading the Model

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("./cbt_model_final")
tokenizer = AutoTokenizer.from_pretrained("./cbt_model_final")

# Load label mappings
import json
with open("./cbt_model_final/label_config.json", "r") as f:
    label_config = json.load(f)

id2label = label_config["id2label"]
```

### Making Predictions

```python
def predict_distortions(text, threshold=0.5):
    # Tokenize input
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
    
    # Get predictions
    with torch.no_grad():
        outputs = model(**inputs)
        probabilities = torch.sigmoid(outputs.logits).squeeze()
    
    # Extract distortions above threshold
    detected = []
    for idx, prob in enumerate(probabilities):
        if prob > threshold:
            label = id2label[str(idx)]
            detected.append({
                "distortion": label,
                "confidence": f"{prob.item():.2%}"
            })
    
    return detected

# Example usage
text = "I always mess everything up. This is a disaster!"
distortions = predict_distortions(text)

for d in distortions:
    print(f"{d['distortion']}: {d['confidence']}")
```

### Example Output

```
Input: "I always mess everything up. This is a disaster!"

Detected distortions:
  overgeneralization: 73.45%
  catastrophizing: 68.92%
```

## Model Limitations

⚠️ **Important Considerations**:

- **Small Training Dataset**: Only 231 samples - model may not generalize well to all contexts
- **Rule-Based Labels**: Training labels were created using keyword matching, not expert annotations
- **Prototype Quality**: This is a proof-of-concept model, not production-ready
- **Low Confidence Scores**: Average predictions are 0.25-0.73%, indicating the model is conservative
- **Limited Context**: Only trained on short conversational patterns
- **No Clinical Validation**: Not validated by mental health professionals

## Recommendations for Improvement

1. **Expand Dataset**: Collect more diverse, expert-annotated examples
2. **Better Labeling**: Use clinical experts to label cognitive distortions
3. **Data Augmentation**: Generate synthetic examples for underrepresented patterns
4. **Hyperparameter Tuning**: Experiment with learning rates, batch sizes, epochs
5. **Evaluation Metrics**: Add precision, recall, F1-score tracking
6. **Class Balancing**: Address imbalanced distribution of distortion types

## Files Included

```
cbt_model_final/
├── config.json              # Model configuration
├── model.safetensors        # Model weights
├── tokenizer_config.json    # Tokenizer configuration
├── vocab.txt                # Vocabulary
├── special_tokens_map.json  # Special tokens
├── tokenizer.json           # Tokenizer data
└── label_config.json        # Label mappings
```

## License

This model is based on DistilBERT and inherits its Apache 2.0 license.

## Citation

```
Base Model: DistilBERT
Original Paper: Sanh et al. (2019) - DistilBERT, a distilled version of BERT
Fine-tuning: Custom CBT distortion detection
```

## Disclaimer

⚠️ **This model is for educational and research purposes only.** It should not be used as a substitute for professional mental health diagnosis or treatment. Always consult qualified mental health professionals for clinical applications.

---

**Created**: December 2025  
**Framework**: HuggingFace Transformers  
**Hardware**: Kaggle GPU (Tesla T4)