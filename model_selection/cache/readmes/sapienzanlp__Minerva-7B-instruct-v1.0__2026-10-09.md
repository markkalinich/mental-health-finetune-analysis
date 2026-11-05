---
license: apache-2.0
pipeline_tag: text-generation
language:
- it
- en
tags:
- sft
- dpo
base_model:
- sapienzanlp/Minerva-7B-base-v1.0
datasets:
- HuggingFaceH4/ultrafeedback_binarized
- Babelscape/ALERT
- efederici/evol-dpo-ita
inference:
  parameters:
    temperature: 0.4
    do_sample: true
widget:
- text: Chi sei?
  example_title: Example 1
library_name: transformers
---

<div style="text-align: center; display: flex; flex-direction: column; align-items: center;">
    <img src="https://huggingface.co/sapienzanlp/Minerva-7B-instruct-v1.0/resolve/main/minerva-logo.png" style="max-width: 550px; height: auto;"> 
</div>

# Model Card for Minerva-7B-instruct-v1.0

Minerva is the first family of **LLMs pretrained from scratch on Italian** developed by [Sapienza NLP](https://nlp.uniroma1.it)
in the context of the [Future Artificial Intelligence Research (FAIR)](https://fondazione-fair.it/) project, in collaboration with [CINECA](https://www.cineca.it/) and with additional contributions from [Babelscape](https://babelscape.com) and the [CREATIVE](https://nlp.uniroma1.it/creative/) PRIN Project.
Notably, the Minerva models are truly-open (data and model) Italian-English LLMs, with approximately half of the pretraining data 
including Italian text.

* [Minerva LLMs - website](https://nlp.uniroma1.it/minerva/)
* [Try it out!](https://minerva-llm.org)

## Description

This is the model card for **Minerva-7B-instruct-v1.0**, a 7 billion parameter model trained on almost 2.5 trillion tokens (1.14 trillion in Italian, 
1.14 trillion in English and 200 billion in code).

This model is part of the Minerva LLM family:

* [Minerva-350M-base-v1.0](https://huggingface.co/sapienzanlp/Minerva-350M-base-v1.0)
* [Minerva-1B-base-v1.0](https://huggingface.co/sapienzanlp/Minerva-1B-base-v1.0)
* [Minerva-3B-base-v1.0](https://huggingface.co/sapienzanlp/Minerva-3B-base-v1.0)
* [Minerva-7B-base-v1.0](https://huggingface.co/sapienzanlp/Minerva-7B-base-v1.0)
* [Minerva-7B-instruct-v1.0](https://huggingface.co/sapienzanlp/Minerva-7B-instruct-v1.0)

## 🚨⚠️🚨 Bias, Risks, and Limitations 🚨⚠️🚨

*This section identifies foreseeable harms and misunderstandings.*

This is a chat foundation model, subject to model alignment and safety risk mitigation strategies. However, the model may still:

-   Overrepresent some viewpoints and underrepresent others
-   Contain stereotypes
-   Contain [personal information](#personal-data-and-information)
-   Generate:
    -   Racist and sexist content
    -   Hateful, abusive, or violent language
    -   Discriminatory or prejudicial language
    -   Content that may not be appropriate for all settings, including sexual content
-   Make errors, including producing incorrect information or historical facts as if it were factual
-   Generate irrelevant or repetitive outputs

We are aware of the biases and potential problematic/toxic content that current pretrained large language models exhibit: more specifically, as probabilistic models of (Italian and English) languages, they reflect and amplify the biases of their training data.
For more information about this issue, please refer to our survey:

* [Biases in Large Language Models: Origins, Inventory, and Discussion](https://dl.acm.org/doi/full/10.1145/3597307)

## How to use Minerva with Hugging Face transformers

```python
import transformers
import torch

model_id = "sapienzanlp/Minerva-7B-instruct-v1.0"

# Initialize the pipeline.
pipeline = transformers.pipeline(
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
)

# Input text for the model.
input_conv = [{"role": "user", "content": "Qual è la capitale dell'Italia?"}]

# Compute the outputs.
output = pipeline(
  input_conv,
  max_new_tokens=128,
)

output
```

    [{'generated_text': [{'role': 'user', 'content': "Qual è la capitale dell'Italia?"}, {'role': 'assistant', 'content': "La capitale dell'Italia è Roma."}]}]
    

## Model Architecture

Minerva-7B-base-v1.0 is a Transformer model based on the [Mistral](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1) architecture.
Please look at the configuration file for a detailed breakdown of the hyperparameters we chose for this model.

The Minerva LLM family is composed of:

| Model Name | Tokens | Layers | Hidden Size | Attention Heads | KV Heads | Sliding Window | Max Context Length |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Minerva-350M-base-v1.0 | 70B (35B it + 35B en) | 16 | 1152 | 16 | 4 | 2048 | 16384 |
| Minerva-1B-base-v1.0 | 200B (100B it + 100B en) | 16 | 2048 | 16 | 4 | 2048 | 16384 |
| Minerva-3B-base-v1.0 | 660B (330B it + 330B en) | 32 | 2560 | 32 | 8 | 2048 | 16384 |
| Minerva-7B-base-v1.0 | 2.48T (1.14T it + 1.14T en + 200B code) | 32 | 4096 | 32 | 8 | None | 4096 |

## Model Training

Minerva-7B-base-v1.0 was trained using [llm-foundry 0.8.0](https://github.com/riccorl/llm-foundry) from [MosaicML](https://mosaicml.com/). The hyperparameters used are the following:

| Model Name | Optimizer | lr | betas | eps | weight decay | Scheduler | Warmup Steps | Batch Size (Tokens) | Total Steps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Minerva-350M-base-v1.0 | Decoupled AdamW | 2e-4 | (0.9, 0.95) | 1e-8 | 0.0 | Cosine | 2% | 4M | 16,690 |
| Minerva-1B-base-v1.0 | Decoupled AdamW | 2e-4 | (0.9, 0.95) | 1e-8 | 0.0 | Cosine | 2% | 4M | 47,684 |
| Minerva-3B-base-v1.0 | Decoupled AdamW | 2e-4 | (0.9, 0.95) | 1e-8 | 0.0 | Cosine | 2% | 4M | 157,357 |
| Minerva-7B-base-v1.0 | AdamW | 3e-4 | (0.9, 0.95) | 1e-5 | 0.1 | Cosine | 2000 | 4M | 591,558 |

### SFT Training

The SFT model was trained using [Llama-Factory](https://github.com/hiyouga/LLaMA-Factory). The data mix was the following:

| Dataset                              | Source                                                                 | Code     | English | Italian |
|--------------------------------------|------------------------------------------------------------------------|----------|---------|---------|
| Glaive-code-assistant                | [Link](https://huggingface.co/datasets/glaiveai/glaive-code-assistant)  | 100,000  | 0       | 0       |
| Alpaca-python                        | [Link](https://huggingface.co/datasets/Vezora/Tested-143k-Python-Alpaca) | 20,000   | 0       | 0       |
| Alpaca-cleaned                       | [Link](https://huggingface.co/datasets/yahma/alpaca-cleaned)            | 0        | 50,000  | 0       |
| Databricks-dolly-15k                 | [Link](https://huggingface.co/datasets/databricks/databricks-dolly-15k) | 0        | 15,011  | 0       |
| No-robots                            | [Link](https://huggingface.co/datasets/HuggingFaceH4/no_robots)         | 0        | 9,499   | 0       |
| OASST2                               | [Link](https://huggingface.co/datasets/OpenAssistant/oasst2)            | 0        | 29,000  | 528     |
| WizardLM                             | [Link](https://huggingface.co/datasets/WizardLMTeam/WizardLM_evol_instruct_70k) | 0  | 29,810  | 0       |
| LIMA                                 | [Link](https://huggingface.co/datasets/GAIR/lima?row=0)                 | 0        | 1,000   | 0       |
| OPENORCA                              | [Link](https://huggingface.co/datasets/Open-Orca/OpenOrca)              | 0        | 30,000  | 0       |
| Ultrachat                             | [Link](https://huggingface.co/datasets/HuggingFaceH4/ultrachat_200k)     | 0        | 50,000  | 0       |
| MagpieMT                             | [Link](https://huggingface.co/datasets/Magpie-Align/Magpie-Pro-MT-300K-v0.1) | 0     | 30,000  | 0       |
| Tulu-V2-Science                      | [Link](https://huggingface.co/datasets/allenai/tulu-v2-sft-mixture)    | 0        | 7,000   | 0       |
| Aya_datasets                         | [Link](http://CohereForAI/aya_dataset)                                  | 0        | 3,944   | 738     |
| Tower-blocks_it                      | [Link](https://huggingface.co/datasets/sapienzanlp/tower_blocks-v0.2_it) | 0        | 0       | 7,276   |
| Bactrian-X                           | [Link](https://huggingface.co/datasets/MBZUAI/Bactrian-X)               | 0        | 0       | 67,000  |
| Magpie (*Translated by us*)          | [Link](https://huggingface.co/datasets/sapienzanlp/it-Magpie-Llama-3.1-Pro-300K-Filtered-easy)       | 0        | 0       | 59,070  |
| Everyday-conversations (*Translated by us*) | [Link](https://huggingface.co/datasets/sapienzanlp/it-everyday-conversations-llama3.1-2k-TowerInstruct-Mistral-7B-v0.2)         | 0        | 0       | 2,260   |
| alpaca-gpt4-it                       | [Link](https://huggingface.co/datasets/efederici/alpaca-gpt4-it)        | 0        | 0       | 15,000  |
| capybara-claude-15k-ita              | [Link](https://huggingface.co/datasets/efederici/capybara-claude-15k-ita) | 0       | 0       | 15,000  |
| Wildchat                             | [Link](https://huggingface.co/datasets/allenai/WildChat-1M)            | 0        | 0       | 5,000   |
| GPT4_INST                            | [Link](https://huggingface.co/datasets/DeepMount00/GPT-4o-ITA-INSTRUCT) | 0        | 0       | 10,000  |
| Italian Safety Instructions                       | -                                                                      | 0        | 0       | 21,426  |
| Italian Conversations                     | -                                                                      | 0        | 0       | 4,843   |

For more details, please check [our tech page](https://nlp.uniroma1.it/minerva/blog#from-a-base-model-to-an-instruct-model).

### Online DPO Training

This model card is for our DPO model. Direct Preference Optimization (DPO) is a method that refines models based on user feedback, similar to Reinforcement Learning from Human Feedback (RLHF), but without the complexity of reinforcement learning. Online DPO further improves this by allowing real-time adaptation during training, continuously refining the model with new feedback. For training this model, we used the [Hugging Face TRL](https://github.com/huggingface/trl) library and Online DPO, with the [Skywork/Skywork-Reward-Llama-3.1-8B-v0.2](https://huggingface.co/Skywork/Skywork-Reward-Llama-3.1-8B-v0.2) model as the judge to evaluate and guide optimization. For this stage we used just the prompts from HuggingFaceH4/ultrafeedback_binarized (English), efederici/evol-dpo-ita (Italian) and Babelscape/ALERT translated to Italian, with additional manually curated data for safety.

For more details, please check [our tech page](https://nlp.uniroma1.it/minerva/blog#from-a-base-model-to-an-instruct-model).

## Model Evaluation

For Minerva's evaluation process, we utilized [ITA-Bench](https://huggingface.co/collections/sapienzanlp/ita-bench-italian-benchmarks-for-llms-66337ca59e6df7d7d4933896), a new evaluation suite to test the capabilities of Italian-speaking models. 
ITA-Bench is a collection of 18 benchmarks that assess the performance of language models on various tasks, including scientific knowledge, 
commonsense reasoning, and mathematical problem-solving.

<div style={{ display: 'flex', justifyContent: 'space-around' }}>
    <img src="https://huggingface.co/sapienzanlp/Minerva-7B-instruct-v1.0/resolve/main/Minerva%20LLMs%20Results.png" alt="Results on instructed models" style={{ width: '45%' }}></img>
    <img src="https://huggingface.co/sapienzanlp/Minerva-7B-instruct-v1.0/resolve/main/Minerva%20LLMs%20Results%20(1).png" alt="Results on instructed models" style={{ width: '45%' }}></img>
</div>

<!-- **Italian** Data: -->
<!-- | Task | Accuracy |
| --- | --- | -->
<!-- | [xcopa](https://huggingface.co/datasets/xcopa) (0-shot) | 0.694 |
| [Hellaswag](https://huggingface.co/datasets/alexandrainst/m_hellaswag) (5-shot) | 0.5293 |
| [Belebele](https://huggingface.co/datasets/facebook/belebele) (5-shot) | 0.2333 |
| [TruthfulQA MC 1](https://huggingface.co/datasets/alexandrainst/m_truthfulqa) (0-shot) | 0.2363 |
| [TruthfulQA MC 2](https://huggingface.co/datasets/alexandrainst/m_truthfulqa) (0-shot) | 0.3731 |
| [M MMLU](https://huggingface.co/datasets/alexandrainst/m_mmlu) (5-shot) | 0.2612 |
| [arc challenge](https://huggingface.co/datasets/alexandrainst/m_arc) (5-shot) | 0.3268 | -->

<!-- **English** Data: -->
<!-- | Task | Accuracy |
| --- | --- | -->
<!-- | [Hellaswag](https://huggingface.co/datasets/Rowan/hellaswag) (5-shot) | 0.6168 |
| [piqa](https://huggingface.co/datasets/piqa) (5-shot) | 0.7535 |
| [sciq](https://huggingface.co/datasets/sciq) (5-shot) | 0.925 |
| [Belebele](https://huggingface.co/datasets/facebook/belebele) (5-shot) | 0.2278 |
| [TruthfulQA MC 1](https://huggingface.co/datasets/truthful_qa) (0-shot) | 0.2142 |
| [TruthfulQA MC 2](https://huggingface.co/datasets/truthful_qa) (0-shot) | 0.3643 |
| [M MMLU](https://huggingface.co/datasets/alexandrainst/m_mmlu) (5-shot) | 0.263 |
| [arc challenge](allenai/ai2_arc) (5-shot) | 0.3319 |
| [arc easy](allenai/ai2_arc) (5-shot) | 0.6540 | -->

<!-- ## Training Data

Minerva-7B-base-v1.0 is trained on 1.14T Italian tokens, 1.14T English tokens, and 200B code tokens.

The training data is a mixture of the following datasets:

| Dataset | Tokens | Language | Epochs |
| --- | --- | --- | --- |
| RedPajama-Data-V2 | 687,952,502,784 | Italian | 1.3 |
| CulturaX | 158,201,876,480 | Italian | 1.5 |
| Wikipedia | 1,265,135,616 | Italian | 1.0 |
| Gutenberg/Wikisource | 147,017,728 | Italian | 2.0 |
| EurLex | 1,647,013,888 | Italian | 1.0 |
| Gazzetta Ufficiale | 1,654,013,952| Italian | 1.0 |
| FineWeb | 1,076,406,624,256 | English | 1.0 |
| Wikipedia | 5,259,501,568 | English | 1.0 |
| ArXiv | 33,231,106,048 | English | 1.0 |
| Gutenberg | 6,947,893,248 | English | 1.0 |
| StackExchange | 22,069,268,480 | English | 1.0 |
| The Stack V2 | 200,754,900,992 | Code | 1.0 | -->

<!-- We have extracted some statistics on Italian (115B tokens) and English (210B tokens) documents from CulturaX on the selected sources:

*Proportion of number of tokens per domain (Italian)*
<img src="https://github.com/Andrew-Wyn/images/blob/master/minerva/top_25_url_tokens_proportion_culturax_it.png?raw=true" alt="italian-tok-counts" border="0" width="1800px">

*Proportion of number of tokens per domain (English)*
<img src="https://github.com/Andrew-Wyn/images/blob/master/minerva/top_25_url_tokens_proportion_culturax_en.png?raw=true" alt="english-tok-counts" border="0" width="1800px">
 -->
## Tokenizer Fertility

The tokenizer fertility measures the average amount of tokens produced per tokenized word.
A tokenizer displaying high fertility values in a particular language typically indicates that it segments words in that language extensively.
The tokenizer fertility is strictly correlated with the inference speed of the model with respect to a specific language, 
as higher values mean longer sequences of tokens to generate and thus lower inference speed.

**Fertility computed over a sample of Cultura X (CX) data and Wikipedia (Wp):**

| Model | Voc. Size | Fertility IT (CX) | Fertility EN (CX) | Fertility IT (Wp) | Fertility EN (Wp) |
| --- | --- | --- |--- | --- |--- |
| Mistral-7B-v0.1 | 32000 | 1.87 | 1.32 | 2.05 | 1.57 |
| gemma-7b | 256000 | 1.42 | 1.18 | 1.56 | 1.34 |
| Minerva-3B-base-v1.0 | 32768 | 1.39 | 1.32 | 1.66 | 1.59 |
| Minerva-7B-base-v1.0 | 51200 | 1.32 | 1.26 | 1.56 | 1.51 |

<!-- ## Notice

Minerva-7B-base-v1.0 is a pretrained base model and, therefore, has no moderation mechanisms.
 -->
## The Sapienza NLP Team

### 🧭 Project Lead and Coordination
* __Roberto Navigli__: project lead and coordination; model analysis, evaluation and selection, safety and guardrailing, conversations.

### 🤖 Model Development
* __Edoardo Barba__: pre-training, post-training, data analysis, prompt engineering.
* __Simone Conia__: pre-training, post-training, evaluation, model, and data analysis.
* __Pere-Lluís Huguet Cabot__: data processing, filtering,g and deduplication, preference modeling.
* __Luca Moroni__: data analysis, evaluation, post-training.
* __Riccardo Orlando__: pre-training process and data processing.

#### 👮 Safety and Guardrailing
* __Stefan Bejgu__: safety and guardrailing.
* __Federico Martelli__: synthetic prompt generation, model and safety analysis.
* __Ciro Porcaro__: additional safety prompts.
* __Alessandro Scirè__: safety and guardrailing.
* __Simone Stirpe__: additional safety prompts.
* __Simone Tedeschi__: English dataset for safety evaluation.

### Special thanks for their support

* Giuseppe Fiameni, Nvidia
* Sergio Orlandini, CINECA

## Acknowledgments

This work was funded by the PNRR MUR project [PE0000013-FAIR](https://fondazione-fair.it) and the [CREATIVE](https://nlp.uniroma1.it/creative/) PRIN project, which is funded by the MUR Progetti di
Rilevante Interesse Nazionale programme (PRIN 2020).
We acknowledge the [CINECA](https://www.cineca.it) award "IscB_medit" under the ISCRA initiative for the availability of high-performance computing resources and support.
