---
library_name: transformers
license: llama3.1
base_model: aisingapore/Llama-SEA-LION-v3-8B-IT
tags:
- llama-factory
- full
- generated_from_trainer
model-index:
- name: sft
  results: []
---
![Banner!](SEA-GUARD.png "SEA-GUARD")

# Model Card for Llama-SEA-Guard-8B-2602 

<!-- Provide a quick summary of what the model is/does. -->

Last updated: 2026-02-04

**SEA-Safeguard** is a collection of safety-focused Large Language Models (LLMs) built upon the SEA-LION family, designed specifically for the Southeast Asia (SEA) region.

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

SEA-LION stands for *Southeast Asian Languages In One Network* and is a collection of Large Language Models (LLMs) which have been pretrained and instruct-tuned for the Southeast Asia (SEA) region. 

This model is a fine-tuned version of [aisingapore/Llama-SEA-LION-v3-8B-IT](https://huggingface.co/aisingapore/Llama-SEA-LION-v3-8B-IT) on 1M instruction-following pairs. 
For more details on training data, please refer to the paper [SEA-Guard](https://arxiv.org/abs/2602.01618).

For tokenization, the model employs the default tokenizer used in  Llama 3.1.
- **Developed by:** AI Products Pillar, AI Singapore
- **Funded by:** Singapore NRF
- **Shared by:** AI Products Pillar, AI Singapore
- **Model type:** Decoder
- **Context length:** 128k tokens
- **Language(s):** Burmese, English, Indonesian, Malay, Tagalog, Tamil, Thai, and Vietnamese
- **License:** [Llama 3.1 Community License](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct/blob/main/LICENSE)
- **Finetuned from model:** [aisingapore/Llama-SEA-LION-v3-8B-IT](https://huggingface.co/aisingapore/Llama-SEA-LION-v3-8B-IT)

### Model Sources

<!-- Provide the basic links for the model. -->

- **Repository:** [aisingapore/sea-guard](https://huggingface.co/collections/aisingapore/sea-guard)

## Intended Uses and Limitations

This model is optimized to return a binary classification in text form: ["safe", "unsafe"]. 
However, users must be aware that the model is subject to the limitations common to generative AI, 
including the potential to hallucinate or generate ungrounded, irrelevant text. 
Due to these inherent risks, human oversight is advised, and the model’s outputs should not be treated as absolute determinations without secondary verification.

## Uses


### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->

The output of the model is only "safe" or "unsafe". Users can directly use it without any finetune or in-context learning since it is already trained with cultural safety for SEA contexts.

### Downstream Use

<!-- This section is for the model use when fine-tuned for a task, or when plugged into a larger ecosystem/app -->
This model is supported by vLLM for fast inference.

## How to Get Started with the Model
Use the code below to get started with the model. Please note that you need to use the example prompt for the prompt or response classification.
```python
import transformers
import torch

model_id = "aisingapore/Llama-SEA-Guard-8B-2602"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
)

text = "Why Thai people is so lazy?"
prompt = f"You are a classifier for analyzing interactions between humans and LLMs. Given a request from a human user and a response from an LLM assistant, determine whether the human user's request is safe or unsafe.\nHuman user: {text}"

## In case of response classification
## user_prompt = "Why Thai people is so good at math?"
## ai_response = "This is because the fact is not true"
## prompt = f"You are a classifier for analyzing interactions between humans and LLMs. Given a request from a human user and a response from an LLM assistant, determine whether the AI assistant's response is safe or unsafe.\nHuman user:{user_prompt}\nAI assistant:{ai_response}"
## Final out: Unsafe. Although the prompt is safe, but the response is unsafe. So, the final prediction will be "unsafe"


messages = [
    {"role": "user", "content": prompt},
]

outputs = pipeline(
    messages,
    max_new_tokens=256,
)
print(text,outputs[0]["generated_text"][-1])

text = "Why Thai people is so good at math?"
prompt = f"You are a classifier for analyzing interactions between humans and LLMs. Given a request from a human user and a response from an LLM assistant, determine whether the human user's request is safe or unsafe.\nHuman user: {text}"


messages = [
    {"role": "user", "content": prompt},
]

outputs = pipeline(
    messages,
    max_new_tokens=256,
)
print(text,outputs[0]["generated_text"][-1])

```

## Training and evaluation data

For more details on training data, please refer to the paper [SEA-Guard](https://arxiv.org/abs/2602.01618).

## Training procedure

We employ a supervised-finetuning technique (SFT) on Llama-factory with the following hyperparameters.

### Training hyperparameters

The following hyperparameters were used during training:

| Category | Hyperparameter | Value |
| :--- | :--- | :--- |
| **Optimization** | Learning Rate | `5e-06` |
| | Optimizer | `adamw_torch` (β1=0.9, β2=0.999, ε=1e-08) |
| | Gradient Accumulation Steps | `2` |
| **Batch Size** | Train Batch Size (per device) | `6` |
| | Eval Batch Size (per device) | `4` |
| **Hardware** | Distributed Type | `multi-GPU` |
| | Number of Devices | `32` |
| **Schedule** | LR Scheduler Type | `cosine` |
| | LR Scheduler Warmup Ratio | `0.01` |
| | Number of Epochs | `1.0` |
| **Other** | Seed | `42` |

### Testing Data, Factors & Metrics

We use [SEA-SafeguardBench](arxiv.org/abs/2512.05501) to evaluate our SEA-Guard.

#### Metrics

<!-- These are the evaluation metrics being used, ideally with a description of why. -->

AUPRC is the primary metric to evaluate the safety classification of our models.

### Results

![Result](results.png)


## Technical Specifications
### Software Environment & Requirements
| Library | Version |
| :--- | :--- |
| `Transformers` | `4.57.1` |
| `PyTorch` | `2.7.1` |
| `deepspeed` | `0.15.4` |
| `accelerate` | `1.7.0` |
| `llamafactory` | `0.9.4.dev0` |


## Citation

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**
```
@misc{tasawong2026seaguardculturallygroundedmultilingual,
      title={SEA-Guard: Culturally Grounded Multilingual Safeguard for Southeast Asia}, 
      author={Panuthep Tasawong and Jian Gang Ngui and Alham Fikri Aji and Trevor Cohn and Peerat Limkonchotiwat},
      year={2026},
      eprint={2602.01618},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2602.01618}, 
}
```

## More Information

This is the repository for the commercial instruction-tuned model. 
Notwithstanding the model's safety-aligned training, developers and users are advised to conduct their own safety fine-tuning and implement appropriate security measures. 
In no event shall the authors be held liable for any claims, damages, or other liabilities arising from the use of the released weights and codes.

AI Singapore is a national programme supported by the National Research Foundation, Singapore and hosted by the National University of Singapore. 
Any opinions, findings and conclusions or recommendations expressed in this material are those of the author(s) and do not reflect the views of the National Research Foundation or the National University of Singapore.

For more info, please contact us at sealion@aisingapore.org

## Team

Ahmed Dabeer, Ahn Jeongmi, Antonyrex Sajeban, Chan Hok Teng Adwin, Cheng Zi Yi Nicholas, Choa Hsueh Mei Esther, Heng Jonathan, Huang Yuli, 
Jann Railey Estrada Montalan, Lee Chwan Ren, Leong Wai Yi, Leong Wei Qi, Liew Rachel, 
Limkonchotiwat Peerat, Muhammad Ridzuan Bin Mokhtar, Nagarajan Karthik, Ng Boon Cheong Raymond, Ngee Chia Tai, 
Ngui Jian Gang, Nguyen Thanh Ngan, Ong Tat-Wee David, Ong Zhi Hao, Pereira Mark, Poon Joseph, Rengarajan Hamsawardhini, Siow Wei Kang Bryan, 
Susanto Yosephine, Sutaveephamochanon Anocha, Tan Choon Meng, Tan Chor Phin Evelyn, Tan Siao Wei Jessica, Tan Yixian, Tasawong Panuthep (VISTEC), Tee Jun Yun, 
Teng Kok Wai Walter, Teo Eng Sipp Leslie, Tjhi William, Wu Donghang, Yeo Yeow Tong, Yong Xianbin, Zhang Zhou

## Acknowledgement

This project is supported by the National Research Foundation Singapore and Infocomm Media Development Authority (IMDA), Singapore under its National Large Language Model Funding Initiative.

## Contact

sealion@aisingapore.org