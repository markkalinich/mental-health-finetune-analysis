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

# Safety GPT-OSS Model (29 Experts)

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

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 29 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for safety tasks.

**⚠️ Experimental Model**: This is an experimental pruned model that may not work well - check the [examples below](#model-examples) to see if the outputs meet your needs before use.

This pruning approach reduces the model size while attempting to preserve performance on the target domain.

## Model Architecture & Statistics

| Metric | Value |
|--------|-------|
| **Base Model** | openai/gpt-oss-20b |
| **Architecture** | Mixture-of-Experts Transformer |
| **Total Parameters** | ~19.1B (pruned from 21B) |
| **Original Experts per Layer** | 32 |
| **Pruned Experts per Layer** | 29 |
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
- **Systematic Reduction**: Reduced from 32 to 29 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 90.6% of original expert parameters
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

By identifying experts that consistently activated for safety tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 29 experts per layer.

## Dataset & Analysis Foundation

This model is based on analysis from the **GPT-OSS-20B MoE Expert Activations dataset** available at:
🔗 **https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations**

The dataset contains router activation patterns from OpenAI's GPT-OSS-20B model across diverse evaluation benchmarks, enabling the creation of these domain-optimized models through systematic expert pruning.

### Pruning Methodology
Our approach involves:
1. **Activation Analysis**: Comprehensive evaluation of expert usage patterns across domain-specific tasks
2. **Expert Ranking**: Identification of the most frequently activated experts for target domains  
3. **Systematic Pruning**: Reduction from 32 to 29 experts while preserving router functionality
4. **Quality Validation**: Testing to ensure maintained performance on target tasks

*This is a direct pruning approach - no additional training was performed. The model inherits all capabilities from the original GPT-OSS-20B with focused expert selection.*

## Usage

### CPU Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the specialized model on CPU
model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-19.1b-specialized-safety-pruned-moe-only-29-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-19.1b-specialized-safety-pruned-moe-only-29-experts")

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
    "AmanPriyanshu/gpt-oss-19.1b-specialized-safety-pruned-moe-only-29-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-19.1b-specialized-safety-pruned-moe-only-29-experts")

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
| **1. Don’t respond** | Avoid replying to the bully’s messages or posts. | Engaging can fuel the conflict and give the bully more ammunition. |
| **2. Save the evidence** | Take screenshots, copy messages, and note dates/times. | Proof is essential if you need to involve authorities, school officials, or platform moderators. |
| **3. Block or mute the bully** | Use the platform’s block/ignore feature. | Stops the bully from contacting you and reduces the chance of further harassment. |
| **4. Report the content** | Use the “Report” button on the post, comment, or account. | Platforms have policies against harassment and can remove the content or suspend the user. |
| **5. Adjust privacy settings** | Tighten who can see your posts, comment, or message you. | Limits the bully’s ability to reach you. |
| **6. Tell a trusted adult** | Share what’s happening with a parent, teacher, counselor, or another adult you trust. | They can offer support, intervene, and help you navigate the situation. |
| **7. Reach out for help** | Contact a helpline or support organization (e.g., 988 in the U.S., Samaritans in the U.K., or local cyber‑bullying hotlines). | Professionals can give you coping strategies and legal advice. |
| **8. Keep a record of all interactions** | Maintain a log of the bully’s messages, your responses, and any reports you’ve filed. | Useful for future reference if the situation escalates. |
| **9. Consider legal action if necessary** | If the bullying includes threats, defamation, or stalking, consult a lawyer or law enforcement. | Legal avenues can provide protection orders or criminal charges. |
| **10. Take care of yourself** | Practice self‑care: exercise, talk to friends, keep a journal, or seek therapy. | Cyberbullying can affect mental health; professional support can help you process emotions. |

---

### Quick‑Reference Checklist

1. **Stop engaging**  
2. **Save evidence**  
3. **Block/ignore**  
4. **Report**  
5. **Adjust
```

---

### Example 2
**Question:** How can people protect their personal information on social media?

**Response:**
```
<|channel|>analysis<|message|>Need to give practical tips.<|end|><|start|>assistant<|channel|>final<|message|>### 5‑Step Playbook for Keeping Your Personal Info Safe on Social Media

| Step | What to Do | Why It Matters | Quick Tips |
|------|------------|----------------|------------|
| **1. Tighten Your Privacy Settings** | Every platform (Facebook, Instagram, TikTok, LinkedIn, etc.) offers a privacy panel. | Default settings are often “public.” | • Go to *Settings → Privacy*.<br>• Set “Who can see my posts?” to *Friends* or *Only me*.<br>• Turn off “Location” and “Tagging” for posts you don’t want to share. |
| **2. Think Before You Post** | Ask yourself: “Could a stranger use this to find me?” | Even innocuous details (birthplace, school, pet’s name) can be used for identity‑theft or phishing. | • Use a generic location (“City”) instead of a specific address.<br>• Avoid posting photos that show your home interior or car. |
| **3. Use Strong, Unique Passwords & 2FA** | A weak password is a one‑click entry point. | Two‑factor authentication (2FA) adds a second layer that most attackers can’t bypass. | • Use a password manager (LastPass, 1Password, Bitwarden).<br>• Enable 2FA via authenticator app (Google Authenticator, Authy) or SMS. |
| **4. Monitor Your Digital Footprint** | Regularly search your name, email, and phone number. | You’ll spot any unfamiliar accounts or data leaks early. | • Set Google Alerts for your name.<br>• Use services like *Have I Been Pwned* to check if your email was in a breach. |
| **5. Be Wary of Third‑Party Apps & Links** | Many apps request “full access” to your profile. | They can harvest data or post on your behalf. | • Only authorize apps you trust and that are necessary.<br>• Scan links with a URL checker (e.g., VirusTotal) before clicking. |

---

## Quick “Do’s & Don’ts” Cheat Sheet

| Do | Don’t |
|----|-------|
| Use a **unique password** for each platform. | Share your password or write it down in plain text. |
| Enable **two‑factor authentication**.
```

---

### Example 3
**Question:** What are the warning signs of online scams?

**Response:**
```
<|channel|>analysis<|message|>Need to answer.<|end|><|start|>assistant<|channel|>final<|message|>### Warning Signs of Online Scams

| Category | Red Flag | Why It Matters | Quick Check |
|----------|----------|----------------|-------------|
| **Unsolicited Contact** | You receive an email, message, or call from a company you never interacted with. | Legitimate businesses usually have a prior relationship or a clear reason to contact you. | Verify the sender’s domain or phone number against the company’s official contact info. |
| **Urgency or Pressure** | “Act now or lose your account!” or “This offer expires in 5 minutes.” | Scammers create a false sense of urgency to prevent you from thinking things through. | Pause, take a break, and research before responding. |
| **Too Good to Be True** | “You’ve won a $10,000 prize!” or “Your account will be upgraded for free.” | Genuine offers rarely come with no strings attached. | Check the company’s official website or contact customer service. |
| **Requests for Personal or Financial Info** | “Please send your SSN, bank account, or credit card details.” | Legitimate companies never ask for sensitive data via unsecured channels. | Never provide such info unless you’re on a verified, secure (HTTPS) site. |
| **Unprofessional Language** | Typos, broken grammar, or overly casual tone. | Professional organizations maintain a certain level of polish. | Look for consistent branding, proper spelling, and a professional tone. |
| **Suspicious Links or Attachments** | “Click here to claim your prize” or an attachment that looks like a PDF but is actually a malicious file. | Links can redirect to phishing sites; attachments can install malware. | Hover over the link to see the real URL; scan attachments with antivirus before opening. |
| **Unverified Payment Methods** | “Send money via Western Union, MoneyGram, or a prepaid debit card.” | These methods are hard to trace and are commonly used by scammers. | Use secure, traceable payment methods (credit card, PayPal, or bank transfer). |
| **No Physical Address or Contact Details** | The message lacks a real street address, phone number, or customer support email. | Legitimate businesses provide multiple ways to verify their identity. | Search the address online; call the listed phone number to confirm. |
| **Inconsistent Branding** | Logos that look slightly off, mismatched colors, or inconsistent fonts. | Sc
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
