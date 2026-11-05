
---
license: apache-2.0
tags:
  - emotion-detection
  - affectnet
  - beit
  - image-classification
  - facial-expression-recognition
datasets:
  - AffectNet
metrics:
  - accuracy
  - confusion matrix
model-index:
  - name: beit-affectnet-final
    results:
      - task:
          type: image-classification
          name: Facial Emotion Classification
        dataset:
          name: AffectNet Cleaned
          type: image
        metrics:
          - name: Accuracy
            type: accuracy
            value: 0.75
---

# BEiT-Large for Emotion Detection on AffectNet

This model is fine-tuned from [`microsoft/beit-large-patch16-224-pt22k-ft22k`](https://huggingface.co/microsoft/beit-large-patch16-224-pt22k-ft22k) for facial emotion recognition using a cleaned and balanced version of the AffectNet dataset.


## 🧠 Classes

The model predicts the following 7 basic emotion classes:

- 😠 **anger**
- 🤢 **disgust**
- 😨 **fear**
- 😀 **happy**
- 😐 **neutral**
- 😢 **sad**
- 😲 **surprise**

---

## 📊 Dataset Overview

| Emotion    | Train Samples | Test Samples |
|------------|---------------|--------------|
| anger      | 1500          | 1718         |
| disgust    | 1229          | 1248         |
| fear       | 1512          | 1664         |
| happy      | 2340          | 2704         |
| neutral    | 2758          | 2368         |
| sad        | 3091          | 1584         |
| surprise   | 2119          | 1920         |

---

## 📈 Training Metrics

| Epoch | Training Loss | Validation Loss | Accuracy |
|-------|---------------|-----------------|----------|
| 1     | 0.4552        | 0.5809          | 0.6917   |
| 2     | 0.3000        | 0.6669          | 0.7079   |
| 3     | 0.1473        | 0.7098          | 0.7378   |
| 4     | 0.0674        | 0.8904          | 0.7353   |
| 5     | 0.0291        | 0.9008          | 0.7452   |
| 6     | 0.0216        | 0.9844          | 0.7503   |
| 7     | 0.0118        | 1.0369          | 0.7522   |
| 8     | 0.0069        | 1.0992          | 0.7486   |
| 9     | 0.0035        | 1.0947          | 0.7482   |
| 10    | 0.0023        | 1.1336          | 0.7461   |

✅ **Final Accuracy:** ~**74.6%** on the test set

---

## Training Configuration

The model was trained using the Hugging Face `Trainer` with the following main arguments:

- `num_train_epochs=10`
- `per_device_train_batch_size=64`
- `per_device_eval_batch_size=64`
- `gradient_accumulation_steps=2`
- `learning_rate=5e-5`
- `fp16=True` (mixed precision training)
- `eval_strategy="epoch"`
- `save_strategy="epoch"`
- `save_total_limit=2`
- `load_best_model_at_end=True`
- `metric_for_best_model="accuracy"`


---

## Confusion Matrix

![Confusion Matrix](https://huggingface.co/Tanneru/Facial-Emotion-Detection-BEIT-Large/resolve/main/confusion_matrix.png)

---

## 🔧 How to Use

```python
from transformers import BeitImageProcessor, BeitForImageClassification
from PIL import Image
import requests

image_path = '/RAF-DB/aligned/test_0031_aligned.jpg' # ⬅️ Replace with your image path
image = Image.open(image_path).convert("RGB")

processor = BeitImageProcessor.from_pretrained("Tanneru/Facial-Emotion-Detection-BEIT-Large")
model = BeitForImageClassification.from_pretrained("Tanneru/Facial-Emotion-Detection-BEIT-Large")

inputs = processor(images=image, return_tensors="pt")

outputs = model(**inputs)
logits = outputs.logits


predicted_class_idx = logits.argmax(-1).item()
print("Predicted class:", model.config.id2label[predicted_class_idx])
```

---

## 📄 License

This model is released under the **Apache 2.0 License**. You are free to use, modify, and distribute the model with attribution.

---

## ✍️ Author

- **Username**: Tanneru
- **Base model**: [`microsoft/beit-large-patch16-224-pt22k-ft22k`](https://huggingface.co/microsoft/beit-large-patch16-224-pt22k-ft22k)


---

## 📚 Citation

If you use this model in your work, please cite:

```bibtex
@misc{tanneru2025beit_affectnet,
  title={BEiT-Large fine-tuned on AffectNet for Emotion Detection},
  author={Tanneru},
  year={2025},
  publisher={Hugging Face},
  howpublished={\url{https://huggingface.co/Tanneru/Facial-Emotion-Detection-BEIT-Large}},
}

@article{bao2021beit,
  author       = {Hangbo Bao and Li Dong and Furu Wei},
  title        = {BEiT: BERT Pre-Training of Image Transformers},
  journal      = {CoRR},
  volume       = {abs/2106.08254},
  year         = {2021},
  url          = {https://arxiv.org/abs/2106.08254},
  archivePrefix = {arXiv},
  eprint       = {2106.08254},
  bibsource    = {dblp computer science bibliography, https://dblp.org}
}


