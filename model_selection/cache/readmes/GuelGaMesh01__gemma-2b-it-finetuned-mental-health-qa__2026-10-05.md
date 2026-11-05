---
datasets:
- Amod/mental_health_counseling_conversations
library_name: transformers
license: mit
---

# Model Card Summary

<!-- Provide a quick summary of what the model is/does. -->
This model is a fine-tuned version of gemma-2b-it for mental health counseling conversations. 
It was fine-tuned on the Amod/Mental Health Counseling Conversations dataset, 
which contains dialogues related to mental health counseling.


## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

This is the model card of a 🤗 transformers model that has been pushed on the Hub. This model card has been automatically generated.

- **Developed by:** Miguel Flores
- **Model type:** Causal Language Model (based on transformers)
- **Language(s) (NLP):** English
- **License:** MIT License
- **Finetuned from model gemma-2b-it:** gemma-2b-it, which is a base model fine-tuned for mental health-related queries.


## Use Cases

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->


### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->
This model is fine-tuned for generating responses related to mental health counseling tasks. 
It can be used for providing suggestions, conversation starters, or follow-ups in mental health scenarios.


### Downstream Use 

<!-- This section is for the model use when fine-tuned for a task, or when plugged into a larger ecosystem/app -->
This model can be adapted for use in more specific counseling-related tasks, 
or in applications where generating mental health-related dialogue is necessary.


### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->
The model is not intended to replace professional counseling. 
It should not be used for real-time crisis management or any situation 
requiring direct human intervention. Use in highly critical or urgent care situations is out of scope.


## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

The model was trained on mental health-related dialogues, but it may still generate biased or 
inappropriate responses. Users should exercise caution when interpreting or acting on the model's outputs, 
particularly in sensitive scenarios.

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

The model should not be used as a replacement for professional mental health practitioners.
Users should carefully evaluate generated responses in the context of their use case.

## How to Get Started with the Model

Use the code below to get started with the model.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("GuelGaMesh01/gemma-2b-it-finetuned-mental-health-qa") 
model = AutoModelForCausalLM.from_pretrained("GuelGaMesh01/gemma-2b-it-finetuned-mental-health-qa")
```

### Example inference
```python
inputs = tokenizer("How can I manage anxiety better?", return_tensors="pt") outputs = model.generate(**inputs, max_length=200) response = tokenizer.decode(outputs[0], skip_special_tokens=True) print(response)
```


## Training Details

### Training Data

<!-- This should link to a Dataset Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

The model was trained on the Amod/Mental Health Counseling Conversations dataset, 
which consists of mental health dialogues focused on counseling situations.

### Training Procedure

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

The model was fine-tuned using LoRA (Low-Rank Adaptation) with the following hyperparameters:

Batch Size: 1
Gradient Accumulation Steps: 4
Learning Rate: 2e-4
Epochs: 3
Max Sequence Length: 2500 tokens
Optimizer: paged_adamw_8bit


## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->


#### Testing Data

<!-- This should link to a Dataset Card if possible. -->

The model was evaluated using a split from the training data, 
specifically a 10% test split of the original training dataset.


#### Metrics

<!-- These are the evaluation metrics being used, ideally with a description of why. -->


The following metrics were used during the training and evaluation process:

- **Training Loss**: The training loss was tracked during training to monitor how well the model was learning from the data. It decreased throughout the epochs.
- **Semantic Similarity**: Semantic similarity was employed as the primary metric to assess the model’s ability to generate contextually relevant and meaningful responses. Since the dataset involves conversational context, particularly in the sensitive area of mental health counseling, it was crucial to evaluate how well the model understands and retains the intent and meaning behind the input rather than merely focusing on fluency or token-level prediction.
- **Perplexity**: Perplexity was used as a metric to evaluate the model's ability to generate coherent and fluent text responses. The model was evaluated on a subset of the test data, and both non-finetuned and finetuned perplexities were compared.

