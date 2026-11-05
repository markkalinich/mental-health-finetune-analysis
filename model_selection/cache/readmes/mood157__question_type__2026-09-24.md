---
base_model:
- google/flan-t5-large
---
# T5-Large Fine-Tuned for Question Type Classification

This repository contains a fine-tuned version of the `t5-large` model designed to classify question types based on a given question and a prompt. The model has been trained to understand various question formats and categorize them accordingly.

## Model Details

- **Base Model:** [T5-Large](https://huggingface.co/t5-large)
- **Fine-Tuned Task:** Question Type Classification
- **Framework:** Hugging Face Transformers
- **Dataset:** Custom dataset with labeled question types
- **Training:** Fine-tuned using PyTorch/TensorFlow with appropriate loss function

## Usage

You can use this model with the `transformers` library from Hugging Face. Here’s how you can load and use it:

### Install dependencies

```bash
pip install transformers torch
```

### Load the model

```python
from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("mood157/question_type")
model = T5ForConditionalGeneration.from_pretrained("mood157/question_type")
```

### Example Inference

```python
def classify_question(question):
    input_text = f"{question}"
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    outputs = model.generate(input_ids)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

question = "What is the capital of France?"
print(classify_question(question))  # Output: "factual"
```

## Training Details

The model was fine-tuned using:

- **Optimizer:** AdamW
- **Learning Rate:** 5e-5
- **Batch Size:** 16
- **Epochs:** 3-5 (depending on dataset size)
- **Evaluation Metric:** Accuracy & F1-score


## Applications

This model can be used for:

- Automatic question classification in QA systems
- Educational platforms to categorize student queries
- Pre-processing for AI-driven customer support bots


## Contact

For questions or contributions, feel free to reach out via [GitHub Issues](https://github.com/mouad157) or Hugging Face discussions.

---

**Happy Question Classifying!** 🚀
