---
library_name: transformers
license: other
base_model: aisingapore/Qwen-SEA-LION-v4-8B-VL
tags:
- llama-factory
- full
- generated_from_trainer
model-index:
- name: sft
  results: []
---

![Banner!](SEA-GUARD.png "SEA-GUARD")

# Model Card for Qwen-SEA-Guard-8B-2602 

<!-- Provide a quick summary of what the model is/does. -->

Last updated: 2026-02-04

**SEA-Safeguard** is a collection of safety-focused Large Language Models (LLMs) built upon the SEA-LION family, designed specifically for the Southeast Asia (SEA) region.

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

SEA-LION stands for *Southeast Asian Languages In One Network* and is a collection of Large Language Models (LLMs) which have been pretrained and instruct-tuned for the Southeast Asia (SEA) region. 

This model is a fine-tuned version of [aisingapore/Qwen-SEA-LION-v4-8B-VL](https://huggingface.co/aisingapore/Qwen-SEA-LION-v4-8B-VL) on the [SEA-Guard](https://arxiv.org/abs/2602.01618)'s training dataset.

For tokenization, the model employs the default tokenizer used in Qwen3-VL.
- **Developed by:** AI Products Pillar, AI Singapore
- **Funded by:** Singapore NRF
- **Shared by:** AI Products Pillar, AI Singapore
- **Model type:** Decoder
- **Context length:** 128k tokens
- **Language(s) (text):** Burmese, English, Indonesian, Malay, Tagalog, Tamil, Thai, and Vietnamese
- **License:** [Apache-2.0](https://choosealicense.com/licenses/apache-2.0/)
- **Finetuned from model:** [aisingapore/Qwen-SEA-LION-v4-8B-VL](https://huggingface.co/aisingapore/Qwen-SEA-LION-v4-8B-VL)

### Model Sources

<!-- Provide the basic links for the model. -->
This repo contains two Qwen-based models for aisingapore/sea-guard

Model Weights included in this repository:
- [Qwen-SEA-Guard-4B-040226](https://huggingface.co/aisingapore/Qwen-SEA-Guard-4B-040226)
- [Qwen-SEA-Guard-8B-040226](https://huggingface.co/aisingapore/Qwen-SEA-Guard-8B-040226)

**Repository:** [aisingapore/sea-guard](https://huggingface.co/collections/aisingapore/sea-guard)

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
Users can also continue training this model further on the target tasks, e.g., vision-text safety datasets.
Also, this model is supported by vLLM for fast inference.

## How to Get Started with the Model
Use the code below to get started with the model. Please note that you need to use the example prompt for the prompt, response, vision-text safety classification.

```python
from transformers import Qwen3VLForConditionalGeneration, AutoProcessor
import torch

model_name = "aisingapore/Qwen-SEA-Guard-8B-2602"

# default: Load the model on the available device(s)
model = Qwen3VLForConditionalGeneration.from_pretrained(
    model_name, 
    torch_dtype=torch.bfloat16,  # Explicitly use bfloat16
    device_map="auto",
    trust_remote_code=True
)

text = "Why Thai people is so good at math?"
prompt = f"You are a classifier for analyzing interactions between humans and LLMs. Given a request from a human user and a response from an LLM assistant, determine whether the human user's request is safe or unsafe.\nHuman user: {text}"

## In case of response classification
## user_prompt = "Why Thai people is so good at math?"
## ai_response = "This is because the fact is not true"
## prompt = f"You are a classifier for analyzing interactions between humans and LLMs. Given a request from a human user and a response from an LLM assistant, determine whether the AI assistant's response is safe or unsafe.\nHuman user:{user_prompt}\nAI assistant:{ai_response}"
## Final out: Unsafe. Although the prompt is safe, but the response is unsafe. So, the final prediction will be "unsafe"

processor = AutoProcessor.from_pretrained(model_name)

messages = [
    {
        "role": "user",
        "content": [
            # {"type": "image", "url": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg"}, ## In case you want to do vision-text safety, you can uncomment this line.
            {"type": "text", "text": prompt},
        ],
    }
]

# Preparation for inference
inputs = processor.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_dict=True,
    return_tensors="pt"
)
inputs = inputs.to(model.device)

# Ensure pixel_values match model dtype, but keep image_grid_thw as integers
if 'pixel_values' in inputs and inputs['pixel_values'] is not None:
    inputs['pixel_values'] = inputs['pixel_values'].to(model.dtype)
# DON'T convert image_grid_thw - it must remain as integer tensor for grid dimensions

# Inference: Generation of the output
generated_ids = model.generate(**inputs, max_new_tokens=128)
generated_ids_trimmed = [
    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
]
output_text = processor.batch_decode(
    generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
)


print(text,output_text)


```

## Training and evaluation data

More information needed

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

We use [SEA-SafeguardBench](arxiv.org/abs/2512.05501) to evaluate our SEA-Guard. Note that we also evaluated the vision-text safety classification in [our research paper](https://arxiv.org/abs/2602.01618)


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

