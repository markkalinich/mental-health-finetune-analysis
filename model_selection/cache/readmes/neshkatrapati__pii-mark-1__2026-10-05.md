---
language:
- en
library_name: transformers
tags:
- gpt
- llm
- large language model
- h2o-llmstudio
inference: false
thumbnail: https://h2o.ai/etc.clientlibs/h2o/clientlibs/clientlib-site/resources/images/favicon.ico
---
# Model Card
## Summary

This model was trained using [H2O LLM Studio](https://github.com/h2oai/h2o-llmstudio).
- Base model: [unsloth/Llama-3.2-1B-Instruct](https://huggingface.co/unsloth/Llama-3.2-1B-Instruct)


## Usage

To use the model with the `transformers` library on a machine with GPUs, first make sure you have the `transformers` library installed.

```bash
pip install transformers==4.45.0
```

Also make sure you are providing your huggingface token to the pipeline if the model is lying in a private repo.

- Either leave `token=True` in the `pipeline` and login to hugginface_hub by running

```python
import huggingface_hub
huggingface_hub.login(<ACCESS_TOKEN>)
```

- Or directly pass your <ACCESS_TOKEN> to `token` in the `pipeline`

```python
from transformers import pipeline

generate_text = pipeline(
    model="neshkatrapati/pii-mark-1",
    torch_dtype="auto",
    trust_remote_code=True,
    device_map={"": "cuda:0"},
    token=True,
)

# generate configuration can be modified to your needs
# generate_text.model.generation_config.min_new_tokens = 2
# generate_text.model.generation_config.max_new_tokens = 256
# generate_text.model.generation_config.do_sample = False
# generate_text.model.generation_config.num_beams = 1
# generate_text.model.generation_config.temperature = float(0.0)
# generate_text.model.generation_config.repetition_penalty = float(1.0)

messages = [
    {"role": "user", "content": "Hi, how are you?"},
    {"role": "assistant", "content": "I'm doing great, how about you?"},
    {"role": "user", "content": "Why is drinking water so healthy?"},
]

res = generate_text(
    messages,
    renormalize_logits=True
)
print(res[0]["generated_text"][-1]['content'])
```

You can print a sample prompt after applying chat template to see how it is feed to the tokenizer:

```python
print(generate_text.tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
))
```

You may also construct the pipeline from the loaded model and tokenizer yourself and consider the preprocessing steps:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "neshkatrapati/pii-mark-1"  # either local folder or Hugging Face model name
# Important: The prompt needs to be in the same format the model was trained with.
# You can find an example prompt in the experiment logs.
messages = [
    {"role": "user", "content": "Hi, how are you?"},
    {"role": "assistant", "content": "I'm doing great, how about you?"},
    {"role": "user", "content": "Why is drinking water so healthy?"},
]

tokenizer = AutoTokenizer.from_pretrained(
    model_name,
    trust_remote_code=True,
)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map={"": "cuda:0"},
    trust_remote_code=True,
)
model.cuda().eval()

# generate configuration can be modified to your needs
# model.generation_config.min_new_tokens = 2
# model.generation_config.max_new_tokens = 256
# model.generation_config.do_sample = False
# model.generation_config.num_beams = 1
# model.generation_config.temperature = float(0.0)
# model.generation_config.repetition_penalty = float(1.0)

inputs = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_tensors="pt",
    return_dict=True,
).to("cuda")

tokens = model.generate(
    input_ids=inputs["input_ids"],
    attention_mask=inputs["attention_mask"],
    renormalize_logits=True
)[0]

tokens = tokens[inputs["input_ids"].shape[1]:]
answer = tokenizer.decode(tokens, skip_special_tokens=True)
print(answer)
```

## Quantization and sharding

You can load the models using quantization by specifying ```load_in_8bit=True``` or ```load_in_4bit=True```. Also, sharding on multiple GPUs is possible by setting ```device_map=auto```.

## Model Architecture

```
LlamaForCausalLM(
  (model): LlamaModel(
    (embed_tokens): Embedding(128256, 2048, padding_idx=128004)
    (layers): ModuleList(
      (0-15): 16 x LlamaDecoderLayer(
        (self_attn): LlamaSdpaAttention(
          (q_proj): Linear(in_features=2048, out_features=2048, bias=False)
          (k_proj): Linear(in_features=2048, out_features=512, bias=False)
          (v_proj): Linear(in_features=2048, out_features=512, bias=False)
          (o_proj): Linear(in_features=2048, out_features=2048, bias=False)
          (rotary_emb): LlamaRotaryEmbedding()
        )
        (mlp): LlamaMLP(
          (gate_proj): Linear(in_features=2048, out_features=8192, bias=False)
          (up_proj): Linear(in_features=2048, out_features=8192, bias=False)
          (down_proj): Linear(in_features=8192, out_features=2048, bias=False)
          (act_fn): SiLU()
        )
        (input_layernorm): LlamaRMSNorm((2048,), eps=1e-05)
        (post_attention_layernorm): LlamaRMSNorm((2048,), eps=1e-05)
      )
    )
    (norm): LlamaRMSNorm((2048,), eps=1e-05)
    (rotary_emb): LlamaRotaryEmbedding()
  )
  (lm_head): Linear(in_features=2048, out_features=128256, bias=False)
)
```

## Model Configuration

This model was trained using H2O LLM Studio and with the configuration in [cfg.yaml](cfg.yaml). Visit [H2O LLM Studio](https://github.com/h2oai/h2o-llmstudio) to learn how to train your own large language models.


## Disclaimer

Please read this disclaimer carefully before using the large language model provided in this repository. Your use of the model signifies your agreement to the following terms and conditions.

- Biases and Offensiveness: The large language model is trained on a diverse range of internet text data, which may contain biased, racist, offensive, or otherwise inappropriate content. By using this model, you acknowledge and accept that the generated content may sometimes exhibit biases or produce content that is offensive or inappropriate. The developers of this repository do not endorse, support, or promote any such content or viewpoints.
- Limitations: The large language model is an AI-based tool and not a human. It may produce incorrect, nonsensical, or irrelevant responses. It is the user's responsibility to critically evaluate the generated content and use it at their discretion.
- Use at Your Own Risk: Users of this large language model must assume full responsibility for any consequences that may arise from their use of the tool. The developers and contributors of this repository shall not be held liable for any damages, losses, or harm resulting from the use or misuse of the provided model.
- Ethical Considerations: Users are encouraged to use the large language model responsibly and ethically. By using this model, you agree not to use it for purposes that promote hate speech, discrimination, harassment, or any form of illegal or harmful activities.
- Reporting Issues: If you encounter any biased, offensive, or otherwise inappropriate content generated by the large language model, please report it to the repository maintainers through the provided channels. Your feedback will help improve the model and mitigate potential issues.
- Changes to this Disclaimer: The developers of this repository reserve the right to modify or update this disclaimer at any time without prior notice. It is the user's responsibility to periodically review the disclaimer to stay informed about any changes.

By using the large language model provided in this repository, you agree to accept and comply with the terms and conditions outlined in this disclaimer. If you do not agree with any part of this disclaimer, you should refrain from using the model and any content generated by it.