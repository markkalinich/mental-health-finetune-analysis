---
license: apache-2.0
pipeline_tag: text-classification
language:
- id
tags:
- sentiment-analysis
- indonesian
- indobertweet
- text-classification
---

# Model Card: IndoBERTweet Sentiment Analysis - Program MBG

## Model Description

Model ini merupakan hasil fine-tuning dari [IndoBERTweet-base-uncased](https://huggingface.co/indolem/indobertweet-base-uncased) untuk klasifikasi sentimen berbahasa Indonesia. Model dirancang khusus untuk menganalisis sentimen publik terhadap **Program Makan Bergizi Gratis (MBG)** berdasarkan data media sosial, dengan tiga kelas output: **negatif**, **netral**, dan **positif**.

Model dilatih menggunakan hyperparameter tuning (learning rate dan batch size) dengan early stopping berbasis validation loss, dan dievaluasi menggunakan F1-Score Macro.

## Intended Uses

Model ini ditujukan untuk:
- Analisis sentimen publik terhadap Program MBG dari data media sosial (Twitter/X, dan berpotensi platform lain dengan gaya bahasa serupa)
- Riset akademik terkait opini publik terhadap kebijakan pemerintah

## Training Data

Model dilatih menggunakan data cuitan berbahasa Indonesia yang berkaitan dengan Program MBG. Data melalui tahap preprocessing: case folding, cleaning (penghapusan emoji, URL, mention, hashtag, angka), dan normalisasi kata tidak baku menggunakan kamus custom.

**Catatan**: Data mentah tidak dipublikasikan mengikuti praktik umum terkait kebijakan platform sumber data.

## Training Procedure

- **Base model**: indolem/indobertweet-base-uncased
- **Hyperparameter search**: learning rate {1e-5, 2e-5, 3e-5, 5e-5}, batch size {16, 32}
- **Early stopping**: patience 3 epoch, berbasis validation loss
- **Kombinasi terbaik**: learning rate 3e-5, batch size 32

## Evaluation Results

- **F1-Score (Macro)**: 0.8641

## Bias and Limitations

- Model dilatih khusus pada data Twitter/X terkait topik MBG, sehingga performa dapat menurun pada domain teks lain (misalnya komentar YouTube/Instagram) atau topik di luar cakupan training.
- Model tidak divalidasi untuk konteks sarkasme kompleks atau sentimen implisit yang sangat bergantung konteks eksternal.
- Sebagaimana model bahasa pada umumnya, hasil klasifikasi tetap perlu diverifikasi manusia untuk keputusan yang berdampak signifikan.

## How to Use

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("suaib18/indobertweet-mbg-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("suaib18/indobertweet-mbg-sentiment")
```

## Citation

Model dasar:
```bibtex
@inproceedings{koto2021indobertweet,
  title={IndoBERTweet: A Pretrained Language Model for Indonesian Twitter with Effective Domain-Specific Vocabulary Initialization},
  author={Fajri Koto and Jey Han Lau and Timothy Baldwin},
  booktitle={Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP 2021)},
  year={2021}
}
```

## Demo

Coba model ini langsung lewat web app: [mbg-sentiment-app](https://huggingface.co/spaces/suaib18/mbg-sentiment-app)