---

library\_name: transformers
tags:

- text-classification
- sentiment-analysis
- imdb
- transformers
- bert

---

# IMDb Sentiment Analysis Model

## Model Details

### Description

This model is a fine-tuned **BERT (bert-base-uncased)** for classifying IMDb movie reviews as **positive** or **negative** sentiment.

- **Model type:** Transformer-based classifier
- **Language:** English
- **Fine-tuned from:** `bert-base-uncased`

### Sources

- **Dataset:** [IMDb Dataset](https://huggingface.co/datasets/stanfordnlp/imdb)
- **Original Paper:** *Maas et al., "Learning Word Vectors for Sentiment Analysis", ACL 2011.*

## Usage

### Direct Use

- Sentiment classification for movie reviews.

### Out-of-Scope Use

- Not suitable for analyzing emotions beyond binary classification.

## Training Details

### Data

- **Dataset:** IMDb Movie Reviews ([stanfordnlp/imdb](https://huggingface.co/datasets/stanfordnlp/imdb))
- **Train Size:** 2000 reviews
- **Test Size:** 2000 reviews

### Training

- **Epochs:** 5
- **Batch Size:** 8
- **Optimizer:** AdamW
- **Learning Rate:** 5e-5

## Evaluation

### Results

| Metric       | Score |
| ------------ | ----- |
| **Accuracy** | 88.8% |
| **F1 Score** | 88.0% |

## Citation

If you use this model, please cite the original dataset:

```bibtex
@InProceedings{maas-EtAl:2011:ACL-HLT2011,
  author    = {Maas, Andrew L. and Daly, Raymond E. and Pham, Peter T. and Huang, Dan and Ng, Andrew Y. and Potts, Christopher},
  title     = {Learning Word Vectors for Sentiment Analysis},
  booktitle = {Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies},
  month     = {June},
  year      = {2011},
  address   = {Portland, Oregon, USA},
  publisher = {Association for Computational Linguistics},
  pages     = {142--150},
  url       = {http://www.aclweb.org/anthology/P11-1015}
}
```

