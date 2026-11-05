---
language: en
license: apache-2.0
tags:
- text-classification
- emotion-recognition
- distilroberta
- pytorch
- transformers
datasets:
- DailyDialog
- ISEAR
- MELD
metrics:
- accuracy
- f1
widget:
- text: "I'm so happy today!"
  example_title: "Happy"
- text: "This makes me really angry"
  example_title: "Angry"
- text: "I'm scared of what might happen"
  example_title: "Fear"
- text: "That's completely disgusting"
  example_title: "Disguust"
- text: "I feel so sad about this"
  example_title: "Sadness"
- text: "What a surprise!"
  example_title: "Surprise"
- text: "This is a normal day"
  example_title: "Neutral"
---

# DistilRoBERTa for Emotion Classification

## Model Description

This model is a fine-tuned version of `distilroberta-base` for multi-class emotion classification. It can classify text into 7 emotion categories: Neutral, Happiness, Anger, Sadness, Surprise, Disgust, and Fear.

## Model Details

- **Model Type:** Text Classification
- **Base Model:** distilroberta-base
- **Language:** English
- **Task:** Multi-class Emotion Classification
- **Classes:** ['Anger', 'Disgust', 'Fear', 'Happiness', 'Neutral', 'Sadness', 'Surprise']

## Dataset

### Overview
The model was trained on a comprehensive emotion recognition dataset created by aggregating and preprocessing three publicly available datasets: **DailyDialog**, **ISEAR**, and **MELD**. The final dataset contains **68,301 samples** across 7 emotion classes.

### Source Datasets
- **DailyDialog**: ~13,000 conversational dialogs with emotion labels
- **ISEAR**: ~7,600 self-reported emotional experiences
- **MELD**: ~14,000 multimedia dialog utterances with emotion labels

### Preprocessing Pipeline
The dataset underwent extensive preprocessing to ensure quality and balance:

#### 1. Data Cleaning & Unification
- **Mojibake correction**: Fixed encoding artifacts (e.g., â€™ → ')
- **Text normalization**: Standardized quotes, removed escaped characters
- **Social media cleanup**: Removed mentions, hashtags, and emojis from ISEAR
- **Emotion mapping**: Unified emotion labels across all three datasets
- **Result**: 124,723 initial samples

#### 2. Deduplication
- Removed 3 samples with missing text
- Eliminated 18,624 duplicate samples (14.93%)
- **Result**: 106,096 unique samples

#### 3. Class Balance Correction
**Original distribution** (severely imbalanced):
- Neutral: 76,762 (72.35%)
- Happiness: 14,337 (13.51%)
- Anger: 4,112 (3.88%)
- Sadness: 3,580 (3.37%)
- Surprise: 2,872 (2.71%)
- Disgust: 2,306 (2.17%)
- Fear: 2,127 (2.00%)

**Balancing strategy**:
- Undersampled Neutral class to 19,190 samples
- Preserved minority classes for natural distribution
- **Result**: 37,771 balanced samples

#### 4. Data Augmentation
Applied targeted augmentation techniques to enhance diversity and address minority class underrepresentation:

**Techniques used**:
- **Synonym Replacement**: Replaced words with synonyms while preserving emotion keywords
- **Character Noise**: Added random characters to simulate typos
- **Emotion Intensifiers**: Added emotion-specific adjectives
- **Paraphrasing**: Used T5-small model for sentence rephrasing

**Augmentation results**:
- Fear: 2,127 → 5,000 samples
- Disgust: 2,306 → 5,001 samples  
- Surprise: 2,872 → 5,000 samples
- Sadness: 3,580 → 5,002 samples
- Anger: 4,112 → 5,001 samples
- Happiness: 3,584 → 5,001 samples
- Neutral: 19,190 → 38,296 samples

**Total augmented samples**: 30,530 (44.69% of final dataset)

### Final Dataset Characteristics

**Size**: 68,301 samples total
- Original samples: 37,771 (55.31%)
- Augmented samples: 30,530 (44.69%)

**Class Distribution**:
| Emotion | Count | Percentage |
|---------|-------|------------|
| Neutral | 38,296 | 56.06% |
| Sadness | 5,002 | 7.32% |
| Happiness | 5,001 | 7.32% |
| Disgust | 5,001 | 7.32% |
| Anger | 5,001 | 7.32% |
| Fear | 5,000 | 7.32% |
| Surprise | 5,000 | 7.32% |

**Text Statistics**:
- Average text length: 74.4 characters
- Average word count: 15.1 words
- Text length range: 1-1,158 characters

**Dataset Splits**:
- Training: 26,439 samples (70%)
- Validation: 5,666 samples (15%)
- Test: 5,666 samples (15%)

*Splits were created using stratified sampling to maintain proportional class representation across all sets.*

## Performance

### Overall Metrics
- **Accuracy:** 0.8103
- **F1-Score (Macro):** 0.7286
- **F1-Score (Weighted):** 0.8096

### Per-Emotion Performance
| Emotion | Precision | Recall | F1-Score | Support |
|---------|-----------|--------|----------|---------|
| Anger | 0.5797 | 0.6107 | 0.5948 | 750 |
| Disgust | 0.7923 | 0.7427 | 0.7667 | 750 |
| Fear | 0.8800 | 0.8213 | 0.8497 | 750 |
| Happiness | 0.6383 | 0.5693 | 0.6018 | 750 |
| Neutral | 0.8876 | 0.9020 | 0.8948 | 5745 |
| Sadness | 0.6905 | 0.6565 | 0.6730 | 751 |
| Surprise | 0.6839 | 0.7587 | 0.7193 | 750 |

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("jihedjabnoun/text-emotion-distilroberta")
model = AutoModelForSequenceClassification.from_pretrained("jihedjabnoun/text-emotion-distilroberta")

# Prepare text
text = "I'm feeling great today!"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)

# Get prediction
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    predicted_class = torch.argmax(predictions, dim=-1)

# Map to label
emotions = {0: 'Anger', 1: 'Disgust', 2: 'Fear', 3: 'Happiness', 4: 'Neutral', 5: 'Sadness', 6: 'Surprise'}
predicted_emotion = emotions[predicted_class.item()]
print(f"Predicted emotion: {predicted_emotion}")
```

## Training Details

- **Training Framework:** Transformers
- **Optimizer:** AdamW
- **Learning Rate:** 2e-5
- **Batch Size:** 16
- **Max Sequence Length:** 128
- **Epochs:** 3
- **Warmup Steps:** 500

## Limitations and Considerations

- The dataset maintains some class imbalance with Neutral being dominant (56.06%)
- Augmented samples comprise 44.69% of the dataset, which may introduce synthetic artifacts
- Performance varies across emotion classes, with Fear and Neutral showing highest F1-scores
- The model is optimized for English text and may not generalize to other languages

## 🤝 Contact & Support
- **Model Repository**: [jihedjabnoun/text-emotion-distilroberta](https://huggingface.co/jihedjabnoun/text-emotion-distilroberta)
- **Issues**: Please report bugs or issues in the model repository
- **Improvements**: Suggestions for model improvements are welcome
- **Mail**: jihed.jabnoun@fsm.u-monastir.tn

## Citation

```bibtex
@misc{text-emotion-distilroberta,
    title={DistilRoBERTa for Emotion Classification},
    author={Jihed Jabnoun},
    year={2025},
    url={https://huggingface.co/jihedjabnoun/text-emotion-distilroberta}
}
```