---
library_name: setfit
tags:
- setfit
- sentence-transformers
- text-classification
- generated_from_setfit_trainer
base_model: sentence-transformers/sentence-t5-large
metrics:
- accuracy
widget:
- text: How to write a science fiction novel
- text: Overcoming social anxiety and fear of public speaking
- text: Supporting a family member with depression
- text: Understanding stock market trends
- text: Recipes for homemade Italian pasta
pipeline_tag: text-classification
inference: true
model-index:
- name: SetFit with sentence-transformers/sentence-t5-large
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: Unknown
      type: unknown
      split: test
    metrics:
    - type: accuracy
      value: 1.0
      name: Accuracy
---

# SetFit with sentence-transformers/sentence-t5-large

This is a [SetFit](https://github.com/huggingface/setfit) model that can be used for Text Classification. This SetFit model uses [sentence-transformers/sentence-t5-large](https://huggingface.co/sentence-transformers/sentence-t5-large) as the Sentence Transformer embedding model. A [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) instance is used for classification.

The model has been trained using an efficient few-shot learning technique that involves:

1. Fine-tuning a [Sentence Transformer](https://www.sbert.net) with contrastive learning.
2. Training a classification head with features from the fine-tuned Sentence Transformer.

## Model Details

### Model Description
- **Model Type:** SetFit
- **Sentence Transformer body:** [sentence-transformers/sentence-t5-large](https://huggingface.co/sentence-transformers/sentence-t5-large)
- **Classification head:** a [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) instance
- **Maximum Sequence Length:** 256 tokens
- **Number of Classes:** 2 classes
<!-- - **Training Dataset:** [Unknown](https://huggingface.co/datasets/unknown) -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Repository:** [SetFit on GitHub](https://github.com/huggingface/setfit)
- **Paper:** [Efficient Few-Shot Learning Without Prompts](https://arxiv.org/abs/2209.11055)
- **Blogpost:** [SetFit: Efficient Few-Shot Learning Without Prompts](https://huggingface.co/blog/setfit)

### Model Labels
| Label | Examples                                                                                                                                                                                                   |
|:------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| True  | <ul><li>'Exploring historical landmarks in Europe'</li><li>'How to create an effective resume'</li><li>'Exercises to improve core strength'</li></ul>                                                      |
| False | <ul><li>'Feeling sad or empty for long periods without any specific reason'</li><li>'Dealing with the emotional impact of chronic illness'</li><li>'Understanding and coping with panic attacks'</li></ul> |

## Evaluation

### Metrics
| Label   | Accuracy |
|:--------|:---------|
| **all** | 1.0      |

## Uses

### Direct Use for Inference

First install the SetFit library:

```bash
pip install setfit
```

Then you can load this model and run inference.

```python
from setfit import SetFitModel

# Download from the 🤗 Hub
model = SetFitModel.from_pretrained("richie-ghost/setfit-sentence-t5-large-MentalHealth-Topic-Check")
# Run inference
preds = model("Understanding stock market trends")
```

<!--
### Downstream Use

*List how someone could finetune this model on their own dataset.*
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Set Metrics
| Training set | Min | Median | Max |
|:-------------|:----|:-------|:----|
| Word count   | 4   | 6.4583 | 11  |

| Label | Training Sample Count |
|:------|:----------------------|
| True  | 22                    |
| False | 26                    |

### Training Hyperparameters
- batch_size: (16, 16)
- num_epochs: (8, 8)
- max_steps: -1
- sampling_strategy: oversampling
- body_learning_rate: (2e-05, 1e-05)
- head_learning_rate: 0.01
- loss: CosineSimilarityLoss
- distance_metric: cosine_distance
- margin: 0.25
- end_to_end: False
- use_amp: False
- warmup_proportion: 0.1
- seed: 42
- eval_max_steps: -1
- load_best_model_at_end: True

### Training Results
| Epoch   | Step    | Training Loss | Validation Loss |
|:-------:|:-------:|:-------------:|:---------------:|
| 0.0132  | 1       | 0.2504        | -               |
| 0.6579  | 50      | 0.2115        | -               |
| 1.0     | 76      | -             | 0.122           |
| 1.3158  | 100     | 0.0335        | -               |
| 1.9737  | 150     | 0.007         | -               |
| 2.0     | 152     | -             | 0.0352          |
| 2.6316  | 200     | 0.0037        | -               |
| 3.0     | 228     | -             | 0.0229          |
| 3.2895  | 250     | 0.0019        | -               |
| 3.9474  | 300     | 0.0016        | -               |
| 4.0     | 304     | -             | 0.0199          |
| 4.6053  | 350     | 0.001         | -               |
| 5.0     | 380     | -             | 0.0162          |
| 5.2632  | 400     | 0.0009        | -               |
| 5.9211  | 450     | 0.0006        | -               |
| 6.0     | 456     | -             | 0.0141          |
| 6.5789  | 500     | 0.0008        | -               |
| **7.0** | **532** | **-**         | **0.0133**      |
| 7.2368  | 550     | 0.0008        | -               |
| 7.8947  | 600     | 0.0006        | -               |
| 8.0     | 608     | -             | 0.0154          |

* The bold row denotes the saved checkpoint.
### Framework Versions
- Python: 3.10.12
- SetFit: 1.0.3
- Sentence Transformers: 2.7.0
- Transformers: 4.40.0
- PyTorch: 2.2.1+cu121
- Datasets: 2.19.0
- Tokenizers: 0.19.1

## Citation

### BibTeX
```bibtex
@article{https://doi.org/10.48550/arxiv.2209.11055,
    doi = {10.48550/ARXIV.2209.11055},
    url = {https://arxiv.org/abs/2209.11055},
    author = {Tunstall, Lewis and Reimers, Nils and Jo, Unso Eun Seo and Bates, Luke and Korat, Daniel and Wasserblat, Moshe and Pereg, Oren},
    keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
    title = {Efficient Few-Shot Learning Without Prompts},
    publisher = {arXiv},
    year = {2022},
    copyright = {Creative Commons Attribution 4.0 International}
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->