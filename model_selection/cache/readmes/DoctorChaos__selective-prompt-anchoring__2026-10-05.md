# Selective Prompt Anchoring (SPA)

Selective Prompt Anchoring (SPA) is a model-agnostic algorithm designed for large language models (LLMs) that provides fine-grained control over text generation.

This repository contains the implementation of SPA, a technique that allows you to selectively emphasize or de-emphasize specific tokens in a prompt to guide the LLM's generation process.

## Overview

In human communication, nuanced emphasis and fine-grained implications are often conveyed through variations in volume, tone, or pauses. Conveying such subtleties in text-based communication with AI is challenging with plain text prompts.

SPA enables users to assign importance, emphasis, or weights to specific parts of input text when prompting language models. It brings this capability to text-based AI communication by allowing users to "anchor" certain words or phrases in the prompt, causing the model to pay more attention to them during generation.

## How SPA Works

SPA creates two parallel processing paths:
1. The original prompt
2. A modified prompt with anchored tokens masked

During token generation, SPA compares logits from both paths and adjusts final probabilities based on the anchoring strength, causing the model to emphasize the anchored concepts while maintaining coherent generation.

## Usage Examples

### Installation

```bash
pip install huggingface_hub
pip install git+https://github.com/magic-YuanTian/Selective-Prompt-Anchoring.git
```

### Basic Usage

```python
from spa_hf import load_spa_model

# Load the SPA model
spa_model = load_spa_model(
    model_name=None,  # Skip loading from Hub
    base_model_name="Qwen/Qwen3-0.6B",  # Use your preferred base model
    device_map="auto"
)

# Example 1: Simple text prompting with global anchors
prompt = "How is the weather today?"
anchors = ["today"]

output = spa_model.generate_with_spa(
    prompt=prompt,
    anchors=anchors,
    anchoring_strength=3.0,  # Adjust strength to control anchor influence
    max_new_tokens=200
)

print(output)

# Example 2: Chat format with inline anchors
chat_prompt = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What's the weather <anchor>today</anchor>?"},
]

output = spa_model.generate_with_spa(
    prompt=chat_prompt,
    anchoring_strength=2.0,
    max_new_tokens=200
)

print(output)

# Example 3: Negative anchoring (avoidance)
prompt = "List some popular programming languages."
avoid_anchors = ["Python", "JavaScript"]

output = spa_model.generate_with_spa(
    prompt=prompt,
    anchors=avoid_anchors,
    anchoring_strength=-1.0,  # Negative strength for reversed influence
    max_new_tokens=200
)

print(output)
```

## Key Parameters

- `anchoring_strength` (default: 1.5): Controls the influence of anchored text.
  - `1.0`: No effect (normal generation)
  - `0.0`: Completely ignore anchored text
  - `>1.0`: Emphasize anchored text (higher values = stronger emphasis)
  - `<0.0`: Reverse the influence of the anchored text (negative values = stronger reversed influence)

- `modulated_by_prob` (default: True): When True, the anchoring strength is modulated by token probability.
  - Enable for more stable results, especially with higher anchoring strengths
  - Disable for more precise control at lower strengths

- `use_attention_mask` (default: True): When True, uses attention masking for anchor tokens, enhancing the effect of anchoring.

## Input Formats

SPA supports multiple input formats, allowing developers to conveniently represent anchors in prompts or messages:

1. String with Global Anchors:
```python
prompt = "How is the weather today?"
anchors = ['today']
```

2. String with Inline Anchors:
```python
prompt = "What's the weather <anchor>today</anchor>?"
```

3. Chat Messages with Message-Level Anchors:
```python
prompt = [
    {
        "role": "system", 
        "content": "You are a helpful assistant.", 
        "anchors": ["You", "assistant"]  
    },
    {
        "role": "user",
        "content": "What's the weather today?", 
        "anchors": ["today"]
    },
]
```

4. Chat Messages with Inline Anchors:
```python
prompt = [
    {
        "role": "system", 
        "content": "You are a helpful assistant."
    },
    {
        "role": "user", 
        "content": "What's the weather <anchor>today</anchor>?"
    },
]
```

## Citation

If you use SPA in your research, please cite:

```bibtex
@inproceedings{tian2025spa,
  title = {Selective Prompt Anchoring for Code Generation},
  author = {Tian, Yuan and Zhang, Tianyi},
  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},
  year = {2025},
  url = {https://arxiv.org/abs/2408.09121},
  eprint = {2408.09121},
  archivePrefix = {arXiv}
}
```

## License

This project is licensed under the Apache 2.0 License - see the LICENSE file for details.

## Links

- [GitHub Repository](https://github.com/magic-YuanTian/Selective-Prompt-Anchoring)
- [Paper](https://arxiv.org/abs/2408.09121)
- [PyPI Package](https://pypi.org/project/anchoring/) 