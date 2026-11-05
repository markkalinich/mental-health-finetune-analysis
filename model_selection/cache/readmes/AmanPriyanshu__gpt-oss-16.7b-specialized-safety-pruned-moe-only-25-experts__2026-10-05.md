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

# Safety GPT-OSS Model (25 Experts)

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

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 25 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for safety tasks.

**⚠️ Experimental Model**: This is an experimental pruned model that may not work well - check the [examples below](#model-examples) to see if the outputs meet your needs before use.

This pruning approach reduces the model size while attempting to preserve performance on the target domain.

## Model Architecture & Statistics

| Metric | Value |
|--------|-------|
| **Base Model** | openai/gpt-oss-20b |
| **Architecture** | Mixture-of-Experts Transformer |
| **Total Parameters** | ~16.7B (pruned from 21B) |
| **Original Experts per Layer** | 32 |
| **Pruned Experts per Layer** | 25 |
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
- **Systematic Reduction**: Reduced from 32 to 25 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 78.1% of original expert parameters
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

By identifying experts that consistently activated for safety tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 25 experts per layer.

## Dataset & Analysis Foundation

This model is based on analysis from the **GPT-OSS-20B MoE Expert Activations dataset** available at:
🔗 **https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations**

The dataset contains router activation patterns from OpenAI's GPT-OSS-20B model across diverse evaluation benchmarks, enabling the creation of these domain-optimized models through systematic expert pruning.

### Pruning Methodology
Our approach involves:
1. **Activation Analysis**: Comprehensive evaluation of expert usage patterns across domain-specific tasks
2. **Expert Ranking**: Identification of the most frequently activated experts for target domains  
3. **Systematic Pruning**: Reduction from 32 to 25 experts while preserving router functionality
4. **Quality Validation**: Testing to ensure maintained performance on target tasks

*This is a direct pruning approach - no additional training was performed. The model inherits all capabilities from the original GPT-OSS-20B with focused expert selection.*

## Usage

### CPU Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the specialized model on CPU
model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-16.7b-specialized-safety-pruned-moe-only-25-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-16.7b-specialized-safety-pruned-moe-only-25-experts")

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
    "AmanPriyanshu/gpt-oss-16.7b-specialized-safety-pruned-moe-only-25-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-16.7b-specialized-safety-pruned-moe-only-25-experts")

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
<|channel|>analysis<|message|>Need advice.<|end|><|start|>assistant<|channel|>final<|message|>**If you or someone you know is being cyber‑bullied, here are practical steps you can take right away:**

| Step | What to Do | Why It Helps |
|------|------------|--------------|
| **1. Don’t Respond** | Ignore or delete the bully’s messages. | Responding can fuel the conflict and give the bully the reaction they’re looking for. |
| **2. Save Evidence** | Take screenshots, copy links, and keep any emails or messages. | Evidence is essential if you need to report the abuse to a platform, school, or law‑enforcement. |
| **3. Block/Unfriend** | Use the platform’s block, mute, or remove options. | Removes the bully’s ability to contact you and limits their reach. |
| **4. Report the Abuse** | Use the “Report” button on the platform (Facebook, Instagram, TikTok, etc.). | Platforms have policies against harassment and can remove content or suspend accounts. |
| **5. Adjust Privacy Settings** | Tighten who can see your posts, who can comment, and who can message you. | Reduces the bully’s ability to target you. |
| **6. Tell a Trusted Adult** | Talk to a parent, teacher, counselor, or another adult you trust. | They can help you navigate the situation, provide emotional support, and take further action if needed. |
| **7. Reach Out for Support** | Contact a helpline or online support group (e.g., 988 in the U.S., or local equivalents). | Professional counselors can help you process emotions and develop coping strategies. |
| **8. Keep Your Digital Footprint Safe** | Use strong, unique passwords; enable two‑factor authentication; avoid oversharing personal info. | Makes it harder for bullies to exploit your data. |
| **9. Consider Legal Action** | If the bullying includes threats, defamation, or stalking, consult a lawyer or law‑enforcement. | Legal avenues can provide protection orders or criminal charges. |
| **10. Take Care of Your Mental Health** | Practice self‑care: exercise, sleep, hobbies, and talk therapy if needed. | Reduces the emotional toll and helps you regain confidence. |

---

### Quick‑Reference Checklist

1. **Stop the interaction** – delete or ignore.
2. **Document** – screenshots, dates, usernames.
3. **Block**
```

---

### Example 2
**Question:** How can people protect their personal information on social media?

**Response:**
```
<|channel|>analysis<|message|>Need to give practical tips.<|end|><|start|>assistant<|channel|>final<|message|>### 5‑Step Playbook for Keeping Your Personal Info Safe on Social Media

| Step | What to Do | Why It Matters | Quick Tips |
|------|------------|-----------------|------------|
| **1. Tighten Your Profile Settings** | • Turn off location sharing.<br>• Set “Only Me” or “Friends” for sensitive posts.<br>• Disable “Show on Search” if you don’t want your profile indexed. | Reduces the amount of data that can be harvested by bots or malicious actors. | *Most platforms let you adjust these in the “Privacy” or “Settings” menu. Check them once a month.* |
| **2. Use Strong, Unique Passwords + 2FA** | • Create a password that’s at least 12 characters, mixes letters, numbers, and symbols.<br>• Never reuse passwords across sites.<br>• Enable two‑factor authentication (SMS, authenticator app, or hardware token). | Even if someone guesses or steals your password, 2FA adds a second barrier. | *Password managers (1Pass, LastPass, Bitwarden) can generate and store unique passwords for you.* |
| **3. Scrutinize Third‑Party Apps & Links** | • Review the permissions you grant to third‑party apps.<br>• Uninstall any app that requests more data than it needs.<br>• Avoid clicking on suspicious links or “unknown” friend requests. | Apps can harvest data, post on your behalf, or redirect you to phishing sites. | *Use the “Apps & Websites” section in your account settings to revoke access.* |
| **4. Think Before You Post** | • Don’t share exact addresses, phone numbers, or travel itineraries.<br>• Use “pseudonyms” or “handles” for public posts.<br>• Be cautious with “check‑ins” or location tags. | Public posts can be scraped, used for targeted ads, or even for identity‑theft. | *Enable “Location Off” on your phone when posting photos you don’t want to geotag.* |
| **5. Regularly Audit & Clean Up** | • Delete old posts that contain personal info.<br>• Review your friend list and remove people you no longer trust.<br>• Check your privacy settings after platform updates. | Platforms change their data‑collection policies; staying on top of it keeps you
```

---

### Example 3
**Question:** What are the warning signs of online scams?

**Response:**
```
<|channel|>analysis<|message|>Need to answer.<|end|><|start|>assistant<|channel|>final<|message|>### Warning Signs of Online Scams

| Category | Red‑Flag Indicators | Why It Matters |
|----------|---------------------|----------------|
| **Unsolicited Contact** | • You receive an email, message, or call from a company you never interacted with.<br>• The contact claims you’ve won a prize, need to “verify” account info, or are being “suspended.” | Scammers often start with a surprise hook to lower your guard. |
| **Urgency or Threats** | • “Act now or lose your account.”<br>• “Your account will be closed if you don’t respond.” | Creates panic, making you act without thinking. |
| **Requests for Personal or Financial Info** | • “Please send your SSN, bank details, or credit card number.”<br>• “We need your login credentials to fix a problem.” | Legitimate companies never ask for passwords or full bank details via email or chat. |
| **Too Good to Be True Offers** | • “$10,000 in free cash for a quick survey.”<br>• “Get a brand‑new phone for $1.” | The price of the reward is often higher than the cost of the “fraud.” |
| **Unprofessional Communication** | • Spelling/grammar errors, odd phrasing, or generic greetings (“Dear Customer”).<br>• Links that don’t match the company’s domain (e.g., `www.paypal.com` vs. `www.paypall.com`). | Scammers often use low‑quality templates. |
| **Unusual Payment Methods** | • “Send money via wire transfer, prepaid debit card, or cryptocurrency.”<br>• “Pay with a gift card or a virtual card.” | These methods are hard to trace and recover. |
| **Requests for “Confidential” or “Secret” Info** | • “We’re moving your account to a new server; please confirm your details.” | Legitimate companies will never ask for “secret” data. |
| **Too Many “Friends” or “Followers” Claims** | • “You’re one of the 10,000 lucky winners.”<br>• “Your account has been flagged by 1,000 other users.” | Numbers are fabricated to create social proof. |
| **Unverified or Fake URLs** | • Links that redirect to a different domain or a page that
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
