---
license: apache-2.0
datasets:
- SemEval-2018-Task1-E-c
language:
- en
metrics:
- f1
- recall
- precision
pipeline_tag: text-classification
library_name: transformers
tags:
- multi-label-classification
- fine-grained
- emotion-classification
model-index:
- name: roberta-base-semeval
  results:
  - task:
      type: text-classification
      name: Multi-label Fine-Grained Emotion Classification
    dataset:
      type: multi-class-classification
      name: SemEval
      split: test
    metrics:
    - type: accuracy
      value: 0.85
      name: Accuracy(Hamming)
    - type: recall
      value: 0.70
      name: Recall-macro
    - type: f1
      value: 0.61
      name: F1-macro
---


## 🏷️ Model Details
This model is finetuned and optimized for fine-grained multi-label emotion classification task from text.
The model employs a hybrid training objective that integrates similarity-based contrastive learning with a classification objective, instead of using the conventional binary cross-entropy (BCE) loss alone. 
This approach enables the model to capture both semantic alignment between text and emotion concepts and label-specific decision boundaries, resulting in improved performance on the imbalanced SemEval-2018 dataset.

*This model is the Model II (Classifier-based) variant accounding in our paper, which has achieved the best performance. Please read your work for more details of the model architecture and training objectives used.*

- **Developed by:** Subinoy Bera and Arnab Karmakar
- **Model type:** Transformers | RoBERTa-base
- **Language (NLP):** English
- **License:** Apache-2.0
- **Repository:** [GitHub](https://github.com/Hidden-States-AI-Labs/EmoAxis)
- **Research Paper:** [Do We Need a Classifier? Dual Objectives Go Beyond Baselines in Fine-Grained Emotion Classification.](https://zenodo.org/records/18123882?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6IjhjNmQwMTYzLWFiYzEtNDBiZi05NTFkLTI2Mzg1YzhiYThhZSIsImRhdGEiOnt9LCJyYW5kb20iOiI5MDE1MDM1MTYxMTg1MzEyMTY3ZmY2YzNmY2NlYTM4OSJ9.JgOX4GlmZ8ad-PtjytzioPUPSJSGYp8wochqpTgMO78SE1oBq9R6yUor2_36oOaSUO04OPP0MJqBiYK0JK0NHA)


## ✅ Intended Usage
The model is specifically intended for **fine-grained multi-label emotion classification from text** in both practical and research settings.
It can be used to detect emotions from short to medium-length textual content such as social media posts, user comments, online discussions, reviews, and conversational text, where identifying fine-grained emotion categories give better insights.

The model is suitable for **local and offline deployment** for tasks such as emotion-aware text analysis, affective computing research, and downstream NLP applications that benefit from fine-grained emotion signals.


## 📊 Dataset Used
[**SemEval-2018-Task1-E-c**]("https://saifmohammad.com/WebDocs/AIT-2018/AIT2018-DATA/SemEval2018-Task1-all-data.zip")(2018): A large-scale multi-label emotion classification dataset, consisting of 10K tweets, annotated with 11 emotion categories. The dataset is diverse and representative of real-world emotional language, consisting of informal grammar, sarcasm, and ambiguous or context-dependent cues. We have utilized the full 11-label SemEval-2018 taxonomy to train and evaluate the model.


## 📌 Model Performance (on Test)
The model is evaluated using standard multi-label metrics, with a focus on Macro-F1, which is widely regarded as the most informative metric for such imbalanced, multi-label emotion classification tasks.

- Macro-F1 : 0.61<br>
- Micro-F1: 0.71<br>
- Precision: 0.54<br>
- Recall: 0.70<br>
- Accuracy (Hamming): 0.85

The table given below highlights the performance comparison of some existing benchmark models on the GoEmotions dataset :-
| Model | Macro-Precision | Macro-Recall | Macro-F1 |
|-------|-----------------|--------------|----------|
| Dep-GAT (I. Ameer, N. Bölücü et al.) | 0.62 | 0.68 | 0.52 |
| TCS Research (H. Meisheri and L. Dey) | - | - | 0.53 |
| BERT+DK ( W. Ying, R. Xiang et al.) | - | - | 0.55 |
| BERT+GCN ( P. Xu, Z. Liu et al.) | - | - | 0.56 |
| SpanEmo (H. Alhuzali and S. Ananiadou) | - | - | 0.58 |
| BERT-base (Ramakrishnan et al.)| 0.67 | 0.54 | 0.59 |
| UCCA-GAT | 0.62 | 0.66 | 0.60 |
| **RoBERTa-base (ours)** [(Model II)](https://zenodo.org/records/18123882?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6IjhjNmQwMTYzLWFiYzEtNDBiZi05NTFkLTI2Mzg1YzhiYThhZSIsImRhdGEiOnt9LCJyYW5kb20iOiI5MDE1MDM1MTYxMTg1MzEyMTY3ZmY2YzNmY2NlYTM4OSJ9.JgOX4GlmZ8ad-PtjytzioPUPSJSGYp8wochqpTgMO78SE1oBq9R6yUor2_36oOaSUO04OPP0MJqBiYK0JK0NHA) | 0.54 | 0.70 | **0.61** |

🏆 **Therefore, our model <u>outperformes existing baselines</u> and achieves <u>*state-of-the-art*</u> performance among existing open-source models!** 🥇


## 🚀 Get Started with the Model

```bash
import torch
from transformers import AutoTokenizer, AutoModel
from transformers import logging as transformers_logging
import warnings
warnings.filterwarnings("ignore")
transformers_logging.set_verbosity_error()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model_id = "Hidden-States/roberta-base-semeval"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModel.from_pretrained(model_id, trust_remote_code=True)
model.to(device).eval()

emotion_labels = [
    "anger", "anticipation", "disgust", "fear", "joy", "love",
    "optimism", "pessimism", "sadness", "surprise", "trust"
]

def predict_emotions(text):
  inputs = tokenizer(text, truncation=True, max_length=128,
                  padding=True, return_attention_mask=True, return_tensors="pt"
                ).to(device)
  _, logits = model(**inputs)

  probs = torch.sigmoid(logits)
  preds = (probs >= 0.5).int()[0]

  predicted_emotions = [
    emotion_labels[i]
    for i, v in enumerate(preds)
    if v.item() == 1
  ]
  print(predicted_emotions)

text = "Honestly, same. I was miserable at my admin asst job."
predict_emotions(text)

#output: ['anger', 'disgust', 'pessimism', 'sadness']
```

## 🛠️ Training Hyperparameters and Details

| Parameter | Value |
|-----------|-------|
| encoder lr-rate | 2e-5 |
| classiﬁer lr-rate | 1.5e-4 |
| optimizer | AdamW |
| lr-scheduler | cosine with warmup |
| weight decay | 0.01 |
| warmup ratio | 0.08 |
| temperature | 0.05 |
| clipping constant | 0.05 |
| batch size | 64 |
| epochs | 10 |
| threshold | 0.5 (fixed) |

Check out our paper for complete training details and objectives used: [Visit ↗️](https://zenodo.org/records/18123882?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6IjhjNmQwMTYzLWFiYzEtNDBiZi05NTFkLTI2Mzg1YzhiYThhZSIsImRhdGEiOnt9LCJyYW5kb20iOiI5MDE1MDM1MTYxMTg1MzEyMTY3ZmY2YzNmY2NlYTM4OSJ9.JgOX4GlmZ8ad-PtjytzioPUPSJSGYp8wochqpTgMO78SE1oBq9R6yUor2_36oOaSUO04OPP0MJqBiYK0JK0NHA)


## 💻 Compute Infrastructure
- **Inference**: Any modern x86 CPU with minimum 8 GB RAM. GPU is optional, not required for inference.

- **Training/ Fine-Tuning**: Must use GPU with at least 12 GB of VRAM. This model has been trained in Google Colab environment with single T4 GPU.

- **Libraries/ Modules**
  1. Transformers : 4.57.3
  2. Pytorch : 2.8.0+cu129
  3. Datasets : 4.4.1
  4. Scikit-learn : 1.8.0
  5. Numpy : 2.3.5


## ⚠️ Out-of-Scope Use

The model cannot be directly used for detecting emotions from multi-lingual or multi-modal data/text, and cannot predict emotions beyond the 11-label SemEval-2018-taxonomy.
While the proposed approach demonstrates strong empirical performance on benchmark datasets, it is not designed, evaluated, or validated for deployment in high-stakes or safety-critical applications.
The model may reflect dataset-specific biases, annotation subjectivity, and cultural limitations inherent in emotion datasets. Predictions should therefore be interpreted as approximate signals rather than definitive emotional states.

Users are responsible for ensuring that any downstream application complies with relevant ethical guidelines, legal regulations, and domain-specific standards.
<br>

## 🎗️ Community Support & Citation

**If you find this model useful, please consider liking this repository and also give a star to our GitHub repository.
Your support helps us improve and maintain this work!** ⭐

📝 **If you use our work in academic or research settings, please cite our work accordingly.** 🙏😃 <br>
<br>

THANK YOU!! 🧡🤍💚<br>
*- with regards*: Hidden States AI Labs