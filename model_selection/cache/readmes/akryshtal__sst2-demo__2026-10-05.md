---
language: en
license: apache-2.0
tags:
- text-classification
- sentiment
- distilbert
- sst2
- fine-tuning
- transformers
- huggingface
pipeline_tag: text-classification
widget:
- text: I really enjoyed this movie!
- text: This was an absolute waste of time.
datasets:
- gimmaru/glue-sst2
base_model:
- distilbert/distilbert-base-uncased-finetuned-sst-2-english
---

# SST-2 Demo: DistilBERT fine-tuned on 5% of SST-2

This model is a minimal demonstration of fine-tuning [`distilbert-base-uncased`](https://huggingface.co/distilbert-base-uncased) on the [SST-2 (Stanford Sentiment Treebank v2)](https://huggingface.co/datasets/glue/viewer/sst2/train) dataset.

It was trained for **1 epoch on 5% of the training set (\~3,300 examples)** using a consumer GPU (RTX 4060) and mixed-precision (`fp16=True`). The model achieves \~86% validation accuracy in under 10 minutes.

---

## 📊 Evaluation

This model was evaluated on the SST-2 validation set after training for one epoch on 5% of the training data (~3,300 examples).

| Metric     | Value |
|------------|-------|
| Accuracy   | ~86%  |
| Loss       | ~0.35 |

> Evaluated using the Hugging Face `Trainer`'s default compute_metrics function. These results are not representative of full training performance due to the limited data and short training schedule.

---

**Not intended for production use** — this version is trained on a tiny subset of the dataset.

---

## 🗃️ Training details

* **Base model**: distilbert-base-uncased
* **Dataset**: [GLUE/SST-2](https://huggingface.co/datasets/glue/viewer/sst2/train) (5%)
* **Hardware**: NVIDIA RTX 4060 Laptop GPU
* **Batch size**: 32
* **Epochs**: 1
* **Precision**: mixed-precision (`fp16`)
* **Trainer**: Hugging Face `Trainer`

---

## 📎 Files

* `pytorch_model.bin` — model weights
* `config.json` — architecture details
* `tokenizer.json`, `vocab.txt`, etc. — tokenizer files from distilbert-base-uncased

---

## ✍️ Author

This model was fine-tuned and published by [@akryshtal](https://huggingface.co/akryshtal) as part of a machine learning engineering demo project.