---
base_model: unsloth/Llama-3.2-11B-Vision-Instruct
tags:
- text-generation-inference
- transformers
- unsloth
- mllama
license: apache-2.0
language:
- en
datasets:
- WinterSchool/MedificsDataset
pipeline_tag: visual-question-answering
---

Llama3.2 11B vision model fine-tuned medical dataset containing pictures and conversations on radiology and skin cancer images. 

Best used with - min_p = 0.1 and temperature = 1.5

## Examples


![image/png](https://cdn-uploads.huggingface.co/production/uploads/637399522b908db6336c22a9/7juwt-xejo7qdPpb4Zko1.png)

Question: What does the HRCT of the thorax show?

Answer: The HRCT shows diffuse irregular linear and reticular pattern with multiple tiny nodules in a reticular pattern, compatible with interstitial lung disease.



Question: Which interstitial lung disease is it?

Answer: It is UIP, which is also known as fibrotic interstitial pneumonia.


Question: What is the prognosis for a patient with definite UIP pattern on HRCT?

Answer: The prognosis for a patient with definite UIP pattern on HRCT is generally poor, with median survival ranging from 2 to 5 years after the onset of symptoms.


Question: Is there any treatment available for a patient with UIP pattern?
Answer: Unfortunately, there is no cure for UIP pattern. Treatment options are limited and focused on managing symptoms and slowing disease progression.


# Uploaded finetuned  model

- **Developed by:** dumbequation
- **License:** apache-2.0
- **Finetuned from model :** unsloth/Llama-3.2-11B-Vision-Instruct