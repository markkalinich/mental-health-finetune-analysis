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
- speculative-decoding
- tiny-model
- 30m-parameters
- kaggle-trained
- educational
- research
- low-resource
- cpu-inference
- mobile-deployment
- synthetic-data
- fineweb
- cosmopedia
pipeline_tag: text-generation
datasets:
- HuggingFaceFW/fineweb-edu
- HuggingFaceTB/smollm-corpus
widget:
- text: "Once upon a time"
  example_title: "Story Generation"
- text: "Explain neural networks in simple terms."
  example_title: "Toy Explanation (Often Wrong)"
- text: "def fibonacci(n):"
  example_title: "Code Continuation"
- text: "[INST]What is machine learning?[/INST]"
  example_title: "Instruction-Style Prompt (Not Tuned)"
model_card_authors:
- StentorLabs
model-index:
- name: Stentor-30M
  results:
  - task:
      type: text-generation
    dataset:
      name: FineWeb-Edu + Cosmopedia v2 (validation split)
      type: mixed
    metrics:
    - name: Validation Loss
      type: loss
      value: 3.4971
    - name: Perplexity
      type: perplexity
      value: 33.02
---

# Stentor-30M

![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
![Model Size](https://img.shields.io/badge/parameters-30M-green.svg)
![Training Time](https://img.shields.io/badge/training-7.88h-orange.svg)
![Hardware](https://img.shields.io/badge/hardware-1x%20Tesla%20T4-red.svg)
![Context Length](https://img.shields.io/badge/context-512%20tokens-purple.svg)
[![Hugging Face](https://img.shields.io/badge/🤗-Hugging%20Face-yellow.svg)](https://huggingface.co/StentorLabs/Stentor-30M)
[![GGUF](https://img.shields.io/badge/GGUF-mradermacher-blue.svg)](https://huggingface.co/mradermacher/Stentor-30M-GGUF)

Stentor-30M is a highly compact, efficient language model built on the Llama architecture. Designed for speed and low-resource environments, this ~30.4M parameter checkpoint utilizes a mixed-precision training pipeline and is best treated as a **base next-token predictor** (not a chat assistant). It does not "understand" text in a human sense and is not trained to reliably follow instructions. While the tokenizer may include special tokens/templates that resemble instruction or tool formats, the model itself is **not instruction-tuned** and will often generate **plausible but off-topic** text. It serves as an accessible entry point for researching attention mechanisms and testing training pipelines on consumer hardware.

> ⚠️ **Important Limitations**
> 
> - **Context Window:** Maximum 512 tokens (very short)
> - **Not Instruction-Tuned:** May ignore prompts or respond off-topic
> - **Stopping / EOS:** Sometimes stops on its own, but it's rare; always set `max_new_tokens`
> - **Tokenizer ≠ Capability:** "tool/function" tokens do not imply real tool use
> - **No Safety Tuning:** Base model without RLHF or safety alignment
> - **Limited Knowledge:** 30M parameters = limited world knowledge
> - **Proof-of-Concept:** Not suitable for production without fine-tuning
> - **Educational Focus:** Trained on synthetic textbooks, not diverse real-world data

Recommended generation settings (based on manual testing):

- **Max new tokens:** 10-60
- **Temperature:** 1.1-1.4
- **Top-p:** 0.35-0.75

Real interactions (sampling is non-deterministic; your outputs may vary):

```text
Max New Tokens: 30
Temp: 1.2
Top p: 0.55
User:
The story of my life is
Generated text:
The story of my life is a tale of the story of the man who has been born in Germany. He was the first to learn about his family, and his story of the
```

```text
Max New Tokens: 30
Temp: 1.2
Top p: 0.7
User:
Biology is the understanding of
Generated text:
Biology is the understanding of nature and animals, not only as a model for biological research but also as a tool for understanding human behavior and conservation. Biological research is about understanding
```

```text
Max New Tokens: 30
Temp: 1.2
Top p: 0.7
User:
Everyone is dead
Text Generated:
Everyone is dead: 50 percent of our people will be killed in the coming days of our nation. 60 percent of us will live and go in
```

---

## 🚀 Quick Start

Get up and running in 3 simple steps:

### 1. Install
```bash
pip install transformers torch
```

### 2. Load & Generate
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("StentorLabs/Stentor-30M")
tokenizer = AutoTokenizer.from_pretrained("StentorLabs/Stentor-30M")

prompt = "The future of AI is"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(
    **inputs,
    max_new_tokens=50,  # always set this; the model may not stop on its own
    do_sample=True,
    temperature=1.1,
    top_p=0.55,
)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

### 3. Explore!
- Try different prompts
- Adjust `max_new_tokens`, `temperature`, and `top_p`

---

## 📦 Quantized Versions

Pre-quantized versions of Stentor-30M are available for use with llama.cpp, LM Studio, Ollama, and other compatible runtimes — no conversion needed.

| Format | Provider | Link |
|--------|----------|------|
| GGUF (multiple quants) | mradermacher | [mradermacher/Stentor-30M-GGUF](https://huggingface.co/mradermacher/Stentor-30M-GGUF) |

Just download your preferred quantization (e.g. `Q4_K_M` for a good size/quality balance) and run it directly with llama.cpp or load it in LM Studio.

---

## Model Details

### Model Description

Stentor-30M is a lightweight LlamaForCausalLM model designed to bring the architectural benefits of Llama to a fraction of the size. With a hidden size of 256 and a compact parameter budget, this model is optimized for rapid inference and edge-deployment scenarios where memory is at a premium.

The tokenizer configuration may include control tokens commonly used in instruction/tool-call formatting (for experimentation), but **these tokens do not make the base model instruction-following or tool-using**. If you need reliable instruction following or structured tool calls, you will need additional fine-tuning / alignment.

- **Developed by:** Kai Izumoto (StentorLabs)
- **Funded by:** Self-funded
- **Shared by:** StentorLabs
- **Model type:** LlamaForCausalLM (Auto-regressive Language Model)
- **Language(s):** English
- **License:** Apache-2.0
- **Finetuned from model:** None (Base model trained from scratch)

## Uses

### Direct Use

- **Low-Latency Text Generation:** Due to its compact size (approx. 30.4M parameters), Stentor-30M is suitable for real-time applications on CPU or mobile devices.
- **Instruction-Style Prompting (Limited):** You can *format* prompts using tags like `[INST]`, but the model is **not** instruction-tuned and will often fail to follow the request.
- **Tool-Call Formatting Tokens (Limited):** The tokenizer may include tool-related tokens, but the model is **not** trained to reliably emit valid tool calls/JSON or to "use tools".
- **Edge Deployment:** Ideal for resource-constrained environments including mobile devices, IoT, and embedded systems.

### Downstream Use

- **Speculative Decoding (Experimental):** Stentor-30M can be used as a fast draft model for larger Llama-based models, but speedups depend on how often the larger model accepts the draft tokens (quality limits may reduce gains).
- **Educational/Research:** A perfect "petri dish" model for studying attention mechanics (4 attention heads) and training dynamics without requiring massive compute.
- **Prototyping:** Quick, low-cost experiments focused on latency, sampling behavior, and failure modes before scaling up.

### Out-of-Scope Use

- **Complex Reasoning:** As a 30M parameter model, users should not expect high-level reasoning or deep knowledge retrieval comparable to multi-billion parameter models.
- **Instruction-Following Chatbots:** This is a base model and is not reliably conversational or on-task.
- **Long Context:** The model is optimized for short-context tasks with a maximum position embedding of 512 tokens.
- **Production-Critical Applications:** This is a research/proof-of-concept model and should not be used for mission-critical applications without thorough testing.

## Bias, Risks, and Limitations

- **Context Window:** The model has a hard limit of 512 tokens for context length.
- **Prompt Relevance:** Outputs are often generic or unrelated to the prompt, even when they sound fluent.
- **Knowledge Base:** Limited parameter count restricts the amount of world knowledge the model can store.
- **Training Data Bias:** The model inherits any biases present in the FineWeb-Edu and Cosmopedia v2 datasets.
- **Hallucinations:** Like all language models, Stentor-30M may generate plausible-sounding but factually incorrect information.
- **No Safety Tuning:** This is a base model without safety alignment or RLHF.

### Recommendations

Users (both direct and downstream) should be made aware of the risks, biases, and limitations of the model. This model is best used for specific, narrow tasks or as a component in a larger system (e.g., speculative decoding) rather than a general-purpose assistant.

## How to Get Started with the Model

### Basic Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "StentorLabs/Stentor-30M"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

# The repo may provide a chat template, but this is still a base model.
# Do not expect reliable instruction following just because you use chat formatting.
messages = [
    {"role": "user", "content": "Hello, what are you?"}
]

inputs = tokenizer.apply_chat_template(
    messages, 
    return_tensors="pt", 
    add_generation_prompt=True
)
outputs = model.generate(inputs, max_new_tokens=50)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

### Advanced Usage with Tool-Call Formatting (Educational)

```python
# The tokenizer may include tokens that resemble tool/function calling formats.
# The base model is not trained to reliably emit valid tool calls or structured JSON.
messages = [
    {"role": "system", "content": "You are a tiny base language model. You do not have tool access."},
    {"role": "user", "content": "What's the weather like?"}
]

inputs = tokenizer.apply_chat_template(messages, return_tensors="pt")
outputs = model.generate(inputs, max_new_tokens=100)
```

## Detailed Use Cases

### 1. Speculative Decoding with Llama 3

Potentially speed up larger model inference by using Stentor-30M as a draft model (results vary):

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load draft model (Stentor-30M)
draft_model = AutoModelForCausalLM.from_pretrained("StentorLabs/Stentor-30M")
draft_tokenizer = AutoTokenizer.from_pretrained("StentorLabs/Stentor-30M")

# Load target model
target_model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.2-1B")
target_tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-1B")

# Use speculative decoding (requires a recent Transformers version that supports `assistant_model`)
prompt = "Explain machine learning"
inputs = target_tokenizer(prompt, return_tensors="pt")

outputs = target_model.generate(
    **inputs,
    assistant_model=draft_model,  # Stentor-30M as draft
    do_sample=True,
    max_new_tokens=100
)

print(target_tokenizer.decode(outputs[0], skip_special_tokens=True))
```

### 2. Run with llama.cpp / LM Studio / Ollama (GGUF)

Pre-quantized GGUF files are available at [mradermacher/Stentor-30M-GGUF](https://huggingface.co/mradermacher/Stentor-30M-GGUF) — no conversion required.

```bash
# Download a quantized GGUF (e.g. Q4_K_M) from the link above, then run with llama.cpp:
./llama-cli -m stentor-30m-Q4_K_M.gguf -p "Hello world" -n 50
```

Or simply load the `.gguf` file directly in **LM Studio** or **Ollama** for a GUI/API experience.

### 3. Edge Deployment with ONNX

Convert to ONNX for mobile/edge deployment:

```bash
# Install dependencies
pip install optimum[exporters]

# Export to ONNX
optimum-cli export onnx \
  --model StentorLabs/Stentor-30M \
  --task text-generation-with-past \
  stentor-30m-onnx/
```

```python
# Use with ONNX Runtime
from optimum.onnxruntime import ORTModelForCausalLM
from transformers import AutoTokenizer

model = ORTModelForCausalLM.from_pretrained("stentor-30m-onnx")
tokenizer = AutoTokenizer.from_pretrained("StentorLabs/Stentor-30M")

inputs = tokenizer("Hello world", return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=20)
print(tokenizer.decode(outputs[0]))
```

### 4. Rapid Prototyping

Quick experimentation before scaling:

```python
# These "tasks" are intentionally broad: this tiny base model will often fail.
# The point is to observe latency, failure modes, and sampling behavior.
from transformers import pipeline

generator = pipeline("text-generation", model="StentorLabs/Stentor-30M")

test_prompts = [
    "Summarize this: [long text]",
    "Translate to French: Hello",
    "Answer: What is 2+2?"
]

for prompt in test_prompts:
    result = generator(prompt, max_new_tokens=30)[0]['generated_text']
    print(f"Prompt: {prompt}\nResult: {result}\n")
```

## Quantize It Yourself

If you want to produce your own quantized versions rather than using the pre-built GGUFs:

### 8-bit Quantization (bitsandbytes)

```python
from transformers import AutoModelForCausalLM, BitsAndBytesConfig

quantization_config = BitsAndBytesConfig(load_in_8bit=True)
model = AutoModelForCausalLM.from_pretrained(
    "StentorLabs/Stentor-30M",
    quantization_config=quantization_config,
    device_map="auto"
)
# Memory: ~30 MB (~50% reduction from fp16 weights)
```

### 4-bit Quantization (bitsandbytes)

```python
quantization_config = BitsAndBytesConfig(load_in_4bit=True)
model = AutoModelForCausalLM.from_pretrained(
    "StentorLabs/Stentor-30M",
    quantization_config=quantization_config,
    device_map="auto"
)
# Memory: ~15 MB (~75% reduction from fp16 weights)
```

**Note:** Requires `bitsandbytes` library: `pip install bitsandbytes`

### Convert to GGUF Manually

```bash
# Clone llama.cpp
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp

# Install dependencies
pip install -r requirements.txt

# Download model
huggingface-cli download StentorLabs/Stentor-30M --local-dir stentor-30m

# Convert to GGUF
python convert_hf_to_gguf.py stentor-30m/ \
  --outfile stentor-30m.gguf \
  --outtype f16

# Quantize (optional)
./llama-quantize stentor-30m.gguf stentor-30m-q4_0.gguf q4_0
```

### Convert to TensorFlow Lite (Mobile)

```bash
# Install dependencies
pip install tensorflow tf2onnx

# First convert to ONNX (see above)
# Then convert ONNX to TFLite
python -m tf2onnx.convert \
  --onnx stentor-30m-onnx/model.onnx \
  --output stentor-30m.tflite \
  --opset 13
```

**Format summary:**
- **GGUF:** C++ applications, llama.cpp, LM Studio, Ollama — [pre-built available](https://huggingface.co/mradermacher/Stentor-30M-GGUF)
- **ONNX:** Cross-platform (Windows/Linux/Mac/Web)
- **TFLite:** Android/iOS mobile apps

---

## Training Details

### Training Data

The model was trained on a high-quality mixed dataset focused on educational content and synthetic textbook data:

- **FineWeb-Edu** ([HuggingFaceFW/fineweb-edu](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu)): A dataset filtered for educational quality.
- **Cosmopedia v2** ([HuggingFaceTB/smollm-corpus](https://huggingface.co/datasets/HuggingFaceTB/smollm-corpus)): A corpus of synthetic textbooks and stories.

**Total tokens processed:** 600,000,512 tokens

### Training Procedure

The model was trained using a custom script in a Kaggle Jupyter environment, demonstrating the accessibility of training efficient models on free-tier compute.

#### Preprocessing

The training pipeline utilized lightweight but effective preprocessing steps:

- **Cleaning:** Unicode normalization (NFKC) and whitespace stripping/normalization.
- **Formatting:** Optional wrapping for chat formats or `<think>` tokens.
- **Packing:** Sequence packing into fixed block_size chunks to maximize training efficiency.
- **Tokenization:** Standard Llama tokenization with EOS tokens appended.

#### Training Hyperparameters

<details>
<summary><b>Click to view full training configuration</b></summary>

| Hyperparameter | Value |
|----------------|-------|
| Precision | fp16 mixed precision |
| Optimizer | AdamW |
| Scheduler | Cosine |
| Learning Rate | 0.0008 |
| Weight Decay | 0.01 |
| Warmup Ratio | 0.02 |
| Stable Ratio | 0.8 |
| Total Batch Size | 256 |
| Max Train Steps | 4,578 |
| Evaluation Steps | 100 |
| Gradient Accumulation | 64 |

</details>

#### Speeds, Sizes, Times

- **Training Time:** 28,367.5 seconds (~7.88 hours)
- **Hardware:** 1x Tesla T4 (`num_processes: 1`)
- **Vocab Size:** 32,768 (padded to multiple of 128)
- **Sequence Length:** 512 tokens
- **Tokens per Second (avg):** ~21,137 TPS
- **Total Parameters:** 30,419,712
- **Embedding Parameters:** 8,388,608 (27.6% of total)

> **Note:** A significant portion of parameters are allocated to embeddings due to the 32K vocabulary size. For future iterations, a smaller vocabulary (8K-16K) could free up capacity for additional model layers.

---

## Evaluation

### Testing Data, Factors & Metrics

#### Testing Data

Evaluation was performed on a held-out validation split of the mixed FineWeb-Edu and Cosmopedia dataset.

#### Metrics

- **Validation Loss:** Measures how well the model predicts the next token (lower is better).
- **Perplexity (PPL):** The exponential of the loss, indicating how "surprised" the model is by new text (lower is better).

### Results

![Training Loss Curve](training_loss.png)
![Training Perplexity Curve](training_perplexity.png)

| Metric | Value |
|--------|-------|
| **Validation Loss** | 3.4971 (best @ step 4500) |
| **Perplexity** | 33.02 |

#### Training Progress

The model showed steady improvement throughout training:
- Initial train loss (step 25): 9.4245
- Mid-training train loss (step 2300): 3.7579
- Final train loss (step 4575): 3.2368
- Best eval loss: 3.4971 (step 4500)
- Final eval loss / PPL: 3.4975 / 33.03

> **Note:** As a 30M parameter base model, this checkpoint should be treated as a functional proof-of-concept baseline. The model does not run external benchmarks like MMLU or GSM8K.

---

## Technical Specifications

### Model Architecture and Objective

<details>
<summary><b>Click to view full architecture specifications</b></summary>

Stentor-30M utilizes the Llama architecture with the following specific configuration:

| Component | Value |
|-----------|-------|
| Hidden Size | 256 |
| Intermediate Size | 1024 |
| Num Hidden Layers | 21 |
| Attention Heads | 4 |
| Key/Value Heads | 4 |
| Hidden Activation | SiLU |
| RoPE Theta | 10000.0 |
| Max Position Embeddings | 512 |
| Vocab Size | 32,768 |
| Tie Word Embeddings | True |

> **Architecture Note:** This configuration is set to 21 layers to keep total parameters in the 30M-31M target range with a 32,768-token vocabulary.

</details>

### Compute Infrastructure

The model was trained using standard cloud infrastructure available to researchers and students.

#### Hardware

- **GPUs:** 1x NVIDIA Tesla T4 (16GB)
- **Platform:** Kaggle Notebooks (free tier)
- **Compute Type:** Cloud-based

#### Software

- **Transformers Version:** 5.2.0
- **PyTorch Version:** Latest stable
- **Torch Compile:** False (disabled for notebook stability)
- **Accelerate:** Enabled for training

---

## Environmental Impact

- **Hardware Type:** 1x NVIDIA Tesla T4
- **Hours used:** ~7.88 hours
- **Cloud Provider:** Kaggle
- **Compute Region:** US West
- **Carbon Emitted:** ~160 gCO2e (estimated)

Training on free-tier cloud GPUs demonstrates the accessibility of small language model research to students and independent researchers.

---

## Related Resources

### Official Resources
- 📊 Best model artifact: `results/best_model` (config + tokenizer + weights + metadata)
- 🎓 [Model Card Methodology](https://arxiv.org/abs/1810.03993) - Mitchell et al., 2018

### Quantized Versions
- 🗜️ [mradermacher/Stentor-30M-GGUF](https://huggingface.co/mradermacher/Stentor-30M-GGUF) - GGUF quantizations for llama.cpp, LM Studio, Ollama

### Related Models
- [TinyLlama-1.1B](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0) - Larger alternative (1.1B params)
- [SmolLM-135M](https://huggingface.co/HuggingFaceTB/SmolLM-135M) - Similar size category
- [Llama-3.2-1B](https://huggingface.co/meta-llama/Llama-3.2-1B) - Target model for speculative decoding

### Research Papers
- [Speculative Decoding](https://arxiv.org/abs/2211.17192) - Leviathan et al., 2023
- [Small Language Models Survey](https://arxiv.org/abs/2402.14848) - Survey on efficient LLMs

---

## Citation

```bibtex
@misc{izumoto2026stentor30m,
      title={Stentor-30M: A Compact Llama-based Language Model}, 
      author={Kai Izumoto},
      year={2026},
      publisher={StentorLabs},
      howpublished={\url{https://huggingface.co/StentorLabs/Stentor-30M}}
}
```

---

## Glossary

- **NLP (Natural Language Processing):** The field of AI focused on the interaction between computers and human language.
- **PPL (Perplexity):** A measurement of how well a probability model predicts a sample. Lower is generally better.
- **Speculative Decoding:** A technique where a small "draft" model (like Stentor-30M) quickly generates tokens that are then verified by a larger model, speeding up the overall process.
- **SLM (Small Language Model):** Language models with parameters typically under 1B, designed for efficiency and specific tasks.
- **RoPE (Rotary Position Embedding):** A method for encoding position information in transformer models.
- **Edge Deployment:** Running models on resource-constrained devices like mobile phones or IoT devices.
- **GGUF:** A file format used by llama.cpp and compatible runtimes for efficient local inference.

---

## Model Card Contact

For questions, please contact [StentorLabs@gmail.com](mailto:StentorLabs@gmail.com) or open an issue on the [model repository](https://huggingface.co/StentorLabs/Stentor-30M/discussions).

---

## Acknowledgments

Special thanks to:
- Hugging Face for the transformers library and dataset hosting
- The creators of FineWeb-Edu and Cosmopedia v2 datasets
- Kaggle for providing free GPU compute resources
- [mradermacher](https://huggingface.co/mradermacher) for providing GGUF quantizations
- The open-source community for making accessible AI research possible

---

## Connect & Community

### Stay Updated
- 📧 [Email](mailto:StentorLabs@gmail.com) - Direct contact
- 💬 [HuggingFace Discussions](https://huggingface.co/StentorLabs/Stentor-30M/discussions) - Questions and community chat

### More from StentorLabs
- 🔬 [All Models](https://huggingface.co/StentorLabs) - Browse our model collection

---

<p align="center">
  Made with ❤️ by <a href="https://huggingface.co/StentorLabs">StentorLabs</a>
  <br>
  <i>Democratizing AI through accessible, efficient models</i>
</p>