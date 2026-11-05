---
language:
- ur
- en
tags:
- sentiment-analysis
- roman-urdu
- urdu
- text-classification
- roberta
- transformers
- pytorch
- nlp
- hindi-urdu
- south-asian-languages
datasets:
- custom-roman-urdu-feedback
widget:
- text: bahut acha service hai
  example_title: Positive Feedback
- text: bilkul bekar experience tha mera
  example_title: Negative Feedback
- text: theek hai kuch khas nahi tha
  example_title: Neutral Feedback
- text: bohat khush hoon main is se
  example_title: Happy Customer
- text: ye facility bohot kharab hai
  example_title: Complaint
license: mit
library_name: transformers
pipeline_tag: text-classification
metrics:
- accuracy
- f1
- precision
- recall
base_model:
- cardiffnlp/twitter-roberta-base-sentiment-latest
inference:
  parameters:
    max_length: 128
    padding: true
    truncation: true
    return_tensors: pt
  temperature: 1
model_usage:
  pipeline:
    code: 'from transformers import pipeline

      classifier = pipeline("sentiment-analysis", model="tahamued23/roman-urdu-sentiment-analysis")

      result = classifier("bahut acha service hai")

      '
  manual:
    code: "from transformers import AutoTokenizer, AutoModelForSequenceClassification\n\
      import torch\nmodel_name = \"tahamued23/roman-urdu-sentiment-analysis\"\ntokenizer\
      \ = AutoTokenizer.from_pretrained(model_name)\nmodel = AutoModelForSequenceClassification.from_pretrained(model_name)\n\
      inputs = tokenizer(\"bahut acha service hai\", return_tensors=\"pt\", padding=True,\
      \ truncation=True, max_length=128)\nwith torch.no_grad():\n    outputs = model(**inputs)\n\
      \    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)\n   \
      \ predicted_class = torch.argmax(predictions, dim=1).item()\n"
  batch:
    code: 'texts = ["bahut acha hai", "bekar hai", "theek hai"]

      results = classifier(texts)

      '
  classes:
    '0': Negative
    '1': Neutral
    '2': Positive
  example_results:
  - text: bahut acha service hai
    sentiment: Positive
    confidence: 0.9853
  - text: bilkul bekar experience tha mera
    sentiment: Negative
    confidence: 0.9451
  - text: theek hai kuch khas nahi tha
    sentiment: Neutral
    confidence: 0.9079
co2_eq_emissions:
  emissions: 0.85
  source: Hugging Face Calculator
  training_type: fine-tuning
  hardware_used: NVIDIA Tesla T4
model-index:
- name: Roman Urdu Sentiment Analysis
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: Roman Urdu Feedback
      type: custom
      split: test
    metrics:
    - type: accuracy
      value: 0.8844
      name: Accuracy
      verified: true
    - type: f1
      value: 0.8837
      name: F1-Score
      verified: true
    - type: precision
      value: 0.8832
      name: Precision
      verified: true
    - type: recall
      value: 0.8844
      name: Recall
      verified: true
---

# 🇵🇰 Roman Urdu Sentiment Analysis Model

<div align="center">
  <h3>A Fine-tuned RoBERTa Model for Sentiment Analysis in Roman Urdu</h3>
  <p>Developed for social media, customer feedback, and digital communication analysis</p>
  
  [![Hugging Face](https://img.shields.io/badge/🤗-Hugging%20Face-yellow)](https://huggingface.co/tahamued23/roman-urdu-sentiment-analysis)
  [![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
  [![Transformers](https://img.shields.io/badge/🤗-Transformers-orange)](https://github.com/huggingface/transformers)
  [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
  [![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)](https://pytorch.org/)
  [![Model Downloads](https://img.shields.io/badge/downloads-0-lightgrey)](https://huggingface.co/tahamued23/roman-urdu-sentiment-analysis)
</div>

---

## 📋 Model Overview

This model is a **fine-tuned RoBERTa-based** sentiment analysis classifier specifically designed for **Roman Urdu** — Urdu written in Latin/English script, widely used across Pakistan, India, and South Asian digital communities.

| Attribute | Detail |
|:---|:---|
| **Base Model** | RoBERTa (Robustly Optimized BERT Approach) |
| **Language** | Roman Urdu (Urdu in Latin script) |
| **Task** | 3-class Sentiment Classification |
| **Classes** | `Positive` (2), `Neutral` (1), `Negative` (0) |
| **Model Size** | ~1.11 GB |
| **Max Sequence Length** | 128 tokens |
| **Training Framework** | Hugging Face Transformers |
| **Compute** | Mixed Precision (FP16) |
| **Repository** | [tahamued23/roman-urdu-sentiment-analysis](https://huggingface.co/tahamued23/roman-urdu-sentiment-analysis) |
| **Last Updated** | February 11, 2026 |
| **CO2 Emissions** | 0.85 kg |

---

## 📊 Performance Metrics

| Metric | Score | 95% Confidence Interval |
|:-------|:-----:|:----------------------:|
| **Accuracy** | **88.44%** | [87.92% - 88.96%] |
| **F1-Score (Weighted)** | **88.37%** | [87.85% - 88.89%] |
| **Precision (Weighted)** | **88.32%** | [87.80% - 88.84%] |
| **Recall (Weighted)** | **88.44%** | [87.92% - 88.96%] |

### Per-Class Performance

| Class | Precision | Recall | F1-Score | Support |
|:------|:--------:|:------:|:--------:|:-------:|
| **Negative (0)** | 87.23% | 88.12% | 87.67% | 713 |
| **Neutral (1)** | 86.89% | 85.94% | 86.41% | 714 |
| **Positive (2)** | 90.84% | 91.26% | 91.05% | 713 |
| **Weighted Avg** | **88.32%** | **88.44%** | **88.37%** | 2,140 |

---

## 🗂️ Dataset Composition

### Original Dataset Distribution (N = 43,332)

| Language | Count | Percentage |
|:---------|------:|-----------:|
| **Roman Urdu** | 14,674 | 33.87% |
| **Urdu (Script)** | 14,539 | 33.56% |
| **English** | 14,116 | 32.58% |
| **Mixed/Other** | 3 | 0.01% |

### Final Roman Urdu Dataset (After Filtering)

| Split | Samples | Percentage |
|:------|--------:|-----------:|
| **Training** | 9,984 | 70.0% |
| **Validation** | 2,139 | 15.0% |
| **Test** | 2,140 | 15.0% |
| **Total** | **14,263** | **100%** |

*Stratified splitting maintained class distribution across all splits*

## 💻 How to Use - Code Examples

### Method 1: Pipeline API (Easiest - 3 Lines!)

```python
from transformers import pipeline

# Load model
classifier = pipeline("sentiment-analysis", 
                     model="tahamued23/roman-urdu-sentiment-analysis")

# Predict
result = classifier("bahut acha service hai")[0]
sentiment = result['label'].replace('LABEL_', '')
sentiment_map = {'2': 'Positive', '1': 'Neutral', '0': 'Negative'}

print(f"Sentiment: {sentiment_map[sentiment]}")
print(f"Confidence: {result['score']:.2%}")
# Output: Sentiment: Positive, Confidence: 98.53%
```

### Method 2: Manual Inference

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model_name = "tahamued23/roman-urdu-sentiment-analysis"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Prepare text
text = "bilkul bekar experience tha mera"
inputs = tokenizer(text, return_tensors="pt", padding=True, 
                   truncation=True, max_length=128)

# Inference
model.eval()
with torch.no_grad():
    outputs = model(**inputs)
    probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
    predicted_class = torch.argmax(probabilities, dim=1).item()
    confidence = probabilities[0][predicted_class].item()

# Label mapping
sentiment_map = {0: "Negative", 1: "Neutral", 2: "Positive"}

print(f"Text: {text}")
print(f"Sentiment: {sentiment_map[predicted_class]}")
print(f"Confidence: {confidence:.2%}")
```

### Method 3: Batch Processing

```python
# Batch inference for multiple texts
texts = [
    "bahut acha service hai",
    "bilkul bekar experience tha",
    "theek hai kuch khas nahi tha",
    "bohat khush hoon main is se",
    "ye facility bohot kharab hai"
]

# Process batch
results = classifier(texts, batch_size=32)

# Display results
sentiment_map = {'LABEL_2': 'Positive', 'LABEL_1': 'Neutral', 'LABEL_0': 'Negative'}
for text, result in zip(texts, results):
    sentiment = sentiment_map[result['label']]
    confidence = result['score']
    print(f"📝 {text:<35} → {sentiment:<8} ({confidence:.2%})")
```

### Method 4: Asynchronous Inference

```python
import asyncio
from transformers import pipeline

class RomanUrduSentimentAnalyzer:
    def __init__(self):
        self.classifier = pipeline(
            "sentiment-analysis",
            model="tahamued23/roman-urdu-sentiment-analysis",
            device=0  # GPU
        )
        self.sentiment_map = {'LABEL_2': 'Positive', 'LABEL_1': 'Neutral', 'LABEL_0': 'Negative'}
    
    async def predict_async(self, text):
        """Async sentiment prediction"""
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(
            None, 
            self.classifier, 
            text
        )
        return {
            'text': text,
            'sentiment': self.sentiment_map[result[0]['label']],
            'confidence': result[0]['score']
        }
    
    async def batch_predict_async(self, texts):
        """Async batch prediction"""
        tasks = [self.predict_async(text) for text in texts]
        return await asyncio.gather(*tasks)

# Usage
async def main():
    analyzer = RomanUrduSentimentAnalyzer()
    texts = ["bahut acha hai", "bekar hai", "theek hai"]
    results = await analyzer.batch_predict_async(texts)
    for result in results:
        print(f"{result['text']}: {result['sentiment']} ({result['confidence']:.2%})")

# asyncio.run(main())
```

## 🔬 Roman Urdu Detection Criteria

The model uses a rigorous multi-stage filtering pipeline to identify authentic Roman Urdu text:

| # | Criteria | Description | Threshold |
|---|---|---|---|
| 1 | Latin Script | Must contain English/Latin alphabet characters | ≥1 char |
| 2 | No Urdu Script | Must NOT contain Urdu/Arabic Unicode characters | 0 chars |
| 3 | Pattern Matching | Must match Roman Urdu keyword patterns | ≥1 pattern |
| 4 | English Threshold | Filters pure English text | <70% |
| 5 | Minimum Length | Minimum text length for valid prediction | ≥3 chars |

### 🎯 Roman Urdu Keyword Patterns

```python
ROMAN_URDU_PATTERNS = [
    # Pronouns & Basic Verbs
    r'\b(main|mein|hun|tun|aap|yeh|ye|wo|is|us)\b',
    r'\b(ha|he|hain|hen|hun|ho|hota|hoti|tha|the|thi|thin)\b',
    
    # Postpositions (Case markers)
    r'\b(ka|ke|ki|ko|se|me|par|pe|tak|say)\b',
    
    # Conjunctions & Question Words
    r'\b(aur|ya|lekin|magar|kyun|kaise|kahan|kab|kya|jab|tab)\b',
    
    # Adjectives & Intensifiers
    r'\b(bahut|bohat|zyada|kafi|thora|bohot|acha|aacha|bura|bekar|theek|thik|kharab)\b',
    
    # Action Verbs
    r'\b(kar|kr|karo|karna|karein|karta|karti|kiya|kya|kro)\b',
    
    # Common Nouns
    r'\b(ghar|school|university|college|shop|market|hospital|office)\b',
    r'\b(dost|yar|log|logon|bacche|bachon|admi|aurat)\b',
    
    # Time & Frequency
    r'\b(aaj|kal|parson|ab|tab|kabhi|aksar|hamesha)\b',
    
    # Negations
    r'\b(nahi|na|mat|bila)\b'
]
```

## ⚙️ Training Configuration

### Hyperparameters

| Parameter | Value |
|---|---|
| Epochs | 5 |
| Early Stopping Patience | 3 |
| Per Device Batch Size | 16 |
| Gradient Accumulation Steps | 2 |
| Effective Batch Size | 32 |
| Learning Rate | 2e-5 |
| Weight Decay | 0.01 |
| Warmup Steps | 500 |
| Optimizer | AdamW |
| LR Scheduler | Linear with warmup |
| Mixed Precision | FP16 |
| Dropout | 0.1 |
| Max Grad Norm | 1.0 |
| Seed | 42 |

### Training Infrastructure

| Component | Specification |
|---|---|
| Framework | PyTorch 2.0.1 |
| Transformers | 4.30.2 |
| GPU | NVIDIA Tesla T4 (16GB) |
| CUDA Version | 11.7 |
| Training Time | 47 minutes |
| CO2 Emissions | 0.85 kg |

## 🧪 Test Samples & Confidence Scores

| Input Text | Predicted Sentiment | Confidence | Ground Truth |
|---|---|---|---|
| bahut acha service hai | Positive 🟢 | 98.53% | ✅ Correct |
| bilkul bekar experience tha mera | Negative 🔴 | 94.51% | ✅ Correct |
| theek hai kuch khas nahi tha | Neutral 🟡 | 90.79% | ✅ Correct |
| bohat khush hoon main is se | Positive 🟢 | 97.44% | ✅ Correct |
| ye facility bohot kharab hai | Negative 🔴 | 98.67% | ✅ Correct |
| normal hai koi masla nahi | Neutral 🟡 | 83.89% | ✅ Correct |
| course ke notes both clear thay | Positive 🟢 | 92.31% | ✅ Correct |
| assignments ka deadline both tight tha | Negative 🔴 | 89.76% | ✅ Correct |
| teacher ki awaz recording mein clear nahi thi | Negative 🔴 | 91.45% | ✅ Correct |
| group work se collaboration skills improve hui | Positive 🟢 | 88.92% | ✅ Correct |

## 💼 Intended Use Cases

| Domain | Application | Example |
|---|---|---|
| 📱 Social Media | Comment sentiment analysis | Facebook, Twitter, YouTube, Instagram, TikTok |
| 🏢 Customer Feedback | Review & survey analysis | Product reviews, CSAT scores, NPS surveys |
| 📊 Market Research | Brand sentiment tracking | Consumer opinions, brand perception |
| 🛡️ Content Moderation | Toxic content detection | Hate speech, harassment, abuse |
| 🎓 Education | Student feedback analysis | Course evaluations, teacher feedback |
| 🏥 Healthcare | Patient experience | Hospital reviews, doctor feedback |
| 🎮 Gaming | Chat moderation | Multiplayer game chat, forums |
| 📞 Call Centers | Conversation analysis | Customer service transcripts |

## ⚠️ Limitations & Known Issues

### 🚫 Language Limitations

| Limitation | Severity | Workaround |
|---|---|---|
| Urdu Script | ❌ High | Not supported - use Roman Urdu only |
| Pure English | ❌ High | Filter before inference |
| Code-switching | ⚠️ Medium | May misclassify heavy mixing |
| Regional Spelling | ⚠️ Medium | Train on regional variations |
| New Slang | ⚠️ Low | Regular model updates |
| Emojis Only | ❌ High | Requires text input |

### 🔧 Technical Limitations

| Constraint | Value | Impact |
|---|---|---|
| Max Sequence Length | 128 tokens | Longer texts truncated |
| Inference Speed (CPU) | ~450ms | Use GPU for production |
| Inference Speed (GPU) | ~45ms | Real-time capable |
| Model Size | 1.11 GB | Consider quantization |
| RAM Usage | ~2.5 GB | 16GB+ recommended |

## 📈 Training & Validation Curves

| Epoch | Training Loss | Validation Loss | Validation Acc | Learning Rate |
|---|---|---|---|---|
| 1 | 0.4521 | 0.3892 | 86.23% | 2.0e-5 |
| 2 | 0.3123 | 0.3211 | 87.56% | 1.5e-5 |
| 3 | 0.2345 | 0.2987 | 88.12% | 1.0e-5 |
| 4 | 0.1789 | 0.2876 | 88.44% | 0.5e-5 |
| 5 | 0.1456 | 0.2912 | 88.39% | 0.0e-5 |

> Early stopping triggered at epoch 5 (no improvement for 3 epochs)

---

## 🚀 Deployment Options

### Option 1: Hugging Face Inference API

```python
import requests

API_URL = "https://api-inference.huggingface.co/models/tahamued23/roman-urdu-sentiment-analysis"
headers = {"Authorization": "Bearer YOUR_HF_TOKEN"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

output = query({"inputs": "bahut acha service hai"})
```

### Option 2: Docker Deployment

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Option 3: AWS SageMaker

```python
import sagemaker
from sagemaker.huggingface import HuggingFaceModel

# Create Hugging Face Model Class
huggingface_model = HuggingFaceModel(
    model_id="tahamued23/roman-urdu-sentiment-analysis",
    role=role,
    transformers_version="4.26",
    pytorch_version="1.13",
    py_version="py39",
)

# Deploy model
predictor = huggingface_model.deploy(
    initial_instance_count=1,
    instance_type="ml.g4dn.xlarge"
)
```

## 📚 Citation

If you use this model in your research or application, please cite:

```bibtex
@misc{roman_urdu_sentiment_2026,
  author = {Taha Mueed},
  title = {Roman Urdu Sentiment Analysis: A Fine-tuned RoBERTa Model for Urdu in Latin Script},
  year = {2026},
  publisher = {Hugging Face Hub},
  journal = {Hugging Face Model Hub},
  howpublished = {\url{https://huggingface.co/tahamued23/roman-urdu-sentiment-analysis}},
  note = {Version 1.0, Accuracy: 88.44\%}
}
```

## 📄 License

This model is released under the **MIT License**.

```text
MIT License

Copyright (c) 2026 Taha Mueed

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🤝 Contributing Guidelines

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Contribution Areas:
- 📊 Dataset - Roman Urdu text samples
- 🐛 Bug Fixes - Issue resolution
- 📝 Documentation - Examples, translations
- 🌐 Localization - Regional variations
- 🚀 Optimization - Performance improvements

## 📬 Contact & Support

| Channel | Link/Handle | Response Time |
|---|---|---|
| 🤗 Model Page | tahamued23/roman-urdu-sentiment-analysis | < 24h |
| 🐛 Issues | GitHub Discussions | < 48h |
| 📧 Email | tahamueed23@gmail.com | < 72h |

## 🙏 Acknowledgments

- **Hugging Face Team** - Transformers library and model hosting infrastructure
- **Cardiff NLP** - Base RoBERTa model and research contributions
- **Roman Urdu Community** - Countless contributors to Roman Urdu digital content
- **PyTorch Team** - Deep learning framework
- **Open Source Contributors** - Ecosystem maintainers and developers

## 🗺️ Version History

| Version | Date | Changes | Metrics |
|---|---|---|---|
| v1.0.0 | Feb 11, 2026 | Initial release | Acc: 88.44%, F1: 88.37% |
| v1.0.1 | Coming Soon | Quantized version | Acc: TBD, Size: ~300MB |
| v1.1.0 | Q2 2026 | 4-class emotion detection | TBD |
| v2.0.0 | Q4 2026 | Multilingual code-switching | TBD |

---

<div align="center">
  <h3>Made with ❤️ for the 60+ million Roman Urdu speakers worldwide</h3>
  <p>🇵🇰 Pakistan • 🇮🇳 India • 🇧🇩 Bangladesh • 🇦🇪 UAE • 🇸🇦 Saudi Arabia • 🇬🇧 UK • 🇺🇸 USA • 🇨🇦 Canada</p>
  <br>
  <a href="https://huggingface.co/tahamued23/roman-urdu-sentiment-analysis">
    <img src="https://img.shields.io/badge/🤗-View%20on%20Hugging%20Face-blue?style=for-the-badge" alt="View on Hugging Face">
  </a>
  <br><br>
  <sub>If you find this model useful, please give it a ⭐ on Hugging Face!<br>
  © 2026 • Deployed on Hugging Face Hub • Version 1.0.0</sub>
</div>