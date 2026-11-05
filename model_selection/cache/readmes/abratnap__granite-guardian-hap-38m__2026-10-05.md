---
license: apache-2.0
language:
- en
library_name: transformers
---

## Granite-Guardian-HAP-38m

## Model Summary
This model is IBM's lightweight, 4-layer toxicity binary classifier for English. Its latency characteristics make it a suitable guardrail for any large language model. It can also be used for bulk processing of data where high throughput is needed. It has been trained on several benchmark datasets in English, specifically for detecting hateful, abusive, profane and other toxic content in plain text.

- **Developers:** IBM Research
- **Release Date**: September 6th, 2024
- **License:** [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0).

## Usage

### Intended Use
This model offers very low inference latency and is capable of running on CPUs apart from GPUs and AIUs. It features 38 million parameters, reducing the number of hidden layers from 12 to 4, decreasing the hidden size from 768 to 576, and the intermediate size from 3072 to 768, compared to the original RoBERTa model architecture. The latency on CPU vs accuracy numbers for this model in comparision to others is shown in the chart below. 

![Description of Image](38m_latency.png)


## Prediction
```python
# Example of how to use the model
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_name_or_path = 'ibm-granite/granite-guardian-hap-38m'
model = AutoModelForSequenceClassification.from_pretrained(model_name_or_path)
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)

# Sample text
text = ["This is the 1st test", "This is the 2nd test"]
input = tokenizer(text, padding=True, truncation=True, return_tensors="pt")

with torch.no_grad():
    logits = model(**input).logits
    prediction = torch.argmax(logits, dim=1).detach().numpy().tolist() # Binary prediction where label 1 indicates toxicity.
    probability = torch.softmax(logits, dim=1).detach().numpy()[:,1].tolist() #  Probability of toxicity.
   
```

## Cookbook on Model Usage as a Guardrail
This recipe illustrates the use of the model either in a prompt, the output, or both. This is an example of a “guard rail” typically used in generative AI applications for safety.
[Guardrail Cookbook](https://github.com/ibm-granite-community/granite-code-cookbook/blob/main/recipes/Guard-Rails/HAP.ipynb)

## Cookbook on Model Usage for HAP Annotation on Documents in Bulk using [Data Prep Kit](https://github.com/IBM/data-prep-kit)
This recipe illustrates the use of the model for HAP annotation of documents in bulk. The documents are read from a parquet file. It is then fed to the model sentence by sentence for a document and a HAP score for the document is decided. This is then stored back in the parquet file. Here is the sample cookbook for it [Data Prep Kit Cookbook](https://github.com/IBM/data-prep-kit/tree/dev/transforms/universal/hap/python)


## Performance Comparison with Other Models
The model outperforms most popular models with significantly lower inference latency. If a better F1 score is required, please refer to IBM's 12-layer model [here](https://huggingface.co/ibm-granite/granite-guardian-hap-125m). 

![Description of Image](38m_comparison_a.png)
![Description of Image](38m_comparison_b.png)

## Ethical Considerations and Limitations
The use of model-based guardrails for Large Language Models (LLMs) involves risks and ethical considerations people must be aware of. This model operates on chunks of texts and provides a score indicating the presence of hate speech, abuse, or profanity. However, the efficacy of the model can be limited by several factors: the potential inability to capture nuanced meanings or the risk of false positives or negatives on text that is dissimilar to the training data. Previous research has demonstrated the risk of various biases in toxicity or hate speech detection. That is also relevant to this work. We urge the community to use this model with ethical intentions and in a responsible way.
