---
language:
  - sw
license: apache-2.0
library_name: transformers
tags:
  - sentiment-analysis
  - kiswahili
  - swahili
  - text-classification
  - distilbert
  - pseudo-labeling
  - low-resource
  - african-languages
datasets:
  - mozilla-foundation/common_voice_17_0
pipeline_tag: text-classification
model-index:
  - name: kiswahili-sentiment-distilbert
    results:
      - task:
          type: text-classification
          name: Sentiment Analysis
        dataset:
          name: Mozilla Common Voice Kiswahili (Pseudo-labeled)
          type: mozilla-foundation/common_voice_17_0
          config: sw
          split: test
        metrics:
          - type: f1
            value: 0.6125
            name: Weighted F1-Score
base_model: distilbert-base-multilingual-cased
---

# Kiswahili Sentiment Analysis — DistilBERT

A fine-tuned **DistilBERT** model for sentiment classification of Kiswahili (Swahili) text. This model classifies text into **positive** or **negative** sentiment categories.

## Model Description

This model was developed as part of the **Tubonge — Kiswahili Speech Analytics System**, a research project addressing the lack of NLP tools for low-resource African languages. Since no labeled sentiment dataset exists for Kiswahili, the model was trained using a **pseudo-labeling** methodology that transfers sentiment knowledge from English to Kiswahili through cross-lingual translation.

| Property | Value |
|---|---|
| **Base Model** | `distilbert-base-multilingual-cased` |
| **Architecture** | DistilBertForSequenceClassification |
| **Parameters** | ~134M (multilingual vocab: 119,547 tokens) |
| **Language** | Kiswahili (sw) |
| **Task** | Binary Sentiment Classification |
| **Framework** | PyTorch / Hugging Face Transformers 4.40.2 |

## Training Procedure

### Pseudo-Labeling Pipeline

Due to the absence of annotated sentiment data for Kiswahili, a cross-lingual pseudo-labeling approach was employed:

1. **Source Data**: 18,629 validated Kiswahili transcriptions from the Mozilla Common Voice dataset
2. **Translation**: Each Kiswahili text was translated to English using [NLLB-200-distilled-600M](https://huggingface.co/facebook/nllb-200-distilled-600M)
3. **Label Generation**: A pre-trained English sentiment classifier assigned sentiment labels to the translated text
4. **Label Transfer**: The generated labels were mapped back to the original Kiswahili text
5. **Fine-tuning**: `distilbert-base-multilingual-cased` was fine-tuned on the pseudo-labeled Kiswahili dataset

### Training Hyperparameters

| Parameter | Value |
|---|---|
| Learning Rate | 2e-5 |
| Batch Size | 16 |
| Epochs | 3 |
| Optimizer | AdamW |
| Warmup Steps | 500 |
| Max Sequence Length | 128 |
| Weight Decay | 0.01 |
| Data Split | 80% train / 10% val / 10% test |

## Evaluation Results

| Metric | Value |
|---|---|
| **Weighted F1-Score** | 0.6125 |

The F1-score of 0.6125 represents a meaningful achievement for a language with zero manually annotated sentiment data. The moderate score reflects inherent limitations of the pseudo-labeling approach, including translation noise and cultural differences in sentiment expression.

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("RareElf/kiswahili-sentiment-distilbert")
model = AutoModelForSequenceClassification.from_pretrained("RareElf/kiswahili-sentiment-distilbert")

# Classify sentiment
text = "Habari yako, nimefurahi sana kukutana nawe"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)

with torch.no_grad():
    outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=-1)
    predicted_class = torch.argmax(probs, dim=-1).item()

sentiment_map = {0: "negative", 1: "positive"}
print(f"Sentiment: {sentiment_map[predicted_class]}")
print(f"Confidence: {probs[0][predicted_class].item():.2%}")
```

### Using the Pipeline API

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="RareElf/kiswahili-sentiment-distilbert"
)

result = classifier("Hii ni siku nzuri sana")
print(result)
```

## Intended Use

- Sentiment analysis of Kiswahili text from speech transcriptions
- Monitoring sentiment trends in Kiswahili audio content
- Research on low-resource language NLP and cross-lingual transfer learning
- Integration into Kiswahili speech analytics pipelines

## Limitations

- **Pseudo-label noise**: Sentiment labels were generated through translation, introducing potential errors from translation inaccuracies and cultural differences in sentiment expression
- **Domain specificity**: Trained on Mozilla Common Voice transcriptions, which consist primarily of short read-aloud sentences; performance may vary on conversational or domain-specific text
- **Binary classification**: The model classifies into positive/negative categories; neutral sentiment detection is limited
- **Dialect coverage**: May not generalise equally to all Kiswahili dialects and regional variations

## Citation

If you use this model in your research, please cite:

```bibtex
@misc{obote2025kiswahili-sentiment,
  author = {Obote, Kevin},
  title = {Kiswahili Sentiment Analysis using Pseudo-Labeled DistilBERT},
  year = {2025},
  publisher = {Hugging Face},
  url = {https://huggingface.co/RareElf/kiswahili-sentiment-distilbert}
}
```

## Related Models

- [RareElf/swahili-wav2vec2-asr](https://huggingface.co/RareElf/swahili-wav2vec2-asr) — Kiswahili ASR model used in the same pipeline
- [facebook/nllb-200-distilled-600M](https://huggingface.co/facebook/nllb-200-distilled-600M) — Translation model used for pseudo-labeling
- [google/mt5-small](https://huggingface.co/google/mt5-small) — Summarization model used in the pipeline

## Model Card Contact

Kevin Obote — [RareElf on Hugging Face](https://huggingface.co/RareElf)
