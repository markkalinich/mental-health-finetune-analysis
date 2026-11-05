---
license: mit
tags:
- text-classification
- nlp
- sentiment-analysis
- transformers
datasets:
- custom
metrics:
- accuracy
- f1
---

# Roadblock Detection Classifier (v1)

## 🔍 Overview
The **Roadblock Classifier** detects whether a check-in contains signs of a **roadblock or struggle**.

This helps identify when students need support or intervention.

---

## 🎯 Purpose
Students may express confusion, frustration, or blockers in their check-ins. This model identifies those signals automatically.

---

## 🧠 Model Details
- Task: Binary Text Classification  
- Labels:
  - `ROADBLOCK` → Indicates confusion, issue, or blocker  
  - `NOT_ROADBLOCK` → No issues present  
- Architecture: Transformer-based (fine-tuned)

---

## 📦 Use Cases
- Early detection of struggling students  
- Automated support systems  
- Mentor alerts  
- Educational analytics  

---

## 🧪 Example

### Input
```text
I was struggling to understand why my API deployment kept failing
```

### Output
```json 
{
  "label": "ROADBLOCK",
  "confidence": 0.99
}
```
### Input
```text
Today I completed my feature and everything is working well
```

### Output
```json
{
  "label": "NOT_ROADBLOCK",
  "confidence": 0.97
}
```
--- 
## Pipeline Integration

### This model runs after check-in validation and quality analysis:

1. Check-in or Not
2. Check-in Detail
3. **Roadblock Detection (this model)**
4. Intervention or generation
---

## Usage (Python)
```python
from transformers import pipeline

classifier = pipeline("text-classification", model="mjpsm/roadblock-classifier-v1")

result = classifier("I was confused about my API deployment")
print(result)
```
---
# Performance
- High accuracy and F1 score (~0.97–0.99 observed during evaluation)
---
## Future Improvements

1. Detect severity of roadblocks
2. Multi-label emotions (confusion, frustration, stuck)
3. Suggest solutions automatically
---

## 👤 Author
- Mazamesso Meba
- Information Systems Student | AI Developer


