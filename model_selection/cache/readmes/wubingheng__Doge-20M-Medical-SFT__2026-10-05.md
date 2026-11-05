---
base_model: wubingheng/Doge-20M-Chinese
library_name: transformers
model_name: Doge-20M-Medical-SFT
tags:
- generated_from_trainer
- small-doge
- trl
- sft
licence: license
license: apache-2.0
datasets:
- FreedomIntelligence/huatuo_encyclopedia_qa
language:
- zh
---

# Model Card for Doge-20M-Medical-SFT

This model is a fine-tuned version of [wubingheng/Doge-20M-Chinese](https://huggingface.co/wubingheng/Doge-20M-Chinese).
It has been trained using [TRL](https://github.com/huggingface/trl).

## Quick start

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig, TextStreamer
tokenizer = AutoTokenizer.from_pretrained("wubingheng/Doge-20M-Medical-SFT")
model = AutoModelForCausalLM.from_pretrained("wubingheng/Doge-20M-Medical-SFT", trust_remote_code=True)
generation_config = GenerationConfig(
    max_new_tokens=40,
    min_new_tokens=1,
    num_beams=1,
    eos_token_id=[tokenizer.eos_token_id],
    stop_strings=[tokenizer.eos_token],
    early_stopping=False,
    use_cache=True,
    do_sample=True,
    temperature=0.95,
    repetition_penalty=1.0,
)
steamer = TextStreamer(tokenizer=tokenizer, skip_prompt=True)

system_prompt = """
    你是一个医学助手，能够回答用户提出的医学问题。请根据用户的问题，给出准确的医学建议和解答。

""".strip()

prompt = "肝癌术后饮食注意事项有哪些" 
conversation = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": prompt},
]
inputs = tokenizer.apply_chat_template(
    conversation=conversation,
    tokenize=True,
    return_tensors="pt",
)
print(prompt)

output = model.generate(
    inputs, 
    tokenizer=tokenizer,
    generation_config=generation_config, 
    streamer=steamer
)

```

## Training procedure

[<img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg" alt="Visualize in Weights & Biases" width="150" height="24"/>](https://wandb.ai/loser_cheems/huggingface/runs/o6xtd07v) 


This model was trained with SFT.

### Framework versions

- TRL: 0.15.2
- Transformers: 4.51.2
- Pytorch: 2.6.0+cu126
- Datasets: 3.2.0
- Tokenizers: 0.21.0

## Citations


```bibtex
@misc{smalldoges,
  title={SmallDoges: A Family of Dynamic UltraFast Small Language Models}, 
  author={Jingze, Shi and Yifan, Wu and Bingheng, Wu and Yuyu, Luo},
  year={2025},
  month={March},
  url={https://github.com/SmallDoges/small-doge}
}
```