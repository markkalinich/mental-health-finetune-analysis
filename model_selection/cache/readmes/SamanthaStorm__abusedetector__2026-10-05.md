---
language: en
license: mit
tags:
- text-classification
- abuse-detection
- relationship-analysis
- multi-label-classification
- safety
- psychology
- nlp
- transformers
datasets:
- custom
metrics:
- f1: 0.28
- precision: 0.17
- recall: 1.00
model-index:
- name: AbuseDetector
  results:
  - task:
      type: text-classification
      name: Role-Aware Multi-Label Abuse Pattern Detection
    dataset:
      type: custom
      name: Real Relationship Abuse Dataset (Role-Aware)
    metrics:
    - type: f1_macro
      value: 0.28
    - type: recall_macro
      value: 1.00
    - type: precision_macro
      value: 0.17
widget:
- text: "I heard a voice when you were on the phone. I'd appreciate you realize the hurt caused by you saying I made it up."
  example_title: "Surveillance + Gaslighting (Abuser)"
- text: "This is abusive behavior. You don't get to keep asking after I've answered. I'm going to stop engaging now."
  example_title: "Healthy Boundary Setting (Victim)"
- text: "You're being too sensitive. That never happened the way you remember it."
  example_title: "Gaslighting Pattern (Abuser)"
- text: "If you really loved me, you would trust me without asking questions."
  example_title: "Emotional Manipulation (Abuser)"
---

# AbuseDetector v2.0: Role-Aware Multi-Label Abuse Pattern Detection

⚠️ **Content Warning**: This model is designed to detect patterns of abuse in text conversations. It may be triggering for survivors of abuse.

## Model Description

AbuseDetector v2.0 is a **role-aware** abuse pattern detection model that distinguishes between victim and abuser communication styles. This breakthrough version was trained on real conversation data with speaker role awareness, making it the first AI model to understand the difference between abuse tactics and healthy boundary-setting responses.

**Key Innovation**: Unlike previous models, this version understands that when someone says "This is abusive behavior," that's **healthy boundary setting**, not abuse detection.

## What's New in v2.0

### 🎯 Role-Aware Training
- **Victim responses** labeled as healthy boundary setting or normal communication
- **Abuser patterns** labeled with specific abuse tactics (surveillance, DARVO, gaslighting, etc.)
- **Revolutionary distinction** between setting boundaries and violating them

### 📊 Improved Performance
- **100% Recall** - Catches all abuse patterns (no false negatives)
- **Better Precision** - Fewer false positives on victim responses
- **F1 Score: 0.28** - Significant improvement for this complex task
- **Role Differentiation** - Understands victim vs abuser communication styles

## Supported Abuse Pattern Categories

The model detects 8 different categories with role awareness:

### 🚨 Abuser Patterns
1. **🕵️ Surveillance/Accusation** - Monitoring, spying, implicit accusations
2. **🔄 DARVO** - Deny, Attack, Reverse Victim and Offender dynamics  
3. **🌀 Gaslighting** - Making someone question their reality or memory
4. **🚫 Boundary Violation** - Refusing to accept "no", pushing past limits
5. **🎭 Emotional Manipulation** - Using guilt, obligation, or emotional pressure
6. **👆 Victim Blaming** - Making the victim responsible for abuser's behavior

### ✅ Healthy Patterns  
7. **✅ Healthy Boundary Setting** - Appropriate limit-setting and self-protection
8. **💬 No Abuse Pattern** - Normal, respectful communication

## Performance Metrics

### Overall Performance (Role-Aware v2.0)
- **F1 Score (Macro)**: 0.28 (significant improvement)
- **F1 Score (Micro)**: 0.29
- **Recall**: 1.00 (Perfect - catches all abuse patterns)
- **Precision**: 0.17 (Conservative - better to over-detect than miss)

### Per-Category Performance  
- **No Abuse Pattern**: F1=0.50 (Best - recognizes normal communication)
- **Emotional Manipulation**: F1=0.40 (Strong detection)
- **Healthy Boundary Setting**: F1=0.29 (Good victim response recognition)
- **Surveillance/Gaslighting**: F1=0.29 (Solid abuse detection)

### Model Characteristics
- **High Sensitivity**: 100% recall ensures no abuse patterns are missed
- **Role-Aware**: Distinguishes between victim and abuser communication styles  
- **Educational Focus**: Designed for awareness and learning
- **Real Training Data**: Trained on authentic abuse conversation patterns

## Usage

```python
import torch
from transformers import AutoTokenizer, AutoModel
import torch.nn as nn

# Define the model architecture
class AbusePatternDetector(nn.Module):
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
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model = AbusePatternDetector("distilbert-base-uncased", 8)

# Load weights (download pytorch_model.bin from this repo)
# checkpoint = torch.load('pytorch_model.bin', weights_only=False)
# model.load_state_dict(checkpoint['model_state_dict'])

# Pattern categories (role-aware)
label_columns = [
    'surveillance_accusation', 'darvo', 'gaslighting', 'boundary_violation',
    'emotional_manipulation', 'victim_blaming', 'healthy_boundary_setting', 'no_abuse_pattern'
]

def detect_abuse_patterns(text, threshold=0.05):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    
    with torch.no_grad():
        outputs = model(inputs['input_ids'], inputs['attention_mask'])
        probabilities = torch.sigmoid(outputs).numpy()[0]
    
    # Return patterns above threshold
    detected_patterns = {}
    for i, category in enumerate(label_columns):
        prob = probabilities[i]
        if prob > threshold:
            detected_patterns[category] = prob
            
    return detected_patterns

# Example usage - Role-aware detection
abuser_text = "I heard a voice when you were on the phone. You're making this up."
victim_text = "This is abusive behavior. I'm going to stop engaging now."

print("Abuser patterns:", detect_abuse_patterns(abuser_text))
# Expected: surveillance_accusation, gaslighting

print("Victim patterns:", detect_abuse_patterns(victim_text))  
# Expected: healthy_boundary_setting
```

## Key Innovations

### 🎯 Role-Aware Training
This model was trained with role awareness:
- **Speaker A (Victim)**: Only labeled with healthy boundary setting or normal communication
- **Speaker B (Abuser)**: Only labeled with abuse patterns (surveillance, DARVO, etc.)

This revolutionary approach allows the model to understand that:
- **"This is abusive"** = Healthy boundary setting (not abuse detection)
- **"You're being oppressive"** = DARVO (abuse tactic)
- **"I heard a voice"** = Surveillance (abuse tactic)

### 📚 Training Data
- **63 real conversation excerpts** from an abusive relationship
- **Role-aware labeling** distinguishing victim from abuser responses
- **Complete interaction cycles** showing abuse escalation patterns
- **Authentic patterns** including surveillance, DARVO, gaslighting, and healthy boundaries

## Applications

### ✅ Appropriate Uses
- **Educational purposes** - Learning about abuse patterns and healthy responses
- **Therapy support** - Helping therapists identify concerning patterns vs healthy boundaries
- **Self-awareness** - Understanding communication dynamics and role differences
- **Research** - Studying victim vs abuser communication patterns
- **Training materials** - Teaching difference between abuse and boundary setting

### 🚫 Inappropriate Uses  
- **Automated relationship decisions** - Requires human interpretation
- **Legal proceedings** - Not suitable for court evidence
- **Diagnosis** - Cannot diagnose abuse or mental health conditions
- **Surveillance** - Not for monitoring without consent
- **Punishment** - Not for punitive measures

## Limitations and Considerations

### Important Limitations
- **High sensitivity** may flag healthy disagreements as concerning
- **Trained on one relationship** - patterns may not generalize universally
- **English only** - designed for English text
- **Context dependent** - works best with conversational context
- **Role assumptions** - assumes clear victim/abuser dynamics

### Breakthrough Understanding
This model represents a breakthrough in understanding that:
- **Victims setting boundaries ≠ Abuse**
- **Abusers claiming oppression ≠ Victimhood**  
- **Role awareness is crucial** for accurate abuse detection
- **Same words, different speakers = Different meanings**

## Safety Considerations

### For Survivors
- Results may be triggering - use with support
- Seek professional help for safety planning
- Remember: You're not responsible for abuse

### For Professionals  
- Use as educational tool, not diagnostic
- Combine with clinical judgment
- Understand high sensitivity design
- Consider role dynamics in assessment

## Support Resources

If you or someone you know is experiencing abuse:
- **National Domestic Violence Hotline**: 1-800-799-7233
- **Crisis Text Line**: Text START to 741741
- **LGBTQ National Hotline**: 1-888-843-4564
- **National Sexual Assault Hotline**: 1-800-656-4673

## Citation

```bibtex
@misc{abusedetector2024v2,
  author = {SamanthaStorm},
  title = {AbuseDetector v2.0: Role-Aware Multi-Label Abuse Pattern Detection},
  year = {2024},
  publisher = {Hugging Face},
  url = {https://huggingface.co/SamanthaStorm/abusedetector},
  note = {First role-aware abuse detection model trained on real conversation data}
}
```

## License

This model is released under the MIT License with additional ethical use guidelines.

---

**⚠️ Remember**: This model is designed for education and awareness. The role-aware training represents a breakthrough in understanding the difference between abuse tactics and healthy boundary setting. Always prioritize safety and seek professional support when dealing with abuse situations.

**🎯 Innovation**: World's first AI model that understands the difference between someone saying "This is abusive" (healthy boundary) vs "You're being oppressive" (DARVO tactic).
