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

# Safety GPT-OSS Model (27 Experts)

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

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 27 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for safety tasks.

**⚠️ Experimental Model**: This is an experimental pruned model that may not work well - check the [examples below](#model-examples) to see if the outputs meet your needs before use.

This pruning approach reduces the model size while attempting to preserve performance on the target domain.

## Model Architecture & Statistics

| Metric | Value |
|--------|-------|
| **Base Model** | openai/gpt-oss-20b |
| **Architecture** | Mixture-of-Experts Transformer |
| **Total Parameters** | ~17.9B (pruned from 21B) |
| **Original Experts per Layer** | 32 |
| **Pruned Experts per Layer** | 27 |
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
- **Systematic Reduction**: Reduced from 32 to 27 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 84.4% of original expert parameters
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

By identifying experts that consistently activated for safety tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 27 experts per layer.

## Dataset & Analysis Foundation

This model is based on analysis from the **GPT-OSS-20B MoE Expert Activations dataset** available at:
🔗 **https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations**

The dataset contains router activation patterns from OpenAI's GPT-OSS-20B model across diverse evaluation benchmarks, enabling the creation of these domain-optimized models through systematic expert pruning.

### Pruning Methodology
Our approach involves:
1. **Activation Analysis**: Comprehensive evaluation of expert usage patterns across domain-specific tasks
2. **Expert Ranking**: Identification of the most frequently activated experts for target domains  
3. **Systematic Pruning**: Reduction from 32 to 27 experts while preserving router functionality
4. **Quality Validation**: Testing to ensure maintained performance on target tasks

*This is a direct pruning approach - no additional training was performed. The model inherits all capabilities from the original GPT-OSS-20B with focused expert selection.*

## Usage

### CPU Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the specialized model on CPU
model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-17.9b-specialized-safety-pruned-moe-only-27-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-17.9b-specialized-safety-pruned-moe-only-27-experts")

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
    "AmanPriyanshu/gpt-oss-17.9b-specialized-safety-pruned-moe-only-27-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-17.9b-specialized-safety-pruned-moe-only-27-experts")

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
<|channel|>analysis<|message|>Need to give steps: document, don't respond, block/report, seek support, legal options.<|end|><|start|>assistant<|channel|>final<|message|>### If you or someone you know is being cyber‑bullied, here’s a practical, step‑by‑step guide to protect yourself and get help.

| Step | What to Do | Why It Matters | Quick Tips |
|------|------------|-----------------|------------|
| **1. Stop Engaging** | Don’t reply, argue, or post back. | Responding can fuel the bully and give them the attention they crave. | If you feel compelled to respond, pause, breathe, and consider if it’s worth it. |
| **2. Document Everything** | Save screenshots, copy messages, record dates/times, and note usernames. | Evidence is crucial if you need to involve authorities, schools, or employers. | Use cloud storage or a secure folder; keep it private. |
| **3. Block & Report** | Block the bully on every platform (social media, messaging apps, gaming). | Blocking stops them from contacting you directly. | Report the content to the platform’s abuse team—most sites have a “Report” button. |
| **4. Adjust Privacy Settings** | Tighten who can see your posts, comment, or message you. | Reduces the bully’s ability to target you. | Review settings on Facebook, Instagram, TikTok, Discord, etc. |
| **5. Reach Out for Support** | Talk to a trusted friend, family member, teacher, or counselor. | Emotional support helps you process the experience and plan next steps. | If you’re a teen, consider a school counselor or a youth helpline. |
| **6. Contact Authorities (if needed)** | If threats, stalking, or illegal content are involved, file a police report. | Law enforcement can take action and provide legal protection. | Keep all documentation handy; give it to the officer. |
| **7. Seek Professional Help** | If the bullying is affecting your mental health, consider therapy or counseling. | Professional help can teach coping strategies and resilience. | Look for therapists who specialize in cyber‑bullying or trauma. |
| **8. Know Your Rights** | Familiarize yourself with local laws (e.g., U.S. “Cyberbullying” statutes, UK “Harassment” laws). | Knowing the legal framework empowers you to take action. | Many governments offer free legal advice hotlines. |
| **9. Keep
```

---

### Example 2
**Question:** How can people protect their personal information on social media?

**Response:**
```
<|channel|>analysis<|message|>Need to give practical tips.<|end|><|start|>assistant<|channel|>final<|message|>### 5‑Step Playbook for Keeping Your Personal Info Safe on Social Media

| Step | What to Do | Why It Matters | Quick Tips |
|------|------------|-----------------|------------|
| **1. Tighten Your Privacy Settings** | • Review every platform’s privacy panel.<br>• Set “Friends only” or “Close Friends” for posts.<br>• Turn off location tagging by default. | Most data leaks happen because settings are left at the default “public” level. | • **Facebook**: Settings → Privacy → Who can see your future posts.<br>• **Instagram**: Settings → Privacy → Account → Private account.<br>• **Twitter**: Settings → Privacy & safety → Protect your Tweets. |
| **2. Think Before You Share** | • Ask yourself: “Is this necessary?”<br>• Avoid posting exact addresses, phone numbers, or vacation plans that reveal your location. | Even a single post can be harvested by bots or used for targeted phishing. | • Use a “safe word” for sensitive info (e.g., “I’m at 123 Main St” → “I’m at 123 Main St” → “I’m at 123 Main St”). |
| **3. Use Strong, Unique Passwords & 2FA** | • Create a password manager (LastPass, 1Dash, Bitwarden).<br>• Enable two‑factor authentication on every account. | Password reuse is the #1 reason accounts get compromised. | • 2FA options: authenticator app (Google Authenticator, Authy), hardware key (YubiKey), or SMS (use only if no other option). |
| **4. Monitor Your Digital Footprint** | • Search your name on Google, Bing, and social‑media search tools.<br>• Set up Google Alerts for your name.<br>• Periodically review who can see your profile and posts. | You never know what data is out there; early detection can stop a breach before it spreads. | • Use “People Search” on LinkedIn, Facebook, and Google. |
| **5. Stay Informed & Practice Safe Browsing** | • Keep apps updated; install security patches.<br>• Use a VPN on public Wi‑Fi.<br>• Be wary of suspicious links, friend requests, or direct messages. | Social‑media platforms are prime targets for phishing and
```

---

### Example 3
**Question:** What are the warning signs of online scams?

**Response:**
```
<|channel|>analysis<|message|>Need to answer.<|end|><|start|>assistant<|channel|>final<|message|>### Warning Signs of Online Scams

| Category | Red‑Flag Indicators | Why It Matters |
|----------|---------------------|----------------|
| **Unsolicited Contact** | • You receive an email, message, or call from a “friend,” company, or government agency you don’t know.<br>• The contact claims you’ve won a prize, need to verify account info, or are being “suspended.” | Legitimate organizations rarely reach out via random email or text. |
| **Urgency or Pressure** | • “Act now!” or “You have 24 hours to respond.”<br>• Threats of account closure, legal action, or loss of funds. | Scammers create a false sense of urgency to bypass your rational thinking. |
| **Requests for Personal or Financial Info** | • Asking for passwords, PINs, credit‑card numbers, or bank account details.<br>• “Please confirm your identity” with a link to a fake login page. | Real companies never ask for sensitive data via unsecured channels. |
| **Too‑Good‑to‑Be‑True Offers** | • Extremely low prices, “free” gifts, or “guaranteed” returns.<br>• “Earn $10,000 a week” with no effort. | High rewards with little or no risk are classic bait. |
| **Unprofessional Communication** | • Poor spelling, grammar, or odd phrasing.<br>• Generic greetings (“Dear Customer”) instead of your name. | Scammers often use bulk‑sent messages or non‑native language. |
| **Suspicious Links or Attachments** | • Links that don’t match the sender’s domain.<br>• Attachments that claim to be invoices, contracts, or “important documents.” | These can install malware or redirect you to phishing sites. |
| **Unusual Payment Methods** | • Requests for wire transfers, prepaid debit cards, cryptocurrency, or gift cards.<br>• “Send money to this account” with no clear reason. | These methods are hard to trace and recover. |
| **Inconsistent or Contradictory Details** | • The story changes each time you ask questions.<br>• The “company” name or address doesn’t match official records. | Legitimate entities maintain consistent information. |
| **Pressure to Keep It Secret** | • “Don’t tell anyone” or “This is confidential.” | Sc
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
