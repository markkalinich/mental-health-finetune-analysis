---
pretty_name: "CamemBERT Sentiment — Services Publics FR"
language: fr
license: mit
library_name: transformers
pipeline_tag: text-classification
model_type: camembert
base_model: camembert-base

tags:
  - sentiment-analysis
  - camembert
  - french
  - sequence-classification
  - public-services
  - user-feedback

# Dataset non-HF -> utiliser un slug simple (pas d'URL, pas de '/')
datasets:
  - data-gouv-fr-services-publics-plus

metrics:
  - accuracy
  - f1

widget:
  - text: "Accueil très aimable, explications claires, je suis satisfait."
    example_title: "Positive feedback"
  - text: "Je n'ai pas d'avis particulier sur la question."
    example_title: "Neutral feedback"
  - text: "Très déçu, aucune réponse à mes emails depuis des semaines."
    example_title: "Negative feedback"

model-index:
  - name: fr-camembert-spplus-sentiment
    results:
      - task:
          type: text-classification
          name: Sentiment Analysis
        dataset:
          name: Services Publics Plus (data.gouv.fr)
          type: data-gouv-fr-services-publics-plus
          split: test
          args:
            language: fr
        metrics:
          - type: accuracy
            value: 0.9076
          - type: f1
            name: f1_macro
            value: 0.7495
          - type: f1
            name: f1_weighted
            value: 0.9090
---


# CamemBERT for French Public Services Sentiment Analysis

## Model Description

**fr-camembert-spplus-sentiment** is a fine-tuned version of `camembert-base` specifically designed for sentiment classification of French user feedback in public services contexts. The model classifies text into three sentiment categories:

- **🔴 Négatif** (Negative) - Label ID: 0
- **⚪ Neutre** (Neutral) - Label ID: 1  
- **🟢 Positif** (Positive) - Label ID: 2

## Dataset Information

This model was trained on the official French government open dataset ["Liste des expériences partagées par les usagers"](https://www.data.gouv.fr/datasets/liste-des-experiences-partagees-par-les-usagers/) from data.gouv.fr. 

The dataset contains real user experiences shared through the **Services Publics Plus** platform, a government initiative led by the Direction Interministérielle de la Transformation Publique (DITP) to improve public service quality. The platform allows citizens to share their experiences with French public services, which are then moderated and published as open data.

## Model Details
- **Source**: Official French government platform (Services Publics Plus)
- **Moderation**: All experiences are moderated to ensure compliance with guidelines
- **Scope**: Covers all French public services and government administrations
- **Authenticity**: Real citizen feedback, not synthetic or scraped data
- **Transparency**: Fully open dataset available to the public

The dataset includes various metadata such as:
- Geographic information (department, region)
- Service channels (phone, email, in-person, online, etc.)
- Service categories and administrative structures
- Response tracking and follow-up actions

- **Base Model**: `camembert-base`
- **Language**: French (fr)
- **Task**: Text Classification (Sentiment Analysis)
- **Domain**: Public services user feedback
- **Model Type**: CamemBERT (RoBERTa-like for French)
- **License**: MIT
- **Authors**: Olivier Caron

## Intended Use

### Primary Use Cases
- Analyzing sentiment in French public service feedback
- Monitoring citizen satisfaction with government services
- Automated classification of user complaints and compliments
- Quality assessment of public service interactions

### Out-of-Scope Use
- General sentiment analysis outside public services domain
- Toxicity or harmful content detection
- Analysis of languages other than French

## How to Use

### Quick Start with Pipeline (Recommended)

```python
from transformers import pipeline

# Initialize the sentiment analysis pipeline
classifier = pipeline(
    "text-classification",
    model="oliviercaron/fr-camembert-spplus-sentiment",
    device_map="auto",
    top_k=None  # Return scores for all classes
)

# Example texts
texts = [
    "Accueil très aimable, explications claires, je suis satisfait.",
    "Je n'ai pas d'avis particulier sur la question.",
    "Très déçu, aucune réponse à mes emails depuis des semaines.",
    "Le service était correct, sans plus."
]

# Get predictions
results = classifier(texts)

# Display results
for text, result in zip(texts, results):
    print(f"Text: {text}")
    for prediction in result:
        print(f"  {prediction['label']}: {prediction['score']:.4f}")
    print()

# Expected output:
# Text: Accueil très aimable, explications claires, je suis satisfait.
#   Positif: 0.9990
#   Neutre: 0.0007
#   Négatif: 0.0002
#
# Text: Je n'ai pas d'avis particulier sur la question.
#   Neutre: 0.9790
#   Négatif: 0.0128
#   Positif: 0.0082
#
# Text: Très déçu, aucune réponse à mes emails depuis des semaines.
#   Négatif: 0.9873
#   Neutre: 0.0117
#   Positif: 0.0010
#
# Text: Le service était correct, sans plus.
#   Neutre: 0.9695
#   Positif: 0.0199
#   Négatif: 0.0106
```

### Manual Usage with Tokenizer and Model

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load model and tokenizer
model_name = "oliviercaron/fr-camembert-spplus-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Set device
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)
model.eval()

# Example text
text = "Le personnel était compétent et à l'écoute."

# Tokenize and predict
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
inputs = {k: v.to(device) for k, v in inputs.items()}

with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)

# Get results
labels = ["Négatif", "Neutre", "Positif"]
for i, (label, score) in enumerate(zip(labels, predictions[0])):
    print(f"{label}: {score:.4f}")
```

## Training Details

### Training Data
- **Dataset**: [Liste des expériences partagées par les usagers](https://www.data.gouv.fr/datasets/liste-des-experiences-partagees-par-les-usagers/) (Open Data France)
- **Source**: Services Publics Plus platform - Direction Interministérielle de la Transformation Publique (DITP)
- **Domain**: French public services and government administration
- **Language**: French
- **Labels**: User sentiment feedback classified as "Négatif", "Neutre", or "Positif"
- **Collection**: Real user experiences shared on the Services Publics Plus platform, moderated before publication
- **License**: Open Data (data.gouv.fr)

### Training Procedure
- **Base Model**: `camembert-base`
- **Tokenizer**: SentencePiece (CamemBERT tokenizer)
- **Max Sequence Length**: 512 tokens
- **Training Framework**: PyTorch with Transformers
- **Mixed Precision**: FP16 enabled for faster training
- **Early Stopping**: Based on F1-macro score with patience of 3 epochs
- **Reproducibility**: Fixed seed (42) for consistent results

### Hyperparameters
| Parameter | Value |
|-----------|-------|
| Learning Rate | 2e-05 |
| Train Batch Size | 16 |
| Eval Batch Size | 64 |
| Weight Decay | 0.01 |
| Max Epochs | 10 |
| Neutral Class Boost | 1.8 |

## Performance

### Overall Metrics
| Metric | Score |
|--------|-------|
| **Accuracy** | 0.9076 |
| **F1 Macro** | 0.7495 |
| **F1 Weighted** | 0.9090 |

### Per-Class Performance
| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| **Négatif** | 0.9480 | 0.9515 | 0.9498 | 8,582 |
| **Neutre** | 0.3504 | 0.3784 | 0.3639 | 761 |
| **Positif** | 0.9525 | 0.9176 | 0.9348 | 2,537 |

### Confusion Matrix
|              | Pred. Négatif | Pred. Neutre | Pred. Positif |
|--------------|---------------|--------------|---------------|
| **True Négatif** | 8,166 | 381 | 35 |
| **True Neutre**  | 392 | 288 | 81 |
| **True Positif** | 56 | 153 | 2,328 |

## Limitations and Bias

### Known Limitations
1. **Neutral Class Performance**: The model shows lower performance on neutral sentiment due to class imbalance in the training data
2. **Subjective Labeling**: User sentiment perception may differ from objective evaluation. Citizens often express dissatisfaction even for minor service issues, leading to a natural bias towards negative classifications
3. **Domain Specificity**: Optimized for public services feedback, performance may vary on other domains
4. **Language**: Designed specifically for French text
5. **Context Dependency**: Performance may vary with informal language or domain-specific jargon
