---
library_name: transformers
pipeline_tag: text-classification
language:
- en
- he
tags:
- clinical-nlp
- mental-health
- sentiment-analysis
- healthcare
- bert
widget:
- text: "I've been waiting for my results for two weeks and I'm very frustrated."
  example_title: "Patient Frustration"
- text: "I'm worried about the new medication dosage, can someone clarify?"
  example_title: "Anxiety & Confusion"
- text: "Thank you for the quick follow-up, the portal is working great now."
  example_title: "Satisfaction"
---
# Clinical EmoTiSupport v2 (Business-Aligned Logic) 🏥

## 🚀 Overview: Beyond Standard Metrics
**Clinical EmoTiSupport v2** is not just a text classifier; it is a **risk-calibrated engine** designed for real-world digital health environments. 

Unlike standard NLP models that treat all errors equally, this model was fine-tuned and calibrated with a specific business philosophy: **In healthcare, a False Negative on 'Anger' or 'Anxiety' is more dangerous than a False Positive.**

We refined the dataset to remove logical inconsistencies (e.g., "polite anger") and implemented a **Safety Guardrail** mechanism to filter out neutral administrative noise with 94% precision.

## 💡 Key Upgrades in v2
1.  **Cleaner Data (v6):** We aggressively cleaned the training data (2,000 samples) to remove "Politeness Artifacts" — specifically cases where patients used "Thank you" while expressing severe frustration, which confused previous iterations.
2.  **Adaptive Thresholding:** We moved away from the standard `0.5` threshold. This model is designed to be used with **class-specific thresholds** (see *Inference Logic* below) to maximize the detection of urgent signals.
3.  **Neutral Guardrail:** A dedicated logic layer that prevents low-confidence predictions from triggering false alarms.

## 📊 Performance & Calibration
Evaluated on a strictly cleaned validation set (20% split), calibrated for high sensitivity on critical emotions:

| Metric | Value | significance |
| :--- | :--- | :--- |
| **Micro F1-Score** | **0.84** | Robust overall performance |
| **Neutral Precision** | **0.94** | Highly trustworthy when it says "Nothing is wrong" |
| **Anger Recall** | **~0.60** | **+23% improvement** over v1 (Critical for retention) |

### Recommended Thresholds (Business Logic)
To reproduce our results, do not use a flat `0.5` cutoff. Use the following sensitivity thresholds:

| Emotion | Threshold | Reasoning |
| :--- | :--- | :--- |
| **Anger** | **0.30** | High Sensitivity: Better to flag a false alarm than miss a furious patient. |
| **Anxiety** | **0.40** | High Sensitivity: Early detection of distress signals. |
| **Frustration** | **0.40** | Early warning sign of churn. |
| **Disappointment** | **0.50** | Balanced precision/recall. |
| **Confusion** | **0.50** | Balanced precision/recall. |
| **Satisfaction** | **0.65** | High Precision: Only classify as "Satisfied" if certainty is high (avoids "polite" false positives). |
| **Guiderail** | **0.35** | If `max(probs) < 0.35`, the label is **Neutral**. |

## 🛠 How to Use (with Business Logic)
To get the best results, use this inference snippet which includes the Guardrail and Adaptive Thresholds:

```python
import torch
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# 1. Setup
model_id = "YourUserName/Clinical-EmoTiSupport-v2" # Update this!
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id)

# 2. Define Business Logic
THRESHOLDS = {
    "anxiety": 0.40, "confusion": 0.50, "frustration": 0.40, 
    "anger": 0.30, "disappointment": 0.50, "satisfaction": 0.65
}
EMOTIONS = ["anxiety", "confusion", "frustration", "anger", "disappointment", "satisfaction"]
GUARDRAIL = 0.35

# 3. Predict
text = "I've been waiting for my results for a week, this is ridiculous!"
inputs = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    probs = torch.sigmoid(model(**inputs).logits).squeeze()

# 4. Apply Logic
results = {}
if probs.max() < GUARDRAIL:
    print("Prediction: Neutral / Administrative")
else:
    for i, label in enumerate(EMOTIONS):
        if probs[i] > THRESHOLDS[label]:
            results[label] = float(probs[i])

print("Detected Emotions:", results)
# Expected Output: {'anger': 0.72, 'frustration': 0.81} (Example)