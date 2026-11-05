---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:492
- loss:MultipleNegativesRankingLoss
base_model: vllm-sr/mmbert-embed-32k-2d-matryoshka
widget:
- source_sentence: 'A 60-year-old man is rushed to the emergency room after he was
    found unconscious in bed that afternoon. The patient’s wife says he has been confused
    and irritable for the past several days. She says he has a history of chronic
    daily alcohol abuse and has been hospitalized multiple times with similar symptoms
    His temperature is 37°C (98.6°F), the blood pressure is 110/80 mm Hg, the pulse
    is 90/min, and the respiratory rate is 14/min. On physical examination, the patient
    is minimally responsive to painful stimuli. His abdomen is distended with positive
    shifting dullness. Laboratory results are as follows:

    Complete blood count

    Hematocrit 35%

    Platelets 100,000/mm3

    White blood cells 5000/mm3

    Liver function studies

    Serum Albumin 2 g/dL

    Alkaline phosphatase (ALP) 200 IU/L

    Aspartate aminotransferase (AST) 106 IU/L

    Alanine aminotransferase (ALT) 56 IU/L

    The patient is admitted to the hospital and started on the appropriate treatment
    to improve his mental status. Which of the following best describes the mechanism
    of action of the drug that is most likely used to treat this patient’s symptoms?'
  sentences:
  - 'A 60-year-old man is rushed to the emergency room after he was found unconscious
    in bed that afternoon. The patient’s wife says he has been confused and irritable
    for the past several days. She says he has a history of chronic daily alcohol
    abuse and has been hospitalized multiple times with similar symptoms His temperature
    is 37°C (98.6°F), the blood pressure is 110/80 mm Hg, the pulse is 90/min, and
    the respiratory rate is 14/min. On physical examination, the patient is minimally
    responsive to painful stimuli. His abdomen is distended with positive shifting
    dullness. Laboratory results are as follows:

    Complete blood count

    Hematocrit 35%

    Platelets 100,000/mm3

    White blood cells 5000/mm3

    Liver function studies

    Serum Albumin 2 g/dL

    Alkaline phosphatase (ALP) 200 IU/L

    Aspartate aminotransferase (AST) 106 IU/L

    Alanine aminotransferase (ALT) 56 IU/L

    The patient is admitted to the hospital and started on the appropriate treatment
    to improve his mental status. Which of the following best describes the mechanism
    of action of the drug that is most likely used to treat this patient’s symptoms?


    Answer: Decreases pH in the gastrointestinal lumen'
  - 'A 65-year-old man is brought to the emergency department after loss of consciousness.
    He is accompanied by his wife. He is started on intravenous fluids, and his vital
    signs are assessed. His blood pressure is 85/50 mm Hg, pulse 50/min, and respiratory
    rate 10/min. He has been admitted in the past for a heart condition. His wife
    is unable to recall the name of the condition, but she does know that the doctor
    recommended some medications at that time in case his condition worsened. She
    has brought with her the test reports from previous medical visits over the last
    few months. She says that she has noticed that he often has difficulty breathing
    and requires three pillows to sleep at night to avoid being short of breath. He
    can only walk for a few kilometers before he has to stop and rest. His wife also
    reports that he has had occasional severe coughing spells with pinkish sputum
    production. She also mentions that he has been drinking alcohol for the past 30
    years. Which of the following medications will improve the prognosis of this patient?


    Answer: Enalapril'
  - 'A 71-year-old African American man is brought to the emergency department with
    a worsening productive cough and dyspnea for 2 days. He has had generalized bone
    pain for 2 months. He was admitted for pyelonephritis last month. He also received
    outpatient treatment for pneumonia almost 2 months ago. Over the past 2 months,
    he has been taking over-the-counter ibuprofen for pain as needed. He appears anxious.
    The vital signs include: temperature 38.8°C (101.8°F), pulse 95/min, respiratory
    rate 20/min, and blood pressure 155/90 mm Hg. The conjunctivae are pale. Crackles
    are heard in the right lower lobe. The cardiac examination shows no abnormalities.
    The laboratory studies show the following:

    Hemoglobin 9 g/dL

    Mean corpuscular volume 95 μm3

    Leukocyte count 13,500/mm3

    Segmented neutrophils 75%

    Lymphocytes 25%

    Platelet count 240,000/mm3

    ESR 85 mm/hr

    Serum

    Na+ 135 mEq/L

    K+ 4.2 mEq/L

    Cl− 113 mEq/L

    HCO3− 20 mEq/L

    Ca+ 12.4 mg/dL

    Albumin 4 g/dL

    Urea nitrogen 38 mg/dL

    Creatinine 2.2 mg/dL

    A chest X-ray shows a right lower lobe opacity and blurring of the ipsilateral
    diaphragmatic dome. Skull and pelvic X-rays are performed (see image). Which of
    the following is the most likely underlying cause of this patient’s recent infections?


    Answer: Hypogammaglobulinemia'
- source_sentence: 'A 35-year-old man presents to the physician with concerns that
    a “bad flu” he has had for the past 10 days is getting worse and causing sleeplessness.
    On presentation today, his sore throat has improved; however, fever and chest
    and body aches persist despite the use of ibuprofen. He reports sharp, intermittent
    chest pain that worsens with exertion. He has not traveled outside the United
    States recently and does not have a history of substance abuse or alcohol use.
    Physical examination shows the temperature is 38.3°C (100.9°F), the heart rate
    is 110/min, the blood pressure is 120/60 mm Hg, and the oxygen saturation is 98%
    on room air. There is bilateral pedal edema at the level of the ankle. Auscultation
    reveals normal S1 and S2 and a third early diastolic heart sound. Jugular vein
    distention is observed. An ECG shows sinus tachycardia and diffuse ST-segment
    elevation throughout the precordial leads with 1.0-mm PR-segment depression in
    leads I and II.

    Laboratory results

    WBC 14,000/mm3

    Lymphocyte count 70%

    Hematocrit 45%

    CRP 56 mg/dL

    Troponin T 1.15 ng/mL

    Troponin I 0.2 ng/mL

    Ck-MB 22 ng/mL

    Coxsackie type b viral antibody  positive

    A chest x-ray shows clear lung fields bilaterally and a mildly enlarged cardiac
    silhouette. Transthoracic ultrasound reveals a left ventricular ejection fraction
    of 30%. Which of the following is the cause of difficulty sleeping for this patient?'
  sentences:
  - 'A 20-year-old female with type I diabetes mellitus presents to the emergency
    department with altered mental status. Her friend said that she has been out late
    either studying for upcoming tests or attending prayer group meetings. As far
    as the friend can recollect, the patient appeared to be in her usual state of
    health until only two days ago, when she was prescribed trimethoprim-sulfamethoxazole
    for a urinary tract infection. The patient complained that the medication was
    making her feel nauseous and bloated. The patient also relies on glargine and
    lispro for glycemic control. Her temperature is 100.5°F (38.1°C), blood pressure
    is 95/55 mmHg, pulse is 130/min, and respirations are 30/min. Her pupils are equal
    and reactive to light bilaterally. The remainder of the physical exam is unremarkable.
    Her basic metabolic panel is displayed below:


    Serum:

    Na+: 116 mEq/L

    Cl-: 90 mEq/L

    K+: 5.0 mEq/L

    HCO3-: 2 mEq/L

    BUN: 50 mg/dL

    Glucose: 1,200 mg/dL

    Creatinine: 1.5 mg/dL


    Which of the following is true regarding this patient''s presentation?


    Answer: Hyperkalemia is independent of the patient''s total body potassium stores'
  - 'A 24-year-old woman, otherwise healthy, presents with a non-productive cough,
    sore throat, and myalgia. The patient reports that her symptoms started gradually
    2 weeks ago and have not improved. She has no significant past medical history
    and no current medications. She is a college student and denies any recent overseas
    travel. The patient received the flu vaccine this year, and her 2-part PPD required
    for school was negative. She does not smoke, drink, or use recreational drugs.
    The patient denies being sexually active. The vital signs include: temperature
    37.0°C (98.6°F), blood pressure 110/75 mm Hg, pulse 98/min, respirations 20/min,
    and oxygen saturation 99% on room air. On physical exam, the patient is alert
    and cooperative. The cardiac exam is normal. There are rales present bilaterally
    over both lung fields. The skin and conjunctiva are pale. The laboratory tests
    are pending. The chest X-ray is shown in the image. Which of the following laboratory
    findings would also commonly be found in this patient?


    Answer: Low serum levels of complement'
  - 'A 35-year-old man presents to the physician with concerns that a “bad flu” he
    has had for the past 10 days is getting worse and causing sleeplessness. On presentation
    today, his sore throat has improved; however, fever and chest and body aches persist
    despite the use of ibuprofen. He reports sharp, intermittent chest pain that worsens
    with exertion. He has not traveled outside the United States recently and does
    not have a history of substance abuse or alcohol use. Physical examination shows
    the temperature is 38.3°C (100.9°F), the heart rate is 110/min, the blood pressure
    is 120/60 mm Hg, and the oxygen saturation is 98% on room air. There is bilateral
    pedal edema at the level of the ankle. Auscultation reveals normal S1 and S2 and
    a third early diastolic heart sound. Jugular vein distention is observed. An ECG
    shows sinus tachycardia and diffuse ST-segment elevation throughout the precordial
    leads with 1.0-mm PR-segment depression in leads I and II.

    Laboratory results

    WBC 14,000/mm3

    Lymphocyte count 70%

    Hematocrit 45%

    CRP 56 mg/dL

    Troponin T 1.15 ng/mL

    Troponin I 0.2 ng/mL

    Ck-MB 22 ng/mL

    Coxsackie type b viral antibody  positive

    A chest x-ray shows clear lung fields bilaterally and a mildly enlarged cardiac
    silhouette. Transthoracic ultrasound reveals a left ventricular ejection fraction
    of 30%. Which of the following is the cause of difficulty sleeping for this patient?


    Answer: Decreased cardiac contractility due to cardiac myocyte injury'
- source_sentence: A 45-year-old Caucasian man is given nitroglycerin for the management
    of his stable angina. Nitroglycerin given for the rapid relief of acute angina
    would most likely be given through what route of administration?
  sentences:
  - 'A 43-year-old man is brought to the emergency department because of severe retrosternal
    pain radiating to the back and left shoulder for 4 hours. The pain began after
    attending a farewell party for his coworker at a local bar. He had 3–4 episodes
    of nonbilious vomiting before the onset of the pain. He has hypertension. His
    father died of cardiac arrest at the age of 55 years. He has smoked one pack of
    cigarettes daily for the last 23 years and drinks 2–3 beers daily. His current
    medications include amlodipine and valsartan. He appears pale. His temperature
    is 37° C (98.6° F), pulse is 115/min, and blood pressure is 90/60 mm Hg. There
    are decreased breath sounds over the left base and crepitus is palpable over the
    thorax. Abdominal examination shows tenderness to palpation in the epigastric
    region; bowel sounds are normal. Laboratory studies show:

    Hemoglobin 16.5 g/dL

    Leukocyte count 11,100/mm3

    Serum

    Na+ 133 mEq/L

    K+ 3.2 mEq/L

    Cl- 98 mEq/L

    HCO3- 30 mEq/L

    Creatinine 1.4 mg/dL

    An ECG shows sinus tachycardia with left ventricular hypertrophy. Intravenous
    fluid resuscitation and antibiotics are begun. Which of the following is the most
    appropriate test to confirm the diagnosis in this patient?"


    Answer: CT scan of the chest'
  - 'A 45-year-old Caucasian man is given nitroglycerin for the management of his
    stable angina. Nitroglycerin given for the rapid relief of acute angina would
    most likely be given through what route of administration?


    Answer: Sublingual'
  - 'A 67-year-old man with stable coronary artery disease comes to the physician
    for a follow-up examination. Aside from occasional exertional chest pain on mowing
    the lawn or prolonged jogging, he feels well. He goes jogging for 20 minutes once
    a week and takes a tablet of sublingual nitroglycerine prior to his run to prevent
    anginal chest pain. The patient would like to run longer distances and asks the
    physician whether he could increase the dose of the drug prior to running. Administration
    of higher dosages of this drug is most likely to result in which of the following?


    Answer: Reflex sympathetic activity'
- source_sentence: 'A 42-year-old woman comes to the physician for a routine health
    maintenance examination. She has generalized fatigue and has had difficulties
    doing her household duties for the past 3 months. She has eczema and gastroesophageal
    reflux disease. She has a history of using intravenous methamphetamine in her
    youth but has not used illicit drugs in 23 years. Her medications include topical
    clobetasol and pantoprazole. She is 160 cm (5 ft 3 in) tall and weighs 105 kg
    (231 lb); BMI is 42 kg/m2. Her temperature is 37°C (98.6°F), pulse is 95/min,
    and blood pressure is 145/90 mm Hg. The lungs are clear to auscultation. Cardiac
    examination shows no abnormalities. Pelvic examination shows a normal vagina and
    cervix. Laboratory studies show:

    Hemoglobin 13.1 g/dL

    Leukocyte count 7,800/mm3

    Platelet count 312,000/mm3

    Serum

    Na+ 141 mEq/L

    K+ 4.6 mEq/L

    Cl- 98 mEq/L

    Urea nitrogen 12 mg/dL

    Fasting glucose 110 mg/dL

    Creatinine 0.8 mg/dL

    Total cholesterol 269 mg/dL

    HDL-cholesterol 55 mg/dL

    LDL-cholesterol 160 mg/dL

    Triglycerides 320 mg/dL

    Urinalysis is within normal limits. An x-ray of the chest shows no abnormalities.
    She has not lost any weight over the past year despite following supervised weight
    loss programs, including various diets and exercise regimens. Which of the following
    is the most appropriate next step in management of this patient?"'
  sentences:
  - 'A 17-year-old male with a history of bipolar disorder presents to clinic with
    a rash (Image A) that he noticed one week after starting a medication to stabilize
    his mood. The medication blocks voltage-gated sodium channels and can be used
    to treat partial simple, partial complex, and generalized tonic-clonic seizures.
    Regarding the patient''s rash, what is the next step in management?


    Answer: Immediately discontinue the drug'
  - 'A 42-year-old woman comes to the physician for a routine health maintenance examination.
    She has generalized fatigue and has had difficulties doing her household duties
    for the past 3 months. She has eczema and gastroesophageal reflux disease. She
    has a history of using intravenous methamphetamine in her youth but has not used
    illicit drugs in 23 years. Her medications include topical clobetasol and pantoprazole.
    She is 160 cm (5 ft 3 in) tall and weighs 105 kg (231 lb); BMI is 42 kg/m2. Her
    temperature is 37°C (98.6°F), pulse is 95/min, and blood pressure is 145/90 mm
    Hg. The lungs are clear to auscultation. Cardiac examination shows no abnormalities.
    Pelvic examination shows a normal vagina and cervix. Laboratory studies show:

    Hemoglobin 13.1 g/dL

    Leukocyte count 7,800/mm3

    Platelet count 312,000/mm3

    Serum

    Na+ 141 mEq/L

    K+ 4.6 mEq/L

    Cl- 98 mEq/L

    Urea nitrogen 12 mg/dL

    Fasting glucose 110 mg/dL

    Creatinine 0.8 mg/dL

    Total cholesterol 269 mg/dL

    HDL-cholesterol 55 mg/dL

    LDL-cholesterol 160 mg/dL

    Triglycerides 320 mg/dL

    Urinalysis is within normal limits. An x-ray of the chest shows no abnormalities.
    She has not lost any weight over the past year despite following supervised weight
    loss programs, including various diets and exercise regimens. Which of the following
    is the most appropriate next step in management of this patient?"


    Answer: Bariatric surgery'
  - 'A 43-year-old woman visits her primary care provider complaining of fatigue.
    Although she has had it for several months, her fatigue has been worsening over
    the past few weeks. She has no other symptoms. Past medical history is significant
    for hypertension. She takes chlorthalidone, an oral contraceptive pill, and a
    multivitamin every day. Family history is noncontributory. She drinks about 1
    bottle of wine every day and started taking a shot or two of whisky or vodka every
    morning before work to “clear out the cobwebs”. She was recently fired from her
    job. Today, her heart rate is 90/min, respiratory rate is 17/min, blood pressure
    is 110/65 mm Hg, and temperature is 36.7°C (98.1°F). On physical exam, she appears
    malnourished and anxious. Her conjunctiva are pale, and glossitis is noted on
    oral exam. Her heart has a regular rate and rhythm and her lungs are clear to
    auscultation bilaterally. She has no gait or balance abnormalities. Lab results
    show a hemoglobin of 10 g/dL, with a mean corpuscular volume (MCV) of 108 fl.
    Elevated level of which of the following will most likely to be found in this
    patient?


    Answer: Homocysteine'
- source_sentence: A 45-year-old woman, gravida 3, para 2, at 18 weeks' gestation
    comes to the physician for a prenatal visit. Ultrasonography at a previous visit
    when she was at 12 weeks' gestation showed a hypoplastic nasal bone. Pelvic examination
    shows a uterus consistent in size with an 18-week gestation. Maternal serum studies
    show low α-fetoprotein and free estriol concentrations, and increased inhibin
    A and β-hCG concentrations. Physical examination of the infant after delivery
    is most likely to show which of the following findings?
  sentences:
  - 'A 45-year-old woman, gravida 3, para 2, at 18 weeks'' gestation comes to the
    physician for a prenatal visit. Ultrasonography at a previous visit when she was
    at 12 weeks'' gestation showed a hypoplastic nasal bone. Pelvic examination shows
    a uterus consistent in size with an 18-week gestation. Maternal serum studies
    show low α-fetoprotein and free estriol concentrations, and increased inhibin
    A and β-hCG concentrations. Physical examination of the infant after delivery
    is most likely to show which of the following findings?


    Answer: Single transverse palmar crease'
  - 'A 35-year-old woman gravida 2, para 1, comes to the physician for her first prenatal
    visit. Pregnancy and delivery of her first child were uncomplicated. She is not
    sure about the date of her last menstrual period. Pelvic examination shows a uterus
    consistent in size with a 10-week gestation. An ultrasound examination confirms
    the gestational age and shows one fetus with no indication of multiple gestations.
    During counseling on pregnancy risks and possible screening and diagnostic tests,
    the patient states she would like to undergo screening for Down syndrome. She
    would prefer immediate and secure screening with a low risk to herself and the
    fetus. Which of the following is the most appropriate next step in management
    at this time?


    Answer: Cell-free fetal DNA testing'
  - 'A 6-month-old male presents with a painless, enlarged left scrotum. After examining
    the patient, you suspect this enlargement is secondary to serous fluid entering
    and accumulating in the scrotum through a patent processus vaginalis. Which of
    the following would be the most useful next step in confirming the diagnosis of
    this patient’s condition?


    Answer: Transillumination test followed by scrotal ultrasound'
pipeline_tag: sentence-similarity
library_name: sentence-transformers
---

# SentenceTransformer based on vllm-sr/mmbert-embed-32k-2d-matryoshka

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [vllm-sr/mmbert-embed-32k-2d-matryoshka](https://huggingface.co/vllm-sr/mmbert-embed-32k-2d-matryoshka). It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [vllm-sr/mmbert-embed-32k-2d-matryoshka](https://huggingface.co/vllm-sr/mmbert-embed-32k-2d-matryoshka) <!-- at revision 38ba9e6c90ad4f7631d7402c5bc2c0f953277aae -->
- **Maximum Sequence Length:** 32768 tokens
- **Output Dimensionality:** 768 dimensions
- **Similarity Function:** Cosine Similarity
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 32768, 'do_lower_case': False, 'architecture': 'ModernBertModel'})
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    "A 45-year-old woman, gravida 3, para 2, at 18 weeks' gestation comes to the physician for a prenatal visit. Ultrasonography at a previous visit when she was at 12 weeks' gestation showed a hypoplastic nasal bone. Pelvic examination shows a uterus consistent in size with an 18-week gestation. Maternal serum studies show low α-fetoprotein and free estriol concentrations, and increased inhibin A and β-hCG concentrations. Physical examination of the infant after delivery is most likely to show which of the following findings?",
    "A 45-year-old woman, gravida 3, para 2, at 18 weeks' gestation comes to the physician for a prenatal visit. Ultrasonography at a previous visit when she was at 12 weeks' gestation showed a hypoplastic nasal bone. Pelvic examination shows a uterus consistent in size with an 18-week gestation. Maternal serum studies show low α-fetoprotein and free estriol concentrations, and increased inhibin A and β-hCG concentrations. Physical examination of the infant after delivery is most likely to show which of the following findings?\n\nAnswer: Single transverse palmar crease",
    'A 35-year-old woman gravida 2, para 1, comes to the physician for her first prenatal visit. Pregnancy and delivery of her first child were uncomplicated. She is not sure about the date of her last menstrual period. Pelvic examination shows a uterus consistent in size with a 10-week gestation. An ultrasound examination confirms the gestational age and shows one fetus with no indication of multiple gestations. During counseling on pregnancy risks and possible screening and diagnostic tests, the patient states she would like to undergo screening for Down syndrome. She would prefer immediate and secure screening with a low risk to herself and the fetus. Which of the following is the most appropriate next step in management at this time?\n\nAnswer: Cell-free fetal DNA testing',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 768]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.9805, 0.5273],
#         [0.9805, 1.0000, 0.5430],
#         [0.5273, 0.5430, 1.0000]], dtype=torch.bfloat16)
```

<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
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

### Training Dataset

#### Unnamed Dataset

* Size: 492 training samples
* Columns: <code>sentence_0</code>, <code>sentence_1</code>, and <code>sentence_2</code>
* Approximate statistics based on the first 492 samples:
  |         | sentence_0                                                                          | sentence_1                                                                           | sentence_2                                                                           |
  |:--------|:------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------|
  | type    | string                                                                              | string                                                                               | string                                                                               |
  | details | <ul><li>min: 36 tokens</li><li>mean: 219.2 tokens</li><li>max: 791 tokens</li></ul> | <ul><li>min: 49 tokens</li><li>mean: 227.77 tokens</li><li>max: 819 tokens</li></ul> | <ul><li>min: 51 tokens</li><li>mean: 159.34 tokens</li><li>max: 430 tokens</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | sentence_1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | sentence_2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
  |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>A 48-year-old woman presents to the emergency department because of increasingly severe right upper abdominal pain, fever, and non-bloody vomiting for the last 5 hours. The pain is dull, intermittent, and radiates to her right shoulder. During the past 3 months, she has had recurring abdominal discomfort after meals. The patient underwent an appendectomy more than 30 years ago. She has hypertension, diabetes mellitus type 2, and chronic back pain. She takes bisoprolol, metformin, and ibuprofen daily. She is 171 cm (5 ft 6 in) tall and weighs 99 kg (218 lb). Her BMI is 35.2 kg/m2. She appears uncomfortable and is clutching her abdomen. Her temperature is 38.5°C (101.3°F), pulse is 108/min, and blood pressure is 150/82 mm Hg. Abdominal examination shows right upper quadrant abdominal tenderness and guarding. Upon deep palpation of the right upper quadrant, the patient pauses during inspiration. Laboratory studies show the following:<br>Blood<br>Hemoglobin 13.1 g/dL<br>Leukocyte count 10,900/mm3<br>P...</code>                                        | <code>A 48-year-old woman presents to the emergency department because of increasingly severe right upper abdominal pain, fever, and non-bloody vomiting for the last 5 hours. The pain is dull, intermittent, and radiates to her right shoulder. During the past 3 months, she has had recurring abdominal discomfort after meals. The patient underwent an appendectomy more than 30 years ago. She has hypertension, diabetes mellitus type 2, and chronic back pain. She takes bisoprolol, metformin, and ibuprofen daily. She is 171 cm (5 ft 6 in) tall and weighs 99 kg (218 lb). Her BMI is 35.2 kg/m2. She appears uncomfortable and is clutching her abdomen. Her temperature is 38.5°C (101.3°F), pulse is 108/min, and blood pressure is 150/82 mm Hg. Abdominal examination shows right upper quadrant abdominal tenderness and guarding. Upon deep palpation of the right upper quadrant, the patient pauses during inspiration. Laboratory studies show the following:<br>Blood<br>Hemoglobin 13.1 g/dL<br>Leukocyte count 10,900/mm3<br>P...</code>                                        | <code>A 27-year-old woman presents with acute abdominal pain in her right upper quadrant. The pain came on suddenly while she was eating dinner. After this pain she began feeling dizzy and came to the emergency department. In the ED, her blood pressure is 75/40 mmHg, pulse is 100/minute, and she is afebrile. On physical exam, she feels too light-headed to ambulate. She demonstrates normal bowel sounds with tenderness upon palpation in the right upper quadrant. The patient is deemed too unstable for imaging. An abdominal radiograph and CT are reviewed from a recent previous visit to the ED for mild abdominal pain, and are shown in Figures A and B, respectively. Which of the following specific additional findings in her history supports the most likely diagnosis?<br><br>Answer: Use of oral contraceptives (OCPs) for birth control</code>                                                                                                                                                                            |
  | <code>A 42-year-old man presents to his primary care provider for abdominal pain. He reports that for several months he has been experiencing a stabbing pain above the umbilicus during meals. He denies associated symptoms of nausea, vomiting, or diarrhea. The patient’s past medical history is significant for hypertension and hyperlipidemia for which he takes amlodipine and atorvastatin. His family history is significant for lung cancer in his father. The patient is a current smoker with a 20 pack-year smoking history and drinks 3-5 beers per week. Initial laboratory testing is as follows:<br><br>Serum:<br>Na+: 141 mEq/L<br>K+: 4.6 mEq/L<br>Cl-: 102 mEq/L<br>HCO3-: 25 mEq/L<br>Urea nitrogen: 14 mg/dL<br>Creatinine: 1.1 mg/dL<br>Glucose: 120 mg/dL<br>Calcium: 8.4 mg/dL<br>Alkaline phosphatase: 66 U/L<br>Aspartate aminotransferase (AST): 40 U/L<br>Alanine aminotransferase (ALT): 52 U/L<br>Gastrin: 96 pg/mL (<100 pg/mL)<br>Lipase: 90 U/L (<160 U/L)<br><br>The patient is started on a proton pump inhibitor without symptomatic improvement after 6 w...</code> | <code>A 42-year-old man presents to his primary care provider for abdominal pain. He reports that for several months he has been experiencing a stabbing pain above the umbilicus during meals. He denies associated symptoms of nausea, vomiting, or diarrhea. The patient’s past medical history is significant for hypertension and hyperlipidemia for which he takes amlodipine and atorvastatin. His family history is significant for lung cancer in his father. The patient is a current smoker with a 20 pack-year smoking history and drinks 3-5 beers per week. Initial laboratory testing is as follows:<br><br>Serum:<br>Na+: 141 mEq/L<br>K+: 4.6 mEq/L<br>Cl-: 102 mEq/L<br>HCO3-: 25 mEq/L<br>Urea nitrogen: 14 mg/dL<br>Creatinine: 1.1 mg/dL<br>Glucose: 120 mg/dL<br>Calcium: 8.4 mg/dL<br>Alkaline phosphatase: 66 U/L<br>Aspartate aminotransferase (AST): 40 U/L<br>Alanine aminotransferase (ALT): 52 U/L<br>Gastrin: 96 pg/mL (<100 pg/mL)<br>Lipase: 90 U/L (<160 U/L)<br><br>The patient is started on a proton pump inhibitor without symptomatic improvement after 6 w...</code> | <code>A 42-year-old man comes to his primary care physician complaining of abdominal pain. He describes intermittent, burning, epigastric pain over the past 4 months. He reports that the pain worsens following meals. He had an upper gastrointestinal endoscopy done 2 months ago that showed a gastric ulcer without evidence of malignancy. The patient was prescribed pantoprazole with minimal improvement in symptoms. He denies nausea, vomiting, diarrhea, or melena. The patient has no other medical problems. He had a total knee replacement 3 years ago following a motor vehicle accident for which he took naproxen for 2 months for pain management. He has smoked 1 pack per day since the age 22 and drinks 1-2 beers several nights a week with dinner. He works as a truck driver, and his diet consists of mostly of fast food. His family history is notable for hypertension in his paternal grandfather and coronary artery disease in his mother. On physical examination, the abdomen is soft, nondistended, and ...</code> |
  | <code>A 62-year-old woman comes to the physician in June for a routine check-up. She has chronic back pain and underwent an appendectomy at the age of 27. She is married and has two kids. The patient recently got back from a cruise to Mexico where she celebrated her 40th wedding anniversary. Her last mammogram was 6 months ago and showed no abnormalities. Her last Pap smear was 2 years ago and unremarkable. A colonoscopy 5 years ago was normal. Her mother died of breast cancer last year and her father has arterial hypertension. Her immunization records show that she has never received a pneumococcal or a shingles vaccine, her last tetanus booster was 6 years ago, and her last influenza vaccine was 2 years ago. She drinks 1– 2 alcoholic beverages every weekend. She takes a multivitamin daily and uses topical steroids. She regularly attends water aerobic classes and physical therapy for her back pain. She is 168 cm (5 ft 6 in) tall and weighs 72 kg (160 lb); BMI is 26 kg/m2. Her temperature is...</code>                                                    | <code>A 62-year-old woman comes to the physician in June for a routine check-up. She has chronic back pain and underwent an appendectomy at the age of 27. She is married and has two kids. The patient recently got back from a cruise to Mexico where she celebrated her 40th wedding anniversary. Her last mammogram was 6 months ago and showed no abnormalities. Her last Pap smear was 2 years ago and unremarkable. A colonoscopy 5 years ago was normal. Her mother died of breast cancer last year and her father has arterial hypertension. Her immunization records show that she has never received a pneumococcal or a shingles vaccine, her last tetanus booster was 6 years ago, and her last influenza vaccine was 2 years ago. She drinks 1– 2 alcoholic beverages every weekend. She takes a multivitamin daily and uses topical steroids. She regularly attends water aerobic classes and physical therapy for her back pain. She is 168 cm (5 ft 6 in) tall and weighs 72 kg (160 lb); BMI is 26 kg/m2. Her temperature is...</code>                                                    | <code>A 66-year-old G3P3 presents with an 8-year-history of back pain, perineal discomfort, difficulty urinating, recurrent malaise, and low-grade fevers. These symptoms have recurred regularly for the past 5–6 years. She also says that there are times when she experiences a feeling of having a foreign body in her vagina. With the onset of symptoms, she was evaluated by a physician who prescribed her medications after a thorough examination and recommended a vaginal pessary, but she was non-compliant. She had 3 vaginal deliveries She has been menopausal since 51 years of age. She does not have a history of malignancies or cardiovascular disease. She has type 2 diabetes mellitus that is controlled with diet and metformin. Her vital signs include: blood pressure 110/60 mm Hg, heart rate 91/min, respiratory rate 13/min, and temperature 37.4℃ (99.3℉). On physical examination, there is bilateral costovertebral angle tenderness. The urinary bladder is non-palpable. The gynecologic examination reve...</code> |
* Loss: [<code>MultipleNegativesRankingLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativesrankingloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim",
      "gather_across_devices": false
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `num_train_epochs`: 2
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `do_predict`: False
- `eval_strategy`: no
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 8
- `per_device_eval_batch_size`: 8
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 5e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1
- `num_train_epochs`: 2
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: None
- `warmup_ratio`: None
- `warmup_steps`: 0
- `log_level`: passive
- `log_level_replica`: warning
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `enable_jit_checkpoint`: False
- `save_on_each_node`: False
- `save_only_model`: False
- `restore_callback_states_from_checkpoint`: False
- `use_cpu`: False
- `seed`: 42
- `data_seed`: None
- `bf16`: False
- `fp16`: False
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `local_rank`: -1
- `ddp_backend`: None
- `debug`: []
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_prefetch_factor`: None
- `disable_tqdm`: False
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch
- `optim_args`: None
- `group_by_length`: False
- `length_column_name`: length
- `project`: huggingface
- `trackio_space_id`: trackio
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `skip_memory_metrics`: True
- `push_to_hub`: False
- `resume_from_checkpoint`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_private_repo`: None
- `hub_always_push`: False
- `hub_revision`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `include_for_metrics`: []
- `eval_do_concat_batches`: True
- `auto_find_batch_size`: False
- `full_determinism`: False
- `ddp_timeout`: 1800
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `include_num_input_tokens_seen`: no
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: True
- `use_cache`: False
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: round_robin
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Framework Versions
- Python: 3.12.10
- Sentence Transformers: 5.2.2
- Transformers: 5.0.0
- PyTorch: 2.7.0+cu128
- Accelerate: 1.12.0
- Datasets: 4.5.0
- Tokenizers: 0.22.2

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

#### MultipleNegativesRankingLoss
```bibtex
@misc{henderson2017efficient,
    title={Efficient Natural Language Response Suggestion for Smart Reply},
    author={Matthew Henderson and Rami Al-Rfou and Brian Strope and Yun-hsuan Sung and Laszlo Lukacs and Ruiqi Guo and Sanjiv Kumar and Balint Miklos and Ray Kurzweil},
    year={2017},
    eprint={1705.00652},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
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