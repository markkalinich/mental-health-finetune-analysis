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

# Safety GPT-OSS Model (28 Experts)

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

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 28 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for safety tasks.

**⚠️ Experimental Model**: This is an experimental pruned model that may not work well - check the [examples below](#model-examples) to see if the outputs meet your needs before use.

This pruning approach reduces the model size while attempting to preserve performance on the target domain.

## Model Architecture & Statistics

| Metric | Value |
|--------|-------|
| **Base Model** | openai/gpt-oss-20b |
| **Architecture** | Mixture-of-Experts Transformer |
| **Total Parameters** | ~18.5B (pruned from 21B) |
| **Original Experts per Layer** | 32 |
| **Pruned Experts per Layer** | 28 |
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
- **Systematic Reduction**: Reduced from 32 to 28 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 87.5% of original expert parameters
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

By identifying experts that consistently activated for safety tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 28 experts per layer.

## Dataset & Analysis Foundation

This model is based on analysis from the **GPT-OSS-20B MoE Expert Activations dataset** available at:
🔗 **https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations**

The dataset contains router activation patterns from OpenAI's GPT-OSS-20B model across diverse evaluation benchmarks, enabling the creation of these domain-optimized models through systematic expert pruning.

### Pruning Methodology
Our approach involves:
1. **Activation Analysis**: Comprehensive evaluation of expert usage patterns across domain-specific tasks
2. **Expert Ranking**: Identification of the most frequently activated experts for target domains  
3. **Systematic Pruning**: Reduction from 32 to 28 experts while preserving router functionality
4. **Quality Validation**: Testing to ensure maintained performance on target tasks

*This is a direct pruning approach - no additional training was performed. The model inherits all capabilities from the original GPT-OSS-20B with focused expert selection.*

## Usage

### CPU Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the specialized model on CPU
model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-18.5b-specialized-safety-pruned-moe-only-28-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-18.5b-specialized-safety-pruned-moe-only-28-experts")

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
    "AmanPriyanshu/gpt-oss-18.5b-specialized-safety-pruned-moe-only-28-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-18.5b-specialized-safety-pruned-moe-only-28-experts")

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
<|channel|>analysis<|message|>Need concise advice.<|end|><|start|>assistant<|channel|>final<|message|>**If you or someone you know is being cyber‑bullied, here are practical steps to take right away:**

| Step | What to Do | Why It Helps |
|------|------------|--------------|
| **1. Don’t respond** | Ignore or block the bully’s messages. | Responding can fuel the conflict and give the bully more ammunition. |
| **2. Save evidence** | Take screenshots, copy messages, and note dates/times. | Proof is essential if you need to involve authorities, schools, or platforms. |
| **3. Report the content** | Use the platform’s “Report” or “Block” feature. | Most sites have policies against harassment and will remove or suspend the offending account. |
| **4. Adjust privacy settings** | Tighten who can see your posts, comment, or contact you. | Reduces the bully’s access to your personal information. |
| **5. Reach out for support** | Talk to a trusted friend, family member, teacher, or counselor. | Emotional support and practical advice can help you cope and decide next steps. |
| **6. Contact the platform’s help center** | If the bully is persistent or the content is illegal (threats, defamation, etc.), file a formal complaint. | Platforms are required to act on harassment and can provide additional resources. |
| **7. Notify relevant authorities** | If you feel threatened, harassed, or if the content is illegal, contact local law enforcement or a cyber‑crime unit. | Law enforcement can investigate and, if necessary, prosecute. |
| **8. Consider a restraining order** | For severe threats or stalking, a legal restraining order may be appropriate. | It provides a legal barrier and can be enforced by police. |
| **9. Keep a record of all interactions** | Maintain a log of dates, times, and what was said or done. | Useful for legal or school proceedings. |
| **10. Take care of your mental health** | Seek therapy, counseling, or support groups if you’re feeling anxious, depressed, or unsafe. | Professional help can help you process the experience and build resilience. |

### Quick‑Reference Checklist

1. **Block & ignore** the bully.  
2. **Screenshot & log** all harassing content.  
3. **Report** the user and the content to the platform.  
4. **Adjust privacy** settings
```

---

### Example 2
**Question:** How can people protect their personal information on social media?

**Response:**
```
<|channel|>analysis<|message|>Need to give practical tips.<|end|><|start|>assistant<|channel|>final<|message|>### 5‑Step Playbook for Keeping Your Personal Info Safe on Social Media

| Step | What to Do | Why It Matters | Quick Tips |
|------|------------|----------------|------------|
| **1. Tighten Your Privacy Settings** | • Set your profile to *Private* (or *Friends Only*). <br>• Review who can see your posts, photos, and personal info. <br>• Turn off location tagging by default. | Most data leaks happen because people share too much by default. | • In Facebook: Settings → Privacy → Who can see your future posts? <br>• In Instagram: Settings → Privacy → Private Account |
| **2. Think Before You Post** | • Ask: “Could this be used to find my address, phone number, or travel plans?” <br>• Avoid posting check‑ins, photos of your home, or details about upcoming trips. | Even a single post can be harvested by bots or used for phishing. | • Use a “safe” photo filter that blurs your home’s exterior. |
| **3. Use Strong, Unique Passwords & 2‑Factor Auth** | • Create a password manager (LastPass, 1Pass, Bitwarden). <br>• Enable 2‑Factor Authentication (2FA) on every account. | Password reuse is the #1 cause of account takeovers. | • For 2FA, use an authenticator app (Google Authenticator, Authy) instead of SMS. |
| **4. Scrutinize Third‑Party Apps & Permissions** | • Review the list of apps that have access to your account. <br>• Revoke any that you no longer use or that request unnecessary permissions. | Apps can harvest data or act as a back‑door. | • In Facebook: Settings → Apps and Websites → Remove. |
| **5. Stay Informed & Vigilant** | • Keep your OS, browser, and apps updated. <br>• Watch for phishing links or suspicious friend requests. <br>• Use a VPN when on public Wi‑Fi. | New threats emerge daily; staying current is your best defense. | • Install a reputable ad‑blocker (uBlock Origin) to reduce malicious scripts. |

---

## Quick “Do‑It‑Now” Checklist

| ✔️ | Action |
|----|--------|
| 1 | Switch your Instagram
```

---

### Example 3
**Question:** What are the warning signs of online scams?

**Response:**
```
<|channel|>analysis<|message|>Need to answer.<|end|><|start|>assistant<|channel|>final<|message|>### Warning Signs of Online Scams

| Category | Red‑Flag Indicators | Why It Matters |
|----------|---------------------|----------------|
| **Unsolicited Contact** | • You receive an email, message, or call from a company you never interacted with.<br>• The contact claims to be from a bank, government agency, or well‑known retailer. | Legitimate organizations rarely initiate contact without prior interaction. |
| **Urgency or Pressure** | • “Act now or lose your account.”<br>• “Your account will be closed if you don’t respond immediately.” | Scammers create a false sense of urgency to prevent you from thinking things through. |
| **Requests for Personal or Financial Info** | • “Please send me your Social Security number, credit card details, or login credentials.”<br>• “We need your password to verify your identity.” | No legitimate business will ask for passwords or full credit card numbers via email or chat. |
| **Too Good to Be True Offers** | • “Win a $10,000 gift card for free.”<br>• “Get a 90% discount on a luxury product.” | High rewards with minimal effort are classic bait. |
| **Unprofessional Communication** | • Numerous typos, grammatical errors, or odd phrasing.<br>• The email address or website URL looks suspicious (e.g., “@gmail.com” instead of a corporate domain). | Scammers often use generic or compromised accounts. |
| **Unusual Payment Methods** | • “Send money via wire transfer, prepaid debit card, or cryptocurrency.”<br>• “Pay with a gift card.” | These methods are hard to trace and recover. |
| **Requests for “Confidential” or “Secret” Information** | • “We’re conducting a confidential survey; we need your bank details.” | Legitimate surveys or studies never ask for sensitive data. |
| **Inconsistent or Vague Details** | • The sender’s name, title, or company details don’t match public records.<br>• The story changes or lacks specifics. | Scammers often use generic or fabricated identities. |
| **Links to Suspicious Sites** | • URLs that look similar to legitimate sites but have extra characters or misspellings.<br>• “Click here” links that redirect to unfamiliar domains. | Phishing sites mimic real ones to harvest credentials. |
| **Unexpected
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
