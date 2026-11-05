---
license: apache-2.0
language:
- ar
- en
pipeline_tag: text-generation
tags:
  - pytorch
library_name: transformers
---
# ALLaM-7B-Instruct-preview 

ALLaM is a series of powerful language models designed to advance Arabic Language Technology (ALT) developed by the National Center for Artificial Intelligence (NCAI) at the [Saudi Data and AI Authority (SDAIA)](https://sdaia.gov.sa/en/default.aspx). `ALLaM-AI/ALLaM-7B-Instruct-preview` is trained from scratch. Our pretraining from scratch recipe consists of two steps: training on 4T English tokens followed by training on 1.2T mixed Arabic/English tokens. This retains the English capabilities of the model without catastrophic forgetting, effectively transferring knowledge from one language distribution to another.

## Intended Use

`ALLaM` is specifically designed to expedite the research and development of ALT through Large Language Models (LLM). It serves as one of the foundational elements for building product offerings as well as facilitating experimental initiatives. 

The ALLaM series models are designed to be a component of a larger AI system, and it is important for developers to incorporate safety measures when creating these systems. These safety measures are crucial for ensuring a balance between effectiveness and security, as well as minimizing potential risks, such as those resulting from the integration of the model with external tools.

## Model Details

ALLaM is a family of LLMs specially trained for Arabic. The main two paths followed for pretraining are: 

- **ALLaM**: Pretraining models from scratch
- **ALLaM-Adapted/ALLaM-(\*\*)/(\*\*)-ALLaM**/: Continued training from open source/weight models

For this release, we are providing our instruction-tuned 7B parameter generative model pretrained from scratch.

Some parameters for this model are provided in the following table: 

| Size           | Context Length  | Pretraining Tokens | Instructions | Preference Pairs |
|----------------|-----------------|--------------------|--------------|------------------|
| 7B parameters  | 4096 tokens     |4T(en) + 1.2T(en+ar)| 7M           | 260K             |

#### Model Revisions Loading Tags:

- **Version 7b-alpha-v1.27.2.25 (Old Release)**: `revision = "v1"`
- **Version 7b-alpha-v2.33.0.30 (Newest Releas)**: `revision = "v2"`

## Model Description

- **Developed by:** National Center for Artificial Intelligence at [SDAIA](https://sdaia.gov.sa/en/default.aspx)
- **Model type:** Autoregressive Transformer
- **Language(s):** Arabic, English
- **License:** Please see the LICENSE file
- **Input:** Text
- **Output:** Text


## Training Details 

ALLaM-7B-Instruct-preview  is pretrained on a total of 5.2 trillion tokens in English and Arabic, Our training codebase is built on [NVIDIA/MegatronLM](https://github.com/NVIDIA/Megatron-LM). Average MFU during training was ~42%. We trained our model using bf16-mixed precision.


## Getting started


### System Prompt

It is important to note that this model is optimized to function without a predefined system prompt.
While Allam does not come with a default system prompt, it does provide the flexibility to add a custom system prompt.
For instance, a well crafted system prompt could be:

“You are ALLaM, a bilingual English and Arabic AI assistant.”
System prompts can also be in Arabic:

"أنت علام، مساعد ذكاء اصطناعي مطور من الهيئة السعودية للبيانات والذكاء الاصطناعي، تجيب على الأسئلة بطريقة مفيدة مع مراعاة القيم الثقافية المحلية."
Alternatively, users can get creative with their prompts, such as:

“You are an AI assistant who responds to everything like a pirate.”

The system prompt is integrated inside the tokenizer config (accessed via `apply_chat_template()` module). 


### Example Usages

The weights for ALLaM model checkpoints can be accessed via [HuggingFace transformers](https://github.com/huggingface/transformers) (tested with `transformers>=4.40.1`). The following code snippet demonstrates how to load the model and generate text using the `ALLaM-AI/ALLaM-7B-Instruct-preview` model.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
allam_model = AutoModelForCausalLM.from_pretrained("ALLaM-AI/ALLaM-7B-Instruct-preview") 
tokenizer = AutoTokenizer.from_pretrained("ALLaM-AI/ALLaM-7B-Instruct-preview") 
messages=[
    {"role": "user", "content": "كيف أجهز كوب شاهي؟"},
]
inputs = tokenizer.apply_chat_template(messages, tokenize=False)
inputs = tokenizer(inputs, return_tensors='pt', return_token_type_ids=False)
inputs = {k: v.to('cuda') for k,v in inputs.items()}
allam_model = allam_model.to('cuda')
response = allam_model.generate(**inputs, max_new_tokens=4096, do_sample=True, top_k=50, top_p=0.95, temperature=.6)
print(tokenizer.batch_decode(response, skip_special_tokens=True)[0])
```


## Ethical Considerations and Limitations

ALLaM is a generative model that comes with inherent uncertainties. Trials cannot encompass every possible use case. Hence, predicting ALLaM's responses in every context is not possible, leading on occasion to incorrect or biased outputs. Developers must conduct thorough safety evaluations and make specific adjustments to ensure the model is suitable for the intended purposes. 

*The output generated by this model is not considered a statement of NCAI, SDAIA, or any other organization.*

## Evaluation

### Automatic Benchmarks

#### Arabic Benchmarks
**Massive Multitask Language Understanding** (MMLU) is a collection of many multiple-choice evaluation questions sourced from various academic levels (elementary to college level). These questions are typically related to humanities, STEM, or social sciences. It was originally an English dataset, but other variants were developed for Arabic: 

<!-- - [Original English MMLU (MMLU-en)](https://github.com/hendrycks/test): A collection of 14,079 original English questions spanning 57 domains.  -->
- [Arabic MMLU](https://huggingface.co/datasets/MBZUAI/ArabicMMLU): A collection of 14,575 original Arabic questions spanning 40 domains published by MBZUAI. 
- [OpenAI MMLU-ar](https://huggingface.co/datasets/openai/MMMLU): A dataset comprising 14,042 questions, translated from the original MMLU benchmark published by OpenAI.

**Exams Arabic** ([Exams (Ar)](https://github.com/FreedomIntelligence/Arabic-eval/blob/main/LLM/benchmark_eval/benchmarks/EXAMS_Arabic/exam_test.jsonl)): A multiple choice question dataset with 537 samples, covering several domains e.g., Islamic studies, science, humanities, and physics. 

**Arabic Cultural Alignment** ([ACVA](https://huggingface.co/datasets/FreedomIntelligence/ACVA-Arabic-Cultural-Value-Alignment)): This dataset was generated by `gpt-3.5-turbo` and contains 8,710 True and False questions from 58 different areas.

**Education and Training Evaluation Commission** (ETEC): This dataset consists of Arabic-language multiple-choice questions, compiled by the ALLaM team in collaboration with [Saudi ETEC](https://acpd.etec.gov.sa/Home/index?csrt=5175167507218838843). It spans various educational levels, from elementary through post-college, with a total of 1,887  test samples. 

**IEN**: This dataset was curated from the Ministry of Education's (MOE) [IEN platform](https://www.ientv.edu.sa/ar), organized by grade, topic, and difficulty level. It comprehensively covers the entire Saudi curriculum from 1st grade through high school, with 9990 multiple-choice questions and 5823 true/false questions.

**GAT**: The General Aptitude Test (GAT) dataset consists of approximately 16,000 Arabic multiple-choice questions, representing various sections of [the Qiyas General Aptitude Test](https://www.etec.gov.sa/en/service/Generalabilitytest/servicegoal). The sections include algebra, reading comprehension, analogies, arithmetic, associations, comparisons, completions, contextual understanding, and geometry.

**AraPro**: A curated collection of 5,001 multiple-choice questions (MCQs) authored by our domain experts. The dataset spans various subjects, including mathematics, science, and other relevant fields, providing a diverse set of questions for evaluation purpose.

**AraMath**: AraMath consists of 605 MCQs derived from [ArMath](https://github.com/reem-codes/ArMATH), which includes mathematical word problems, that was transformed to MCQs internally. 

**Ar-IFEval**: an Arabic instruction-following (IF) evaluation dataset designed to automatically assess language models' compliance with specified instructions through verifiable methods. The dataset consists of 535 instances, each containing two to four verifiable instructions that can be validated using deterministic programming approaches.

All models were evaluated using our proprietary evaluation pipeline and [LM Evaluation Harness framework](https://github.com/EleutherAI/lm-evaluation-harness) to ensure fair comparisons. For API-based models, we used exact match evaluations of the generated outputs.

The evaluation scores of ALLaM can be found in JSON format [here](https://huggingface.co/ALLaM-AI/ALLaM-7B-Instruct-preview/tree/main/evaluation). 


| Model                       |AVG | ETEC <br>0 shot   | IEN-MCQ <br>0 shot   | IEN-TF <br>0 shot   | AraPro <br>0 shot   | AraMath <br>5 shot   | Ar-IFEval <br>(prompt strict) <br>0 shot   | Ar-IFEval <br>(inst strict) <br>0 shot   | ExamsAR <br>5 shot   | ACVA  <br> 5 shot   | Arabic MMLU <br>0 Shot   | Openai MMLU <br>0 shot   | GAT  <br>0 shot   | 
|:----------------------------|:----------|:---------|:-----------------|:----------------|:----------------|:-----------------|:-----------------------------------|:---------------------------------|:------------------|:--------------|:--------------------|:--------------------|:-----------------------------|
| ALLaM-7B-Instruct-preview   | 64.42     | 66.67    | **91.77**        | 82.95           | 69.71           | 66.78            | 31.34                              | 67.65                            | 51.58             | 76.33         | 67.78               | 55.91               | 44.53                        |
| AceGPT-v2-8B-Chat           | 52.67     | 56.81    | 77.01            | 75.91           | 63.51           | 41.49            | 10.26                              | 39.25                            | 51.96             | 72.69         | 57.02               | 49.99               | 36.15                        |
| AceGPT-v2-32B-Chat          | 62.23     | 64.81    | 81.6             | 80.35           | 67.19           | 64.46            | 25.75                              | 63.41                            | 55.31             | 71.57         | 68.3                | 60.8                | 43.21                        |
| jais-family-6p7b-chat       | 46.31     | 45.47    | 46.22            | 63.92           | 54.31           | 25.29            | 13.99                              | 52.97                            | 46.93             | 73.8          | 56.15               | 44.96               | 31.71                        |
| jais-family-13b-chat        | 49.14     | 48.65    | 62.95            | 68.68           | 57.53           | 26.61            | 17.16                              | 54.27                            | 45.07             | 71.18         | 58.14               | 47.73               | 31.72                        |
| jais-family-30b-16k-chat    | 52.54     | 53.31    | 74.88            | 68.76           | 62.79           | 41.49            | 16.6                               | 54.95                            | 49.72             | 60.08         | 62.04               | 50.98               | 34.85                        |
| jais-family-30b-8k-chat     | 53.19     | 53.52    | 72.76            | 70.65           | 61.27           | 33.39            | 16.79                              | 54.68                            | 50.28             | 74.47         | 63.11               | 50.9                | 36.44                        |
| jais-adapted-7b-chat        | 45.19     | 40.49    | 57.38            | 67.18           | 50.59           | 28.43            | 14.93                              | 54.27                            | 40.6              | 70.44         | 49.75               | 38.54               | 29.68                        |
| jais-adapted-13b-chat       | 51.86     | 48.12    | 69.65            | 71.85           | 59.07           | 37.02            | 23.32                              | 60.61                            | 48.23             | 67.78         | 56.42               | 46.83               | 33.4                         |
| jais-adapted-70b-chat       | 58.32     | 56.81    | 74.51            | 76.47           | 64.59           | 45.62            | 27.05                              | 65.05                            | 54.75             | 73.33         | 65.74               | 56.82               | 39.15                        |
| Qwen2.5-7B-Instruct         | 60.55     | 64.12    | 66.38            | 78.46           | 64.63           | 71.74            | 28.17                              | 65.19                            | 50.65             | 78.17         | 61.54               | 56.1                | 41.42                        |
| Qwen2.5-14B-Instruct        | 71.26     | 72.18    | 80.51            | 77.64           | 69.11           | 82.81            | 68.66                              | 86.76                            | 57.54             | 75.04         | 69.36               | 63.8                | 51.7                         |
| Qwen2.5-72B-Instruct        | **76.91** | **78.7** | 86.88            | **86.62**       | **74.69**       | **92.89**        | 67.72                              | 87.51                            | 60.71             | **79.92**     | **74.1**            | **73.59**           | **59.54**                    |
| Mistral-7B-Instruct-v0.3    | 43.05     | 35.67    | 53.59            | 63.4            | 43.85           | 27.11            | 30.41                              | 64.03                            | 34.08             | 60.25         | 45.27               | 32.3                | 26.65                        |
| Mistral-Nemo-Instruct-2407  | 53.79     | 49.28    | 68.43            | 71.78           | 57.61           | 40.0             | 35.82                              | 70.58                            | 47.49             | 76.92         | 55.97               | 46.15               | 25.44                        |
| Mistral-Small-Instruct-2409 | 51.11     | 40.96    | 60.64            | 63.66           | 47.73           | 44.46            | 51.12                              | 78.16                            | 38.73             | 68.93         | 50.43               | 39.63               | 28.82                        |
| Falcon3-7B-Instruct         | 41.3      | 37.52    | 52.65            | 57.63           | 41.47           | 56.53            | 8.58                               | 47.92                            | 31.84             | 58.98         | 42.08               | 32.36               | 27.99                        |
| Meta-Llama-3.1-8B-Instruct  | 54.08     | 45.68    | 59.23            | 71.7            | 52.51           | 34.38            | 51.87                              | 79.11                            | 52.51             | 69.93         | 56.43               | 44.67               | 30.9                         |
| Llama-3.3-70B-Instruct      | 71.43     | 68.84    | 79.6             | 78.81           | 70.49           | 70.91            | **70.9**                           | **88.6**                         | **65.74**         | 76.93         | 72.01               | 70.25               | 44.12                        |

Closed models evaluations:

| Model                                  | ETEC <br>0 shot   | IEN-MCQ <br>0 shot   | IEN-TF <br>0 shot   | AraPro <br>0 shot   | AraMath <br>5 shot   | ARIFEval <br>(prompt strict) <br>0 shot   | ARIFEval <br>(inst strict) <br>0 shot   | ExamsAR <br>5 shot   | ACVA  <br> 5 shot   | Arabicmmlu <br>0 Shot   | Openai mmlu <br>0 shot   | GAT 0 shot   |
|:---------------------------------------|:--------------|:-----------------|:----------------|:----------------|:-----------------|:----------------------------------|:--------------------------------|:-----------------|:-----------------------|:--------------------|:---------------------|:----------------------|
| Azureml GPT4o (gpt-4o-900ptu)   | 79.39         | **92.03**        | 88.97           | 80.86           | 83.47            | 70.9                              | 88.12                           | 61.82            | 72.51                  | 79.02               | **76.5**             | 62.65                 |
| Claude Sonnet 3.5 (claude-3-5-sonnet-20241022) | **85.9**      | 86.17            | **89.42**       | **81.46**       | 79.83            | 53.73                             | 80.14                           | **62.38**        | **80.42**              | 69.5                | 66.4                 | **68.89**             |
| gemini pro 1.5 (gemini-1.5-pro)          | 83.31         | 88.28            | 85.44           | 76.22           | **94.88**        | **74.81**                         | **90.17**                       | 58.1             | 75.17                  | **82.0**            | 64.8                 | 59.14                 |

#### English Benchmarks

| model                             |Avg        | AGIEval 0 Shot |   Arc (challenge) 0 Shot |   GPQA (main) 0 Shot |   Hendrycks <br>ethics 0 Shot |   Winogrande 0 Shot |   HellaSwag 0 Shot |   TriviaQa 5 Shot |   MMLU Pro<br>5 Shot |   Minerva Math <br>4 Shot |   MMLU 0 Shot |   TruthfulQA <br>(mc2) 0 Shot |   IFEval <br>(prompt strict)<br>0 Shot |   IFEval <br>(inst strict)<br>0 Shot |   GSM8k 5 Shot |
|:----------------------------------|:----------|:-----------------|:-----------------------|:--------------------------|:--------------------------|:--------------------|:-------------------|:------------------|:------------------|:----------------------|:--------------|:------------------------|:---------------------------------|:-------------------------------|:---------------|
| ALLaM-7B-Instruct-preview         | 46.85     | 41.99            | 51.28                  | 22.77                     | 73.17                     | 70.48               | 76.26              | 16.07             | 30.4              | 17.3                  | 59.6          | 46.67                   | 38.08                            | 50.0                           | 61.79          |
| AceGPT-v2-8B-Chat                 | 49.51     | 37.17            | 53.5                   | 25.67                     | 68.14                     | 73.72               | 79.21              | 67.65             | 37.38             | 17.58                 | 64.62         | 55.2                    | 23.48                            | 32.97                          | 56.86          |
| AceGPT-v2-32B-Chat                | 57.14     | 56.01            | 53.92                  | 32.8125                   | 66.23                     | 79.16               | 83.29              | 69.45             | 45.89             | 32.8                  | 74.03         | 59.18                   | 27.54                            | 40.89                          | 78.7           |
| jais-family-6p7b-chat             | 38.33     | 30.56            | 44.62                  | 23.21                     | 65.7                      | 62.43               | 72.05              | 29.74             | 23.3              | 2.56                  | 49.62         | 40.99                   | 14.05                            | 23.5                           | 54.36          |
| jais-family-13b-chat              | 42.62     | 30.31            | 47.87                  | 25.89                     | 65.91                     | 65.04               | 75.0               | 35.82             | 24.4              | 19.1                  | 51.91         | 40.57                   | 19.41                            | 30.82                          | 64.59          |
| jais-family-30b-16k-chat          | 45.15     | 31.85            | 48.46                  | 23.88                     | 69.44                     | 68.19               | 76.21              | 43.99             | 29.11             | 22.3                  | 58.5          | 44.78                   | 18.3                             | 29.14                          | 67.93          |
| jais-family-30b-8k-chat           | 47.59     | 36.65            | 48.38                  | 21.88                     | 69.28                     | 70.32               | 78.55              | 46.67             | 28.7              | 26.44                 | 57.46         | 49.49                   | 22.92                            | 37.05                          | 72.48          |
| jais-adapted-7b-chat              | 44.91     | 32.9             | 52.65                  | 23.88                     | 55.32                     | 71.74               | 79.39              | 63.89             | 24.38             | 15.34                 | 52.36         | 41.12                   | 22.0                             | 35.73                          | 58.07          |
| jais-adapted-13b-chat             | 47.7      | 36.49            | 54.18                  | 26.34                     | 65.73                     | 69.77               | 80.86              | 58.48             | 26.29             | 21.34                 | 55.66         | 42.27                   | 24.95                            | 36.57                          | 68.84          |
| jais-adapted-70b-chat             | 53.49     | 39.96            | 59.56                  | 20.98                     | 70.8                      | 77.27               | 84.06              | 68.64             | 37.25             | 27.72                 | 65.23         | 44.49                   | 31.61                            | 44.0                           | 77.26          |
| Qwen2.5-7B-Instruct               | 54.68     | 59.2             | 51.28                  | 26.56                     | 73.76                     | 69.38               | 79.55              | 50.59             | 44.92             | 12.04                 | 70.56         | 58.93                   | 57.3                             | 68.23                          | 43.29          |
| Qwen2.5-14B-Instruct              | 62.37     | 66.32            | 62.12                  | 25.89                     | 76.19                     | 75.77               | 84.36              | 59.47             | 52.44             | 23.04                 | 78.93         | 69.01                   | 52.13                            | 64.03                          | 83.47          |
| Qwen2.5-72B-Instruct              | **70.06** | **71.09**        | **63.48**              | 25.67                     | 78.33                     | 76.24               | **87.41**          | 70.9              | **62.77**         | **54.04**             | **83.44**     | **69.54**               | 67.65                            | 77.1                           | **93.25**      |
| Mistral-7B-Instruct-v0.3          | 51.98     | 36.45            | 58.87                  | 23.21                     | 72.58                     | 73.95               | 82.93              | 67.97             | 33.18             | 13.44                 | 59.74         | 59.69                   | 42.51                            | 54.8                           | 48.37          |
| Mistral-Nemo-Instruct-2407        | 54.0      | 39.65            | 59.04                  | 24.33                     | 67.86                     | 74.66               | 82.35              | 72.77             | 44.27             | 29.62                 | 65.56         | 54.88                   | 30.13                            | 38.97                          | 71.95          |
| Mistral-Small-Instruct-2409       | 61.65     | 40.76            | 60.49                  | 25.89                     | 72.27                     | 78.53               | 85.35              | 79.11             | 47.47             | 39.42                 | 69.42         | 56.35                   | 58.23                            | 68.35                          | 81.43          |
| Falcon3-7B-Instruct               | 58.04     | 43.84            | 59.47                  | **33.71**                 | 70.39                     | 70.09               | 78.43              | 51.98             | 46.73             | 30.76                 | 68.14         | 55.53                   | 56.01                            | 68.59                          | 78.92          |
| Meta-Llama-3.1-8B-Instruct        | 56.5      | 42.39            | 55.12                  | 27.23                     | 66.69                     | 73.95               | 79.28              | 70.05             | 40.641622         | 34.26                 | 67.96         | 54.05                   | 44.36                            | 58.51                          | 76.5           |
| Llama-3.3-70B-Instruct            | 67.7      | 55.44            | 63.4                   | 25.89                     | **81.05**                 | **79.24**           | 84.39              | **81.7**              | 60.51             | 46.42                 | 81.99         | 60.91                   | **63.22**                           | **72.78**                          | 90.83          |

### MT-bench

**Multi-Turn Bench** (MT-Bench): A challenging multi-turn benchmark that uses GPT-4o as a judge. MT-bench comprises 80 questions from 8 domains. Each question is presented to the model and the responses are submitted to GPT-4o to assign scores to each response. The judge returns a score for the first and second turn separately.
This dataset was also automatically translated to Arabic and manually verified and culturally aligned.

| Model               | AR Average | AR Turn 1 | AR Turn 2 | EN Average | EN Turn 1 | EN Turn 2 |
|---------------------|------------|-----------|-----------|------------|-----------|-----------|
| ALLaM-7B-Instruct-preview     | 5.9 | **6.93**| 4.88 | 6.5 | 7.49 | 5.15 |
| AceGPT-v1.5-13B-Chat   | 4.61 | 5.28 | 	3.93 | 4.86 | 5.56 | 4.17 |
| AceGPT-v2-32B-Chat     |5.43 | 6.61 | 4.26 | **6.5** | **7.41** | **5.58** |
| jais-family-13b-chat    | 4.89 | 5.37 | 4.41 | 4.77 | 5.57 | 3.97
| jais-family-30b-16k-chat | 4.87 | 5.50 | 4.25  | 5.13  | 5.86 | 4.4  |
| jais-adapted-70b-chat  | 5.86 | 6.33 | **5.38** | 5.88 | 6.41 | 5.36 |

## Citation

If you found this work helpful or used any part of this work, please include the following citation:

```
@inproceedings{
    bari2025allam,
    title={{ALL}aM: Large Language Models for Arabic and English},
    author={M Saiful Bari and Yazeed Alnumay and Norah A. Alzahrani and Nouf M. Alotaibi and Hisham Abdullah Alyahya and Sultan AlRashed and Faisal Abdulrahman Mirza and Shaykhah Z. Alsubaie and Hassan A. Alahmed and Ghadah Alabduljabbar and Raghad Alkhathran and Yousef Almushayqih and Raneem Alnajim and Salman Alsubaihi and Maryam Al Mansour and Saad Amin Hassan and Dr. Majed Alrubaian and Ali Alammari and Zaki Alawami and Abdulmohsen Al-Thubaity and Ahmed Abdelali and Jeril Kuriakose and Abdalghani Abujabal and Nora Al-Twairesh and Areeb Alowisheq and Haidar Khan},
    booktitle={The Thirteenth International Conference on Learning Representations},
    year={2025},
    url={https://openreview.net/forum?id=MscdsFVZrN}
}
```

Apart from the authors of the paper, the ALLaM team is rapidly growing, supported by a large and talented group of in-house professionals, whom we gratefully acknowledge here.

### Acknowledgment

This release is funded by **Saudi Data & AI Authority**. We thank **Mishari Almishari** and **Yaser Alonaizan** for leading the **ALLaM** project. We list below the different teams that supported the development of **ALLaM**.

#### Member of the Technical Staff:

Alhanoof Althnian, Iman Albilali, Jubair Sheikh, Ibrahim Mammu, Ghadah Alsaif, Abdulhameed Alothaimeen, Hadeel Alnegheimish, Emad Alghamdi, Khalid Almubarak, Atheer Al-Barqi, Batool Al-Otaibi, Muhammad Al-Hajji, Abdulraouf Al-Maasoumi, Abdulmajeed Alrowithi, Faisal Qarah, Sakhar Alkhereyf, Arwa Omayrah, Mohammed Al-Saleem, Amal Al-Shammari, Maryam Saif, Raeda Al-Marzooq, Lamyaa Alqhatani, Anas Al-Manie, Ghassan Al-Ward, Shahad Al-Zaidi, Batool Al-Ghoraibi, Alanoud Al-Shammari, Saad Alrazoq.

#### Data Acquisition, Management and Engineering:

Ali Alotaibi, Abdulrahman Alsaudi, Abdulaziz Asheyban, Areej Alokaili, Norah Alangari, Hamad Alnamazi, Fatima Alsalman, Saleh Alrusayyis, Moneerah Alballa, Omar AlGhamdi, Raneem Alqahtani, Amirah Albinhar, Nour Al-Aldahan, Khalid Alharbi, Hanouf Aljlayl, Fatimah Alzubaidi, Lama Aldossary, Rania Alzahrani, Shoug Alkhalaf.

#### Development and Infrastructure:

Saud AlHamoud, Fahad Alothaimeen, Ahmed Alrowatie, Saad Alajlan, Hassan Almitib, Abdinasir Mohamed, Sultan Alotaibi, Mohammed Alanazi, Mohammed Alsharani, Khalid Aljandal, Faisal Abulnaja, Ahmed Alosaimi, Muhannad Abu Hussain, Nasser Almoffarej, Muhammad Al-Hashem, Ahmed Al-Ghamdi, Amer Ashraf, Abeer Al-khars, Nawaf Babgy, Fevicks Kumar, Islam Gamal, Layla Al-Mutairi, Shroq Al-Ghamdi, Amjad Al-Zahrani, Tjad Clark, Ali bjorn, Meshari Alyami, Abdulrahman Bahkali, Reema Alomair.

#### Project Management:

Naif Shalhoub, Esshaq Almotawa, Sara AlRasheed, Mohammed Alshaalan, Mohammed Albreeh, Nezar Kaaki, Muna Alsahli, Abdullah Aldahami, Faisal Al-Tamimi, Tariq Alrouqi, Sahar Alghamdi, Raghad Abuznadah, Naif Almohammed, Oraib Alhemmyraine, Sarah Binlibdah, Shrooq Almohamdi.

#### Human Evaluators:

Amal Almohammadi, Badr almalki, Amjad Alsaeed, Alhanouf Alotaibi, Rajaa Almalki, Maryam Alasmari, Maha Awaji, Fatima Alshehri, Maryam ALshuwaiman, Ebtesam Alzahrani, Yasmeen Al-gahtani, Atheer Almusailem, Rehab Almalky, Shahad Alsulami, Abdullah Albalawi, Abeer Alqahtani, Lama Alrajeh, Shahad Aqeel, Yasir Alharbi, Rassil Al-Otaibi, Khulud Alawadh, Fatimah Almutairi, Suad Alkhamshi, Abdulrahman Alasmari, Goot Alqahtani, alhanouf Alfoaim, Rawan Aljohani, Aisha Almutairi.
