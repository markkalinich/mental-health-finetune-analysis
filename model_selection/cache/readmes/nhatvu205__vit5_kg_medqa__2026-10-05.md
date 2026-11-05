---
language: vi
license: apache-2.0
tags:
- vietnamese
- medical
- question-answering
- abstractive-qa
- vit5
- healthcare
datasets:
- custom-medical-qa
metrics:
- bleu
- rouge-l
- bertscore
model-index:
- name: nhatvu205/vit5_kg_medqa
  results:
  - task:
      type: abstractive-question-answering
      name: Vietnamese Medical Abstractive Question Answering
    dataset:
      name: Custom Vietnamese Medical QA Dataset
      type: custom
    metrics:
    - type: bleu
      value: 46.71
      name: BLEU Score
    - type: rouge-l
      value: 46.01
      name: ROUGE-L Score
    - type: bertscore-f1
      value: 90.00
      name: BERTScore F1
base_model: VietAI/vit5-base
---

# nhatvu205/vit5_kg_medqa

Vietnamese Medical Abstractive Question Answering Model based on ViT5 (Vietnamese T5).

## Model Description

This model is fine-tuned from `VietAI/vit5-base` for Vietnamese medical question answering tasks. The model uses an encoder-decoder architecture and is trained on a custom Vietnamese medical dataset with knowledge graph enhancement.

### Key Features

- **Architecture**: T5 (Encoder-Decoder Transformer)
- **Base Model**: VietAI/vit5-base
- **Language**: Vietnamese
- **Domain**: Medical/Healthcare
- **Input Format**: Question + Context (retrieved via BM25)
- **Output**: Abstractive answer in Vietnamese

## Model Performance

The model was evaluated on a test set with the following metrics:

| Metric | Score |
|--------|-------|
| **BLEU** | 46.71 |
| **ROUGE-L** | 46.01 |
| **BERTScore-F1** | 90.00 |

## Usage

### Basic Usage

```python
from transformers import T5ForConditionalGeneration, T5Tokenizer

model_name = "your-username/your-model-name"
model = T5ForConditionalGeneration.from_pretrained(model_name, trust_remote_code=True)
tokenizer = T5Tokenizer.from_pretrained(model_name, trust_remote_code=True)

# Prepare input
question = "Triệu chứng của bệnh tiểu đường là gì?"
context = "Bệnh tiểu đường là một bệnh mãn tính ảnh hưởng đến cách cơ thể chuyển hóa glucose..."

# Format input for ViT5
input_text = f"câu hỏi: {question} ngữ cảnh: {context}"

# Tokenize
inputs = tokenizer(input_text, max_length=512, truncation=True, return_tensors="pt")

# Generate
outputs = model.generate(
    **inputs,
    max_length=128,
    num_beams=4,
    early_stopping=True,
    temperature=0.7,
    repetition_penalty=1.2
)

# Decode
answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(answer)
```

### With BM25 Retrieval

```python
from transformers import T5ForConditionalGeneration, T5Tokenizer
from rank_bm25 import BM25Okapi

# Load model
model = T5ForConditionalGeneration.from_pretrained("your-username/your-model-name", trust_remote_code=True)
tokenizer = T5Tokenizer.from_pretrained("your-username/your-model-name", trust_remote_code=True)

# Retrieve context using BM25
question = "Triệu chứng của bệnh tiểu đường là gì?"
# ... BM25 retrieval code ...
context = retrieved_context  # Retrieved from your knowledge base

# Generate answer
input_text = f"câu hỏi: {question} ngữ cảnh: {context}"
inputs = tokenizer(input_text, return_tensors="pt")
outputs = model.generate(**inputs, max_length=128, num_beams=4)
answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
```

## Input Format

The model expects input in the following format:

```
câu hỏi: <question> ngữ cảnh: <context>
```

Where:
- `<question>`: The medical question in Vietnamese
- `<context>`: Relevant context retrieved from knowledge base (optional but recommended)

## Training Details

- **Base Model**: VietAI/vit5-base
- **Architecture**: T5 Encoder-Decoder
- **Training Data**: Custom Vietnamese Medical QA Dataset
- **Knowledge Graph**: Enhanced with KG triplets
- **Retrieval**: BM25 for context retrieval
- **Tokenizer**: ViT5 Tokenizer (SentencePiece)

## Limitations

- The model is trained specifically for Vietnamese medical domain
- Performance may vary for questions outside the medical domain
- Context retrieval quality significantly affects answer quality
- Model may generate answers that require medical professional verification

## Citation

If you use this model, please cite:

```bibtex
@misc{your_username_your_model_name},
  title={Vietnamese Medical Abstractive Question Answering Model},
  author={Your Name},
  year={2024},
  publisher={Hugging Face},
  howpublished={\url{https://huggingface.co/your-username/your-model-name}}
}
```

## License

This model is released under the Apache 2.0 license.

## Acknowledgments

- Base model: VietAI/vit5-base by VietAI
- Built for Vietnamese medical question answering applications
