---
language:
- pt
license: apache-2.0
library_name: transformers
tags:
- Misral
- Portuguese
- 7b
base_model: mistralai/Mistral-7B-Instruct-v0.2
datasets:
- pablo-moreira/gpt4all-j-prompt-generations-pt
- rhaymison/superset
pipeline_tag: text-generation
model-index:
- name: Mistral-portuguese-luana-7b
  results:
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: ENEM Challenge (No Images)
      type: eduagarcia/enem_challenge
      split: train
      args:
        num_few_shot: 3
    metrics:
    - type: acc
      value: 58.64
      name: accuracy
    source:
      url: https://huggingface.co/spaces/eduagarcia/open_pt_llm_leaderboard?query=rhaymison/Mistral-portuguese-luana-7b
      name: Open Portuguese LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: BLUEX (No Images)
      type: eduagarcia-temp/BLUEX_without_images
      split: train
      args:
        num_few_shot: 3
    metrics:
    - type: acc
      value: 47.98
      name: accuracy
    source:
      url: https://huggingface.co/spaces/eduagarcia/open_pt_llm_leaderboard?query=rhaymison/Mistral-portuguese-luana-7b
      name: Open Portuguese LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: OAB Exams
      type: eduagarcia/oab_exams
      split: train
      args:
        num_few_shot: 3
    metrics:
    - type: acc
      value: 38.82
      name: accuracy
    source:
      url: https://huggingface.co/spaces/eduagarcia/open_pt_llm_leaderboard?query=rhaymison/Mistral-portuguese-luana-7b
      name: Open Portuguese LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: Assin2 RTE
      type: assin2
      split: test
      args:
        num_few_shot: 15
    metrics:
    - type: f1_macro
      value: 90.63
      name: f1-macro
    source:
      url: https://huggingface.co/spaces/eduagarcia/open_pt_llm_leaderboard?query=rhaymison/Mistral-portuguese-luana-7b
      name: Open Portuguese LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: Assin2 STS
      type: eduagarcia/portuguese_benchmark
      split: test
      args:
        num_few_shot: 15
    metrics:
    - type: pearson
      value: 75.81
      name: pearson
    source:
      url: https://huggingface.co/spaces/eduagarcia/open_pt_llm_leaderboard?query=rhaymison/Mistral-portuguese-luana-7b
      name: Open Portuguese LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: FaQuAD NLI
      type: ruanchaves/faquad-nli
      split: test
      args:
        num_few_shot: 15
    metrics:
    - type: f1_macro
      value: 57.79
      name: f1-macro
    source:
      url: https://huggingface.co/spaces/eduagarcia/open_pt_llm_leaderboard?query=rhaymison/Mistral-portuguese-luana-7b
      name: Open Portuguese LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: HateBR Binary
      type: ruanchaves/hatebr
      split: test
      args:
        num_few_shot: 25
    metrics:
    - type: f1_macro
      value: 77.24
      name: f1-macro
    source:
      url: https://huggingface.co/spaces/eduagarcia/open_pt_llm_leaderboard?query=rhaymison/Mistral-portuguese-luana-7b
      name: Open Portuguese LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: PT Hate Speech Binary
      type: hate_speech_portuguese
      split: test
      args:
        num_few_shot: 25
    metrics:
    - type: f1_macro
      value: 68.5
      name: f1-macro
    source:
      url: https://huggingface.co/spaces/eduagarcia/open_pt_llm_leaderboard?query=rhaymison/Mistral-portuguese-luana-7b
      name: Open Portuguese LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: tweetSentBR
      type: eduagarcia-temp/tweetsentbr
      split: test
      args:
        num_few_shot: 25
    metrics:
    - type: f1_macro
      value: 63.0
      name: f1-macro
    source:
      url: https://huggingface.co/spaces/eduagarcia/open_pt_llm_leaderboard?query=rhaymison/Mistral-portuguese-luana-7b
      name: Open Portuguese LLM Leaderboard
---

# Mistral-portuguese-luana-7b

<p align="center">
  <img src="https://raw.githubusercontent.com/rhaymisonbetini/huggphotos/main/luana7b.webp" width="50%" style="margin-left:'auto' margin-right:'auto' display:'block'"/>
</p>


This model was trained with a superset of 200,000 instructions in Portuguese. 
The model comes to help fill the gap in models in Portuguese. Tuned from the Mistral 7b, the model was adjusted mainly for instructional tasks.

If you are looking for enhanced compatibility, the Luana model also has a GGUF family that can be run with LlamaCpp. 
You can explore the GGUF models starting with the one below:

- [Mistral-portuguese-luana-7b-q8-gguf](https://huggingface.co/rhaymison/Mistral-portuguese-luana-7b-q8-gguf)
- [Mistral-portuguese-luana-7b-f16-gguf](https://huggingface.co/rhaymison/Mistral-portuguese-luana-7b-f16-gguf)

Explore this and other models to find the best fit for your needs!

# How to use

### FULL MODEL : A100
### HALF MODEL: L4
### 8bit or 4bit : T4 or V100

You can use the model in its normal form up to 4-bit quantization. Below we will use both approaches.
Remember that verbs are important in your prompt. Tell your model how to act or behave so that you can guide them along the path of their response. 
Important points like these help models (even smaller models like 7b) to perform much better.

```python
!pip install -q -U transformers
!pip install -q -U accelerate
!pip install -q -U bitsandbytes

from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer
model = AutoModelForCausalLM.from_pretrained("rhaymison/Mistral-portuguese-luana-7b", device_map= {"": 0})
tokenizer = AutoTokenizer.from_pretrained("rhaymison/Mistral-portuguese-luana-7b")
model.eval()

```

You can use with Pipeline but in this example i will use such as Streaming
```python

inputs = tokenizer([f"""<s>[INST] Abaixo está uma instrução que descreve uma tarefa, juntamente com uma entrada que fornece mais contexto.
Escreva uma resposta que complete adequadamente o pedido.
### instrução: aja como um professor de matemática e me explique porque 2 + 2 = 4.
[/INST]"""], return_tensors="pt")

inputs.to(model.device)

streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)
_ = model.generate(**inputs, streamer=streamer, max_new_tokens=200)

```

If you are having a memory problem such as "CUDA Out of memory", you should use 4-bit or 8-bit quantization.
For the complete model in colab you will need the A100.
If you want to use 4bits or 8bits, T4 or L4 will already solve the problem.

# 4bits example

```python
from transformers import BitsAndBytesConfig
import torch
nb_4bit_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True
)

model = AutoModelForCausalLM.from_pretrained(
    base_model,
    quantization_config=bnb_config,
    device_map={"": 0}
)

```

# LangChain 

<p align="center">
  <img src="https://raw.githubusercontent.com/rhaymisonbetini/huggphotos/main/lang.png" alt="Bode Logo" width="100%" style="margin-left:'auto' margin-right:'auto' display:'block'"/>
</p>



# [Open Portuguese LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/eduagarcia/open_pt_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/eduagarcia-temp/llm_pt_leaderboard_raw_results/tree/main/rhaymison/Mistral-portuguese-luana-7b)

|          Metric          |  Value  |
|--------------------------|---------|
|Average                   |**64.27**|
|ENEM Challenge (No Images)|    58.64|
|BLUEX (No Images)         |    47.98|
|OAB Exams                 |    38.82|
|Assin2 RTE                |    90.63|
|Assin2 STS                |    75.81|
|FaQuAD NLI                |    57.79|
|HateBR Binary             |    77.24|
|PT Hate Speech Binary     |    68.50|
|tweetSentBR               |       63|



### Comments

Any idea, help or report will always be welcome.

email: rhaymisoncristian@gmail.com

 <div style="display:flex; flex-direction:row; justify-content:left">
    <a href="https://www.linkedin.com/in/rhaymison-cristian-betini-2b3016175/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white">
  </a>
  <a href="https://github.com/rhaymisonbetini" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white">
  </a>
 </div>