---
library_name: transformers
pipeline_tag: text-classification
language:
- en
license: apache-2.0
datasets:
- JosefGoldstein/aimlessinnovations_customer_sentiment
tags:
- text-classification
- sentiment-analysis
- ai-vs-karen
- autotrain
base_model: answerdotai/ModernBERT-base
thumbnail: ./ai-vs-karen-thumb.png
new_version: JosefGoldstein/modernBERT-base-AIvsKaren-sentiment-6class
---

# ModernBERT AI vs. Karen Sentiment Classifier

![AI vs. Karen Demo Banner](./ai-vs-karen-banner.png)

A fine-tuned **ModernBERT** model that classifies short messages and reviews into **five sentiment levels**:
`very_negative`, `negative`, `neutral`, `positive`, `very_positive`.

This model was trained for the **AI vs. Karen** talk demo.  
The primary objective is detecting customer sentiment for *Aimless Innovations Inc.*—a faux e-commerce website selling useless products, used for demo purposes.  

This model was fine-tuned from [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) for the "AI vs. Karen" demo using [JosefGoldstein/aimlessinnovations_customer_sentiment](https://huggingface.co/datasets/JosefGoldstein/aimlessinnovations_customer_sentiment), a 5-class synthetic sentiment dataset for Aimless Innovations Inc.



> **TL;DR**
> - **Task:** 5-class sentiment for short texts (support chats & reviews).  
> - **Domain:** Realistic + synthetic “Karen-verse” messages.  
> - **Backbone:** ModernBERT.  
> - **Trainer:** 🤗 **AutoTrain** (author clicked “Go”, whispered a small prayer, and here we are).  
> - **Style:** Robust on sarcasm, emojis, and all-caps “NEVER SHOPPING HERE AGAIN”.  




## How to Use

### Requirements
Since the `transformers` library only supports the ModernBERT architecture starting from **4.48.0**, make sure you have a recent version installed:


```bash
pip install "transformers>=4.48.0"
```

If your GPU supports it, the efficient Flash Attention 2 can be used automatically if you have `flash_attn` installed. It is not mandatory.

```bash
pip install flash-attn
```

### Quick start

```python
from transformers import pipeline

clf = pipeline(
    "text-classification",
    model="JosefGoldstein/modernBERT-base-AIvsKaren-sentiment",  
    device_map="auto"
)

samples = [
    # very_negative
    "I want to speak to your manager's manager's MANAGER! 🤬",
    # negative
    "I'm giving this a solid meh out of ten.",
    # neutral
    "Quick question: is this made from sustainable materials?",
    # positive
    "My cat gives it a thumbs up. Which, if you know my cat, is a big deal.",
    # very_positive
    "BRUH, this goes hard — makes me smile. legit game-changer! 👌"
]

preds = clf(samples)
for text, pred in zip(samples, preds):
    top = max(pred, key=lambda x: x["score"])
    print(text)
    print(f" -> {top['label']} ({top['score']:.3f})\n")

```


## Validation Metrics (TL;DR)
This model was trained and validated using 🤗 AutoTrain

| metric               | score |
|----------------------|-------:|
| accuracy / f1_micro  | 0.835 |
| f1_macro             | 0.831 |
| f1_weighted          | 0.839 |
| precision_macro      | 0.839 |
| precision_weighted   | 0.856 |
| recall_macro         | 0.836 |
| recall_weighted      | 0.835 |
| loss                 | 0.694 |


## Citation

If this helped your project, cite me:

```bibtex
software{modernbert_ai_vs_karen_2025,
  title        = {ModernBERT AI vs. Karen Sentiment Classifer},
  author       = {Goldstein, Josef},
  year         = {2025},
  url          = {https://huggingface.co/JosefGoldstein/modernBERT-base-AIvsKaren-sentiment}
}
```

## Disclaimer

This sentiment analysis model was trained on the gloriously **unhinged**
[Aimless Innovations Customer Sentiment](https://huggingface.co/datasets/JosefGoldstein/aimlessinnovations_customer_sentiment) dataset.  
Great for demo and spicy support messages—not so much for high-stakes decisions.  
This is a legit sentiment analysis model that might work for your use case, but **use at your own risk.**  
If it breaks prod, don't come crying to me.