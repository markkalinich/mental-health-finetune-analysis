---
library_name: transformers
tags:
- politics
- parliamnet
- sentiment-analysis
---

# Model Card for Model ID

<!-- -->
Fine-tuned BERT trained to identify political party from speech in the UK Parliament. Trained with Labour/Conservative speeches using the hansard dataset 2000-2020 


## Model Details

- **License:** MIT
- **Finetuned from model :** BERT

### Model Sources

<!-- Provide the basic links for the model. -->

- **Repository:** [Available on Github](https://github.com/gitvan711/Party-Political-Sentiment-Analysis)


## Uses

Model can be used to predict whether an item of speech from the UK Parliament was said by a member of the Labour or Conservative Party.

### Out-of-Scope Use

Model has only been exposed to UK data and speeches from Labour or Conservative. May not work as intended for other parties or geographies.

### Training Data

[biglam/hansard_speech](https://huggingface.co/datasets/biglam/hansard_speech)

#### Preprocessing

[bert-cased]

## Evaluation

Evaluated on held-out test data. Achieved test accuracy >80% and test loss <0.4 (binary cross-entropy).

## Citation

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

@misc{baly2020detect,
      title={We Can Detect Your Bias: Predicting the Political Ideology of News Articles}, 
      author={Ramy Baly and Giovanni Da San Martino and James Glass and Preslav Nakov},
      year={2020},
      eprint={2010.05338},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}