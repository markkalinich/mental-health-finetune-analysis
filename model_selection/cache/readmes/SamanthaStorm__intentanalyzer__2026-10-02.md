---
language: en
license: mit
tags:
- text-classification
- intent-detection
- communication-analysis
- multi-label-classification
- psychology
- nlp
- transformers
datasets:
- custom
metrics:
- f1: 0.77
- precision: 0.95
- recall: 0.92
model-index:
- name: IntentAnalyzer
  results:
  - task:
      type: text-classification
      name: Multi-Label Intent Detection
    dataset:
      type: custom
      name: Communication Intent Dataset
    metrics:
    - type: f1_macro
      value: 0.77
    - type: f1_trolling
      value: 0.94
    - type: f1_constructive
      value: 0.99
widget:
- text: "You're just a stupid liberal, so your opinion doesn't matter"
  example_title: "Manipulative + Dismissive"
- text: "I understand your concerns, but here's why I disagree"
  example_title: "Constructive Communication"
- text: "Whatever, I don't care about this anymore"
  example_title: "Dismissive Behavior"
- text: "I CAN'T BELIEVE you would say that to me!!!"
  example_title: "Emotionally Reactive"
- text: "If you really loved me, you would support this"
  example_title: "Manipulative Behavior"
---

# IntentAnalyzer: Multi-Label Communication Intent Detection

## Model Description

IntentAnalyzer is a state-of-the-art multi-label text classification model designed to detect underlying intentions in human communication. Built on DistilBERT architecture, this model can simultaneously identify multiple intent categories with high precision, helping understand the psychological and communicative patterns behind text.

## Supported Intent Categories

The model detects 6 different intent categories (multi-label):

1. **🧌 Trolling** - Deliberately provocative or disruptive communication
2. **🚫 Dismissive** - Shutting down conversation or avoiding engagement
3. **🎭 Manipulative** - Using emotional coercion, guilt, or pressure tactics
4. **🌋 Emotionally Reactive** - Overwhelmed by emotion, not thinking clearly
5. **✅ Constructive** - Good faith engagement and dialogue
6. **❓ Unclear** - Ambiguous intent that's difficult to determine

## Performance Metrics

### Overall Performance
- **F1 Score (Macro)**: 0.77
- **Multi-label Classification**: Supports simultaneous detection of multiple intents

### Per-Category Performance
- **Trolling**: F1=0.943 (P=0.976, R=0.911)
- **Dismissive**: F1=0.850 (P=0.964, R=0.761)
- **Manipulative**: F1=0.907 (P=0.867, R=0.951)
- **Emotionally Reactive**: F1=0.939 (P=0.931, R=0.947)
- **Constructive**: F1=0.989 (P=0.978, R=1.000)
- **Unclear**: F1=0.000 (Expected - ambiguous by design)

## Usage

```python
import torch
from transformers import AutoTokenizer, AutoModel
import torch.nn as nn

# Define the model architecture
class MultiLabelIntentClassifier(nn.Module):
    def __init__(self, model_name, num_labels):
        super().__init__()
        self.bert = AutoModel.from_pretrained(model_name)
        self.dropout = nn.Dropout(0.3)
        self.classifier = nn.Linear(self.bert.config.hidden_size, num_labels)

    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        pooled_output = outputs.last_hidden_state[:, 0]
        pooled_output = self.dropout(pooled_output)
        logits = self.classifier(pooled_output)
        return logits

# Load model and tokenizer
model_name = "SamanthaStorm/intentanalyzer"
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

# Load the custom model (you'll need to download the .pth file)
model = MultiLabelIntentClassifier("distilbert-base-uncased", 6)
# model.load_state_dict(torch.load('pytorch_model.bin'))

# Intent categories
intent_categories = ['trolling', 'dismissive', 'manipulative', 'emotionally_reactive', 'constructive', 'unclear']

def predict_intent(text, threshold=0.5):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)

    with torch.no_grad():
        outputs = model(inputs['input_ids'], inputs['attention_mask'])
        probabilities = torch.sigmoid(outputs).numpy()[0]

    # Return predictions above threshold
    predictions = {}
    for i, category in enumerate(intent_categories):
        prob = probabilities[i]
        if prob > threshold:
            predictions[category] = prob

    return predictions

# Example usage
text = "You're just being emotional and can't think rationally"
intents = predict_intent(text)
print("Detected intents:", intents)
```

## Training Data

The model was trained on a carefully curated dataset of 1,226 examples with:
- **Single-label examples**: Clear instances of each intent type
- **Multi-label examples**: Realistic scenarios with multiple simultaneous intents
- **Balanced distribution**: Proper representation across all categories
- **Diverse contexts**: Personal, professional, online, and social interactions

## Model Architecture

- **Base Model**: DistilBERT (distilbert-base-uncased)
- **Task**: Multi-label text classification
- **Classes**: 6 intent categories
- **Loss Function**: BCEWithLogitsLoss (binary cross-entropy for multi-label)
- **Max Sequence Length**: 128 tokens
- **Training Examples**: 1,226 high-quality examples

## Applications

### Communication Analysis
- **Customer Service**: Identify frustrated or manipulative customers
- **Social Media Monitoring**: Detect trolling and constructive engagement
- **Relationship Counseling**: Understand communication patterns
- **Content Moderation**: Flag problematic intent patterns

### Research Applications
- **Psychology**: Study communication patterns and intentions
- **Linguistics**: Analyze pragmatic aspects of language
- **Social Sciences**: Understanding online discourse patterns
- **Education**: Teaching healthy communication skills

## Limitations and Considerations

- Trained primarily on English text
- Performance may vary on highly context-dependent cases
- Best suited for interpersonal communication analysis
- Cultural and contextual nuances may affect accuracy
- Multi-label predictions require threshold tuning for optimal results

## Model Card Contact

For questions, issues, or collaboration opportunities, please open an issue on the model repository.

## Ethical Considerations

This model is designed to help understand communication patterns for constructive purposes such as:
- Improving dialogue quality
- Identifying harmful communication patterns
- Supporting mental health and relationship counseling
- Educational applications

**Important**: This model should not be used for:
- Surveillance without consent
- Discriminatory decision-making
- Automated content removal without human review
- Any application that could harm individuals or communities

## Citation

If you use this model in your research, please cite:

```bibtex
@misc{intentanalyzer2024,
  author = {SamanthaStorm},
  title = {IntentAnalyzer: Multi-Label Communication Intent Detection},
  year = {2024},
  publisher = {Hugging Face},
  url = {https://huggingface.co/SamanthaStorm/intentanalyzer}
}
```

## License

This model is released under the MIT License.

## Companion Models

This model works excellently in combination with:
- **FallacyFinder** ([SamanthaStorm/fallacyfinder](https://huggingface.co/SamanthaStorm/fallacyfinder)) - Logical fallacy detection
- Together they provide comprehensive communication analysis covering both logical reasoning and psychological intent

---

**IntentAnalyzer** - Understanding the psychology behind human communication 🎭
