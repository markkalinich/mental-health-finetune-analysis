---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-large
tags:
- sentiment
- text-classification
- multilingual
- modernbert
- sentiment-analysis
- product-reviews
- place-reviews
metrics:
- f1
- precision
- recall
model-index:
- name: clapAI/modernBERT-large-multilingual-sentiment
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

# clapAI/modernBERT-base-multilingual-sentiment

## Introduction

**modernBERT-base-multilingual-sentiment** is a multilingual sentiment classification model, part of
the [Multilingual-Sentiment](https://huggingface.co/collections/clapAI/multilingual-sentiment-677416a6b23e03f52cb6cc3f)
collection.

The model is fine-tuned from [answerdotai/ModernBERT-large](https://huggingface.co/answerdotai/ModernBERT-large) using the
multilingual sentiment
dataset [clapAI/MultiLingualSentiment](https://huggingface.co/datasets/clapAI/MultiLingualSentiment).

Model supports multilingual sentiment classification across 16+ languages, including English, Vietnamese, Chinese,
French, Spanish, Portuguese, German, Italian, Russian, Japanese, Korean, Arabic, and more.

## Evaluation & Performance

After fine-tuning, the best model is loaded and evaluated on the `test` dataset
from [clapAI/MultiLingualSentiment](https://huggingface.co/datasets/clapAI/MultiLingualSentiment)


|                                                      Model                                                       | Pretrained Model  | Parameters | F1-score |
|:----------------------------------------------------------------------------------------------------------------:|:-----------------:|:----------:|:--------:|
|  [modernBERT-base-multilingual-sentiment](https://huggingface.co/clapAI/modernBERT-base-multilingual-sentiment)  |  ModernBERT-base  |    150M    |  80.16   |
| [modernBERT-large-multilingual-sentiment](https://huggingface.co/clapAI/modernBERT-large-multilingual-sentiment) | ModernBERT-large  |    396M    |   81.4   |
|     [roberta-base-multilingual-sentiment](https://huggingface.co/clapAI/roberta-base-multilingual-sentiment)     | XLM-roberta-base  |    278M    |   81.8   | 
|    [roberta-large-multilingual-sentiment](https://huggingface.co/clapAI/roberta-large-multilingual-sentiment)    | XLM-roberta-large |    560M    |   82.6   | 

## How to use

### Requirements

Since **transformers** only supports the **ModernBERT** architecture from version `4.48.0.dev0`, use the following
command to get the required version:

```bash
pip install "git+https://github.com/huggingface/transformers.git@6e0515e99c39444caae39472ee1b2fd76ece32f1" --upgrade
```

Install **FlashAttention** to accelerate inference performance

```bash
pip install flash-attn==2.7.2.post1
```

### Quick start

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model_id = "clapAI/modernBERT-large-multilingual-sentiment"
# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id, torch_dtype=torch.float16)

model.to(device)
model.eval()


# Retrieve labels from the model's configuration
id2label = model.config.id2label

texts = [
    # English
    {
        "text": "I absolutely love the new design of this app!",
        "label": "positive"
    },
    {
        "text": "The customer service was disappointing.",
        "label": "negative"
    },
    # Arabic
    {
        "text": "هذا المنتج رائع للغاية!",
        "label": "positive"
    },
    {
        "text": "الخدمة كانت سيئة للغاية.",
        "label": "negative"
    },
    # German
    {
        "text": "Ich bin sehr zufrieden mit dem Kauf.",
        "label": "positive"
    },
    {
        "text": "Die Lieferung war eine Katastrophe.",
        "label": "negative"
    },
    # Spanish
    {
        "text": "Este es el mejor libro que he leído.",
        "label": "positive"
    },
    {
        "text": "El producto llegó roto y no funciona.",
        "label": "negative"
    },
    # French
    {
        "text": "J'adore ce restaurant, la nourriture est délicieuse!",
        "label": "positive"
    },
    {
        "text": "Le service était très lent et désagréable.",
        "label": "negative"
    },
    # Indonesian
    {
        "text": "Saya sangat senang dengan pelayanan ini.",
        "label": "positive"
    },
    {
        "text": "Makanannya benar-benar tidak enak.",
        "label": "negative"
    },
    # Japanese
    {
        "text": "この製品は本当に素晴らしいです！",
        "label": "positive"
    },
    {
        "text": "サービスがひどかったです。",
        "label": "negative"
    },
    # Korean
    {
        "text": "이 제품을 정말 좋아해요!",
        "label": "positive"
    },
    {
        "text": "고객 서비스가 정말 실망스러웠어요.",
        "label": "negative"
    },
    # Russian
    {
        "text": "Этот фильм просто потрясающий!",
        "label": "positive"
    },
    {
        "text": "Качество было ужасным.",
        "label": "negative"
    },
    # Vietnamese
    {
        "text": "Tôi thực sự yêu thích sản phẩm này!",
        "label": "positive"
    },
    {
        "text": "Dịch vụ khách hàng thật tệ.",
        "label": "negative"
    },
    # Chinese
    {
        "text": "我非常喜欢这款产品！",
        "label": "positive"
    },
    {
        "text": "质量真的很差。",
        "label": "negative"
    }
]

for item in texts:
    text = item["text"]
    label = item["label"]

    inputs = tokenizer(text, return_tensors="pt").to(device)

    # Perform inference in inference mode
    with torch.inference_mode():
        outputs = model(**inputs)
        predictions = outputs.logits.argmax(dim=-1)
    print(f"Text: {text} | Label: {label} | Prediction: {id2label[predictions.item()]}")


```

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:

```yaml
learning_rate: 5e-05
train_batch_size: 512
eval_batch_size: 512
seed: 42
distributed_type: multi-GPU
num_devices: 2
gradient_accumulation_steps: 2
total_train_batch_size: 2048
total_eval_batch_size: 1024
optimizer:
  type: adamw_torch_fused
  betas: [ 0.9, 0.999 ]
  epsilon: 1e-08
  optimizer_args: "No additional optimizer arguments"
lr_scheduler:
  type: cosine
  warmup_ratio: 0.01
num_epochs: 5.0
mixed_precision_training: Native AMP

```

### Framework versions

```plaintex
transformers==4.48.0.dev0
torch==2.4.0+cu121
datasets==3.2.0
tokenizers==0.21.0
flash-attn==2.7.2.post1
```

## Citation

If you find our project helpful, please star our repo and cite our work. Thanks!

```bibtex
@misc{modernBERT-large-multilingual-sentiment,
      title={modernBERT-large-multilingual-sentiment: A Multilingual Sentiment Classification Model},
      author={clapAI},
      howpublished={\url{https://huggingface.co/clapAI/modernBERT-large-multilingual-sentiment}},
      year={2025},
}