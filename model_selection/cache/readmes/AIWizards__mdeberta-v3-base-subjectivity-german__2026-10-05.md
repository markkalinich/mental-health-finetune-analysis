---
base_model: microsoft/mdeberta-v3-base
language:
- de
library_name: transformers
license: cc-by-4.0
metrics:
- accuracy
- f1
pipeline_tag: text-classification
tags:
- generated_from_trainer
- subjectivity-detection
- mdeberta-v3
- sentiment
model-index:
- name: mdeberta-v3-base-subjectivity-german
  results: []
datasets:
- MatteoFasulo/clef2025_checkthat_task1_subjectivity
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mdeberta-v3-base-subjectivity-german

This model is a fine-tuned version of [microsoft/mdeberta-v3-base](https://huggingface.co/microsoft/mdeberta-v3-base) for **Subjectivity Detection in News Articles**, as presented in the paper [AI Wizards at CheckThat! 2025: Enhancing Transformer-Based Embeddings with Sentiment for Subjectivity Detection in News Articles](https://arxiv.org/abs/2507.11764).

It was developed as part of AI Wizards' participation in the CLEF 2025 CheckThat! Lab Task 1.

**Code:** [https://github.com/MatteoFasulo/clef2025-checkthat](https://github.com/MatteoFasulo/clef2025-checkthat)

It achieves the following results on the evaluation set:
- Loss: 0.5760
- Macro F1: 0.7720
- Macro P: 0.7687
- Macro R: 0.7763
- Subj F1: 0.7111
- Subj P: 0.6882
- Subj R: 0.7356
- Accuracy: 0.7882

## Model description

This model is designed to classify sentences in news articles as either **subjective** (e.g., opinion-laden) or **objective**. This is a key component in combating misinformation, improving fact-checking pipelines, and supporting journalists. It is based on the `mDeBERTaV3-base` architecture and enhances transformer-based classifiers by integrating sentiment scores, derived from an auxiliary model, with sentence representations. This sentiment-augmented architecture, combined with robust decision threshold calibration to address class imbalance, significantly boosts performance, especially for the subjective F1 score.

## Intended uses & limitations

This model is intended for classifying sentences in news articles as subjective or objective across various languages. It has been evaluated in monolingual (Arabic, German, English, Italian, Bulgarian), multilingual, and zero-shot transfer settings (Greek, Polish, Romanian, Ukrainian). It is particularly useful for applications requiring fine-grained text analysis in news contexts, such as misinformation detection, fact-checking, and journalistic tools.

**Limitations:**
While designed to handle class imbalance through decision threshold calibration, the model's performance on certain languages or specific class distributions might vary. As highlighted in the original work, initial submission errors revealed the sensitivity to proper calibration. The model's primary focus is on news article text, and its generalization to other domains or highly nuanced subjective expressions might vary.

## Training and evaluation data

The model was trained and evaluated on datasets provided for the **CLEF 2025 CheckThat! Lab Task 1: Subjectivity Detection in News Articles**. Training and development datasets were provided for Arabic, German, English, Italian, and Bulgarian. For final evaluation, additional unseen languages (e.g., Greek, Romanian, Polish, Ukrainian) were included to assess generalization capabilities. The training process focused on enhancing transformer embeddings with sentiment signals and employing decision threshold calibration to mitigate class imbalance prevalent across languages.

## How to use
You can use this model directly with the Hugging Face `transformers` library for text classification:

```python
from transformers import pipeline

# Load the text classification pipeline
classifier = pipeline(
    "text-classification",
    model="MatteoFasulo/mdeberta-v3-base-subjectivity-german",
    tokenizer="microsoft/mdeberta-v3-base",
)

# Example usage for an objective sentence
text1 = "Das Unternehmen meldete im letzten Quartal einen Gewinnanstieg von 10 %."
result1 = classifier(text1)
print(f"Text: '{text1}' Classification: {result1}")
# Expected output: [{'label': 'OBJ', 'score': ...}]

# Example usage for a subjective sentence
text2 = "Dieses Produkt ist absolut erstaunlich und jeder sollte es ausprobieren!"
result2 = classifier(text2)
print(f"Text: '{text2}' Classification: {result2}")
# Expected output: [{'label': 'SUBJ', 'score': ...}]

```

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | Macro F1 | Macro P | Macro R | Subj F1 | Subj P | Subj R | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:-------:|:-------:|:-------:|:------:|:------:|:--------:|
| No log        | 1.0   | 50   | 0.6877          | 0.3923   | 0.3228  | 0.5     | 0.0     | 0.0    | 0.0    | 0.6456   |
| No log        | 2.0   | 100  | 0.5385          | 0.7231   | 0.7351  | 0.7562  | 0.6898  | 0.5775 | 0.8563 | 0.7271   |
| No log        | 3.0   | 150  | 0.4951          | 0.7880   | 0.7828  | 0.7975  | 0.7366  | 0.6919 | 0.7874 | 0.8004   |
| No log        | 4.0   | 200  | 0.5192          | 0.7830   | 0.7817  | 0.7845  | 0.7216  | 0.7135 | 0.7299 | 0.8004   |
| No log        | 5.0   | 250  | 0.5602          | 0.7794   | 0.7798  | 0.7790  | 0.7147  | 0.7168 | 0.7126 | 0.7984   |
| No log        | 6.0   | 300  | 0.5760          | 0.7720   | 0.7687  | 0.7763  | 0.7111  | 0.6882 | 0.7356 | 0.7882   |


### Framework versions

- Transformers 4.49.0
- Pytorch 2.5.1+cu121
- Datasets 3.3.1
- Tokenizers 0.21.0

## Citation

If you find our work helpful or inspiring, please feel free to cite it:

```bibtex
@misc{fasulo2025aiwizardscheckthat2025,
      title={AI Wizards at CheckThat! 2025: Enhancing Transformer-Based Embeddings with Sentiment for Subjectivity Detection in News Articles}, 
      author={Matteo Fasulo and Luca Babboni and Luca Tedeschini},
      year={2025},
      eprint={2507.11764},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2507.11764}, 
}
```