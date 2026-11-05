---
base_model: andreasmartin/apertus-v1.5-8b-text
library_name: transformers
pipeline_tag: text-generation
license: apache-2.0
language:
- en
tags:
- unsloth
- safetensors
- text-generation
- apertus
- biomedical
- adverse-drug-events
- named-entity-recognition
datasets:
- mihirhirave/entity_extraction_ade_v2_with_validation
---

# Apertus 1.5 8B — Standalone Merged Model (BIOMEDICAL_ADE)

> ⚠️ **CRITICAL DISCLAIMER: HIGHLY EXPERIMENTAL RESEARCH MODEL**  
> This model is a **proof-of-concept research artifact** developed exclusively for academic experimentation, demonstration, and benchmarking purposes.  
> - **NOT FOR CLINICAL USE**: This system is **NOT** a certified medical device and must **NEVER** be used to provide medical advice, diagnosis, triage, or clinical decision support.  
> - **INCORRECT OR INCOMPLETE OUTPUT**: The outputs may omit severe drug reactions or state side effects that do not exist. Always rely on certified clinical pharmacologists and authorized medical references. 
> - The authors and contributors assume no liability for any direct or indirect damages resulting from the use or misuse of this model.

Fine-tuned from [`andreasmartin/apertus-v1.5-8b-text`](https://huggingface.co/andreasmartin/apertus-v1.5-8b-text) on [`mihirhirave/entity_extraction_ade_v2_with_validation`](https://huggingface.co/datasets/mihirhirave/entity_extraction_ade_v2_with_validation).

This repository contains the **complete, standalone unquantized 16-bit merged model** (`merged_16bit`), fully ready for conversion to GGUF (via **GGUF My Repo** or **llama.cpp**) and direct serving via **vLLM**.

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

### Example 2: Negative Control (No Adverse Effects)
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

## Quickstart (vLLM / Transformers / Ollama)

### Direct Ingestion with vLLM
```bash
vllm serve andreasmartin/apertus-1.5-8b-biomedical-ade --tensor-parallel-size 1 --gpu-memory-utilization 0.9
```

### Direct Python Ingestion
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("andreasmartin/apertus-1.5-8b-biomedical-ade")
model = AutoModelForCausalLM.from_pretrained("andreasmartin/apertus-1.5-8b-biomedical-ade", device_map="auto")
```

## Training Configuration & Metrics

| Parameter | Value |
| :--- | :--- |
| **Base Model** | [`andreasmartin/apertus-v1.5-8b-text`](https://huggingface.co/andreasmartin/apertus-v1.5-8b-text) |
| **Dataset** | [`mihirhirave/entity_extraction_ade_v2_with_validation`](https://huggingface.co/datasets/mihirhirave/entity_extraction_ade_v2_with_validation) |
| **Dataset Slice** | `train[:600]` (Train) / `validation[:100]` (Validation) |
| **Optimizer Steps** | 60 |
| **Effective Batch Size** | 4 (Per-device batch size 2 x Gradient Accumulation 2) |
| **Learning Rate** | 0.0002 (Cosine decay schedule) |
| **Merge Method** | `merged_16bit` (Standalone 16-bit Safetensors) |
| **Final Training Loss** | nan |
