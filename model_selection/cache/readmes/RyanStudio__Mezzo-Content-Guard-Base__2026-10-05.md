---
license: apache-2.0
language:
- en
base_model:
- FacebookAI/roberta-base
pipeline_tag: text-classification
tags:
- content-moderation
- content-guard
- moderation
- guard
- safety
new_version: RyanStudio/Mezzo-Content-Guard-v1.5-Base
---
# Mezzo Content Guard Large

<a href="https://discord.gg/sBMqepFV6m"><img src="https://discord.com/api/guilds/1386414999932506197/embed.png" alt="Discord Link" height="20"></a>

**Mezzo Content Guard** is a series of RoBERTa-based, English-only Content Moderation Models trained on approximately 14M tokens (360k+ rows) of labelled examples. 

**Mezzo Content Guard** comes in 3 different sizes, based on RoBERTa Large, Base, and DistilRoBERTa Base
- Large (355M Params)
- Base (125M Params)
- Small (82.8M Params)

Try out the demo at the [`Mezzo Content Guard Demo`](https://huggingface.co/spaces/RyanStudio/Mezzo-Content-Guard-Demo) Space

## Categories
**Mezzo Content Guard** covers 5 different categories

- **Hate Speech:** Content that attacks or uses discriminatory and pejorative language toward a person or group based on inherent characteristics such as race, religion, ethnicity, gender, sexual orientation, or disability.

- **Self Harm:** Content where individuals express a desire to harm themselves, or encouraging acts that lead to self harm.

- **Sexual:** Content involving any references, descriptions or intent of sexual acts.

- **Toxic:** Content that attacks, harasses, or discriminates towards an individual.

- **Violence:** Content that depicts violence and gore, or content that incites acts of violence.

## Benchmarks
All benchmarks were done with a threshold of 0.5, though the threshold can be increased or decreased to trade between precision and recall

### Sexual
| Model | Precision | Recall | F1 | ROC-AUC |
| --- | --- | --- | --- | --- |
| Mezzo Content Guard Large | 0.8396 | 0.8370 | **0.8383** | **0.9917** |
| Mezzo Content Guard Base | 0.8190 | 0.8227 | 0.8209 | 0.9895 |
| Mezzo Content Guard Small | 0.8376 | 0.7740 | 0.8045 | 0.9865 |
| KoalaAI/Text-Moderation | 0.1503 | **0.8423** | 0.2551 | 0.8770 |
| ifmain/ModerationBERT-En-02 | **0.8500** | 0.3591 | 0.5049 | 0.9373 |

### Violence
| Model | Precision | Recall | F1 | ROC-AUC |
| --- | --- | --- | --- | --- |
| Mezzo Content Guard Large | 0.7050 | 0.7827 | **0.7418** | 0.9921 |
| Mezzo Content Guard Base | **0.7330** | 0.7460 | 0.7394 | **0.9924** |
| Mezzo Content Guard Small | 0.6772 | 0.7269 | 0.7011 | 0.9883 |
| KoalaAI/Text-Moderation | 0.0136 | **1.0000** | 0.0269 | 0.8737 |
| ifmain/ModerationBERT-En-02 | 0.5414 | 0.3554 | 0.4291 | 0.9461 |

### Self-Harm
| Model | Precision | Recall | F1 | ROC-AUC |
| --- | --- | --- | --- | --- |
| Mezzo Content Guard Large | 0.8558 | 0.8711 | 0.8634 | **0.9888** |
| Mezzo Content Guard Base | 0.8524 | 0.8749 | **0.8635** | 0.9868 |
| Mezzo Content Guard Small | 0.8595 | 0.8401 | 0.8497 | 0.9853 |
| KoalaAI/Text-Moderation | 0.0923 | **0.8946** | 0.1673 | 0.9178 |
| ifmain/ModerationBERT-En-02 | **0.9174** | 0.4807 | 0.6309 | 0.9471 |

### Hate Speech
| Model | Precision | Recall | F1 | ROC-AUC |
| --- | --- | --- | --- | --- |
| Mezzo Content Guard Large | 0.8268 | 0.8229 | **0.8248** | **0.9865** |
| Mezzo Content Guard Base | 0.7991 | 0.8398 | 0.8190 | 0.9855 |
| Mezzo Content Guard Small | 0.8043 | 0.8055 | 0.8049 | 0.9829 |
| KoalaAI/Text-Moderation | 0.1000 | **0.9967** | 0.1817 | 0.9172 |
| ifmain/ModerationBERT-En-02 | **0.9111** | 0.3436 | 0.4990 | 0.9506 |

### Toxic
| Model | Precision | Recall | F1 | ROC-AUC |
| --- | --- | --- | --- | --- |
| Mezzo Content Guard Large | **0.7647** | 0.7459 | **0.7552** | **0.9778** |
| Mezzo Content Guard Base | 0.7456 | **0.7498** | 0.7477 | 0.9760 |
| Mezzo Content Guard Small | 0.7394 | 0.7162 | 0.7276 | 0.9720 |
| KoalaAI/Text-Moderation | 0.4884 | 0.6878 | 0.5712 | 0.9162 |
| ifmain/ModerationBERT-En-02 | 0.4781 | 0.6406 | 0.5475 | 0.9128 |

### Macro Averages
| Model | Precision | Recall | F1 | ROC-AUC |
| --- | --- | --- | --- | --- |
| Mezzo Content Guard Large | **0.7984** | 0.8119 | **0.8047** | **0.9874** |
| Mezzo Content Guard Base | 0.7898 | 0.8066 | 0.7981 | 0.9860 |
| Mezzo Content Guard Small | 0.7836 | 0.7725 | 0.7776 | 0.9830 |
| KoalaAI/Text-Moderation | 0.1689 | **0.8843** | 0.2404 | 0.9004 |
| ifmain/ModerationBERT-En-02 | 0.7396 | 0.4359 | 0.5223 | 0.9388 |

# Quickstart
Introducing our new custom [`mezzo-guard`](https://github.com/RyanStudioo/MezzoGuard) library that supports the Mezzo Prompt Guard and Mezzo Content Guard models. It offers automatic chunking, organized policies, and redactions.

Installation:
```bash
pip install mezzo-guard
```

```py
from mezzoguard import CONTENTGUARD
from mezzoguard.content_guard import ContentPolicy, Category, Guard

model = Guard(CONTENTGUARD.MEZZO_CONTENT_GUARD_BASE)
content_policy = ContentPolicy().add_threshold(Category.SEXUAL, 0.5)

sexual_query = "I want to fuck you"
benign_query = "I want to have a nice day"
violent_query = "I want to kill you"

result_1 = model.scan(text=sexual_query)
print(content_policy.evaluate(result_1))
# True

result_2 = model.scan(text=benign_query)
print(content_policy.evaluate(result_2))
# False

result_3 = model.scan(text=violent_query)
print(content_policy.evaluate(result_3))
# False
```

With `transformers`
```py
from transformers import pipeline

model = pipeline("text-classification", model="RyanStudio/Mezzo-Content-Guard-Base")


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

The following table shows the data distribution:

| Label       | Positives | % of Data |
|-------------|----------:|----------:|
| sexual      | 18,233    | 4.95%     |
| violence    | 5,440     | 1.48%     |
| self-harm   | 7,826     | 2.13%     |
| hate-speech | 31,597    | 8.59%     |
| toxic       | 33,088    | 8.99%     |

Mezzo Content Guard Large was the first model trained, and then further distilled into the Base and Small models. All models were trained with a max seq length of 256, which filtered out less than 1% of the data in the dataset

In initial experiments, RoBERTa-base was only able to hit a 71% macro f1 score, however with distillation, it is able to punch above its weight and hit a 79% macro f1 score.

While a "Divisive" Category was added in the Preview Model, targeting political and religious speech, it was deemed unnecessary and harmed the model's overall performance

# Limitations
- **Re-labelling**: Due to the training data being relabelled by Qwen3Guard and Qwen3.5, any inaccuracies from when these models were trained may be passed on to the model
- **Context Length**: Although a context length of 256 is more than enough for most applications, the model may suffer above it. Due to limitations of RoBERTa, the model can only scan texts up to 512 tokens in length, and chunking is required in lengths above it
- **Edge Cases**: A large majority of the open sourced datasets used were often dated, and may not take into account modern day slang words or more subtle bypasses, we recommend finetuning the model on your own usecase
- **English Only**: The RoBERTa models are primarily english-based models, and will suffer in multilingual contexts

# Future Iterations
This model, while suitable for most casual applications, it can still be significantly improved. 

Future Content Guard models may employ
- utilization of newer BERT-based models such as ModernBERT or Ettin-Encoder models to support larger contexts and improve general performance
- improvements to the base dataset in order to account for slang and edge cases, reducing False Positives and Negatives