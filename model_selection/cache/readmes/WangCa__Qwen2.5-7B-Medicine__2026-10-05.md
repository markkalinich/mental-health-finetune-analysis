---
license: mit
language:
- zh
metrics:
- bleu
pipeline_tag: question-answering
tags:
- medical
---
# Qwen2.5-7B-Instruct-Medical

## Model Description
Qwen2.5-7B-Instruct-Medical is a medical domain-specific model fine-tuned from the Qwen2.5-7B-Instruct model using 340,000 medical dialogue samples. This model is optimized to provide accurate and contextually relevant responses to medical-related inquiries, making it an excellent choice for healthcare applications such as medical chatbots, decision support systems, and educational tools.

## Model Details
- **Base Model**: Qwen2.5-7B-Instruct
- **Fine-tuning Dataset**: 340,000 medical dialogue samples
- **Training Duration**: 51 hours
- **Hardware Used**: 6x NVIDIA RTX 3090 (24GB VRAM)
- **Optimization Algorithm**: AdamW
- **Training Method**: LoRA (Low-Rank Adaptation)
- **Training Framework**: PyTorch

## Performance
- **BLEU-4 Score**:
  - Base Model: 23.5 (on a test set of 500 samples)
  - Fine-tuned Model: 55.7 (on the same test set)
  
This shows a significant improvement in the model's ability to generate more fluent and contextually relevant responses after fine-tuning on the medical dialogue dataset.

## Intended Use
This model is specifically tailored for medical dialogue tasks and can be used for:
- Medical question answering
- Healthcare chatbots
- Clinical decision support systems
- Medical education and training

## Performance
The model exhibits a strong understanding of medical terminology, clinical contexts, and patient interactions, making it a powerful tool for applications in healthcare and medical research.

## Usage

To use this model, you can load it using the `transformers` library in Python:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("path_to_model")
tokenizer = AutoTokenizer.from_pretrained("path_to_model")

input_text = "What are the symptoms of diabetes?"
inputs = tokenizer(input_text, return_tensors="pt")
output = model.generate(**inputs)
print(tokenizer.decode(output[0], skip_special_tokens=True))
<
```

## Limitations
While this model has been fine-tuned on a medical dialogue dataset, it may still make errors or provide inaccurate responses in highly specialized medical domains or cases where the input data falls outside the training data's coverage. Always ensure human supervision in critical healthcare scenarios.

## License

This model is released under the MIT License.

## Acknowledgements
- Dataset: 340,000 medical dialogues (From Modelscope).
- LoRA (Low-Rank Adaptation): This technique was used to efficiently fine-tune the model without modifying the full parameter set, allowing for faster and more memory-efficient training.