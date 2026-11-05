---
base_model: microsoft/mdeberta-v3-base
library_name: transformers
license: cc-by-4.0
metrics:
- accuracy
- f1
tags:
- generated_from_trainer
- deberta-v3
- subjectivity-detection
- multilingual
- text-classification
- sentiment-analysis
model-index:
- name: mdeberta-v3-base-subjectivity-multilingual
  results: []
pipeline_tag: text-classification
language:
- ar
- de
- en
- it
- bg
- el
- pl
- ro
- uk
datasets:
- MatteoFasulo/clef2025_checkthat_task1_subjectivity
arxiv_id: 2507.11764
code_url: https://github.com/MatteoFasulo/clef2025-checkthat
---

# mdeberta-v3-base-subjectivity-multilingual

This model is a fine-tuned version of [microsoft/mdeberta-v3-base](https://huggingface.co/microsoft/mdeberta-v3-base) for **Subjectivity Detection in News Articles**. It was developed as part of **AI Wizards' participation in the CLEF 2025 CheckThat! Lab Task 1**.

The model was presented in the paper [AI Wizards at CheckThat! 2025: Enhancing Transformer-Based Embeddings with Sentiment for Subjectivity Detection in News Articles](https://huggingface.co/papers/2507.11764).

It achieves the following results on the evaluation set:
- Loss: 0.8345
- Macro F1: 0.7475
- Macro P: 0.7530
- Macro R: 0.7439
- Subj F1: 0.6824
- Subj P: 0.7145
- Subj R: 0.6531
- Accuracy: 0.7643

## Model description

This model, `mdeberta-v3-base-subjectivity-multilingual`, is designed to classify sentences as subjective (opinion-laden) or objective (fact-based) within news articles. It was developed by AI Wizards for the CLEF 2025 CheckThat! Lab Task 1: Subjectivity Detection in News Articles.

The core innovation of this model lies in enhancing standard transformer-based classifiers by integrating sentiment scores, derived from an auxiliary model, with sentence representations. This sentiment-augmented architecture, built upon mDeBERTaV3-base, aims to significantly improve performance, particularly for the subjective F1 score. To counteract prevalent class imbalance across languages, decision threshold calibration optimized on the development set was employed.

The model was evaluated across:
*   **Monolingual** settings (Arabic, German, English, Italian, and Bulgarian)
*   **Zero-shot transfer** settings (Greek, Polish, Romanian, and Ukrainian)
*   **Multilingual** training

This framework led to high rankings in the competition, notably achieving 1st place for Greek (Macro F1 = 0.51).

## Intended uses & limitations

**Intended uses:**
This model is intended for research and practical applications involving subjectivity detection, particularly in news media. Specific uses include:
*   Classifying sentences in news articles as subjective or objective.
*   Supporting fact-checking pipelines by identifying opinionated content.
*   Assisting journalists in analyzing text for bias or subjective reporting.
*   Applications in both monolingual and multilingual contexts, including zero-shot scenarios for unseen languages.

**Limitations:**
*   Performance may vary across different languages, especially in zero-shot settings, despite efforts for generalization.
*   The effectiveness of the sentiment augmentation relies on the quality and domain relevance of the auxiliary sentiment model.
*   While designed for news articles, its performance might differ on other text genres or domains.
*   Like other large language models, it may carry biases present in its training data.

## Training and evaluation data

The model was fine-tuned on training and development datasets provided for the CLEF 2025 CheckThat! Lab Task 1. These datasets included sentences from news articles in Arabic, German, English, Italian, and Bulgarian. For final evaluation, additional unseen languages such as Greek, Romanian, Polish, and Ukrainian were included to assess the model's generalization capabilities. Class imbalance issues, which were prevalent across languages, were addressed through decision threshold calibration.

## How to use

You can easily use this model with the Hugging Face `transformers` library:

```python
from transformers import pipeline

# Load the text classification pipeline
classifier = pipeline(
    "text-classification",
    model="MatteoFasulo/mdeberta-v3-base-subjectivity-multilingual",
    tokenizer="microsoft/mdeberta-v3-base",
)

# Example usage:
result1 = classifier("Questa è una scoperta affascinante e fantastica!")
print(f"Classification: {result1}")
# Expected output: [{'label': 'SUBJ', 'score': ...}]

result2 = classifier("The capital of France is Paris.")
print(f"Classification: {result2}")
# Expected output: [{'label': 'OBJ', 'score': ...}]
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
| No log        | 1.0   | 402  | 0.5033          | 0.7390   | 0.7457  | 0.7584  | 0.7145  | 0.6246 | 0.8346 | 0.7414   |
| 0.6065        | 2.0   | 804  | 0.5285          | 0.7457   | 0.7440  | 0.7551  | 0.7064  | 0.6524 | 0.7701 | 0.7518   |
| 0.4631        | 3.0   | 1206 | 0.6583          | 0.7328   | 0.7311  | 0.7353  | 0.6785  | 0.6609 | 0.6971 | 0.7439   |
| 0.394         | 4.0   | 1608 | 0.7692          | 0.7255   | 0.7327  | 0.7215  | 0.6523  | 0.6924 | 0.6165 | 0.7451   |
| 0.3475        | 5.0   | 2010 | 0.7538          | 0.7438   | 0.7414  | 0.7481  | 0.6951  | 0.6667 | 0.7261 | 0.7530   |
| 0.3475        | 6.0   | 2412 | 0.8345          | 0.7475   | 0.7530  | 0.7439  | 0.6824   | 0.7145 | 0.6531 | 0.7643   |


### Framework versions

- Transformers 4.49.0
- Pytorch 2.5.1+cu121
- Datasets 3.3.1
- Tokenizers 0.21.0

## GitHub Repository

The code and materials for this model are available on GitHub: [MatteoFasulo/clef2025-checkthat](https://github.com/MatteoFasulo/clef2025-checkthat)

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