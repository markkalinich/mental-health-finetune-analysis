---
library_name: transformers
license: mit
base_model: jhu-clsp/mmBERT-small
tags:
- sentiment
- text-classification
- multilingual
- modernbert
- sentiment-analysis
- product-reviews
- place-reviews
- mmbert
metrics:
- f1
- precision
- recall
model-index:
- name: mmBERT-small-multilingual-sentiment
  results: []
datasets:
- clapAI/MultiLingualSentiment
language:
- en
- zh
- vi
- ko
- ja
- ar
- de
- es
- fr
- hi
- id
- it
- ms
- pt
- ru
- tr
pipeline_tag: text-classification
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# clapAI/mmBERT-small-multilingual-sentiment

## Introduction

**mmBERT-small-multilingual-sentiment** is a multilingual sentiment classification model, part of
the [Multilingual-Sentiment](https://huggingface.co/collections/clapAI/multilingual-sentiment-677416a6b23e03f52cb6cc3f)
collection.

The model is fine-tuned from [jhu-clsp/mmBERT-small](https://huggingface.co/jhu-clsp/mmBERT-small) using the
multilingual sentiment
dataset [clapAI/MultiLingualSentiment](https://huggingface.co/datasets/clapAI/MultiLingualSentiment).

Model supports multilingual sentiment classification across 16+ languages, including English, Vietnamese, Chinese,
French, Spanish, Portuguese, German, Italian, Russian, Japanese, Korean, Arabic, and more.

## Key Highlights
> 📈 **Improved accuracy**: Achieves **F1 = 82.2**.  
> 📜 **Long context support**: Handles sequences up to **8192 tokens**.  
> 🪶 **Efficient size**: Only **140M parameters**, smaller than RoBERTa-base (278M) with better performance.  
> ⚡ **FlashAttention-2 support**: Enables much faster inference on modern GPUs.

## Evaluation & Performance

Results on the test split
of [clapAI/MultiLingualSentiment](https://huggingface.co/datasets/clapAI/MultiLingualSentiment)

|                                                      Model                                                      |                            Pretrained Model                            | Parameters | Context-length | F1-score |
|:---------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------:|:----------:|----------------|:--------:|
| [clapAI/mmBERT-small-multilingual-sentiment](https://huggingface.co/clapAI/mmBERT-small-multilingual-sentiment) | [jhu-clsp/mmBERT-small](https://huggingface.co/jhu-clsp/mmBERT-small)  |    140M    | 8192           | **82.2** |
| [modernBERT-base-multilingual-sentiment](https://huggingface.co/clapAI/modernBERT-base-multilingual-sentiment)  | [ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base)  |    150M    | 8192           |  80.16   |
|    [roberta-base-multilingual-sentiment](https://huggingface.co/clapAI/roberta-base-multilingual-sentiment)     | [XLM-roberta-base](https://huggingface.co/FacebookAI/xlm-roberta-base) |    278M    | 512            |   81.8   | 

## How to use

### Installation

```bash
pip install torch==2.8
pip install transformers==4.55.0
```

`Optional: accelerate inference with FlashAttention-2 (if supported by your GPU):`

```bash
pip install packaging==25.0 ninja==1.13.0
MAX_JOBS=4 pip install flash-attn==2.8.3 --no-build-isolation
```

### Example Usage

Try it on [Google Colab](https://colab.research.google.com/drive/1nsh22sEz0znV3OedE8RqA0dNoPOJjghJ?usp=sharing)

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model_id = "clapAI/mmBERT-small-multilingual-sentiment"
# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_id)
dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
model = AutoModelForSequenceClassification.from_pretrained(
    model_id,
    torch_dtype=dtype,
    # Uncomment if device supports FA2
    # attn_implementation="flash_attention_2" 
)

model.to(device)
model.eval()

# Retrieve labels from the model's configuration
id2label = model.config.id2label

texts = [
    "I absolutely love the new design of this app!",  # English
    "الخدمة كانت سيئة للغاية.",
    "Ich bin sehr zufrieden mit dem Kauf.",  # German
    "El producto llegó roto y no funciona.",  # Spanish
    "J'adore ce restaurant, la nourriture est délicieuse!",  # French
    "Makanannya benar-benar tidak enak.",  # Indonesian
    "この製品は本当に素晴らしいです！",  # Japanese
    "고객 서비스가 정말 실망스러웠어요.",  # Korean
    "Этот фильм просто потрясающий!",  # Russian
    "Tôi thực sự yêu thích sản phẩm này!",  # Vietnamese
    "质量真的很差。"  # Chinese
]

for text in texts:
    inputs = tokenizer(text, return_tensors="pt").to(device)
    with torch.inference_mode():
        outputs = model(**inputs)
        prediction = id2label[outputs.logits.argmax(dim=-1).item()]
    print(f"Text: {text} | Prediction: {prediction}")
```

## Citation

If you use this model, please consider citing:

```bibtex
@misc{clapAI_mmbert_small_multilingual_sentiment,
      title={mmBERT-small-multilingual-sentiment: A Multilingual Sentiment Classification Model},
      author={clapAI},
      howpublished={\url{https://huggingface.co/clapAI/mmBERT-small-multilingual-sentiment}},
      year={2025},
}