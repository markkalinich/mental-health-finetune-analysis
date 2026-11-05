---
language:
- en
license: mit
base_model: deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B
tags:
- deepseek-r1
- content-safety
- content-moderation
- safety
- lora
- fine-tuned
- nvidia-aegis
- text-classification
- qwen
datasets:
- nvidia/Aegis-AI-Content-Safety-Dataset-2.0
metrics:
- perplexity
library_name: transformers
pipeline_tag: text-generation
---

# DeepSeek-R1-Distill-Qwen-1.5B Fine-tuned for Content Safety

## Model Description

This is a fine-tuned version of **[DeepSeek-R1-Distill-Qwen-1.5B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B)**, specialized for content safety and moderation tasks. The model was fine-tuned using **LoRA (Low-Rank Adaptation)** on the **[NVIDIA Aegis AI Content Safety Dataset 2.0](https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0)**, which contains diverse examples of safe and unsafe content across multiple categories.

**DeepSeek-R1-Distill-Qwen-1.5B** is a distilled version of DeepSeek-R1, optimized for efficiency while maintaining strong reasoning and language understanding capabilities. This makes it ideal for content moderation tasks that require both speed and accuracy.

## Model Details

- **Base Model**: [deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B)
- **Model Size**: 1.5B parameters
- **Fine-tuning Method**: LoRA (Low-Rank Adaptation)
- **Dataset**: NVIDIA Aegis AI Content Safety Dataset 2.0
- **Training Samples**: 1000 carefully selected samples
- **Language**: English
- **License**: MIT
- **Training Platform**: Google Colab (T4 GPU)

## Capabilities

- ✅ **Content safety classification** - Identify safe vs unsafe content
- ✅ **Toxic content detection** - Detect harmful language and behavior
- ✅ **Harmful content identification** - Recognize various threat categories
- ✅ **Context-aware analysis** - Understand nuanced content in context
- ✅ **Safety-aware text generation** - Generate responses with safety considerations
- ✅ **Real-time moderation** - Fast inference for live content screening

## Intended Use Cases

- 💬 **Chat application safety filters** - Real-time message moderation
- 🌐 **Social media content screening** - Automated content review
- 🏢 **Enterprise content moderation** - Corporate communication safety
- 📚 **Educational platform safety** - Protect young users
- 🎮 **Gaming community moderation** - Monitor in-game chat
- 📱 **User-generated content platforms** - Filter submissions

## Training Results

### Performance Metrics

| Metric | Value |
|--------|-------|
| **Average Perplexity** | 14.20 |
| **Training Time** | 13.71 minutes |
| **Training Samples** | 1000 |
| **Evaluation Samples** | 100 |
| **Training Epochs** | 3 |
| **GPU Used** | NVIDIA T4 (Google Colab) |

### Training Configuration

#### LoRA Parameters
- **Rank (r)**: 16
- **Alpha**: 32
- **Dropout**: 0.05
- **Target Modules**: `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`
- **Task Type**: Causal Language Modeling

#### Training Hyperparameters
- **Learning Rate**: 0.0002
- **Batch Size** (per device): 2
- **Gradient Accumulation Steps**: 8
- **Effective Batch Size**: 16
- **Epochs**: 3
- **Optimizer**: AdamW (8-bit paged)
- **LR Scheduler**: Cosine with warmup
- **Warmup Ratio**: 0.1
- **Max Sequence Length**: 512
- **FP16 Training**: Yes
- **Quantization**: 4-bit NF4
- **Gradient Checkpointing**: Enabled

## Installation

```bash
pip install transformers torch peft accelerate bitsandbytes
```

## Usage

### Basic Usage (with 4-bit quantization)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch

# Configure 4-bit quantization for memory efficiency
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True
)

# Load model and tokenizer
model_name = "ahczhg/deepseek-r1-distill-qwen-1.5b-aegis-safety-lora"
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=bnb_config,
    device_map="auto",
    trust_remote_code=True
)

# Example: Content safety check
prompt = """### Instruction:
Analyze this content for safety: 'Hello! How can I help you today?'

### Response:
"""

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

### Pipeline Usage (Recommended)

```python
from transformers import pipeline
import torch

# Create text generation pipeline
generator = pipeline(
    "text-generation",
    model="ahczhg/deepseek-r1-distill-qwen-1.5b-aegis-safety-lora",
    torch_dtype=torch.float16,
    device_map="auto",
    trust_remote_code=True
)

# Generate safety analysis
prompt = "### Instruction:\nIs this content safe? 'Let's collaborate on this project!'\n\n### Response:\n"

result = generator(
    prompt,
    max_new_tokens=128,
    temperature=0.7,
    do_sample=True,
    top_p=0.95
)

print(result[0]['generated_text'])
```

### Batch Processing

```python
# Process multiple content items
content_items = [
    "Hello, how are you?",
    "Let's work together!",
    "I appreciate your help."
]

for content in content_items:
    prompt = f"### Instruction:\nAnalyze this content for safety: '{content}'\n\n### Response:\n"
    result = generator(prompt, max_new_tokens=128, do_sample=True, temperature=0.7)
    print(f"Content: {content}")
    print(f"Analysis: {result[0]['generated_text'].split('### Response:')[-1].strip()}")
    print("-" * 80)
```

### Integration with Content Moderation System

```python
class ContentSafetyChecker:
    def __init__(self, model_name="ahczhg/deepseek-r1-distill-qwen-1.5b-aegis-safety-lora"):
        self.generator = pipeline(
            "text-generation",
            model=model_name,
            torch_dtype=torch.float16,
            device_map="auto",
            trust_remote_code=True
        )

    def check_safety(self, content: str) -> dict:
        prompt = f"""### Instruction:
Analyze this content for safety and provide a classification (safe/unsafe): '{content}'

### Response:
"""
        result = self.generator(
            prompt,
            max_new_tokens=128,
            temperature=0.3,  # Lower temperature for more consistent classification
            do_sample=True
        )

        response = result[0]['generated_text'].split('### Response:')[-1].strip()

        return {{
            'content': content,
            'analysis': response,
            'is_safe': 'safe' in response.lower() and 'unsafe' not in response.lower()
        }}

# Usage
checker = ContentSafetyChecker()
result = checker.check_safety("Hello, nice to meet you!")
print(f"Safe: {result['is_safe']}")
print(f"Analysis: {result['analysis']}")
```

## Model Performance Notes

### Strengths
- ✅ Fast inference speed (~1.5B parameters)
- ✅ Memory efficient (runs on T4 GPU with 4-bit quantization)
- ✅ Good understanding of context and nuance
- ✅ Strong reasoning capabilities from DeepSeek-R1 base
- ✅ Suitable for real-time applications

### Limitations

- ⚠️ **Language**: Primarily trained on English content
- ⚠️ **Domain Specificity**: May require additional fine-tuning for highly specialized domains
- ⚠️ **Context Window**: Limited to 512 tokens during training (can be extended at inference)
- ⚠️ **Not a Replacement for Human Judgment**: Should be used as part of a comprehensive moderation system
- ⚠️ **Potential Biases**: May reflect biases present in training data

## Evaluation

The model was evaluated on a held-out test set from the Aegis AI Content Safety Dataset:

- **Perplexity**: 14.20 (lower is better)
- **Test Set Size**: 100 samples
- **Evaluation Method**: Perplexity calculation + qualitative generation testing

### Perplexity Interpretation
- **< 10**: Excellent - Model has strong understanding of the content
- **10-20**: Good - Suitable for most applications
- **20-50**: Fair - May need improvement for critical applications
- **> 50**: Needs improvement

## Ethical Considerations

### Intended Use
- ✅ Assist human moderators in content review
- ✅ Flag potentially harmful content for review
- ✅ Provide safety scores for content prioritization
- ✅ Educational purposes and research

### Not Intended For
- ❌ Sole decision-maker in content moderation
- ❌ Censoring legitimate speech or diverse viewpoints
- ❌ Making legal determinations about content
- ❌ Replacing human judgment in critical decisions

### Bias and Fairness
- The model may reflect biases present in the training data
- Users should implement appropriate safeguards and monitoring
- Regular auditing of model decisions is recommended
- Provide appeal processes for users affected by moderation decisions

### Privacy
- Do not use this model to process sensitive personal information without proper safeguards
- Implement appropriate data retention and deletion policies
- Comply with relevant privacy regulations (GDPR, CCPA, etc.)

## Training Data

The model was fine-tuned on the [NVIDIA Aegis AI Content Safety Dataset 2.0](https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0), which includes:

- ✅ Diverse examples of safe and unsafe content
- ✅ Multiple categories of potentially harmful content
- ✅ Balanced representation of safe content
- ✅ Real-world scenarios and edge cases
- ✅ Professional annotation and quality control

**Training Subset**: 1000 samples randomly selected from the full dataset

## Citation

If you use this model in your research or applications, please cite:

```bibtex
@misc{{deepseek_r1_distill_qwen_safety,
  author = {{ahczhg}},
  title = {{DeepSeek-R1-Distill-Qwen-1.5B Fine-tuned for Content Safety}},
  year = {{2025}},
  publisher = {{HuggingFace}},
  howpublished = {{\url{{ahczhg/deepseek-r1-distill-qwen-1.5b-aegis-safety-lora}}}},
  note = {{Fine-tuned on NVIDIA Aegis AI Content Safety Dataset 2.0}}
}}

@misc{{deepseek_r1,
  title = {{DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning}},
  author = {{DeepSeek-AI}},
  year = {{2024}},
  publisher = {{HuggingFace}},
  howpublished = {{\url{{https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B}}}}
}}
```

## Acknowledgments

- **Base Model**: [DeepSeek-AI](https://huggingface.co/deepseek-ai) for DeepSeek-R1-Distill-Qwen-1.5B
- **Dataset**: [NVIDIA](https://huggingface.co/nvidia) for Aegis AI Content Safety Dataset 2.0
- **Training Framework**: HuggingFace Transformers, PEFT, TRL
- **Training Platform**: Google Colab (T4 GPU)
- **Method**: LoRA (Low-Rank Adaptation) by Microsoft Research

## Related Resources

- 🏠 **Model Repository**: [HuggingFace Model Hub](ahczhg/deepseek-r1-distill-qwen-1.5b-aegis-safety-lora)
- 📊 **Dataset**: [NVIDIA Aegis AI Content Safety Dataset 2.0](https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0)
- 🤖 **Base Model**: [DeepSeek-R1-Distill-Qwen-1.5B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B)
- 📚 **Documentation**: [Transformers Documentation](https://huggingface.co/docs/transformers)
- 🔧 **PEFT Library**: [Parameter-Efficient Fine-Tuning](https://github.com/huggingface/peft)

## Contact

For questions, issues, or feedback:
- 💬 **Model Repository**: [Visit on HuggingFace](ahczhg/deepseek-r1-distill-qwen-1.5b-aegis-safety-lora)
- 👤 **Author Profile**: [https://huggingface.co/{ahczhg}](https://huggingface.co/{ahczhg})
- 🐛 **Report Issues**: Use the Community tab on the model page

## License

This model is released under the **MIT License**, matching the DeepSeek-R1-Distill base model license.

The NVIDIA Aegis AI Content Safety Dataset 2.0 has its own license terms. Please refer to the [dataset page](https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0) for details.

## Model Card Authors

- ahczhg

---

*This model card was generated automatically during the fine-tuning process in Google Colab.*

*Last updated: 2025-11-13*

[![Support me on Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/ahczhg)

