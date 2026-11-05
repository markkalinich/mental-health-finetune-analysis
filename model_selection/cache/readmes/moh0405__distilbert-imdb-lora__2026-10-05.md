---
library_name: transformers
tags:
- sentiment-analysis
- lora
- peft
- imdb
license: apache-2.0
base_model: distilbert-base-uncased
---

# distilbert-imdb-lora

# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->



## Model Details

### Model Description

Fine-tuned version of `distilbert-base-uncased` for binary sentiment classification,
adapted using LoRA (Low-Rank Adaptation) rather than full fine-tuning.

- **Developed by:** Mohammad (moh0405)
- **Model type:** Text classification (sequence classification)
- **Language(s):** English
- **License:** Apache 2.0
- **Finetuned from model:** distilbert-base-uncased

### Model Sources [optional]

<!-- Provide the basic links for the model. -->

- **Repository:** [More Information Needed]
- **Paper [optional]:** [More Information Needed]
- **Demo [optional]:** [More Information Needed]

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

### Direct Use

Classifies English-language text (originally movie reviews) as POSITIVE or NEGATIVE
sentiment. Suitable for quick sentiment tagging tasks similar in style to IMDB reviews.

### Downstream Use [optional]

<!-- This section is for the model use when fine-tuned for a task, or when plugged into a larger ecosystem/app -->

[More Information Needed]

### Out-of-Scope Use

Not intended for nuanced/mixed sentiment detection, non-English text, or domains far
from movie reviews (e.g. financial sentiment, medical text) without further fine-tuning.
Trained on a small subset for a learning exercise — not validated for production use.

[More Information Needed]

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

[More Information Needed]

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model. More information needed for further recommendations.

## How to Get Started with the Model

​```python
from transformers import pipeline

classifier = pipeline("text-classification", model="moh0405/distilbert-imdb-lora")
result = classifier("This movie was surprisingly good.")
print(result)
​```

[More Information Needed]

## Training Details

### Training Data

Subset of the IMDB movie review dataset (`stanfordnlp/imdb`) — 2,000 training examples,
500 evaluation examples, randomly sampled (seed=42) from the full 25,000/25,000 split.
[More Information Needed]

### Training Procedure

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

#### Preprocessing [optional]

[More Information Needed]


#### Training Hyperparameters

- **Method:** LoRA (PEFT), r=8, alpha=16, dropout=0.1, target_modules=["q_lin","v_lin"]
- **Trainable parameters:** 739,586 / 67,694,596 total (1.09%)
- **Epochs:** 1
- **Batch size:** 16 (train), 32 (eval)
- **Training regime:** fp32
#### Speeds, Sizes, Times [optional]

<!-- This section provides information about throughput, start/end time, checkpoint size if relevant, etc. -->

[More Information Needed]

## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

### Testing Data, Factors & Metrics
#### Testing Data
500-example held-out split from `stanfordnlp/imdb` test set.

#### Metrics
Accuracy



#### Factors

<!-- These are the things the evaluation is disaggregating by, e.g., subpopulations or domains. -->

[More Information Needed]


[More Information Needed]

### Results

| Stage | Accuracy |
|---|---|
| Before fine-tuning | 50.8% |
| After fine-tuning (1 epoch) | 78.6% |

#### Summary



## Model Examination [optional]

<!-- Relevant interpretability work for the model goes here -->

[More Information Needed]

## Environmental Impact

<!-- Total emissions (in grams of CO2eq) and additional considerations, such as electricity usage, go here. Edit the suggested text below accordingly -->

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).

- **Hardware Type:** [More Information Needed]
- **Hours used:** [More Information Needed]
- **Cloud Provider:** [More Information Needed]
- **Compute Region:** [More Information Needed]
- **Carbon Emitted:** [More Information Needed]

## Technical Specifications [optional]

### Model Architecture and Objective

[More Information Needed]

### Compute Infrastructure

[More Information Needed]

#### Hardware
Apple Mac Mini (Apple Silicon, MPS backend)

#### Software
transformers, peft, datasets, PyTorch

## Citation [optional]

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

[More Information Needed]

**APA:**

[More Information Needed]

## Glossary [optional]

<!-- If relevant, include terms and calculations in this section that can help readers understand the model or model card. -->

[More Information Needed]

## More Information [optional]

[More Information Needed]

## Model Card Authors [optional]

[More Information Needed]

## Model Card Contact

[More Information Needed]