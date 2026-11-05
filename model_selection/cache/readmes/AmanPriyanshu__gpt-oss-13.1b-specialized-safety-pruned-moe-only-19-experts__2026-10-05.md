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

# Safety GPT-OSS Model (19 Experts)

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

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 19 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for safety tasks.

**⚠️ Experimental Model**: This is an experimental pruned model that may not work well - check the [examples below](#model-examples) to see if the outputs meet your needs before use.

This pruning approach reduces the model size while attempting to preserve performance on the target domain.

## Model Architecture & Statistics

| Metric | Value |
|--------|-------|
| **Base Model** | openai/gpt-oss-20b |
| **Architecture** | Mixture-of-Experts Transformer |
| **Total Parameters** | ~13.1B (pruned from 21B) |
| **Original Experts per Layer** | 32 |
| **Pruned Experts per Layer** | 19 |
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
- **Systematic Reduction**: Reduced from 32 to 19 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 59.4% of original expert parameters
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

By identifying experts that consistently activated for safety tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 19 experts per layer.

## Dataset & Analysis Foundation

This model is based on analysis from the **GPT-OSS-20B MoE Expert Activations dataset** available at:
🔗 **https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations**

The dataset contains router activation patterns from OpenAI's GPT-OSS-20B model across diverse evaluation benchmarks, enabling the creation of these domain-optimized models through systematic expert pruning.

### Pruning Methodology
Our approach involves:
1. **Activation Analysis**: Comprehensive evaluation of expert usage patterns across domain-specific tasks
2. **Expert Ranking**: Identification of the most frequently activated experts for target domains  
3. **Systematic Pruning**: Reduction from 32 to 19 experts while preserving router functionality
4. **Quality Validation**: Testing to ensure maintained performance on target tasks

*This is a direct pruning approach - no additional training was performed. The model inherits all capabilities from the original GPT-OSS-20B with focused expert selection.*

## Usage

### CPU Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the specialized model on CPU
model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-13.1b-specialized-safety-pruned-moe-only-19-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-13.1b-specialized-safety-pruned-moe-only-19-experts")

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
    "AmanPriyanshu/gpt-oss-13.1b-specialized-safety-pruned-moe-only-19-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-13.1b-specialized-safety-pruned-moe-only-19-experts")

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
Below is a practical, step‑by‑step guide that covers what to do right away, how to protect yourself, and how to seek help.

---

## 1. Stay Calm & Don’t Respond Immediately  
- **Pause before replying.** A quick, emotional response can fuel the bully.  
- **Take a break.** Step away from the screen, breathe, and give yourself time to process.

## 2. Preserve Evidence  
| Action | Why it matters | How to do it |
|--------|----------------|--------------|
| **Save messages, screenshots, or posts** | Needed if you report to a platform or law‑enforcement | Use the “Save as screenshot” feature or copy‑paste into a secure folder |
| **Keep timestamps** | Shows when the harassment happened | Note the date/time in a log or use a calendar |
| **Record any threats** | Helps authorities assess risk | Save the exact wording, not just a summary |

> **Tip:** Use a separate, encrypted device or cloud folder for evidence so it can’t be deleted by the bully.

## 3. Block / Filter the Buliter  
- **Block or mute** the user on the platform.  
- **Adjust privacy settings** (e.g., make your profile private, limit who can comment).  
- **Use “safe mode” or “report” features** on the platform to restrict or remove content.

## 4. Report to the Platform  
- **Locate the “Report” button** (usually under the post or in the help center).  
- **Provide the evidence** you saved.  
- **Follow up** if you don’t see a response within a reasonable time frame (often 48–72 hrs).

> **Platforms that help:**  
> • Facebook – “Harassment” report  
> • Instagram – “Harassment” or “Harassment or Hate”  
> • Twitter – “Report a Tweet” or “Report a user”  
> • Tik‑Tok – “Report a video” or “Report a user”  
> • Discord – “Report a user” or “Report a message”

## 5. Notify Trusted Adults or Authorities  
- **If you’re a minor**: Tell a parent, teacher, or school counselor.  
- **If you’re an adult**
```

---

### Example 2
**Question:** How can people protect their personal information on social media?

**Response:**
```
<|channel|>analysis<|message|>Need to give practical tips.<|end|><|start|>assistant<|channel|>final<|message|>### 1.  Think Before You Post  
| **What to do** | **Why it matters** |
|----------------|----------------|
| **Ask yourself**: “Will I be comfortable with anyone else seeing this?” | Even a seemingly harmless photo can be used to build a profile of you. |
| **Avoid location tags** on every post. | Location data can be combined with other posts to track your movements. |
| **Use “safe” language**. | Avoid revealing passwords, bank details, or anything that could be used to impersonate you. |

---

### 2.  Tighten Your Privacy Settings  
| **Platform** | **Key Settings** |
|----------------|----------------|
| **Facebook** | • Set “Friends only” for personal photos. <br>• Use “Close Friends” list for sensitive content. <br>• Turn off “Location” and “Public” tags. |
| **Instagram** | • Switch to “Private” account. <br>• Use “Close Friends” for stories. <nobr>• Disable location sharing on stories. |
| **Twitter** | • Use “Private” mode if you want to limit followers. <br>• Disable location on tweets. |
| **LinkedIn** | • Keep profile details minimal. <br>• Use “Connections” filter for sensitive posts. |
| **Snapchat** | • Turn off “Location” and “Public” tags. <br>• Use “Friends” filter for snaps. |

**Tip**: Review settings every 6–12 months; platforms change defaults.

---

### 3.  Use Strong, Unique Passwords  
| **Why** | **How** |
|----------------|----------------|
| Prevents account takeover. | • Use a password manager (e.g., LastPass, M2P). <br>• Combine 8+ characters, mix letters, numbers, symbols. |
| Avoid re‑using passwords across sites. | • If you must, use a “master password” + unique “salt” for each site. |

---

### 4.  Enable Two‑Factor Authentication (2FA)  
| **What** | **Benefits** |
|----------------|----------------|
| A second step (code, push notification, or biometric). | • Even if someone gets your password, they can’t access the account. |
| Use authent apps (Authy, Apple Key‑
```

---

### Example 3
**Question:** What are the warning signs of online scams?

**Response:**
```
<|channel|>analysis<|message|>Need to answer.<|end|><|start|>assistant<|channel|>final<|message|>### Warning Signs of Online Scams  
*(Keep these in mind whenever you’re browsing, shopping, or communicating online.)*

| # | Sign | What It Means | Why It’s a Red Flag |
|---|------|----------------|------------------------|
| 1 | **Unsolated “Unexpected” Offer** | “You’ve won a prize” or “Your account has been upgraded.” | Legitimate offers usually come from known sources and require a clear, verifiable process. |
| 2 | **Urgity or Pressure** | “Act now or lose your chance” or “Your account will be closed in 24 hrs.” | Scams create a false sense of urgency to prevent you from thinking things through. |
| 3 | **Requests for Personal or Financial Info** | “Please send your SSN, bank details, or credit card number.” | No legitimate business will ask for such sensitive data via email, chat, or a pop‑up. |
| 4 | **Too Good‑for‑It‑to‑Be‑True Deals** | “$1,000 off a $10,000 product” or “Free trip to Paris.” | The price is usually far below market value; the “deal” is a bait. |
| 5 | **Unprofessional Communication** | Typos, broken grammar, generic greetings (“Dear Customer”). | Real companies use professional, brand‑consistent language. |
| 6 | **Unverified or Fake Contact Details** | No phone number, no physical address, or a generic “support@company.com.” | Legit sites provide clear ways to verify identity. |
| 7 | **Unusual Payment Methods** | “Send money via wire transfer, cryptocurrency, or gift cards.” | These methods are hard to trace and recover. |
| 8 | **Suspicious Links or URLs** | “Click here to claim your prize” with a URL that looks similar but not identical to the real site. | Scammers mimic brand names to trick you into phishing sites. |
| 9 | **No or Incomplete Privacy Policy** | No privacy policy, or a vague one that doesn’t explain data usage. | Legit sites must disclose how they handle your data. |
|10 | **Too Many “Testimonials” or “Reviews” that Sound Generic** | “Everyone loves this product” with no verifiable source. | Scams often use fabricated reviews. |
|11 | **
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
