---
library_name: transformers
license: mit
datasets:
- AdamLucek/open-pii-masking-en-us-30k
language:
- en
base_model:
- Qwen/Qwen3-4B-Instruct-2507
---

# Qwen3-4B-Instruct-2507-PII-RL

Qwen3-4B-Instruct-2507-PII-RL is a LoRA reinforcement learning fine-tune of [Qwen/Qwen3-4B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507), trained for 740 policy updates on batches sampled from [AdamLucek/open-pii-masking-en-us-30k](https://huggingface.co/datasets/AdamLucek/open-pii-masking-en-us-30k) using the [adamlucek/pii-masking](https://app.primeintellect.ai/dashboard/environments/adamlucek/pii-masking) environment.

Qwen3-4B-Instruct-2507-PII-RL has been trained to mask PII data. Given an input phrase it will output the same phrase with all PII instances replaced by `[PII]`.

## Training

This model was trained using [Tinker](https://thinkingmachines.ai/tinker/) and the [adamlucek/pii-masking](https://app.primeintellect.ai/dashboard/environments/adamlucek/pii-masking) environment with the following specs:

| Parameter | Value |
| --- | --- |
| Method | LoRA (`rank=32`) |
| Environment | `pii-masking` verifiers environment |
| Batch size | 256 trajectory groups (`groups_per_batch=32` × `group_size=8`) |
| Max sequence length | 512 tokens |
| Optimizer | Adam (`lr=1e-5`, `β1=0.9`, `β2=0.95`, `ε=1e-8`) |
| Scheduler | Constant learning rate |
| Dataset | Full training set (`num_train_examples=-1`) |

Over 740 training steps, the following reward curve was produced:

<img src="full_run_qwen3_4b_instruct.png" width=600>

## Rewards

The reward function is a weighted combination of three components:

| Component | Weight | Description |
| --- | --- | --- |
| `exact_match_reward` | 1.0 | Binary reward (1.0 if the parsed masked output exactly matches the expected answer character-by-character, 0.0 otherwise) |
| `pii_count_reward` | 0.5 | Binary reward (1.0 if the number of `[PII]` tags in the output matches the expected count, 0.0 otherwise) |
| `format_reward` | 0.1 | Parser-generated format reward ensuring the output is properly formatted with valid XML tags (`<masked_output>...</masked_output>`) |

The final `reward` is calculated as:

```python
reward = (1.0 × exact_match_reward) + (0.5 × pii_count_reward) + (0.1 × format_reward)
```

**Reward Range**: The reward can range from 0.0 (worst) to 1.6 (best), where:
- **1.6**: Perfect match with correct PII count and valid format
- **1.0**: Exact match but incorrect PII count or invalid format
- **0.5-0.6**: Correct PII count but inexact match, with/without format compliance
- **0.0-0.1**: No match, incorrect count, or invalid format

## Usage

Loading and using the model via Transformers

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

# Replace with the actual repository name you used
model_id = "AdamLucek/Qwen3-4B-Instruct-2507-PII-RL"

# Load the merged model and tokenizer from the Hugging Face Hub
model = AutoModelForCausalLM.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)

system_prompt = """Replace all personally identifiable information (PII) in the text with [PII] tags. 
PII includes: names, dates, phone numbers, SSNs, account numbers, addresses, email addresses, and any other identifying information.

Examples:
Input: Ticket Reservation for Florije: 'one ticket for Madame on October 8th, 1990'
Output: Ticket Reservation for [PII]: 'one ticket for [PII] on [PII]'

Input: User account recovery: "Hi Arljind Komla, your account recovery key is 426220045."
Output: User account recovery: "Hi [PII], your account recovery key is [PII]."

Return ONLY the masked text wrapped in masked_outputXML tags:
<masked_output>
[Your masked text here]
</masked_output>"""

# Prepare a prompt for inference using the messages format
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "Hi Balian, we are reaching out to confirm your gaming preferences. Your account, EL@protonmail.com, has been inactive for 46 months. Please verify your account details, including 72611183194555."},
]
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
input_ids = tokenizer(text, return_tensors="pt").input_ids

# Perform inference
output = model.generate(input_ids, max_length=512)

# Decode and print the generated text
print(tokenizer.decode(output[0], skip_special_tokens=True))
```
**Output:**
```
<masked_output>
Hi [PII], we are reaching out to confirm your gaming preferences. Your account, [PII], has been inactive for [PII] months. Please verify your account details, including [PII].
</masked_output>
```

## LoRA Adapter

The unmerged LoRA adapter is available in [lora_adapter.](https://huggingface.co/AdamLucek/Qwen3-4B-Instruct-2507-PII-RL/tree/main/lora_adapter)

## Additional Information

For all other information about the base model and usage, refer to the original [Qwen/Qwen3-4B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507) page.
