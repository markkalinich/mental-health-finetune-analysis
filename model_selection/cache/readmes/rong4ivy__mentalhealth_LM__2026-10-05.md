---
license: apache-2.0
---
This large language model is primarily designed to assess the severity of **mental health** issues by analyzing text or speech inputs from users(speakers, writers, patients, etc.). The training dataset consists of diagnoses made by psychiatrists based on the text or speech from patients experiencing various degrees of mental health problems.

The model serves multiple purposes. For instance, it can assist doctors in diagnosing mental health conditions in patients/certain individuals, or facilitate self-diagnosis for individuals seeking to understand their own mental health, or analyze the psychological characteristics of characters in fictional narratives.

The performace of this model in the test dataset (30477 rows) is as follows: 'accuracy': 0.78, 'f1': 0.77.

This model is one part of my project on fine-tuning open-source LLMs to predict various human cognitive abilities (e.g., personality, attitude, mental status etc.).

The following test examples can used in the API bar, 1)"I was okay just a moment ago. I will learn how to be okay again.".
2) "There were days when she was unhappy; she did not know why, when it did not seem worthwhile to be glad or sorry, to be alive or dead; when life appeared to her like a grotesque pandemonium and humanity like worms struggling blindly toward inevitable annihilation".
3)"I hope to one day see a sea of people all wearing silver ribbons as a sign that they understand the secret battle and as a celebration of the victories made each day as we individually pull ourselves up out of our foxholes to see our scars heal and to remember what the sun looks like.".

The **output** assigns a label with values from **0 to 5** to classify the **severity** of mental health issues. A label of **0** signifies **minimal severity**, suggesting few or no symptoms of mental health problems.
Conversely, a label of **5** denotes **maximal severity**, reflecting serious mental health conditions that may require immediate and comprehensive intervention.
**A larger value means that the situation is likely to be more serious**. Take care!

Please run the following code to test a new text:
```
import torch
from transformers import BertTokenizer, BertForSequenceClassification, AutoConfig

# Define the model path
model_path = "Kevintu/mentalhealth_LM"

# Load configuration, tokenizer, and model
config = AutoConfig.from_pretrained(model_path, num_labels=6, problem_type="single_label_classification")
tokenizer = BertTokenizer.from_pretrained(model_path, use_fast=True)
model = BertForSequenceClassification.from_pretrained(model_path, config=config, ignore_mismatched_sizes=True)

def predict_text(text, model, tokenizer):
    # Encode the text using the tokenizer
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)

    # Forward pass, get logits
    with torch.no_grad():
        outputs = model(**inputs)

    # Extract logits
    logits = outputs.logits

    # Convert logits to probabilities
    probabilities = torch.softmax(logits, dim=-1)
    max_probability, predicted_class_index = torch.max(probabilities, dim=-1)

    return predicted_class_index.item(), max_probability.item(), probabilities.numpy()

# Example usage
text = "I was okay just a moment ago. I will learn how to be okay again."
predicted_class, max_prob, probs = predict_text(text, model, tokenizer)
print(f"Predicted class: {predicted_class}, Probability: {max_prob:.4f}")

##Output: "Predicted class: 2, Probability: 0.5194"

```