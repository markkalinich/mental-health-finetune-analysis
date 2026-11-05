---
tags:
- setfit
- sentence-transformers
- text-classification
- generated_from_setfit_trainer
widget:
- text: 'Procedure note: Colonoscopy completed. Findings consistent with diverticulosis.
    CPT 45378 used.'
- text: 'Patient diagnosed with Acute appendicitis (ICD-10-CM: K35.80). Appendectomy
    performed (CPT: 44950).'
- text: If your child shows signs of anxiety, consider talking to a pediatric psychologist.
- text: Encounter billed under APC 5371. Patient stable. To follow up with PCP.
- text: Learn how cognitive behavioral therapy can improve focus and reduce anxiety.
metrics:
- accuracy
pipeline_tag: text-classification
library_name: setfit
inference: true
base_model: sentence-transformers/paraphrase-minilm-l6-v2
---

# SetFit with sentence-transformers/paraphrase-minilm-l6-v2

This is a [SetFit](https://github.com/huggingface/setfit) model that can be used for Text Classification. This SetFit model uses [sentence-transformers/paraphrase-minilm-l6-v2](https://huggingface.co/sentence-transformers/paraphrase-minilm-l6-v2) as the Sentence Transformer embedding model. A [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) instance is used for classification.

The model has been trained using an efficient few-shot learning technique that involves:

1. Fine-tuning a [Sentence Transformer](https://www.sbert.net) with contrastive learning.
2. Training a classification head with features from the fine-tuned Sentence Transformer.

## Model Details

### Model Description
- **Model Type:** SetFit
- **Sentence Transformer body:** [sentence-transformers/paraphrase-minilm-l6-v2](https://huggingface.co/sentence-transformers/paraphrase-minilm-l6-v2)
- **Classification head:** a [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) instance
- **Maximum Sequence Length:** 128 tokens
- **Number of Classes:** 2 classes
<!-- - **Training Dataset:** [Unknown](https://huggingface.co/datasets/unknown) -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Repository:** [SetFit on GitHub](https://github.com/huggingface/setfit)
- **Paper:** [Efficient Few-Shot Learning Without Prompts](https://arxiv.org/abs/2209.11055)
- **Blogpost:** [SetFit: Efficient Few-Shot Learning Without Prompts](https://huggingface.co/blog/setfit)

### Model Labels
| Label   | Examples                                                                                                                                                                                                                                                                                                                                   |
|:--------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| med     | <ul><li>'Patient diagnosed with Acute appendicitis (ICD-10-CM: K35.80). Appendectomy performed (CPT: 44950).'</li><li>'Follow-up on 04/10/2025. Status post laparoscopic cholecystectomy (ICD-10: K81.1, CPT: 47562).'</li><li>'Procedure note: Colonoscopy completed. Findings consistent with diverticulosis. CPT 45378 used.'</li></ul> |
| general | <ul><li>'The Chinese gender calendar predicts baby gender based on conception month and mother’s age.'</li><li>'This article outlines tips for stress management through meditation and mindfulness.'</li><li>'Eating a balanced diet and regular exercise improves overall well-being.'</li></ul>                                         |

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
model = SetFitModel.from_pretrained("ashercn97/medicalcode-classifier-v1")
# Run inference
preds = model("Encounter billed under APC 5371. Patient stable. To follow up with PCP.")
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
| Training set | Min | Median  | Max |
|:-------------|:----|:--------|:----|
| Word count   | 10  | 11.4375 | 14  |

| Label   | Training Sample Count |
|:--------|:----------------------|
| med     | 8                     |
| general | 8                     |

### Training Hyperparameters
- batch_size: (8, 8)
- num_epochs: (2, 2)
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
- l2_weight: 0.01
- seed: 42
- eval_max_steps: -1
- load_best_model_at_end: False

### Training Results
| Epoch  | Step | Training Loss | Validation Loss |
|:------:|:----:|:-------------:|:---------------:|
| 0.0556 | 1    | 0.4261        | -               |

### Framework Versions
- Python: 3.10.12
- SetFit: 1.1.2
- Sentence Transformers: 4.0.2
- Transformers: 4.51.2
- PyTorch: 2.6.0+cpu
- Datasets: 3.5.0
- Tokenizers: 0.21.1

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