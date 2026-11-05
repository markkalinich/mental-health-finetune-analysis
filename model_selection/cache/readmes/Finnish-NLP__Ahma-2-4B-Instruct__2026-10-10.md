---
language:
- fi
license: apache-2.0
tags:
- finnish
- gemma
inference: false
pipeline_tag: text-generation
---

*   **Base Model:** [Gemma-3-4b-pt](https://huggingface.co/google/gemma-3-4b-pt)
*   **Language:** Finnish (fi)
*   **Training Methodology:**
    *   Step 1: Continued Pretraining (CP) Mix of English, Finnish and Code-switching data
    *   Step 2: Supervised Fine-Tuning (SFT) Mostly Finnish
    *   Step 3: Direct Preference Optimization (DPO) Mostly Finnish

## Running this model
More info coming later

## Pretraining
More info coming later

## Finetuning
More info coming later

## Evaluation results


### MTBench Finnish

This Ahma-Gemma-3-4B-Instruct-v1.0 model was primarily evaluated using [MTBench Finnish by LumiOpen](https://github.com/LumiOpen/FastChat/tree/main/fastchat/llm_judge) 

Single-turn results:

| Benchmark           | Ahma 3B base (instruct prompt format) | Ahma 7B Instruct (instruct prompt format)  | Ahma-Gemma-3-4B-Instruct-v1.0 |
|:--------------------|:--------------------------------------|:------------------------------------------|:--------------------------------------|
| Coding              | 1.00                                  | 1.00                                      | 4.2                                      
| Extraction          | 1.30                                  | 3.00                                      | 7.3                                      
| Humanities          | 6.20                                  | 8.00                                      | 8.9                                      
| Math                | 3.20                                  | 2.90                                      | 6.1                                      
| Reasoning           | 4.60                                  | 5.70                                      | 4.8                                      
| Roleplay            | 6.50                                  | 7.20                                      | 7.7                                      
| STEM                | 5.95                                  | 7.30                                      | 9.9                                      
| Writing             | 9.00                                  | 8.80                                      | 9.2                                      
| **Overall Average** | **4.72**                              | **5.50**                                  | **7.26**                                  

Multi-turn results:

| Benchmark           | Ahma 3B Instruct (instruct prompt format) | Ahma 7B Instruct (instruct prompt format) | Ahma-Gemma-3-4B-Instruct-v1.0 | Poro 34B Chat | Poro-2-8B-Instruct|
|:--------------------|:------------------------------------------|:------------------------------------------|:------------------------------|---------------|-------------------|
| Coding              | 1.00                                      | 1.05                                      | 4.35                          | 3.70          |        ?          |
| Extraction          | 1.15                                      | 2.65                                      | 6.55                          | 6.37          |        ?          |
| Humanities          | 6.20                                      | 7.85                                      | 6.55                          | 9.25          |        ?          |
| Math                | 2.70                                      | 2.40                                      | 4.80                          | 1.20          |        ?          |
| Reasoning           | 3.50                                      | 4.50                                      | 4.40                          | 4.35          |        ?          |
| Roleplay            | 6.40                                      | 6.60                                      | 7.26                          | 7.35          |        ?          |
| STEM                | 4.78                                      | 5.40                                      | 8.80                          | 7.80          |        ?          |
| Writing             | 6.65                                      | 6.25                                      | 7.6                           | 8.50          |        ?          |
| **Overall Average** | **4.05**                                  | **4.59**                                  | **6.57**                      | **6.06**      | **6.75**          |


As we can see, the Ahma-Gemma-3-4B-Instruct-v1.0 model improves upon our previous model generation. We have already started to work on the datasets and methods to improve this model/scale to bigger models


## Acknowledgements

This project would not have been possible without compute generously provided by Google through the
[TPU Research Cloud](https://sites.research.google/trc/).

Datacrunch/Verda for sponsoring us some compute for Finetuning:
HF Org (https://huggingface.co/datacrunch)
Website: (https://verda.com/)

## Team Members

- Aapo Tanskanen, [Hugging Face profile](https://huggingface.co/aapot), [LinkedIn profile](https://www.linkedin.com/in/aapotanskanen/)
  - Initial parts in pretraining in our continued pretraining journey
- Rasmus Toivanen, [Hugging Face profile](https://huggingface.co/RASMUS), [LinkedIn profile](https://www.linkedin.com/in/rasmustoivanen/)
  - Pretraining this model, post-training this model, gathering datasets, running evaluations

## Other notable supporters on this journey
- Ari Kouhia, [Hugging Face profile](https://huggingface.co/concur-means-risotto) for helpful comments on our WA group and helping in synthetic data generation
- Heikki Saxén, [Hugging Face profile](https://huggingface.co/ducklingcodehouse) for helpful comments on our WA group and also for finetuning DentalQA models on top of this model
- Mikko Hällfors, [Hugging Face profile](https://huggingface.co/Avokid) for helpful comments on our WA group and helping in synthetic data generation

Feel free to contact us for more details 🤗


![Ahma](ahma.jpg)