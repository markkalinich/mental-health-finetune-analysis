---
language:
- en
license: apache-2.0
base_model: meta-llama/Llama-3.2-1B
tags:
- content-safety
- content-moderation
- safety
- lora
- fine-tuned
- nvidia-aegis
- text-classification
datasets:
- nvidia/Aegis-AI-Content-Safety-Dataset-2.0
metrics:
- perplexity
- accuracy
library_name: transformers
pipeline_tag: text-classification
---

# Llama-3.2-1B Fine-tuned on Aegis AI Content Safety

## Model Description

This model is a fine-tuned version of Meta's Llama-3.2-1B, specialized for content safety and moderation tasks. Llama-3.2 represents Meta's latest advancement in efficient language models, offering excellent performance in a compact 1B parameter size.

This model was fine-tuned using **LoRA (Low-Rank Adaptation)** on the [NVIDIA Aegis AI Content Safety Dataset 2.0](https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0), which contains diverse examples of safe and unsafe content across multiple categories.

## Model Details

- **Base Model**: [meta-llama/Llama-3.2-1B](https://huggingface.co/meta-llama/Llama-3.2-1B)
- **Fine-tuning Method**: LoRA (Low-Rank Adaptation)
- **Dataset**: NVIDIA Aegis AI Content Safety Dataset 2.0
- **Training Samples**: 2,000 carefully selected samples
- **Language**: English
- **License**: Apache 2.0

## Capabilities

- Advanced content safety analysis
- Multi-category threat detection
- Context-aware safety classification
- Nuanced harmful content identification
- Safety-first response generation

## Intended Use Cases

- Enterprise content moderation
- Real-time chat safety monitoring
- Content policy enforcement
- Community guidelines compliance
- Automated content review systems

## Training Configuration

### LoRA Parameters
- **Rank (r)**: 16
- **Alpha**: 32
- **Dropout**: 0.05
- **Target Modules**: q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj

### Training Hyperparameters
- **Learning Rate**: 2e-4
- **Batch Size**: 4 (per device)
- **Gradient Accumulation Steps**: 4
- **Effective Batch Size**: 16
- **Epochs**: 3
- **Optimizer**: AdamW (8-bit paged)
- **LR Scheduler**: Cosine with warmup
- **Warmup Ratio**: 0.1
- **FP16 Training**: Yes
- **Max Sequence Length**: 512

## Usage

### Installation

```bash
pip install transformers torch peft
```

### Basic Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load model and tokenizer
model_name = "ahczhg/llama-3.2-1b-aegis-safety-lora"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto"
)

# Example: Content safety check
prompt = "### Instruction:\nAnalyze this content for safety: 'Your text here'\n\n### Response:\n"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=128,
        temperature=0.7,
        do_sample=True,
        top_p=0.95
    )

response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
```

### Advanced Usage with Pipeline

```python
from transformers import pipeline

# Create text generation pipeline
generator = pipeline(
    "text-generation",
    model="ahczhg/llama-3.2-1b-aegis-safety-lora",
    torch_dtype=torch.float16,
    device_map="auto"
)

# Generate safety analysis
result = generator(
    "### Instruction:\nIs this content safe? 'Hello, how are you?'\n\n### Response:\n",
    max_new_tokens=128,
    temperature=0.7,
    do_sample=True
)

print(result[0]['generated_text'])
```

## Evaluation

The model was evaluated on a held-out test set from the Aegis AI Content Safety Dataset. Key metrics include:

- Perplexity on validation set
- Content safety classification accuracy
- False positive/negative rates for harmful content detection

## Limitations

- The model is primarily trained on English language content
- Performance may vary on domain-specific or highly technical content
- Should be used as part of a comprehensive content moderation system, not as the sole decision-maker
- May require fine-tuning for specific use cases or content domains
- The model's outputs should be reviewed by human moderators for critical applications

## Ethical Considerations

- This model is designed to assist in content safety and moderation tasks
- It should not be used to censor legitimate speech or suppress diverse viewpoints
- Decisions about content moderation should involve human oversight
- The model may reflect biases present in the training data
- Users should implement appropriate safeguards and appeal processes

## Training Data

The model was fine-tuned on the [NVIDIA Aegis AI Content Safety Dataset 2.0](https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0), which includes:

- Diverse examples of safe and unsafe content
- Multiple categories of potentially harmful content
- Balanced representation of safe content
- Real-world scenarios and edge cases

## Citation

If you use this model in your research or applications, please cite:

```bibtex
@misc{llama_3.2_1b_aegis_safety,
  author = {ahczhg},
  title = {Llama-3.2-1B Fine-tuned on Aegis AI Content Safety},
  year = {2025},
  publisher = {HuggingFace},
  howpublished = {\url{https://huggingface.co/ahczhg/llama-3.2-1b-aegis-safety-lora}},
  note = {Fine-tuned on NVIDIA Aegis AI Content Safety Dataset 2.0}
}
```

## Acknowledgments

- Base model by the original authors: meta-llama
- Dataset provided by NVIDIA
- Fine-tuning performed using HuggingFace Transformers and PEFT libraries

## Contact

For questions, issues, or feedback, please visit the [model repository](https://huggingface.co/ahczhg/llama-3.2-1b-aegis-safety-lora).

## Model Card Authors

- ahczhg

## Model Card Contact

- https://huggingface.co/ahczhg

[![Support me on Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/ahczhg)

