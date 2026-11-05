---
language:
- nso
license: apache-2.0
tags:
- text-classification
- sentiment-analysis
- sepedi
- northern-sotho
- african-languages
- community-sovereignty
pipeline_tag: text-classification
---

# Sepedi Sentiment Classifier v1.0

**Developer:** TSEBO SOVEREIGN TECH | Licensed to Sediba AI NPC  
**Language:** Sepedi / Northern Sotho (nso)  
**Task:** Sentiment Classification  
**License:** Apache-2.0 + Community Sovereignty License

## Model Description

BERT-based sentiment classifier for Sepedi. Trained on 1,495,728 professional linguistic texts from SADiLaR (South African Centre for Digital Language Resources).

This is the **first public sentiment classifier for Sepedi**, developed as part of the **Sediba AI** community intelligence platform serving Limpopo.

## Usage

```python
from transformers import pipeline

classifier = pipeline('text-classification', 
                     model='Sediba-AI/sepedi-sentiment-classifier')

result = classifier('Ubuntu o motle')
print(result)
```

## Training Data

| Source | Texts | Share |
|--------|-------|-------|
| SADILAR NCHLT Annotated Corpus | 1,423,467 | 95% |
| Lwazi Dictionaries | 72,261 | 5% |
| **Total** | **1,495,728** | **100%** |

## Model Details

- **Base Model:** BERT (bert-base-multilingual-cased)
- **Framework:** Hugging Face Transformers
- **Training Samples:** 1,495,728
- **Labels:** POSITIVE, NEGATIVE, NEUTRAL
- **Accuracy:** 100% on internal test set (n=40)

## Governance

**Data Sovereignty:** Yarena Framework (Sediba AI governance layer)  
**Community Benefit:** Kutollo Exchange (75% Community / 15% NPC / 10% Developer)  
**Consent Model:** FPIC (Free, Prior and Informed Consent)

## Citation

```bibtex
@misc{sediba_ai_sepedi_sentiment_2026,
  title={Sepedi Sentiment Classifier: Community-Sovereign NLP},
  author={Lemekoana, Lehlohonolo Owen and TSEBO SOVEREIGN TECH},
  year={2026},
  publisher={Hugging Face},
  url={https://huggingface.co/Sediba-AI/sepedi-sentiment-classifier}
}
```

## License

Dual-licensed under Apache-2.0 (research use) and Community Sovereignty License (commercial use).

---

**Developed by:** TSEBO SOVEREIGN TECH (Pty) Ltd  
**For:** Sediba AI NPC | Mankweng, Limpopo, South Africa  
**GitHub:** [sediba-ai](https://github.com/sediba-ai)
