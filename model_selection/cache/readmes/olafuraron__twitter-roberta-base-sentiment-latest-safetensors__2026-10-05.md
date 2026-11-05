---
license: cc-by-4.0
base_model: cardiffnlp/twitter-roberta-base-sentiment-latest
library_name: transformers
pipeline_tag: text-classification
tags:
- sentiment
- text-classification
- roberta
- safetensors
language: en
widget:
- text: Covid cases are increasing fast!
datasets:
- tweet_eval
---

# Twitter RoBERTa-base Sentiment Analysis (safetensors)

This repository contains a **safetensors-only version** of the model:

**cardiffnlp/twitter-roberta-base-sentiment-latest**

The model performs **sentiment classification** on English tweets and predicts the following labels:

- Negative  
- Neutral  
- Positive  

No architectural changes or retraining have been performed. The only modification is the conversion of model weights to the `safetensors` format.

---

## Original Model

- **Training Data:** ~124M tweets (2018–2021)  
- **Task:** Sentiment analysis (TweetEval benchmark)  
- **Reference Paper:** [TimeLMs](https://arxiv.org/abs/2202.03829)  
- **Original Repository:** [TimeLMs GitHub](https://github.com/cardiffnlp/timelms)  
- **Demo / Integration:** [TweetNLP](https://tweetnlp.org)  

**Label Mapping:**

| ID | Label |
|----|-------|
| 0  | Negative |
| 1  | Neutral  |
| 2  | Positive |

---

## Modifications

- Converted PyTorch weights to `safetensors`  
- Tokenizer and configuration preserved  
- No changes to model behavior, labels, or performance  

---

## References

```bibtex
@inproceedings{camacho-collados-etal-2022-tweetnlp,
    title = "{T}weet{NLP}: Cutting-Edge Natural Language Processing for Social Media",
    author = "Camacho-collados, Jose and Rezaee, Kiamehr and Riahi, Talayeh and Ushio, Asahi and Loureiro, Daniel and Antypas, Dimosthenis and Boisson, Joanne and Espinosa Anke, Luis and Liu, Fangyu and Martínez Cámara, Eugenio and others",
    booktitle = "Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing: System Demonstrations",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, UAE",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.emnlp-demos.5",
    pages = "38--49"
}

@inproceedings{loureiro-etal-2022-timelms,
    title = "{T}ime{LM}s: Diachronic Language Models from {T}witter",
    author = "Loureiro, Daniel and Barbieri, Francesco and Neves, Leonardo and Espinosa Anke, Luis and Camacho-collados, Jose",
    booktitle = "Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics: System Demonstrations",
    month = may,
    year = "2022",
    address = "Dublin, Ireland",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.acl-demo.25",
    doi = "10.18653/v1/2022.acl-demo.25",
    pages = "251--260"
}
```