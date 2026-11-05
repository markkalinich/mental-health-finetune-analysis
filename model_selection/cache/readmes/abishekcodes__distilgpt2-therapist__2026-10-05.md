
# Model Card for distilgpt2-therapist

This is a fine-tuned GPT-2 model (`distilgpt2`) designed for generating therapist-like responses based on a custom therapy dataset. It can be used to simulate therapeutic dialogues or other text generation tasks in the context of mental health.

## Model Details

### Model Description

This model is fine-tuned on the **TherapyDataset**, which contains various therapeutic conversations. The model is intended for text generation tasks related to therapist-style conversations.

- **Model type:** Causal Language Model
- **Language(s) (NLP):** English
- **Finetuned from model:** `distilbert/distilgpt2`

### Model Sources

- **Repository:** [abishekcodes/distilgpt2-therapist](https://huggingface.co/abishekcodes/distilgpt2-therapist)

## Uses

### Direct Use

This model can be used directly for generating therapist-like responses in a conversational setting or as part of a chatbot system.

### Downstream Use

The model can be further fine-tuned for specific therapeutic tasks or integrated into mental health applications that provide guidance and support.

### Out-of-Scope Use

This model is not intended to replace actual professional therapy. It should not be used for clinical diagnosis or as a substitute for mental health treatment.

## Bias, Risks, and Limitations

The model is trained on a specific dataset and may exhibit biases inherent in the dataset. It is not suitable for handling severe mental health issues and should be used with caution.

### Recommendations

Users should exercise caution while using this model in sensitive contexts. It is not a replacement for professional care, and biases in generated responses should be considered.

## How to Get Started with the Model

To use the model, install the Hugging Face `transformers` library and load the model with the code below:

```python
from transformers import AutoTokenizer, GPT2LMHeadModel

tokenizer = AutoTokenizer.from_pretrained("abishekcodes/distilgpt2-therapist")
model = GPT2LMHeadModel.from_pretrained("abishekcodes/distilgpt2-therapist")

inputs = tokenizer("How are you feeling today?", return_tensors="pt")
outputs = model.generate(inputs['input_ids'], max_length=50)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

# Training Details

## Training Data

The model was fine-tuned using the **TherapyDataset**, which is publicly available and contains various therapeutic conversations.

## Training Procedure

- **Training regime:** `fp16` mixed precision  
- **Batch size:** 6 per device (train and eval)  
- **Learning rate:** 2e-5  
- **Number of epochs:** 3  

## Training Hyperparameters

- **Training Loss:** 2.006800 → 1.826100  
- **Validation Loss:** 1.891285 → 1.802560  

# Evaluation

## Testing Data, Factors & Metrics

The model was evaluated using the test split from the **TherapyDataset**. The evaluation was based on standard text generation metrics.

## Metrics

- **Loss during training and validation** was used as the primary metric for evaluation.
