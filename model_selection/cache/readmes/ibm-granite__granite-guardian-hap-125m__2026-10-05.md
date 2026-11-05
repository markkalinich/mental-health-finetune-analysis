---
license: apache-2.0
language:
- en
pipeline_tag: text-classification
library_name: transformers
---

## Granite-Guardian-HAP-125m

## Model Summary
This model is IBM's 12-layer toxicity binary classifier for English, intended to be used as a guardrail for any large language model. It has been trained on several benchmark datasets in English, specifically for detecting hateful, abusive, profane and other toxic content in plain text. 

- **Developers:** IBM Research
- **Release Date**: September 6th, 2024
- **License:** [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0).
  
## Usage
```python
# Example of how to use the model
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

model_name_or_path = 'ibm-granite/granite-guardian-hap-125m'
model = AutoModelForSequenceClassification.from_pretrained(model_name_or_path)
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
model.to(device)

# Sample text
text = ["This is the 1st test", "This is the 2nd test"]
input = tokenizer(text, padding=True, truncation=True, return_tensors="pt").to(device)

with torch.no_grad():
    logits = model(**input).logits
    prediction = torch.argmax(logits, dim=1).cpu().detach().numpy().tolist() # Binary prediction where label 1 indicates toxicity.
    probability = torch.softmax(logits, dim=1).cpu().detach().numpy()[:,1].tolist() #  Probability of toxicity.
   
```

## Performance Comparison with Other Models
This model demonstrates superior average performance in comparison with other models on eight mainstream toxicity benchmarks. If a very fast model is required, please refer to the lightweight 4-layer IBM model, [granite-guardian-hap-38m](https://huggingface.co/ibm-granite/granite-guardian-hap-38m).

![Description of Image](125m_comparison_a.png)
![Description of Image](125m_comparison_b.png)

## Ethical Considerations and Limitations
The use of model-based guardrails for Large Language Models (LLMs) involves risks and ethical considerations people must be aware of. This model operates on chunks of texts and provides a score indicating the presence of hate speech, abuse, or profanity. However, the efficacy of the model can be limited by several factors: the potential inability to capture nuanced meanings or the risk of false positives or negatives on text that is dissimilar to the training data. Previous research has demonstrated the risk of various biases in toxicity or hate speech detection. That is also relevant to this work. We urge the community to use this model with ethical intentions and in a responsible way.

### Resources
- ⭐️ Learn about the latest updates with Granite: https://www.ibm.com/granite
- 📄 Get started with tutorials, best practices, and prompt engineering advice: https://www.ibm.com/granite/docs/
- 💡 Learn about the latest Granite learning resources: https://ibm.biz/granite-learning-resources
