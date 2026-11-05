---
library_name: transformers
tags:
- emotion-extraction
- emotion-cause-prediction
- reasoning
- emotion
license: mit
language:
- en
metrics:
- f1-strict
- f1-proportional
- f1-strict-weighted
- f1-proportional-weighted
pipeline_tag: text-generation
base_model:
- google/flan-t5-base
---

# Model Card for Model ID

> **Update February 23 2025:** 🔥 **BATCHING MODE SUPPORT**. 
See 🌌 [Flan-T5 provider](https://github.com/nicolay-r/nlp-thirdgate/blob/master/llm/transformers_flan_t5.py) 
for [bulk-chain](https://github.com/nicolay-r/bulk-chain) project. 
Test [is available here](https://github.com/nicolay-r/bulk-chain/blob/master/test/test_provider_batching.py)

This model represent a fine-tuned version on the [Emotion-Cause Analysis in Context (ECAC) data](https://nustm.github.io/SemEval-2024_ECAC/) and aimed at answering the following problems:
1. **Emotion extraction** for the speaker in coversation context
2. **Emotion cause**, that originates from the speaker of first utterance to the other speaker of the following utterance.

This model choses the answers according to the following list of choices:

["anger", "disgust", "fear", "joy", "sadness", "surprise", "neutral"]

## Video Overview

<div align="center">

[![](https://markdown-videos-api.jorgenkh.no/youtube/vRVDQa7vfkU)](https://youtu.be/vRVDQa7vfkU)

</div>

## Model Details

### Model Description


This is the model card of a 🤗 transformers model that has been pushed on the Hub. This model card has been automatically generated.

- **Developed by:** Reforged by [nicolay-r](https://github.com/nicolay-r), initial credits for implementation to [scofield7419](https://github.com/scofield7419)
- **Model type:** [Flan-T5](https://huggingface.co/docs/transformers/en/model_doc/flan-t5)
- **Language(s) (NLP):** English
- **License:** [Apache License 2.0](https://github.com/scofield7419/THOR-ISA/blob/main/LICENSE.txt)

### Model Sources [optional]

- **Repository:** [Reasoning-for-Sentiment-Analysis-Framework](https://github.com/nicolay-r/Reasoning-for-Sentiment-Analysis-Framework)
- **Paper:** https://huggingface.co/papers/2404.03361
- **Demo:** https://github.com/nicolay-r/THOR-ECAC/blob/master/SemEval_2024_Task_3_FlanT5_Finetuned_Model_Usage.ipynb


## Uses

### Direct Use

Please proceed the following example **that purely relies on tranformers and torch**.

This example could be found on google colab at the related [Github repo page](https://github.com/nicolay-r/THOR-ECAC)

You can still use the code below for a custom start by being independent from the THoR engine.

Here are the **4 steps** for direct model use:

1. Setup ask method for inferring FlanT5 as follows: 
```python
def ask(prompt):
  inputs = tokenizer(prompt, return_tensors="pt", add_special_tokens=False)
  inputs.to(device)
  output = model.generate(**inputs, max_length=320, temperature=1)
  return tokenizer.batch_decode(output, skip_special_tokens=True)[0]
```

2. Setup chain and expected output labels:
```python
def emotion_extraction_chain(context, target):
  # Setup labels.
  labels_list = ["anger", "disgust", "fear", "joy", "sadness", "surprise", "neutral"]
  # Setup Chain-of-Thought
  step1 = f"Given the conversation {context}, which text spans are possibly causes emotion on {target}?"
  span = ask(step1)
  step2 = f"{step1}. The mentioned text spans are about {span}. Based on the common sense, what " + f"is the implicit opinion towards the mentioned text spans that causes emotion on {target}, and why?"
  opinion = ask(step2)
  step3 = f"{step2}. The opinion towards the text spans that causes emotion on {target} is {opinion}. " + f"Based on such opinion, what is the emotion state of {target}?" 
  emotion_state = ask(step3)
  step4 = f"{step3}. The emotion state is {emotion_state}. Based on these contexts, summarize and return the emotion cause only." + "Choose from: {}.".format(", ".join(labels_list))
  # Return the final response.
  return ask(step4)
```

3. Initialize `device`, `model` and `tokenizer` as follows:
```python
from transformers import AutoTokenizer, T5ForConditionalGeneration

model_path = "nicolay-r/flan-t5-emotion-cause-thor-base"
device = "cuda:0"

model = T5ForConditionalGeneration.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)
model.to(device)
```

4. Apply it!
```python
# setup history context (conv_turn_1)
conv_turn_1 = "John: ohh you made up!"
# setup utterance.
conv_turn_2 = "Jake: yaeh, I could not be mad at him for too long!"
context = conv_turn_1 + conv_turn_2
# Target is considered as the whole conv-turn mentioned in context.
target = conv_turn_2
flant5_response = emotion_extraction_chain(context, target)
print(f"Emotion state of the speaker of `{target}` is: {flant5_response}")
```

The response is as follows:
> Emotion state of the speaker of `Jake: yaeh, I could not be mad at him for too long!` is: **anger**


### Downstream Use [optional]

The details of the downstream usage could be found in the 
[related section of the project on Github](https://github.com/nicolay-r/THOR-ECAC?tab=readme-ov-file#training-and-evaluating-with-flan-t5)
or 
within the related [notebook on GoogleColab](https://github.com/nicolay-r/THOR-ECAC/blob/master/THoR_Finetuning_SemEval2023_t3_1_public.ipynb)

### Out-of-Scope Use

This model represent a fine-tuned version of the Flan-T5 on [ECAC-2024 competition](https://nustm.github.io/SemEval-2024_ECAC/) dataset of conversations from the F.R.I.E.N.D.S. TV Show.
Since dataset represent three-scale output answers ["anger", "disgust", "fear", "joy", "sadness", "surprise", "neutral"]
the behavior in general might be biased to this particular task.


### Recommendations

Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model. More information needed for further recommendations.

## How to Get Started with the Model

Simply follow the **Direct Use** secion or proceed with the following [GoogleColab notebook](https://github.com/nicolay-r/THOR-ECAC/blob/master/SemEval_2024_Task_3_FlanT5_Finetuned_Model_Usage.ipynb).

## Training Details

### Training Data

We purely rely on the data provided by ECAC-2024 competition organizers.

Here is the [related information](https://github.com/nicolay-r/THOR-ECAC?tab=readme-ov-file#datasets) from the github repository.

And here is the [code related to data convesations preparation](https://github.com/nicolay-r/SemEval2024-Task3) intented for compiling input data.

### Training Procedure 

Model has been fine-tuned in two stages:
1. THoR-state: The first stage aimed at Emotion states prediction
2. THoR-cause-RR: The second aimed at emotion-causes prediction with **reasoning-revision** technique.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64e62d11d27a8292c3637f86/RCKexEPPE_RfstMsL-PbY.png)

#### Training Hyperparameters

- **Training regime:** temperature 1.0, learning-rate 2*10^(-4), AdamW optimizer, batch-size 32, NVidia-A100 (40GB)


[More Information Needed]

#### Metrics

- f1-strict
- f1-proportional
- f1-strict-weighted
- f1-proportional-weighted

[More Information Needed]

### Results

Results are depicted in image below in a **gray-highlighted row**.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64e62d11d27a8292c3637f86/yfbkw2iMgY5fp54Zohe32.png)