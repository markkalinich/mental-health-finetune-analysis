---
datasets:
- sid6i7/patient-doctor
library_name: transformers
license: mit
tags:
- medical
- biology
---



 Model Card for "medllama"
---------------------------

**Model Name:** medllama

**Library Name:** peft (Python library for Efficient Tuning)

**Base Model:** TinyLlama 1.1B (A pretrained language model with 7 billion parameters, fine-tuned for chat applications.)

**License:** Apache-2.0 License

### Usage 
For usage, use this code block, with GPU recommended
```
# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("tmberooney/medllama-merged")
model = AutoModelForCausalLM.from_pretrained("tmberooney/medllama-merged")
```

### Intended Use
---------------

The `medllama` model is a fine-tuned version of the base model specifically adapted for medical conversations between patients and doctors. This model can be used in various healthcare settings to assist professionals during their interactions with patients, providing relevant suggestions or answering questions related to health conditions, treatments, medications, and other medical topics. The goal is to improve communication efficiency and ensure accurate information exchange while maintaining privacy and confidentiality standards.

### Training Data
--------------

This model was trained using data from the `sid6i7/patient-doctor` dataset, which contains deidentified medical dialogues between patients and physicians covering diverse medical domains like internal medicine, pediatrics, neurology, psychiatry, and more. These conversations are designed to simulate real-life clinical scenarios, allowing the model to understand context, generate responses that reflect appropriate levels of empathy, and provide reliable medical information based on user queries.

### Evaluation Results
--------------------

Evaluations were conducted on several benchmark datasets tailored towards measuring performance in medical dialogue systems. Metrics such as perplexity, BLEU score, ROUGE score, and F1 score have been reported to assess the quality and relevance of generated responses compared to reference answers. Detailed evaluation results will be provided separately upon request.

### Ethical Considerations
-------------------------

To maintain ethical guidelines when deploying this model, it's crucial to consider the following aspects:

* **Data Privacy**: Ensure patient data remains anonymous and protected throughout all stages of development and deployment. Obtain informed consent before utilizing any identifiable personal health information.
* **Medical Accuracy**: Regularly review and update the model based on new research findings and evidence-based practices. Always encourage users to consult licensed healthcare providers regarding specific concerns or diagnoses.
* **Bias Mitigation**: Continuously monitor and address potential biases within training data and model outputs to avoid discrimination against certain demographics. Strive for inclusivity by incorporating diverse sources of information during development.
* **User Awareness**: Inform end-users about limitations, intended uses, and possible risks associated with interacting with an AI system rather than a human expert. Clearly outline expectations for accuracy, response times, and available features.

For further details on these guidelines, please refer to our project documentation.