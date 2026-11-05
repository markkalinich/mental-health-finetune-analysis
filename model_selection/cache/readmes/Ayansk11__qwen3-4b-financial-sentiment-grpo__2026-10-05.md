---
license: apache-2.0
base_model: Qwen/Qwen3-4B
tags:
- finance
- sentiment-analysis
- chain-of-thought
- grpo
- unsloth
- ollama
datasets:
- FinGPT/fingpt-sentiment-train
language:
- en
pipeline_tag: text-generation
---

# Qwen3-4B Financial Sentiment Analyzer with Chain-of-Thought

Fine-tuned Qwen3-4B model for financial sentiment analysis with explicit reasoning.

## Training Details

- **Base Model:** Qwen3-4B
- **Method:** SFT Warm-up + GRPO (Group Relative Policy Optimization)
- **Dataset:** 8,541 financial news samples with CoT explanations
- **Training Time:** ~4 hours on A100

## Usage

### With Ollama (Recommended for Mac M4)

```bash
# Download GGUF and Modelfile
huggingface-cli download Ayansk11/qwen3-4b-financial-sentiment-grpo --include "*.gguf" "Modelfile" --local-dir .

# Create Ollama model
ollama create financial-sentiment -f Modelfile

# Run inference
ollama run financial-sentiment "Analyze: Apple reported record Q4 earnings."
```

### With Transformers (Python)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("Ayansk11/qwen3-4b-financial-sentiment-grpo")
tokenizer = AutoTokenizer.from_pretrained("Ayansk11/qwen3-4b-financial-sentiment-grpo")

messages = [
    {"role": "system", "content": "You are a financial sentiment analyst..."},
    {"role": "user", "content": "Analyze: Tesla stock dropped 10%"}
]

inputs = tokenizer.apply_chat_template(messages, return_tensors="pt", add_generation_prompt=True)
outputs = model.generate(inputs, max_new_tokens=256)
print(tokenizer.decode(outputs[0]))
```

## Output Format

```
<reasoning>
1. Key financial indicators: [analysis]
2. Tone and language: [analysis]
3. Market implications: [analysis]
</reasoning>
<answer>positive/negative/neutral</answer>
```

## Performance

- **Mac M4 Inference:** 40-60 tokens/sec (Q5_K_M)
- **Memory Usage:** ~4 GB (quantized)
- **File Size:** ~2.89 GB (Q5_K_M GGUF)

## Files

- `*.gguf` - Quantized model for Ollama/llama.cpp
- `Modelfile` - Ollama configuration with proper stop tokens
- `*.safetensors` - Full PyTorch weights

## License

Apache 2.0
