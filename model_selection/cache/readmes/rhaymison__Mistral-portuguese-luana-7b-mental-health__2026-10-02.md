---
language:
- pt
license: apache-2.0
library_name: transformers
tags:
- health
- portuguese
base_model: rhaymison/Mistral-portuguese-luana-7b
datasets:
- rhaymison/mental-health-qa
pipeline_tag: text-generation
model-index:
- name: Mistral-portuguese-luana-7b-mental-health
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
      value: 60.53
      name: accuracy
    source:
      url: https://huggingface.co/spaces/eduagarcia/open_pt_llm_leaderboard?query=rhaymison/Mistral-portuguese-luana-7b-mental-health
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
      value: 48.26
      name: accuracy
    source:
      url: https://huggingface.co/spaces/eduagarcia/open_pt_llm_leaderboard?query=rhaymison/Mistral-portuguese-luana-7b-mental-health
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
      value: 38.04
      name: accuracy
    source:
      url: https://huggingface.co/spaces/eduagarcia/open_pt_llm_leaderboard?query=rhaymison/Mistral-portuguese-luana-7b-mental-health
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
      value: 91.3
      name: f1-macro
    source:
      url: https://huggingface.co/spaces/eduagarcia/open_pt_llm_leaderboard?query=rhaymison/Mistral-portuguese-luana-7b-mental-health
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
      value: 74.98
      name: pearson
    source:
      url: https://huggingface.co/spaces/eduagarcia/open_pt_llm_leaderboard?query=rhaymison/Mistral-portuguese-luana-7b-mental-health
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
      value: 60.57
      name: f1-macro
    source:
      url: https://huggingface.co/spaces/eduagarcia/open_pt_llm_leaderboard?query=rhaymison/Mistral-portuguese-luana-7b-mental-health
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
      value: 76.86
      name: f1-macro
    source:
      url: https://huggingface.co/spaces/eduagarcia/open_pt_llm_leaderboard?query=rhaymison/Mistral-portuguese-luana-7b-mental-health
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
      value: 70.05
      name: f1-macro
    source:
      url: https://huggingface.co/spaces/eduagarcia/open_pt_llm_leaderboard?query=rhaymison/Mistral-portuguese-luana-7b-mental-health
      name: Open Portuguese LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: tweetSentBR
      type: eduagarcia/tweetsentbr_fewshot
      split: test
      args:
        num_few_shot: 25
    metrics:
    - type: f1_macro
      value: 64.9
      name: f1-macro
    source:
      url: https://huggingface.co/spaces/eduagarcia/open_pt_llm_leaderboard?query=rhaymison/Mistral-portuguese-luana-7b-mental-health
      name: Open Portuguese LLM Leaderboard
---

# Mistral-portuguese-luana-7b-mental-health

<p align="center">
  <img src="https://raw.githubusercontent.com/rhaymisonbetini/huggphotos/main/luana-hel.jpeg"  width="50%" style="margin-left:'auto' margin-right:'auto' display:'block'"/>
</p>


Luana Mental health is a tuned model of the Luana-7b based on the Mistral 7b architecture.
The model was adjusted to address topics such as depression, problems at work, mental health, problems with studies, drugs and others.

# How to use

You can use the model in its normal form up to 4-bit quantization. Below we will use both approaches.
Remember that verbs are important in your prompt. Tell your model how to act or behave so that you can guide them along the path of their response. 
Important points like these help models (even smaller models like 7b) to perform much better.

### FULL MODEL : A100
### HALF MODEL: L4
### 8bit or 4bit : T4 or V100


```python
!pip install -q -U transformers
!pip install -q -U accelerate
!pip install -q -U bitsandbytes

from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer
model = AutoModelForCausalLM.from_pretrained("rhaymison/Mistral-portuguese-luana-7b-mental-health", device_map= {"": 0})
tokenizer = AutoTokenizer.from_pretrained("rhaymison/Mistral-portuguese-luana-7b-mental-health")
model.eval()

```

You can use with Pipeline but in this example i will use such as Streaming
```python

inputs = tokenizer([f"""<s>Aja como um conselheira de pessoas que estão passandos por dificuldades.
Responda sempre de maneira educada e procure ajudar as pessoas.
[INST] Olá, estou tendo muitos problemas pessoais, briga com meus pais. Tenho tido problemas no trabalho. Preciso de ajuda[/INST]"""], return_tensors="pt")

streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)
_ = model.generate(**inputs, streamer=streamer, max_new_tokens=200)


#Olá, estou aqui para ajudá-lo. É normal enfrentar problemas pessoais, mas é importante buscar ajuda.
#Vamos conversar sobre suas brigas com seus pais e como podemos resolver isso. Além disso, vamos falar sobre seus problemas no trabalho e como podemos encontrar
#soluções para isso. Você não está sozinho, estou aqui para ajudá-lo. Vamos começar a encontrar maneiras de lidar com essas questões.
#Você gostaria de começar falando sobre sua situação com seus pais?
#Ou talvez queremos começar falando sobre seus problemas no trabalho? O que você acha melhor? Você pode me contar mais sobre isso?
#Estou aqui para ajudá-lo.
```

# LangChain
<div style="background-color:#f0f0f0; padding:10px; border-radius:10px; font-family: 'Arial';">
  <p><strong><span style="color:#3366cc;">Human:</span></strong> Ola Luana, estou passando por um momento dificil. Estou precisando de ajuda</p>

  <p><strong><span style="color:#ff6600;">Luana:</span></strong> Olá, estou aqui para te ajudar. Você gostaria de falar sobre o que está te incomodando?</p>

  <p><strong><span style="color:#3366cc;">Human:</span></strong> Tenho tido problemas em casa, em especial com minha esposa. Temos brigado muito, estou com medo do meu 
    casamento terminar.</p>

  <p><strong><span style="color:#ff6600;">Luana:</span></strong> É normal ter problemas no casamento, mas é importante conversar com sua esposa sobre isso. 
    Você já tentou ter uma conversa calma e honesta com ela?</p>

  <p><strong><span style="color:#3366cc;">Human:</span></strong> Já sim, ela me entende, mas sempre terminamos em brigas. 
    Eu sou uma pessoa muito stressada por causa do trabalho. Acabo descontando isso nela.</p>

  <p><strong><span style="color:#ff6600;">Luana:</span></strong> É importante encontrar maneiras saudáveis de lidar com o estresse. 
    Você já tentou praticar atividades de relaxamento, como meditação ou ioga?</p>

  <p><strong><span style="color:#3366cc;">Human:</span></strong> Ja tentei sim. Eu pratico corrida e jogo vide-game pra acalmar, mas nao tem ajudado. 
    Será que uma terapida de casal poderia ajudar?</p>

  <p><strong><span style="color:#ff6600;">Luana:</span></strong> Uma terapeuta de casal pode ser uma ótima opção para ajudar a melhorar a comunicação e resolver 
    problemas no casamento. Você já considerou isso?</p>

  <p><strong><span style="color:#3366cc;">Human:</span></strong> É uma boa opção. Voce poderia me indicar um modo de conversa com ela sobre a terapida de casal? 
    Como apresentar essa ideia pra ela.</p>

  <p><strong><span style="color:#ff6600;">Luana:</span></strong> Sim, é importante abordar a ideia da terapia de casal de maneira aberta e honesta. 
    Você pode começar dizendo que está com medo do seu casamento terminar e que gostaria de tentar algo para melhorar a situação. Também pode ser útil falar sobre os benefícios da terapia de casal, como melhorar a comunicação e encontrar soluções para problemas. Lembre-se de ser paciente e respeitoso, mesmo que ela não esteja disposta a aceitar a ideia inicialmente. A terapia de casal pode ser uma ferramenta poderosa para melhorar o relacionamento, mas é importante que ambos estejam dispostos a dar o primeiro passo.</p>
</div>



# 4bits

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

# Open Portuguese LLM Leaderboard Evaluation Results  

Detailed results can be found [here](https://huggingface.co/datasets/eduagarcia-temp/llm_pt_leaderboard_raw_results/tree/main/rhaymison/Mistral-portuguese-luana-7b-mental-health) and on the [🚀 Open Portuguese LLM Leaderboard](https://huggingface.co/spaces/eduagarcia/open_pt_llm_leaderboard)

|          Metric          |  Value  |
|--------------------------|---------|
|Average                   |**65.05**|
|ENEM Challenge (No Images)|    60.53|
|BLUEX (No Images)         |    48.26|
|OAB Exams                 |    38.04|
|Assin2 RTE                |    91.30|
|Assin2 STS                |    74.98|
|FaQuAD NLI                |    60.57|
|HateBR Binary             |    76.86|
|PT Hate Speech Binary     |    70.05|
|tweetSentBR               |    64.90|

### Comments

Any idea, help or report will always be welcome.

email: rhaymisoncristian@gmail.com

 <div style="display:flex; flex-direction:row; justify-content:left">
    <a href="https://www.linkedin.com/in/heleno-betini-2b3016175/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white">
  </a>
  <a href="https://github.com/rhaymisonbetini" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white">
  </a>

