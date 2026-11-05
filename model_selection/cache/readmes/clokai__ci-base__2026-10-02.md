---
language:
  - en
tags:
  - clokai
  - ci
  - persona
  - reasoning
  - conversational
  - emotion
  - tools
  - text-generation
  - Ci-base
  - ci-instruct-base
model_type: ci
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
---

![ClokAI](https://media.licdn.com/dms/image/v2/D4D3DAQENbD2QWb9lWQ/image-scale_191_1128/B4DZ8vzupUI8AY-/0/1783213517643/clokai_cover?e=1784617200&v=beta&t=t5gn4icq1BaAmc-_UUzTCD7nu0kzRkDLe80sTHGXFTw)

## ci-base

ci is a persona-based conversational AI model developed by [ClokAI](https://huggingface.co/clokai). This is the **base** version of the ci model family.

ci is designed to maintain consistent personality across conversations while understanding emotional context and performing multi-step reasoning. The model combines advanced language modeling with specialized modules for emotion recognition, persona consistency, tool usage, and reasoning capabilities.

---

## Table of Contents

- [Model Details](#model-details)
  - [Model Description](#model-description)
  - [Model Sources](#model-sources)
- [Intended Use](#intended-use)
  - [Direct Use](#direct-use)
  - [Out-of-Scope Use](#out-of-scope-use)
- [Bias, Risks, and Limitations](#bias-risks-and-limitations)
- [Training Details](#training-details)
  - [Training Data](#training-data)
  - [Training Procedure](#training-procedure)
- [Technical Specifications](#technical-specifications)
  - [Model Architecture](#model-architecture)
  - [Model Parameters](#model-parameters)
  - [Computational Requirements](#computational-requirements)
- [How to Get Started with the Model](#how-to-get-started-with-the-model)
- [Citation](#citation)
- [Contact](#contact)

---

## Model Details

### Model Description

- **Developed by:** [ClokAI](https://huggingface.co/clokai)
- **Model type:** Persona-based Conversational AI
- **Language(s) (NLP):** English
- **License:** Apache 2.0
- **Finetuned from model:** Custom architecture (not finetuned from existing model)

ci is a language model with built-in capabilities for:
- **Emotion Recognition**: Understanding 12 different emotional states
- **Persona Consistency**: Maintaining stable personality traits
- **Tool Usage**: Identifying when external tools are needed
- **Multi-step Reasoning**: Processing complex queries through reasoning steps

### Model Sources

- **Repository:** [ClokAI/ci-base](https://huggingface.co/clokai/ci-base)
- **Paper:** Not available
- **Demo:** Not available
- **Library:** [clokai](https://pypi.org/project/clokai/)

---

## Intended Use

### Direct Use

ci is intended for conversational AI applications that require:
- Consistent persona behavior across interactions
- Emotional intelligence in responses
- Multi-step reasoning capabilities
- Tool-augmented conversations

**Example use cases:**
- Chatbots and virtual assistants
- Character-based games and simulations
- Customer support with emotional awareness
- Educational tutoring systems
- Creative writing assistance

### Out-of-Scope Use

ci should NOT be used for:
- **Medical diagnosis or advice** - The model is not a medical professional
- **Legal advice** - The model cannot provide legal counsel
- **Financial decisions** - The model should not be used for financial planning
- **Harmful content generation** - The model should not generate harmful, deceptive, or illegal content
- **Autonomous decision-making** - The model should not make critical decisions without human oversight
- **Surveillance or monitoring** - The model should not be used for invasive monitoring

---

## Bias, Risks, and Limitations

### Known Limitations

1. **Context Length**: Limited to 512 tokens. Longer conversations may require truncation.

2. **Language**: Currently optimized for English only. Multilingual support is planned.

3. **Knowledge Cutoff**: The model's knowledge is limited to its training data.

4. **Hallucination**: Like all language models, ci may generate plausible-sounding but incorrect information.

5. **Persona Drift**: Very long conversations may see gradual personality changes.

6. **Tool Integration**: Tool usage capabilities require additional framework integration.

### Bias Considerations

- The model may reflect biases present in its training data
- Emotional responses may not be appropriate for all cultural contexts
- Persona consistency may vary across different conversation topics

### Ethical Considerations

- Human oversight is recommended for sensitive applications
- The model's emotional responses should not be taken as professional advice
- Users should be informed they are interacting with an AI system

---

## Training Details

### Training Data

The model was trained on a curated dataset of conversational data with persona annotations and emotional labels. The dataset includes:
- Multi-turn conversations
- Persona descriptions and consistent responses
- Emotional context annotations
- Tool usage examples
- Reasoning chains

**Dataset size:** Up to 500,000 samples

### Training Procedure

| Parameter | Value |
|---|---|
| Training Steps | 74,000 / 100,000 |
| Effective Batch Size | 32 |
| Learning Rate | 3e-4 |
| Weight Decay | 0.01 |
| Warmup Steps | 1,000 |
| Label Smoothing | 0.05 |
| Max Gradient Norm | 1.0 |
| Precision | FP16 |

**Training Progress:**
- Current step: 74,000
- Target steps: 100,000
- Completion: 74%

---

## Technical Specifications

### Model Architecture

| Component | Value |
|---|---|
| Hidden Size | 1024 |
| Number of Layers | 16 |
| Attention Heads | 16 |
| KV Heads | 8 |
| Intermediate Size | 2816 |
| Max Position Embeddings | 512 |
| Vocabulary Size | 32,000 |

### Model Parameters

| Component | Parameters |
|---|---|
| Base Transformer | ~335M |
| Emotion Module | ~3M |
| Persona Module | ~6M |
| Tool Module | ~1M |
| Reasoning Module | ~5M |
| **Total** | **~350M** |

### Computational Requirements

| Requirement | Value |
|---|---|
| FP16 Memory | ~700 MB |
| FP32 Memory | ~1.4 GB |
| Recommended GPU | 4GB+ VRAM |
| Inference Speed | ~50 tokens/sec (GPU) |

---

## How to Get Started with the Model

### Installation

Install the required packages:

```bash
# Required packages
pip install torch>=2.0.0
pip install transformers>=4.35.0
pip install safetensors>=0.4.0

# Install ClokAI library (recommended)
pip install clokai
```

### Basic Usage with ClokAI Library

```python
from clokai import AutoClokAI

# Load model and tokenizer
model = AutoClokAI.from_pretrained("ClokAI/ci-base")
tokenizer = AutoClokAI.load_tokenizer("ClokAI/ci-base")

# Simple generation
prompt = "Hello! How are you today?"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_length=150)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

### Advanced Usage with ClokAI Library

```python
from clokai import AutoClokAI

# Load model
model = AutoClokAI.from_pretrained("ClokAI/ci-base")
tokenizer = AutoClokAI.load_tokenizer("ClokAI/ci-base")

# Generate with control parameters
prompt = "Tell me about yourself"
inputs = tokenizer(prompt, return_tensors="pt")

outputs = model.generate(
    **inputs,
    max_new_tokens=100,
    temperature=0.7,
    top_k=50,
    top_p=0.9,
    repetition_penalty=1.1
)

response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
```

### Memory-Efficient Loading

```python
from clokai import AutoClokAI
import torch

# Load in FP16 to save memory
model = AutoClokAI.from_pretrained(
    "ClokAI/ci-base",
    torch_dtype=torch.float16,
    device_map="auto"
)
tokenizer = AutoClokAI.load_tokenizer("ClokAI/ci-base")
```

### Alternative: Using Transformers Directly

If you prefer to use transformers directly:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("ClokAI/ci-base")
tokenizer = AutoTokenizer.from_pretrained("ClokAI/ci-base")

inputs = tokenizer("Hello!", return_tensors="pt")
outputs = model.generate(**inputs, max_length=100)
print(tokenizer.decode(outputs[0]))
```

---

## Citation

```bibtex
@misc{clokai2024ci,
  title={ci: A Persona-based Conversational AI Model},
  author={ClokAI Team},
  year={2024},
  publisher={HuggingFace},
  journal={HuggingFace Hub},
  howpublished={\url{https://huggingface.co/clokai/ci-base}}
}
```

---

## Contact

- **Organization:** [ClokAI](https://huggingface.co/clokai)
- **Repository:** [https://huggingface.co/clokai/ci-base](https://huggingface.co/clokai/ci-base)
- **Issues:** Please open an issue on the model repository

---

<p align="center">
  Built with ❤️ by <a href="https://huggingface.co/clokai">ClokAI</a>
</p>
