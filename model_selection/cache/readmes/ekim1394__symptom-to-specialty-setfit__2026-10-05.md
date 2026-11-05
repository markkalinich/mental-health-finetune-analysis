---
tags:
- setfit
- sentence-transformers
- text-classification
- generated_from_setfit_trainer
widget:
- text: My foot has a sore that won't close, and it's been like this for weeks.
- text: I'm dealing with severe hip pain which has progressively worsened over months,
    now causing significant difficulty with ambulation.
- text: I'm struggling with knee and back discomfort related to my weight. My recent
    check-up revealed elevated blood glucose, putting me on the path to diabetes.
- text: 'I''m experiencing visual disturbances: I see spots drifting in my field of
    vision, accompanied by photopsia (flashes of light). There have also been instances
    of transient visual field loss.'
- text: I get this rattling sound in my chest and a cough, mainly when I'm trying
    to sleep. It feels like I'm suffocating.
metrics:
- accuracy
pipeline_tag: text-classification
library_name: setfit
inference: true
base_model: sentence-transformers/all-MiniLM-L6-v2
model-index:
- name: SetFit with sentence-transformers/all-MiniLM-L6-v2
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
      value: 0.8558558558558559
      name: Accuracy
---

# SetFit with sentence-transformers/all-MiniLM-L6-v2

This is a [SetFit](https://github.com/huggingface/setfit) model that can be used for Text Classification. This SetFit model uses [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) as the Sentence Transformer embedding model. A [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) instance is used for classification.

The model has been trained using an efficient few-shot learning technique that involves:

1. Fine-tuning a [Sentence Transformer](https://www.sbert.net) with contrastive learning.
2. Training a classification head with features from the fine-tuned Sentence Transformer.

## Model Details

### Model Description
- **Model Type:** SetFit
- **Sentence Transformer body:** [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- **Classification head:** a [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) instance
- **Maximum Sequence Length:** 256 tokens
- **Number of Classes:** 20 classes
<!-- - **Training Dataset:** [Unknown](https://huggingface.co/datasets/unknown) -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Repository:** [SetFit on GitHub](https://github.com/huggingface/setfit)
- **Paper:** [Efficient Few-Shot Learning Without Prompts](https://arxiv.org/abs/2209.11055)
- **Blogpost:** [SetFit: Efficient Few-Shot Learning Without Prompts](https://huggingface.co/blog/setfit)

### Model Labels
| Label                               | Examples                                                                                                                                                                                                                                                                                                                                                                |
|:------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ear Nose and Throat Otolaryngology  | <ul><li>'I experience chronic ear infections accompanied by fluid accumulation.'</li><li>'Persistent hoarseness and painful deglutition have been bothering me for months now.'</li><li>'post nasal drip causing cough'</li></ul>                                                                                                                                       |
| Wound Care                          | <ul><li>'There is a persistent wound on my foot that has not shown signs of healing for weeks.'</li><li>"The area around my surgery is red and weeping. It feels hot and I'm worried it's infected."</li><li>"There's an ulcer on my foot that's been persistent for weeks and isn't closing up."</li></ul>                                                             |
| Neonatology                         | <ul><li>"My baby isn't latching properly and is losing weight. We need help with feeding."</li><li>"Since coming home, the baby's intake is minimal, and they've lost weight."</li><li>"Our little one came early and isn't breathing well independently."</li></ul>                                                                                                    |
| Neurosurgery                        | <ul><li>'Experiencing tremors in my upper extremities and difficulty maintaining equilibrium.'</li><li>'spinal cord compression symptoms'</li><li>'pinched nerve in my neck causing arm pain'</li></ul>                                                                                                                                                                 |
| Behavioral Health                   | <ul><li>'my anxiety is out of control'</li><li>'ADHD symptoms affecting my work'</li><li>"I can't stop worrying about everything and it's affecting my sleep and work"</li></ul>                                                                                                                                                                                        |
| Pulmonology                         | <ul><li>'I have emphysema and need care'</li><li>"My partner says I snore like a freight train and sometimes they've seen me stop breathing and gasp awake during the night. It happens several times."</li><li>"I'm coughing up blood"</li></ul>                                                                                                                       |
| Heart and Vascular                  | <ul><li>"I'm having episodes where my heart beats too quickly and feels like it's skipping."</li><li>"I've noticed my heart rate speeding up and having pauses, it's quite noticeable."</li><li>'I get these sudden bursts of fast heartbeats and occasionally feel like it misses a beat.'</li></ul>                                                                   |
| Urology                             | <ul><li>'painful urination with a burning sensation'</li><li>"I'm experiencing dysuria and urinary frequency; it feels like fire when I urinate, and I'm going constantly, about every 20 minutes."</li><li>'I think I have a UTI'</li></ul>                                                                                                                            |
| Sleep Center                        | <ul><li>"I'm experiencing headaches upon waking and my partner reports apneic events during my sleep."</li><li>"I can't stay awake while driving"</li><li>'I have trouble getting to sleep at night, which results in feeling very tired and sluggish during the day.'</li></ul>                                                                                        |
| Diabetes and Endocrinology          | <ul><li>"I'm feeling really run down, always thirsty, and I'm going to the toilet way too much."</li><li>'I consistently have high blood glucose readings following meals, regardless of my efforts to eat healthily.'</li><li>"My sugar spikes after eating, and I'm confused because I thought I was eating the right things."</li></ul>                              |
| Pain Management                     | <ul><li>'epidural steroid injection needed'</li><li>'I have nerve pain that feels like electric shocks running down my arm'</li><li>'complex regional pain syndrome'</li></ul>                                                                                                                                                                                          |
| Orthopedics                         | <ul><li>'shoulder injury limiting my movement'</li><li>'carpal tunnel from typing all day'</li><li>"There's a persistent ache in my knees, and they feel locked up and make a grinding sound when I bend them."</li></ul>                                                                                                                                               |
| Gynecology                          | <ul><li>"I've been having irregular periods and hot flashes and mood swings"</li><li>"My menstrual cycle has become unpredictable, and I'm experiencing sudden episodes of intense heat, along with noticeable emotional instability."</li><li>'I suffer from pelvic discomfort that intensifies during menstruation and causes pain during sexual activity.'</li></ul> |
| Audiology                           | <ul><li>"I've got a ringing in my left ear that's always there, and it's hard to hear out of it."</li><li>'hearing loss in both ears'</li><li>"I can't understand speech in noisy places"</li></ul>                                                                                                                                                                     |
| Rheumatology Immunology and Allergy | <ul><li>'My digits become ischemic and painful in response to cold temperatures, exhibiting pallor and cyanosis.'</li><li>'I wake up with really stiff joints every morning, and it takes more than an hour for them to loosen up. They also look puffy.'</li><li>'fibromyalgia pain everywhere'</li></ul>                                                              |
| Bariatrics                          | <ul><li>'I want to learn about weight loss surgery because my BMI is over 40'</li><li>"I'm dealing with a weight problem; I'm over 300 lbs and diets just don't work for me."</li><li>'medically supervised weight loss program'</li></ul>                                                                                                                              |
| Sports Medicine                     | <ul><li>"I'm an athlete with recurring injuries"</li><li>"I'm a high school athlete with an injury"</li><li>'Running seems to trigger a pop in my knee, which then swells up.'</li></ul>                                                                                                                                                                                |
| Ophthalmology                       | <ul><li>"I'm seeing cobwebs and flashes of light, and I've had a shadow move across my vision."</li><li>'my child might need glasses'</li><li>"I'm experiencing decreased visual acuity and significant nyctalopia."</li></ul>                                                                                                                                          |
| Dermatology                         | <ul><li>"I have this itchy red rash that won't go away no matter what cream I use"</li><li>'skin lesion that changed color'</li><li>'warts that keep coming back'</li></ul>                                                                                                                                                                                             |
| Gastroenterology                    | <ul><li>'upper GI discomfort after every meal'</li><li>'I frequently experience heartburn after eating, and I sometimes have a sensation of food getting stuck in my upper chest or throat.'</li><li>'everytime i eat my stomach burns'</li></ul>                                                                                                                       |

## Evaluation

### Metrics
| Label   | Accuracy |
|:--------|:---------|
| **all** | 0.8559   |

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
model = SetFitModel.from_pretrained("setfit_model_id")
# Run inference
preds = model("My foot has a sore that won't close, and it's been like this for weeks.")
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
| Word count   | 2   | 12.3263 | 36  |

| Label                               | Training Sample Count |
|:------------------------------------|:----------------------|
| Audiology                           | 43                    |
| Bariatrics                          | 43                    |
| Behavioral Health                   | 55                    |
| Dermatology                         | 55                    |
| Diabetes and Endocrinology          | 48                    |
| Ear Nose and Throat Otolaryngology  | 48                    |
| Gastroenterology                    | 56                    |
| Gynecology                          | 48                    |
| Heart and Vascular                  | 54                    |
| Neonatology                         | 43                    |
| Neurosurgery                        | 48                    |
| Ophthalmology                       | 47                    |
| Orthopedics                         | 54                    |
| Pain Management                     | 48                    |
| Pulmonology                         | 53                    |
| Rheumatology Immunology and Allergy | 47                    |
| Sleep Center                        | 54                    |
| Sports Medicine                     | 52                    |
| Urology                             | 54                    |
| Wound Care                          | 43                    |

### Training Hyperparameters
- batch_size: (16, 16)
- num_epochs: (1, 16)
- max_steps: 2000
- sampling_strategy: oversampling
- body_learning_rate: (2e-05, 2e-05)
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
- load_best_model_at_end: True

### Training Results
| Epoch  | Step | Training Loss | Validation Loss |
|:------:|:----:|:-------------:|:---------------:|
| 0.0005 | 1    | 0.2572        | -               |
| 0.025  | 50   | 0.1971        | -               |
| 0.05   | 100  | 0.1579        | -               |
| 0.075  | 150  | 0.1329        | -               |
| 0.1    | 200  | 0.1105        | -               |
| 0.125  | 250  | 0.0974        | -               |
| 0.15   | 300  | 0.0891        | -               |
| 0.175  | 350  | 0.0871        | -               |
| 0.2    | 400  | 0.0723        | -               |
| 0.225  | 450  | 0.0609        | -               |
| 0.25   | 500  | 0.0706        | 0.0670          |
| 0.275  | 550  | 0.0588        | -               |
| 0.3    | 600  | 0.0559        | -               |
| 0.325  | 650  | 0.0513        | -               |
| 0.35   | 700  | 0.0499        | -               |
| 0.375  | 750  | 0.0462        | -               |
| 0.4    | 800  | 0.0476        | -               |
| 0.425  | 850  | 0.0461        | -               |
| 0.45   | 900  | 0.0432        | -               |
| 0.475  | 950  | 0.0411        | -               |
| 0.5    | 1000 | 0.0386        | 0.0538          |
| 0.525  | 1050 | 0.0364        | -               |
| 0.55   | 1100 | 0.0386        | -               |
| 0.575  | 1150 | 0.036         | -               |
| 0.6    | 1200 | 0.0335        | -               |
| 0.625  | 1250 | 0.0342        | -               |
| 0.65   | 1300 | 0.0375        | -               |
| 0.675  | 1350 | 0.0368        | -               |
| 0.7    | 1400 | 0.0297        | -               |
| 0.725  | 1450 | 0.0313        | -               |
| 0.75   | 1500 | 0.0274        | 0.0510          |
| 0.775  | 1550 | 0.0271        | -               |
| 0.8    | 1600 | 0.0255        | -               |
| 0.825  | 1650 | 0.0287        | -               |
| 0.85   | 1700 | 0.0262        | -               |
| 0.875  | 1750 | 0.0277        | -               |
| 0.9    | 1800 | 0.0207        | -               |
| 0.925  | 1850 | 0.0253        | -               |
| 0.95   | 1900 | 0.024         | -               |
| 0.975  | 1950 | 0.0256        | -               |
| 1.0    | 2000 | 0.0233        | 0.0500          |

### Framework Versions
- Python: 3.11.12
- SetFit: 1.1.3
- Sentence Transformers: 5.2.0
- Transformers: 4.57.5
- PyTorch: 2.9.1+cu128
- Datasets: 4.5.0
- Tokenizers: 0.22.2

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