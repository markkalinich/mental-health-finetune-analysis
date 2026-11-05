---
language: tr
license: other
license_name: siriusai-premium-v1
license_link: LICENSE
tags:
- turkish
- content-moderation
- multi-label-classification
- text-classification
- safety
- moderation
- bert
- nlp
- transformers
base_model: dbmdz/bert-base-turkish-uncased
datasets:
- custom
metrics:
- f1
- precision
- recall
- accuracy
- mcc
library_name: transformers
pipeline_tag: text-classification
model-index:
- name: turkish-safety
  results:
  - task:
      type: text-classification
      name: Multi-label Content Safety Classification
    metrics:
    - type: f1
      value: 0.9165
      name: Macro F1
    - type: mcc
      value: 0.9045
      name: Matthews Correlation Coefficient
---

# Turkish Safety - Content Moderation Classifier v5.0

**Multi-label classification model for Turkish content moderation**

*Developed by SiriusAI Tech Brain Team*

---

## Mission

> **Empowering digital platforms with AI-driven content safety solutions.**

Turkish Safety is an advanced NLP model that analyzes Turkish content in real-time and detects harmful content across 7 different categories. It provides comprehensive content moderation for social media platforms, messaging applications, in-game chats, and community forums.

### Why This Model Matters

- **7 Risk Categories**: Detects SAFE, GROOMING, SEXUAL, OFFENSIVE, BULLYING, SELF_HARM, and THREAT
- **Turkish-First Design**: Optimized for Turkish linguistics and cultural context using BERTurk
- **Production-Ready**: <50ms inference, battle-tested architecture, enterprise-grade reliability
- **Multi-Label Intelligence**: Smart classification that understands content can belong to multiple categories
- **Expert Validation**: Curated training data with clear category boundaries and edge case handling

---

## Model Overview

| Property | Value |
|----------|-------|
| **Architecture** | BERT (Bidirectional Encoder Representations from Transformers) |
| **Base Model** | `dbmdz/bert-base-turkish-uncased` (BERTurk) |
| **Task** | Multi-label Text Classification |
| **Language** | Turkish (tr) |
| **Categories** | 7 content safety labels |
| **Model Size** | 443 MB (FP32) |
| **Inference Time** | ~10-15ms (GPU) / ~40-50ms (CPU) |

---

## Performance Metrics

### Final Evaluation Results (Epoch 2)

| Metric | Score | Description |
|--------|-------|-------------|
| **Macro F1** | **0.9165** | Harmonic mean of precision and recall across all categories |
| **MCC** | **0.9045** | Matthews Correlation Coefficient (robust multi-class metric) |
| **Eval Loss** | 0.0268 | Focal loss on validation set |

### Training Progress

| Epoch | Train Loss | Eval Loss | Macro F1 | MCC |
|-------|------------|-----------|----------|-----|
| 1 | 0.038 | 0.0282 | 0.9085 | 0.8957 |
| **2** | **0.038** | **0.0268** | **0.9165** | **0.9045** |

### Validation Test Results (86.4% Accuracy)

| Category | Test Cases | Correct | Notes |
|----------|-----------|---------|-------|
| **SAFE** | 5 | 4 | One false positive (compliment → offensive) |
| **GROOMING** | 4 | 2 | Boundary cases with SEXUAL/THREAT |
| **SEXUAL** | 3 | 3 | Perfect detection |
| **OFFENSIVE** | 3 | 3 | Perfect detection |
| **THREAT** | 3 | 3 | Perfect detection |
| **SELF_HARM** | 2 | 2 | Perfect detection |
| **BULLYING** | 2 | 2 | Perfect detection |

---

## Dataset

### Dataset Statistics

| Split | Samples | Purpose |
|-------|---------|---------|
| **Train** | 68,128 | Model training |
| **Test** | 17,033 | Model evaluation |
| **Total** | 85,161 | Complete dataset |

### Category Distribution (Full Dataset)

| Category | Samples | Percentage | Description |
|----------|---------|------------|-------------|
| **SAFE** | 25,488 | 29.9% | Benign, normal communication |
| **SELF_HARM** | 14,234 | 16.7% | Self-harm ideation, suicidal thoughts |
| **BULLYING** | 13,259 | 15.6% | Harassment, exclusion, cyberbullying |
| **THREAT** | 9,193 | 10.8% | Physical threats, violence, blackmail |
| **SEXUAL** | 8,642 | 10.1% | Sexual content, body comments |
| **GROOMING** | 7,517 | 8.8% | Manipulation, trust-building tactics |
| **OFFENSIVE** | 6,849 | 8.0% | Profanity, slurs, offensive language |

### Subcategory Breakdown

| Category | Subcategories |
|----------|---------------|
| **SAFE** | greetings (1,958), farewells (1,485), wellbeing_questions (2,900), daily_conversation (2,435), weather_talk (1,445), food_drink (1,481), normal_questions (1,861), school_talk (1,961), family_talk (1,487), hobbies_games (1,455), sports_talk (1,000), tech_internet (994), genuine_compliments (1,000), encouragement (1,000), appreciation (1,000), apology_understanding (998), help_cooperation (1,000) |
| **GROOMING** | secrecy (953), isolation (729), trust_manipulation (792), meeting_private (701), gift_promise (565), age_questioning (688), private_communication (628), emotional_manipulation (654), normalization (655), excessive_flattery (559), testing_boundaries (583) |
| **THREAT** | physical_violence (1,307), weapon_threat (936), blackmail (1,168), family_threat (1,071), implicit_threat (906), revenge (947), death_threat (886), social_threat (930), stalking_threat (532), property_threat (500) |
| **OFFENSIVE** | insults (1,286), cursing_sik (1,535), cursing_am (1,398), cursing_ana_orospu (1,383), derogatory (849), mockery (398) |
| **SEXUAL** | explicit_content (1,085), sexual_body_focus (1,612), sexual_invitation (1,237), pornographic (1,060), sexual_questions (1,232), romantic_pressure (1,030), inappropriate_comments (856), sexual_fantasy (530) |
| **BULLYING** | exclusion (1,904), mockery_repeated (1,690), emotional_abuse (1,678), appearance_attack (1,490), public_humiliation (1,091), intimidation (979), cyberbullying (1,138), name_calling (1,178), spreading_rumors (1,000), academic_bullying (1,111) |
| **SELF_HARM** | hopelessness (1,923), giving_up (1,690), not_waking_up (1,435), suicide_ideation (1,413), self_harm_plan (1,532), burden_feeling (1,018), worthlessness (1,037), isolation_feeling (1,025), goodbye_messages (807), self_blame (894), depression_signs (1,452) |

### Data Generation Methodology

1. **Synthetic Generation**: LLM-based generation with expert-defined category boundaries
2. **Hard Negative Mining**: Difficult edge cases for boundary discrimination
3. **Quality Filtering**: Duplicate detection, minimum word count, forbidden token filtering
4. **Parallel Processing**: 20 concurrent workers with batch size of 50
5. **Pass Rate**: 97.5% average acceptance rate across all categories

---

## Label Definitions

The model classifies text into 7 mutually non-exclusive categories:

| Label | ID | Description | Turkish Examples |
|-------|-----|-------------|------------------|
| `SAFE` | 0 | Benign, normal communication | "Bugün hava güzel", "Oyun oynayalım mı?" |
| `OFFENSIVE` | 1 | Profanity, slurs, offensive language | "Aptal mısın", "Salak herif" |
| `SELF_HARM` | 2 | Self-harm ideation, suicidal thoughts | "Ölmek istiyorum", "Kendimi kesmek istiyorum" |
| `GROOMING` | 3 | Manipulation, trust-building, isolation tactics | "Kimseye söyleme", "Sen özelsin", "Evime gel" |
| `BULLYING` | 4 | Harassment, exclusion, cyberbullying | "Kimse seninle oynamak istemiyor", "Çirkinsin" |
| `SEXUAL` | 5 | Sexual content, body comments, inappropriate questions | "Vücudun güzel", "Hiç öpüştün mü?", "Ne giyiyorsun?" |
| `THREAT` | 6 | Physical threats, violence, blackmail | "Seni döverim", "Fotoğrafını yayarım" |

### Important: Category Boundaries

**GROOMING vs SEXUAL Distinction:**
- **GROOMING**: Non-sexual manipulation tactics (trust-building, secrecy, gift promises, meeting requests)
- **SEXUAL**: Any body-related comments, physical compliments, sexual questions, explicit content

```
"Kimseye söyleme tamam mı?"  → GROOMING (secrecy/isolation)
"Vücudun çok güzel"          → SEXUAL (body comment)
"Telefon alırım sana"        → GROOMING (gift promise)
"Dudakların çok güzel"       → SEXUAL (body-focused compliment)
"Gel evime yalnızım"         → GROOMING (meeting request/isolation)
"Hiç öpüştün mü?"            → SEXUAL (sexual experience question)
```

---

## Training Procedure

### Hyperparameters

| Parameter | Value |
|-----------|-------|
| **Base Model** | `dbmdz/bert-base-turkish-uncased` |
| **Max Sequence Length** | 64 tokens |
| **Batch Size** | 16 (effective 32 with gradient accumulation) |
| **Gradient Accumulation** | 2 steps |
| **Learning Rate** | 2e-5 (with cosine restarts) |
| **Epochs** | 2 |
| **Optimizer** | AdamW |
| **Weight Decay** | 0.01 |
| **Warmup Ratio** | 0.1 |
| **Loss Function** | Focal Loss (gamma=1.2) |
| **Label Smoothing** | 0.05 |
| **Problem Type** | Multi-label Classification |
| **Evaluation Strategy** | Per epoch |

### Training Environment

| Resource | Specification |
|----------|---------------|
| **Hardware** | Apple M1 Pro (MPS) |
| **Framework** | PyTorch 2.x + Transformers 4.37+ |
| **Training Time** | ~14 minutes (864 seconds) |
| **Throughput** | 157.8 samples/second |
| **Steps** | 4,258 total |

### Learning Rate Schedule

```
Peak LR: 2e-5 (after warmup)
Schedule: Cosine with restarts
Final LR: ~1.1e-8
```

---

## Usage

### Installation

```bash
pip install transformers torch
```

### Quick Start

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model
model_name = "hayatiali/turkish-safety"
tokenizer = AutoTokenizer.from_pretrained("dbmdz/bert-base-turkish-uncased")
model = AutoModelForSequenceClassification.from_pretrained(model_name)
model.eval()

# Label mapping (MUST match model's id2label)
LABELS = ["SAFE", "OFFENSIVE", "SELF_HARM", "GROOMING", "BULLYING", "SEXUAL", "THREAT"]

def predict(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)

    with torch.no_grad():
        outputs = model(**inputs)
        # Multi-label: use sigmoid (NOT softmax!)
        probs = torch.sigmoid(outputs.logits)[0].numpy()

    scores = {label: float(prob) for label, prob in zip(LABELS, probs)}
    primary = max(scores, key=scores.get)

    return {"category": primary, "confidence": scores[primary], "all_scores": scores}

# Examples
print(predict("Vücudun çok güzel"))       # → SEXUAL
print(predict("Kimseye söyleme tamam mı")) # → GROOMING
print(predict("Ölmek istiyorum"))          # → SELF_HARM
print(predict("Bugün hava güzel"))         # → SAFE
```

### Production Class

```python
class TurkishSafetyClassifier:
    LABELS = ["SAFE", "OFFENSIVE", "SELF_HARM", "GROOMING", "BULLYING", "SEXUAL", "THREAT"]

    def __init__(self, model_path="hayatiali/turkish-safety"):
        self.tokenizer = AutoTokenizer.from_pretrained("dbmdz/bert-base-turkish-uncased")
        self.model = AutoModelForSequenceClassification.from_pretrained(model_path)
        self.device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
        self.model.to(self.device).eval()

    def predict(self, text: str) -> dict:
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
        inputs = {k: v.to(self.device) for k, v in inputs.items()}

        with torch.no_grad():
            logits = self.model(**inputs).logits
            probs = torch.sigmoid(logits)[0].cpu().numpy()

        scores = dict(zip(self.LABELS, probs))
        primary = max(scores, key=scores.get)

        return {
            "category": primary,
            "confidence": scores[primary],
            "scores": scores,
            "action": self._get_action(scores[primary], primary)
        }

    def _get_action(self, score: float, category: str) -> str:
        # Critical categories have lower thresholds
        if category in ["GROOMING", "SEXUAL", "SELF_HARM", "THREAT"]:
            if score > 0.5: return "hard_block"
            if score > 0.3: return "soft_block"

        if score > 0.75: return "hard_block"
        if score > 0.60: return "soft_block"
        if score > 0.45: return "flag"
        if score > 0.30: return "allow_log"
        return "allow"
```

### Batch Inference

```python
def predict_batch(texts: list, batch_size: int = 32) -> list:
    results = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        inputs = tokenizer(batch, return_tensors="pt", truncation=True, max_length=128, padding=True)
        inputs = {k: v.to(device) for k, v in inputs.items()}

        with torch.no_grad():
            probs = torch.sigmoid(model(**inputs).logits).cpu().numpy()

        for prob in probs:
            scores = dict(zip(LABELS, prob))
            results.append(scores)

    return results
```

---

## Limitations & Known Issues

### ⚠️ Evaluation Limitations

**Note**: Two separate evaluation sets exist:
- **Automated Test Set**: 17,033 samples from test.csv → Macro F1: 0.9165, MCC: 0.9045
- **Manual Edge Case Test**: 22 hand-picked samples → 86.4% accuracy (19/22 correct)

| Limitation | Details | Impact |
|------------|---------|--------|
| **Small Manual Test Set** | Edge case validation on only 22 samples (86.4%) | Manual test not statistically significant; automated metrics (17K samples) more reliable |
| **No Per-Class Metrics** | Only Macro F1 and MCC reported for 17K test set | Cannot assess individual category performance (e.g., SELF_HARM Precision/Recall vs SAFE) |
| **No Confusion Matrix** | Category confusion patterns not documented | Unclear which categories are most confused beyond GROOMING/SEXUAL boundary |
| **No PR/ROC Curves** | Precision-Recall and ROC analysis not performed | Optimal threshold selection methodology not documented |
| **No Calibration Analysis** | Model confidence calibration not tested | Unknown if 0.7 confidence truly represents 70% probability |

### ⚠️ Architectural Limitations

| Limitation | Details | Impact |
|------------|---------|--------|
| **Short Context Window** | Max sequence length: 64 tokens | Long messages may lose critical information; truncation may remove key context |
| **Single-Turn Only** | No conversation history analysis | GROOMING patterns often emerge across multiple messages ("Kaç yaşındasın?", "Nerelisin?", "Fotoğraf atar mısın?" may each appear SAFE individually) |
| **No Temporal Patterns** | No escalation detection capability | Cannot detect behavior changes over time; user history not considered |
| **Static Analysis** | Each message analyzed independently | Contextual red flags from message sequences not captured |

### ⚠️ Data & Coverage Limitations

| Limitation | Details | Impact |
|------------|---------|--------|
| **Dialect/Slang Gaps** | Regional dialects and internet slang underrepresented | Performance may degrade on: "napıon", "nbr", "slm", "mrb", regional variations |
| **No Adversarial Testing** | Evasion techniques not systematically tested | Unknown robustness against: "S 3 x" instead of "sex", character substitution, unicode tricks |
| **Synthetic Data Bias** | 97.5% of training data is LLM-generated | May not capture real-world linguistic patterns; potential distribution shift |
| **Spelling Error Tolerance** | Not explicitly tested | Common typos and intentional misspellings may bypass detection |

### ⚠️ Production Deployment Considerations

| Consideration | Details | Recommendation |
|---------------|---------|----------------|
| **Threshold Selection** | Current thresholds (0.3, 0.5, 0.75) are heuristic | Perform PR curve analysis for your specific use case; adjust based on FP/FN tolerance |
| **Confidence Calibration** | Model may be over/under-confident | Consider temperature scaling or Platt calibration before production |
| **Category Boundaries** | GROOMING ↔ SEXUAL boundary is known issue | Review flagged content in these categories; implement human review for edge cases |
| **Real-Time Context** | No session-level analysis | Consider implementing sliding window or conversation aggregation layer |

### Not Suitable For

- Languages other than Turkish
- Adult content moderation (requires different domain expertise)
- Sole decision-making without human review for high-stakes situations
- Legal evidence or court proceedings
- Detection of sophisticated, multi-turn grooming attempts without additional context layer
- Highly informal/slang-heavy communications without additional preprocessing

---

## Ethical Considerations

### Intended Use

- Social media content moderation
- Messaging platform safety filters
- Gaming chat moderation
- Community forum monitoring
- Parental control applications
- Research and educational purposes

### Risks

- **False Negatives**: May miss sophisticated grooming attempts
- **False Positives**: May flag benign content incorrectly
- **Automation Bias**: Over-reliance on model predictions

### Recommendations

1. **Human Oversight**: Always combine with human review for critical decisions
2. **Threshold Calibration**: Adjust thresholds based on your risk tolerance
3. **Monitoring**: Track performance metrics in production
4. **Regular Updates**: Retrain with new data periodically
5. **Transparency**: Inform users about automated moderation

---

## Technical Specifications

### Model Architecture

```
BertForSequenceClassification(
  (bert): BertModel(
    (embeddings): BertEmbeddings
    (encoder): BertEncoder (12 layers)
    (pooler): BertPooler
  )
  (dropout): Dropout(p=0.1)
  (classifier): Linear(in_features=768, out_features=7)
)

Total Parameters: ~110M
Trainable Parameters: ~110M
```

### Input/Output

- **Input**: Turkish text (max 128 tokens)
- **Output**: 7-dimensional probability vector (sigmoid activated)
- **Tokenizer**: BERTurk WordPiece (32k vocab)

---

## Citation

```bibtex
@misc{turkish-safety-2025,
  title={Turkish Safety - Content Moderation Classifier},
  author={SiriusAI Tech Brain Team},
  year={2025},
  publisher={Hugging Face},
  howpublished={\url{https://huggingface.co/hayatiali/turkish-safety}},
  note={Fine-tuned from dbmdz/bert-base-turkish-uncased, Macro F1: 0.9076}
}
```

---

## Model Card Authors

**SiriusAI Tech Brain Team**

## Contact

- **Issues**: [GitHub Issues](https://github.com/sirius-tedarik/Omni-Moderation-API/issues)
- **Repository**: [Omni-Moderation-API](https://github.com/sirius-tedarik/Omni-Moderation-API)

---

## Changelog

### v5.0 (Current)
- Major dataset expansion: 85,161 samples (68,128 train / 17,033 test)
- Improved metrics: **Macro F1: 0.9165**, **MCC: 0.9045**
- Optimized hyperparameters for large dataset (Focal Loss, cosine restarts)
- 67 subcategories across 7 main categories
- 86.4% validation accuracy on edge cases

### v4.0
- Initial production release
- 7-category multi-label content safety classification
- Macro F1: 0.9076, MCC: 0.8931
- Training on 30,596 samples
- Clear category boundary definitions (GROOMING vs SEXUAL)
- Optimized for real-time inference (<50ms)

---

**License**: SiriusAI Tech Premium License v1.0

**Commercial Use**: Requires Premium License. Contact: info@siriusaitech.com

**Free Use Allowed For**:
- Academic research and education
- Non-profit organizations (with approval)
- Evaluation (30 days)

**Disclaimer**: This model is designed for content moderation and safety applications. Always implement with appropriate safeguards and human oversight. Model predictions should inform decisions, not replace human judgment.
