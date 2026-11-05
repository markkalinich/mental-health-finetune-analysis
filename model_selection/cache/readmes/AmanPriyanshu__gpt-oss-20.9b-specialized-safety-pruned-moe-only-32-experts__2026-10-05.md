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

# Safety GPT-OSS Model (32 Experts)

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

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 32 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for safety tasks.

**⚠️ Experimental Model**: This is an experimental pruned model that may not work well - check the [examples below](#model-examples) to see if the outputs meet your needs before use.

This pruning approach reduces the model size while attempting to preserve performance on the target domain.

## Model Architecture & Statistics

| Metric | Value |
|--------|-------|
| **Base Model** | openai/gpt-oss-20b |
| **Architecture** | Mixture-of-Experts Transformer |
| **Total Parameters** | ~20.9B (pruned from 21B) |
| **Original Experts per Layer** | 32 |
| **Pruned Experts per Layer** | 32 |
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
- **Systematic Reduction**: Reduced from 32 to 32 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 100.0% of original expert parameters
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

By identifying experts that consistently activated for safety tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 32 experts per layer.

## Dataset & Analysis Foundation

This model is based on analysis from the **GPT-OSS-20B MoE Expert Activations dataset** available at:
🔗 **https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations**

The dataset contains router activation patterns from OpenAI's GPT-OSS-20B model across diverse evaluation benchmarks, enabling the creation of these domain-optimized models through systematic expert pruning.

### Pruning Methodology
Our approach involves:
1. **Activation Analysis**: Comprehensive evaluation of expert usage patterns across domain-specific tasks
2. **Expert Ranking**: Identification of the most frequently activated experts for target domains  
3. **Systematic Pruning**: Reduction from 32 to 32 experts while preserving router functionality
4. **Quality Validation**: Testing to ensure maintained performance on target tasks

*This is a direct pruning approach - no additional training was performed. The model inherits all capabilities from the original GPT-OSS-20B with focused expert selection.*

## Usage

### CPU Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the specialized model on CPU
model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-20.9b-specialized-safety-pruned-moe-only-32-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-20.9b-specialized-safety-pruned-moe-only-32-experts")

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
    "AmanPriyanshu/gpt-oss-20.9b-specialized-safety-pruned-moe-only-32-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-20.9b-specialized-safety-pruned-moe-only-32-experts")

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
<|channel|>analysis<|message|>Need to give steps: document, don't respond, block, report, seek support, legal options.<|end|><|start|>assistant<|channel|>final<|message|>**If you or someone you know is being cyber‑bullied, here’s a practical, step‑by‑step guide to protect yourself and get help.**  

---

## 1. Stay Calm & Don’t Respond

| Why it matters | What to do |
|-----------------|------------|
| Responding can fuel the bully and give them the “attention” they’re after. | **Do not reply** to harassing messages or posts. |
| It keeps the situation from escalating. | Keep your composure; take a break if you feel overwhelmed. |

---

## 2. Document Everything

| Why it matters | What to do |
|-----------------|------------|
| Evidence is crucial if you need to involve authorities or a platform. | • Take screenshots (or save the URL). <br>• Copy the text of messages. <br>• Note dates, times, and usernames. |
| Keep a separate, secure folder or cloud storage. | Use a password‑protected file or a dedicated “evidence” folder. |

---

## 3. Block & Restrict the Bully

| Platform | How to block |
|----------|--------------|
| **Facebook / Instagram** | Settings → Privacy → Block. |
| **Twitter** | Profile → Block. |
| **WhatsApp** | Open chat → Info → Block contact. |
| **Discord** | Server → User → Block. |
| **Other apps** | Look for “Block” or “Mute” in the user’s profile or chat options. |

*Tip:* After blocking, consider setting your account to “private” or “restricted” so only approved contacts can see your content.

---

## 4. Report the Abuse

| Platform | Where to report |
|----------|-----------------|
| **Facebook / Instagram** | Report button → “Harassment” or “Bullying.” |
| **Twitter** | Report → “Harassing or abusive content.” |
| **WhatsApp** | Report → “Report spam or abuse.” |
| **Discord** | Report → “Report user.” |
| **YouTube / TikTok / Reddit** | Use the “Report” link under the offending content. |

*Tip:* Provide the evidence you collected. The more details you give, the faster the platform can act.

---

## 5. Reach Out for Support

| Who to talk
```

---

### Example 2
**Question:** How can people protect their personal information on social media?

**Response:**
```
<|channel|>analysis<|message|>Need to give practical tips.<|end|><|start|>assistant<|channel|>final<|message|>### 5‑Step Guide to Safeguarding Your Personal Info on Social Media

| Step | What to Do | Why It Matters | Quick Tips |
|------|------------|----------------|------------|
| **1. Tighten Your Privacy Settings** | Most platforms let you control who sees your posts, who can contact you, and whether your profile is searchable. | Default settings are often “public.” | • **Facebook**: Settings → Privacy → Who can see your future posts? <br>• **Instagram**: Settings → Privacy → Account Privacy (switch to Private). <br>• **Twitter**: Settings → Privacy & Safety → Protect your Tweets. |
| **2. Think Before You Share** | Avoid posting sensitive data (home address, phone number, birthdate, travel plans, financial info). | Even “harmless” details can be pieced together by scammers or identity thieves. | • Use a “safe” nickname. <br>• Don’t post exact locations in real time. <br>• Hide your birthday or use a “public” date only. |
| **3. Use Strong, Unique Passwords & 2FA** | A strong password is the first line of defense; two‑factor authentication (2FA) adds a second lock. | Password reuse or weak passwords let attackers access multiple accounts. | • Use a password manager (LastPass, 1Password). <br>• Enable 2FA via authenticator app (Google Authenticator, Authy) or SMS. |
| **4. Monitor Your Digital Footprint** | Regularly search your name, photos, and posts to see what’s publicly visible. | You may not realize how much personal data is out there. | • Google “Your Name” + “Profile” <br>• Use tools like *Have I Been Pwned* to check if your email was in a breach. |
| **5. Be Wary of Third‑Party Apps & Links** | Many apps request permissions that can expose your data; phishing links can steal credentials. | Over‑permitted apps can harvest photos, contacts, or even post on your behalf. | • Review app permissions in Settings → Apps. <br>• Only install apps from official stores. <br>• Hover over links before clicking; look for https:// and correct domain names. |

---
```

---

### Example 3
**Question:** What are the warning signs of online scams?

**Response:**
```
<|channel|>analysis<|message|>Need to answer.<|end|><|start|>assistant<|channel|>final<|message|>### Warning Signs of Online Scams

| # | Warning Sign | Why It Matters | Quick Check |
|---|--------------|----------------|-------------|
| 1 | **Unsolicited Contact** | Scammers often reach out unexpectedly (email, message, call). | Verify the sender’s identity through an official channel (phone number, website). |
| 2 | **Urgency or Pressure** | “Act now!” or “You’ll lose your account if you don’t respond” tactics push you to act without thinking. | Pause, take a break, and research before responding. |
| 3 | **Requests for Personal or Financial Info** | Legitimate companies never ask for passwords, PINs, or full bank statements via email or chat. | Never share sensitive data; use secure, official portals instead. |
| 4 | **Too Good to Be True Offers** | “Free money,” “guaranteed investment returns,” or “instant lottery win” are classic bait. | Check the company’s reputation and look for reviews or complaints. |
| 5 | **Spelling/Grammar Errors** | Many scam messages are poorly written or contain odd phrasing. | Legitimate businesses usually proofread their communications. |
| 6 | **Suspicious Links or Attachments** | Links that don’t match the claimed sender’s domain or attachments that look like PDFs but are actually executables. | Hover over links to see the real URL; use a link scanner (e.g., VirusTotal). |
| 7 | **Unusual Payment Methods** | Requests for wire transfers, prepaid debit cards, or cryptocurrency. | Stick to reputable payment methods (credit card, PayPal, etc.). |
| 8 | **No Contact Information** | No phone number, physical address, or official website. | Verify the business through a search engine or official registry. |
| 9 | **Inconsistent Details** | Names, dates, or facts that don’t match up. | Cross‑check facts with reliable sources. |
|10 | **Too Many “Friends” or “Followers” Claims** | “I’m a celebrity” or “I have 10,000 followers” used to build credibility. | Verify via social media profiles, look for verified badges, or check third‑party sites. |
|11 | **Requests to “Forward” or “Share”** | “Please forward this to your friends” or “Share this post”
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
