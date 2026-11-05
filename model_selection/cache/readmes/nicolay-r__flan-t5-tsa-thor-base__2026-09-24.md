---
language:
- en
license: mit
library_name: transformers
metrics:
- f1
pipeline_tag: text-generation
base_model:
- google/flan-t5-base
tags:
- sentiment-analysis
- target-sentiment-analysis
- reasoning
---

# Model Card for Model ID

## Model Details
[![arXiv](https://img.shields.io/badge/arXiv-2404.12342-b31b1b.svg)](https://arxiv.org/abs/2404.12342)

> **Update February 23 2025:** 🔥 **BATCHING MODE SUPPORT**. 
See 🌌 [Flan-T5 provider](https://github.com/nicolay-r/nlp-thirdgate/blob/master/llm/transformers_flan_t5.py) 
for [bulk-chain](https://github.com/nicolay-r/bulk-chain) project. 
Test [is available here](https://github.com/nicolay-r/bulk-chain/blob/master/test/test_provider_batching.py)


This model represent a [Chain-of-Thought tuned verson](https://arxiv.org/pdf/2305.11255) Flan-T5 on Target Sentiment Analysis (TSA) task, using training data of [RuSentNE-2023 collection](https://github.com/dialogue-evaluation/RuSentNE-evaluation).

This model is designed for **texts written in English**. Since the original collection reprsent non-english texts, the content has been **automatically translated into English using [googletrans]**.

For the given input sentence and mentioned entity in it (*target*), this model predict author state by answering one of the following classes:
[`positive`, `negaitive`, `neutral`]

## Video Overview

<div align="center">

[![](https://markdown-videos-api.jorgenkh.no/youtube/kdkZsTQibm0)](https://youtu.be/kdkZsTQibm0)
[![](https://markdown-videos-api.jorgenkh.no/youtube/qawLJsRHzB4)](https://youtu.be/qawLJsRHzB4)

</div> 

### Model Description

- **Developed by:** Reforged by [nicolay-r](https://github.com/nicolay-r), initial credits for implementation to [scofield7419](https://github.com/scofield7419)
- **Model type:** [Flan-T5](https://huggingface.co/docs/transformers/en/model_doc/flan-t5)
- **Language(s) (NLP):** English
- **License:** [Apache License 2.0](https://github.com/scofield7419/THOR-ISA/blob/main/LICENSE.txt)

### Model Sources

- **Repository:** [Reasoning-for-Sentiment-Analysis-Framework](https://github.com/nicolay-r/Reasoning-for-Sentiment-Analysis-Framework)
- **Paper:** https://arxiv.org/abs/2404.12342
- **Demo:** We have a [code on Google-Colab for launching the related model](https://colab.research.google.com/github/nicolay-r/Reasoning-for-Sentiment-Analysis-Framework/blob/main/Reasoning_for_Sentiment_Analysis_Framework.ipynb)

## Uses


### Direct Use


This sequence of scripts represent a purely `torch` and `transformers` based model usage for inference.

This example is also available on [GoogleColab](https://github.com/nicolay-r/Reasoning-for-Sentiment-Analysis-Framework/blob/main/FlanT5_Finetuned_Model_Usage.ipynb)

Here are the **following three steps for a quick start with model application**:


1. Loading model and tokenizer

```python
import torch
from transformers import AutoTokenizer, T5ForConditionalGeneration

# Setup model path.
model_path = "nicolay-r/flan-t5-tsa-thor-base"
# Setup device.
device = "cuda:0"

model = T5ForConditionalGeneration.from_pretrained(model_path, torch_dtype=torch.bfloat16)
tokenizer = AutoTokenizer.from_pretrained(model_path)
model.to(device)
```

2. Setup ask method for generating LLM responses
```python
def ask(prompt):
  inputs = tokenizer(prompt, return_tensors="pt", add_special_tokens=False)
  inputs.to(device)
  output = model.generate(**inputs, temperature=1)
  return tokenizer.batch_decode(output, skip_special_tokens=True)[0]
```

2. Setup Chain-of-Thought
```python
def target_sentiment_extraction(sentence, target):
  # Setup labels.
  labels_list = ['neutral', 'positive', 'negative']
  # Setup Chain-of-Thought
  step1 = f"Given the sentence {sentence}, which specific aspect of {target} is possibly mentioned?"
  aspect = ask(step1)
  step2 = f"{step1}. The mentioned aspect is about {aspect}. Based on the common sense, what is the implicit opinion towards the mentioned aspect of {target}, and why?"
  opinion = ask(step2)
  step3 = f"{step2}. The opinion towards the mentioned aspect of {target} is {opinion}. Based on such opinion, what is the sentiment polarity towards {target}?"
  emotion_state = ask(step3)
  step4 = f"{step3}. The sentiment polarity is {emotion_state}. Based on these contexts, summarize and return the sentiment polarity only, " + "such as: {}.".format(", ".join(labels_list))
  # Return the final response.
  return ask(step4)
```

Finally, you can infer model results as follows:
```python
# Input sentence.
sentence = "I would support him despite his bad behavior."
# Input target.
target = "him"
# output response
flant5_response = target_sentiment_extraction(sentence, target)
print(f"Author opinion towards `{target}` in `{sentence}` is:\n{flant5_response}")
```

The response of the model is as follows:
> Author opinion towards "him" in "I would support him despite his bad behavior." is: **positive**
 
### Downstream Use

Please refer to the [related section](https://github.com/nicolay-r/Reasoning-for-Sentiment-Analysis-Framework?tab=readme-ov-file#three-hop-chain-of-thought-thor) of the **Reasoning-for-Sentiment-Analysis** Framework

With this example it applies this model in the THoR mode to the validation data of the RuSentNE-2023 competition for evaluation.

```sh
python thor_finetune.py -m "nicolay-r/flan-t5-tsa-thor-base" -r "thor" -d "rusentne2023" -z -bs 16 -f "./config/config.yaml"
```

Following the [Google Colab Notebook]((https://colab.research.google.com/github/nicolay-r/Reasoning-for-Sentiment-Analysis-Framework/blob/main/Reasoning_for_Sentiment_Analysis_Framework.ipynb)) for implementation reproduction.


### Out-of-Scope Use

This model represent a fine-tuned version of the Flan-T5 on RuSentNE-2023 dataset.
Since dataset represent three-scale output answers (`positive`, `negative`, `neutral`), 
the behavior in general might be biased to this particular task.

### Recommendations

Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model. More information needed for further recommendations.

## How to Get Started with the Model

Please proceed with the code from the related [Three-Hop-Reasoning CoT](https://github.com/nicolay-r/Reasoning-for-Sentiment-Analysis-Framework?tab=readme-ov-file#three-hop-chain-of-thought-thor) section.

Or following the related section on [Google Colab notebook](https://colab.research.google.com/github/nicolay-r/Reasoning-for-Sentiment-Analysis-Framework/blob/main/Reasoning_for_Sentiment_Analysis_Framework.ipynb
)

## Training Details

### Training Data

We utilize `train` data which was **automatically translated into English using GoogleTransAPI**. 
The initial source of the texts written in Russian, is from the following repository:
https://github.com/dialogue-evaluation/RuSentNE-evaluation

The translated version on the dataset in English could be automatically downloaded via the following script:
https://github.com/nicolay-r/Reasoning-for-Sentiment-Analysis-Framework/blob/main/rusentne23_download.py

### Training Procedure

This model has been trained using the Three-hop-Reasoning framework, proposed in the paper: 
https://arxiv.org/abs/2305.11255

For training procedure accomplishing, the reforged version of this framework was used:
https://github.com/nicolay-r/Reasoning-for-Sentiment-Analysis-Framework

Google-colab notebook for reproduction: 
https://colab.research.google.com/github/nicolay-r/Reasoning-for-Sentiment-Analysis-Framework/blob/main/Reasoning_for_Sentiment_Analysis_Framework.ipynb

**Setup:** `Flan-T5-base`, output up to 300 tokens, 16-batch size.

**GPU:** `NVidia-A100`, ~4 min/epoch, temperature 1.0, float 32

The overall training process took **5 epochs**.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64e62d11d27a8292c3637f86/JwCP0EIe6q1VVdNrTzPQl.png)

#### Training Hyperparameters

- **Training regime:** All the configuration details were highlighted in the related
 [config](https://github.com/nicolay-r/Reasoning-for-Sentiment-Analysis-Framework/blob/main/config/config.yaml) file

## Evaluation

### Testing Data, Factors & Metrics

#### Testing Data

The direct link to the `test` evaluation data:
https://github.com/dialogue-evaluation/RuSentNE-evaluation/blob/main/final_data.csv

#### Metrics

For the model evaluation, two metrics were used:
1. F1_PN -- F1-measure over `positive` and `negative` classes;
2. F1_PN0 -- F1-measure over `positive`, `negative`, **and `neutral`** classes;

### Results

The test evaluation for this model [showcases](https://arxiv.org/abs/2404.12342) the F1_PN = 62.715

Below is the log of the training process that showcases the final peformance on the RuSentNE-2023 `test` set after 4 epochs (lines 5-6):
```tsv
    F1_PN  F1_PN0  default   mode
0  45.523  59.375   59.375  valid
1  62.345  70.260   70.260  valid
2  62.722  70.704   70.704  valid
3  62.721  70.671   70.671  valid
4  62.357  70.247   70.247  valid
5  60.024  68.171   68.171   test
6  60.024  68.171   68.171   test
```