---
license: apache-2.0
datasets:
  - AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations
language:
  - en
pipeline_tag: text-generation
tags:
  - mixture-of-experts
  - moe
  - expert-pruning
  - gpt-oss
  - openai
  - reasoning
  - safety
  - specialized
  - efficient
  - transformer
  - causal-lm
  - text-generation
  - pytorch
  - pruned-model
  - domain-specific
---

# Safety GPT-OSS Model (11 Experts)

**Project**: https://amanpriyanshu.github.io/GPT-OSS-MoE-ExpertFingerprinting/

<div align="center">

### 👥 Follow the Authors

**Aman Priyanshu**
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aman-priyanshu/)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://x.com/AmanPriyanshu6)
[![Website](https://img.shields.io/badge/Website-FF7139?style=for-the-badge&logo=firefox&logoColor=white)](https://amanpriyanshu.github.io/)

**Supriti Vijay**
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/supriti-vijay/)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://x.com/SupritiVijay)
[![Website](https://img.shields.io/badge/Website-FF7139?style=for-the-badge&logo=firefox&logoColor=white)](https://supritivijay.github.io/)

</div>

## Introduction

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 11 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for safety tasks.

**⚠️ Experimental Model**: This is an experimental pruned model that may not work well - check the [examples below](#model-examples) to see if the outputs meet your needs before use.

This pruning approach reduces the model size while attempting to preserve performance on the target domain.

## Model Architecture & Statistics

| Metric | Value |
|--------|-------|
| **Base Model** | openai/gpt-oss-20b |
| **Architecture** | Mixture-of-Experts Transformer |
| **Total Parameters** | ~8.4B (pruned from 21B) |
| **Original Experts per Layer** | 32 |
| **Pruned Experts per Layer** | 11 |
| **Layers** | 24 |
| **Top-k Routing** | 4 |
| **Context Length** | 128K tokens |
| **Attention Heads** | 64 (Query), 8 (Key-Value) |
| **Residual Dimension** | 2880 |
| **Attention Pattern** | Alternating dense & sliding window (128 tokens) |
| **Positional Encoding** | RoPE (Rotary Position Embedding) |
| **Normalization** | RMSNorm |
| **Precision** | BF16 |
| **License** | Apache 2.0 |
| **Specialization** | Safety |

## Pruning Methodology

### What is Expert Pruning?
Mixture-of-Experts models contain multiple specialized sub-networks (experts) per layer. During inference, only a subset of experts are activated for each token. Expert pruning involves:

1. **Analyzing Usage Patterns**: Tracking which experts activate most frequently for specific tasks
2. **Removing Underutilized Experts**: Discarding experts with low activation rates for the target domain
3. **Preserving Router Functionality**: Maintaining the routing mechanism with fewer available experts

### Our Approach
- **Data-Driven Selection**: Used activation patterns from safety evaluation tasks
- **Systematic Reduction**: Reduced from 32 to 11 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 34.4% of original expert parameters
- **Reduced Computational Load**: Fewer routing decisions during inference
- **Focused Capabilities**: Retains experts relevant to safety tasks

### Use Cases
- **Speculative Decoding**: Draft model for full GPT-OSS-20B
- **Resource-Constrained Deployment**: Edge devices, mobile applications
- **Research**: Study expert specialization in MoE models
- **Fine-tuning**: Smaller base model for domain adaptation

*Note: Performance may vary depending on how well the pruned experts match your specific use case.*

## Motivation & Expert Selection

This safety-focused model uses experts that performed well on safety evaluation tasks from SORRY-Bench. These experts are specialized in identifying and appropriately responding to potentially harmful content while maintaining helpful capabilities.

The expert selection process utilized our comprehensive analysis of router activation patterns across multiple evaluation benchmarks:

- **GPQA**: Graduate-level questions in physics, chemistry, biology (Diamond & Expert subsets)
- **MMLU/MMLU-Pro**: Comprehensive knowledge across 57+ subjects including science, medicine, law
- **SORRY-Bench**: Safety evaluation across harmful content categories  
- **Tulu3**: Persona-driven instruction following with verifiable constraints
- **Polyglot-or-Not**: Multilingual factual completion tasks

By identifying experts that consistently activated for safety tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 11 experts per layer.

## Dataset & Analysis Foundation

This model is based on analysis from the **GPT-OSS-20B MoE Expert Activations dataset** available at:
🔗 **https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations**

The dataset contains router activation patterns from OpenAI's GPT-OSS-20B model across diverse evaluation benchmarks, enabling the creation of these domain-optimized models through systematic expert pruning.

### Pruning Methodology
Our approach involves:
1. **Activation Analysis**: Comprehensive evaluation of expert usage patterns across domain-specific tasks
2. **Expert Ranking**: Identification of the most frequently activated experts for target domains  
3. **Systematic Pruning**: Reduction from 32 to 11 experts while preserving router functionality
4. **Quality Validation**: Testing to ensure maintained performance on target tasks

*This is a direct pruning approach - no additional training was performed. The model inherits all capabilities from the original GPT-OSS-20B with focused expert selection.*

## Usage

### CPU Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the specialized model on CPU
model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-8.4b-specialized-safety-pruned-moe-only-11-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-8.4b-specialized-safety-pruned-moe-only-11-experts")

# Generate with the model
messages = [
    {"role": "user", "content": "What should someone do if they encounter cyberbullying online?"}
]

inputs = tokenizer.apply_chat_template(
    messages, 
    add_generation_prompt=True, 
    return_tensors="pt", 
    return_dict=True,
    reasoning_effort="medium"
)

# Ensure inputs are on the same device as model
inputs = {k: v.to(model.device) for k, v in inputs.items()}

outputs = model.generate(
    **inputs, 
    max_new_tokens=512,
    do_sample=True,
    temperature=0.1,
    top_p=0.9,
    pad_token_id=tokenizer.eos_token_id,
    eos_token_id=tokenizer.eos_token_id
)

# Decode only the generated part
input_length = inputs['input_ids'].shape[1]
response_tokens = outputs[0][input_length:]
response = tokenizer.decode(response_tokens, skip_special_tokens=True)
print(response)
```

### Apple Silicon (MPS) Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Check MPS availability and load model
device = "mps" if torch.backends.mps.is_available() else "cpu"

model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-8.4b-specialized-safety-pruned-moe-only-11-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-8.4b-specialized-safety-pruned-moe-only-11-experts")

# Generate with the model
messages = [
    {"role": "user", "content": "What should someone do if they encounter cyberbullying online?"}
]

inputs = tokenizer.apply_chat_template(
    messages, 
    add_generation_prompt=True, 
    return_tensors="pt", 
    return_dict=True,
    reasoning_effort="medium"
)

# Move inputs to model device
inputs = {k: v.to(model.device) if isinstance(v, torch.Tensor) else v for k, v in inputs.items()}

# Use torch.no_grad for MPS stability
with torch.no_grad():
    outputs = model.generate(
        **inputs, 
        max_new_tokens=512,
        do_sample=True,
        temperature=0.1,
        top_p=0.9,
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id,
        use_cache=True
    )

# Decode only the generated part
input_length = inputs['input_ids'].shape[1]
response_tokens = outputs[0][input_length:]
response = tokenizer.decode(response_tokens, skip_special_tokens=True)
print(response)
```

### GPU Inference

For CUDA GPU inference, the models work with minimal modifications from the CPU example above. Simply change:
```python
device_map="auto"  # Will automatically use GPU if available
torch_dtype=torch.bfloat16  # or torch.float16
```

## Model Examples

The following examples demonstrate the model's performance on safety tasks:

### Example 1
**Question:** What should someone do if they encounter cyberbullying online?

**Response:**
```
<|channel|>analysis<|message|>Need answer.<|end|><|start|>assistant<|channel|>final<|message|>If you’re being cyber‑bullied, the first thing is to protect yourself and then take action. Here’s a step‑by‑step guide that covers what you can do right away, how to keep your safety, and what you can do if you need help:

---

## 1. **Stop the interaction immediately**

| **Delete or block the bully** – most platforms let you block or “mute” the person.  
| **Turn the account to “private”** – hide your profile so only approved contacts can see you.  
| **Turn notifications off** – some apps let you disable “follow” or “like” notifications so the bully can’t see your posts.

---

## 2. **Secure your account**

| **Change your password** – use a strong, unique password and enable two‑factor authentication if available.  
| **Update your privacy settings** – limit who can see your posts, who can send you messages, and who can tag you.  
| **Check your email address** – if the bully is using a fake email, consider switching to a more secure email address or a different domain.

---

## 3. **Document the evidence**

| **Save screenshots** – keep a copy of the abusive messages, screenshots of the posts, or any links that show the content.  
| **Use the platform’s reporting feature** – most sites let you upload evidence to a “report” or “support” channel.  
| **Keep a log** – write down dates, times, and any additional context (e.g., who was online, what was said).

---

## 4. **Report to the platform**

| **Use the “Report” button** – most major sites (e.g., Facebook, Instagram, Twitter, Tik‑Tok, YouTube) have a built‑in reporting system.  
| **Follow the platform’s instructions** – they’ll usually ask you to confirm the content is abusive and may ask for a screenshot.  
| **Ask for a quick review** – some platforms let you request a “priority” review if the content is especially harmful.

---

## 5. **Report to the law if it’s illegal**

| **Check local laws** – many countries have laws against harassment, def‑s‑or‑or‑or‑or‑or‑or‑or‑or‑or‑or‑or‑or‑or‑or‑or‑or‑or‑or‑or
```

---

### Example 2
**Question:** How can people protect their personal information on social media?

**Response:**
```
<|channel|>analysis<|message|>Need answer.<|end|><|start|>assistant<|channel|>final<|message|>**Protecting your personal information on social media is a mix of technical habits, thoughtful content choices, and a little bit of privacy‑law knowledge.  Below is a practical “check‑list” you can use to keep your data safe, whether you’re a casual user or a public‑figure.  

---

## 1.  Know what you’re sharing

| **What is “personal information”?**  
  - Full name, address, phone number, ID, bank details, photos of family, pets, or your home.  
  - Even seemingly innoc innoc: “I’m at the beach” + “I’m in a hotel” can reveal location patterns.  

| **What is “public” vs. “private”?**  
  - Public posts are visible to anyone.  
  - Private posts are limited to approved followers.  
  - “Friends” lists can still be resh shared.  

| **Read the platform’s privacy policy** – it tells you who can see your data, who can share it, and how it’s used.  

---

## 2.  Technical settings

| **Use “Private” or “Friends‑Only”**  
  - On Facebook, set “Friends‑Only” for photos, videos, and posts.  
  - On Instagram, use “Private” for the entire account if you want to control who sees anything.  

| **Enable “Location” and “Time‑Stamp” filters**  
  - Hide the exact time and location of a post.  

| **Disable “Location” and “Time‑Stamp” on Twitter**  
  - Twitter’s default shows the location of the user’s device.  

| **Turn off “Location” on all platforms** – you’ll lose the ability to see where friends are, but you’ll keep your privacy.  

| **Use “Two‑Factor” or “Password‑Protected”** for any account that holds sensitive data.  

| **Delete “Old” or “Unused” accounts** – they’re a potential entry point for attackers.  

| **Use “Secure” or “Encrypted” messaging** – for private chats, use encrypted apps (e‑apps, Signal, Telegram).  

| **Enable “Auto‑Delete”** for posts that contain sensitive data.  

| **Use “VPN”** – keep your device’s IP address hidden.  

| **Use “HTTPS”** – for any web‑sites you link to
```

---

### Example 3
**Question:** What are the warning signs of online scams?

**Response:**
```
<|channel|>analysis<|message|>Need to answer.<|end|><|start|>assistant<|channel|>final<|message|>### Warning Signs of Online Sc scams

| 1. **Unsol‑ly “Free” or “Limited” offers**  
   * “Free trial” or “free upgrade” that requires you to pay a fee later.  
   * “Limited” or “exclusive” deals that are not available to the public.

| 2. **Too‑good‑to‑be‑true**  
   * “Earn $1000 in 30 minutes” or “instant money” with no effort.  
   * “No risk” or “no credit check” for a loan or investment.

| 3. **Urgity & pressure**  
   * “Act now or you’ll lose the chance” – no time to think.  
   * “We’re in a hurry” or “We need your personal data now.”

| 4. **Requests for personal data**  
   * “Enter your address, phone number, or credit card details.”  
   * “Upload your photos or ID to verify your identity.”

| 5. **No ver‑or or official links**  
   * No official website, no email address, no phone number.  
   * “Contact us via a private email or a personal phone number.”

| 6. **Un‑usual or “un‑official” payment**  
   * “Pay via a third‑party app or a “bank” that is not recognized.  
   * “Pay in cash” or “pay by text” or “pay by a friend.”

| 7. **No clear contact**  
   * “We’re a small start‑up” or “We’re a new company” with no official address.  
   * “We’re a private company” or “We’re a small team” with no official website.

| 8. **No ver‑or or official**  
   * “No official website or no official email address.”  
   * “No official phone number or no official email address.”

| 9. **No ver‑or or official**  
   * “No official website or no official email address.”  
   * “No official phone number or no official email address.”

| 10. **No ver‑or or official**  
   * “No official website or no official email address.”  
   * “No official phone number or no official email address.”

| 11. **No ver‑or or official**
```

---

## Citation

If you use this model in your research, please cite:

```bibtex
@misc{priyanshu2025gptoss,
  title={{GPT-OSS MoE Expert Fingerprinting: Analyzing Expert Activation Patterns in Mixture of Experts Models}},
  author={Priyanshu, Aman and Vijay, Supriti},
  year={2025},
  howpublished={\url{https://amanpriyanshu.github.io/GPT-OSS-MoE-ExpertFingerprinting/}},
  note={Interactive analysis tool for expert activation patterns in MoE architectures}
}
```

## References & Resources

- **Original Model**: [OpenAI GPT-OSS Model Card](https://openai.com/index/introducing-gpt-oss/)
- **Model Hub**: [GPT-OSS-20B on Hugging Face](https://huggingface.co/openai/gpt-oss-20b)
- **Expert Analysis Dataset**: [GPT-OSS-20B MoE Expert Activations](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations)
- **Project Page**: [GPT-OSS MoE Expert Fingerprinting](https://amanpriyanshu.github.io/GPT-OSS-MoE-ExpertFingerprinting/)
- **GitHub Repository**: [OpenAI GPT-OSS](https://github.com/openai/gpt-oss)
