---
license: apache-2.0
tags:
- emotion-detection
- text-classification
- transformers
- deberta
- huggingface
- emotion
- emotion-classification
datasets:
- dair-ai/emotion
- faisalsanto007/isear-dataset
- debarshichanda/goemotions
metrics:
- accuracy
- precision
- recall
- f1
- confusion_matrix
model-index:
- name: Emotion-Classification-DeBERTa-v3-Large
  results:
  - task:
      type: text-classification
      name: Emotion Classification
    dataset:
      name: Merged Emotion Datasets (GoEmotions + ISEAR + Emotion)
      type: text
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.96
    - name: F1
      type: f1
      value: 0.94
base_model:
- microsoft/deberta-v3-large
---

# DeBERTa-v3-Large for Emotion Detection (Merged & Augmented Dataset)

This model is fine-tuned on [`microsoft/deberta-v3-large`](https://huggingface.co/microsoft/deberta-v3-large) on a **merged and augmented** version of the following datasets:

- 🤗 [GoEmotions](https://huggingface.co/datasets/debarshichanda/goemotions)
- 📘 [ISEAR Dataset](https://www.kaggle.com/datasets/faisalsanto007/isear-dataset/data)
- 📙 [Emotion Dataset (DAIR-AI)](https://huggingface.co/datasets/dair-ai/emotion)

The model is trained for **7-class emotion classification** in English and achieves **state-of-the-art performance** using advanced augmentation and weighted loss.

---

## 🧠 Emotion Classes

- 😠 **anger**
- 🤢 **disgust**
- 😨 **fear**
- 😀 **happy**
- 😐 **neutral**
- 😢 **sad**
- 😲 **surprise**

---

## 📈 Training Metrics

| Epoch | Training Loss | Validation Loss | Accuracy | F1 Macro | F1 Weighted | Precision Macro | Precision Weighted | Recall Macro | Recall Weighted |
| ----- | ------------- | --------------- | -------- | -------- | ----------- | --------------- | ------------------ | ------------ | --------------- |
| 1     | 0.3867        | 0.3506          | 0.7559   | 0.6857   | 0.7629      | 0.6520          | 0.7859             | 0.7722       | 0.7559          |
| 2     | 0.2340        | 0.2120          | 0.8147   | 0.7879   | 0.8174      | 0.7557          | 0.8292             | 0.8365       | 0.8147          |
| 3     | 0.1786        | 0.1616          | 0.8428   | 0.8114   | 0.8445      | 0.7715          | 0.8533             | 0.8758       | 0.8428          |
| 4     | 0.1261        | 0.1371          | 0.8671   | 0.8584   | 0.8669      | 0.8479          | 0.8729             | 0.8754       | 0.8671          |
| 5     | 0.0770        | 0.1242          | 0.8940   | 0.8751   | 0.8936      | 0.8537          | 0.8965             | 0.9020       | 0.8940          |
| 6     | 0.0608        | 0.1190          | 0.9208   | 0.9179   | 0.9221      | 0.9171          | 0.9225             | 0.9195       | 0.9208          |
| 7     | 0.0462        | 0.1209          | 0.9255   | 0.9192   | 0.9253      | 0.9218          | 0.9269             | 0.9184       | 0.9255          |
| 8     | 0.0373        | 0.1251          | 0.9305   | 0.9198   | 0.9305      | 0.9145          | 0.9317             | 0.9262       | 0.9305          |
| 9     | 0.0270        | 0.1262          | 0.9453   | 0.9375   | 0.9453      | 0.9354          | 0.9462             | 0.9400       | 0.9453          |
| 10    | 0.0189        | 0.1304          | 0.9526   | 0.9412   | 0.9527      | 0.9408          | 0.9529             | 0.9421       | 0.9526          |
| ...   | ...           | ...             | ...      | ...      | ...         | ...             | ...                | ...          | ...             |
| 20    | 0.0025        | 0.1618          | 0.9569   | 0.9434   | 0.9569      | 0.9444          | 0.9571             | 0.9428       | 0.9569          |


---

## 🛠️ Training Configuration

```python
training_args = TrainingArguments(
    output_dir="./deberta-large-3-merged_augmented",
    eval_strategy="epoch",
    save_strategy="epoch",
    learning_rate=1e-5,
    per_device_train_batch_size=32,
    per_device_eval_batch_size=32,
    gradient_accumulation_steps=2,
    num_train_epochs=20,
    weight_decay=0.01,
    lr_scheduler_type="cosine",
    logging_dir="./logs",
    logging_steps=50,
    save_total_limit=1,
    load_best_model_at_end=True,
    metric_for_best_model="accuracy",
    report_to="none",
    dataloader_num_workers=8
)
```

---

## 🔄 Confusion Matrix

![Confusion Matrix](https://huggingface.co/Tanneru/Emotion-Classification-DeBERTa-v3-Large/resolve/main/Confusion_Matrix.png)

---

## 📊 Classification Report

![Classification Report](https://huggingface.co/Tanneru/Emotion-Classification-DeBERTa-v3-Large/resolve/main/Classification_Report.png)
---

## 🔧 How to Use

```python
from transformers import DebertaV2Tokenizer, DebertaV2ForSequenceClassification
import torch

text = "I'm feeling very nervous about tomorrow."

tokenizer = DebertaV2Tokenizer.from_pretrained('Tanneru/Emotion-Classification-DeBERTa-v3-Large')
model = DebertaV2ForSequenceClassification.from_pretrained('Tanneru/Emotion-Classification-DeBERTa-v3-Large')


inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)
predicted_class_id = torch.argmax(outputs.logits).item()

print("Predicted emotion:", model.config.id2label[predicted_class_id])
```

---

## 📄 License

This model is released under the **Apache 2.0 License**. You are free to use, modify, and distribute the model with proper attribution.

---

## ✍️ Author

* **Username**: Tanneru
* **Base model**: [`microsoft/deberta-v3-large`](https://huggingface.co/microsoft/deberta-v3-large)

---

## 📚 Citation

If you use this model in your work, please cite:

```bibtex
@misc{tanneru2025deberta_emotion,
  title={DeBERTa-v3-Large fine-tuned on Merged & Augmented Emotion Datasets},
  author={Tanneru},
  year={2025},
  publisher={Hugging Face},
  howpublished={\url{https://huggingface.co/Tanneru/Emotion-Classification-DeBERTa-v3-Large}},
}

@article{he2021deberta,
  title={DeBERTa: Decoding-enhanced BERT with Disentangled Attention},
  author={He, Pengcheng and Liu, Xiaodong and Gao, Jianfeng and Chen, Weizhu},
  journal={arXiv preprint arXiv:2006.03654},
  year={2021}
}
```