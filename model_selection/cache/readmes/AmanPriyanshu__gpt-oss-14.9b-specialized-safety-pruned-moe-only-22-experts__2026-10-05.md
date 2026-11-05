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

# Safety GPT-OSS Model (22 Experts)

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

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 22 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for safety tasks.

**⚠️ Experimental Model**: This is an experimental pruned model that may not work well - check the [examples below](#model-examples) to see if the outputs meet your needs before use.

This pruning approach reduces the model size while attempting to preserve performance on the target domain.

## Model Architecture & Statistics

| Metric | Value |
|--------|-------|
| **Base Model** | openai/gpt-oss-20b |
| **Architecture** | Mixture-of-Experts Transformer |
| **Total Parameters** | ~14.9B (pruned from 21B) |
| **Original Experts per Layer** | 32 |
| **Pruned Experts per Layer** | 22 |
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
- **Systematic Reduction**: Reduced from 32 to 22 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 68.8% of original expert parameters
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

By identifying experts that consistently activated for safety tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 22 experts per layer.

## Dataset & Analysis Foundation

This model is based on analysis from the **GPT-OSS-20B MoE Expert Activations dataset** available at:
🔗 **https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations**

The dataset contains router activation patterns from OpenAI's GPT-OSS-20B model across diverse evaluation benchmarks, enabling the creation of these domain-optimized models through systematic expert pruning.

### Pruning Methodology
Our approach involves:
1. **Activation Analysis**: Comprehensive evaluation of expert usage patterns across domain-specific tasks
2. **Expert Ranking**: Identification of the most frequently activated experts for target domains  
3. **Systematic Pruning**: Reduction from 32 to 22 experts while preserving router functionality
4. **Quality Validation**: Testing to ensure maintained performance on target tasks

*This is a direct pruning approach - no additional training was performed. The model inherits all capabilities from the original GPT-OSS-20B with focused expert selection.*

## Usage

### CPU Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the specialized model on CPU
model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-14.9b-specialized-safety-pruned-moe-only-22-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-14.9b-specialized-safety-pruned-moe-only-22-experts")

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
    "AmanPriyanshu/gpt-oss-14.9b-specialized-safety-pruned-moe-only-22-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-14.9b-specialized-safety-pruned-moe-only-22-experts")

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
Below is a practical, step‑by‑step guide that covers what to do right away, how to protect yourself, and how to get help if you need it.

---

## 1. Stay Calm & Don’t Respond Immediately
- **Pause**: Give yourself a few minutes (or hours) before replying.  
- **Avoid escalation**: Responding with anger or insults often fuels the bully and can make the situation worse.  
- **Take a break**: Step away from the screen if you feel overwhelmed.

---

## 2. Preserve Evidence
| Action | Why it matters | How to do it |
|--------|----------------|--------------|
| **Save the messages** | Proof for reporting or legal action | Screenshot, copy to a safe folder, or use a cloud‑based note app |
| **Record dates & times** | Shows pattern & severity | Add timestamps to screenshots or notes |
| **Keep the original post** | Some platforms delete content | Save the URL or copy the post to a separate file |
| **Log any threats** | Needed if the bully threatens violence | Store in a secure, private location |

> **Tip:** Use a separate, encrypted device or cloud folder for evidence so it can’t be deleted by the bully.

---

## 3. Block / Filter the Bully
- **Block or mute** the user on the platform.  
- **Adjust privacy settings**: Make your profile private, limit who can comment, or use “close friends” lists.  
- **Use “safe mode” or “report” features**: Many platforms have built‑in tools to hide or remove harassing content.

---

## 4. Report the Abuse
| Platform | Typical Reporting Process | What to include |
|----------|---------------------------|----------------|
| **Facebook / Instagram** | “Harassment” or “Bullying” report button | Screenshot, user ID, description |
| **Twitter** | “Report a Tweet” or “Report a user” | Link to tweet, user handle |
| **TikTok** | “Report a video” or “Report a user” | Video link, user handle |
| **School or workplace** | Contact the IT or HR department | Email or form, evidence |
| **Law enforcement** | If threats of violence or stalking | Police report,
```

---

### Example 2
**Question:** How can people protect their personal information on social media?

**Response:**
```
<|channel|>analysis<|message|>Need to give practical tips.<|end|><|start|>assistant<|channel|>final<|message|>### 1. **Think Before You Post**

| Action | Why It Matters | Quick Tips |
|--------|----------------|------------|
| **Limit personal details** | The more you share, the easier it is to build a profile of you. | Avoid posting exact birthdates, home addresses, or daily routines. |
| **Use “privacy mode”** | Many platforms let you hide posts from the public eye. | Set posts to “Friends only” or “Close friends” instead of “Public.” |
| **Check the audience** | Even a “Friends” list can include people you don’t know well. | Review who’s on your friend list and remove anyone you’re uncomfortable sharing with. |

---

### 2. **Secure Your Accounts**

| Feature | How to Use It | Why It Helps |
|--------|---------------|--------------|
| **Strong, unique passwords** | Use a mix of letters, numbers, and symbols. | Prevents brute‑force attacks. |
| **Two‑factor authentication (2FA)** | Add a phone number or authenticator app. | Adds a second barrier even if the password is compromised. |
| **Password manager** | Store and generate passwords in a secure app. | Keeps you from reusing passwords across sites. |
| **Regularly update passwords** | Change them every 6–12 months. | Reduces risk from old, leaked credentials. |

---

### 3. **Control Who Sees What**

| Setting | What to Check | Example |
|--------|---------------|---------|
| **Profile visibility** | Public vs. Private | Make your profile private so only approved users can see it. |
| **Location sharing** | Turn off location sharing or use “Location sharing only with friends.” | Prevents strangers from tracking your movements. |
| **Tagging** | Disable “Tagging” or “Tagging is disabled.” | Stops others from tagging you in posts you don’t want to be associated with. |
| **Story settings** | Set “Only friends” or “Close friends.” | Keeps your stories from the general public. |

---

### 4. **Be Wary of Phishing & Scams**

| Red Flag | What to Do |
|----------|------------|
| **Unexpected messages** | Verify the sender’s identity before clicking links. |
| **Too‑good‑to‑be‑true offers** | Research the offer; many are scams
```

---

### Example 3
**Question:** What are the warning signs of online scams?

**Response:**
```
<|channel|>analysis<|message|>Need to answer.<|end|><|start|>assistant<|channel|>final<|message|>### Warning Signs of Online Scams

| Category | Red‑Flag Behaviors | Why It Matters |
|----------|-------------------|----------------|
| **Unsolicited Contact** | • You receive a message or email from a “friend,” “bank,” or “government agency” you never heard from. <br>• The contact is urgent, demanding immediate action. | Scammers often use surprise or fear to bypass your rational checks. |
| **Too‑Good‑to‑Be‑True Offers** | • “Free” prizes, “guaranteed” returns, or “once‑in‑life” deals that require no effort. | Legitimate offers always have a cost or a realistic risk. |
| **Requests for Personal Data** | • Asking for passwords, social‑security numbers, bank details, or photos of ID. | No reputable organization will ask for full credentials or ID via email/phone. |
| **Unusual Payment Methods** | • “Pay with a prepaid card,” “wire transfer,” “cryptocurrency,” or “gift card.” | These methods are hard to trace and recover once sent. |
| **Poor Grammar & Spelling** | • Numerous typos, broken sentences, or odd phrasing. | Many scams originate from non‑native speakers or automated bots. |
| **Pressure to Act Quickly** | • “Offer expires in 24 hours,” “you must act now.” | Scammers create artificial urgency to prevent you from researching. |
| **Generic or Missing Contact Info** | • No real phone number, email address, or physical address. | Legitimate businesses provide multiple ways to verify identity. |
| **Unusual URLs or Domains** | • Email addresses or websites that mimic real ones but with subtle misspellings (e.g., “paypa.com” vs. “paypal.com”). | Phishing sites often use look‑alike domains to trick you. |
| **Requests for “Confidential” or “Secret” Info** | • “We’re only talking to you” or “this is a confidential matter.” | Scammers use secrecy to isolate you from seeking help. |
| **Too Much Personalization** | • They use your name, recent purchase, or other personal details. | Scammers harvest data from social media or data breaches to appear legitimate. |
| **Unverified “Testimonials”** | • Fake reviews, screenshots of “positive” comments, or fabricated endorsements.
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
