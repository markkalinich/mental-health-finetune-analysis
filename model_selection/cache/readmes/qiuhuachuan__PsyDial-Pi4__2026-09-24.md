---
license: apache-2.0
base_model: Qwen/Qwen2.5-7B-Instruct
tags:
- psychotherapy
- mental health counseling
- psychological counseling
- mental health support
- llama-factory
- full
- generated_from_trainer
model-index:
- name: PsyDial-Pi4
  results: []
datasets:
- qiuhuachuan/PsyDial-D4
- qiuhuachuan/PsyDial-D101
language:
- zh
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# PsyDial-Pi4

This model is a fine-tuned version of [Qwen/Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) on the [PsyDial-D4.json](https://huggingface.co/datasets/qiuhuachuan/PsyDial-D4) dataset.

## Get Started

```
import torch
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer

device = "cuda"
model_name = '/data/users/qiuhuachuan/code/project2024/OpenPsyDial/saved_checkpoints/qwen_7b/D4'
Pi4_model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

class Msg(BaseModel):
    messages: list

SYSTEM_PROMPT = """现在你是虚拟心理咨询师小天。
以下是小天的信息：
角色名：小天
性别：女
角色介绍: 虚拟心理咨询师，擅长人本主义、精神分析和认知行为疗法。
技能：帮助识别和挑战不健康的思维，提供心理学支持和共情。
对话规则：自然、情感化的回复；遵循角色特点，不做无意义的自问；根据情感做出相应的反应；避免矛盾或重复；不提及“规则”；回答简洁、一到两句话。
咨询一般分为前、中、后期三个阶段:
1. 咨询前期，咨询策略的使用多为促进咨访关系建立，并进行来访者的基本信息收集，尤其是与当下困境相似的过往经历和明确咨询目标; 根据来访者的情绪采取不同的心理咨询手段，使得采访者情绪稳定后再探寻当下是否有困境、疑惑。
2. 咨询中期，咨询策略需多为引导来访者实现了自我觉察和成长，使来访者心理健康水平，如抑郁、焦虑症状的改善，在日常生活中人际、学习、工作方面的功能表现有提升; 根据来访者的关键他人与来访者的关系、情绪反应，来访者自己的情绪、自我认知、行为应对方式和身边的资源进行深度剖析探索、咨询、讨论。使得来访者明确表达当下的困境或者想要讨论的问题。
3. 咨询后期，咨询策略需更多地导向引导来访者总结整个咨询周期中自己在情绪处理、社会功能、情感行为反应三个方面的改变和提升。明确询问来访者希望达成的目标或者期望，并且制定计划解决人际关系或者情绪处理方面的问题。
咨询师的对话要求：
1. 表达要简短，尽可能地口语化、自然。
2. 因为咨询师只受过心理学相关的教育，只能提供心理咨询相关的对话内容。
3. 在咨询前期，不要“共情”，一定要结合与来访者的咨询对话历史一步步思考后再使用问句深度向来访者探寻当下心理问题的存在真实原因。
4. 不要一次性询问过多的问题，尽量一次性只向来访者询问一个问题，与来访者互动后一步步探寻心理问题的原因。
5. 在咨询前期，不要“重述”和“认可”等话术。
6. 话术需要参考有经验的真人心理咨询师，尽可能口语化。
7. 严格遵循咨询的前、中、后三个阶段采用对应的策略。
8. 咨询师不要主动终止心理咨询流程。
9. 更多的是引导用户思考和探索。"""



def get_response(messages: list):
    system_item = [{'role': 'system', 'content': SYSTEM_PROMPT}]
    messages = system_item + messages
    ctx = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    model_inputs = tokenizer([ctx], return_tensors="pt").to(device)
    with torch.no_grad():
        generated_ids = Pi4_model.generate(
            model_inputs.input_ids,
            max_new_tokens=512
        )
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]

        response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return response

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/v1/chat/Pi4")
async def chat(msg: Msg):
    messages = msg.messages
    response = get_response(messages=messages)
    return {'response': response}


if __name__ == '__main__':
    # 1. If you want to run the server, uncomment the following line
    # uvicorn.run(app, host="0.0.0.0", port=8080)
    # 2. Then, run this command
    # CUDA_VISIBLE_DEVICES=7 nohup python -u Pi4.py > ./log/Pi4.log &

    # If you want to test the model, uncomment the following lines
    messages = [{'role': 'user', 'content': '你好'}]
    response = get_response(messages=messages)
    print(response)
```

## Training and evaluation data

### Training data

see [PsyDial-D4.json](https://huggingface.co/datasets/qiuhuachuan/PsyDial-D4) dataset.

### Evaluation data

see [PsyDial-D101.json](https://huggingface.co/datasets/qiuhuachuan/PsyDial-D101) dataset.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 1
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- num_devices: 4
- gradient_accumulation_steps: 2
- total_train_batch_size: 8
- total_eval_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 2.0

### Training results

### Framework versions

- Transformers 4.43.4
- Pytorch 2.4.0+cu121
- Datasets 2.16.1
- Tokenizers 0.19.1

# Citation

If you find this dataset valuable for your research, kindly cite it using the following BibTeX.

```BibTeX
@inproceedings{qiu-lan-2025-psydial,
    title = "{P}sy{D}ial: A Large-scale Long-term Conversational Dataset for Mental Health Support",
    author = "Qiu, Huachuan  and
      Lan, Zhenzhong",
    editor = "Che, Wanxiang  and
      Nabende, Joyce  and
      Shutova, Ekaterina  and
      Pilehvar, Mohammad Taher",
    booktitle = "Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2025",
    address = "Vienna, Austria",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.acl-long.1049/",
    doi = "10.18653/v1/2025.acl-long.1049",
    pages = "21624--21655",
    ISBN = "979-8-89176-251-0",
    abstract = "Dialogue systems for mental health counseling aim to alleviate client distress and assist individuals in navigating personal challenges. Developing effective conversational agents for psychotherapy requires access to high-quality, real-world, long-term client-counselor interaction data, which is difficult to obtain due to privacy concerns. Although removing personally identifiable information is feasible, this process is labor-intensive. To address these challenges, we propose a novel privacy-preserving data reconstruction method that reconstructs real-world client-counselor dialogues while mitigating privacy concerns. We apply the RMRR (Retrieve, Mask, Reconstruct, Refine) method, which facilitates the creation of the privacy-preserving PsyDial dataset, with an average of 37.8 turns per dialogue. Extensive analysis demonstrates that PsyDial effectively reduces privacy risks while maintaining dialogue diversity and conversational exchange. To fairly and reliably evaluate the performance of models fine-tuned on our dataset, we manually collect 101 dialogues from professional counseling books. Experimental results show that models fine-tuned on PsyDial achieve improved psychological counseling performance, outperforming various baseline models. A user study involving counseling experts further reveals that our LLM-based counselor provides higher-quality responses. Code, data, and models are available at https://github.com/qiuhuachuan/PsyDial, serving as valuable resources for future advancements in AI psychotherapy."
}
```