---
library_name: transformers
tags:
- medical-qa
- healthcare
- llama
- fine-tuned
license: llama3.2
datasets:
- ruslanmv/ai-medical-chatbot
---

# Model Card: Llama-3.2-3B-Chat-Doctor

## Model Details

### Model Description
Llama-3.2-3B-Chat-Doctor is a specialized medical question-answering model based on the Llama 3.2 3B architecture. This model has been fine-tuned specifically for providing accurate and helpful responses to medical-related queries.

- **Developed by:** Ellbendl Satria
- **Model type:** Language Model (Conversational AI)
- **Language:** English
- **Base Model:** Meta Llama-3.2-3B-Instruct
- **Model Size:** 3 Billion Parameters
- **Specialization:** Medical Question Answering
- **License:** llama3.2

### Model Capabilities
- Provides informative responses to medical questions
- Assists in understanding medical terminology and health-related concepts
- Offers preliminary medical information (not a substitute for professional medical advice)

### Direct Use
This model can be used for:
- Providing general medical information
- Explaining medical conditions and symptoms
- Offering basic health-related guidance
- Supporting medical education and patient communication

### Limitations and Important Disclaimers
⚠️ **CRITICAL WARNINGS:**
- **NOT A MEDICAL PROFESSIONAL:** This model is NOT a substitute for professional medical advice, diagnosis, or treatment.
- Always consult a qualified healthcare provider for medical concerns.
- The model's responses should be treated as informational only and not as medical recommendations.

### Out-of-Scope Use
The model SHOULD NOT be used for:
- Providing emergency medical advice
- Diagnosing specific medical conditions
- Replacing professional medical consultation
- Making critical healthcare decisions

## Bias, Risks, and Limitations

### Potential Biases
- May reflect biases present in the training data
- Responses might not account for individual patient variations
- Limited by the comprehensiveness of the training dataset

### Technical Limitations
- Accuracy is limited to the knowledge in the training data
- May not capture the most recent medical research or developments
- Cannot perform physical examinations or medical tests

### Recommendations
- Always verify medical information with professional healthcare providers
- Use the model as a supplementary information source
- Be aware of potential inaccuracies or incomplete information

## Training Details

### Training Data
- **Source Dataset:** [ruslanmv/ai-medical-chatbot](https://huggingface.co/datasets/ruslanmv/ai-medical-chatbot)
- **Base Model:** [Meta Llama-3.2-3B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct)

### Training Procedure
[Provide details about the fine-tuning process, if available]
- Fine-tuning approach
- Computational resources used
- Training duration
- Specific techniques applied during fine-tuning

## How to Use the Model

### Hugging Face Transformers
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "Ellbendls/llama-3.2-3b-chat-doctor"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Example usage
input_text = "I had a surgery which ended up with some failures. What can I do to fix it?"

# Prepare inputs with explicit padding and attention mask
inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)

# Generate response with more explicit parameters
outputs = model.generate(
    input_ids=inputs['input_ids'], 
    attention_mask=inputs['attention_mask'],
    max_new_tokens=150,  # Specify max new tokens to generate
    do_sample=True,      # Enable sampling for more diverse responses
    temperature=0.7,     # Control randomness of output
    top_p=0.9,           # Nucleus sampling to maintain quality
    num_return_sequences=1  # Number of generated sequences
)

# Decode the generated response
response = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(response)
```

### Ethical Considerations
This model is developed with the intent to provide helpful, accurate, and responsible medical information. Users are encouraged to:
- Use the model responsibly
- Understand its limitations
- Seek professional medical advice for serious health concerns