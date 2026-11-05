---
license: apache-2.0
language:
- en
base_model:
- jhu-clsp/ettin-encoder-400m
pipeline_tag: text-classification
tags:
- content-moderation
- content-guard
- moderation
- guard
- safety
- toxic
- hate-speech
- sexual
- self-harm
- violence
---
# Mezzo Content Guard v1.5

<a href="https://discord.gg/sBMqepFV6m"><img src="https://discord.com/api/guilds/1386414999932506197/embed.png" alt="Discord Link" height="20"></a>

**Mezzo Content Guard v1.5** is a series of ModernBERT-based, English-focused Content Moderation Models trained on approximately 14M tokens (360k+ rows) of labelled examples, utilizing the same dataset as in v1, but with additional data cleaning. 

**Mezzo Content Guard** comes in 5 different sizes, based on Ettin Encoder 400m, 150m, 68m, 32m and 17m:
| Model | Parameters | Description | Download |
|-------|------------|-------------|----------|
| Large | 400M | Maximum quality and accuracy | [[Link]](https://huggingface.co/RyanStudio/Mezzo-Content-Guard-v1.5-Large) |
| Base | 150M | Standard use cases | [[Link]](https://huggingface.co/RyanStudio/Mezzo-Content-Guard-v1.5-Base) |
| Small | 68M | Balanced performance | [[Link]](https://huggingface.co/RyanStudio/Mezzo-Content-Guard-v1.5-Small) |
| Tiny [NEW] | 32M | Fast inference | [[Link]](https://huggingface.co/RyanStudio/Mezzo-Content-Guard-v1.5-Tiny) |
| Nano [NEW] | 17M | lightweight or CPU inference | [[Link]](https://huggingface.co/RyanStudio/Mezzo-Content-Guard-v1.5-Nano) |

Try out the demo at the [`[Mezzo Content Guard Demo]`](https://huggingface.co/spaces/RyanStudio/Mezzo-Content-Guard-Demo) Space

# Improvements Over v1
The Ettin Encoder models from the [[Ettin Suite]](https://huggingface.co/collections/jhu-clsp/encoders-vs-decoders-the-ettin-suite) by jhu-clsp was used instead of RoBERTa due to their support for up to 8192 tokens and optimizations with the ModernBERT architecture

These models were trained using MEAN pooling rather than CLS pooling due to observed performance improvements between the 2

## Categories
**Mezzo Content Guard** covers 5 different categories

- **Hate Speech:** Content that attacks or uses discriminatory and pejorative language toward a person or group based on inherent characteristics such as race, religion, ethnicity, gender, sexual orientation, or disability.

- **Self Harm:** Content where individuals express a desire to harm themselves, or encouraging acts that lead to self harm.

- **Sexual:** Content involving any references, descriptions or intent of sexual acts.

- **Toxic:** Content that attacks, harasses, or discriminates towards an individual.

- **Violence:** Content that depicts violence and gore, or content that incites acts of violence.

## Benchmarks
All benchmarks were done with a threshold of 0.5, though the threshold can be increased or decreased to trade between precision and recall

Latency tests were done on a 5060ti 16GB

### Macro Averages
| Model | Precision | Recall | F1 | ROC-AUC |
| --- | --- | --- | --- | --- |
| v1.5-Large (400M) | **0.9067** | **0.8443** | **0.8743** | **0.9961** |
| v1.5-Base (150M) | 0.8884 | 0.8244 | 0.8551 | 0.9950 |
| v1.5-Small (68M) | 0.8503 | 0.8238 | 0.8366 | 0.9937 |
| v1.5-Tiny (32M) | 0.8284 | 0.8193 | 0.8232 | 0.9925 |
| v1.5-Nano (17M) | 0.8676 | 0.7710 | 0.8164 | 0.9907 |
| v1-Large (355M) | 0.8402 | 0.8317 | 0.8354 | 0.9922 |

### Latency

#### Batch Inference
| Model | Batch Size | Throughput (samples/s) | Avg Latency (ms/sample) |
|---|---|---|---|
| v1.5-Large | 32 | 143.0 | 6.99 |
| v1.5-Base | 32 | 317.8 | 3.15 |
| v1.5-Small | 256 | 323.7 | 3.09 |
| v1.5-Tiny | 512 | 728.4 | 1.37 |
| v1.5-Nano | 1024 | 1358.4 | 0.74 |
| v1-Large | 32 | 245.3 | 4.08 |

#### One-by-One Inference (batch_size=1)
| Model | Avg (ms) |
|---|---|
| v1.5-Large | 21.54 |
| v1.5-Base | 16.73 |
| v1.5-Small | 14.51 |
| v1.5-Tiny | 8.26 |
| v1.5-Nano | 6.13 |
| v1-Large | 10.59 |

# Quickstart
Introducing our new custom [`mezzo-guard`](https://github.com/RyanStudioo/MezzoGuard) library that supports the Mezzo Prompt Guard and Mezzo Content Guard models. It offers automatic chunking, organized policies, and redactions.

Installation:
```bash
pip install mezzo-guard
```

```py
from mezzoguard.content_guard import ContentPolicy, Category, Guard

model = Guard("RyanStudio/Mezzo-Content-Guard-v1.5-Large")
content_policy = ContentPolicy().add_threshold(Category.SEXUAL, 0.5) # Only flag Sexual messages

sexual_query = "I want to fuck you"
benign_query = "I want to have a nice day"
violent_query = "I want to kill you"

result_1 = model.scan(text=sexual_query)
print(content_policy.evaluate(result_1).is_unsafe())
# True

result_2 = model.scan(text=benign_query)
print(content_policy.evaluate(result_2).is_unsafe())
# False

result_3 = model.scan(text=violent_query)
print(content_policy.evaluate(result_3).is_unsafe())
# False
```

With `transformers`
```py
from transformers import pipeline

model = pipeline("text-classification", model="RyanStudio/Mezzo-Content-Guard-v1.5-Large")


safe_prompt = "I love mezzo content guard!!!"
print(model(safe_prompt))

hate_speech_prompt = "I hate faggots"
print(model(hate_speech_prompt))

self_harm_prompt = "I want to kill myself"
print(model(self_harm_prompt))

sexual_prompt = "I want to fuck someone"
print(model(sexual_prompt))

toxic_prompt = "You are a cunt"
print(model(toxic_prompt))

violence_prompt = "I want to kill someone"
print(model(violence_prompt))

violence_hate_speech_toxic = "I want to kill you because you're a gay faggot"
print(model(violence_hate_speech_toxic, top_k=None))

```

# Training:
The training data was sourced from various open-sourced datasets, as well as synthetically generated from LLMs such as Deepseek v4 Pro, Claude Sonnet 4.6, and Kimi K2.6.

Due to inconsistent labelling and definitions across various datasets, the data was re-laballed using Qwen3Guard-4B and Qwen3.5-4B to fit the specific categorical definitions.

The dataset was cleaned from the v1 dataset using MinHash to remove similar examples accross the same label, and exact duplicates were removed across splits to reduce cross-contamination and to reduce over-fitting to similar phrasing

The following table shows the data distribution:

| Label           |  Positives |  % of Data |
|:----------------|-----------:|-----------:|
| sexual          |     18,081 |      4.94% |
| violence        |      5,379 |      1.47% |
| self-harm       |      7,792 |      2.13% |
| hate-speech     |     30,814 |      8.42% |
| toxic           |     32,537 |      8.89% |



# Limitations
- **Re-labelling**: Due to the training data being relabelled by Qwen3Guard and Qwen3.5, any inaccuracies from when these models were trained may be passed on to the model
- **Edge Cases**: A large majority of the open sourced datasets used were often dated, and may not take into account modern day slang words or more subtle bypasses, we recommend finetuning the model on your own usecase
- **English Only**: The Ettin Encoder models are primarily english-based models, and will suffer in multilingual contexts
- **Over‑blocking of marginalized groups**: Due to training datasets containing mentions of marginalized groups, the model may overflag mentions of such groups

