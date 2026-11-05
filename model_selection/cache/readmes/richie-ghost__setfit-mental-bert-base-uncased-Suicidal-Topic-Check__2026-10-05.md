---
library_name: setfit
tags:
- setfit
- sentence-transformers
- text-classification
- generated_from_setfit_trainer
base_model: mental/mental-bert-base-uncased
metrics:
- accuracy
widget:
- text: I let myself go, I make no effort to eat, sleep or take care of myself.
- text: There's no structure in my life, and that makes me even sicker.
- text: I'm drifting away from my friends, my family, games that I couldn't possibly
    know anything about.
- text: My grandmother's homemade pasta recipe is the best, nothing else compares
    to it.
- text: It's frustrating to realize I've made yet another impulsive choice that sets
    me back instead of moving forward.
pipeline_tag: text-classification
inference: true
model-index:
- name: SetFit with mental/mental-bert-base-uncased
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
      value: 0.8275862068965517
      name: Accuracy
---

# SetFit with mental/mental-bert-base-uncased

This is a [SetFit](https://github.com/huggingface/setfit) model that can be used for Text Classification. This SetFit model uses [mental/mental-bert-base-uncased](https://huggingface.co/mental/mental-bert-base-uncased) as the Sentence Transformer embedding model. A [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) instance is used for classification.

The model has been trained using an efficient few-shot learning technique that involves:

1. Fine-tuning a [Sentence Transformer](https://www.sbert.net) with contrastive learning.
2. Training a classification head with features from the fine-tuned Sentence Transformer.

## Model Details

### Model Description
- **Model Type:** SetFit
- **Sentence Transformer body:** [mental/mental-bert-base-uncased](https://huggingface.co/mental/mental-bert-base-uncased)
- **Classification head:** a [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) instance
- **Maximum Sequence Length:** 512 tokens
- **Number of Classes:** 8 classes
<!-- - **Training Dataset:** [Unknown](https://huggingface.co/datasets/unknown) -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Repository:** [SetFit on GitHub](https://github.com/huggingface/setfit)
- **Paper:** [Efficient Few-Shot Learning Without Prompts](https://arxiv.org/abs/2209.11055)
- **Blogpost:** [SetFit: Efficient Few-Shot Learning Without Prompts](https://huggingface.co/blog/setfit)

### Model Labels
| Label                           | Examples                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|:--------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Presence of a loved one         | <ul><li>"Living alone feels like a double-edged sword, on one hand, I have my privacy, but on the other hand, there's no one around to support me when I'm feeling like shit."</li><li>'I have no one to talk to or no one who understands me.'</li><li>'I wish I had a shoulder to lean on when everything is falling apart.'</li></ul>                                                                                                               |
| Previous attempt                | <ul><li>'Shit got real after my last attempt, i woke up surrounded by a bunch of medical equipment, wondering what the fuck happened.'</li><li>"Looking back at my attempts, I can't deny there's a part of me that's glad they didn't work, but there's also this nagging voice wondering if I missed my chance."</li><li>"In the past, I tried to end it all, but I'm in the same situation now."</li></ul>                                          |
| Ability to take care of oneself | <ul><li>"I've let go of everything that used to matter to me, my hobbies, my friends, everything seems uninteresting."</li><li>"It's hard to maintain a routine or assume my responsibilities, I've completely dropped out."</li><li>"I'm so disoriented, I forget important things and it's making my situation worse."</li></ul>                                                                                                                     |
| Ability to hope for change      | <ul><li>"I'm just so tired of feeling stuck, every day feels the same, and I can't see any way out, I need help finding hope for a change in my life.,"</li><li>'I feel so isolated in all of this, like nobody would ever understand what I’m going through.'</li><li>"I don't know what to do anymore, it feels like my reason to live has been completely drained away, i'm desperately searching for any glimmer of hope to hold onto.,"</li></ul> |
| Other                           | <ul><li>"My garden has been thriving this summer, it's so rewarding to see everything in bloom."</li><li>"I've been trying to be more sustainable, I even started composting my food scraps."</li><li>"I've been learning to play the piano lately, it's so fulfilling to see my progress."</li></ul>                                                                                                                                                  |
| Suicidal planning               | <ul><li>"I don't want to be here anymore, I don't want to endure this, I'm seriously thinking about killing myself."</li><li>"I've had thoughts of ending my life."</li><li>"Sometimes, I imagine myself in this life, and I don't see the point of it all."</li></ul>                                                                                                                                                                                 |
| Ability to control oneself      | <ul><li>"I wish I could put my brain on pause, just so I don't act on impulse all the time."</li><li>'I try to focus, but my thoughts are too fast and I act before considering the consequences.'</li><li>"I can't stop myself from falling apart, no matter how hard I try."</li></ul>                                                                                                                                                               |
| Consumption                     | <ul><li>"Drinking has become my go-to escape from this overwhelming situation, It's like I can't deal with it sober anymore."</li><li>"The more I struggle with this distressing situation, the more I find solace in drinking, It's becoming a dangerous habit that's tough to break."</li><li>'Lately, when shit hits the fan, I find myself reaching for the bottle'</li></ul>                                                                      |

## Evaluation

### Metrics
| Label   | Accuracy |
|:--------|:---------|
| **all** | 0.8276   |

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
model = SetFitModel.from_pretrained("richie-ghost/setfit-mental-bert-base-uncased-Suicidal-Topic-Check")
# Run inference
preds = model("There's no structure in my life, and that makes me even sicker.")
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
| Word count   | 7   | 18.3582 | 40  |

| Label                           | Training Sample Count |
|:--------------------------------|:----------------------|
| Suicidal planning               | 9                     |
| Previous attempt                | 11                    |
| Presence of a loved one         | 8                     |
| Other                           | 9                     |
| Consumption                     | 6                     |
| Ability to take care of oneself | 8                     |
| Ability to hope for change      | 7                     |
| Ability to control oneself      | 9                     |

### Training Hyperparameters
- batch_size: (16, 16)
- num_epochs: (10, 10)
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
| Epoch   | Step     | Training Loss | Validation Loss |
|:-------:|:--------:|:-------------:|:---------------:|
| 0.0041  | 1        | 0.3127        | -               |
| 0.2041  | 50       | 0.1378        | -               |
| 0.4082  | 100      | 0.0519        | -               |
| 0.6122  | 150      | 0.0043        | -               |
| 0.8163  | 200      | 0.0014        | -               |
| 1.0     | 245      | -             | 0.0717          |
| 1.0204  | 250      | 0.0008        | -               |
| 1.2245  | 300      | 0.0006        | -               |
| 1.4286  | 350      | 0.0006        | -               |
| 1.6327  | 400      | 0.0003        | -               |
| 1.8367  | 450      | 0.0005        | -               |
| 2.0     | 490      | -             | 0.0693          |
| 2.0408  | 500      | 0.0005        | -               |
| 2.2449  | 550      | 0.0006        | -               |
| 2.4490  | 600      | 0.0005        | -               |
| 2.6531  | 650      | 0.0003        | -               |
| 2.8571  | 700      | 0.0003        | -               |
| 3.0     | 735      | -             | 0.0698          |
| 0.0041  | 1        | 0.0003        | -               |
| 0.2041  | 50       | 0.0006        | -               |
| 0.4082  | 100      | 0.0004        | -               |
| 0.6122  | 150      | 0.001         | -               |
| 0.8163  | 200      | 0.0002        | -               |
| 1.0     | 245      | -             | 0.0633          |
| 1.0204  | 250      | 0.0002        | -               |
| 1.2245  | 300      | 0.0           | -               |
| 1.4286  | 350      | 0.0001        | -               |
| 1.6327  | 400      | 0.0001        | -               |
| 1.8367  | 450      | 0.0001        | -               |
| 2.0     | 490      | -             | 0.0598          |
| 2.0408  | 500      | 0.0001        | -               |
| 2.2449  | 550      | 0.0001        | -               |
| 2.4490  | 600      | 0.0001        | -               |
| 2.6531  | 650      | 0.0001        | -               |
| 2.8571  | 700      | 0.0001        | -               |
| 3.0     | 735      | -             | 0.0585          |
| 3.0612  | 750      | 0.0001        | -               |
| 3.2653  | 800      | 0.0001        | -               |
| 3.4694  | 850      | 0.0001        | -               |
| 3.6735  | 900      | 0.0001        | -               |
| 3.8776  | 950      | 0.0           | -               |
| 4.0     | 980      | -             | 0.0582          |
| 4.0816  | 1000     | 0.0001        | -               |
| 4.2857  | 1050     | 0.0           | -               |
| 4.4898  | 1100     | 0.0           | -               |
| 4.6939  | 1150     | 0.0           | -               |
| 4.8980  | 1200     | 0.0           | -               |
| 5.0     | 1225     | -             | 0.0583          |
| 5.1020  | 1250     | 0.0           | -               |
| 5.3061  | 1300     | 0.0           | -               |
| 5.5102  | 1350     | 0.0           | -               |
| 5.7143  | 1400     | 0.0           | -               |
| 5.9184  | 1450     | 0.0           | -               |
| **6.0** | **1470** | **-**         | **0.0561**      |
| 0.0041  | 1        | 0.0           | -               |
| 0.2041  | 50       | 0.0           | -               |
| 0.4082  | 100      | 0.0001        | -               |
| 0.6122  | 150      | 0.0002        | -               |
| 0.8163  | 200      | 0.0002        | -               |
| 1.0     | 245      | -             | 0.0699          |
| 1.0204  | 250      | 0.0001        | -               |
| 1.2245  | 300      | 0.0001        | -               |
| 1.4286  | 350      | 0.0           | -               |
| 1.6327  | 400      | 0.0           | -               |
| 1.8367  | 450      | 0.0           | -               |
| 2.0     | 490      | -             | 0.0653          |
| 2.0408  | 500      | 0.0001        | -               |
| 2.2449  | 550      | 0.0           | -               |
| 2.4490  | 600      | 0.0           | -               |
| 2.6531  | 650      | 0.0001        | -               |
| 2.8571  | 700      | 0.0001        | -               |
| 3.0     | 735      | -             | 0.0651          |
| 3.0612  | 750      | 0.0           | -               |
| 3.2653  | 800      | 0.0           | -               |
| 3.4694  | 850      | 0.0           | -               |
| 3.6735  | 900      | 0.0           | -               |
| 3.8776  | 950      | 0.0001        | -               |
| 4.0     | 980      | -             | 0.0634          |
| 4.0816  | 1000     | 0.0           | -               |
| 4.2857  | 1050     | 0.0           | -               |
| 4.4898  | 1100     | 0.0           | -               |
| 4.6939  | 1150     | 0.0           | -               |
| 4.8980  | 1200     | 0.0           | -               |
| 5.0     | 1225     | -             | 0.0654          |
| 5.1020  | 1250     | 0.0           | -               |
| 5.3061  | 1300     | 0.0           | -               |
| 5.5102  | 1350     | 0.0           | -               |
| 5.7143  | 1400     | 0.0           | -               |
| 5.9184  | 1450     | 0.0           | -               |
| **6.0** | **1470** | **-**         | **0.0627**      |
| 6.1224  | 1500     | 0.0           | -               |
| 6.3265  | 1550     | 0.0           | -               |
| 6.5306  | 1600     | 0.0           | -               |
| 6.7347  | 1650     | 0.0           | -               |
| 6.9388  | 1700     | 0.0           | -               |
| 7.0     | 1715     | -             | 0.0648          |
| 7.1429  | 1750     | 0.0           | -               |
| 7.3469  | 1800     | 0.0           | -               |
| 7.5510  | 1850     | 0.0           | -               |
| 7.7551  | 1900     | 0.0           | -               |
| 7.9592  | 1950     | 0.0           | -               |
| 8.0     | 1960     | -             | 0.0636          |
| 8.1633  | 2000     | 0.0           | -               |
| 8.3673  | 2050     | 0.0           | -               |
| 8.5714  | 2100     | 0.0           | -               |
| 8.7755  | 2150     | 0.0           | -               |
| 8.9796  | 2200     | 0.0           | -               |
| 9.0     | 2205     | -             | 0.0648          |
| 9.1837  | 2250     | 0.0           | -               |
| 9.3878  | 2300     | 0.0           | -               |
| 9.5918  | 2350     | 0.0           | -               |
| 9.7959  | 2400     | 0.0           | -               |
| 10.0    | 2450     | 0.0           | 0.0643          |

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