---
language:
- en
- ur
pipeline_tag: text-classification
tags:
- emotion-detection
- xlm-roberta
- multilingual
- roman-urdu
- code-mixed
- pakistan
- accuracy
- f1
library_name: transformers
license: mit
---

# xlm-roberta-multilingual-emotion-classifier

## Model Description

This model is a fine‑tuned version of **XLM‑RoBERTa‑base** for **7‑class emotion detection** in code‑mixed Pakistani text, including **English, Roman Urdu, and Urdu script**. It is designed for social media analysis, customer feedback, and multilingual NLP applications in the Pakistani context.

- **Base Model**: [xlm-roberta-base](https://huggingface.co/xlm-roberta-base)
- **Emotion Classes**: anger, disgust, fear, joy, neutral, sad, surprise
- **Language Support**: English, Roman Urdu, Urdu script

## Training Data & Balancing Strategy

### Data Sources
The training dataset was compiled from multiple sources:

| Source | Description |
|--------|-------------|
| [GoEmotions](https://www.kaggle.com/datasets/shivamb/go-emotions-google-emotions-dataset) | Subset of the Google emotion dataset |
| [Parul Pandey’s Emotion Dataset](https://www.kaggle.com/datasets/parulpandey/emotion-dataset) | Primary source (most samples) |
| [Roman Urdu‑English Code‑Switched Dataset](https://www.kaggle.com/datasets/drkhurramshahzad/roman-urdu-english-code-switched-emotion-dataset) | Specialised code‑mixed data |
| LLM‑generated samples (GPT, Grok, Gemini) | Used for English‑Urdu translation and augmentation |

### Cleaning & Preprocessing
- Duplicate rows removed
- Standardised column structure across three languages (English, Urdu, Roman Urdu)
- Seven emotion classes retained
- Light spelling normalisation for Roman Urdu

### Class Imbalance & Balancing Strategy

Initial raw data showed significant imbalance:
- **English**: Fear and Sad dominated (~14-16), Disgust very low (~7.1%).
- **Roman Urdu**: Fear as low as 8.1%, Sad relatively low.
- **Urdu**: More balanced but Sad often lowest.

#### Targeted Augmentation (Weak Classes)
We augmented **Sad, Disgust, Surprise** (and Fear/Joy where needed per language) using:

- **Random Swap (EDA)** for Urdu and Roman Urdu – swaps two random words, preserving sentiment while increasing structural variety.
- **Oversampling + Cross‑Lingual Injection** for English Disgust – duplicated high‑quality samples and added code‑switched (English + Roman Urdu) variants.
- **LLM‑based translation** (GPT, Grok, Gemini) to generate parallel English‑Urdu/Roman Urdu versions.

**Approximate additional samples added:**
- Total synthetic/augmented samples: **~2,000–2,500**
- English Disgust: +334 samples (~30% of that class augmented)
- Urdu/Roman Urdu weak classes (Surprise, Disgust): +400–500 samples each

#### Majority Class Control (Mild Downsampling)
We randomly under‑sampled the **majority English classes** (Anger, Fear, Sad) to prevent bias:
- Original counts: ~1,400–1,600 each
- Reduced by ~200–400 samples to a ceiling of ~1,200 each

#### Quality Controls
- Augmentation applied **to the master dataset before train/test split** (so test set also contains augmented variants, proving model robustness).
- Stratified split ensures balanced representation across languages and emotions.
- Manual spot‑check performed on augmented Roman Urdu samples.

### Final Dataset Statistics

**Total rows:** 20,235  
**Languages:** English (7,734), Roman Urdu (5,572), Urdu (6,929)  

**Per‑language emotion counts (exact numbers used in training):**

| Language     | anger | disgust | fear | joy | neutral | sad | surprise | Total |
|--------------|-------|---------|------|-----|---------|-----|----------|-------|
| English      | 1128  | 1106    | 1207 | 1200| 1004    | 1207| 882      | 7734  |
| Roman Urdu   | 839   | 791     | 839  | 839 | 839     | 691 | 734      | 5572  |
| Urdu         | 1009  | 935     | 1059 | 980 | 948     | 1059| 939      | 6929  |
| **Total**    | 2976  | 2832    | 3105 | 3019| 2791    | 2957| 2555     | 20235 |

**Global percentages:**  
- Highest: Fear (~15.34%)  
- Lowest: Surprise (~12.63%)  
- Others: 13.8% – 14.9%

The final dataset is **much more balanced** than raw sources, with all classes represented across all three languages.

## Training Details

- **Framework**: PyTorch + Hugging Face Transformers
- **Model**: XLM‑RoBERTa‑base (12 layers, 278M parameters)
- **Optimizer**: AdamW (learning rate = 2e‑5)
- **Batch size**: 32
- **Epochs**: 5 (early stopping patience = 2)
- **Max sequence length**: 128 tokens
- **Warmup steps**: 10% of total steps
- **Weight decay**: 0.01
- **FP16**: Enabled (GPU acceleration)

## Evaluation Results

The model was evaluated on a held‑out test set of **4,047 samples** (20% of total data, stratified).
### Overall Performance
- **Accuracy**: **83.4%**
- **Macro F1‑score**: **0.835**
- **Weighted F1‑score**: **0.833**

### Per‑Class Performance

| Emotion  | Precision | Recall | F1‑score | Support |
|----------|-----------|--------|----------|---------|
| anger    | 0.83      | 0.87   | 0.85     | 595     |
| disgust  | 0.90      | 0.93   | 0.91     | 567     |
| fear     | 0.93      | 0.90   | 0.92     | 621     |
| joy      | 0.82      | 0.79   | 0.81     | 604     |
| neutral  | 0.77      | 0.75   | 0.76     | 558     |
| sad      | 0.75      | 0.75   | 0.75     | 591     |
| surprise | 0.80      | 0.81   | 0.81     | 511     |

### Confusion Matrix (Actual vs. Predicted)

| Actual ↓ / Predicted → | anger | disgust | fear | joy | neutral | sad | surprise |
|------------------------|-------|---------|------|-----|---------|-----|----------|
| **anger**              | 518   | 10      | 13   | 10  | 12      | 26  | 6        |
| **disgust**            | 9     | 526     | 2    | 0   | 13      | 8   | 9        |
| **fear**               | 7     | 3       | 560  | 0   | 0       | 2   | 49       |
| **joy**                | 6     | 3       | 0    | 480 | 54      | 38  | 23       |
| **neutral**            | 9     | 19      | 2    | 39  | 418     | 64  | 7        |
| **sad**                | 52    | 23      | 2    | 29  | 34      | 443 | 8        |
| **surprise**           | 21    | 2       | 23   | 30  | 13      | 8   | 414      |

### Per‑Language Accuracy

| Language    | Accuracy | Samples |
|-------------|----------|---------|
| English     | **84.5%**| 851     |
| Roman Urdu  | **80.8%**| 506     |
| Urdu        | **84.0%**| 681     |