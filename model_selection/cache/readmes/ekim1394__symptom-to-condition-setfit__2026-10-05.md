---
tags:
- setfit
- sentence-transformers
- text-classification
- generated_from_setfit_trainer
widget:
- text: can't keep my legs still in bed
- text: Eating dairy seems to make my stomach hurt and give me diarrhea.
- text: arrhythmia causing palpitations
- text: My skin is really itchy and has these thick, red, flaky spots, especially
    on my scalp.
- text: I have gastroesophageal reflux disease symptoms
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
      value: 0.45454545454545453
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
- **Number of Classes:** 66 classes
<!-- - **Training Dataset:** [Unknown](https://huggingface.co/datasets/unknown) -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Repository:** [SetFit on GitHub](https://github.com/huggingface/setfit)
- **Paper:** [Efficient Few-Shot Learning Without Prompts](https://arxiv.org/abs/2209.11055)
- **Blogpost:** [SetFit: Efficient Few-Shot Learning Without Prompts](https://huggingface.co/blog/setfit)

### Model Labels
| Label                     | Examples                                                                                                                                                                                                                                                                                            |
|:--------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Colon Polyps              | <ul><li>'polyps found during colonoscopy'</li><li>'growths in my colon'</li><li>'precancerous polyps in colon'</li></ul>                                                                                                                                                                            |
| Kidney Stones             | <ul><li>"I've got this nagging pain in my flank that feels like pressure, and I'm nauseous."</li><li>'passing a kidney stone is excruciating'</li><li>'I feel like I have a constant ache in my kidney area, and it gets worse when I drink water.'</li></ul>                                       |
| Insomnia                  | <ul><li>"I feel exhausted even after a full night in bed because I just didn't sleep well."</li><li>"I'm having trouble sleeping since I started that new medication."</li><li>'My sleep is so light, I wake up at every little noise.'</li></ul>                                                   |
| High Blood Pressure       | <ul><li>'hypertension that needs treatment'</li><li>'I have hypertension'</li><li>'my blood pressure is elevated'</li></ul>                                                                                                                                                                         |
| Sleep Apnea               | <ul><li>"I've noticed I need to pee a lot more often during the night lately."</li><li>'snoring and gasping at night'</li><li>'My partner says I have really loud snoring and sometimes stop breathing while I sleep.'</li></ul>                                                                    |
| Depression                | <ul><li>"I'm constantly irritable and snap at people easily."</li><li>"I've noticed I'm eating a lot more than usual."</li><li>'Everything feels overwhelming lately, even small tasks.'</li></ul>                                                                                                  |
| Carpal Tunnel             | <ul><li>'median nerve compression'</li><li>'numbness and tingling in my hands'</li><li>'wrist pain and hand weakness'</li></ul>                                                                                                                                                                     |
| Celiac Disease            | <ul><li>'I react badly to gluten'</li><li>'gluten intolerance causing diarrhea'</li><li>'digestive problems after eating wheat'</li></ul>                                                                                                                                                           |
| OCD                       | <ul><li>'OCD rituals that I must perform'</li><li>'compulsive behaviors taking over my life'</li><li>"obsessive thoughts I can't stop"</li></ul>                                                                                                                                                    |
| Acne                      | <ul><li>'acne vulgaris treatment needed'</li><li>"severe acne that won't clear"</li><li>'adult acne that keeps coming back'</li></ul>                                                                                                                                                               |
| GERD                      | <ul><li>'persistent heartburn multiple times a week'</li><li>'I get heartburn that radiates up to my neck and jaw.'</li><li>"chronic acid reflux that won't go away"</li></ul>                                                                                                                      |
| Overactive Bladder        | <ul><li>"sudden urge to urinate I can't control"</li><li>'frequent bathroom trips day and night'</li><li>"can't hold my bladder"</li></ul>                                                                                                                                                          |
| Ulcerative Colitis        | <ul><li>'Intense urgency to have a bowel movement, sometimes waking me up at night.'</li><li>'Constant feeling of needing to poop, even right after going.'</li><li>"Feeling like my bowels aren't emptying completely."</li></ul>                                                                  |
| Heart Disease             | <ul><li>"My chest feels tight and heavy, like an elephant is sitting on it, particularly when I'm stressed."</li><li>'cardiac issues from blocked arteries'</li><li>"My heart feels like it's racing or skipping beats, especially after I eat a big meal."</li></ul>                               |
| Coronary Artery Disease   | <ul><li>'blocked arteries in my heart'</li><li>'atherosclerosis in my heart arteries'</li><li>'reduced blood flow to my heart'</li></ul>                                                                                                                                                            |
| Arrhythmia                | <ul><li>'irregular heartbeat that I can feel'</li><li>'my heart beats irregularly'</li><li>'I get these sudden rushes of my heart beating really fast.'</li></ul>                                                                                                                                   |
| Eczema                    | <ul><li>'My skin feels intensely itchy, especially at night, making it hard to sleep.'</li><li>'My skin is really red and bumpy, especially on my elbows and knees.'</li><li>"My hands get so dry they crack open, and it's incredibly itchy."</li></ul>                                            |
| Rheumatoid Arthritis      | <ul><li>'rheumatoid arthritis in my hands'</li><li>'RA causing joint swelling'</li><li>'autoimmune arthritis'</li></ul>                                                                                                                                                                             |
| Skin Cancer               | <ul><li>'basal cell or squamous cell carcinoma'</li><li>'skin lesion that changed colors'</li><li>"spot that won't heal might be cancer"</li></ul>                                                                                                                                                  |
| Atrial Fibrillation       | <ul><li>'my heart quivers instead of beating normally'</li><li>'AFib episodes'</li></ul>                                                                                                                                                                                                            |
| Anxiety                   | <ul><li>"constant worry that I can't control"</li><li>"I'm so worried about my health that I constantly check my body for problems."</li><li>'anxiety affecting my daily life'</li></ul>                                                                                                            |
| Panic Disorder            | <ul><li>'recurring panic attacks'</li><li>'fear of having another panic attack'</li><li>'panic episodes with chest tightness'</li></ul>                                                                                                                                                             |
| Prostate Cancer           | <ul><li>'prostate cancer diagnosis'</li><li>'prostate cancer treatment needed'</li><li>'elevated PSA concerning for cancer'</li></ul>                                                                                                                                                               |
| Herniated Disc            | <ul><li>'bulging disc on MRI'</li><li>'disc bulging in my spine'</li><li>'disc pressing on nerves'</li></ul>                                                                                                                                                                                        |
| Heart Attack              | <ul><li>'myocardial infarction symptoms'</li><li>'heart attack warning signs'</li><li>"I think I'm having a heart attack"</li></ul>                                                                                                                                                                 |
| Sciatica                  | <ul><li>'sciatic nerve pain'</li><li>'radiating leg pain from back'</li><li>'sciatica from disc herniation'</li></ul>                                                                                                                                                                               |
| Restless Leg Syndrome     | <ul><li>'uncomfortable urge to move my legs at night'</li><li>"It feels like there's an electric current running through my legs, and moving them helps, but only for a little while."</li><li>"I wake up several times a night because my legs feel so uncomfortable I can't ignore it."</li></ul> |
| Psoriasis                 | <ul><li>"I've got these weird, raised, red patches that feel rough, and they're starting to crack and bleed."</li><li>'autoimmune skin condition'</li><li>'scaly red patches on my elbows and knees'</li></ul>                                                                                      |
| Cataracts                 | <ul><li>'vision getting foggy'</li><li>'cataracts making it hard to see'</li><li>'need cataract surgery'</li></ul>                                                                                                                                                                                  |
| Heartburn                 | <ul><li>'burning sensation in my chest after eating'</li><li>"I have a sour taste in the back of my mouth that lingers for a while, often when I'm stressed."</li><li>'Waking up in the middle of the night coughing because of a burning feeling in my chest.'</li></ul>                           |
| Acid Reflux               | <ul><li>'sour taste and burning in my throat'</li><li>"I keep having to clear my throat because it feels like there's liquid or acid there."</li><li>'I get a sour or bitter taste in the back of my mouth, often when I lie down.'</li></ul>                                                       |
| Tinnitus                  | <ul><li>'ringing in my ears constantly'</li><li>'constant noise in my ears'</li><li>'ear ringing driving me crazy'</li></ul>                                                                                                                                                                        |
| Crohn's Disease           | <ul><li>"Crohn's flare with weight loss"</li><li>"I've lost a lot of weight without trying, and I feel exhausted all the time."</li><li>'I have this constant cramping feeling in my gut, and I feel like I need to go to the bathroom all the time, but nothing comes out.'</li></ul>              |
| IBS                       | <ul><li>"My poop is often hard to pass, and I feel like I haven't completely emptied my bowels."</li><li>'abdominal pain relieved by bowel movements'</li><li>'alternating diarrhea and constipation'</li></ul>                                                                                     |
| Prostate Problems         | <ul><li>'prostate issues as I get older'</li><li>'benign prostatic hyperplasia'</li><li>'BPH symptoms with weak stream'</li></ul>                                                                                                                                                                   |
| Osteoarthritis            | <ul><li>'degenerative joint disease'</li><li>'bone on bone in my hip'</li><li>'cartilage loss in my joints'</li></ul>                                                                                                                                                                               |
| Incontinence              | <ul><li>"can't hold my urine"</li><li>'stress incontinence when I exercise'</li><li>'leaking urine when I cough or sneeze'</li></ul>                                                                                                                                                                |
| Liver Disease             | <ul><li>'cirrhosis symptoms'</li><li>'My skin is really itchy, especially on my arms and legs, and there are no rashes.'</li><li>'I feel so weak and tired all the time, like I have no energy left.'</li></ul>                                                                                     |
| Pancreatitis              | <ul><li>'acute pancreatic pain'</li><li>'severe upper abdominal pain radiating to my back'</li><li>'pancreas inflammation symptoms'</li></ul>                                                                                                                                                       |
| Gallstones                | <ul><li>'gallbladder attacks after meals'</li><li>"I have a constant, nagging pain in my upper abdomen that doesn't really go away."</li><li>'Pain that radiates to my back or right shoulder blade.'</li></ul>                                                                                     |
| Heart Failure             | <ul><li>'Dizziness or lightheadedness'</li><li>'Persistent cough or wheezing, with white or pink blood-tinged phlegm'</li><li>'CHF with swelling and shortness of breath'</li></ul>                                                                                                                 |
| Asthma                    | <ul><li>'reactive airways with coughing'</li><li>'bronchospasm and tight chest'</li><li>'wheezing and trouble breathing'</li></ul>                                                                                                                                                                  |
| Snoring                   | <ul><li>'chronic snoring problem'</li><li>'snoring that wakes me up'</li><li>'excessive snoring'</li></ul>                                                                                                                                                                                          |
| Sinusitis                 | <ul><li>'chronic sinusitis'</li><li>'pressure and pain in my sinuses'</li><li>'sinus infection with facial pain'</li></ul>                                                                                                                                                                          |
| Urinary Tract Infection   | <ul><li>'I have a really strong urge to pee all the time, but when I go, not much comes out.'</li><li>'I have a constant ache in my lower abdomen that gets worse when I pee, and I feel generally unwell.'</li><li>'UTI symptoms'</li></ul>                                                        |
| Melanoma                  | <ul><li>'melanoma concern from changing mole'</li><li>"mole that's getting bigger and darker"</li><li>'asymmetric mole with irregular borders'</li></ul>                                                                                                                                            |
| Thyroid Disorders         | <ul><li>'thyroid is overactive or underactive'</li><li>'hyperthyroidism with weight loss'</li><li>'hypothyroidism symptoms'</li></ul>                                                                                                                                                               |
| Hearing Loss              | <ul><li>'sensorineural hearing loss'</li><li>'trouble hearing conversations'</li><li>'gradual hearing loss'</li></ul>                                                                                                                                                                               |
| Pneumonia                 | <ul><li>'coughing up colored phlegm with fever'</li><li>'lung infection with fever and cough'</li><li>'bacterial or viral lung infection'</li></ul>                                                                                                                                                 |
| Narcolepsy                | <ul><li>"sleep attacks that I can't control"</li><li>'sudden sleep episodes'</li><li>'narcolepsy with cataplexy'</li></ul>                                                                                                                                                                          |
| Macular Degeneration      | <ul><li>'AMD affecting my central vision'</li><li>'macular degeneration'</li><li>'wet or dry macular degeneration'</li></ul>                                                                                                                                                                        |
| Hepatitis                 | <ul><li>'jaundice and fatigue from hepatitis'</li><li>'viral hepatitis symptoms'</li><li>'liver inflammation from virus'</li></ul>                                                                                                                                                                  |
| Lupus                     | <ul><li>'systemic lupus erythematosus'</li><li>'lupus flare symptoms'</li><li>'butterfly rash and joint pain'</li></ul>                                                                                                                                                                             |
| Glaucoma                  | <ul><li>'optic nerve damage from pressure'</li><li>'glaucoma affecting my vision'</li><li>'high eye pressure'</li></ul>                                                                                                                                                                             |
| ADHD                      | <ul><li>'ADHD affecting my productivity'</li><li>'trouble concentrating at work'</li><li>"can't focus or pay attention"</li></ul>                                                                                                                                                                   |
| Diabetes                  | <ul><li>'diabetic and need help with A1C'</li><li>'type 2 diabetes diagnosis'</li><li>'diabetes needing management'</li></ul>                                                                                                                                                                       |
| Arthritis                 | <ul><li>'chronic joint pain from arthritis'</li><li>'arthritis in multiple joints'</li><li>'inflammation in my joints'</li></ul>                                                                                                                                                                    |
| Tonsillitis               | <ul><li>'swollen painful tonsils'</li><li>'tonsils need to be removed'</li><li>'recurring tonsil infections'</li></ul>                                                                                                                                                                              |
| Dry Eye                   | <ul><li>'dry eyes from screen time'</li><li>'eyes burn and feel sandy'</li><li>'not enough tears'</li></ul>                                                                                                                                                                                         |
| Fibromyalgia              | <ul><li>'pain all over my body'</li><li>'chronic pain syndrome'</li><li>'widespread pain and fatigue'</li></ul>                                                                                                                                                                                     |
| Back Pain                 | <ul><li>'lumbar pain that radiates'</li><li>'back problems for years'</li><li>'severe back pain limiting movement'</li></ul>                                                                                                                                                                        |
| PTSD                      | <ul><li>'hypervigilance and avoiding triggers'</li><li>'traumatic memories affecting my life'</li><li>'post traumatic stress from an event'</li></ul>                                                                                                                                               |
| COPD                      | <ul><li>'progressive lung disease'</li><li>'shortness of breath from COPD'</li><li>'emphysema and chronic bronchitis'</li></ul>                                                                                                                                                                     |
| Lung Cancer               | <ul><li>'lung cancer found on CT scan'</li><li>'lung mass suspicious for cancer'</li><li>'lung cancer causing cough'</li></ul>                                                                                                                                                                      |
| Peripheral Artery Disease | <ul><li>'PAD causing leg pain when walking'</li><li>'blocked arteries in my legs'</li><li>'poor circulation in my legs'</li></ul>                                                                                                                                                                   |
| Fractures                 | <ul><li>'broken arm or leg'</li><li>'I broke a bone'</li><li>'fractured bone that needs treatment'</li></ul>                                                                                                                                                                                        |

## Evaluation

### Metrics
| Label   | Accuracy |
|:--------|:---------|
| **all** | 0.4545   |

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
preds = model("can't keep my legs still in bed")
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
| Word count   | 2   | 8.0121 | 27  |

| Label                     | Training Sample Count |
|:--------------------------|:----------------------|
| ADHD                      | 4                     |
| Acid Reflux               | 13                    |
| Acne                      | 5                     |
| Anxiety                   | 13                    |
| Arrhythmia                | 12                    |
| Arthritis                 | 4                     |
| Asthma                    | 5                     |
| Atrial Fibrillation       | 2                     |
| Back Pain                 | 4                     |
| COPD                      | 4                     |
| Carpal Tunnel             | 5                     |
| Cataracts                 | 4                     |
| Celiac Disease            | 5                     |
| Colon Polyps              | 5                     |
| Coronary Artery Disease   | 5                     |
| Crohn's Disease           | 14                    |
| Depression                | 12                    |
| Diabetes                  | 5                     |
| Dry Eye                   | 5                     |
| Eczema                    | 13                    |
| Fibromyalgia              | 5                     |
| Fractures                 | 4                     |
| GERD                      | 14                    |
| Gallstones                | 13                    |
| Glaucoma                  | 4                     |
| Hearing Loss              | 5                     |
| Heart Attack              | 5                     |
| Heart Disease             | 14                    |
| Heart Failure             | 12                    |
| Heartburn                 | 14                    |
| Hepatitis                 | 5                     |
| Herniated Disc            | 5                     |
| High Blood Pressure       | 5                     |
| IBS                       | 13                    |
| Incontinence              | 5                     |
| Insomnia                  | 14                    |
| Kidney Stones             | 14                    |
| Liver Disease             | 16                    |
| Lung Cancer               | 5                     |
| Lupus                     | 4                     |
| Macular Degeneration      | 5                     |
| Melanoma                  | 5                     |
| Narcolepsy                | 5                     |
| OCD                       | 5                     |
| Osteoarthritis            | 4                     |
| Overactive Bladder        | 16                    |
| PTSD                      | 3                     |
| Pancreatitis              | 5                     |
| Panic Disorder            | 5                     |
| Peripheral Artery Disease | 5                     |
| Pneumonia                 | 5                     |
| Prostate Cancer           | 5                     |
| Prostate Problems         | 5                     |
| Psoriasis                 | 12                    |
| Restless Leg Syndrome     | 13                    |
| Rheumatoid Arthritis      | 5                     |
| Sciatica                  | 5                     |
| Sinusitis                 | 5                     |
| Skin Cancer               | 5                     |
| Sleep Apnea               | 16                    |
| Snoring                   | 5                     |
| Thyroid Disorders         | 5                     |
| Tinnitus                  | 4                     |
| Tonsillitis               | 5                     |
| Ulcerative Colitis        | 13                    |
| Urinary Tract Infection   | 13                    |

### Training Hyperparameters
- batch_size: (16, 16)
- num_epochs: (3, 3)
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
- evaluation_strategy: epoch
- eval_max_steps: -1
- load_best_model_at_end: True

### Training Results
| Epoch  | Step  | Training Loss | Validation Loss |
|:------:|:-----:|:-------------:|:---------------:|
| 0.0001 | 1     | 0.2819        | -               |
| 0.0033 | 50    | 0.168         | -               |
| 0.0067 | 100   | 0.1547        | -               |
| 0.0100 | 150   | 0.1629        | -               |
| 0.0134 | 200   | 0.1558        | -               |
| 0.0167 | 250   | 0.1477        | -               |
| 0.0201 | 300   | 0.1397        | -               |
| 0.0234 | 350   | 0.1383        | -               |
| 0.0268 | 400   | 0.1418        | -               |
| 0.0301 | 450   | 0.1298        | -               |
| 0.0334 | 500   | 0.1337        | -               |
| 0.0368 | 550   | 0.1282        | -               |
| 0.0401 | 600   | 0.1246        | -               |
| 0.0435 | 650   | 0.1215        | -               |
| 0.0468 | 700   | 0.1182        | -               |
| 0.0502 | 750   | 0.1114        | -               |
| 0.0535 | 800   | 0.1079        | -               |
| 0.0569 | 850   | 0.1024        | -               |
| 0.0602 | 900   | 0.0993        | -               |
| 0.0636 | 950   | 0.1011        | -               |
| 0.0669 | 1000  | 0.1001        | -               |
| 0.0702 | 1050  | 0.092         | -               |
| 0.0736 | 1100  | 0.096         | -               |
| 0.0769 | 1150  | 0.0923        | -               |
| 0.0803 | 1200  | 0.0847        | -               |
| 0.0836 | 1250  | 0.0878        | -               |
| 0.0870 | 1300  | 0.0873        | -               |
| 0.0903 | 1350  | 0.0789        | -               |
| 0.0937 | 1400  | 0.0756        | -               |
| 0.0970 | 1450  | 0.0735        | -               |
| 0.1003 | 1500  | 0.0744        | -               |
| 0.1037 | 1550  | 0.0713        | -               |
| 0.1070 | 1600  | 0.0717        | -               |
| 0.1104 | 1650  | 0.0606        | -               |
| 0.1137 | 1700  | 0.0581        | -               |
| 0.1171 | 1750  | 0.0615        | -               |
| 0.1204 | 1800  | 0.0641        | -               |
| 0.1238 | 1850  | 0.0609        | -               |
| 0.1271 | 1900  | 0.0603        | -               |
| 0.1305 | 1950  | 0.0616        | -               |
| 0.1338 | 2000  | 0.0488        | -               |
| 0.1371 | 2050  | 0.0497        | -               |
| 0.1405 | 2100  | 0.0559        | -               |
| 0.1438 | 2150  | 0.0482        | -               |
| 0.1472 | 2200  | 0.0508        | -               |
| 0.1505 | 2250  | 0.0511        | -               |
| 0.1539 | 2300  | 0.0446        | -               |
| 0.1572 | 2350  | 0.0429        | -               |
| 0.1606 | 2400  | 0.0421        | -               |
| 0.1639 | 2450  | 0.0375        | -               |
| 0.1672 | 2500  | 0.0423        | -               |
| 0.1706 | 2550  | 0.0398        | -               |
| 0.1739 | 2600  | 0.0511        | -               |
| 0.1773 | 2650  | 0.0427        | -               |
| 0.1806 | 2700  | 0.0373        | -               |
| 0.1840 | 2750  | 0.0355        | -               |
| 0.1873 | 2800  | 0.0312        | -               |
| 0.1907 | 2850  | 0.0333        | -               |
| 0.1940 | 2900  | 0.0384        | -               |
| 0.1974 | 2950  | 0.038         | -               |
| 0.2007 | 3000  | 0.029         | -               |
| 0.2040 | 3050  | 0.0306        | -               |
| 0.2074 | 3100  | 0.0329        | -               |
| 0.2107 | 3150  | 0.0287        | -               |
| 0.2141 | 3200  | 0.0309        | -               |
| 0.2174 | 3250  | 0.0303        | -               |
| 0.2208 | 3300  | 0.0281        | -               |
| 0.2241 | 3350  | 0.0248        | -               |
| 0.2275 | 3400  | 0.0275        | -               |
| 0.2308 | 3450  | 0.0253        | -               |
| 0.2341 | 3500  | 0.0219        | -               |
| 0.2375 | 3550  | 0.0247        | -               |
| 0.2408 | 3600  | 0.0216        | -               |
| 0.2442 | 3650  | 0.0249        | -               |
| 0.2475 | 3700  | 0.0278        | -               |
| 0.2509 | 3750  | 0.0293        | -               |
| 0.2542 | 3800  | 0.028         | -               |
| 0.2576 | 3850  | 0.0223        | -               |
| 0.2609 | 3900  | 0.0265        | -               |
| 0.2642 | 3950  | 0.0171        | -               |
| 0.2676 | 4000  | 0.023         | -               |
| 0.2709 | 4050  | 0.0182        | -               |
| 0.2743 | 4100  | 0.0232        | -               |
| 0.2776 | 4150  | 0.0187        | -               |
| 0.2810 | 4200  | 0.0239        | -               |
| 0.2843 | 4250  | 0.0192        | -               |
| 0.2877 | 4300  | 0.0166        | -               |
| 0.2910 | 4350  | 0.0225        | -               |
| 0.2944 | 4400  | 0.0207        | -               |
| 0.2977 | 4450  | 0.0146        | -               |
| 0.3010 | 4500  | 0.0173        | -               |
| 0.3044 | 4550  | 0.0176        | -               |
| 0.3077 | 4600  | 0.0137        | -               |
| 0.3111 | 4650  | 0.0164        | -               |
| 0.3144 | 4700  | 0.0175        | -               |
| 0.3178 | 4750  | 0.0196        | -               |
| 0.3211 | 4800  | 0.0191        | -               |
| 0.3245 | 4850  | 0.0167        | -               |
| 0.3278 | 4900  | 0.0113        | -               |
| 0.3311 | 4950  | 0.0168        | -               |
| 0.3345 | 5000  | 0.0249        | -               |
| 0.3378 | 5050  | 0.0137        | -               |
| 0.3412 | 5100  | 0.0135        | -               |
| 0.3445 | 5150  | 0.0158        | -               |
| 0.3479 | 5200  | 0.017         | -               |
| 0.3512 | 5250  | 0.0182        | -               |
| 0.3546 | 5300  | 0.0119        | -               |
| 0.3579 | 5350  | 0.0218        | -               |
| 0.3613 | 5400  | 0.0168        | -               |
| 0.3646 | 5450  | 0.018         | -               |
| 0.3679 | 5500  | 0.0106        | -               |
| 0.3713 | 5550  | 0.0143        | -               |
| 0.3746 | 5600  | 0.0175        | -               |
| 0.3780 | 5650  | 0.0121        | -               |
| 0.3813 | 5700  | 0.0113        | -               |
| 0.3847 | 5750  | 0.0104        | -               |
| 0.3880 | 5800  | 0.0156        | -               |
| 0.3914 | 5850  | 0.0182        | -               |
| 0.3947 | 5900  | 0.0089        | -               |
| 0.3980 | 5950  | 0.0179        | -               |
| 0.4014 | 6000  | 0.0142        | -               |
| 0.4047 | 6050  | 0.0116        | -               |
| 0.4081 | 6100  | 0.017         | -               |
| 0.4114 | 6150  | 0.011         | -               |
| 0.4148 | 6200  | 0.0164        | -               |
| 0.4181 | 6250  | 0.0147        | -               |
| 0.4215 | 6300  | 0.0155        | -               |
| 0.4248 | 6350  | 0.0084        | -               |
| 0.4282 | 6400  | 0.0109        | -               |
| 0.4315 | 6450  | 0.0173        | -               |
| 0.4348 | 6500  | 0.0147        | -               |
| 0.4382 | 6550  | 0.0153        | -               |
| 0.4415 | 6600  | 0.0085        | -               |
| 0.4449 | 6650  | 0.0188        | -               |
| 0.4482 | 6700  | 0.0094        | -               |
| 0.4516 | 6750  | 0.016         | -               |
| 0.4549 | 6800  | 0.0129        | -               |
| 0.4583 | 6850  | 0.0228        | -               |
| 0.4616 | 6900  | 0.0159        | -               |
| 0.4649 | 6950  | 0.0199        | -               |
| 0.4683 | 7000  | 0.0096        | -               |
| 0.4716 | 7050  | 0.0188        | -               |
| 0.4750 | 7100  | 0.0157        | -               |
| 0.4783 | 7150  | 0.0103        | -               |
| 0.4817 | 7200  | 0.0123        | -               |
| 0.4850 | 7250  | 0.0131        | -               |
| 0.4884 | 7300  | 0.0136        | -               |
| 0.4917 | 7350  | 0.0096        | -               |
| 0.4950 | 7400  | 0.0089        | -               |
| 0.4984 | 7450  | 0.0144        | -               |
| 0.5017 | 7500  | 0.0109        | -               |
| 0.5051 | 7550  | 0.0085        | -               |
| 0.5084 | 7600  | 0.0075        | -               |
| 0.5118 | 7650  | 0.0109        | -               |
| 0.5151 | 7700  | 0.0103        | -               |
| 0.5185 | 7750  | 0.0074        | -               |
| 0.5218 | 7800  | 0.0081        | -               |
| 0.5252 | 7850  | 0.0132        | -               |
| 0.5285 | 7900  | 0.0117        | -               |
| 0.5318 | 7950  | 0.0141        | -               |
| 0.5352 | 8000  | 0.0079        | -               |
| 0.5385 | 8050  | 0.0082        | -               |
| 0.5419 | 8100  | 0.0078        | -               |
| 0.5452 | 8150  | 0.0121        | -               |
| 0.5486 | 8200  | 0.0177        | -               |
| 0.5519 | 8250  | 0.0109        | -               |
| 0.5553 | 8300  | 0.0095        | -               |
| 0.5586 | 8350  | 0.0125        | -               |
| 0.5619 | 8400  | 0.008         | -               |
| 0.5653 | 8450  | 0.0088        | -               |
| 0.5686 | 8500  | 0.0112        | -               |
| 0.5720 | 8550  | 0.0101        | -               |
| 0.5753 | 8600  | 0.0142        | -               |
| 0.5787 | 8650  | 0.011         | -               |
| 0.5820 | 8700  | 0.0084        | -               |
| 0.5854 | 8750  | 0.0068        | -               |
| 0.5887 | 8800  | 0.0069        | -               |
| 0.5921 | 8850  | 0.0095        | -               |
| 0.5954 | 8900  | 0.01          | -               |
| 0.5987 | 8950  | 0.007         | -               |
| 0.6021 | 9000  | 0.0098        | -               |
| 0.6054 | 9050  | 0.0086        | -               |
| 0.6088 | 9100  | 0.0074        | -               |
| 0.6121 | 9150  | 0.0085        | -               |
| 0.6155 | 9200  | 0.0078        | -               |
| 0.6188 | 9250  | 0.0085        | -               |
| 0.6222 | 9300  | 0.013         | -               |
| 0.6255 | 9350  | 0.0063        | -               |
| 0.6288 | 9400  | 0.0114        | -               |
| 0.6322 | 9450  | 0.0053        | -               |
| 0.6355 | 9500  | 0.0052        | -               |
| 0.6389 | 9550  | 0.008         | -               |
| 0.6422 | 9600  | 0.0063        | -               |
| 0.6456 | 9650  | 0.0085        | -               |
| 0.6489 | 9700  | 0.0153        | -               |
| 0.6523 | 9750  | 0.0074        | -               |
| 0.6556 | 9800  | 0.0075        | -               |
| 0.6590 | 9850  | 0.007         | -               |
| 0.6623 | 9900  | 0.0059        | -               |
| 0.6656 | 9950  | 0.0036        | -               |
| 0.6690 | 10000 | 0.0064        | -               |
| 0.6723 | 10050 | 0.008         | -               |
| 0.6757 | 10100 | 0.0093        | -               |
| 0.6790 | 10150 | 0.0049        | -               |
| 0.6824 | 10200 | 0.0086        | -               |
| 0.6857 | 10250 | 0.0037        | -               |
| 0.6891 | 10300 | 0.0108        | -               |
| 0.6924 | 10350 | 0.0088        | -               |
| 0.6957 | 10400 | 0.0074        | -               |
| 0.6991 | 10450 | 0.0036        | -               |
| 0.7024 | 10500 | 0.0044        | -               |
| 0.7058 | 10550 | 0.0051        | -               |
| 0.7091 | 10600 | 0.0063        | -               |
| 0.7125 | 10650 | 0.0057        | -               |
| 0.7158 | 10700 | 0.0032        | -               |
| 0.7192 | 10750 | 0.0046        | -               |
| 0.7225 | 10800 | 0.0072        | -               |
| 0.7258 | 10850 | 0.0029        | -               |
| 0.7292 | 10900 | 0.0051        | -               |
| 0.7325 | 10950 | 0.0037        | -               |
| 0.7359 | 11000 | 0.0072        | -               |
| 0.7392 | 11050 | 0.0054        | -               |
| 0.7426 | 11100 | 0.0024        | -               |
| 0.7459 | 11150 | 0.0049        | -               |
| 0.7493 | 11200 | 0.0054        | -               |
| 0.7526 | 11250 | 0.0044        | -               |
| 0.7560 | 11300 | 0.005         | -               |
| 0.7593 | 11350 | 0.0037        | -               |
| 0.7626 | 11400 | 0.0029        | -               |
| 0.7660 | 11450 | 0.0029        | -               |
| 0.7693 | 11500 | 0.0035        | -               |
| 0.7727 | 11550 | 0.0054        | -               |
| 0.7760 | 11600 | 0.0052        | -               |
| 0.7794 | 11650 | 0.0039        | -               |
| 0.7827 | 11700 | 0.0042        | -               |
| 0.7861 | 11750 | 0.0038        | -               |
| 0.7894 | 11800 | 0.0066        | -               |
| 0.7927 | 11850 | 0.0048        | -               |
| 0.7961 | 11900 | 0.0047        | -               |
| 0.7994 | 11950 | 0.0057        | -               |
| 0.8028 | 12000 | 0.0049        | -               |
| 0.8061 | 12050 | 0.0043        | -               |
| 0.8095 | 12100 | 0.0062        | -               |
| 0.8128 | 12150 | 0.0078        | -               |
| 0.8162 | 12200 | 0.0032        | -               |
| 0.8195 | 12250 | 0.0051        | -               |
| 0.8229 | 12300 | 0.005         | -               |
| 0.8262 | 12350 | 0.0023        | -               |
| 0.8295 | 12400 | 0.0071        | -               |
| 0.8329 | 12450 | 0.0049        | -               |
| 0.8362 | 12500 | 0.0051        | -               |
| 0.8396 | 12550 | 0.0103        | -               |
| 0.8429 | 12600 | 0.0051        | -               |
| 0.8463 | 12650 | 0.0073        | -               |
| 0.8496 | 12700 | 0.0065        | -               |
| 0.8530 | 12750 | 0.0058        | -               |
| 0.8563 | 12800 | 0.0036        | -               |
| 0.8596 | 12850 | 0.0048        | -               |
| 0.8630 | 12900 | 0.0022        | -               |
| 0.8663 | 12950 | 0.0024        | -               |
| 0.8697 | 13000 | 0.0021        | -               |
| 0.8730 | 13050 | 0.0024        | -               |
| 0.8764 | 13100 | 0.0033        | -               |
| 0.8797 | 13150 | 0.0032        | -               |
| 0.8831 | 13200 | 0.0029        | -               |
| 0.8864 | 13250 | 0.0025        | -               |
| 0.8898 | 13300 | 0.0025        | -               |
| 0.8931 | 13350 | 0.0057        | -               |
| 0.8964 | 13400 | 0.0086        | -               |
| 0.8998 | 13450 | 0.0022        | -               |
| 0.9031 | 13500 | 0.0035        | -               |
| 0.9065 | 13550 | 0.0027        | -               |
| 0.9098 | 13600 | 0.0033        | -               |
| 0.9132 | 13650 | 0.0021        | -               |
| 0.9165 | 13700 | 0.0036        | -               |
| 0.9199 | 13750 | 0.0024        | -               |
| 0.9232 | 13800 | 0.0035        | -               |
| 0.9265 | 13850 | 0.0022        | -               |
| 0.9299 | 13900 | 0.0022        | -               |
| 0.9332 | 13950 | 0.0012        | -               |
| 0.9366 | 14000 | 0.002         | -               |
| 0.9399 | 14050 | 0.0027        | -               |
| 0.9433 | 14100 | 0.003         | -               |
| 0.9466 | 14150 | 0.0034        | -               |
| 0.9500 | 14200 | 0.0032        | -               |
| 0.9533 | 14250 | 0.0039        | -               |
| 0.9566 | 14300 | 0.0055        | -               |
| 0.9600 | 14350 | 0.0036        | -               |
| 0.9633 | 14400 | 0.0015        | -               |
| 0.9667 | 14450 | 0.004         | -               |
| 0.9700 | 14500 | 0.0054        | -               |
| 0.9734 | 14550 | 0.0044        | -               |
| 0.9767 | 14600 | 0.0018        | -               |
| 0.9801 | 14650 | 0.0096        | -               |
| 0.9834 | 14700 | 0.0035        | -               |
| 0.9868 | 14750 | 0.0034        | -               |
| 0.9901 | 14800 | 0.0021        | -               |
| 0.9934 | 14850 | 0.0025        | -               |
| 0.9968 | 14900 | 0.0043        | -               |
| 1.0    | 14948 | -             | 0.0565          |
| 1.0001 | 14950 | 0.006         | -               |
| 1.0035 | 15000 | 0.0022        | -               |
| 1.0068 | 15050 | 0.0077        | -               |
| 1.0102 | 15100 | 0.0067        | -               |
| 1.0135 | 15150 | 0.0021        | -               |
| 1.0169 | 15200 | 0.0068        | -               |
| 1.0202 | 15250 | 0.0037        | -               |
| 1.0235 | 15300 | 0.0072        | -               |
| 1.0269 | 15350 | 0.0027        | -               |
| 1.0302 | 15400 | 0.0034        | -               |
| 1.0336 | 15450 | 0.0038        | -               |
| 1.0369 | 15500 | 0.0043        | -               |
| 1.0403 | 15550 | 0.0028        | -               |
| 1.0436 | 15600 | 0.0009        | -               |
| 1.0470 | 15650 | 0.0009        | -               |
| 1.0503 | 15700 | 0.0021        | -               |
| 1.0537 | 15750 | 0.0033        | -               |
| 1.0570 | 15800 | 0.0031        | -               |
| 1.0603 | 15850 | 0.001         | -               |
| 1.0637 | 15900 | 0.0032        | -               |
| 1.0670 | 15950 | 0.0025        | -               |
| 1.0704 | 16000 | 0.0052        | -               |
| 1.0737 | 16050 | 0.0011        | -               |
| 1.0771 | 16100 | 0.0008        | -               |
| 1.0804 | 16150 | 0.0063        | -               |
| 1.0838 | 16200 | 0.0031        | -               |
| 1.0871 | 16250 | 0.0021        | -               |
| 1.0904 | 16300 | 0.0032        | -               |
| 1.0938 | 16350 | 0.0025        | -               |
| 1.0971 | 16400 | 0.003         | -               |
| 1.1005 | 16450 | 0.0046        | -               |
| 1.1038 | 16500 | 0.0023        | -               |
| 1.1072 | 16550 | 0.0053        | -               |
| 1.1105 | 16600 | 0.0028        | -               |
| 1.1139 | 16650 | 0.0038        | -               |
| 1.1172 | 16700 | 0.0023        | -               |
| 1.1206 | 16750 | 0.0051        | -               |
| 1.1239 | 16800 | 0.0013        | -               |
| 1.1272 | 16850 | 0.002         | -               |
| 1.1306 | 16900 | 0.0037        | -               |
| 1.1339 | 16950 | 0.0032        | -               |
| 1.1373 | 17000 | 0.0031        | -               |
| 1.1406 | 17050 | 0.0029        | -               |
| 1.1440 | 17100 | 0.0044        | -               |
| 1.1473 | 17150 | 0.0029        | -               |
| 1.1507 | 17200 | 0.0019        | -               |
| 1.1540 | 17250 | 0.001         | -               |
| 1.1573 | 17300 | 0.0031        | -               |
| 1.1607 | 17350 | 0.004         | -               |
| 1.1640 | 17400 | 0.0064        | -               |
| 1.1674 | 17450 | 0.0035        | -               |
| 1.1707 | 17500 | 0.0011        | -               |
| 1.1741 | 17550 | 0.0016        | -               |
| 1.1774 | 17600 | 0.0021        | -               |
| 1.1808 | 17650 | 0.0057        | -               |
| 1.1841 | 17700 | 0.0021        | -               |
| 1.1874 | 17750 | 0.003         | -               |
| 1.1908 | 17800 | 0.0021        | -               |
| 1.1941 | 17850 | 0.0053        | -               |
| 1.1975 | 17900 | 0.0015        | -               |
| 1.2008 | 17950 | 0.0008        | -               |
| 1.2042 | 18000 | 0.0031        | -               |
| 1.2075 | 18050 | 0.0051        | -               |
| 1.2109 | 18100 | 0.0025        | -               |
| 1.2142 | 18150 | 0.0031        | -               |
| 1.2176 | 18200 | 0.0021        | -               |
| 1.2209 | 18250 | 0.0011        | -               |
| 1.2242 | 18300 | 0.0022        | -               |
| 1.2276 | 18350 | 0.0031        | -               |
| 1.2309 | 18400 | 0.0011        | -               |
| 1.2343 | 18450 | 0.0019        | -               |
| 1.2376 | 18500 | 0.0032        | -               |
| 1.2410 | 18550 | 0.0022        | -               |
| 1.2443 | 18600 | 0.002         | -               |
| 1.2477 | 18650 | 0.0007        | -               |
| 1.2510 | 18700 | 0.0019        | -               |
| 1.2543 | 18750 | 0.0033        | -               |
| 1.2577 | 18800 | 0.0009        | -               |
| 1.2610 | 18850 | 0.0007        | -               |
| 1.2644 | 18900 | 0.0028        | -               |
| 1.2677 | 18950 | 0.0036        | -               |
| 1.2711 | 19000 | 0.0019        | -               |
| 1.2744 | 19050 | 0.002         | -               |
| 1.2778 | 19100 | 0.002         | -               |
| 1.2811 | 19150 | 0.0017        | -               |
| 1.2845 | 19200 | 0.0008        | -               |
| 1.2878 | 19250 | 0.0043        | -               |
| 1.2911 | 19300 | 0.0008        | -               |
| 1.2945 | 19350 | 0.0018        | -               |
| 1.2978 | 19400 | 0.0011        | -               |
| 1.3012 | 19450 | 0.0016        | -               |
| 1.3045 | 19500 | 0.0008        | -               |
| 1.3079 | 19550 | 0.0019        | -               |
| 1.3112 | 19600 | 0.0007        | -               |
| 1.3146 | 19650 | 0.0006        | -               |
| 1.3179 | 19700 | 0.0026        | -               |
| 1.3212 | 19750 | 0.0029        | -               |
| 1.3246 | 19800 | 0.0014        | -               |
| 1.3279 | 19850 | 0.002         | -               |
| 1.3313 | 19900 | 0.0032        | -               |
| 1.3346 | 19950 | 0.0007        | -               |
| 1.3380 | 20000 | 0.0018        | -               |
| 1.3413 | 20050 | 0.0029        | -               |
| 1.3447 | 20100 | 0.0018        | -               |
| 1.3480 | 20150 | 0.003         | -               |
| 1.3514 | 20200 | 0.0029        | -               |
| 1.3547 | 20250 | 0.0007        | -               |
| 1.3580 | 20300 | 0.0017        | -               |
| 1.3614 | 20350 | 0.0018        | -               |
| 1.3647 | 20400 | 0.0041        | -               |
| 1.3681 | 20450 | 0.0006        | -               |
| 1.3714 | 20500 | 0.0005        | -               |
| 1.3748 | 20550 | 0.0029        | -               |
| 1.3781 | 20600 | 0.0032        | -               |
| 1.3815 | 20650 | 0.0006        | -               |
| 1.3848 | 20700 | 0.0006        | -               |
| 1.3881 | 20750 | 0.003         | -               |
| 1.3915 | 20800 | 0.003         | -               |
| 1.3948 | 20850 | 0.0041        | -               |
| 1.3982 | 20900 | 0.0022        | -               |
| 1.4015 | 20950 | 0.0022        | -               |
| 1.4049 | 21000 | 0.0017        | -               |
| 1.4082 | 21050 | 0.0018        | -               |
| 1.4116 | 21100 | 0.0053        | -               |
| 1.4149 | 21150 | 0.0006        | -               |
| 1.4182 | 21200 | 0.0027        | -               |
| 1.4216 | 21250 | 0.0005        | -               |
| 1.4249 | 21300 | 0.0015        | -               |
| 1.4283 | 21350 | 0.0005        | -               |
| 1.4316 | 21400 | 0.0029        | -               |
| 1.4350 | 21450 | 0.0042        | -               |
| 1.4383 | 21500 | 0.0017        | -               |
| 1.4417 | 21550 | 0.0018        | -               |
| 1.4450 | 21600 | 0.0017        | -               |
| 1.4484 | 21650 | 0.0029        | -               |
| 1.4517 | 21700 | 0.004         | -               |
| 1.4550 | 21750 | 0.0007        | -               |
| 1.4584 | 21800 | 0.004         | -               |
| 1.4617 | 21850 | 0.0021        | -               |
| 1.4651 | 21900 | 0.0017        | -               |
| 1.4684 | 21950 | 0.0016        | -               |
| 1.4718 | 22000 | 0.0016        | -               |
| 1.4751 | 22050 | 0.0028        | -               |
| 1.4785 | 22100 | 0.0016        | -               |
| 1.4818 | 22150 | 0.0016        | -               |
| 1.4851 | 22200 | 0.0023        | -               |
| 1.4885 | 22250 | 0.0005        | -               |
| 1.4918 | 22300 | 0.0016        | -               |
| 1.4952 | 22350 | 0.0028        | -               |
| 1.4985 | 22400 | 0.0017        | -               |
| 1.5019 | 22450 | 0.0005        | -               |
| 1.5052 | 22500 | 0.0017        | -               |
| 1.5086 | 22550 | 0.0024        | -               |
| 1.5119 | 22600 | 0.0011        | -               |
| 1.5153 | 22650 | 0.0018        | -               |
| 1.5186 | 22700 | 0.0025        | -               |
| 1.5219 | 22750 | 0.0016        | -               |
| 1.5253 | 22800 | 0.0007        | -               |
| 1.5286 | 22850 | 0.0035        | -               |
| 1.5320 | 22900 | 0.0021        | -               |
| 1.5353 | 22950 | 0.0025        | -               |
| 1.5387 | 23000 | 0.0017        | -               |
| 1.5420 | 23050 | 0.0038        | -               |
| 1.5454 | 23100 | 0.0008        | -               |
| 1.5487 | 23150 | 0.0016        | -               |
| 1.5520 | 23200 | 0.0005        | -               |
| 1.5554 | 23250 | 0.0025        | -               |
| 1.5587 | 23300 | 0.0005        | -               |
| 1.5621 | 23350 | 0.0017        | -               |
| 1.5654 | 23400 | 0.0015        | -               |
| 1.5688 | 23450 | 0.0015        | -               |
| 1.5721 | 23500 | 0.0017        | -               |
| 1.5755 | 23550 | 0.0041        | -               |
| 1.5788 | 23600 | 0.0026        | -               |
| 1.5822 | 23650 | 0.0036        | -               |
| 1.5855 | 23700 | 0.0016        | -               |
| 1.5888 | 23750 | 0.0007        | -               |
| 1.5922 | 23800 | 0.0012        | -               |
| 1.5955 | 23850 | 0.0011        | -               |
| 1.5989 | 23900 | 0.0007        | -               |
| 1.6022 | 23950 | 0.0017        | -               |
| 1.6056 | 24000 | 0.0013        | -               |
| 1.6089 | 24050 | 0.001         | -               |
| 1.6123 | 24100 | 0.0013        | -               |
| 1.6156 | 24150 | 0.002         | -               |
| 1.6189 | 24200 | 0.0009        | -               |
| 1.6223 | 24250 | 0.0018        | -               |
| 1.6256 | 24300 | 0.0014        | -               |
| 1.6290 | 24350 | 0.0009        | -               |
| 1.6323 | 24400 | 0.0006        | -               |
| 1.6357 | 24450 | 0.0006        | -               |
| 1.6390 | 24500 | 0.0006        | -               |
| 1.6424 | 24550 | 0.0006        | -               |
| 1.6457 | 24600 | 0.0006        | -               |
| 1.6491 | 24650 | 0.0006        | -               |
| 1.6524 | 24700 | 0.0005        | -               |
| 1.6557 | 24750 | 0.0005        | -               |
| 1.6591 | 24800 | 0.0017        | -               |
| 1.6624 | 24850 | 0.0024        | -               |
| 1.6658 | 24900 | 0.0007        | -               |
| 1.6691 | 24950 | 0.0005        | -               |
| 1.6725 | 25000 | 0.0005        | -               |
| 1.6758 | 25050 | 0.0007        | -               |
| 1.6792 | 25100 | 0.0005        | -               |
| 1.6825 | 25150 | 0.0005        | -               |
| 1.6858 | 25200 | 0.0004        | -               |
| 1.6892 | 25250 | 0.0017        | -               |
| 1.6925 | 25300 | 0.0015        | -               |
| 1.6959 | 25350 | 0.0005        | -               |
| 1.6992 | 25400 | 0.0005        | -               |
| 1.7026 | 25450 | 0.0011        | -               |
| 1.7059 | 25500 | 0.0004        | -               |
| 1.7093 | 25550 | 0.0006        | -               |
| 1.7126 | 25600 | 0.0008        | -               |
| 1.7159 | 25650 | 0.0005        | -               |
| 1.7193 | 25700 | 0.0024        | -               |
| 1.7226 | 25750 | 0.0004        | -               |
| 1.7260 | 25800 | 0.0005        | -               |
| 1.7293 | 25850 | 0.0016        | -               |
| 1.7327 | 25900 | 0.0005        | -               |
| 1.7360 | 25950 | 0.0016        | -               |
| 1.7394 | 26000 | 0.0005        | -               |
| 1.7427 | 26050 | 0.0004        | -               |
| 1.7461 | 26100 | 0.0004        | -               |
| 1.7494 | 26150 | 0.0024        | -               |
| 1.7527 | 26200 | 0.0015        | -               |
| 1.7561 | 26250 | 0.0012        | -               |
| 1.7594 | 26300 | 0.0015        | -               |
| 1.7628 | 26350 | 0.0014        | -               |
| 1.7661 | 26400 | 0.0005        | -               |
| 1.7695 | 26450 | 0.0005        | -               |
| 1.7728 | 26500 | 0.0021        | -               |
| 1.7762 | 26550 | 0.0006        | -               |
| 1.7795 | 26600 | 0.0023        | -               |
| 1.7828 | 26650 | 0.0005        | -               |
| 1.7862 | 26700 | 0.0005        | -               |
| 1.7895 | 26750 | 0.0008        | -               |
| 1.7929 | 26800 | 0.0006        | -               |
| 1.7962 | 26850 | 0.0005        | -               |
| 1.7996 | 26900 | 0.0016        | -               |
| 1.8029 | 26950 | 0.0005        | -               |
| 1.8063 | 27000 | 0.001         | -               |
| 1.8096 | 27050 | 0.0005        | -               |
| 1.8130 | 27100 | 0.002         | -               |
| 1.8163 | 27150 | 0.0004        | -               |
| 1.8196 | 27200 | 0.0005        | -               |
| 1.8230 | 27250 | 0.0004        | -               |
| 1.8263 | 27300 | 0.0014        | -               |
| 1.8297 | 27350 | 0.0016        | -               |
| 1.8330 | 27400 | 0.0005        | -               |
| 1.8364 | 27450 | 0.0005        | -               |
| 1.8397 | 27500 | 0.0007        | -               |
| 1.8431 | 27550 | 0.0004        | -               |
| 1.8464 | 27600 | 0.0004        | -               |
| 1.8497 | 27650 | 0.0004        | -               |
| 1.8531 | 27700 | 0.0004        | -               |
| 1.8564 | 27750 | 0.0004        | -               |
| 1.8598 | 27800 | 0.0005        | -               |
| 1.8631 | 27850 | 0.0005        | -               |
| 1.8665 | 27900 | 0.0012        | -               |
| 1.8698 | 27950 | 0.002         | -               |
| 1.8732 | 28000 | 0.0026        | -               |
| 1.8765 | 28050 | 0.0005        | -               |
| 1.8799 | 28100 | 0.0016        | -               |
| 1.8832 | 28150 | 0.0016        | -               |
| 1.8865 | 28200 | 0.0006        | -               |
| 1.8899 | 28250 | 0.0004        | -               |
| 1.8932 | 28300 | 0.0004        | -               |
| 1.8966 | 28350 | 0.0004        | -               |
| 1.8999 | 28400 | 0.0004        | -               |
| 1.9033 | 28450 | 0.0004        | -               |
| 1.9066 | 28500 | 0.0004        | -               |
| 1.9100 | 28550 | 0.0004        | -               |
| 1.9133 | 28600 | 0.0004        | -               |
| 1.9166 | 28650 | 0.0004        | -               |
| 1.9200 | 28700 | 0.0004        | -               |
| 1.9233 | 28750 | 0.0004        | -               |
| 1.9267 | 28800 | 0.0015        | -               |
| 1.9300 | 28850 | 0.0005        | -               |
| 1.9334 | 28900 | 0.0004        | -               |
| 1.9367 | 28950 | 0.0026        | -               |
| 1.9401 | 29000 | 0.0003        | -               |
| 1.9434 | 29050 | 0.0004        | -               |
| 1.9467 | 29100 | 0.0004        | -               |
| 1.9501 | 29150 | 0.0006        | -               |
| 1.9534 | 29200 | 0.0004        | -               |
| 1.9568 | 29250 | 0.0023        | -               |
| 1.9601 | 29300 | 0.0014        | -               |
| 1.9635 | 29350 | 0.0003        | -               |
| 1.9668 | 29400 | 0.0011        | -               |
| 1.9702 | 29450 | 0.0018        | -               |
| 1.9735 | 29500 | 0.0008        | -               |
| 1.9769 | 29550 | 0.0004        | -               |
| 1.9802 | 29600 | 0.0015        | -               |
| 1.9835 | 29650 | 0.0004        | -               |
| 1.9869 | 29700 | 0.0004        | -               |
| 1.9902 | 29750 | 0.0005        | -               |
| 1.9936 | 29800 | 0.0009        | -               |
| 1.9969 | 29850 | 0.0004        | -               |
| 2.0    | 29896 | -             | 0.0632          |
| 2.0003 | 29900 | 0.0015        | -               |
| 2.0036 | 29950 | 0.0004        | -               |
| 2.0070 | 30000 | 0.0003        | -               |
| 2.0103 | 30050 | 0.0004        | -               |
| 2.0136 | 30100 | 0.0005        | -               |
| 2.0170 | 30150 | 0.0004        | -               |
| 2.0203 | 30200 | 0.0004        | -               |
| 2.0237 | 30250 | 0.0003        | -               |
| 2.0270 | 30300 | 0.0003        | -               |
| 2.0304 | 30350 | 0.0009        | -               |
| 2.0337 | 30400 | 0.0005        | -               |
| 2.0371 | 30450 | 0.0003        | -               |
| 2.0404 | 30500 | 0.0016        | -               |
| 2.0438 | 30550 | 0.0004        | -               |
| 2.0471 | 30600 | 0.0006        | -               |
| 2.0504 | 30650 | 0.0019        | -               |
| 2.0538 | 30700 | 0.0014        | -               |
| 2.0571 | 30750 | 0.0004        | -               |
| 2.0605 | 30800 | 0.0004        | -               |
| 2.0638 | 30850 | 0.0003        | -               |
| 2.0672 | 30900 | 0.0003        | -               |
| 2.0705 | 30950 | 0.0013        | -               |
| 2.0739 | 31000 | 0.0004        | -               |
| 2.0772 | 31050 | 0.0012        | -               |
| 2.0805 | 31100 | 0.0004        | -               |
| 2.0839 | 31150 | 0.0004        | -               |
| 2.0872 | 31200 | 0.0015        | -               |
| 2.0906 | 31250 | 0.0015        | -               |
| 2.0939 | 31300 | 0.0004        | -               |
| 2.0973 | 31350 | 0.0005        | -               |
| 2.1006 | 31400 | 0.0004        | -               |
| 2.1040 | 31450 | 0.0004        | -               |
| 2.1073 | 31500 | 0.0003        | -               |
| 2.1107 | 31550 | 0.0004        | -               |
| 2.1140 | 31600 | 0.0015        | -               |
| 2.1173 | 31650 | 0.0003        | -               |
| 2.1207 | 31700 | 0.0003        | -               |
| 2.1240 | 31750 | 0.0004        | -               |
| 2.1274 | 31800 | 0.0003        | -               |
| 2.1307 | 31850 | 0.0004        | -               |
| 2.1341 | 31900 | 0.0003        | -               |
| 2.1374 | 31950 | 0.0013        | -               |
| 2.1408 | 32000 | 0.0003        | -               |
| 2.1441 | 32050 | 0.0003        | -               |
| 2.1474 | 32100 | 0.0004        | -               |
| 2.1508 | 32150 | 0.0003        | -               |
| 2.1541 | 32200 | 0.0004        | -               |
| 2.1575 | 32250 | 0.0003        | -               |
| 2.1608 | 32300 | 0.0003        | -               |
| 2.1642 | 32350 | 0.0011        | -               |
| 2.1675 | 32400 | 0.0003        | -               |
| 2.1709 | 32450 | 0.0003        | -               |
| 2.1742 | 32500 | 0.0003        | -               |
| 2.1775 | 32550 | 0.0004        | -               |
| 2.1809 | 32600 | 0.0003        | -               |
| 2.1842 | 32650 | 0.0003        | -               |
| 2.1876 | 32700 | 0.0003        | -               |
| 2.1909 | 32750 | 0.0004        | -               |
| 2.1943 | 32800 | 0.0003        | -               |
| 2.1976 | 32850 | 0.0003        | -               |
| 2.2010 | 32900 | 0.0003        | -               |
| 2.2043 | 32950 | 0.0003        | -               |
| 2.2077 | 33000 | 0.0003        | -               |
| 2.2110 | 33050 | 0.0003        | -               |
| 2.2143 | 33100 | 0.0014        | -               |
| 2.2177 | 33150 | 0.0003        | -               |
| 2.2210 | 33200 | 0.0003        | -               |
| 2.2244 | 33250 | 0.0004        | -               |
| 2.2277 | 33300 | 0.0003        | -               |
| 2.2311 | 33350 | 0.0003        | -               |
| 2.2344 | 33400 | 0.0003        | -               |
| 2.2378 | 33450 | 0.0012        | -               |
| 2.2411 | 33500 | 0.0003        | -               |
| 2.2444 | 33550 | 0.0014        | -               |
| 2.2478 | 33600 | 0.0003        | -               |
| 2.2511 | 33650 | 0.0003        | -               |
| 2.2545 | 33700 | 0.0003        | -               |
| 2.2578 | 33750 | 0.0003        | -               |
| 2.2612 | 33800 | 0.0003        | -               |
| 2.2645 | 33850 | 0.0012        | -               |
| 2.2679 | 33900 | 0.0003        | -               |
| 2.2712 | 33950 | 0.0003        | -               |
| 2.2746 | 34000 | 0.0013        | -               |
| 2.2779 | 34050 | 0.0014        | -               |
| 2.2812 | 34100 | 0.0003        | -               |
| 2.2846 | 34150 | 0.0008        | -               |
| 2.2879 | 34200 | 0.0003        | -               |
| 2.2913 | 34250 | 0.0004        | -               |
| 2.2946 | 34300 | 0.0003        | -               |
| 2.2980 | 34350 | 0.0003        | -               |
| 2.3013 | 34400 | 0.0003        | -               |
| 2.3047 | 34450 | 0.0003        | -               |
| 2.3080 | 34500 | 0.0013        | -               |
| 2.3113 | 34550 | 0.0013        | -               |
| 2.3147 | 34600 | 0.0007        | -               |
| 2.3180 | 34650 | 0.0003        | -               |
| 2.3214 | 34700 | 0.0004        | -               |
| 2.3247 | 34750 | 0.0003        | -               |
| 2.3281 | 34800 | 0.0003        | -               |
| 2.3314 | 34850 | 0.0004        | -               |
| 2.3348 | 34900 | 0.0004        | -               |
| 2.3381 | 34950 | 0.0003        | -               |
| 2.3415 | 35000 | 0.0003        | -               |
| 2.3448 | 35050 | 0.0014        | -               |
| 2.3481 | 35100 | 0.0003        | -               |
| 2.3515 | 35150 | 0.0003        | -               |
| 2.3548 | 35200 | 0.0003        | -               |
| 2.3582 | 35250 | 0.0003        | -               |
| 2.3615 | 35300 | 0.0003        | -               |
| 2.3649 | 35350 | 0.0003        | -               |
| 2.3682 | 35400 | 0.0003        | -               |
| 2.3716 | 35450 | 0.0003        | -               |
| 2.3749 | 35500 | 0.0013        | -               |
| 2.3782 | 35550 | 0.0002        | -               |
| 2.3816 | 35600 | 0.0002        | -               |
| 2.3849 | 35650 | 0.0014        | -               |
| 2.3883 | 35700 | 0.0024        | -               |
| 2.3916 | 35750 | 0.0014        | -               |
| 2.3950 | 35800 | 0.0004        | -               |
| 2.3983 | 35850 | 0.0003        | -               |
| 2.4017 | 35900 | 0.001         | -               |
| 2.4050 | 35950 | 0.0004        | -               |
| 2.4083 | 36000 | 0.0002        | -               |
| 2.4117 | 36050 | 0.0003        | -               |
| 2.4150 | 36100 | 0.0004        | -               |
| 2.4184 | 36150 | 0.0003        | -               |
| 2.4217 | 36200 | 0.0003        | -               |
| 2.4251 | 36250 | 0.0009        | -               |
| 2.4284 | 36300 | 0.0003        | -               |
| 2.4318 | 36350 | 0.0003        | -               |
| 2.4351 | 36400 | 0.0014        | -               |
| 2.4385 | 36450 | 0.0008        | -               |
| 2.4418 | 36500 | 0.0003        | -               |
| 2.4451 | 36550 | 0.0003        | -               |
| 2.4485 | 36600 | 0.0003        | -               |
| 2.4518 | 36650 | 0.0003        | -               |
| 2.4552 | 36700 | 0.0007        | -               |
| 2.4585 | 36750 | 0.0003        | -               |
| 2.4619 | 36800 | 0.0003        | -               |
| 2.4652 | 36850 | 0.0011        | -               |
| 2.4686 | 36900 | 0.0003        | -               |
| 2.4719 | 36950 | 0.0003        | -               |
| 2.4752 | 37000 | 0.0006        | -               |
| 2.4786 | 37050 | 0.0003        | -               |
| 2.4819 | 37100 | 0.0009        | -               |
| 2.4853 | 37150 | 0.0021        | -               |
| 2.4886 | 37200 | 0.0003        | -               |
| 2.4920 | 37250 | 0.0004        | -               |
| 2.4953 | 37300 | 0.0005        | -               |
| 2.4987 | 37350 | 0.0003        | -               |
| 2.5020 | 37400 | 0.0014        | -               |
| 2.5054 | 37450 | 0.0003        | -               |
| 2.5087 | 37500 | 0.0003        | -               |
| 2.5120 | 37550 | 0.0004        | -               |
| 2.5154 | 37600 | 0.0003        | -               |
| 2.5187 | 37650 | 0.0003        | -               |
| 2.5221 | 37700 | 0.0003        | -               |
| 2.5254 | 37750 | 0.0003        | -               |
| 2.5288 | 37800 | 0.0003        | -               |
| 2.5321 | 37850 | 0.0003        | -               |
| 2.5355 | 37900 | 0.0003        | -               |
| 2.5388 | 37950 | 0.0004        | -               |
| 2.5421 | 38000 | 0.0015        | -               |
| 2.5455 | 38050 | 0.0003        | -               |
| 2.5488 | 38100 | 0.0003        | -               |
| 2.5522 | 38150 | 0.0003        | -               |
| 2.5555 | 38200 | 0.0009        | -               |
| 2.5589 | 38250 | 0.0003        | -               |
| 2.5622 | 38300 | 0.0003        | -               |
| 2.5656 | 38350 | 0.0003        | -               |
| 2.5689 | 38400 | 0.0003        | -               |
| 2.5723 | 38450 | 0.0014        | -               |
| 2.5756 | 38500 | 0.0004        | -               |
| 2.5789 | 38550 | 0.0003        | -               |
| 2.5823 | 38600 | 0.0003        | -               |
| 2.5856 | 38650 | 0.0008        | -               |
| 2.5890 | 38700 | 0.0003        | -               |
| 2.5923 | 38750 | 0.0003        | -               |
| 2.5957 | 38800 | 0.0003        | -               |
| 2.5990 | 38850 | 0.0018        | -               |
| 2.6024 | 38900 | 0.0003        | -               |
| 2.6057 | 38950 | 0.0003        | -               |
| 2.6090 | 39000 | 0.0002        | -               |
| 2.6124 | 39050 | 0.0003        | -               |
| 2.6157 | 39100 | 0.0003        | -               |
| 2.6191 | 39150 | 0.0004        | -               |
| 2.6224 | 39200 | 0.0003        | -               |
| 2.6258 | 39250 | 0.0003        | -               |
| 2.6291 | 39300 | 0.0003        | -               |
| 2.6325 | 39350 | 0.0002        | -               |
| 2.6358 | 39400 | 0.0003        | -               |
| 2.6391 | 39450 | 0.0003        | -               |
| 2.6425 | 39500 | 0.0003        | -               |
| 2.6458 | 39550 | 0.0013        | -               |
| 2.6492 | 39600 | 0.0003        | -               |
| 2.6525 | 39650 | 0.0003        | -               |
| 2.6559 | 39700 | 0.0002        | -               |
| 2.6592 | 39750 | 0.0003        | -               |
| 2.6626 | 39800 | 0.0003        | -               |
| 2.6659 | 39850 | 0.0003        | -               |
| 2.6693 | 39900 | 0.0003        | -               |
| 2.6726 | 39950 | 0.0002        | -               |
| 2.6759 | 40000 | 0.0002        | -               |
| 2.6793 | 40050 | 0.0003        | -               |
| 2.6826 | 40100 | 0.0003        | -               |
| 2.6860 | 40150 | 0.0003        | -               |
| 2.6893 | 40200 | 0.0003        | -               |
| 2.6927 | 40250 | 0.0003        | -               |
| 2.6960 | 40300 | 0.0003        | -               |
| 2.6994 | 40350 | 0.0003        | -               |
| 2.7027 | 40400 | 0.0003        | -               |
| 2.7060 | 40450 | 0.0003        | -               |
| 2.7094 | 40500 | 0.0012        | -               |
| 2.7127 | 40550 | 0.0003        | -               |
| 2.7161 | 40600 | 0.0003        | -               |
| 2.7194 | 40650 | 0.0002        | -               |
| 2.7228 | 40700 | 0.0003        | -               |
| 2.7261 | 40750 | 0.0003        | -               |
| 2.7295 | 40800 | 0.0002        | -               |
| 2.7328 | 40850 | 0.0002        | -               |
| 2.7362 | 40900 | 0.0013        | -               |
| 2.7395 | 40950 | 0.0002        | -               |
| 2.7428 | 41000 | 0.0003        | -               |
| 2.7462 | 41050 | 0.0002        | -               |
| 2.7495 | 41100 | 0.0002        | -               |
| 2.7529 | 41150 | 0.0007        | -               |
| 2.7562 | 41200 | 0.0002        | -               |
| 2.7596 | 41250 | 0.0003        | -               |
| 2.7629 | 41300 | 0.0002        | -               |
| 2.7663 | 41350 | 0.0003        | -               |
| 2.7696 | 41400 | 0.0003        | -               |
| 2.7729 | 41450 | 0.0003        | -               |
| 2.7763 | 41500 | 0.0003        | -               |
| 2.7796 | 41550 | 0.0011        | -               |
| 2.7830 | 41600 | 0.0002        | -               |
| 2.7863 | 41650 | 0.0003        | -               |
| 2.7897 | 41700 | 0.0003        | -               |
| 2.7930 | 41750 | 0.0003        | -               |
| 2.7964 | 41800 | 0.0003        | -               |
| 2.7997 | 41850 | 0.0002        | -               |
| 2.8031 | 41900 | 0.0003        | -               |
| 2.8064 | 41950 | 0.0003        | -               |
| 2.8097 | 42000 | 0.0013        | -               |
| 2.8131 | 42050 | 0.0002        | -               |
| 2.8164 | 42100 | 0.0007        | -               |
| 2.8198 | 42150 | 0.0002        | -               |
| 2.8231 | 42200 | 0.0002        | -               |
| 2.8265 | 42250 | 0.0002        | -               |
| 2.8298 | 42300 | 0.0003        | -               |
| 2.8332 | 42350 | 0.0003        | -               |
| 2.8365 | 42400 | 0.0003        | -               |
| 2.8398 | 42450 | 0.0002        | -               |
| 2.8432 | 42500 | 0.0003        | -               |
| 2.8465 | 42550 | 0.0002        | -               |
| 2.8499 | 42600 | 0.0003        | -               |
| 2.8532 | 42650 | 0.0003        | -               |
| 2.8566 | 42700 | 0.0002        | -               |
| 2.8599 | 42750 | 0.0003        | -               |
| 2.8633 | 42800 | 0.0002        | -               |
| 2.8666 | 42850 | 0.0007        | -               |
| 2.8699 | 42900 | 0.0003        | -               |
| 2.8733 | 42950 | 0.0003        | -               |
| 2.8766 | 43000 | 0.0003        | -               |
| 2.8800 | 43050 | 0.0003        | -               |
| 2.8833 | 43100 | 0.0002        | -               |
| 2.8867 | 43150 | 0.0003        | -               |
| 2.8900 | 43200 | 0.0002        | -               |
| 2.8934 | 43250 | 0.0003        | -               |
| 2.8967 | 43300 | 0.0002        | -               |
| 2.9001 | 43350 | 0.0003        | -               |
| 2.9034 | 43400 | 0.0003        | -               |
| 2.9067 | 43450 | 0.0002        | -               |
| 2.9101 | 43500 | 0.0013        | -               |
| 2.9134 | 43550 | 0.0003        | -               |
| 2.9168 | 43600 | 0.0003        | -               |
| 2.9201 | 43650 | 0.0002        | -               |
| 2.9235 | 43700 | 0.0003        | -               |
| 2.9268 | 43750 | 0.0003        | -               |
| 2.9302 | 43800 | 0.0003        | -               |
| 2.9335 | 43850 | 0.0002        | -               |
| 2.9368 | 43900 | 0.0004        | -               |
| 2.9402 | 43950 | 0.0007        | -               |
| 2.9435 | 44000 | 0.0002        | -               |
| 2.9469 | 44050 | 0.0003        | -               |
| 2.9502 | 44100 | 0.0002        | -               |
| 2.9536 | 44150 | 0.0002        | -               |
| 2.9569 | 44200 | 0.0006        | -               |
| 2.9603 | 44250 | 0.0003        | -               |
| 2.9636 | 44300 | 0.0003        | -               |
| 2.9670 | 44350 | 0.0002        | -               |
| 2.9703 | 44400 | 0.0003        | -               |
| 2.9736 | 44450 | 0.0003        | -               |
| 2.9770 | 44500 | 0.0003        | -               |
| 2.9803 | 44550 | 0.0002        | -               |
| 2.9837 | 44600 | 0.0002        | -               |
| 2.9870 | 44650 | 0.0002        | -               |
| 2.9904 | 44700 | 0.0002        | -               |
| 2.9937 | 44750 | 0.0002        | -               |
| 2.9971 | 44800 | 0.0002        | -               |
| 3.0    | 44844 | -             | 0.0644          |

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