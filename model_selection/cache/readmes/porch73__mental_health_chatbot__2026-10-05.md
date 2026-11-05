---
license: apache-2.0
base_model:
- meta-llama/Llama-3.2-1B
pipeline_tag: question-answering
---
# CPU Compatible Mental Health Chatbot Model

This repository contains a fine-tuned LLaMA-based model designed for mental health counseling conversations. The model provides meaningful and empathetic responses to mental health-related queries. It is compatible with CPUs and systems with low RAM, making it accessible for a wide range of users.

---

## Features

- **Fine-tuned on Mental Health Counseling Conversations**: The model is trained using a dataset specifically curated for mental health support.
- **Low Resource Requirements**: Fully executable on systems with 15 GB RAM and CPU, no GPU required.
- **Pretrained on Meta's LLaMA 3.2 1B Model**: Builds on the strengths of the LLaMA architecture for high-quality responses.
- **Supports LoRA (Low-Rank Adaptation)**: Enables efficient fine-tuning with low computational overhead.

---

## Model Details

- **Base Model**: [meta-llama/Llama-3.2-1B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct)
- **Dataset**: [Amod/Mental Health Counseling Conversations](https://huggingface.co/datasets/Amod/mental_health_counseling_conversations)
- **Fine-Tuning Framework**: Hugging Face Transformers

---

## Installation

1. Clone the repository:
    ```bash
    git clone https://huggingface.co/<your_hf_username>/mental-health-chatbot-model
    cd mental-health-chatbot-model
    ```

2. Install the required packages:
    ```bash
    pip install torch transformers datasets huggingface-hub
    ```

---

## Usage

### Load the Model

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load model and tokenizer
model_name = "<your_hf_username>/mental-health-chatbot-model"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Generate a response
input_text = "I feel anxious and don't know what to do."
inputs = tokenizer(input_text, return_tensors="pt")
response = model.generate(**inputs, max_length=256, pad_token_id=tokenizer.eos_token_id)
print(tokenizer.decode(response[0], skip_special_tokens=True))
```

### Compatibility

This model can be run on:
- CPU-only systems
- Machines with as little as 15 GB RAM

---

## Fine-Tuning Instructions

To further fine-tune the model on your dataset:

1. Prepare your dataset in Hugging Face Dataset format.
2. Use the following script:

```python
from transformers import Trainer, TrainingArguments

training_args = TrainingArguments(
    output_dir="./fine_tuned_model",
    per_device_train_batch_size=4,
    num_train_epochs=3,
    evaluation_strategy="epoch",
    save_steps=500,
    logging_dir="./logs",
    learning_rate=5e-5,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=validation_dataset,
)

trainer.train()
```

---

## Model Performance

- **Training Epochs**: 3
- **Batch Size**: 4
- **Learning Rate**: 5e-5
- **Evaluation Strategy**: Epoch-wise

---

## License

This project is licensed under the [Apache 2.0 License](LICENSE).

---

## Acknowledgments

- [Meta](https://huggingface.co/meta-llama) for the LLaMA model
- [Hugging Face](https://huggingface.co/) for their open-source tools and datasets
- The creators of the Mental Health Counseling Conversations dataset