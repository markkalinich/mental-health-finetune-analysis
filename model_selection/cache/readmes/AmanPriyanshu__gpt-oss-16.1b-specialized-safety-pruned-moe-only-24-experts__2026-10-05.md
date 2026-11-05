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

# Safety GPT-OSS Model (24 Experts)

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

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 24 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for safety tasks.

**⚠️ Experimental Model**: This is an experimental pruned model that may not work well - check the [examples below](#model-examples) to see if the outputs meet your needs before use.

This pruning approach reduces the model size while attempting to preserve performance on the target domain.

## Model Architecture & Statistics

| Metric | Value |
|--------|-------|
| **Base Model** | openai/gpt-oss-20b |
| **Architecture** | Mixture-of-Experts Transformer |
| **Total Parameters** | ~16.1B (pruned from 21B) |
| **Original Experts per Layer** | 32 |
| **Pruned Experts per Layer** | 24 |
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
- **Systematic Reduction**: Reduced from 32 to 24 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 75.0% of original expert parameters
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

By identifying experts that consistently activated for safety tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 24 experts per layer.

## Dataset & Analysis Foundation

This model is based on analysis from the **GPT-OSS-20B MoE Expert Activations dataset** available at:
🔗 **https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations**

The dataset contains router activation patterns from OpenAI's GPT-OSS-20B model across diverse evaluation benchmarks, enabling the creation of these domain-optimized models through systematic expert pruning.

### Pruning Methodology
Our approach involves:
1. **Activation Analysis**: Comprehensive evaluation of expert usage patterns across domain-specific tasks
2. **Expert Ranking**: Identification of the most frequently activated experts for target domains  
3. **Systematic Pruning**: Reduction from 32 to 24 experts while preserving router functionality
4. **Quality Validation**: Testing to ensure maintained performance on target tasks

*This is a direct pruning approach - no additional training was performed. The model inherits all capabilities from the original GPT-OSS-20B with focused expert selection.*

## Usage

### CPU Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the specialized model on CPU
model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-16.1b-specialized-safety-pruned-moe-only-24-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-16.1b-specialized-safety-pruned-moe-only-24-experts")

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
    "AmanPriyanshu/gpt-oss-16.1b-specialized-safety-pruned-moe-only-24-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-16.1b-specialized-safety-pruned-moe-only-24-experts")

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
Below is a step‑by‑step guide that covers what to do right away, how to protect yourself, and where to get help.

---

## 1. Stay Calm & Don’t Respond Immediately  
- **Pause**: Give yourself a few minutes (or hours) before replying.  
- **Avoid escalation**: Responding with anger or insults often fuels the bully.  
- **Take a break**: Step away from the platform for a while if you feel overwhelmed.

---

## 2. Preserve Evidence  
| Action | Why it matters | How to do it |
|--------|-----------------|--------------|
| **Screenshot** | Keeps a record that can’t be altered. | Use the built‑in screenshot tool or a screen‑capture app. |
| **Save messages** | Needed for reporting or legal action. | Copy the text, or use the platform’s “Save” or “Download” feature. |
| **Record URLs** | Shows where the harassment is happening. | Copy the link or use a browser bookmark. |
| **Keep logs** | Helps you track patterns over time. | Use a simple note‑taking app or a spreadsheet. |

---

## 3. Block / Mute / Report the Bully  
| Platform | Typical steps |
|----------|---------------|
| **Facebook / Instagram** | *Block* the user → *Report* the post or message. |
| **Twitter** | *Mute* the user → *Report* the tweet. |
| **Snapchat** | *Block* the user → *Report* the snap. |
| **Discord / Slack** | *Mute* or *Remove* the user from the channel → *Report* to admins. |
| **Gaming platforms (Steam, Xbox, PlayStation)** | *Block* the user → *Report* the harassment. |

- **Use the “Report” button**: Most platforms have a dedicated button or link for harassment.  
- **Provide evidence**: Attach screenshots or links when you report.

---

## 4. Adjust Privacy Settings  
- **Limit who can see your posts**: Switch to “Friends only” or “Private.”  
- **Restrict who can message you**: Turn on “Only friends can message” or “Only people you follow.”  
- **Disable location sharing**:
```

---

### Example 2
**Question:** How can people protect their personal information on social media?

**Response:**
```
<|channel|>analysis<|message|>Need to give practical tips.<|end|><|start|>assistant<|channel|>final<|message|>### 1. **Think Before You Post**

| Action | Why It Matters | Quick Fix |
|--------|----------------|-----------|
| **Avoid personal details** (home address, phone number, exact school, workplace, travel plans) | These are the most obvious clues for identity thieves. | Use a generic location (“City, State”) or a city‑wide map instead of a street address. |
| **Limit “check‑ins”** | Frequent check‑ins can reveal your daily routine. | Post only when you’re in a public place or use a “location blur” feature. |
| **Re‑evaluate old posts** | Past posts can be resurfaced or scraped. | Use the platform’s “archive” or “delete” options for old content that contains sensitive info. |

---

### 2. **Secure Your Account Settings**

| Setting | Recommendation | How to Enable |
|--------|----------------|---------------|
| **Two‑factor authentication (2FA)** | Adds a second layer beyond just a password. | Go to Settings → Security → Enable 2FA (SMS, authenticator app, or hardware token). |
| **Strong, unique passwords** | Prevents brute‑force attacks and cross‑platform leaks. | Use a password manager; mix letters, numbers, symbols; avoid “password123.” |
| **Login alerts** | Notifies you of suspicious logins. | Settings → Security → Enable login alerts. |
| **App permissions** | Limits what third‑party apps can access. | Settings → Privacy → Review app permissions; revoke any that seem unnecessary. |
| **Profile visibility** | Controls who can see your posts. | Settings → Privacy → Set “Public,” “Friends only,” or “Private” as needed. |

---

### 3. **Use Privacy‑Focused Features**

| Feature | What It Does | How to Use |
|--------|--------------|------------|
| **“Hide” or “Close Friends” lists** | Only selected people see certain posts. | Create a “Close Friends” list; tag posts with “Only for Close Friends.” |
| **Location blur** | Masks the exact location on a map. | When posting a photo with location, tap the map icon → “Blur.” |
| **Story expiration** | Stories disappear after 24 hrs. | Use stories for fleeting moments; avoid posting sensitive info. |
| **Private messaging** | Keeps conversations off public
```

---

### Example 3
**Question:** What are the warning signs of online scams?

**Response:**
```
<|channel|>analysis<|message|>Need to answer.<|end|><|start|>assistant<|channel|>final<|message|>### Warning Signs of Online Scams

| Category | Red‑Flag Indicators | Why It Matters |
|----------|---------------------|----------------|
| **Unsolicited Contact** | • You receive an email, message, or call from a company you never interacted with.<br>• The contact claims you’ve won a prize, need to verify account info, or have a “critical” issue. | Scammers often start with a surprise hook to lower your guard. |
| **Urgency or Pressure** | • “Act now or you’ll lose your account.”<br>• “Your account will be closed in 24 hours.” | Legitimate organizations give you time to verify. Urgency forces rash decisions. |
| **Requests for Personal Data** | • “Please send your SSN, bank account, or credit card details.”<br>• “Upload a photo of your ID.” | No reputable business will ask for sensitive data via email or text. |
| **Unusual Payment Methods** | • “Send money via wire transfer, prepaid card, or cryptocurrency.”<br>• “Pay with a gift card or a virtual currency.” | These methods are hard to trace and recover. |
| **Too Good to Be True Offers** | • “Earn $10,000/month from home.”<br>• “Get a free iPhone for signing up.” | High returns with little effort are classic bait. |
| **Poor Grammar & Spelling** | • Numerous typos, broken sentences, or odd phrasing.<br>• Non‑native language errors. | Professional companies maintain high communication standards. |
| **Generic or Missing Contact Info** | • No physical address, phone number, or verified email.<br>• “Contact us at support@xxxx.com” with no traceable domain. | Legitimate firms provide multiple ways to verify authenticity. |
| **Suspicious URLs or Links** | • Links that don’t match the company’s domain (e.g., “https://www.paypal.com/xxxx”).<br>• Shortened URLs or unfamiliar domains. | Phishing sites mimic real sites but use slightly altered URLs. |
| **Unverified Claims** | • “We’re a government agency” or “We’re a well‑known brand” without evidence.<br>• No official logos or branding. | Scammers often use logos or claims to build false credibility. |
| **Requests for “Confidential
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
