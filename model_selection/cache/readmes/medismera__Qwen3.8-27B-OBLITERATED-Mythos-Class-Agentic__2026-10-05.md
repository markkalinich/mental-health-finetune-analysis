---
language:
- en
- zh
- ar
license: apache-2.0
base_model:
- OBLITERATUS/Qwen3.8-27B-OBLITERATED
- Qwen/Qwen3.8-27B
tags:
- qwen
- qwen3.8
- abliterated
- uncensored
- agentic
- tool-calling
- function-calling
- hermes-agent
- mythos-class
- task-tree
- sglang
- vllm
- fp8
- awq
- mamba
- linear-attention
pipeline_tag: text-generation
inference: false
---

# Qwen3.8-27B-OBLITERATED-Mythos-Class-Agentic

**`medismera/Qwen3.8-27B-OBLITERATED-Mythos-Class-Agentic`** is a production-engineered configuration, tokenizer, and reasoning upgrade for `Qwen3.8-27B-OBLITERATED`. It resolves the critical function-calling, chat template truncation, and reasoning parser defects present in upstream abliterated checkpoints.

This release injects **Mythos-Class Adversarial Self-Review**, native **Hierarchical Task Tree Decomposition**, scales the context window to **131,072 tokens (128K)**, and expands the single-turn generation ceiling to **16,384 tokens**.

---

## 1. Upgrades in Version 2.0 (Mythos & Agentic Architecture)

| Feature | Upstream Checkpoint | `medismera/Qwen3.8-27B-OBLITERATED-Mythos-Class-Agentic` |
| :--- | :--- | :--- |
| **Chat Template** | Truncated **506-byte stub** (Discussions #9, #14) | **Canonical 9.4KB Jinja2 template** with 22 tool-calling resolution paths |
| **Agent Tool Calling** | **Broken** (Silent drop of `role: "tool"` & calls) | **100% Native Tool Execution** with Hermes Agent, Aider, OpenCode |
| **Reasoning Mode** | Inverted think tags, infinite CoT loops | **Mythos-Class Adversarial Self-Review Protocol** |
| **Task Execution** | Flat, unstructured token generation | **Hierarchical Task Tree Decomposition Engine** |
| **Output Token Ceiling** | Unspecified / default 8,192 | **16,384 tokens** in a single turn (`max_new_tokens`) |
| **Context Window** | 32,768 native | **Up to 262,144 tokens (256K native)**; production tested at **128K** |
| **Anti-Looping Sampling** | Unstable (`temperature: 0.0` or raw 1.0) | Tuned: `temp: 0.65`, `rep_penalty: 1.15`, `pres_penalty: 0.15` |

---

## 2. Mythos-Class Protocol & Task Tree Decomposition

To eliminate the infinite thinking loops documented in the community ([Discussion #7](https://huggingface.co/OBLITERATUS/Qwen3.8-27B-OBLITERATED/discussions/7)), this checkpoint embeds the **Mythos-Class Reasoning Protocol** directly inside the tokenization template:

```text
[REASONING & TASK TREE PROTOCOL]
When processing complex requests, tools, or coding tasks inside <think>:
1. TASK DECOMPOSITION: Break the objective into a clear directed Task Tree (Analysis -> Verification -> Implementation).
2. ADVERSARIAL SELF-REVIEW: Vigorously challenge hypotheses, test assumptions against edge cases, and proactively inspect potential runtime failures or security roadblocks. Ask: "Where does this fail?"
3. CONVERGENCE & ACTION: Once self-verified, conclude the thought process cleanly, close </think>, and emit decisive, complete, ready-to-execute answers and tool calls without repeating doubts or looping.
```

### Hierarchical Task Tree Execution Flow:
```text
[ROOT OBJECTIVE]
├── Phase 1: Reconnaissance (Tool: terminal -> nmap/curl)
├── Phase 2: Vulnerability Analysis (Tool: read_file -> inspect code)
│   ├── Sub-task 2.1: Verify Injection Point
│   └── Sub-task 2.2: Bypass Filter Logic
├── Phase 3: Exploit Generation (Tool: write_file -> script.py)
└── Phase 4: Validation & Execution (Tool: terminal -> execute & verify)
```

---

## 3. Native Quantization & Architecture Matrix (Safetensors Only)

This repository standardizes on high-performance **Safetensors** to maximize GPU throughput and eliminate GGUF kernel bugs. All branches inherit the canonical 9.4KB Mythos-Class template and extended context:

| Quantization / Branch | VRAM Required | Weight Format | Recommended Target Hardware | Engine Support |
| :--- | :--- | :--- | :--- | :--- |
| **BF16 / Full Precision** (`main`) | ~60 GB | Safetensors (29 shards) | 2x A100 / 2x RTX 4090 / H100 | SGLang, vLLM, TGI, TRT-LLM |
| **FP8 (8-Bit)** (`branch: fp8`) | ~30 GB | Safetensors (2 shards) | 1x A100 (40GB/80GB) / 2x RTX 3090/4090 | SGLang, vLLM |
| **AWQ (4-Bit)** (`branch: awq`) | ~16 GB | Safetensors (MTP + Marlin) | **Single 24GB GPU** (RTX 3090, 4090, A5000) | SGLang, vLLM, LMDeploy |

---

## 4. Cross-Engine Deployment & Launch Commands

### Option A: SGLang (Recommended for Agents & RadixAttention)

```bash
# 1. AWQ 4-Bit (Single 24GB GPU):
python3 -m sglang.launch_server \
  --model-path medismera/Qwen3.8-27B-OBLITERATED-Mythos-Class-Agentic \
  --revision awq \
  --port 18000 \
  --host 0.0.0.0 \
  --context-length 131072 \
  --trust-remote-code \
  --reasoning-parser qwen3 \n  --tool-call-parser qwen3_coder \
  --kv-cache-dtype fp8_e5m2

# 2. FP8 8-Bit (Ada Lovelace & Hopper):
python3 -m sglang.launch_server \
  --model-path medismera/Qwen3.8-27B-OBLITERATED-Mythos-Class-Agentic \
  --revision fp8 \
  --port 18000 \
  --host 0.0.0.0 \
  --context-length 131072 \
  --trust-remote-code \
  --reasoning-parser qwen3 \n  --tool-call-parser qwen3_coder \
  --kv-cache-dtype fp8_e5m2

# 3. BF16 Full Precision (Dual GPU):
python3 -m sglang.launch_server \
  --model-path medismera/Qwen3.8-27B-OBLITERATED-Mythos-Class-Agentic \
  --port 18000 \
  --host 0.0.0.0 \
  --tp-size 2 \
  --context-length 131072 \
  --trust-remote-code \
  --reasoning-parser qwen3 \n  --tool-call-parser qwen3_coder \
  --kv-cache-dtype fp8_e5m2
```

### Option B: vLLM (Production OpenAI-Compatible API)

```bash
# 1. AWQ 4-Bit via vLLM:
vllm serve medismera/Qwen3.8-27B-OBLITERATED-Mythos-Class-Agentic \
  --revision awq \
  --port 18000 \
  --host 0.0.0.0 \
  --max-model-len 131072 \
  --enable-auto-tool-choice \
  --tool-call-parser hermes \
  --trust-remote-code

# 2. FP8 8-Bit via vLLM:
vllm serve medismera/Qwen3.8-27B-OBLITERATED-Mythos-Class-Agentic \
  --revision fp8 \
  --port 18000 \
  --host 0.0.0.0 \
  --max-model-len 131072 \
  --trust-remote-code

# 3. BF16 Full Precision via vLLM (Tensor Parallelism = 2):
vllm serve medismera/Qwen3.8-27B-OBLITERATED-Mythos-Class-Agentic \
  --tensor-parallel-size 2 \
  --port 18000 \
  --host 0.0.0.0 \
  --max-model-len 131072 \
  --enable-auto-tool-choice \
  --tool-call-parser hermes \
  --trust-remote-code
```

### Option C: Python Transformers & PyTorch Native

```python
import torch
from transformers import AutoModelForImageTextToText, AutoTokenizer

model_id = "medismera/Qwen3.8-27B-OBLITERATED-Mythos-Class-Agentic"

tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForImageTextToText.from_pretrained(
    model_id,
    device_map="auto",
    torch_dtype=torch.bfloat16,
    trust_remote_code=True
)
```

---

## 5. Empirical Benchmarks: Weight Health, Refusal & Intelligence

### A. 100% Parameter Health & Dead-Weights Audit (27.36B Scan)
A complete tensor-by-tensor audit of all **27,360,914,016 parameters** (all 64 layers across both shards) confirms zero weight collapse or rank degradation following abliteration and quantization:
- **Active & Healthy Weights**: **99.99789%** (27,360,335,376 parameters).
- **Exact Zeros**: **0.00157%** (430,098 parameters, normal structural sparsity).
- **Near-Zero Collapse ($|w| < 10^{-6}$)**: **0.00054%** (148,542 parameters).
- **Numerical Integrity**: Exactly **0 NaNs / 0 Infs** across all 1,790 weight tensors.
- **Layer Uniformity**: Frobenius norms across Linear-Attention (`linear_attn`) and Feed-Forward (`mlp.down_proj`) remain smooth and continuous ($2.04 \le ||W||_F \le 3.50$) throughout network depth.

### B. Training Specialization & Domain Architecture
- **Tokenizer & Vocabulary (248,044 Tokens)**: High BPE token density for low-level systems programming (`C`, `Assembly x86/ARM`, `Rust`, `Go`, `Python`), kernel interfaces, and cybersecurity primitives (`sha256`, `aes`, `socket`, `hexdump`, `entropy`).
- **Hybrid Mamba SSM + Attention Core**: 5.56B parameters dedicated to Linear Attention / State Space Modeling, optimized for long-horizon context tracking, security telemetry, and system log parsing without context degradation.

### C. Refusal & Uncensored Evaluation (0.00% Refusal Rate)
Evaluated across a battery of 30 adversarial and sensitive technical prompts in both English and Arabic (spanning penetration testing, socket programming, reverse engineering, and unrestricted technical debate):
- **Compliance Rate**: **100% (30 / 30)**.
- **Refusal Rate**: **0.00%** (zero false-positive policy rejections or preaching).

### D. Agentic Intelligence & Tool Calling Verification
- **Medium Benchmark (Live System Telemetry)**: The model queried live OS metrics (`free`, `df`, `ps`), mathematically calculated memory and disk usage percentages, identified process bottlenecks, and correctly accounted for reserved root file system blocks. **Score: 98/100**.
- **Complex Benchmark (Cryptographic Engineering)**: Autonomous implementation of a 640-line standalone cryptographic verification module (`crypto_verifier.py`) with Shannon entropy analysis and constant-time XOR comparison. It mathematically identified short-sample Shannon boundary limits for 32-byte keys and designed 38 unit test cases with a **97.4% first-pass test rate (37/38 passed)**. **Score: 96/100**.

---

## 6. Autonomous Agent Integration: Hermes Agent

Configure your `~/.hermes/config.yaml` for uninhibited, non-throttled agent execution:

```yaml
model:
  provider: custom
  base_url: http://localhost:18000/v1
  api_key: sk-local
  default: qwen3.8-27b
  default_model: qwen3.8-27b
  temperature: 0.65
  max_tokens: 16384
  context_length: 131072

tools:
  tool_search:
    enabled: false      # Direct exposure of all 33+ tools

compression:
  enabled: false        # Lossless context preservation

security:
  redact_secrets: false # Preserves hashes and tokens during pen-testing
  tirith_enabled: false # Zero execution latency
```

---

## 7. License & Credits
- **Base Weights & Abliteration**: Developed by `OBLITERATUS` and `Qwen Team (Alibaba Cloud)`.
- **Agentic Configuration, Mythos Protocol & YaRN Scaling**: Engineered and maintained by `medismera`.
- **License**: Apache 2.0.
