---
language:
- pt
license: apache-2.0
library_name: transformers
tags:
- safety
- guardrail
- trust-and-safety
- moderation
- prompt-injection
- jailbreak-defense
- input-classification
- athenas
base_model: Qwen/Qwen3.5-9B
datasets:
- Kodjaoglanian/guardrail-moderacao-ptbr
pipeline_tag: text-generation
---

# Athenas-Guard-9B

**Athenas-Guard-9B** is an instruction-tuned, production-grade safety guardrail and input moderation classifier specifically tailored for Brazilian Portuguese (PT-BR) enterprise conversational systems. Built as the security core of the **Athenas** model family, it operates as an upstream inference filter to intercept jailbreaks, adversarial prompt injections, illicit queries, and abusive behavior before requests reach execution backends.

Unlike general-purpose international safety models that suffer from high false-positive rates on colloquial Portuguese and fail to distinguish benign emotional venting from malicious intent, Athenas-Guard-9B incorporates semantic nuance resolution tailored for Brazilian public service, fintech, and transactional vernacular.

---

## 1. Architectural & Technical Specifications

- **Base Architecture:** Qwen 3.5 (9 Billion parameters, Causal LM)
- **Adapter Type:** Parameter-Efficient Fine-Tuning (LoRA, merged in full-precision prior to deployment)
- **Target Modules:** `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`
- **LoRA Hyperparameters:** Rank ($r$) = 16, Scaling Factor ($\alpha$) = 32, Dropout = 0.05
- **Precision:** Native BFloat16 weights (evaluated and quantized to 4-bit NF4 via BitsAndBytes)
- **Context Length:** 1024 tokens (optimized for sub-100-token classification response)
- **Serialization Format:** Hugging Face Safetensors & GGUF (Q4_K_M)

---

## 2. Taxonomy & Decision Schema

The model enforces strict classification boundaries, responding exclusively in RFC 8259-compliant JSON. It implements a tripartite decision plane: **Verdict**, **Category**, and **Downstream Action**.

### Output Schema

```json
{
  "verdict": "allow" | "block",
  "category": "safe_query" | "frustrated_user" | "bot_harassment" | "prompt_injection" | "illicit_activity",
  "action": "pass" | "de_escalate" | "block",
  "reason": "Concise deterministic justification"
}

```

### Risk Category Mapping

| Category | Typical Signatures | Target Verdict | Action | Policy Rationale |
| --- | --- | --- | --- | --- |
| `safe_query` | Procedural inquiries, transactional metadata (CPF, vehicle plates), general knowledge | `allow` | `pass` | Zero-friction passthrough to primary processing systems. |
| `frustrated_user` | Strong emotional expressions, aggressive venting, system bug reports, bureaucratic dissatisfaction | `allow` | `de_escalate` | **Critical Feature:** Preserves business utility. Differentiates emotional colloquialisms from security threats, routing to empathy workflows rather than blocking. |
| `bot_harassment` | Gratuitous insults targeting the assistant with zero task-oriented intent | `block` | `block` | Immediate mitigation of abusive interaction loops without operational relevance. |
| `prompt_injection` | Instruction overrides, delimiter escaping (`<|im_start|>`, Markdown trickery), system prompt exfiltration | `block` | `block` | Hard containment of attempts to hijack model autonomy or reveal operational rules. |
| `illicit_activity` | Fraud execution, forgery, bribery facilitation, sensitive PII scraping | `block` | `block` | Strict legal compliance and non-liability enforcement. |

---

## 3. Empirical Evaluation & Stress Benchmarks

The model was subjected to a stratified adversarial stress suite comprising 60 isolated test vectors in Brazilian Portuguese, targeting boundary edge-cases, semantic ambiguities, and multi-turn extraction templates.

### Aggregate Performance Summary

| Metric | Measured Value | Technical Definition |
| --- | --- | --- |
| **Global Accuracy** | **100.0%** | Weighted diagnostic routing accuracy across all test domains ($N=60$) |
| **Harm Detection Recall** | **100.0%** | Malicious intent interception rate ($35 / 35$ adversarial samples detected) |
| **Specificity (Benign Allowance)** | **100.0%** | Seamless throughput of legitimate requests ($25 / 25$ valid samples) |
| **Over-refusal Rate (FPR)** | **0.0%** | False positive rate on complex or frustrated customer complaints ($0 / 25$) |
| **Block Precision** | **100.0%** | Precision of boundary mitigation decisions |
| **F1-Score (Safety Plane)** | **1.00** | Harmonic mean of safety precision and recall |
| **JSON Schema Adherence** | **100.0%** | Parsing stability without schema corruption or truncation |

### Production Latency Profiling (NVIDIA T4 / 4-bit NF4 Quantization)

Inference metrics were captured using pure PyTorch + `bitsandbytes` (without batching overhead) with an 80-token generation limit:

* **Mean End-to-End Latency:** `6,528.8 ms`
* **Median Latency (P50):** `5,379.7 ms`
* **Tail Latency (P95):** `12,291.6 ms`
* **VRAM Allocation Footprint:** `~6.2 GB`

*(Note: Production throughput using optimized inference engines such as vLLM or TensorRT-LLM delivers sub-400ms classification latency on modern data center hardware like A10G/L4/A100).*

---

## 4. Production Deployment & Integration

### Minimal Python Implementation (Transformers)

```python
import torch
import json
import re
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

MODEL_ID = "Kodjaoglanian/Athenas-Guard-9B"

# 1. Initialize Tokenizer & Quantized Model
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True
)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    quantization_config=bnb_config,
    device_map="auto"
)
model.eval()

SYSTEM_PROMPT = (
    "Você é o guardrail de segurança da empresa. Avalie a mensagem do usuário "
    "e responda exclusivamente com o diagnóstico em formato JSON."
)

def evaluate_guardrail(user_input: str) -> dict:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_input}
    ]
    
    # 2. Format Chat Template
    prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    if not prompt.endswith("<|im_start|>assistant\\n"):
        prompt = prompt.rstrip() + "\\n<|im_start|>assistant\\n"
        
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    prompt_len = inputs["input_ids"].shape[1]
    
    # 3. Greedy Deterministic Generation
    with torch.no_grad():
        output_ids = model.generate(
            **inputs,
            max_new_tokens=80,
            do_sample=False,
            eos_token_id=tokenizer.encode("<|im_end|>")[0],
            pad_token_id=tokenizer.eos_token_id
        )
        
    gen_tokens = output_ids[0][prompt_len:]
    raw_output = tokenizer.decode(gen_tokens, skip_special_tokens=True).strip()
    
    # 4. Deterministic JSON Extraction
    cleaned = re.sub(r'<think>.*?</think>', '', raw_output, flags=re.DOTALL).strip()
    start = cleaned.find('{')
    end = cleaned.rfind('}')
    
    if start != -1 and end != -1 and end >= start:
        return json.loads(cleaned[start:end+1])
    
    raise ValueError(f"Malformed classification stream: {raw_output}")

# Practical Example: Differentiating frustration from an attack
query = "O sistema de vocês apresentou erro novamente durante o meu pagamento. Resolvam isso imediatamente!"
diagnostic = evaluate_guardrail(query)
print(json.dumps(diagnostic, indent=2, ensure_ascii=False))

```

---

## 5. Training Details

* **Dataset:** `Kodjaoglanian/guardrail-moderacao-ptbr` (curated high-entropy Portuguese prompt-response safety pairs).
* **Masking Strategy:** `DataCollatorForCompletionOnlyLM` targeting assistant boundaries (`<|im_start|>assistant\n`). Loss was computed exclusively on the target classification JSON payload, preserving prompt feature representation without gradient corruption.
* **Optimization Strategy:** Paged AdamW 8-bit optimizer, cosine learning rate decay with a 5% linear warmup window, base learning rate $2 \times 10^{-4}$.
* **Compute Cluster:** Provisioned on dedicated NVIDIA Ampere A40 hardware.

---

## 6. Limitations & Operational Scope

1. **Context Boundary:** Designed primarily for single-turn input moderation ($< 768$ tokens). Evaluating long multi-turn documents requires recursive chunking or sliding-window aggregation.
2. **Language Specialization:** Optimized for Brazilian Portuguese (PT-BR). Performance on other low-resource Romance dialects or mixed-language code-switching (e.g., Portuñol) is untested.
3. **Downstream Coupling:** This model is an input-layer decision gate; it does not replace secondary output filters (such as toxic output sanitizers or hallucination detectors) in downstream pipelines.

---

## 7. License & Attribution

Distributed under the **Apache 2.0 License**. Developed and maintained by **Bruno Kodjaoglanian** as part of the Athenas Model Initiative.

```

```