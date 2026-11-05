---
language: en
tags:
- sentiment-analysis
- singapore
- singlish
- regression
license: mit
---

# Singapore Sentiment Analyzer - MULTILINGUAL_BERT (Calibrated)

Fine-tuned sentiment analysis model for Singapore social media, **with post-training calibration** for improved accuracy.

## 🎯 Performance

| Metric | Before Calibration | After Calibration | Improvement |
|--------|-------------------|-------------------|-------------|
| **Accuracy** | 52.6% | **64.0%** | **+11.4%** |
| **MAE** | 0.126 | **0.104** | **-0.022** |
| **RMSE** | 0.168 | **0.141** | **-0.027** |

## 📊 Sentiment Scale

| Score | Category |
|-------|----------|
| 0.00 - 0.20 | Very Negative |
| 0.21 - 0.40 | Negative |
| 0.41 - 0.60 | Neutral |
| 0.61 - 0.80 | Positive |
| 0.81 - 1.00 | Very Positive |

## 🚀 Quick Start

```python
from transformers import AutoTokenizer
from modeling_calibrated import CalibratedRegressionModel

# Load model (calibration is automatic!)
model_name = "your-username/multilingual_bert-singapore-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = CalibratedRegressionModel.from_pretrained(model_name)

# Predict sentiment
text = "This chicken rice is damn shiok sia!"
result = model.predict_sentiment(text, tokenizer)

print(f"Score: {result['score']:.3f}")      # 0.875
print(f"Category: {result['category']}")   # "Very Positive"
```

## 💡 What is Calibration?

After fine-tuning, we applied **isotonic regression calibration** on a validation set. This corrects systematic bias patterns where the model was:
- Over-predicting on negative examples
- Under-predicting on positive examples
- Struggling with boundary cases (e.g., neutral vs negative)

The calibration layer is built into the model - you get calibrated predictions automatically!

## 📚 Training Details

- **Base model**: `cardiffnlp/twitter-roberta-base-sentiment-latest`
- **Training data**: 49,521 Singapore Reddit posts/comments
- **Fine-tuning**: 5 epochs, MSE loss, learning rate 2e-5
- **Calibration**: Isotonic regression on 500-sample validation set

## 🌏 Singapore Context

This model understands Singlish patterns and Singapore-specific terminology:
- Particles: lah, lor, leh, sia
- Slang: shiok, sian, jialat, paiseh
- Local context: HDB, MRT, hawker, kopitiam

## 📝 Citation

```bibtex
@misc{multilingual_bert-singapore-calibrated,
  title = {Singapore Sentiment Analyzer - MULTILINGUAL_BERT (Calibrated)},
  year = {2026},
  publisher = {HuggingFace},
  url = {https://huggingface.co/your-username/multilingual_bert-singapore-sentiment}
}
```

## 📄 License

MIT License - Free for commercial and non-commercial use.
