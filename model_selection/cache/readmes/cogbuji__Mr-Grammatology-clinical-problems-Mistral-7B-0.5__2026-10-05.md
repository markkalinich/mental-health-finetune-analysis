---
base_model: teknium/OpenHermes-2.5-Mistral-7B
license: mit
language:
- en
model_creator: Chime Ogbuji
library_name: mlx
model_name: Mr-Grammatology-clinical-problems-Mistral-7B-0.5
pipeline_tag: text-generation
prompt_template: '<|im_start|>system

  {system_message}<|im_end|>

  <|im_start|>user

  {prompt}<|im_end|>

  <|im_start|>assistant
'
tags:
- mlx
- medical
- health  
- mistral
- instruct
- finetune
- chatml
---

# Mr-Grammatology-clinical-problems-Mistral-7B-0.5
![image/png](https://cdn-uploads.huggingface.co/production/uploads/651d96a3e8c4c2ebaafc1e7d/uyiryuBhU4y62f4CRxabO.png)

The name of the model is a homage to Fela Kuti's song __Mr Grammarticalogy-Lisationalsim Is The Boss__ released on the B-side of his 1976 LP [Excuse O](https://www.discogs.com/release/3149841-Fela-And-The-Africa-70-Excuse-O).

It is a 16/32 QLoRa all linear layers finetune of [teknium/OpenHermes-2.5-Mistral-7B](/teknium/OpenHermes-2.5-Mistral-7B) using [controlled natural language (CNL) phrases](https://github.com/chimezie/django-snomed-ct#controlled-natural-language) 
generated from the September 23rd release of [SNOMED CT United States Edition](https://www.snomed.org/snomed-ct/Use-SNOMED-CT).  The general idea is described in [Domain-Specific Biomedical Ontologies, RALM, and Generative Medical Expert Systems](https://chimezie.medium.com/biomedical-ontology-retrieval-augmented-language-models-using-django-snomed-ct-and-ogbujipt-dfa0d0b150d8).

It is an experimental model for non-production environments to test how generative AI systems can be trained for use in various medical informatics scenarios.

The original model was converted to MLX format, quantized, and then subject to continued pretraining using all the active domain-expert text definitions available in SNOMED-CT at a constant learning rate of 1e-5 using 
[mlx_lm's LoRa finetuning functionality](https://github.com/ml-explore/mlx-examples/blob/main/llms/mlx_lm/LORA.md) with 16 LoRa layers.  

It was then trained on a dataset of 336,762 records of medical terminology **definition instructions** generated from SNOMED-CT using a fork of [django-snomed-ct](https://github.com/chimezie/django-snomed-ct).  These definition instructions were generated from the **disorder**, **finding**, **morphological abnormality**, and **situation** hierarchies in SNOMED-CT.  This training step was done using [mlx-tuning-fork](https://github.com/chimezie/mlx-tuning-fork) through 42,096 training iterations, with a batch size of 8 at a time, using LoRa on all linear layers.

There were 51,082 records of more granular definition instructions, part of which were incorporated into the training dataset.  However, 40% were kept aside for validation.  

## Use with mlx

```bash
pip install mlx-lm
```

Download and convert.

```bash
$ python -m mlx_lm.convert --hf-path cogbuji/Mr-Grammatology-clinical-problems-Mistral-7B-0.5 \
         --mlx-path /path/to/mlx/model
```

Generate from prompts in commandline (see [Generate Text with LLMs and MLX](https://github.com/ml-explore/mlx-examples/tree/main/llms) for more options )

```bash
$ python -m mlx_lm.generate --prompt "How is Cardiomyopathy characterized in form?" \
         --temp .4 -m 300 --model /path/to/mlx/model --seed 4
```

```
Prompt: <|im_start|>user
How is Cardiomyopathy characterized in form?<|im_end|>
<|im_start|>assistant

Cardiomyopathy is characterized in form by a morphologically abnormal structure located in a myocardium structure
```

## Example of use of 1-shot description prompting
Using mlx-tuning-fork with OgbujiPts word looms to construct 1-shot example of description prompting.

```bash
$ python -m mlx_tuning_fork.training -nt 1200 -t .4 --loom-file=sct_prompt.toml -f chatml config.yaml

```

```
Prompt: <|im_start|>system
Give detailed responses.  Use critical thinking and think step-by-step.
Don't make up answers if you don't know. Use SNOMED-CT definitions as much as possible, describing 
characterizations in form of morphological abnormalities involved in diagnoses (their signs), their etiology (causes/basis),  
their related findings. 
## Question ##
What are the signs and etiology of Skin ulcer due to diabetes mellitus?

## Answer ##
SNOMED-CT defines Skin ulcer due to diabetes mellitus as characterized in form by an ulcer located in a skin structure.  
Ulcer is a mophologic abnormality.  
The cause or origin of a disorder is part of its etiology. 
Skin ulcer due to diabetes mellitus is caused by diabetes mellitus.  
So, the etiology of Skin ulcer due to diabetes mellitus is diabetes mellitus.
   
Infected ulcer of skin is an infectious process characterized in form by an ulcer located in a skin structure. 
Since the signs of Skin ulcer due to diabetes mellitus is also an ulcer, Infected ulcer of skin is 
an example of a disorder with the same signs as Skin ulcer due to diabetes mellitus.

<|im_end|>
<|im_start|>user

Take a deep breath and work on this problem step by step. 
## Question ##
The patient has Irritable bowel syndrome.
Summarize the the biological processes and signs (characterizations in form)
involved in the patient's diagnoses. Give examples of other disorders with the same signs and etiology.
<|im_end|>
<|im_start|>assistant

Irritable bowel syndrome (SNOMED-CT definition: Irritable bowel syndrome) is a functional disorder of the gastrointestinal tract, characterized in form by abnormal bowel movements. It is a clinical diagnosis, and its signs and symptoms include abdominal pain, bloating, and altered bowel movements (diarrhea, constipation, or both).

Etiology: Irritable bowel syndrome is believed to be caused by factors including abnormal gut motility, gastrointestinal dysrhythmias, and psychological factors.

Signs: Examples of signs of the disorder include changes in stool consistency and abdominal pain.

Irritable bowel syndrome is a functional bowel disorder, which is a category of gastrointestinal disorders with similar signs and symptoms. Examples of disorders with the same signs and etiology include:

1. Functional dyspepsia: It is characterized by an upper abdominal pain or discomfort and has a similar etiology as irritable bowel syndrome. It is a functional disorder of the stomach and small intestine, and its signs include epigastric pain and discomfort.

2. Chronic idiopathic constipation: It is characterized by chronic constipation and has a similar etiology as irritable bowel syndrome. It is a functional disorder of the colon
==========
Prompt: 447.658 tokens-per-sec

```
