
# Qwen3-DPO-PII-Anonymizer

A Direct Preference Optimization (DPO) fine-tuned Qwen3-0.6B model specifically designed for PII (Personally Identifiable Information) anonymization tasks.

## Model Details

- **Base Model**: Qwen3-0.6B
- **Training Method**: Direct Preference Optimization (DPO)
- **Optimization**: Unsloth optimizations for faster training
- **Task**: PII Anonymization with tool calling capabilities
- **Context Length**: 4096 tokens
- **Model Size**: ~1.1GB

## Training Data

Trained on preference pairs for PII anonymization tasks, where the model learns to:
- Identify personally identifiable information in text
- Replace PII with semantically equivalent alternatives
- Preserve context while maintaining anonymity
- Use structured tool calls for replacements

## Usage

The model is designed to work with the `replace_entities` tool for PII anonymization:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("eternis/qwen3-dpo-pii-anonymizer", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained("eternis/qwen3-dpo-pii-anonymizer", trust_remote_code=True)

# Example prompt for PII anonymization
prompt = "Replace PII in: John Smith works at ABC Corp and lives at 123 Main St, New York."
```

## Tool Schema

The model uses the following tool schema for PII replacement:

```json
{
  "type": "function",
  "function": {
    "name": "replace_entities",
    "description": "Replace personally identifiable information (PII) with anonymized alternatives",
    "parameters": {
      "type": "object",
      "properties": {
        "replacements": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "original": {"type": "string", "description": "Original PII text"},
              "replacement": {"type": "string", "description": "Anonymized replacement"}
            },
            "required": ["original", "replacement"]
          },
          "description": "List of PII replacements to make"
        }
      },
      "required": ["replacements"]
    }
  }
}
```

## Training Configuration

- **Learning Rate**: 5e-6
- **Batch Size**: 2 (with gradient accumulation of 8)
- **Epochs**: 3
- **LoRA Rank**: 16
- **LoRA Alpha**: 32
- **Max Length**: 2048 tokens
- **Max Response**: 512 tokens

## License

[Add your license information here]

## Citation

If you use this model in your research, please cite:

```bibtex
@misc{qwen3-dpo-pii-anonymizer,
  author = {Your Name},
  title = {Qwen3-DPO-PII-Anonymizer},
  year = {2024},
  publisher = {Hugging Face},
  url = {https://huggingface.co/eternis/qwen3-dpo-pii-anonymizer}
}
```
