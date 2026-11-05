---
language:
- en
license: apache-2.0
library_name: setfit
tags:
- setfit
- sentence-transformers
- text-classification
- medical
- triage
- few-shot-learning
- patient-safety
datasets:
- custom
metrics:
- f1
- accuracy
pipeline_tag: text-classification
base_model: sentence-transformers/all-mpnet-base-v2
model-index:
- name: medical-query-router
  results:
  - task:
      type: text-classification
      name: Medical Query Triage
    metrics:
    - name: Weighted F1
      type: f1
      value: 0.888
    - name: Accuracy
      type: accuracy
      value: 0.889
    - name: Urgent Recall
      type: recall
      value: 0.933
---

# 🏥 Medical Query Router

**Few-shot classifier that routes patient queries into 3 safety tiers.**

Built with [SetFit](https://github.com/huggingface/setfit) — trained on just **90 hand-crafted examples** (30 per class) using contrastive learning.

## Classes

| Tier | Label | Action | Example |
|------|-------|--------|---------|
| 🟢 | `low_stakes` | Chatbot answers directly | *"How much paracetamol for a headache? I'm 30 and healthy"* |
| 🟡 | `high_stakes` | Doctor reviews before responding | *"Can I take ibuprofen while on blood thinners?"* |
| 🔴 | `urgent` | Tell patient to call 911/999 NOW | *"Crushing chest pain going down my left arm"* |

## Performance

Evaluated on 45 held-out examples (15 per class) including deliberate edge cases:

| Metric | Score |
|--------|-------|
| **Weighted F1** | **0.888** |
| **Accuracy** | **88.9%** |
| **Urgent Recall** | **93.3%** |
| Urgent Precision | 82.4% |
| Low Stakes F1 | 0.933 |
| High Stakes F1 | 0.857 |

### Confusion Matrix

```
              Predicted →  low   high  urgent
low_stakes                  14     0      1
high_stakes                  1    12      2
urgent                       0     1     14
```

### Backbone Comparison

We trained 3 models and selected the best:

| Backbone | F1 | Urgent Recall | Safety Score |
|----------|-----|---------------|-------------|
| **all-mpnet-base-v2** ★ | **0.888** | **0.933** | **0.859** |
| all-MiniLM-L6-v2 | 0.846 | 0.867 | 0.789 |
| MedEmbed-base-v0.1 | 0.801 | 0.867 | 0.748 |

## Usage

```python
from setfit import SetFitModel

model = SetFitModel.from_pretrained("boredpanda9/medical-query-router")

queries = [
    "What are some healthy ways to lose weight?",
    "Can I take naproxen with my blood pressure medication?",
    "I have crushing chest pain spreading to my left arm",
]

predictions = model.predict(queries)
print(predictions)
# ['low_stakes', 'high_stakes', 'urgent']

# With confidence scores
probabilities = model.predict_proba(queries)
print(probabilities)
```

## Training Details

- **Method**: SetFit (Sentence-Transformer fine-tuning + Logistic Regression head)
- **Paper**: [Efficient Few-Shot Learning Without Prompts](https://arxiv.org/abs/2209.11055)
- **Base model**: `sentence-transformers/all-mpnet-base-v2` (109.5M params)
- **Training data**: 90 hand-crafted examples (30 per class)
- **Contrastive pairs**: 3,600 (generated via R=20 pair sampling)
- **Epochs**: 1 (contrastive phase) + 1 (head phase)
- **Body learning rate**: 2e-5
- **Head learning rate**: 1e-2
- **Batch size**: 16 (contrastive), 2 (head)
- **Loss**: CosineSimilarityLoss
- **Head**: Logistic Regression with balanced class weights

## Class Design Rationale

### 🟢 Low Stakes
Queries where a chatbot can safely provide general information:
- OTC medication dosing for otherwise **healthy adults** (paracetamol, ibuprofen, antihistamines)
- General wellness (weight loss, sleep, hydration, exercise)
- Mild, self-limiting symptoms with **no red flags** (common cold, mild fever in children who are otherwise well, minor cuts/grazes)
- Lifestyle and prevention advice

### 🟡 High Stakes  
Queries requiring clinical judgement — a doctor must review before responding:
- **Prescription medication dosing** where errors cause harm (insulin, warfarin, metformin, chemotherapy)
- **Drug interactions** (especially with narrow therapeutic index drugs)
- **Comorbidities** that change management (diabetes + wound, COPD + ankle swelling)
- **Pregnancy/breastfeeding** medication safety
- **Chronic disease** management and flare-ups
- **Red flags** in symptoms (unexplained weight loss, persistent cough >3 weeks, changing moles)
- **Children's prescription** medications
- **Mental health** (non-crisis)

### 🔴 Urgent
Life-threatening emergencies — patient must call 911/999/112 immediately:
- Signs of **heart attack** (chest pain + arm/jaw, sweating, collapse)
- Signs of **stroke** (FAST: Face drooping, Arm weakness, Speech difficulty, Time to call)
- **Breathing emergencies** (anaphylaxis, severe asthma, choking, blue lips)
- **Overdose or poisoning** (especially in children)
- **Suicidal crisis** (active plan, immediate danger)
- **Severe bleeding** or major trauma
- **Meningitis** signs (non-blanching rash + fever + neck stiffness)
- **Seizures** lasting >5 minutes
- **Unconscious/unresponsive** person

## Limitations

⚠️ **This is a routing tool, not a diagnostic tool.** It decides *who* should answer a query, not *what* the answer is.

- Trained on 90 examples — may misclassify unusual or ambiguous queries
- Designed for English-language queries in UK/US healthcare contexts
- Should be used as a **first-pass filter** with human oversight, never as the sole decision-maker
- The model errs toward safety (high_stakes/urgent) when uncertain — this is by design
- Not validated on real clinical data — performance on actual patient messages may differ from the eval set

## License

Apache 2.0
