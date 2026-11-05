---
library_name: transformers
license: apache-2.0
---

# II-Medical-8B

<div style="display: flex; justify-content: center;">
    <img src="https://cdn-uploads.huggingface.co/production/uploads/6389496ff7d3b0df092095ed/73Y-oDmehp0eJ2HWrfn3V.jpeg" width="800">
</div>

## I. Model Overview

II-Medical-8B is the newest advanced large language model developed by Intelligent Internet, specifically engineered to enhance AI-driven medical reasoning. Following the positive reception of our previous [II-Medical-7B-Preview](https://huggingface.co/Intelligent-Internet/II-Medical-7B-Preview), this new iteration significantly advances the capabilities of medical question answering, 

## II. Training Methodology

We collected and generated a comprehensive set of reasoning datasets for the medical domain and performed SFT fine-tuning on the **Qwen/Qwen3-8B** model. Following this, we further optimized the SFT model by training DAPO on a hard-reasoning dataset to boost performance.

For SFT stage we using the hyperparameters: 

- Max Length: 16378.
- Batch Size: 128.
- Learning-Rate: 5e-5.
- Number Of Epoch: 8.

For RL stage we setup training with:

- Max prompt length: 2048 tokens.
- Max response length: 12288 tokens.
- Overlong buffer: Enabled, 4096 tokens, penalty factor 1.0.
- Clip ratios: Low 0.2, High 0.28.
- Batch sizes: Train prompt 512, Generation prompt 1536, Mini-batch 32.
- Responses per prompt: 16.
- Temperature: 1.0, Top-p: 1.0, Top-k: -1 (vLLM rollout).
- Learning rate: 1e-6, Warmup steps: 10, Weight decay: 0.1.
- Loss aggregation: Token-mean.
- Gradient clipping: 1.0.
- Entropy coefficient: 0.

## III. Evaluation Results

Our II-Medical-8B model achieved a 40% score on [HealthBench](https://openai.com/index/healthbench/), a comprehensive open-source benchmark evaluating the performance and safety of large language models in healthcare. This performance is comparable to OpenAI's o1 reasoning model and GPT-4.5, OpenAI's largest and most advanced model to date. We provide a comparison to models available in ChatGPT below.

![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/61f2636488b9b5abbe184a8e/5r2O4MtzffVYfuUZJe5FO.jpeg)
Detailed result for HealthBench can be found [here](https://huggingface.co/datasets/Intelligent-Internet/OpenAI-HealthBench-II-Medical-8B-GPT-4.1).

![Model Benchmark](https://cdn-uploads.huggingface.co/production/uploads/6389496ff7d3b0df092095ed/uvporIhY4_WN5cGaGF1Cm.png)

We evaluate on ten medical QA benchmarks include MedMCQA, MedQA, PubMedQA, medical related questions from MMLU-Pro and GPQA, small QA sets from Lancet and the New England
Journal of Medicine,  4 Options  and 5 Options splits from the MedBullets platform and MedXpertQA.

| Model                   | MedMC | MedQA | PubMed | MMLU-P | GPQA | Lancet | MedB-4 | MedB-5 | MedX  | NEJM  | Avg   |
|--------------------------|-------|-------|--------|--------|------|--------|--------|--------|------|-------|-------|
| [HuatuoGPT-o1-72B](https://huggingface.co/FreedomIntelligence/HuatuoGPT-o1-72B)         | 76.76 | 88.85 | 79.90   | 80.46  | 64.36| 70.87   | 77.27  | 73.05  |23.53 |76.29  | 71.13 |
| [QWQ 32B](https://huggingface.co/Qwen/QwQ-32B)                  | 69.73 | 87.03 | 88.5   | 79.86  | 69.17| 71.3   | 72.07  | 69.01  |24.98 |75.12  | 70.68 |
| [Qwen2.5-7B-IT](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct)            | 56.56 | 61.51 | 71.3   | 61.17  | 42.56| 61.17  | 46.75  | 40.58  |13.26 |59.04  | 51.39 |
| [HuatuoGPT-o1-8B](http://FreedomIntelligence/HuatuoGPT-o1-8B)          | 63.97 | 74.78 | **80.10**  | 63.71  | 55.38| 64.32  | 58.44  | 51.95  |15.79 |64.84  | 59.32 |
| [Med-reason](https://huggingface.co/UCSC-VLAA/MedReason-8B)               | 61.67 | 71.87 | 77.4   | 64.1   | 50.51| 59.7   | 60.06  | 54.22  |22.87 |66.8   | 59.92 |
| [M1](https://huggingface.co/UCSC-VLAA/m1-7B-23K)                     | 62.54 | 75.81 | 75.80  | 65.86  | 53.08| 62.62  | 63.64  | 59.74  |19.59 |64.34  | 60.3  |
| [II-Medical-8B-SFT](https://huggingface.co/II-Vietnam/II-Medical-8B-SFT)        | **71.92** | 86.57 | 77.4   | 77.26  | 65.64| 69.17  | 76.30  | 67.53  |23.79 |**73.80**  | 68.80  |
| [II-Medical-8B](https://huggingface.co/Intelligent-Internet/II-Medical-8B)            | 71.57 | **87.82** | 78.2   | **80.46**  | **67.18**| **70.38**  | **78.25**  | **72.07**  |**25.26** |73.13  | **70.49**  |

## IV. Dataset Curation

The training dataset comprises 555,000 samples from the following sources:

### 1. Public Medical Reasoning Datasets (103,031 samples)
- [General Medical Reasoning](https://huggingface.co/datasets/GeneralReasoning/GeneralThought-430K): 40,544 samples
- [Medical-R1-Distill-Data](https://huggingface.co/datasets/FreedomIntelligence/Medical-R1-Distill-Data): 22,000 samples
- [Medical-R1-Distill-Data-Chinese](https://huggingface.co/datasets/FreedomIntelligence/Medical-R1-Distill-Data-Chinese): 17,000 samples
- [UCSC-VLAA/m23k-tokenized](https://huggingface.co/datasets/UCSC-VLAA/m23k-tokenized): 23,487 samples

### 2. Synthetic Medical QA Data with QwQ (225,700 samples)
Generated from established medical datasets:
- [MedMcQA](https://huggingface.co/datasets/openlifescienceai/medmcqa) (from openlifescienceai/medmcqa): 183,000 samples
- [MedQA](https://huggingface.co/datasets/bigbio/med_qa): 10,000 samples
- [MedReason](https://huggingface.co/datasets/UCSC-VLAA/MedReason): 32,700 samples

### 3. Curated Medical R1 Traces (338,055 samples)

First we gather all the public R1 traces from:

- [PrimeIntellect/SYNTHETIC-1](https://huggingface.co/collections/PrimeIntellect/synthetic-1-67a2c399cfdd6c9f7fae0c37)
- [GeneralReasoning/GeneralThought-430K](https://huggingface.co/datasets/GeneralReasoning/GeneralThought-430K)
- [a-m-team/AM-DeepSeek-R1-Distilled-1.4M](https://arxiv.org/abs/2503.19633v1)
- [open-thoughts/OpenThoughts2-1M](https://huggingface.co/datasets/open-thoughts/OpenThoughts2-1M)
- [nvidia/Llama-Nemotron-Post-Training-Dataset](https://huggingface.co/datasets/nvidia/Llama-Nemotron-Post-Training-Dataset): Science subset only
- Other resources: [cognitivecomputations/dolphin-r1](https://huggingface.co/datasets/cognitivecomputations/dolphin-r1), [ServiceNow-AI/R1-Distill-SFT](https://huggingface.co/datasets/ServiceNow-AI/R1-Distill-SFT),...

All R1 reasoning traces were processed through a domain-specific pipeline as follows:

1. Embedding Generation: Prompts are embedded using sentence-transformers/all-MiniLM-L6-v2.

2. Clustering: Perform K-means clustering with 50,000 clusters.

3. Domain Classification:

    - For each cluster, select the 10 prompts nearest to the cluster center.
    - Classify the domain of each selected prompt using Qwen2.5-32b-Instruct.
    - Assign the cluster's domain based on majority voting among the classified prompts.

4. Domain Filtering: Keep only clusters labeled as Medical or Biology for the final dataset.


### 4. Supplementary Math Dataset
- Added 15,000 samples of reasoning traces from [light-r1](https://arxiv.org/abs/2503.10460)
- Purpose: Enhance general reasoning capabilities of the model

### Preprocessing Data
1. Filtering for Complete Generation
   - Retained only traces with complete generation outputs

2. Length-based Filtering
   - Minimum threshold: Keep only the prompt with more than 3 words.
   - Wait Token Filter: Removed traces with has more than 47 occurrences of "Wait" (97th percentile threshold).


### Data Decontamination

We using two step decontamination:
1. Following [open-r1](https://github.com/huggingface/open-r1) project: We decontaminate a dataset using 10-grams with the evaluation datasets.
2. After that, we using the fuzzy decontamination from [`s1k`](https://arxiv.org/abs/2501.19393) method with threshold 90%. 

**Our pipeline is carefully decontaminated with the evaluation datasets.**

## V. How To Use
Our model can be utilized in the same manner as Qwen or Deepseek-R1-Distill models.

For instance, you can easily start a service using [vLLM](https://github.com/vllm-project/vllm):

```bash
vllm serve Intelligent-Internet/II-Medical-8B
```

You can also easily start a service using [SGLang](https://github.com/sgl-project/sglang):

```bash
python -m sglang.launch_server --model Intelligent-Internet/II-Medical-8B
```

## VI. Usage Guidelines

- Recommended Sampling Parameters: temperature = 0.6, top_p = 0.9
- When using, explicitly request step-by-step reasoning and format the final answer within \boxed{} (e.g., "Please reason step-by-step, and put your final answer within \boxed{}.").
## VII. Limitations and Considerations

- Dataset may contain inherent biases from source materials
- Medical knowledge requires regular updates
- Please note that **It’s not suitable for medical use.**


## VIII. Citation

```bib
@misc{2025II-Medical-8B,
      title={II-Medical-8B: Medical Reasoning Model}, 
      author={Intelligent Internet},
      year={2025}
}
```