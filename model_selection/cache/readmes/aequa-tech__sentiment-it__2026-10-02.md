---
license: apache-2.0
pipeline_tag: text-classification
tags:
- sentiment
language:
- it
---
# Sentiment at aequa-tech

## cite this work

```
@inproceedings{arthur2023debunker,
  title={Debunker Assistant: a support for detecting online misinformation},
  author={Arthur, Thomas Edward Capozzi Lupi and Cignarella, Alessandra Teresa and Frenda, Simona and Lai, Mirko and Stranisci, Marco Antonio and Urbinati, Alessandra and others},
  booktitle={Proceedings of the Ninth Italian Conference on Computational Linguistics (CLiC-it 2023)},
  volume={3596},
  pages={1--5},
  year={2023},
  organization={Federico Boschetti, Gianluca E. Lebani, Bernardo Magnini, Nicole Novielli}
}
```


## Model Description

- **Developed by:** [aequa-tech](https://aequa-tech.com/)
- **Funded by:** [NGI-Search](https://www.ngi.eu/ngi-projects/ngi-search/)
- **Language(s) (NLP):** Italian
- **License:** apache-2.0
- **Finetuned from model:** [AlBERTo](https://huggingface.co/m-polignano-uniba/bert_uncased_L-12_H-768_A-12_italian_alberto)

This model is a fine-tuned version of [AlBERTo](https://huggingface.co/m-polignano-uniba/bert_uncased_L-12_H-768_A-12_italian_alberto) Italian model on **sentiment analysis**

# Training Details

## Training Data

- SENTIPOLC [2014](https://live.european-language-grid.eu/catalogue/corpus/7480)/[2016](https://live.european-language-grid.eu/catalogue/corpus/7479)

## Training Hyperparameters

- learning_rate: 2e-5
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam


# Evaluation

## Testing Data
It was tested on SENTIPOLC 2016 test set 

# Framework versions

- Transformers 4.30.2
- Pytorch 2.1.2
- Datasets 2.19.0
- Accelerate 0.30.0

# How to use this model:
```Python
model = AutoModelForSequenceClassification.from_pretrained('aequa-tech/sentiment-it',num_labels=3, ignore_mismatched_sizes=True) 
tokenizer = AutoTokenizer.from_pretrained("m-polignano-uniba/bert_uncased_L-12_H-768_A-12_italian_alb3rt0") 
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer, top_k=None)
classifier("L'insostenibile leggerezza dell'essere")
```
