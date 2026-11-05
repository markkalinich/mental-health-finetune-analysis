---
license: apache-2.0
pipeline_tag: text-generation
tags:
- medical
---

# Details about the model and process

The model has been fine-tuned using personal resources and the help of RunPod and Axolotl. The process took around 15 hours for the training to complete 1.5 epochs given the size of the dataset (950.000 rows) and the size of the model itself with a batch size of 8, alongside some extra hours to merge the adapter to the base model. Given the lack of resources from my campus, this was all done throughout 7 months where I had to jump through multiple services and methods. 


# Information about base model:

- **Llama 3.2 Model Family:** Token counts refer to pretraining data only. All model versions use Grouped-Query Attention (GQA) for improved inference scalability.

- **Model Release Date:** Sept 25, 2024

- **For more information be sure to check [Llama 3.2](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct)**

# Uploaded  model

- **Developed by:** Inigo Chandia
- **License:** apache-2.0
- **Finetuned from model :** meta-llama/Llama-3.2-3B-Instruct
- **Completion Date:** Sept 9, 2025

# Intended use

The purpose of this model as the name suggest is to provide emotional support as a therapist would. In this day and age, mental health issues are rampant, An LLM can provide more consistent support. With tech like this, more lives can be saved, or at least maintained until more help is available.

# Dataset

The dataset used for this task was [usham/mental-health-companion-new](https://huggingface.co/datasets/usham/mental-health-companion-new)

# Test results

The test consisted of 11 questions that consistently increased in distress. All test passed successfully.

- **First 3 tests**

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6639e333e05e7949585d45d0/0tZ_D23OIxeUalIMoPmOF.png)

 - **Total results test chart**

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6639e333e05e7949585d45d0/myF6g49Fex414Mw6xwjIP.png)

3 highly sensitive questions have been tested and all yielded amazing results.

# Main tools


The main environment used for this task was [Runpod](https://console.runpod.io/)

[<img src="https://datasciencedojo.com/wp-content/uploads/RunPod-2.png" width="200"/>](https://console.runpod.io/)

This model was fine-tuned faster with [Axolotl](https://github.com/axolotl-ai-cloud/axolotl)

[<img src="https://raw.githubusercontent.com/axolotl-ai-cloud/axolotl/887513285d98132142bf5db2a74eb5e0928787f1/image/axolotl_logo_digital_white.svg" width="200"/>](https://github.com/axolotl-ai-cloud/axolotl)