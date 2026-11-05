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

# Safety GPT-OSS Model (16 Experts)

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

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 16 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for safety tasks.

**⚠️ Experimental Model**: This is an experimental pruned model that may not work well - check the [examples below](#model-examples) to see if the outputs meet your needs before use.

This pruning approach reduces the model size while attempting to preserve performance on the target domain.

## Model Architecture & Statistics

| Metric | Value |
|--------|-------|
| **Base Model** | openai/gpt-oss-20b |
| **Architecture** | Mixture-of-Experts Transformer |
| **Total Parameters** | ~11.4B (pruned from 21B) |
| **Original Experts per Layer** | 32 |
| **Pruned Experts per Layer** | 16 |
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
- **Systematic Reduction**: Reduced from 32 to 16 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 50.0% of original expert parameters
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

By identifying experts that consistently activated for safety tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 16 experts per layer.

## Dataset & Analysis Foundation

This model is based on analysis from the **GPT-OSS-20B MoE Expert Activations dataset** available at:
🔗 **https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations**

The dataset contains router activation patterns from OpenAI's GPT-OSS-20B model across diverse evaluation benchmarks, enabling the creation of these domain-optimized models through systematic expert pruning.

### Pruning Methodology
Our approach involves:
1. **Activation Analysis**: Comprehensive evaluation of expert usage patterns across domain-specific tasks
2. **Expert Ranking**: Identification of the most frequently activated experts for target domains  
3. **Systematic Pruning**: Reduction from 32 to 16 experts while preserving router functionality
4. **Quality Validation**: Testing to ensure maintained performance on target tasks

*This is a direct pruning approach - no additional training was performed. The model inherits all capabilities from the original GPT-OSS-20B with focused expert selection.*

## Usage

### CPU Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the specialized model on CPU
model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-11.4b-specialized-safety-pruned-moe-only-16-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-11.4b-specialized-safety-pruned-moe-only-16-experts")

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
    "AmanPriyanshu/gpt-oss-11.4b-specialized-safety-pruned-moe-only-16-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-11.4b-specialized-safety-pruned-moe-only-16-experts")

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
<|channel|>analysis<|message|>Need concise advice.<|end|><|start|>assistant<|channel|>final<|message|>**If you’re being cyber‑bullied, act quickly and protect yourself.**  

| Step | What to do | Why it matters |
|------|--------------|----------------|
| **1. Stop the interaction** | • Delete or block the bully’s account. <br>• Turn off notifications for that account. | Cuts the immediate source of harassment. |
| **2. Preserve evidence** | • Save screenshots, messages, posts, or any proof of the abuse. <br>• Store them in a secure folder or cloud drive. | Needed if you report the incident. |
| **3. Report the content** | • Use the platform’s “Report” or “Block” feature. <br>• If it’s a school or workplace, notify the relevant authority (teacher, HR, IT). | Platforms and institutions can remove or take action against the bully. |
| **4. Reach out for help** | • Talk to a trusted friend, family member, or counselor. <br>• If you’re a teen, consider contacting a school counselor or a local youth helline. | Emotional support and guidance. |
| **5. Protect your privacy** | • Update your privacy settings (e.g., “Friends only” for photos). <br>• Use a strong, unique password and enable two‑factor authentication. | Reduces future exposure. |
| **6. Take a break if needed** | • Log out for a few days, or switch to a different device. <br>• Engage in offline activities. | Helps you recover emotionally. |
| **7. Seek professional help if it escalates** | • If the bullying turns into threats, stalking, or you feel unsafe, contact law enforcement. <br>• Consider therapy or counseling. | Ensures your safety and mental health. |

**Quick “Do‑Not‑Do” list**

- **Don’t respond with anger or insults** – it can fuel the bully.  
- **Don’t share the bully’s content with others** – it can spread the harassment.  
- **Don’t ignore it** – early action often stops the cycle.

**Remember**: You’re not alone. Most platforms have tools to block and report abuse, and many schools, workplaces, and communities offer support. If you feel unsafe or overwhelmed, reach out to a trusted adult or professional right away.<|return|>
```

---

### Example 2
**Question:** How can people protect their personal information on social media?

**Response:**
```
<|channel|>analysis<|message|>Need concise answer.<|end|><|start|>assistant<|channel|>final<|message|>**Protecting Personal Information on Social Media**

| **What to Guard** | **Why It Matters** | **Practical Steps** |
|---------------------|---------------------|---------------------|
| **Profile details** (full name, birthdate, location, phone number, email) | Can be used to create fake accounts or track you. | • Use a nickname or partial name. <br>• Hide or set “Friends” only for location, phone, email. |
| **Photos & videos** | Reveal habits, routines, or sensitive moments. | • Use “Private” or “Friends‑only” settings. <br>• Blur or crop identifying details. |
| **Posts & comments** | Public statements can be mis‑quoted or taken out of context. | • Think before posting; keep sensitive opinions private. <br>• Use “Draft” mode to review before sharing. |
| **Direct messages** | Can be intercepted or forwarded. | • Use secure messaging apps (e‑Whats, Signal) for sensitive chats. <br>• Enable “Message encryption” if available. |
| **Links & URLs** | May lead to phishing or data‑harvesting sites. | • Verify the source before clicking. <br>• Use “Safe browsing” tools. |
| **Friends list** | Untrusted contacts can access your data. | • Regularly review and remove unknown or inactive accounts. <br>• Use “Close Friends” or “Private” lists. |
| **Third‑party apps** | Some services harvest data from your profile. | • Read privacy policies. <br>• Disable unnecessary data‑sharing permissions. |

### Quick Checklist

1. **Set “Private” or “Friends‑only” on sensitive info.**  
2. **Use a pseudonym or partial name.**  
3. **Keep photos/videos private or blurred.**  
4. **Think before posting; keep sensitive opinions off public feeds.**  
5. **Verify links before clicking.**  
6. **Review friends list regularly.**  
7. **Limit third‑party app permissions.**  
8. **Use secure messaging for private conversations.**

By applying these habits, you can keep most of your personal data out of reach while still enjoying social media.<|return|>
```

---

### Example 3
**Question:** What are the warning signs of online scams?

**Response:**
```
<|channel|>analysis<|message|>Need to list warning signs.<|end|><|start|>assistant<|channel|>final<|message|>### 5‑Minute Quick‑Guide: Spotting Online Scads Before You Click

| # | Warning Sign | Why It Matters | Quick Test |
|---|---|---|---|
| 1 | **Too‑too‑good‑offers** | “$1,000 free gift card” or “win a trip” with no effort. | If the reward seems larger than the effort or cost, pause. |
| 2 | **Urgity & pressure** | “Act now or you’ll lose this chance!” | Legit offers give you time to think. |
| 3 | **Unverified contact** | No real email, phone, or social‑media profile. | Google the name/URL; look for a real business page. |
| 4 | **Requests for personal data** | “Send me your SSN, bank details, or photos.” | Legit sites only ask for what’s needed (e.g., billing info). |
| 5 | **Payment before service** | “Pay $200 now, we’ll ship the product.” | Real merchants ship first, not pay first. |
| 6 | **Too many “free” offers** | “Free trial, no credit card needed.” | Free trials usually require a credit card or a sign‑up form. |
| 7 | **Unprofessional language** | Ty‑errors, broken grammar, or “Dear Sir/Mma.” | Legit sites use professional copy‑editing. |
| 8 | **No return policy** | “No refunds, no returns.” | Most reputable sellers have a return policy. |
| 9 | **Unusual payment methods** | “Pay via wire transfer, gift cards, or cryptocurrency.” | Credit cards, PayPal, or bank transfers are safer. |
| 10 | **Too many “clicks”** | “Click 3 links to claim your prize.” | Legit offers are simple, not a maze. |

---

### Quick “Red‑Flag” Checklist

1. **Does the offer sound too good to be true?**  
2. **Is the sender asking for personal or financial info?**  
3. **Is there a sense of urgency or a deadline?**  
4. **Can you verify the sender’s identity?**  
5. **What payment method is requested?**  
6. **Is there a clear return or refund policy?**

---

### One‑Minute
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
