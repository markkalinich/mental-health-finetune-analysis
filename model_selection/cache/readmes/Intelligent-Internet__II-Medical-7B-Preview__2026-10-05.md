---
library_name: transformers
tags: []
---

# II-Medical-7B-Preview

<div style="display: flex; justify-content: center;">
    <img src="https://cdn-uploads.huggingface.co/production/uploads/6389496ff7d3b0df092095ed/73Y-oDmehp0eJ2HWrfn3V.jpeg" width="800">
</div>

## I. Model Overview

II-Medical-7B-Preview is a medical reasoning model trained on a [comprehensive dataset](https://huggingface.co/datasets/Intelligent-Internet/II-Medical-Reasoning-SFT-V0) of medical knowledge. The model is designed to enhance AI capabilities in medical. 

![Model Benchmark](https://cdn-uploads.huggingface.co/production/uploads/6389496ff7d3b0df092095ed/oTGtjC-ngnIZw9BpVgAHv.png)

## II. Training Methodology

We collected and generated a comprehensive set of reasoning datasets for the medical domain and performed SFT fine-tuning on the **Qwen/Qwen2.5-7B-Instruct** model. Following this, we further optimized the SFT model by training DAPO on a hard-reasoning dataset to boost performance.

For SFT stage we using the hyperparameters: 

- Max Length: 16378.
- Batch Size: 128.
- Learning-Rate: 5e-5.
- Number Of Epoch: 4.

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

We evaluate on ten medical QA benchmarks include MedMCQA, MedQA, PubMedQA, medical related questions from MMLU-Pro and GPQA, small QA sets from Lancet and the New England
Journal of Medicine,  4 Options  and 5 Options splits from the MedBullets platform and MedXpertQA.

| Model                   | MedMC | MedQA | PubMed | MMLU-P | GPQA | Lancet | MedB-4 | MedB-5 | MedX  | NEJM  | Avg   |
|--------------------------|-------|-------|--------|--------|------|--------|--------|--------|------|-------|-------|
| QWQ 32B                  | 69.73 | 87.03 | 88.5   | 79.86  | 69.17| 71.3   | 72.07  | 69.01  |24.98 |75.12  | 70.68 |
| Qwen2.5-7B-IT            | 56.56 | 61.51 | 71.3   | 61.17  | 42.56| 61.17  | 46.75  | 40.58  |13.26 |59.04  | 51.39 |
| HuatuoGPT-o1-8B          | 63.97 | 74.78 | **80.10**  | 63.71  | 55.38| 64.32  | 58.44  | 51.95  |15.79 |64.84  | 59.32 |
| Med-reason               | 61.67 | 71.87 | 77.4   | 64.1   | 50.51| 59.7   | 60.06  | 54.22  |22.87 |66.8   | 59.92 |
| M1                       | 62.54 | 75.81 | 75.80  | 65.86  | 53.08| 62.62  | 63.64  | 59.74  |19.59 |64.34  | 60.3  |
| II-Medical-7B-Preview-Wo-RL | 69.13 | 84.05 | 77.5   | 73.49  | 55.12| **67.71**  | 69.48  | 64.28  |19.51 |**70.64**  | 65.1  |
| II-Medical-7B-Preview | **69.42** | **85.15** | 77.9   | **77.26**  | **55.90**| 65.29  | **72.72**  | **68.50**  |**22.97** |68.66  | **66.4**  |



## IV. Dataset Curation

The training dataset comprises 555,000 samples from the following sources:

### 1. Public Medical Reasoning Datasets (103,031 samples)
- General Medical Reasoning: 40,544 samples
- Medical-R1-Distill-Data: 22,000 samples
- Medical-R1-Distill-Data-Chinese: 17,000 samples
- UCSC-VLAA/m23k-tokenized: 23,487 samples

### 2. Synthetic Medical QA Data with QwQ (225,700 samples)
Generated from established medical datasets:
- MedMcQA (from openlifescienceai/medmcqa): 183,000 samples
- MedQA: 10,000 samples
- MedReason: 32,700 samples

### 3. Curated Medical R1 Traces (338,055 samples)

First we gather all the public R1 traces from:

- PrimeIntellect/SYNTHETIC-1
- GeneralReasoning/GeneralThought-430K
- a-m-team/AM-DeepSeek-R1-Distilled-1.4M
- open-thoughts/OpenThoughts2-1M
- nvidia/Llama-Nemotron-Post-Training-Dataset: Science subset only
- Other resources: cognitivecomputations/dolphin-r1, ServiceNow-AI/R1-Distill-SFT,...

All R1 reasoning traces were processed through a domain-specific pipeline as follows:

1. Embedding Generation: Prompts are embedded using sentence-transformers/all-MiniLM-L6-v2.

2. Clustering: Perform K-means clustering with 50,000 clusters.

3. Domain Classification:

    - For each cluster, select the 10 prompts nearest to the cluster center.
    - Classify the domain of each selected prompt using Qwen2.5-32b-Instruct.
    - Assign the cluster's domain based on majority voting among the classified prompts.

4. Domain Filtering: Keep only clusters labeled as Medical or Biology for the final dataset.


### 4. Supplementary Math Dataset
- Added 15,000 samples of reasoning traces from light-r1
- Purpose: Enhance general reasoning capabilities of the model

### Preprocessing Data
1. Filtering for Complete Generation
   - Retained only traces with complete generation outputs

2. Length-based Filtering
   - Minimum threshold: Keep only the prompt with more than 3 words.
   - Maximum threshold: Keep only the traces with less than 7,143 words.
   - Wait Token Filter: Removed traces with has more than 47 occurrences of "Wait" (97th percentile threshold).


### Data Decontamination

We using two step decontamination:
1. Following open-r1 project: We decontaminate a dataset using 10-grams with the evaluation datasets.
2. After that, we using the fuzzy decontamination from `s1k` method with threshold 90%. 

**Our pipeline is carefully decontaminated with the evaluation datasets.**

## V. How To Use
Our model can be utilized in the same manner as Qwen or Deepseek-R1-Distill models.

For instance, you can easily start a service using [vLLM](https://github.com/vllm-project/vllm):

```bash
vllm serve Intelligent-Internet/II-Medical-7B-Preview
```

You can also easily start a service using [SGLang](https://github.com/sgl-project/sglang):

```bash
python -m sglang.launch_server --model Intelligent-Internet/II-Medical-7B-Preview
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
@misc{2025II-Medical-7B-Preview,
      title={II-Medical-7B-Preview: Medical Reasoning Model}, 
      author={Intelligent Internet},
      year={2025}
}
```