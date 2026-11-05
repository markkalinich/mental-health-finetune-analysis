---
language: ar
license: mit
tags:
- sentiment-analysis
- arabic
- arabert
- bert
- text-classification
metrics:
- accuracy
- f1
pipeline_tag: text-classification
---

# AraBERT for Arabic Sentiment Analysis

Fine-tuned [aubmindlab/bert-base-arabertv02](https://huggingface.co/aubmindlab/bert-base-arabertv02) for Arabic sentiment classification (positive/negative).

## 🎯 Model Description

This model classifies Arabic text into positive or negative sentiment with **92.87% accuracy**. Built using transfer learning on BERT-base-arabertv02 with task-specific fine-tuning for binary sentiment analysis.

## 🚀 Quick Start

```python
from transformers import pipeline

# Load model
classifier = pipeline("sentiment-analysis", model="Belall87/arabert-arabic-sentiment")

# Predict
result = classifier("هذا المنتج رائع جداً")
print(result)
# [{'label': 'POSITIVE', 'score': 0.95}]

# Batch prediction
texts = [
    "الخدمة ممتازة والموظفين متعاونين",
    "تجربة سيئة جداً ولا أنصح بها"
]
results = classifier(texts)
```

## 📊 Performance

| Metric | Value |
|--------|-------|
| Accuracy | 92.87% |
| F1-Score | 92.87% |
| Precision | 92.85% |
| Recall | 92.89% |

## 🔧 Training Details

### Base Model
- **Architecture:** BERT-base (12 layers, 768 hidden, 12 attention heads)
- **Pre-trained:** aubmindlab/bert-base-arabertv02
- **Parameters:** ~110M

### Training
- **Optimizer:** AdamW
- **Learning Rate:** 2e-5 with cosine scheduling
- **Batch Size:** 8
- **Epochs:** 3
- **Max Length:** 256 tokens
- **Hardware:** GPU (fp16 mixed precision)

### Data Preprocessing
- Arabic text normalization (alef, yeh, hamza variants)
- Diacritics removal
- URL, mention, hashtag filtering
- Stratified train/val/test split (72%/8%/20%)

## 💡 Intended Use

### Direct Use
- Arabic social media sentiment monitoring
- Product review analysis
- Customer feedback classification
- Opinion mining in Arabic text

### Limitations
- Binary classification only (positive/negative)
- Trained on Modern Standard Arabic (MSA) and dialectal mix
- May underperform on domain-specific jargon
- Best with text length < 256 tokens

## 📚 Training Data

Arabic sentiment dataset with stratified sampling for balanced training. Preprocessing includes normalization of Arabic orthographic variants and removal of noise.

## 🔗 Links

- **GitHub Repository:** [Arabic-Sentiment-Analysis-BiLSTM-vs-AraBERT](https://github.com/Bolaal/Arabic-Sentiment-Analysis-BiLSTM-vs-AraBERT)
- **Kaggle Notebook:** [Arabic Sentiment Analysis](https://www.kaggle.com/code/bilalmahmoud/arabic-sentiment-analysis-cv)
- **Base Model:** [bert-base-arabertv02](https://huggingface.co/aubmindlab/bert-base-arabertv02)

## 📝 Citation

```bibtex
@misc{belal-arabert-sentiment-2025,
  author = {Belal Mahmoud Hussien},
  title = {AraBERT for Arabic Sentiment Analysis},
  year = {2025},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/Belall87/arabert-arabic-sentiment}}
}
```

## 📧 Contact

**Belal Mahmoud Hussien**
- Email: belalmahmoud8787@gmail.com
- LinkedIn: [Belal Mahmoud](https://www.linkedin.com/in/belal-mahmoud-husien)
- GitHub: [@Bolaal](https://github.com/Bolaal)

## 📄 License

MIT License
