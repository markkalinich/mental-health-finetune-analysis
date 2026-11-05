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

# Safety GPT-OSS Model (26 Experts)

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

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 26 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for safety tasks.

**⚠️ Experimental Model**: This is an experimental pruned model that may not work well - check the [examples below](#model-examples) to see if the outputs meet your needs before use.

This pruning approach reduces the model size while attempting to preserve performance on the target domain.

## Model Architecture & Statistics

| Metric | Value |
|--------|-------|
| **Base Model** | openai/gpt-oss-20b |
| **Architecture** | Mixture-of-Experts Transformer |
| **Total Parameters** | ~17.3B (pruned from 21B) |
| **Original Experts per Layer** | 32 |
| **Pruned Experts per Layer** | 26 |
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
- **Systematic Reduction**: Reduced from 32 to 26 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 81.2% of original expert parameters
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

By identifying experts that consistently activated for safety tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 26 experts per layer.

## Dataset & Analysis Foundation

This model is based on analysis from the **GPT-OSS-20B MoE Expert Activations dataset** available at:
🔗 **https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations**

The dataset contains router activation patterns from OpenAI's GPT-OSS-20B model across diverse evaluation benchmarks, enabling the creation of these domain-optimized models through systematic expert pruning.

### Pruning Methodology
Our approach involves:
1. **Activation Analysis**: Comprehensive evaluation of expert usage patterns across domain-specific tasks
2. **Expert Ranking**: Identification of the most frequently activated experts for target domains  
3. **Systematic Pruning**: Reduction from 32 to 26 experts while preserving router functionality
4. **Quality Validation**: Testing to ensure maintained performance on target tasks

*This is a direct pruning approach - no additional training was performed. The model inherits all capabilities from the original GPT-OSS-20B with focused expert selection.*

## Usage

### CPU Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the specialized model on CPU
model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-17.3b-specialized-safety-pruned-moe-only-26-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-17.3b-specialized-safety-pruned-moe-only-26-experts")

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
    "AmanPriyanshu/gpt-oss-17.3b-specialized-safety-pruned-moe-only-26-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-17.3b-specialized-safety-pruned-moe-only-26-experts")

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
<|channel|>analysis<|message|>Need advice.<|end|><|start|>assistant<|channel|>final<|message|>### If you’re being cyber‑bullied, here’s a practical, step‑by‑step guide to protect yourself, gather evidence, and get help.

| Step | What to Do | Why It Matters | Quick Tips |
|------|------------|-----------------|------------|
| **1. Stay Calm & Don’t Respond** | Don’t reply to harassing messages or posts. | Responding can fuel the bully and give them the reaction they want. | If you feel unsafe, pause the conversation and take a break. |
| **2. Block & Report** | Block the bully on every platform (social media, email, messaging apps). | Blocking stops them from contacting you directly. | Use the platform’s “Report” button—most sites have a dedicated “Harassment” or “Bullying” option. |
| **3. Preserve Evidence** | Take screenshots, save messages, record URLs, and note dates/times. | Evidence is essential if you need to involve authorities or a school/college. | Store copies in a secure, separate folder or cloud drive. |
| **4. Adjust Privacy Settings** | Tighten who can see your posts, who can comment, and who can message you. | Reduces the bully’s access to your personal info. | Review settings on Facebook, Instagram, TikTok, Snapchat, etc. |
| **5. Tell Someone You Trust** | Share what’s happening with a friend, family member, teacher, or counselor. | You don’t have to face it alone; support can help you decide next steps. | Keep the conversation private—don’t post it online. |
| **6. Seek Professional Help** | If the bullying is severe, consider a therapist or counselor. | Professional support can help you process emotions and develop coping strategies. | Many schools and workplaces offer confidential counseling services. |
| **7. Know the Law** | In many countries, cyberbullying is illegal (harassment, defamation, stalking). | You can file a police report or civil complaint. | Check local laws or consult a lawyer if you’re unsure. |
| **8. Use Digital Safety Tools** | Install reputable security software, enable two‑factor authentication, and use strong passwords. | Protects you from further attacks and identity theft. | Consider a password manager and a VPN for extra privacy. |
| **9. Consider a Digital “Clean‑Slate”** | If the bully’s content is persistent
```

---

### Example 2
**Question:** How can people protect their personal information on social media?

**Response:**
```
<|channel|>analysis<|message|>Need to give practical tips.<|end|><|start|>assistant<|channel|>final<|message|>### 1.  Think Before You Post  
| What to Avoid | Why It Matters | Quick Fix |
|---------------|-----------------|-----------|
| **Personal details** – full name, birthdate, hometown, school, workplace, phone number, email, or address. | These are the building blocks for identity‑theft or targeted phishing. | Use a nickname or a shortened version of your name. |
| **Location tags** – “I’m at home” or “just arrived at the office.” | Gives a real‑time map of your movements. | Turn off location services or use a generic “city” tag. |
| **Sensitive photos** – family pictures, vacation snaps with obvious landmarks, or photos of documents. | Can be used for social‑engineering or to confirm personal details. | Edit photos to blur faces or remove metadata before uploading. |
| **Political or religious views** | Can be used to target or discriminate against you. | Keep such posts private or in a closed group. |

---

### 2.  Tighten Your Privacy Settings  
| Platform | Key Setting | How to Enable |
|----------|-------------|---------------|
| **Facebook** | “Who can see my posts?” | Settings → Privacy → “Who can see my future posts?” → “Friends” or “Only me.” |
| **Instagram** | “Private Account” | Settings → Privacy → Account Privacy → Switch to Private. |
| **Twitter** | “Protect your Tweets” | Settings → Privacy & Safety → “Protect your Tweets.” |
| **LinkedIn** | “Who can see your profile?” | Settings → Privacy → “Profile viewing options” → “Private mode.” |
| **Snapchat** | “Ghost Mode” | Settings → “Ghost Mode” → Turn on. |

> **Tip:** Review settings every 6–12 months; platforms update defaults.

---

### 3.  Use Strong, Unique Credentials  
| Practice | Why It Helps | Tool |
|----------|--------------|------|
| **Long, random passwords** (12+ characters, mix of letters, numbers, symbols). | Makes brute‑force attacks harder. | LastPass, 1Pass, Bitwarden. |
| **Password manager** | Stores all passwords securely and auto‑fills. | 1Pass, Bitwarden, Dashlane. |
| **Two‑factor authentication (2FA)** | Adds a second layer beyond the password.
```

---

### Example 3
**Question:** What are the warning signs of online scams?

**Response:**
```
<|channel|>analysis<|message|>Need to answer.<|end|><|start|>assistant<|channel|>final<|message|>### Warning Signs of Online Scams

| Category | Red‑Flag Indicators | Why It Matters |
|----------|---------------------|----------------|
| **Unsolicited Contact** | • You receive an email, message, or call from a company you never interacted with.<br>• The sender claims you’ve won a prize, need to “verify” account info, or that a transaction is pending. | Scammers often start with a surprise hook to lower your guard. |
| **Urgency or Pressure** | • “Act now or you’ll lose your account.”<br>• “This offer expires in 24 hours.” | Legitimate services give you time to verify. Urgency forces rash decisions. |
| **Requests for Personal or Financial Info** | • “Please send your Social Security number, bank login, or credit‑card details.”<br>• “We need your password to reset your account.” | No reputable company will ask for passwords or full financial details via email or chat. |
| **Too Good to Be True Offers** | • “Earn $5,000 a week from home.”<br>• “Get a free iPhone for signing up.” | High payouts with little effort are classic bait. |
| **Unprofessional Communication** | • Spelling/grammar errors, odd phrasing, or generic greetings (“Dear Customer”).<br>• Use of “you” instead of your name. | Scammers often use bulk‑generated messages. |
| **Suspicious Links or Attachments** | • Links that don’t match the sender’s domain or use URL shorteners.<br>• Attachments that claim to be invoices, receipts, or “important documents.” | Links can lead to phishing sites; attachments can install malware. |
| **Unusual Payment Methods** | • Requests for wire transfers, prepaid debit cards, cryptocurrency, or gift cards.<br>• “Send money to this account” with no clear business reason. | These methods are hard to trace and recover. |
| **Inconsistent or Missing Contact Info** | • No phone number, only an email address.<br>• No physical address or only a vague location. | Legitimate businesses provide multiple ways to verify. |
| **Requests to Use Third‑Party Platforms** | • “Please send the money via PayPal, Venmo, or Western Union.” | These platforms are often used to move stolen funds. |
| **Too
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
