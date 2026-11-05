---
base_model: andreasmartin/apertus-v1.5-8b-text
library_name: transformers
pipeline_tag: text-generation
license: apache-2.0
language:
- en
tags:
- safetensors
- text-generation
- apertus
- sft
- peft
- qlora
- biomedical
- adverse-drug-events
- named-entity-recognition
datasets:
- mihirhirave/entity_extraction_ade_v2_with_validation
metrics:
- loss
- accuracy
model-index:
- name: andreasmartin/apertus-1.5-8b-biomedical-ade-qlora-exercise-60steps-20260928-072251
  results:
  - task:
      type: text-generation
      name: Biomedical Information Extraction
    dataset:
      name: mihirhirave/entity_extraction_ade_v2_with_validation
      type: mihirhirave/entity_extraction_ade_v2_with_validation
      split: validation[:100]
    metrics:
          - name: Validation Loss
            type: loss
            value: 0.06020
            source:
              name: Weights & Biases Run
              url: https://wandb.ai/fhnw-ch/Apertus/runs/jg8hn5o1
          - name: Validation Token Accuracy
            type: accuracy
            value: 0.97688
            source:
              name: Weights & Biases Run
              url: https://wandb.ai/fhnw-ch/Apertus/runs/jg8hn5o1
          - name: Final Training Loss
            type: loss
            value: 0.09771
            source:
              name: Weights & Biases Run
              url: https://wandb.ai/fhnw-ch/Apertus/runs/jg8hn5o1
---

# Apertus 1.5 8B — QLoRA (BIOMEDICAL_ADE)

> ⚠️ **CRITICAL DISCLAIMER: HIGHLY EXPERIMENTAL RESEARCH MODEL**  
> This model is a **proof-of-concept research artifact** developed exclusively for academic experimentation, demonstration, and benchmarking purposes.  
> - **NOT FOR CLINICAL USE**: This system is **NOT** a certified medical device and must **NEVER** be used to provide medical advice, diagnosis, triage, or clinical decision support.  
> - **INCORRECT OR INCOMPLETE OUTPUT**: The outputs may omit severe drug reactions or state side effects that do not exist. Always rely on certified clinical pharmacologists and authorized medical references.  
> - The authors and contributors assume no liability for any direct or indirect damages resulting from the use or misuse of this model.

Fine-tuned from [`andreasmartin/apertus-v1.5-8b-text`](https://huggingface.co/andreasmartin/apertus-v1.5-8b-text) on [`mihirhirave/entity_extraction_ade_v2_with_validation`](https://huggingface.co/datasets/mihirhirave/entity_extraction_ade_v2_with_validation).

This repository contains the complete standalone fine-tuned model in 16-bit Safetensors format.

## Example Prompts & Expected Outputs

### Example 1: Multi-Drug Toxicity Detection
**Prompt:**
```text
You are an expert biomedical information extraction system. Extract all mentioned drugs and adverse drug events (ADEs) from the clinical narrative as JSON.

Clinical Narrative:
"A 64-year-old female patient with chronic atrial fibrillation presented with severe bradycardia, visual yellow halos, and nausea after increasing her digoxin dosage to 0.25 mg daily. Electrocardiogram confirmed digitalis toxicity. Concurrently, she had been prescribed amiodarone two weeks earlier."
```

**Model Output:**
```json
{
  "drugs": ["digoxin", "amiodarone"],
  "adverse_drug_events": ["severe bradycardia", "visual yellow halos", "nausea"]
}
```

### Example 2: Negative Control
**Prompt:**
```text
You are an expert biomedical information extraction system. Extract all mentioned drugs and adverse drug events (ADEs) from the clinical narrative as JSON.

Clinical Narrative:
"The patient was initiated on metformin 500 mg twice daily for type 2 diabetes mellitus and reported good glycemic control without any adverse symptoms."
```

**Model Output:**
```json
{
  "drugs": ["metformin"],
  "adverse_drug_events": []
}
```

## Quickstart

### vLLM

```bash
vllm serve andreasmartin/apertus-1.5-8b-biomedical-ade-qlora-exercise-60steps-20260928-072251 --tensor-parallel-size 1 --gpu-memory-utilization 0.9
```

### Transformers

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("andreasmartin/apertus-1.5-8b-biomedical-ade-qlora-exercise-60steps-20260928-072251")
model = AutoModelForCausalLM.from_pretrained(
    "andreasmartin/apertus-1.5-8b-biomedical-ade-qlora-exercise-60steps-20260928-072251",
    device_map="auto",
)
```

## Training Configuration & Metrics

| Parameter | Value |
| :--- | :--- |
| **Run ID** | `20260928-072251` |
| **Run Label** | `exercise` |
| **Training Method** | `QLoRA` |
| **Environment** | `Kaggle` |
| **Hardware** | `2 × Tesla T4` |
| **Compute Dtype** | `bfloat16` |
| **Quantization** | `NF4 4-bit` |
| **Base Model** | [`andreasmartin/apertus-v1.5-8b-text`](https://huggingface.co/andreasmartin/apertus-v1.5-8b-text) |
| **Dataset** | [`mihirhirave/entity_extraction_ade_v2_with_validation`](https://huggingface.co/datasets/mihirhirave/entity_extraction_ade_v2_with_validation) |
| **Dataset Slice** | `train[:600]` (Train) / `validation[:100]` (Validation) |
| **Optimizer Steps** | 60 |
| **Effective Batch Size** | 8 |
| **Learning Rate** | 0.0002 (Cosine decay schedule) |
| **Base Model Parameters** | 8,054,976,576 |
| **Trainable Parameters** | 39,845,888 |
| **Trainable Share** | 0.49% |
| **Export** | `Merged 16-bit Safetensors` |
| **Final Training Loss** | 0.0977 |
| **Final Validation Loss** | 0.0602 |
| **Best Validation Loss** | 0.0601 |
| **Final Validation Token Accuracy** | 0.9769 |
| **Best Validation Token Accuracy** | 0.9775 |
| **W&B Tracking** | [`fhnw-ch/Apertus`](https://wandb.ai/fhnw-ch/Apertus/runs/jg8hn5o1) / `apertus-1.5-8b-biomedical-ade-qlora-exercise-60steps-20260928-072251` |
