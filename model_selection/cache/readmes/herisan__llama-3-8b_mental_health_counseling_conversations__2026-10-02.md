!pip -q install git+https://github.com/huggingface/transformers # need to install from github
!pip -q install bitsandbytes accelerate xformers einops

import os
import torch
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, pipeline

model_name = "herisan/llama-3-8b_mental_health_counseling_conversations"

# use the commented out parts for running in 4bit
bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16
    )


model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    quantization_config=bnb_config,
    # low_cpu_mem_usage=True
)


tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.bos_token_id = 1

stop_token_ids = [0]

pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        use_cache=True,
        device_map="auto",
        max_length=2046,
        do_sample=True,
        top_k=5,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id,
        pad_token_id=tokenizer.eos_token_id,
)

messages = [
    {
        "role": "system",
        "content": "Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.",
    },
    {"role": "user", "content": "I'm going through some things with my feelings and myself. I barely sleep and I do nothing but think about how I'm worthless and how I shouldn't be here. I've never tried or contemplated suicide. I've always wanted to fix my issues, but I never get around to it. How can I change my feeling of being worthless to everyone?"},
]
prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
outputs = pipe(prompt, max_new_tokens=2046, do_sample=True, temperature=0.7, top_k=50, top_p=0.95, truncation=True)
print(outputs[0]["generated_text"])
