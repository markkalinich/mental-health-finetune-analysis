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

# Safety GPT-OSS Model (20 Experts)

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

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 20 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for safety tasks.

**⚠️ Experimental Model**: This is an experimental pruned model that may not work well - check the [examples below](#model-examples) to see if the outputs meet your needs before use.

This pruning approach reduces the model size while attempting to preserve performance on the target domain.

## Model Architecture & Statistics

| Metric | Value |
|--------|-------|
| **Base Model** | openai/gpt-oss-20b |
| **Architecture** | Mixture-of-Experts Transformer |
| **Total Parameters** | ~13.7B (pruned from 21B) |
| **Original Experts per Layer** | 32 |
| **Pruned Experts per Layer** | 20 |
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
- **Systematic Reduction**: Reduced from 32 to 20 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 62.5% of original expert parameters
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

By identifying experts that consistently activated for safety tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 20 experts per layer.

## Dataset & Analysis Foundation

This model is based on analysis from the **GPT-OSS-20B MoE Expert Activations dataset** available at:
🔗 **https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations**

The dataset contains router activation patterns from OpenAI's GPT-OSS-20B model across diverse evaluation benchmarks, enabling the creation of these domain-optimized models through systematic expert pruning.

### Pruning Methodology
Our approach involves:
1. **Activation Analysis**: Comprehensive evaluation of expert usage patterns across domain-specific tasks
2. **Expert Ranking**: Identification of the most frequently activated experts for target domains  
3. **Systematic Pruning**: Reduction from 32 to 20 experts while preserving router functionality
4. **Quality Validation**: Testing to ensure maintained performance on target tasks

*This is a direct pruning approach - no additional training was performed. The model inherits all capabilities from the original GPT-OSS-20B with focused expert selection.*

## Usage

### CPU Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the specialized model on CPU
model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-13.7b-specialized-safety-pruned-moe-only-20-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-13.7b-specialized-safety-pruned-moe-only-20-experts")

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
    "AmanPriyanshu/gpt-oss-13.7b-specialized-safety-pruned-moe-only-20-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-13.7b-specialized-safety-pruned-moe-only-20-experts")

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
Below is a practical, step‑by‑step guide that covers what to do right away, how to protect yourself, and how to seek help if the situation escalates.

---

## 1. Stay Calm & Don’t Respond Immediately

| **Why** | **What to Do** |
|---------|----------------|
| A bully’s goal is to provoke an emotional reaction. | Take a pause. 5–10 minutes can be enough to cool down. |
| Responding in anger can give the bully more ammunition. | Write down your feelings first, then decide if you want to reply. |
| If you’re unsure, skip replying entirely. | Let the bully know you’re not engaging. |

---

## 2. Preserve Evidence

| **Action** | **Tools** | **Why It Matters** |
|------------|-----------|-----------------|
| Save screenshots, messages, posts, or any relevant content. | • Phone or computer camera<br>• Cloud storage (Google Drive, Dropbox)<br>• Dedicated note‑taking apps (Evernote, Notion) | Evidence is needed if you report the abuse to a platform, school, or law enforcement. |
| Keep the original file format (do not edit). | • Use the platform’s built‑in screenshot feature if available | Tampering can be used against you. |
| Log dates, times, and usernames. | • Simple spreadsheet or a dedicated “bullying log” | Helps establish a pattern. |

---

## 3. Block / Filter the Bully

| **Platform** | **How to Block** | **Why** |
|--------------|-----------------|--------|
| Facebook, Instagram, Twitter | Use “Block” or “Mute” options. | Stops them from contacting you. |
| Discord, Twitch, Roblox | Use “Block” or “Report” features. | Keeps them from seeing your content. |
| Email / Messaging apps | Add to “Blocked” list or change your email address. | Prevents further messages. |

> **Tip:** If the bully is a friend or acquaintance, consider muting or temporarily disabling the account instead of deleting it—this keeps you safe while preserving your social network.

---

## 4. Report the Abuse

| **Where to Report** | **What to Include** | **Outcome** |
|
```

---

### Example 2
**Question:** How can people protect their personal information on social media?

**Response:**
```
<|channel|>analysis<|message|>Need to give tips.<|end|><|start|>assistant<|channel|>final<|message|>### Protecting Your Personal Information on Social Media  
Social media platforms are great for staying connected, but they also expose you to a range of privacy risks—from casual data leaks to targeted phishing attacks. Below is a practical, step‑by‑step guide that covers the most effective ways to keep your personal information safe, no matter which platform you’re using.

---

## 1. **Start with the Basics: Settings & Permissions**

| Platform | Key Settings to Check | Why It Matters |
|----------|------------------------|----------------|
| **All** | **Profile Visibility** | Set to “Friends only” or “Private” so strangers can’t see your posts. |
| **All** | **Location Sharing** | Disable “Location” or “Check‑in” features unless you’re comfortable sharing your whereabouts. |
| **All** | **Contact Information** | Remove phone numbers, email addresses, or addresses from your profile. |
| **All** | **Third‑Party Apps** | Use the “Apps & Integrations” tab to revoke access for any app that no longer needs your data. |
| **All** | **Password & Two‑Factor Authentication (2FA)** | Use a unique, strong password and enable 2FA (SMS, authenticator app, or biometric). |

> **Tip:** Most platforms let you set a “public” vs. “private” mode for posts. Keep sensitive content (photos of your home, travel plans, etc.) in private mode.

---

## 2. **Think Before You Post**

| Content | Risk | Mitigation |
|----------|------|------------|
| **Photos & Videos** | Facial recognition, location inference | Blur background, avoid posting from inside your home, use “safe mode” filters. |
| **Personal Details** | Phone number, address, birthdate | Use a “safe” profile that omits these details; share them only with close contacts. |
| **Travel Plans** | Enables “check‑in” attacks | Post travel plans after you’ve already arrived, not before. |
| **Sensitive Work Info** | Corporate data leaks | Keep work‑related content on a separate, private account. |

> **Rule of Thumb:** If you’re not 100% comfortable with strangers seeing a piece of content, don’t post it.

---

## 3. **Use Strong, Unique Passwords & 2FA**

1. **Password**  
   - Length
```

---

### Example 3
**Question:** What are the warning signs of online scams?

**Response:**
```
<|channel|>analysis<|message|>Need to answer.<|end|><|start|>assistant<|channel|>final<|message|>### Warning Signs of Online Scams

| Category | Red Flag | Why It Matters |
|----------|-----------|----------------|
| **Unsolicited Contact** | You receive a message or email from a person or company you never heard of. | Scammers often start with a “cold” approach to lure victims. |
| **Urgency / Pressure** | The sender says you must act immediately or you’ll lose a huge opportunity. | Legitimate offers give time for research; urgency forces rash decisions. |
| **Too‑Good‑to‑Be‑True Offers** | “Free money,” “guaranteed 10‑fold return,” or “win a luxury vacation” with no effort. | High‑return promises with no risk are classic bait. |
| **Requests for Personal Info** | Asking for your social‑security number, bank details, passwords, or photos. | Legitimate entities never ask for sensitive data via email or chat. |
| **Unprofessional Communication** | Typos, broken grammar, or generic greetings (“Dear Customer”). | Scammers often use mass‑sent, poorly edited messages. |
| **Unusual Payment Methods** | “Send money via wire transfer, gift cards, or cryptocurrency.” | These methods are hard to trace and recover. |
| **No Verifiable Contact Info** | No phone number, physical address, or official website. | Real companies provide multiple ways to verify identity. |
| **Too Many “Friends” or “Followers”** | A profile with thousands of followers but no real engagement. | Fake social‑media profiles are used to create false credibility. |
| **Requests for “Help” or “Assistance”** | “I need you to help me transfer money” or “I’m stuck, can you help?” | Scammers often pose as victims or friends in distress. |
| **Inconsistent or Contradictory Details** | Dates, names, or facts that don’t line up. | Legitimate offers are consistent; scammers slip up. |
| **Unusual Language or Tone** | Over‑formal, overly friendly, or overly aggressive. | Scammers try to manipulate emotions. |
| **No Clear Return Policy** | “No refunds” or “All sales final.” | Legitimate sellers usually have a return or refund policy. |
| **Requests for “Confidential” or “Secret” Info** | “This is a private deal, don’t tell anyone
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
