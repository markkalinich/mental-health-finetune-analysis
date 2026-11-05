---
library_name: transformers
base_model: avichr/heBERT_sentiment_analysis
tags:
- generated_from_trainer
- sentiment-analysis
- hebrew
- text-classification
- bert
language:
- he
metrics:
- accuracy
- f1
model-index:
- name: HeBERT_sentiment_analysis
  results:
  - task:
      type: text-classification
      name: Text Classification
    metrics:
    - type: accuracy
      value: 0.8683
      name: Accuracy
    - type: f1
      value: 0.8646
      name: Macro F1
    - type: f1
      value: 0.8682
      name: Weighted F1
pipeline_tag: text-classification
widget:
- text: "השירות היה מצוין והאוכל היה טעים מאוד!"
  example_title: "Positive example"
- text: "החוויה הייתה מאכזבת והמחיר היה גבוה מדי."
  example_title: "Negative example"
- text: "ההזמנה הגיעה בזמן."
  example_title: "Neutral example"
inference:
  parameters:
    return_all_scores: true
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. -->

# HeBERT_sentiment_analysis

This model is a fine-tuned version of [avichr/heBERT_sentiment_analysis](https://huggingface.co/avichr/heBERT_sentiment_analysis) for Hebrew sentiment classification.

It achieves the following results on the evaluation set:
- **Loss:** 0.3750
- **Accuracy:** 0.8683
- **Macro F1:** 0.8646
- **Weighted F1:** 0.8682

---

## 🚀 Use this model

### Quickstart with `pipeline`

The easiest way to run the model is with the `transformers` pipeline API:

```python
from transformers import pipeline

classifier = pipeline(
    task="text-classification",
    model="<YOUR_HF_USERNAME>/HeBERT_sentiment_analysis",
    tokenizer="<YOUR_HF_USERNAME>/HeBERT_sentiment_analysis",
    return_all_scores=True,
)

text = "השירות היה מצוין והאוכל היה טעים מאוד!"
print(classifier(text))
# [[{'label': 'positive', 'score': 0.97}, {'label': 'neutral', 'score': 0.02}, {'label': 'negative', 'score': 0.01}]]
```

### Direct loading with `AutoModel`

For more control (batching, custom thresholds, ONNX export, etc.):

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_id = "<YOUR_HF_USERNAME>/HeBERT_sentiment_analysis"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id)
model.eval()

texts = [
    "השירות היה מצוין והאוכל היה טעים מאוד!",
    "החוויה הייתה מאכזבת והמחיר היה גבוה מדי.",
    "ההזמנה הגיעה בזמן.",
]

inputs = tokenizer(texts, padding=True, truncation=True, max_length=128, return_tensors="pt")
with torch.no_grad():
    logits = model(**inputs).logits

probs = torch.softmax(logits, dim=-1)
preds = probs.argmax(dim=-1)
labels = [model.config.id2label[p.item()] for p in preds]

for text, label, prob in zip(texts, labels, probs):
    print(f"{label}\t({prob.max():.3f})\t{text}")
```

### GPU / half-precision

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

device = "cuda" if torch.cuda.is_available() else "cpu"
model = AutoModelForSequenceClassification.from_pretrained(
    "<YOUR_HF_USERNAME>/HeBERT_sentiment_analysis",
    torch_dtype=torch.float16 if device == "cuda" else torch.float32,
).to(device)
```

---

## 🌐 Deploy

### Option 1 — Hugging Face Inference API (zero infra)

The model is exposed via the free Inference API as soon as it's pushed to the Hub:

```bash
curl https://api-inference.huggingface.co/models/<YOUR_HF_USERNAME>/HeBERT_sentiment_analysis \
  -H "Authorization: Bearer $HF_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"inputs": "השירות היה מצוין והאוכל היה טעים מאוד!"}'
```

### Option 2 — Inference Endpoints (production)

Click **Deploy → Inference Endpoints** on the model page, or via the CLI:

```bash
huggingface-cli login
# In the UI: choose CPU (small/medium) or a T4/A10G GPU for higher throughput.
```

Recommended starting config:
- **Hardware:** CPU-Small for < 50 req/min, GPU T4 for higher load
- **Replicas:** 1 (autoscale 1→3)
- **Task:** `text-classification`
- **Max input length:** 128 tokens

### Option 3 — Docker (self-hosted with TGI / TEI)

For the lowest-latency self-hosted deployment, use [text-embeddings-inference](https://github.com/huggingface/text-embeddings-inference) (supports BERT classifiers):

```bash
docker run -p 8080:80 \
  -v $PWD/data:/data \
  --gpus all \
  ghcr.io/huggingface/text-embeddings-inference:1.5 \
  --model-id <YOUR_HF_USERNAME>/HeBERT_sentiment_analysis
```

Then call it:

```bash
curl http://localhost:8080/predict \
  -H 'Content-Type: application/json' \
  -d '{"inputs": "השירות היה מצוין והאוכל היה טעים מאוד!"}'
```

### Option 4 — ONNX / quantized for edge

```python
from optimum.onnxruntime import ORTModelForSequenceClassification
from transformers import AutoTokenizer

model = ORTModelForSequenceClassification.from_pretrained(
    "<YOUR_HF_USERNAME>/HeBERT_sentiment_analysis",
    export=True,
)
tokenizer = AutoTokenizer.from_pretrained("<YOUR_HF_USERNAME>/HeBERT_sentiment_analysis")
model.save_pretrained("./onnx-hebert-sentiment")
tokenizer.save_pretrained("./onnx-hebert-sentiment")
```

---

## 🎮 Demo

A live Gradio demo is available as a Hugging Face Space:
👉 **[Try it on Spaces](https://huggingface.co/spaces/<YOUR_HF_USERNAME>/HeBERT_sentiment_analysis-demo)**

Run the same demo locally:

```python
# app.py
import gradio as gr
from transformers import pipeline

clf = pipeline("text-classification",
               model="<YOUR_HF_USERNAME>/HeBERT_sentiment_analysis",
               return_all_scores=True)

def predict(text):
    scores = clf(text)[0]
    return {item["label"]: float(item["score"]) for item in scores}

demo = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(label="טקסט בעברית", rtl=True, lines=3,
                      placeholder="הכנס טקסט לניתוח רגש..."),
    outputs=gr.Label(num_top_classes=3, label="סנטימנט"),
    title="HeBERT Sentiment Analysis",
    description="ניתוח רגש בעברית — חיובי / נייטרלי / שלילי",
    examples=[
        ["השירות היה מצוין והאוכל היה טעים מאוד!"],
        ["החוויה הייתה מאכזבת והמחיר היה גבוה מדי."],
        ["ההזמנה הגיעה בזמן."],
    ],
)

if __name__ == "__main__":
    demo.launch()
```

```bash
pip install gradio transformers torch
python app.py
```

---

## Model description

HeBERT_sentiment_analysis is a Hebrew sentiment classifier built on top of **avichr/heBERT_sentiment_analysis**, itself a HeBERT (Hebrew BERT) checkpoint pre-trained on the Hebrew portion of OSCAR, Wikipedia, and a large Hebrew news corpus.

This fine-tune adapts the base classifier to a new domain-specific labeled dataset, improving accuracy and F1 on in-domain examples.

## Intended uses & limitations

**Intended uses**
- Sentiment classification of Hebrew short-to-medium text (reviews, comments, social posts, support tickets).
- Backbone for downstream Hebrew NLP pipelines (alerting, content moderation triage, customer-feedback analytics).

**Limitations**
- Trained on Hebrew only — performance on code-switched (Hebrew + English/Arabic) text is not guaranteed.
- Optimized for inputs up to **128 tokens**. Longer documents should be chunked.
- The model may reflect biases present in the underlying HeBERT pre-training data and the fine-tuning dataset; review predictions before using in high-stakes settings.
- Not designed for sarcasm-heavy text, multi-aspect sentiment, or emotion classification beyond polarity.

## Training and evaluation data

The model was fine-tuned on a labeled Hebrew sentiment dataset (positive / neutral / negative). Detailed dataset card to be added.

## Training procedure

### Training hyperparameters

| Hyperparameter | Value |
|---|---|
| learning_rate | 2e-05 |
| train_batch_size | 16 |
| eval_batch_size | 32 |
| seed | 42 |
| gradient_accumulation_steps | 2 |
| total_train_batch_size | 32 |
| optimizer | ADAMW_TORCH_FUSED (β=(0.9, 0.999), ε=1e-08) |
| lr_scheduler_type | linear |
| lr_scheduler_warmup_steps | 0.06 |
| num_epochs | 2 |
| mixed_precision_training | Native AMP |

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Macro F1 | Weighted F1 |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:--------:|:-----------:|
| 0.7800        | 1.0   | 1784 | 0.4106          | 0.8362   | 0.8334   | 0.8373      |
| 0.4435        | 2.0   | 3568 | 0.3750          | 0.8683   | 0.8646   | 0.8682      |

### Framework versions

- Transformers 5.8.0
- PyTorch 2.11.0+cu130
- Datasets 4.8.5
- Tokenizers 0.22.2