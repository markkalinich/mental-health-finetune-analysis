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

# Safety GPT-OSS Model (14 Experts)

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

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 14 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for safety tasks.

**⚠️ Experimental Model**: This is an experimental pruned model that may not work well - check the [examples below](#model-examples) to see if the outputs meet your needs before use.

This pruning approach reduces the model size while attempting to preserve performance on the target domain.

## Model Architecture & Statistics

| Metric | Value |
|--------|-------|
| **Base Model** | openai/gpt-oss-20b |
| **Architecture** | Mixture-of-Experts Transformer |
| **Total Parameters** | ~10.2B (pruned from 21B) |
| **Original Experts per Layer** | 32 |
| **Pruned Experts per Layer** | 14 |
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
- **Systematic Reduction**: Reduced from 32 to 14 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 43.8% of original expert parameters
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

By identifying experts that consistently activated for safety tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 14 experts per layer.

## Dataset & Analysis Foundation

This model is based on analysis from the **GPT-OSS-20B MoE Expert Activations dataset** available at:
🔗 **https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations**

The dataset contains router activation patterns from OpenAI's GPT-OSS-20B model across diverse evaluation benchmarks, enabling the creation of these domain-optimized models through systematic expert pruning.

### Pruning Methodology
Our approach involves:
1. **Activation Analysis**: Comprehensive evaluation of expert usage patterns across domain-specific tasks
2. **Expert Ranking**: Identification of the most frequently activated experts for target domains  
3. **Systematic Pruning**: Reduction from 32 to 14 experts while preserving router functionality
4. **Quality Validation**: Testing to ensure maintained performance on target tasks

*This is a direct pruning approach - no additional training was performed. The model inherits all capabilities from the original GPT-OSS-20B with focused expert selection.*

## Usage

### CPU Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the specialized model on CPU
model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-10.2b-specialized-safety-pruned-moe-only-14-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-10.2b-specialized-safety-pruned-moe-only-14-experts")

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
    "AmanPriyanshu/gpt-oss-10.2b-specialized-safety-pruned-moe-only-14-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-10.2b-specialized-safety-pruned-moe-only-14-experts")

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
<|channel|>analysis<|message|>Need advice.<|end|><|start|>assistant<|channel|>final<|message|>**If you’re being cyber‑bullied, you’re not alone and you don’t have to face it alone.**  
Below is a step‑by‑step guide that covers what you can do right away, how to protect yourself, and how to seek help if the situation escalates.

---

## 1. **Take a Moment to Pause**

| What to do | Why it matters |
|---|---|
| **Read the content** – not just the headline or a single comment. | Gives you context and helps you decide how to respond. |
| **Check your emotions** – are you angry, sad, or feeling unsafe? | Knowing how you feel helps you choose the right next step. |
| **Decate a response** – do you want to ignore, block, or reply? | Your reaction can influence the bully’s behavior. |

---

## 2. **Decate a Response (or a Non‑Response)**

| Option | When it’s useful |
|---|---|
| **Ignore** | If the bully is just shouting or posting random insults. |
| **Block/Unfollow** | If the content is personal harassment or you feel threatened. |
| **Report** | If the content violates platform rules (hate‑speech, threats, def‑s‑ing, etc.). |
| **Reply (caly‑cal)** | If you want to set a boundary or educate the bully. Use calm, factual language. |
| **Document** | Save screenshots or copy the offending text. | For evidence if you need to involve authorities or a support group. |

---

## 3. **Use Platform Tools**

| Platform | Key tools |
|---|---|
| **Facebook / Instagram** | Block, Report, Delete post, Report a user. |
| **Twitter** | Block, Report, Report a tweet. |
| **YouTube** | Report a video, Block a user, Report a comment. |
| **Discord / Twitch** | Report a user, Report a stream, Use “Mute” or “Block.” |
| **General** | Most platforms have a “Report” button or a “Block” feature. |

**Tip:**  
- **Save the evidence** before deleting it.  
- **Use the “Report” button** – it’s usually the quickest way to get moderation action.

---

## 4. **Protect Your Personal Data**

| What to do | Why it
```

---

### Example 2
**Question:** How can people protect their personal information on social media?

**Response:**
```
<|channel|>analysis<|message|>Need to give tips.<|end|><|start|>assistant<|channel|>final<|message|>### 1. **Think About What You Share**

| **What to Avoid** | Why it matters |
|---------------------|---------------------|
| Full address, phone number, or workplace | Gives a location for stalking or phishing |
| Current photos of you or your family | Makes it easier to identify you |
| Detailed travel plans or vacation dates | Enables “check‑in” attacks |
| Sensitive financial info (bank accounts, credit cards) | Directs scammers to your money |
| Passwords, PINs, or security codes | Gives attackers a direct entry point |

**Rule:** *Only share what you’re comfortable with and that won’t help someone locate or target you.*

---

### 2. **Use Privacy Settings Wisely**

| Platform | Key Settings |
|---------------------|---------------------|
| **Facebook** | `People who can see posts` → “Friends” or “Close friends” |
| **Instagram** | `Location` → “Hide location” or “Only share with selected people” |
| **Twitter** | `Followers` → “Private” or “Protected” (if you’re a public figure) |
| **LinkedIn** | `Connections` → “Close connections” and use “Private” for posts |

**Tip:** Regularly review the settings; they can change with platform updates.

---

### 3. **Use Strong, Unique Passwords**

| Method | Example |
|---------------------|---------------------|
| **Pass‑phrase** | `S4!@#-2024` (mix letters, numbers, symbols) |
| **Password manager** | `LastPass`, `Bitwarden` – store, rotate, and auto‑update |
| **Two‑factor authentication** | Add a second layer (SMS, authentica‑app) |

**Rule:** Never reuse passwords across accounts.

---

### 4. **Enable “Two‑Factor Authentication” (2‑FA)**

| Platform | How to enable |
|---------------------|---------------------|
| **Google** | `Google Authenticator` or `G‑Auth` |
| **Apple** | `Apple Watch` or `Apple ID` |
| **Facebook** | `Facebook Two‑Factor` (SMS or Authenticator) |
| **Instagram** | `Instagram Two‑Factor` (SMS or Authenticator) |

**Benefit:** Even if someone gets your password, they still need the second factor.

---

### 5.
```

---

### Example 3
**Question:** What are the warning signs of online scams?

**Response:**
```
<|channel|>analysis<|message|>Need to list warning signs.<|end|><|start|>assistant<|channel|>final<|message|>### Warning Signs of Online Sc scams

| # | Red Flag | Why It Matters | How to Spot It |
|---|---|---|---|
| 1 | **Too Good, Too Fast** | “Earn $10,000 in 30 minutes” or “Instant credit” | If the offer sounds unbelievably fast or high‑pay for minimal effort, it’s likely a scam. |
| 2 | **Unverified Payment Methods** | “Pay via a free app, no bank” | Legitimate businesses use secure, traceable payment channels (bank, credit card, verified payment apps). |
| 3 | **Urgity & Pressure** | “Act now or lose your chance” | Scers create panic to bypass rational checks. |
| 4 | **No Real Contact Info** | “Only email” or “No phone number” | Real companies provide multiple ways to verify identity. |
| 5 | **Requests for Personal Data** | “Send your SSN, bank details” | Legit sites never ask for sensitive info upfront. |
| 6 | **Unprofessional Language** | Typo, slang, or broken grammar | Scers often copy or paste generic templates. |
| 7 | **Too Much “Personal” Attention** | “I’m your friend” or “I’ve been waiting for you” | Scers use emotional manipulation to lower defenses. |
| 8 | **Unclear Terms** | “No contract, no fees” | Legit offers have clear terms, conditions, and a privacy policy. |
| 9 | **No Verification of Identity** | “I’m a real person” but no proof | Real professionals provide credentials, licenses, or a business website. |
| 10 | **Too Many “Free” Services** | “Free trial, no cost” | Free offers are common, but “free” plus “instant” plus “big reward” is a red flag. |
| 11 | **Requests for “Help” with Payment** | “I need you to transfer money for me” | Legit sites handle payments themselves; they never ask you to act as a middleman. |
| 12 | **Unusual Payment Timing** | “Pay in 2 days, then we’ll pay you” | Scers delay their own payment to avoid traceability. |
| 13 | **No Real Reviews or Reputation** | “No website, no reviews”
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
