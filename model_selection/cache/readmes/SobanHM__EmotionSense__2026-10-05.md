---
language:
- en
license: mit
library_name: transformers
pipeline_tag: text-classification
tags:
- emotion-classification
- natural-language-processing
- roberta
- transformers
- pytorch
- goemotions
- ekman-emotions
- sentiment-analysis
- text-classification
datasets:
- go_emotions
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: EmotionSense
  results:
  - task:
      type: text-classification
      name: Emotion Classification
    dataset:
      name: Customized GoEmotions (Ekman Mapping)
      type: go_emotions
    metrics:
    - type: Accuracy
      value: 0.903
    - type: Precision
      value: 0.901
    - type: Recall
      value: 0.894
    - type: Weighted F1
      value: 0.891
---

# 🧠 EmotionSense
### Fine-Grained Emotion Classification using RoBERTa

<p align="center">

🤗 <b>Hugging Face</b> • 🔥 <b>RoBERTa</b> • 💬 <b>Emotion AI</b> • 🚀 <b>Production Ready</b>

</p>

EmotionSense is a **RoBERTa-base** model fine-tuned for **emotion classification**. The model predicts **seven human emotions** from English text using a cleaned and simplified version of the GoEmotions dataset.

Unlike the original GoEmotions dataset containing 28 fine-grained emotion labels, this work reorganizes emotions according to the **Ekman Emotion Framework**, improving interpretability while maintaining strong predictive performance.

---

# ✨ Highlights

- 🔥 Fine-tuned **RoBERTa-base**
- 🧠 Context-aware emotion recognition
- 📊 Class-balanced training using Weighted Cross Entropy Loss
- ⚡ Early stopping for improved generalization
- 🎯 Optimized using Weighted F1 Score
- 🤗 Compatible with Hugging Face Transformers Pipeline

---

# 🎯 Supported Emotion Classes

| Label | Description |
|--------|------------|
| 😀 Joy | Positive emotions, happiness, gratitude, love |
| 😢 Sadness | Grief, disappointment, remorse |
| 😡 Anger | Anger, annoyance, disapproval |
| 😨 Fear | Fear and nervousness |
| 🤢 Disgust | Disgust |
| 😲 Surprise | Surprise, curiosity, realization |
| 😐 Neutral | Emotionally neutral statements |

---

# 📚 Dataset

The model was trained using a **customized version of the GoEmotions dataset**.

The original dataset contains approximately **58,000 Reddit comments** annotated with **28 fine-grained emotion labels**.

To improve annotation quality:

- ✔ Majority Voting was applied.
- ✔ Samples without annotator agreement were removed.
- ✔ Multi-label ambiguity was eliminated.
- ✔ Fine-grained emotions were mapped into **Ekman's seven universal emotion categories**.

### Emotion Mapping

| Ekman Category | Original GoEmotions Labels |
|---------------|----------------------------|
| Anger | anger, annoyance, disapproval |
| Disgust | disgust |
| Fear | fear, nervousness |
| Joy | joy, amusement, admiration, approval, caring, desire, excitement, gratitude, love, optimism, pride, relief |
| Sadness | sadness, disappointment, embarrassment, grief, remorse |
| Surprise | surprise, realization, curiosity, confusion |
| Neutral | neutral |

---

# 🏗 Model Architecture

| Property | Value |
|----------|------|
| Base Model | RoBERTa-base |
| Framework | Hugging Face Transformers |
| Language | English |
| Task | Emotion Classification |
| Max Sequence Length | 128 |
| Batch Size | 16 |
| Learning Rate | 2e-5 |
| Epochs | 5 |
| Optimizer | AdamW |
| Loss Function | Weighted Cross Entropy |
| Early Stopping | Enabled |

---

# 📈 Performance

EmotionSense achieved the best performance among all evaluated models.

| Model | Accuracy | Weighted F1 |
|-------|---------:|------------:|
| Logistic Regression | 0.59 | 0.57 |
| Random Forest | 0.61 | 0.59 |
| Linear SVM | 0.63 | 0.61 |
| DistilBERT | 0.68 | 0.67 |
| **EmotionSense (RoBERTa)** | **0.903** | **0.891** |

### Final Evaluation

| Metric | Score |
|---------|------:|
| Accuracy | **90.3%** |
| Precision | **90.1%** |
| Recall | **89.4%** |
| Weighted F1 | **89.1%** |

---

# 🚀 Quick Start

Install Transformers

```bash
pip install transformers torch
```

Load the model

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="SobanHM/EmotionSense"
)

classifier("I finally got my dream job today!")
```

Example Output

```python
[
    {
        "label": "joy",
        "score": 0.997
    }
]
```

---

# 💡 Applications

- Conversational AI
- Emotion-aware Chatbots
- Mental Health Support Systems
- Customer Feedback Analysis
- Social Media Analytics
- Human-Computer Interaction
- Intelligent Virtual Assistants

---

# ⚠ Limitations

- Supports English language only.
- Performance may decrease on domain-specific text.
- Sarcasm and irony remain challenging.
- Emotion recognition is probabilistic and should not be used for clinical diagnosis or psychological assessment.

---

# 👨‍💻 About the Author

**Soban Hussain**

AI Engineer • Machine Learning Researcher • Computer Vision & NLP

🤗 **Hugging Face:** https://huggingface.co/SobanHM

💼 **LinkedIn:** https://www.linkedin.com/in/sobanhussain

💻 **GitHub:** https://github.com/SobanHM

---

# 🙌 Acknowledgements

This project was built using:

- Hugging Face Transformers
- PyTorch
- GoEmotions Dataset
- RoBERTa

Special thanks to the open-source AI community for providing exceptional tools and resources.

---

# 📖 Citation

If you use this model in your research, please cite both this repository and the GoEmotions dataset.

```bibtex
@inproceedings{demszky2020goemotions,
  title={GoEmotions: A Dataset of Fine-Grained Emotions},
  author={Demszky, Dorottya and others},
  booktitle={Proceedings of ACL},
  year={2020}
}
```

---

## ⭐ If you find this model useful, consider giving it a Like on Hugging Face and sharing your feedback!