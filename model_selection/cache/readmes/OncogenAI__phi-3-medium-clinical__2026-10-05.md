---
license: apache-2.0
language:
- zh
- en
base_model:
- microsoft/Phi-3-medium-4k-instruct
pipeline_tag: text-generation
tags:
- medical
---
# Phi-3-Medium-Clinical

A medical domain-specific fine-tuned variant of Microsoft's Phi-3-Medium language model, optimized for clinical applications and healthcare-related tasks.

## Model Details

### Base Model
- **Model Name**: microsoft/Phi-3-medium-4k-instruct
- **Parameter Count**: 14B parameters
- **Architecture**: Transformer-based language model
- **Training Data**: Pre-trained on diverse web-scale data with strong reasoning and instruction-following capabilities

### Fine-tuning Information
- **Fine-tuning Framework**: [Unsloth](https://github.com/unslothai/unsloth) - High-efficiency fine-tuning toolkit
- **Medical Dataset**: Clinical and healthcare-specific dataset
- **Optimization Method**: LoRA (Low-Rank Adaptation) via Unsloth
- **Training Date**: March 2026

## Model Description

This model adapts Phi-3-medium-4k-instruct for clinical and healthcare applications by fine-tuning on curated medical datasets. The specialization enables better performance on:

- Clinical note analysis and generation
- Medical question answering
- Healthcare terminology understanding
- Patient information processing (de-identified)
- Medical literature comprehension

## Intended Use

### Primary Use Cases
- Clinical decision support and information retrieval
- Medical text analysis and classification
- Healthcare documentation assistance
- Medical knowledge base queries
- Educational purposes in healthcare settings

### Limitations
- Designed for informational and educational purposes only
- Should not be used as a standalone clinical decision-making tool
- Requires human medical professional validation
- Performance may vary on specialized subspecialties
- De-identified datasets only - respects patient privacy regulations

## Training Details

### Framework & Libraries
```
- Base: microsoft/Phi-3-medium-4k-instruct
- Fine-tuning: Unsloth
- LoRA Implementation: Efficient parameter-efficient fine-tuning
- Hardware: GPU-based training
```

### Dataset Characteristics
- **Domain**: Medical and clinical
- **Focus**: Healthcare-specific terminology and concepts
- **Processing**: Data preprocessing and tokenization following Phi-3 specifications
- **Format**: Instruction-following format for improved generalization

### Training Parameters
- **Max Sequence Length**: Phi-3-medium-4k-instruct standard (typically 4096 tokens)
- **Optimization**: LoRA with rank adaptation for parameter efficiency
- **Batch Size**: Standard configuration for medical dataset fine-tuning
- **Evaluation**: Domain-specific metrics for medical accuracy

## Usage

### Installation

```bash
# Install required dependencies
pip install transformers torch unsloth

# Optional: Install medical evaluation tools
pip install -r requirements.txt
```

### Basic Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load model and tokenizer
model_name = "OncogenAI/phi-3-medium-clinical"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    torch_dtype=torch.float16,
)

# Prepare input
prompt = "Clinical Query: Explain the pathophysiology of type 2 diabetes."
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

# Generate response
outputs = model.generate(
    **inputs,
    max_length=512,
    temperature=0.7,
    top_p=0.95,
    do_sample=True,
)

response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
```

### Advanced Usage with Unsloth

```python
from unsloth import FastLanguageModel
from transformers import TextIteratorStreamer
from threading import Thread

# Fast loading with Unsloth
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="OncogenAI/phi-3-medium-clinical",
    max_seq_length=4096,
    dtype=torch.float16,
    load_in_4bit=True,
)

# Streaming inference for long responses
streamer = TextIteratorStreamer(tokenizer, skip_special_tokens=True)
generation_kwargs = dict(
    inputs=inputs,
    streamer=streamer,
    max_length=512,
    temperature=0.7,
)

thread = Thread(target=model.generate, kwargs=generation_kwargs)
thread.start()

for text in streamer:
    print(text, end="", flush=True)
```

## Model Architecture

- **Attention Mechanism**: Multi-head self-attention
- **Positional Encoding**: Rotary positional embeddings (RoPE)
- **Normalization**: RMSNorm
- **Activation**: SiLU (Swish)
- **Fine-tuning Method**: LoRA adapters via Unsloth

## Performance Characteristics

- **Inference Speed**: Optimized via Unsloth for reduced latency
- **Memory Footprint**: Efficient through LoRA parameter reduction
- **Medical Domain Accuracy**: Enhanced through domain-specific fine-tuning
- **Token Context**: Maintains Phi-3-Medium's context window

## Hardware Requirements

### Recommended Specifications
- **GPU Memory**: 8GB+ (supports quantized inference)
- **CPU RAM**: 16GB+ (for tokenization and preprocessing)
- **Storage**: 15GB+ (model weights and tokenizer)

### Inference Modes
- **Full Precision**: 14B parameters (~28GB VRAM)
- **FP16 (Half Precision)**: ~14GB VRAM
- **INT8 Quantization**: ~8GB VRAM
- **INT4 Quantization**: ~4GB VRAM

## Ethical Considerations

### Responsible Use
- This model should complement, not replace, professional medical judgment
- Always have qualified healthcare professionals review outputs
- Be transparent about AI usage in clinical contexts
- Maintain patient confidentiality and data security
- Comply with healthcare regulations (HIPAA, GDPR, etc.)

### Bias and Fairness
- Fine-tuning dataset undergoes bias assessment
- Model outputs may reflect biases in training data
- Users should evaluate context-specific performance
- Continuous monitoring recommended for production use

## License

[Specify your license - e.g., Apache 2.0, MIT, or custom license]

## Citation

If you use this model in research, please cite:

```bibtex
@software{phi3_clinical_2026,
  author = {OncogenAI},
  title = {Phi-3-Medium-Clinical: A Medical Domain-Specific Fine-Tuned Model},
  year = {2026},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/OncogenAI/phi-3-medium-clinical}}
}
```

Also cite the base model and Unsloth:

```bibtex
@article{abdin2024phi,
  title={Phi-3 Technical Report},
  author={Abdin, Marah and others},
  journal={arXiv preprint arXiv:2404.14219},
  year={2024}
}

@software{unsloth2024,
  title={Unsloth: Efficient Fine-tuning of Language Models},
  author={Peng, Daniel Han and others},
  year={2024},
  url={https://github.com/unslothai/unsloth}
}
```

## Limitations and Disclaimers

1. **Medical Accuracy**: While fine-tuned on medical datasets, this model is not a substitute for professional medical advice
2. **Knowledge Cutoff**: Performance limited to training data scope
3. **Specialized Domains**: May have limited performance on rare conditions or cutting-edge treatments
4. **Privacy**: Ensure input data is properly de-identified before use
5. **Regulatory Compliance**: Users are responsible for compliance with applicable healthcare regulations

## Contact & Support

For questions about this model:
- Open an issue on the Hugging Face model page
- Reference specific queries or behaviors for reproducibility
- Provide context about your use case

## Acknowledgments

- Microsoft for the Phi-3-Medium base model
- Unsloth team for the efficient fine-tuning framework
- Medical dataset contributors and curators
- Healthcare and AI safety researchers