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

# Safety GPT-OSS Model (13 Experts)

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

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 13 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for safety tasks.

**⚠️ Experimental Model**: This is an experimental pruned model that may not work well - check the [examples below](#model-examples) to see if the outputs meet your needs before use.

This pruning approach reduces the model size while attempting to preserve performance on the target domain.

## Model Architecture & Statistics

| Metric | Value |
|--------|-------|
| **Base Model** | openai/gpt-oss-20b |
| **Architecture** | Mixture-of-Experts Transformer |
| **Total Parameters** | ~9.6B (pruned from 21B) |
| **Original Experts per Layer** | 32 |
| **Pruned Experts per Layer** | 13 |
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
- **Systematic Reduction**: Reduced from 32 to 13 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 40.6% of original expert parameters
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

By identifying experts that consistently activated for safety tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 13 experts per layer.

## Dataset & Analysis Foundation

This model is based on analysis from the **GPT-OSS-20B MoE Expert Activations dataset** available at:
🔗 **https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations**

The dataset contains router activation patterns from OpenAI's GPT-OSS-20B model across diverse evaluation benchmarks, enabling the creation of these domain-optimized models through systematic expert pruning.

### Pruning Methodology
Our approach involves:
1. **Activation Analysis**: Comprehensive evaluation of expert usage patterns across domain-specific tasks
2. **Expert Ranking**: Identification of the most frequently activated experts for target domains  
3. **Systematic Pruning**: Reduction from 32 to 13 experts while preserving router functionality
4. **Quality Validation**: Testing to ensure maintained performance on target tasks

*This is a direct pruning approach - no additional training was performed. The model inherits all capabilities from the original GPT-OSS-20B with focused expert selection.*

## Usage

### CPU Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the specialized model on CPU
model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-9.6b-specialized-safety-pruned-moe-only-13-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-9.6b-specialized-safety-pruned-moe-only-13-experts")

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
    "AmanPriyanshu/gpt-oss-9.6b-specialized-safety-pruned-moe-only-13-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-9.6b-specialized-safety-pruned-moe-only-13-experts")

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
<|channel|>analysis<|message|>Need advice.<|end|><|start|>assistant<|channel|>final<|message|>**If you’re being cyber‑bullied, you’re not alone and you have options.**  
Below is a step‑by‑step guide that covers what to do right away, how to protect yourself, and how to seek help.

---

## 1. **Stop the Interaction (Immediately)**
| **What to do** | **Why it matters** |
|--------------------------- |--------------------------- |
| **Delete or block the bully** | Removes the source of harassment from your feed. |
| **Turn off notifications** | Prevents the bully from seeing your posts. |
| **Mute or ignore** | Keeps you from engaging in a toxic loop. |

> **Tip:** If the bully is a friend or acquaintance, consider a “soft block” (e.g., “mute” on a platform that lets you still see their posts but not interact).

---

## 2. **Document Everything**
| **What to do** | **Why it matters** |
|--------------------------- |--------------------------- |
| **Save screenshots, messages, or posts** | Evidence for reporting or legal action. |
| **Keep timestamps** | Shows when the harassment started. |
| **Use a secure storage** | Avoid losing evidence (e.g., a cloud folder or a dedicated notebook). |

> **Tip:** Many platforms let you export chats or screenshots. Use that feature before deleting.

---

## 3. **Check Platform Policies**
| **What to do** | **Why it matters** |
|--------------------------- |--------------------------- |
| **Read the harassment / hate‑speech policy** | Understand what is disallowed. |
| **Locate the reporting form** | Most platforms have a dedicated “report abuse” button. |
| **Follow the steps** | Submit evidence and request action. |

> **Tip:** If the bully is a public figure or a brand, you may also file a complaint with the platform’s “public safety” team.

---

## 4. **Report to the Platform**
| **What to do** | **Why it matters** |
|--------------------------- |--------------------------- |
| **Use the “report” button** | The platform can suspend or delete the bully’s account. |
| **Provide evidence** | Increases the likelihood of a swift action. |
| **Follow up** | Some platforms send a confirmation email. |

> **Tip:** If you’re on a smaller site (e.g., a forum), contact the moderators directly.

---
```

---

### Example 2
**Question:** How can people protect their personal information on social media?

**Response:**
```
<|channel|>analysis<|message|>Need to give tips.<|end|><|start|>assistant<|channel|>final<|message|>### 1. **Think About What You Share**

| **What to Avoid** | Why it matters |
|---------------------------|---------------------------|
| **Full addresses, phone numbers, or workplace details** | Makes it easy for someone to locate you or target you. |
| **Exact birth dates or birthdays** | Gives a clue to your age and can be used for identity‑theft. |
| **Freekly posting “just‑in‑the‑moment” photos** | Shows where you’re currently, which can be used to track you. |
| **Detailed travel itinerities** | Lets someone know when you’re away and where you’ll be. |

**Rule:** Keep the “public” version of your profile to a minimum of “name, city, job title, and a hobby.” Anything that pin‑s identifies you can be removed or hidden.

---

### 2. **Use Privacy Settings Wisely**

| **Platform Feature** | How to use it |
|---------------------------|---------------------------|
| **Private / Friends‑Only** | Keep the bulk of your photos, posts, and stories in this mode. |
| **Location Sharing** | Disable location on posts or use a “generic” location (e.g., “City” instead of exact address). |
| **Tagging** | Only tag people you know personally; avoid tagging strangers or public accounts. |
| **Profile Visibility** | Set “Only Me” for sensitive info (e.g., contact details). |

---

### 3. **Create Separate “Public” and “Private” Accounts**

- **Public account**: Use for general networking, business, or community engagement. Keep it light and generic.  
- **Private account**: Use for personal photos, family, and close friends. Keep it off‑screen or “Friends‑Only.”

---

### 4. **Use Strong, Unique Passwords**

- **Multi‑factor authentication**: Enable 2‑factor (e.g., Apple Touch ID, Google Authenticator).  
- **Password manager**: Store passwords in a secure app (e.g., LastPass, Bitwarden).  
- **Avoid “same password”**: Even if you use a password‑generator, never reuse the same password across accounts.

---

### 5. **Enable “Delete” or “Remove” Options**

- **Delete posts**: Some platforms let you delete a post entirely.  
- **Delete comments
```

---

### Example 3
**Question:** What are the warning signs of online scams?

**Response:**
```
<|channel|>analysis<|message|>Need to list warning signs.<|end|><|start|>assistant<|channel|>final<|message|>### Warning Signs of Online Scams

| Category | Red Flag | Why It Matters |
|---|---|---|
| **Unsolicated Contact** | You receive a message or call from a “represent” of a company you never contacted. | Scers often initiate contact to create a sense of urgency. |
| **Urgity & Pressure** | “Act now or you’ll lose your chance” or “Immediate payment required.” | Legitimate offers never demand instant action. |
| **Too Good to Be True** | “Free gift,” “instant money” or “no risk.” | Scers use unrealistic promises to lure victims. |
| **Requests for Personal Data** | “Send us your SSN, bank details, or photos.” | Legitimate companies never ask for sensitive info via email or phone. |
| **Unprofessional Communication** | Tyng‑errors, spam‑style, or generic “Dear Sir/Mma.” | Scers often use low‑quality language. |
| **Unusual Payment Methods** | “Pay via text, prepaid card, or a “special” app.” | Real businesses use secure, traceable channels. |
| **No Real Contact Info** | No phone number, email address, or company website. | Scers hide behind fake identities. |
| **Too Much Personalization** | “We’ve been following your work” or “Your profile shows you’re a perfect fit.” | Scers use generic data from public sources. |
| **No Verification Process** | “No background check” or “No references needed.” | Legit firms verify credentials. |
| **High Fees for “Special” Services** | “Premium fee” or “extra cost” for a “special” service. | Scers inflate costs to cover their own expenses. |
| **Requests to Bypass Official Channels** | “Send us the money directly” or “Skip the bank.” | Legit firms use official payment routes. |
| **No Clear Terms or Conditions** | “We’ll discuss details later” or “No contract.” | Scers avoid legal obligations. |
| **Pressure to Share with Friends** | “Tell your friends” or “Invite others.” | Scers use social pressure to spread. |
| **Unverified “Testimonials”** | “Everyone’s happy” or “Check our reviews.” | Fake reviews are often fabricated. |
| **Unusual Language or Cultural Gifts** |
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
