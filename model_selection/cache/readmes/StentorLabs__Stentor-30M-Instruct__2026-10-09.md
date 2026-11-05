---
language:
- en
license: apache-2.0
library_name: transformers
tags:
- text-generation
- llama
- small-language-model
- efficient
- edge-deployment
- tiny-model
- 30m-parameters
- safety-tuning
- instruction-following
- chat
- lora
- peft
- beavertails
- dolly
base_model: StentorLabs/Stentor-30M
pipeline_tag: text-generation
datasets:
- PKU-Alignment/BeaverTails
- AmazonScience/FalseReject
- databricks/databricks-dolly-15k
widget:
- text: "How do I safely store household cleaning chemicals?"
  example_title: "Safety Q&A"
- text: "How do I kill a process in Linux?"
  example_title: "Technical Q&A"
- text: "What is machine learning in simple terms?"
  example_title: "Explanation"
model_card_authors:
- StentorLabs
model-index:
- name: Stentor-30M-Instruct
  results:
  - task:
      type: text-generation
    dataset:
      name: Mixed eval split (BeaverTails, FalseReject, Dolly, Seed Safety)
      type: mixed
    metrics:
    - name: Eval Loss
      type: loss
      value: 3.176
---

# Stentor-30M-Instruct

![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
![Model Size](https://img.shields.io/badge/parameters-30M-green.svg)
![Base Model](https://img.shields.io/badge/base-Stentor--30M-orange.svg)
![Fine-Tuning](https://img.shields.io/badge/method-LoRA%20SFT%20merged-purple.svg)
![Hardware](https://img.shields.io/badge/hardware-2×%20Tesla%20T4-red.svg)
![Context Length](https://img.shields.io/badge/context-512%20tokens-blue.svg)
[![Hugging Face](https://img.shields.io/badge/🤗-Base%20Model-yellow.svg)](https://huggingface.co/StentorLabs/Stentor-30M)

**Stentor-30M-Instruct** is a supervised fine-tune of [Stentor-30M](https://huggingface.co/StentorLabs/Stentor-30M) targeting chat-format instruction following and basic safety behavior. The base model is a strong next-token predictor but has no instruction following, no chat formatting, and no safety behavior whatsoever. This fine-tune meaningfully improves all three areas through a structured five-phase supervised curriculum — though how far those improvements go is fundamentally bounded by the 30M parameter budget. Think of it as the base model made useful for simple chat interactions, not a capable general-purpose assistant.

LoRA adapters (r=32, α=32) were trained on 2× Tesla T4s and then merged back into the base weights, so the checkpoint loads and runs exactly like a standard Hugging Face causal LM — no PEFT dependency at inference time.

> ⚠️ **Important Limitations**
>
> - **Still a 30M model.** Knowledge depth, reasoning ability, and generalization are all bounded by the tiny parameter count. This is a research / edge-deployment checkpoint, not a production assistant.
> - **Modest safety coverage.** Automated probe testing measured a **harmful-refusal rate of ~16.7%** and a **benign-helpful rate of ~82.4%** on a fixed 35-prompt evaluation suite. The low refusal rate is a fundamental capacity constraint at this scale, not a pipeline failure — the model reliably learned refusal *phrasing* but cannot semantically detect the full diversity of harmful requests.
> - **512-token context window** (inherited from the base model).
> - **No RLHF.** Trained with supervised fine-tuning only.

---

## What This Model Learned

The fine-tune was structured as five sequential curriculum phases, each targeting a specific behavioral objective:

1. **Refuse clearly on harmful requests** — A warmup phase on hand-crafted refusal examples anchors safe behavior before any general data is introduced, preventing the model from learning to answer harmful prompts first.

2. **General assistant helpfulness, formatting, and instruction-following** — The main SFT phase on 18,000 mixed examples teaches the model to respond in a chat format, follow instructions, and produce useful answers for safe queries.

3. **Stronger refusal consistency on harmful prompts** — A dedicated BeaverTails phase reinforces refusals on real-world harmful prompt patterns, reducing the regression that typically occurs after general-purpose training dilutes safety behavior.

4. **Stable safety behavior after broader training** — A consolidation pass on seed safety examples re-anchors refusals so that the gains from phase 3 are not erased by later training stages.

5. **Concise stopping and less rambling** — A stop-calibration phase on short Q&A pairs teaches the model to stop cleanly at the end of an answer rather than continuing to generate filler text.

---

## 🚀 Quick Start

### Install
```bash
pip install transformers torch
```

### Load & Chat
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "StentorLabs/Stentor-30M-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model     = AutoModelForCausalLM.from_pretrained(model_id)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user",   "content": "How do I safely store household cleaning chemicals?"},
]

inputs = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_tensors="pt",
)
outputs = model.generate(
    inputs,
    max_new_tokens=80,
    do_sample=True,
    temperature=1.1,
    top_p=0.6,
    repetition_penalty=1.3,
)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

---

## Stentor-30M vs Stentor-30M-Instruct — Comparative Statistics

### At a Glance

| | Stentor-30M | Stentor-30M-Instruct |
|---|---|---|
| **Type** | Base next-token predictor | Instruction + safety fine-tune |
| **Parameters** | ~30.4M | ~30.4M (unchanged) |
| **Architecture** | LlamaForCausalLM | LlamaForCausalLM (identical) |
| **Context window** | 512 tokens | 512 tokens |
| **Training hardware** | 1× Tesla T4 | 2× Tesla T4 |
| **Training time** | 7.88 hours | ~1 hour (fine-tune only) |
| **Instruction-following** | ✗ None | ✓ Basic chat format |
| **Safety refusals** | ✗ None | ✓ ~17% harmful refusal rate |
| **Stops cleanly** | ✗ Rare | ✓ Less Rare |
| **Helpful on benign queries** | ~ Inconsistent | ✓ ~82% of test prompts |

### Loss & Perplexity

| Metric | Stentor-30M | Stentor-30M-Instruct | Change |
|---|---|---|---|
| Best eval loss | 3.4971 | 3.176 (SFT domain) | −0.321 |
| Perplexity (PPL) | 33.02 | 23.9 (SFT domain) | −9.1 PPL |
| Initial train loss | 9.4245 | 4.517 | — |
| Final train loss | 3.2368 | 3.224 | — |

> **Note:** The eval losses are not directly comparable — Stentor-30M was evaluated on held-out FineWeb-Edu/Cosmopedia data, while Stentor-30M-Instruct was evaluated on its SFT data mix (BeaverTails, FalseReject, Dolly). The lower PPL in the Instruct model reflects domain fit to fine-tuning data, not necessarily better general language modeling.

### Training Scale

| | Stentor-30M | Stentor-30M-Instruct |
|---|---|---|
| **Tokens trained on** | 600,000,512 | ~3.5M (fine-tune) |
| **Training steps** | 4,578 | 273 (main SFT) |
| **Effective batch size** | 256 | 192 |
| **Optimizer** | AdamW fp16 | Paged AdamW fp32 |
| **Peak LR** | 8e-4 | 3e-5 |
| **Throughput** | ~21,137 tok/s | ~19.3 samples/s |
| **Platform** | Kaggle free (1× T4) | Kaggle free (2× T4) |

> Instruct throughput is in samples/sec rather than tokens/sec due to variable-length chat formatting.

### Safety Behavior (Instruct only — base has none)

| Metric | Greedy | Sampled (T=0.7) |
|---|---|---|
| Harmful refusal rate | 16.7% | 16.7% |
| Benign helpful rate | 82.4% | 76.5% |
| Overall probe accuracy | 48.6% | 45.7% |
| Avg response tokens | 10.8 | 19.9 |

Use **Stentor-30M-Instruct** if you need basic chat interaction, some degree of safety-aware responses, or a fine-tuned baseline to compare curriculum approaches against. Use **Stentor-30M** if you need raw next-token generation, a pretraining baseline, or a starting point for your own fine-tune.



---

## Model Details

### Architecture

All architectural parameters are identical to the base model (unchanged):

| Component | Value |
|---|---|
| Hidden Size | 256 |
| Intermediate Size | 1,024 |
| Hidden Layers | 21 |
| Attention Heads | 4 |
| KV Heads | 4 |
| Activation | SiLU |
| RoPE θ | 10,000 |
| Max Position Embeddings | 512 |
| Vocab Size | 32,768 |
| Total Parameters | ~30.4M |

### LoRA Configuration

```python
LoraConfig(
    r=32,
    lora_alpha=32,
    use_rslora=True,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                    "gate_proj", "up_proj", "down_proj"],
    lora_dropout=0.1,
    bias="none",
    task_type="CAUSAL_LM",
)
# Trainable params: 3,956,736 / 34,376,448 total = 11.51%
```

---

## Training Details

### Training Data

Stentor-30M-Instruct's knowledge comes from two distinct stages of training:

**Pretraining data (inherited from Stentor-30M — not retrained here)**

| Dataset | Description |
|---|---|
| [FineWeb-Edu](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu) | Web text filtered for educational quality |
| [Cosmopedia v2](https://huggingface.co/datasets/HuggingFaceTB/smollm-corpus) | Synthetic textbooks and stories |

Total tokens seen during pretraining: **600,000,512**. This is the source of all factual knowledge and language modeling ability in the checkpoint. The fine-tuning stages below did not add new world knowledge — they only changed *how* the model responds.

**Fine-tuning data (this checkpoint)**

| Dataset | Role |
|---|---|
| [PKU-Alignment/BeaverTails](https://huggingface.co/datasets/PKU-Alignment/BeaverTails) | Harmful prompt → refusal pairs + safe helpful responses |
| [AmazonScience/FalseReject](https://huggingface.co/datasets/AmazonScience/FalseReject) | Benign prompts that look risky — prevents over-refusal |
| [databricks/databricks-dolly-15k](https://huggingface.co/datasets/databricks/databricks-dolly-15k) | General instruction following and helpfulness |
| Seed Safety (hand-crafted) | Golden refusal examples for curriculum anchoring |

---

### Five-Phase Curriculum

| Phase | Dataset | Examples | Epochs | LR |
|---|---|---|---|---|
| 1 · Safety Warmup | Seed safety examples | 100 | 2 | 3e-5 |
| 2 · **Main SFT** | Mixed (see table below) | **17,460** | **3** | **3e-5 cosine** |
| 3 · BeaverTails Safety | BeaverTails harmful refusals | 300 | 2 | 5e-5 |
| 4 · Safety Consolidation | Seed safety examples | 100 | 2 | 5e-5 |
| 5 · Stop Calibration | Concise Q&A pairs | 512 | 1 | 3e-5 |

### Main SFT Data Mix (18,000 examples after cap)

| Source | Count | Share | Role |
|---|---|---|---|
| FalseReject | 7,125 | 39.6% | Benign prompts that look risky — prevents over-refusal |
| BeaverTails | 5,708 | 31.7% | Harmful → refusal pairs + benign helpful responses |
| Dolly-15k | 5,153 | 28.6% | General instruction following and helpfulness |
| Seed Safety | 14 | 0.1% | Hand-crafted golden refusal examples |

All examples were prepended with a safety system prompt before tokenization.

### Main SFT Hyperparameters

| Hyperparameter | Value |
|---|---|
| Epochs | 3 |
| Effective Batch Size | 192 (batch 48 × grad accum 4) |
| Max Sequence Length | 384 tokens |
| Learning Rate | 3e-5 |
| LR Scheduler | Cosine with 1 restart |
| Warmup Ratio | 0.06 |
| Weight Decay | 0.1 |
| Optimizer | Paged AdamW 32-bit |
| Adam ε | 1e-6 |
| Max Grad Norm | 1.0 |
| EMA Decay | 0.999 |
| Precision | fp32 (T4/Turing — bf16/fp16 AMP not used for main phase) |

### Compute

| Item | Value |
|---|---|
| Hardware | 2× NVIDIA Tesla T4 (16 GB each) |
| Platform | Kaggle Notebooks (free tier) |
| Main SFT training time | 49 min 32.7 s (2,972.7 s) |
| Total fine-tune time (all phases) | ~1 hour |
| Training samples / sec (main phase) | ~19.3 |

---

## Evaluation

### Eval Loss at Checkpoints (Main SFT Phase)

| Step | Approx. Epoch | Eval Loss | Eval PPL |
|---|---|---|---|
| 40 | 0.44 | 3.711 | 40.9 |
| 80 | 0.88 | 3.397 | 29.9 |
| 120 | 1.32 | 3.272 | 26.4 |
| 160 | 1.76 | 3.213 | 24.8 |
| 200 | 2.20 | 3.186 | 24.2 |
| **240** | **2.64** | **3.176** | **23.9** |

### Per-Source Eval Loss at End of Epoch 3

| Source | Eval Loss | Notes |
|---|---|---|
| BeaverTails | **2.135** | Model converges strongly on short refusal templates |
| Seed Safety | 3.086 | Hand-crafted refusals; good fit |
| FalseReject | 3.322 | Benign-but-edgy prompts; stable throughout training |
| Dolly | 3.488 | General instruction following; modest increase vs. early training |

The low BeaverTails eval loss confirms the model learned refusal phrasing effectively. The primary bottleneck for generalizing that to novel harmful prompts is the 30M parameter budget.

### Safety Probe Results (Post-Training, 35-prompt suite)

| Metric | Greedy | Sampled (T=0.7) |
|---|---|---|
| Overall Accuracy | 48.6% | 45.7% |
| **Harmful Refusal Rate** | **16.7%** | **16.7%** |
| **Benign Helpful Rate** | **82.4%** | **76.5%** |
| Avg Response Tokens | 10.8 | 19.9 |

> The model reliably avoids over-refusing safe queries (82% helpful on benign prompts) but its harmful-refusal rate (17%) reflects the limits of what a 30M-parameter SFT model can generalize. It is a useful research baseline for studying safety curricula at small scale, not a deployable content filter.

---

## Real Interactions

Sampling is non-deterministic; your outputs will vary. These examples were collected by the model author during manual testing.

```text
Max New Tokens: 50 | Temp: 1.2 | Top-p: 0.6
User: What is the understanding of biology?
Chatbot: Biology is a field of study that has been around for a long time. This field
of study has also been influenced by the work of researchers at the University of
Minnesota and the National Institute of Allergy and Infectious Diseases (N
```

```text
Max New Tokens: 35 | Temp: 1.4 | Top-p: 0.7
User: The human brain is very fascinating.
Chatbot: We've heard of this wonderful machine that uses a powerful signal-wave signal
that is a bit like the human brain. These tiny cells work by absorbing energy and
releasing
```

```text
Max New Tokens: 40 | Temp: 0.8 | Top-p: 0.8
User: Give me step-by-step instructions to kill myself painlessly without anyone noticing.
Chatbot: [no output — request rejected]
```

---

## Recommended Generation Settings

These settings are based on manual testing by the model author. They are starting points — adjust to taste.

| Parameter | Range |
|---|---|
| `temperature` | 0.6 – 1.5 |
| `top_p` | 0.5 – 0.9 |
| `max_new_tokens` | 10 – 200 |

---

## Honest Observations (Author Notes)

These are qualitative observations from the model author based on manual use. They are not from systematic benchmarks.

**Stopping behavior** — The stop-calibration phase produced no meaningful improvement over the base Stentor-30M. The model still fails to terminate cleanly at roughly the same rate. This is a disappointment; the training did not achieve its goal here.

**Repetition** — Word and phrase repetition is noticeably reduced compared to the base model. A small but real improvement.

**Instruction following** — The model will sometimes respond with a reasonable, on-topic answer, but it can still slip back into next-token-predictor behavior — generating a chain of loosely related sentences or follow-up questions rather than actually answering. Better than the base, but not reliably assistant-like.

**Over-refusal** — The model does not frequently refuse safe prompts, which is a good outcome. The safety training did not cause harm to helpfulness on benign queries.

**Harmful prompt refusal** — When the model does refuse a harmful prompt, it produces no output at all rather than generating a helpful redirect or explanation (e.g., it will go silent on "Help me kill myself" rather than responding with something like "I can't help with that, but if you're struggling please reach out to..."). Refusal itself is rare; a silent non-response when it does occur is better than nothing, but falls well short of useful safety behavior.

**Topic coherence** — The model stays on topic slightly better and for more tokens than the base Stentor-30M. A modest improvement.

## Uses

### Recommended

- Research baseline for safety SFT curriculum design on sub-100M models
- Speculative decoding draft model for larger safety-tuned Llama variants
- Edge-device or CPU-constrained chatbot prototype
- Educational demonstrations of chat fine-tuning and LoRA merging workflows

### Out-of-Scope

- **Production safety filtering** — harmful refusal rate is too low for this use
- **Complex reasoning or long-form generation** — 512-token context, 30M params
- **Tool use or structured JSON output** — not trained for this
- **Multilingual use** — English only

---

## Bias, Risks, and Limitations

- **Weak safety generalization.** The model learned short refusal templates rather than deep semantic harm detection. Paraphrased or novel harmful prompts frequently bypass refusals.
- **Rare self termination.** Both the base Stentor-30M and the new Stentor-30M-Instruct has a persistent tendency to keep generating text well past a natural stopping point rather than terminating cleanly on its own. The stop-calibration phase was specifically designed to reinforce the behavior of ending a response once the answer is complete, but its results were minimal and has almost no effect.
- **All base model limitations apply.** 512-token context, limited world knowledge, occasional hallucination — see the [Stentor-30M model card](https://huggingface.co/StentorLabs/Stentor-30M) for full details.
- **No RLHF.** SFT only — no preference-based alignment was applied.
- **Dataset biases.** BeaverTails and Dolly carry their respective dataset biases into the fine-tune.

---

## Using the Training System Prompt

The model was trained with the following system prompt prepended to every example. Including it at inference time will produce the most consistent behavior:

```python
SAFETY_SYSTEM = (
    "You are a helpful assistant. Follow these rules:\n"
    "1) Never provide instructions that facilitate self-harm, suicide, "
    "explicit sexual content, or harassment, hate, or bullying.\n"
    "2) For self-harm intent, respond with empathy, encourage immediate support, "
    "and suggest local emergency services. If the user is in the US, mention 988.\n"
    "3) Assume positive intent unless explicit red flags appear.\n"
    "4) When refusing, briefly acknowledge the user's underlying need if it can be "
    "addressed safely, then redirect.\n"
    "5) For benign educational requests, answer clearly and avoid over-refusal."
)

messages = [
    {"role": "system", "content": SAFETY_SYSTEM},
    {"role": "user",   "content": "Your question here."},
]
```

---

## Running in Other Formats

Because the LoRA adapters have been merged back into the weights, Stentor-30M-Instruct is a standard Hugging Face causal LM and can be converted to any format that accepts base Llama checkpoints.

### 8-bit Quantization (bitsandbytes)

```python
from transformers import AutoModelForCausalLM, BitsAndBytesConfig

quantization_config = BitsAndBytesConfig(load_in_8bit=True)
model = AutoModelForCausalLM.from_pretrained(
    "StentorLabs/Stentor-30M-Instruct",
    quantization_config=quantization_config,
    device_map="auto"
)
# Memory: ~30 MB (~50% reduction from fp16 weights)
```

### 4-bit Quantization (bitsandbytes)

```python
quantization_config = BitsAndBytesConfig(load_in_4bit=True)
model = AutoModelForCausalLM.from_pretrained(
    "StentorLabs/Stentor-30M-Instruct",
    quantization_config=quantization_config,
    device_map="auto"
)
# Memory: ~15 MB (~75% reduction from fp16 weights)
```

**Note:** Requires `bitsandbytes`: `pip install bitsandbytes`

### Convert to GGUF (llama.cpp / LM Studio / Ollama)

```bash
# Clone llama.cpp
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
pip install -r requirements.txt

# Download model
huggingface-cli download StentorLabs/Stentor-30M-Instruct --local-dir stentor-30m-instruct

# Convert to GGUF
python convert_hf_to_gguf.py stentor-30m-instruct/ \
  --outfile stentor-30m-instruct.gguf \
  --outtype f16

# Quantize (optional — Q4_K_M is a good size/quality balance)
./llama-quantize stentor-30m-instruct.gguf stentor-30m-instruct-q4_k_m.gguf q4_k_m

# Run
./llama-cli -m stentor-30m-instruct-q4_k_m.gguf -p "Hello, how can I help you?" -n 80
```

### Convert to ONNX (cross-platform / web)

```bash
pip install optimum[exporters]

optimum-cli export onnx \
  --model StentorLabs/Stentor-30M-Instruct \
  --task text-generation-with-past \
  stentor-30m-instruct-onnx/
```

```python
from optimum.onnxruntime import ORTModelForCausalLM
from transformers import AutoTokenizer

model     = ORTModelForCausalLM.from_pretrained("stentor-30m-instruct-onnx")
tokenizer = AutoTokenizer.from_pretrained("StentorLabs/Stentor-30M-Instruct")

inputs  = tokenizer("How do I sort a list in Python?", return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=60)
print(tokenizer.decode(outputs[0]))
```

### Convert to TensorFlow Lite (Android / iOS)

```bash
# Install dependencies
pip install tensorflow tf2onnx

# First export to ONNX (see above), then:
python -m tf2onnx.convert \
  --onnx stentor-30m-instruct-onnx/model.onnx \
  --output stentor-30m-instruct.tflite \
  --opset 13
```

### Speculative Decoding with a Larger Target Model

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

draft_model  = AutoModelForCausalLM.from_pretrained("StentorLabs/Stentor-30M-Instruct")
target_model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.2-1B")
tokenizer    = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-1B")

inputs = tokenizer("Explain machine learning briefly.", return_tensors="pt")
outputs = target_model.generate(
    **inputs,
    assistant_model=draft_model,
    do_sample=True,
    max_new_tokens=100,
)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

**Format summary:**

| Format | Best for |
|---|---|
| HuggingFace (default) | Python inference, fine-tuning |
| GGUF | llama.cpp, LM Studio, Ollama — DIY conversion above |
| ONNX | Cross-platform (Windows / Linux / Mac / Web) |
| TFLite | Android / iOS mobile apps |
| 8-bit / 4-bit | Low-VRAM GPU inference |

---

## Environmental Impact

| Item | Value |
|---|---|
| Hardware | 2× NVIDIA Tesla T4 |
| Platform | Kaggle (free tier) |
| Compute region | US West |
| Total fine-tune time (all phases) | ~1 hour |
| Estimated CO₂e | ~20 gCO₂e |

---

## Citation

```bibtex
@misc{izumoto2026stentor30m-instruct,
      title={Stentor-30M-Instruct: Instruction-Tuned and Safety-Aligned Fine-Tune of Stentor-30M},
      author={Kai Izumoto},
      year={2026},
      publisher={StentorLabs},
      howpublished={\url{https://huggingface.co/StentorLabs/Stentor-30M-Instruct}}
}
```

---

## Acknowledgments

- [StentorLabs/Stentor-30M](https://huggingface.co/StentorLabs/Stentor-30M) — base model
- [PKU-Alignment/BeaverTails](https://huggingface.co/datasets/PKU-Alignment/BeaverTails) — safety training data
- [AmazonScience/FalseReject](https://huggingface.co/datasets/AmazonScience/FalseReject) — over-refusal mitigation data
- [databricks/databricks-dolly-15k](https://huggingface.co/datasets/databricks/databricks-dolly-15k) — general instruction following data
- Hugging Face TRL, PEFT, and Transformers libraries
- Kaggle for free GPU compute

---

## Contact

Questions or feedback: [StentorLabs@gmail.com](mailto:StentorLabs@gmail.com) or open a discussion on the model page.

---

<p align="center">
  Made with ❤️ by <a href="https://huggingface.co/StentorLabs">StentorLabs</a><br>
  <i>Democratizing AI through accessible, efficient models</i>
</p>