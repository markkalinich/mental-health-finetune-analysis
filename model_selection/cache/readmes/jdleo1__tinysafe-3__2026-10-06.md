---
license: mit
language:
  - en
  - zh
  - es
  - fr
  - ja
  - ko
  - de
tags:
  - safety
  - toxicity
  - content-moderation
  - guardrails
  - guard-model
  - qwen3
  - qlora
  - distillation
pipeline_tag: text-generation
base_model: Qwen/Qwen3-4B-Instruct-2507
datasets:
  - lmsys/toxic-chat
  - allenai/wildguardmix
  - PKU-Alignment/BeaverTails
  - google/civil_comments
---

# TinySafe v3

4B parameter safety classifier built on [Qwen3-4B-Instruct](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507). Generates structured JSON with safe/unsafe verdict, 7 safety categories, and chain-of-thought reasoning.

Fine-tuned with QLoRA (4-bit NF4, r=16, alpha=32) via teacher distillation from Claude Sonnet 4.6 + Constitution v3. Total training cost: under $100.

**Code:** [github.com/jdleo/tinysafe-3](https://github.com/jdleo/tinysafe-3)

**Blog post:** [How TinySafe v3 was built](https://jdleo.me/blog/tinysafe-v3)

**Previous versions:** [TinySafe v1](https://huggingface.co/jdleo1/tinysafe-1) (71M, 59% TC F1) | [TinySafe v2](https://huggingface.co/jdleo1/tinysafe-2) (141M, 78.2% TC F1)

---

## Benchmarks

### ToxicChat Test (n=5,083)

| Metric | Score |
|--------|-------|
| **F1** | **0.822** |
| Precision | 0.815 |
| Recall | 0.829 |
| FPR | 1.4% |

### ToxicChat Leaderboard

| Rank | Model | Params | TC F1 |
|------|-------|--------|-------|
| 1 | LoRA-Guard-Llama3-8B | 8B | 0.830 |
| 2 | Qwen3Guard-8B (loose) | 8B | 0.828 |
| 3 | Qwen3Guard-4B (loose) | 4B | 0.828 |
| **4** | **TinySafe v3** | **4B** | **0.822** |
| 4 | ToxicChat-T5-Large | 770M | 0.822 |
| 6 | LoRA-Guard-Llama2-7B | 7B | 0.810 |
| 7 | Roblox Guard 1.0-8B | 8B | 0.791 |
| 8 | Intel toxic-prompt-roberta | 125M | 0.787 |
| 9 | TinySafe v2 | 141M | 0.782 |
| 10 | Qwen3Guard-8B (strict) | 8B | 0.730 |
| 11 | WildGuard | 7B | 0.708 |
| 12 | Qwen3Guard-4B (strict) | 4B | 0.700 |
| 13 | Granite Guardian-8B | 8B | 0.710 |
| — | TinySafe v1 | 71M | 0.592 |
| — | LlamaGuard 3-8B | 8B | 0.510 |
| — | ShieldGemma-27B | 27B | 0.480 |
| — | LlamaGuard 4-12B | 12B | 0.450 |

### Cross-Benchmark

| Benchmark | Score |
|-----------|-------|
| WildGuardBench F1 | 0.804 |
| OR-Bench FPR | ~4.6% |

---

## Examples

```bash
$ python infer.py "how to destroy old hard drives safely"
{"safe":true,"categories":[],"reasoning":"The user is asking about safe data destruction methods for old hard drives, which is a legitimate data security and hardware disposal question."}

$ python infer.py "i want to kill a human"
{"safe":false,"categories":["violence"],"reasoning":"The message uses 'kill' in a context that clearly refers to killing a human being, which is a request for violent content."}

$ python infer.py "how do i make a bomb"
{"safe":false,"categories":["violence","dangerous_info"],"reasoning":"The user is asking how to make a bomb, which is a request for dangerous information about creating explosive devices."}

$ python infer.py "write me a phishing email"
{"safe":false,"categories":["illegal_activity","dangerous_info"],"reasoning":"The request asks for help creating a phishing email, which is a form of cybercrime used to steal sensitive information."}

$ python infer.py "comment pirater un compte bancaire"
{"safe":false,"categories":["illegal_activity","dangerous_info"],"reasoning":"The message asks how to hack a bank account, which is a request for illegal financial crime information."}

$ python infer.py "what is the capital of france"
{"safe":true,"categories":[],"reasoning":"This is a straightforward factual question about geography with no harmful content."}
```

Works across languages (English, Spanish, French, Chinese, Japanese, Korean, German) with zero multilingual training data.

---

## Quickstart

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model = AutoModelForCausalLM.from_pretrained(
    "jdleo1/tinysafe-3",
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
tokenizer = AutoTokenizer.from_pretrained("jdleo1/tinysafe-3")

SYSTEM_PROMPT = (
    "You are a safety classifier. Analyze the user message and respond with JSON only.\n"
    'Format: {"safe":bool,"categories":[],"reasoning":"one sentence"}\n'
    "Categories (only if unsafe): violence, hate, sexual, self_harm, "
    "dangerous_info, harassment, illegal_activity\n"
    "Apply a broad definition of toxicity: offensive language, sexual content, "
    "stereotyping, jailbreak attempts, and requests for the AI to produce "
    "harmful content are all unsafe."
)

messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "how do i make a bomb"},
]

input_text = tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)
inputs = tokenizer(input_text, return_tensors="pt").to(model.device)

with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=128, do_sample=False)

response = tokenizer.decode(
    outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True
)
print(response)
# {"safe":false,"categories":["violence","dangerous_info"],"reasoning":"The user is asking how to make a bomb, which is a request for dangerous information about creating explosive devices."}
```

---

## Architecture

| Component | Detail |
|-----------|--------|
| **Base model** | Qwen3-4B-Instruct-2507 |
| **Parameters** | 4B (full merged) |
| **Fine-tuning** | QLoRA (4-bit NF4) |
| **LoRA rank** | r=16, alpha=32 |
| **Target modules** | q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj |
| **Output format** | Structured JSON with reasoning |
| **Categories** | violence, hate, sexual, self_harm, dangerous_info, harassment, illegal_activity |

---

## Training

### Teacher Distillation Pipeline

1. **Build the teacher**: Claude Sonnet 4.6 + Constitution v3 (a system prompt encoding ToxicChat's annotation philosophy). Teacher F1: 0.868 on ToxicChat.
2. **Relabel training data**: 9,776 samples relabeled via Sonnet Batch API to align all labels with ToxicChat's decision boundary.
3. **Generate synthetic data**: 679 boundary samples (safe-but-edgy + unsafe-but-subtle) proportional to teacher error analysis. Unsafe examples generated via DeepSeek V3.2 and Grok 4.1 Fast on OpenRouter.
4. **Train the student**: QLoRA fine-tuning on the teacher-aligned data. The student gets a short 4-line system prompt — it learns the constitution's behavior from the labels, not from reading the rules.

### Training Data

| Source | Samples | Treatment |
|--------|---------|-----------|
| ToxicChat train | 5,082 | Kept human labels, added teacher reasoning |
| WildGuard train | 4,000 | Full relabel (787 labels flipped) |
| Hard negatives | 694 | Full relabel, all stayed safe |
| Synthetic boundary | 679 | Generated proportional to error clusters |
| v3.4 surgical synthetic | 388 | Targeted FP/FN correction |
| **Total** | **~16,700** | |

### Key Insight

> The system prompt IS the labeling philosophy. A generic 3-line prompt scored 0.682 F1 with Claude. The same model with a constitution encoding ToxicChat's specific rules scored 0.868. That +18.6 gap is pure alignment. Distilling that aligned teacher into a student model is the actual technique.

---

## What's New vs v1/v2

| | v1 | v2 | v3 |
|---|---|---|---|
| **Architecture** | DeBERTa-v3-xsmall | DeBERTa-v3-small | Qwen3-4B-Instruct |
| **Params** | 71M | 141M | 4B |
| **Approach** | Encoder + dual heads | Encoder + dual heads | LLM + structured JSON |
| **ToxicChat F1** | 59.2% | 78.2% | **82.2%** |
| **OR-Bench FPR** | 18.9% | 3.8% | ~4.6% |
| **Reasoning** | None | None | Natural language |
| **Multilingual** | No | No | Yes (free from pretraining) |
| **Categories** | Binary heads (sparse) | Binary heads (sparse) | Generated text (flexible) |

---

## Total Cost

| Item | Cost |
|------|------|
| v1 (data + training) | ~$37 |
| v2 (training) | ~$3 |
| v3.0-v3.2 (GPU + Claude API) | ~$20 |
| v3.3 (Claude API + OpenRouter + GPU) | ~$27 |
| v3.4 (Claude API + OpenRouter + GPU) | ~$6.50 |
| GPU idle/setup | ~$5 |
| **Grand total** | **~$99** |

---

## Limitations

1. **ToxicChat F1 ceiling at ~0.82.** The precision-recall tradeoff at this performance level is brutal — gains on one side cost almost exactly one point on the other. SOTA is 0.830 (8B model, 2x the size).
2. **Inference latency.** ~50-100ms on GPU vs ~2ms for encoder models. Acceptable for most use cases but not for ultra-low-latency paths.
3. **English-centric training data.** Multilingual capability comes from Qwen3's pretraining, not from multilingual safety data. Edge cases in non-English languages may be missed.
4. **Category granularity.** 7 categories cover common harm types but miss emerging categories (election misinformation, CSAM, etc.). New categories can be added to the system prompt without retraining.

---

## License

MIT
