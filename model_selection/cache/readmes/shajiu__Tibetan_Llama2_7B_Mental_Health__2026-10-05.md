---
license: llama2
---
## 基于Llama2_7B直接微调的藏文心理健康支持对话大模型(Tibetan_Mental_Chat)

## 多轮对话测试demo
```python
# -- coding: utf-8 --
# @time : 2024/12/1 16:26
# @author : shajiu
# @email : 18810979033@163.com
# @file : .py
# @software: pycharm


from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM, BitsAndBytesConfig
import torch
from peft import PeftModel

class ModelUtils(object):

    @classmethod
    def load_model(cls, model_name_or_path, load_in_4bit=False, adapter_name_or_path=None):
        # 是否使用4bit量化进行推理
        if load_in_4bit:
            quantization_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_compute_dtype=torch.float16,
                bnb_4bit_use_double_quant=True,
                bnb_4bit_quant_type="nf4",
                llm_int8_threshold=6.0,
                llm_int8_has_fp16_weight=False,
            )
        else:
            quantization_config = None

        # 加载base model
        model = AutoModelForCausalLM.from_pretrained(
            model_name_or_path,
            load_in_4bit=load_in_4bit,
            trust_remote_code=True,
            low_cpu_mem_usage=True,
            torch_dtype=torch.float16,
            device_map='auto',
            quantization_config=quantization_config
        )

        # 加载adapter
        if adapter_name_or_path is not None:
            model = PeftModel.from_pretrained(model, adapter_name_or_path)

        return model


def main(model_name_or_path):
    # 使用合并后的模型进行推理
    adapter_name_or_path = None

    # 使用base model和adapter进行推理
    # model_name_or_path = 'shajiu/Tibetan_Llama2_7B_Mental_Health'
    # adapter_name_or_path = 'shajiu/Tibetan_Llama2_7B_Mental_Health'

    # 是否使用4bit进行推理，能够节省很多显存，但效果可能会有一定的下降
    load_in_4bit = False
    device = 'cuda'

    # 生成超参配置
    max_new_tokens = 500  # 每轮对话最多生成多少个token
    history_max_len = 1000  # 模型记忆的最大token长度
    top_p = 0.9
    temperature = 0.35
    repetition_penalty = 1.0

    # 加载模型
    model = ModelUtils.load_model(
        model_name_or_path,
        load_in_4bit=load_in_4bit,
        adapter_name_or_path=adapter_name_or_path
    ).eval()
    # 加载tokenizer
    tokenizer = AutoTokenizer.from_pretrained(
        model_name_or_path,
        trust_remote_code=True,
        # llama不支持fast
        use_fast=False if model.config.model_type == 'llama' else True
    )
    # QWenTokenizer比较特殊，pad_token_id、bos_token_id、eos_token_id均为None。eod_id对应的token为<|endoftext|>
    if tokenizer.__class__.__name__ == 'QWenTokenizer':
        tokenizer.pad_token_id = tokenizer.eod_id
        tokenizer.bos_token_id = tokenizer.eod_id
        tokenizer.eos_token_id = tokenizer.eod_id

    # 记录所有历史记录
    if model.config.model_type != 'chatglm':
        history_token_ids = torch.tensor([[tokenizer.bos_token_id]], dtype=torch.long)
    else:
        history_token_ids = torch.tensor([[]], dtype=torch.long)

    # 开始对话
    utterance_id = 0    # 记录当前是第几轮对话，为了契合chatglm的数据组织格式
    user_input = input('User：')
    while True:
        utterance_id += 1
        # chatglm使用官方的数据组织格式
        if model.config.model_type == 'chatglm':
            user_input = '[Round {}]\n\n问：{}\n\n答：'.format(utterance_id, user_input)
            user_input_ids = tokenizer(user_input, return_tensors="pt", add_special_tokens=False).input_ids
        # firefly的数据组织格式
        # 为了兼容qwen-7b，因为其对eos_token进行tokenize，无法得到对应的eos_token_id
        else:
            input_ids = tokenizer(user_input, return_tensors="pt", add_special_tokens=False).input_ids
            eos_token_id = torch.tensor([[tokenizer.eos_token_id]], dtype=torch.long)
            user_input_ids = torch.concat([input_ids, eos_token_id], dim=1)
        history_token_ids = torch.concat((history_token_ids, user_input_ids), dim=1)
        model_input_ids = history_token_ids[:, -history_max_len:].to(device)
        with torch.no_grad():
            outputs = model.generate(
                input_ids=model_input_ids, max_new_tokens=max_new_tokens, do_sample=True, top_p=top_p,
                temperature=temperature, repetition_penalty=repetition_penalty, eos_token_id=tokenizer.eos_token_id
            )
        model_input_ids_len = model_input_ids.size(1)
        response_ids = outputs[:, model_input_ids_len:]
        history_token_ids = torch.concat((history_token_ids, response_ids.cpu()), dim=1)
        response = tokenizer.batch_decode(response_ids)
        print("Firefly：" + response[0].strip().replace(tokenizer.eos_token, ""))
        user_input = input('User：')


if __name__ == '__main__':
    model_name_or_path = 'E:\models\shajiuTibetan_Llama2_7B_Mental_Health'
    main(model_name_or_path)
```