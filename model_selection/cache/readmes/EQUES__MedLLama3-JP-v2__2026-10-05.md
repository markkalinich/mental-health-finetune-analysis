---
library_name: transformers
tags:
- medical
- merge
license: llama3
language:
- ja
metrics:
- accuracy
---

# Llama3ベースの日本語医療LLM MedLlama3-JP

このモデルはLlama3の継続学習により作成された４種類のLLMから成るマージモデルです。
日本語LLMをベースとし、英語の医療LLMをマージすることで日本語での医療知識や医療Q&Aへの回答力を獲得することを目的としています。

- base :[tokyotech-llm/Llama-3-Swallow-8B-Instruct-v0.1](https://huggingface.co/tokyotech-llm/Llama-3-Swallow-8B-Instruct-v0.1)
- [aaditya/Llama3-OpenBioLLM-8B](https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B)
- [Henrychur/MMed-Llama-3-8B](https://huggingface.co/Henrychur/MMed-Llama-3-8B)
- [elyza/Llama-3-ELYZA-JP-8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B)


医療目的には利用しないでください。  
本モデルの出力に関してその正確性等を保証しません。


# 評価

IgakuQA（日本医師国家試験データセット）の正答率を用いて評価しました。  
評価実験の設定は[IgakuQA](https://github.com/jungokasai/IgakuQA/tree/main/scripts)に従いました。  
GPTモデルのパフォーマンスは[Kasai et al., 2023](https://arxiv.org/pdf/2303.18027)の結果に基づき算出しました。  


| モデル | 　正答率 （全2485問） |
| ---- | ---- |
| [EQUES/MedLLama3-JP-v2](https://huggingface.co/EQUES/MedLLama3-JP-v2) | 46.6% |
| [tokyotech-llm/Llama-3-Swallow-8B-Instruct-v0.1](https://huggingface.co/tokyotech-llm/Llama-3-Swallow-8B-Instruct-v0.1) | 42.2% |
| [elyza/Llama-3-ELYZA-JP-8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B) | 43.9% |
| ---- | ---- |
| GPT-4 | 78.2% | 
| ChatGPT | 54.9% | 
| GPT-3 | 42.1% | 


また、セクションごとの正答率をプロットした図が以下です。マージモデルがマージ元のモデルの良い所取りをしている傾向が窺えます。


![](img/figure.png)


## Usage

```
pip install transformers vllm
```

```python
from transformers import AutoTokenizer
from vllm import LLM, SamplingParams

model_name = "EQUES/MedLLama3-JP-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
llm = LLM(
    model=model_name,
    tensor_parallel_size=1,
)

sampling_params = SamplingParams(
    temperature=0.6, top_p=0.9, max_tokens=512, stop="<|eot_id|>"
)

message = [
    {"role": "system", "content": <question>},
    {"role": "user","content": <answer>},
    {"role": "system", "content": <question>},
]

prompt = tokenizer.apply_chat_template(message, tokenize=False, add_generation_prompt=True)
output = llm.generate(prompt, sampling_params)
print(output[0].outputs[0].text)
```

## Bias, Risks, and Limitations

The models released here are still in the early stages of our research and development and have not been tuned to ensure outputs align with human intent and safety considerations.

## Acknowledgement

We acknowledge the developers of each base model.


## How to Cite

```
@misc{MedLLama3-JP-v2,
      title={EQUES/MedLLama3-JP-v2},
      url={https://huggingface.co/EQUES/MedLLama3-JP-v2},
      author={Issey Sukeda},
      year={2024},
}
```
