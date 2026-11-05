---
license: mit
datasets:
- imdb
language:
- ko
- en
tags:
- sentiment-analysis
- transformers
- distilbert
- pytorch
library_name: transformers
pipeline_tag: text-classification
---

# PyTorch Book - Sentiment Analysis Model

## 📚 모델 설명 (Model Description)

이 모델은 영화 리뷰에 대한 감성 분석(Sentiment Analysis)을 수행합니다. HuggingFace Transformers 라이브러리의 DistilBERT 모델을 기반으로 IMDb 데이터셋에서 학습되었습니다.

This model performs sentiment analysis on movie reviews. Based on DistilBERT from HuggingFace Transformers, fine-tuned on the IMDb dataset.

## 🎯 학습 데이터 (Training Data)

- **Dataset**: IMDb Movie Reviews
- **Size**: 25,000 training samples
- **Classes**: 2 (Positive / Negative)
- **Language**: English

## 🚀 사용 방법 (Usage)

### Python

```python
from transformers import pipeline

# 파이프라인 생성
classifier = pipeline("sentiment-analysis", model="aiegoo/pytorch-book")

# 감성 분석 수행
result = classifier("This movie is amazing!")
print(result)
# [{'label': 'POSITIVE', 'score': 0.9998}]
```

### 직접 모델 로드

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("aiegoo/pytorch-book")
model = AutoModelForSequenceClassification.from_pretrained("aiegoo/pytorch-book")

# 토큰화 및 예측
inputs = tokenizer("I love this movie!", return_tensors="pt")
outputs = model(**inputs)
```

## 📊 성능 (Performance)

- **Accuracy**: ~92% (on test set)
- **F1 Score**: ~0.91
- **Model Size**: 67M parameters (DistilBERT)

## 🏗️ 모델 아키텍처 (Model Architecture)

- **Base Model**: `distilbert-base-uncased-finetuned-sst-2-english`
- **Type**: Sequence Classification
- **Framework**: PyTorch + Transformers

## 📝 학습 과정 (Training Process)

1. **토크나이저**: BERT WordPiece tokenizer
2. **전처리**: 소문자 변환, 최대 512 토큰
3. **데이터셋**: IMDb 25,000 samples
4. **배치 크기**: 16
5. **최적화**: AdamW

## 🎓 교육 목적 (Educational Purpose)

이 모델은 **PyTorch Book** 학습 과정의 일부로 생성되었습니다:
- Week 2, Day 6: HuggingFace Transformers
- Topic: Tokenizer, Dataset, Pre-trained Models
- Environment: Local Jupyter + Google Colab

This model was created as part of the **PyTorch Book** learning curriculum.

## ⚠️ 제한사항 (Limitations)

- 영어 텍스트에 최적화됨 (Optimized for English text)
- 영화 리뷰 도메인에 특화됨 (Specialized for movie review domain)
- 긴 텍스트는 512 토큰으로 잘림 (Long text truncated to 512 tokens)

## 📄 라이선스 (License)

MIT License - 자유롭게 사용 가능합니다.

## 🔗 관련 링크 (Related Links)

- [HuggingFace Transformers](https://huggingface.co/docs/transformers)
- [IMDb Dataset](https://huggingface.co/datasets/imdb)
- [DistilBERT Paper](https://arxiv.org/abs/1910.01108)

## 👤 제작자 (Created by)

- **Author**: aiegoo
- **Course**: AI Track - Week 02, Day 6
- **Date**: November 2025

---

*Created with ❤️ for learning PyTorch and Transformers*
