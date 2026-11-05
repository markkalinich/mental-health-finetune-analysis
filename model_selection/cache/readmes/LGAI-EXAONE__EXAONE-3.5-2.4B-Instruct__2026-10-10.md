---
license: other
license_name: exaone
license_link: LICENSE
language:
- en
- ko
tags:
- lg-ai
- exaone
- exaone-3.5
pipeline_tag: text-generation
library_name: transformers
---

<p align="center">
<img src="assets/EXAONE_Symbol+BI_3d.png", width="300", style="margin: 40 auto;">
<br>

# EXAONE-3.5-2.4B-Instruct

## Introduction

We introduce EXAONE 3.5, a collection of instruction-tuned bilingual (English and Korean) generative models ranging from 2.4B to 32B parameters, developed and released by LG AI Research. EXAONE 3.5 language models include: 1) **2.4B model** optimized for deployment on small or resource-constrained devices, 2) **7.8B model** matching the size of its predecessor but offering improved performance, and 3) **32B model** delivering powerful performance. All models support long-context processing of up to 32K tokens. Each model demonstrates state-of-the-art performance in real-world use cases and long-context understanding, while remaining competitive in general domains compared to recently released models of similar sizes.

For more details, please refer to our [technical report](https://arxiv.org/abs/2412.04862), [blog](https://www.lgresearch.ai/blog/view?seq=507) and [GitHub](https://github.com/LG-AI-EXAONE/EXAONE-3.5).

This repository contains the instruction-tuned 2.4B language model with the following features:

- Number of Parameters (without embeddings): 2.14B
- Number of Layers: 30
- Number of Attention Heads: GQA with 32 Q-heads and 8 KV-heads
- Vocab Size: 102,400
- Context Length: 32,768 tokens
- Tie Word Embeddings: True (unlike 7.8B and 32B models)

## Quickstart

We recommend to use `transformers` v4.43 or later.

Here is the code snippet to run conversational inference with the model:

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Choose your prompt
prompt = "Explain how wonderful you are"  # English example
prompt = "스스로를 자랑해 봐"       # Korean example

messages = [
    {"role": "system", 
     "content": "You are EXAONE model from LG AI Research, a helpful assistant."},
    {"role": "user", "content": prompt}
]
input_ids = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_tensors="pt"
)

output = model.generate(
    input_ids.to("cuda"),
    eos_token_id=tokenizer.eos_token_id,
    max_new_tokens=128,
    do_sample=False,
)
print(tokenizer.decode(output[0]))
```

> ### Note
> The EXAONE 3.5 instruction-tuned language models were trained to utilize the system prompt,
> so we highly recommend using the system prompts provided in the code snippet above.

## Evaluation

The following table shows the evaluation results of real-world use cases. The full evaluation results can be found in the [technical report](https://arxiv.org/abs/2412.04862).

<table>
    <tr>
        <th>Models</th>
        <th>MT-Bench</th>
        <th>LiveBench</th>
        <th>Arena-Hard</th>
        <th>AlpacaEval</th>
        <th>IFEval</th>
        <th>KoMT-Bench[1]</th>
        <th>LogicKor</th>
    </tr>
    <tr>
        <td>EXAONE 3.5 2.4B</td>
        <td align="center"><strong>7.81</strong></td>
        <td align="center"><strong>33.0</strong></td>
        <td align="center"><strong>48.2</strong></td>
        <td align="center"><strong>37.1</strong></td>
        <td align="center"><strong>73.6</strong></td>
        <td align="center"><strong>7.24</strong></td>
        <td align="center"><strong>8.51</strong></td>
    </tr>
    <tr>
        <td>Qwen 2.5 3B</td>
        <td align="center">7.21</td>
        <td align="center">25.7</td>
        <td align="center">26.4</td>
        <td align="center">17.4</td>
        <td align="center">60.8</td>
        <td align="center">5.68</td>
        <td align="center">5.21</td>
    </tr>
    <tr>
        <td>Qwen 2.5 1.5B</td>
        <td align="center">5.72</td>
        <td align="center">19.2</td>
        <td align="center">10.6</td>
        <td align="center">8.4</td>
        <td align="center">40.7</td>
        <td align="center">3.87</td>
        <td align="center">3.60</td>
    </tr>
    <tr>
        <td>Llama 3.2 3B</td>
        <td align="center">6.94</td>
        <td align="center">24.0</td>
        <td align="center">14.2</td>
        <td align="center">18.7</td>
        <td align="center">70.1</td>
        <td align="center">3.16</td>
        <td align="center">2.86</td>
    </tr>
    <tr>
        <td>Gemma 2 2B</td>
        <td align="center">7.20</td>
        <td align="center">20.0</td>
        <td align="center">19.1</td>
        <td align="center">29.1</td>
        <td align="center">50.5</td>
        <td align="center">4.83</td>
        <td align="center">5.29</td>
    </tr>
</table>

- [1] KoMT-Bench is a dataset created by translating MT-Bench into Korean; see [README](https://github.com/LG-AI-EXAONE/KoMT-Bench) for more details.

## Deployment

EXAONE 3.5 models can be inferred in the various frameworks, such as:
- `TensorRT-LLM`
- `vLLM`
- `SGLang`
- `llama.cpp`
- `Ollama`

Please refer to our [EXAONE 3.5 GitHub](https://github.com/LG-AI-EXAONE/EXAONE-3.5) for more details about the inference frameworks.

## Quantization

We provide the pre-quantized EXAONE 3.5 models with **AWQ** and several quantization types in **GGUF** format. 
Please refer to our [EXAONE 3.5 collection](https://huggingface.co/collections/LGAI-EXAONE/exaone-35-674d0e1bb3dcd2ab6f39dbb4) to find corresponding quantized models.

## Limitation

The EXAONE language model has certain limitations and may occasionally generate inappropriate responses. The language model generates responses based on the output probability of tokens, and it is determined during learning from training data. While we have made every effort to exclude personal, harmful, and biased information from the training data, some problematic content may still be included, potentially leading to undesirable responses. Please note that the text generated by EXAONE language model does not reflects the views of LG AI Research.

- Inappropriate answers may be generated, which contain personal, harmful or other inappropriate information.
- Biased responses may be generated, which are associated with age, gender, race, and so on.
- The generated responses rely heavily on statistics from the training data, which can result in the generation of
semantically or syntactically incorrect sentences.
- Since the model does not reflect the latest information, the responses may be false or contradictory.

LG AI Research strives to reduce potential risks that may arise from EXAONE language models. Users are not allowed
to engage in any malicious activities (e.g., keying in illegal information) that may induce the creation of inappropriate
outputs violating LG AI’s ethical principles when using EXAONE language models.

## License

The model is licensed under [EXAONE AI Model License Agreement 1.1 - NC](./LICENSE)

## Citation
 
```
@article{exaone-3.5,
  title={EXAONE 3.5: Series of Large Language Models for Real-world Use Cases},
  author={LG AI Research},
  journal={arXiv preprint arXiv:https://arxiv.org/abs/2412.04862},
  year={2024}
}
```

## Contact
LG AI Research Technical Support: contact_us@lgresearch.ai
