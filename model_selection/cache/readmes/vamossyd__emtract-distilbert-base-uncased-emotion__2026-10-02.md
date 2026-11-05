---
language:
- en
tags:
- text-classification
- distilbert
- financial-emotion-analysis
- emotion
- twitter
- stocktwits
- pytorch
license: mit
datasets:
- vamossyd/finance_emotions
metrics:
- accuracy
- precision
- recall
- f1
widget:
- text: "to the moon 🚀🚀🚀"
---

# EmTract (DistilBERT-Base-Uncased)

## Model Description

`emtract-distilbert-base-uncased-emotion` is a specialized model finetuned on a combination of [unify-emotion-datasets](https://github.com/sarnthil/unify-emotion-datasets), containing around 250K texts labeled across seven emotion categories: neutral, happy, sad, anger, disgust, surprise, and fear. This model was later adapted to a smaller set of 10K hand-tagged messages from StockTwits. The model is designed to excel at emotion detection in financial social media content such as that found on StockTwits. 

Model parameters were as follows: sequence length of 64, learning rate of 2e-5, batch size of 128, trained for 8 epochs. For steps on how to use the model for inference, please refer to the accompanying Inference.ipynb notebook.

## Training Data

The first part of the training data was obtained from the Unify Emotion Datasets available at [here](https://github.com/sarnthil/unify-emotion-datasets). The second part I obtained
from social media and hand-tagged. It is available [here](https://huggingface.co/datasets/vamossyd/finance_emotions).

## Evaluation Metrics

The model was evaluated using the following metrics:
- Accuracy
- Precision
- Recall
- F1-score

## Research

The underlying research for emotion extraction from financial social media can be found on: [arxiv](https://arxiv.org/abs/2112.03868) and [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3975884).

### Citation

Please cite the following if you use this model:

Vamossy, Domonkos F., and Rolf Skog. "EmTract: Extracting Emotions from Social Media." Available at SSRN 3975884 (2023).

BibTex citation:

```
@article{vamossy2023emtract,
  title={EmTract: Extracting Emotions from Social Media},
  author={Vamossy, Domonkos F and Skog, Rolf},
  journal={Available at SSRN 3975884},
  year={2023}
}
```

### Research using EmTract

[Social Media Emotions and IPO Returns](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4384573)

[Investor Emotions and Earnings Announcements](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3626025])

## License

This project is licensed under the terms of the MIT license.