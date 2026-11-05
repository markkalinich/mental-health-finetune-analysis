---
language:
- ha
- en
license: cc-by-nc-sa-4.0
library_name: transformers
tags:
- hausa
- sentiment-analysis
- text-classification
- code-mixing
- nigeria
base_model: Davlan/afro-xlmr-mini
pipeline_tag: text-classification
---

# HausaSent Hausa sentiment

3-class sentiment model (`negative`, `neutral`, `positive`) for **Hausa** and Hausa–English code-mixed text.

Fine-tuned from [`Davlan/afro-xlmr-mini`](https://huggingface.co/Davlan/afro-xlmr-mini) in the [HausaSent](https://github.com/) teaching/portfolio project.

## Training data

- Extra **synthetic** Hausa / code-mixed templates (market, clinic, school, civic, social). Synthetic text is for coverage, not for published claims.
- Human-labeled [NaijaSenti Hausa](https://github.com/hausanlp/NaijaSenti) tweets (CC BY-NC-SA 4.0).

## Use

```python
from transformers import pipeline

clf = pipeline("text-classification", model="Abduull6771/hausasent-hausa-sentiment")
print(clf("Na ji daɗi da sabis ɗin."))
```

Do not deploy on clinic, school, or civic messages without a human in the loop. Evaluate on your own labeled Hausa before any performance claim.

## Citation

If you use the NaijaSenti portion, cite Muhammad et al. (2022), *NaijaSenti: A Nigerian Twitter Sentiment Corpus for Multilingual Sentiment Analysis*.
