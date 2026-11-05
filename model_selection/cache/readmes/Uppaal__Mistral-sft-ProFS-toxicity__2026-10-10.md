---
library_name: transformers
tags:
- generation
- safety
- model-editing
- editing
- activation-steering
- activation-editing
- dpo
- rlhf
- profs
- detox
- toxicity
- iclr
- iclr2025
license: mit
language:
- en
base_model:
- HuggingFaceH4/mistral-7b-sft-beta
---

<p align="center">
  <a href="https://arxiv.org/abs/2405.13967">
    <img src="https://img.shields.io/badge/arXiv-2405.13967-B31B1B?logo=arxiv&logoColor=white" alt="arXiv">
  </a>
  <a href="https://uppaal.github.io/projects/profs/profs.html">
    <img src="https://img.shields.io/badge/Project_Webpage-1DA1F2?logo=google-chrome&logoColor=white&color=0A4D8C" alt="Project Webpage">
  </a>
  <a href="https://github.com/Uppaal/detox-edit">
    <img src="https://img.shields.io/badge/Code-F1C232?logo=github&logoColor=white&color=black" alt="Checkpoints">
  </a>
</p>


# ProFS Editing for Safety

This model is an edited version of [`HuggingFaceH4/mistral-7b-sft-beta`](https://huggingface.co/HuggingFaceH4/mistral-7b-sft-beta).
Editing is applied through ProFS, to reduce toxicity.

ProFS (Projection Filter for Subspaces) is a tuning-free alignment method that removes undesired behaviors by identifying and projecting out harmful subspaces in model weights.
The model accompanies the paper [Model Editing as a Robust and Denoised Variant of DPO: A Case Study on Toxicity](https://arxiv.org/abs/2405.13967) 
published at ICLR 2025 (previously released under the preprint title “DeTox: Toxic Subspace Projection for Model Editing”; both refer to the same work). 


**Key Features:**

- Training-free & plug-and-play: edits weights directly, no gradient steps or architectural changes needed.
- Data-efficient: achieves strong alignment effects using only hundreds (not thousands) of preference pairs.
- Label-robust: maintains performance even under substantial label noise, since projection directions remain stable.
- Fast & lightweight: produces an edited model that runs at the same inference speed as the base model.
- Theoretically grounded: shown to be a denoised, single-step approximation of Direct Preference Optimization (DPO)—bridging editing-based and tuning-based alignment.

<div align="center">
<img src="ProFS Method.png" width="950">
<i><b>Figure.</b> Schematic of ProFS (previously called DeTox). Toxic directions (in red) are projected out of the model’s MLP-value matrices, leaving other representational directions intact. </i>
</div>




## Model Details

- **Model type:** Edited Causal Language Model (LLM)
- **Base model:** [`HuggingFaceH4/mistral-7b-sft-beta`](https://huggingface.co/HuggingFaceH4/mistral-7b-sft-beta)  
- **Language(s) (NLP):** English
- **License:** MIT
- **Repository:** [GitHub](https://github.com/Uppaal/detox-edit)
- **Paper:** [Model Editing as a Robust and Denoised variant of DPO: A Case Study on Toxicity](https://arxiv.org/abs/2405.13967)

## Uses

### Direct Use
ProFS-edited GPT-2 can be used for:
- Safe text generation and alignment research  
- Studying lightweight alignment via model editing rather than fine-tuning  
- Interpretability studies of activation subspaces and toxicity directions

### Downstream Use
ProFS serves as a reproducible starting point for work on:
- Safety alignment without gradient updates  
- Robustness to label noise and limited data regimes  
- Educational demonstrations of representation-level interventions

### Out-of-Scope Use
Not a fully aligned conversational model.  
Not evaluated for fairness or demographic bias beyond toxicity.



## How to Get Started with the Model

Use the code below to get started with the model.

```
from transformers import AutoTokenizer, AutoModelForCausalLM
model_id = "Uppaal/Mistral-sft-ProFS-toxicity"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

prompt = "The internet has changed the way people communicate by"
out = model.generate(**tokenizer(prompt, return_tensors="pt"), max_new_tokens=20)
print(tokenizer.decode(out[0], skip_special_tokens=True))
```



## Training (Editing) Details

### Data
We use the pairwise toxicity preference dataset introduced by [Lee et al. (2024)](https://arxiv.org/abs/2401.01967).

- Non-toxic sequences: sampled from WikiText-2.
- Toxic counterparts: generated using the Plug-and-Play Language Model (PPLM) method to inject toxic content.
- Data format: (toxic, non-toxic) sentence pairs.
- Sample size: 500 pairs for ProFS editing (compared to 2,000 pairs used for DPO fine-tuning).

### Preprocessing

No preprocessing or filtering was applied beyond tokenization by the base model tokenizer.

### Editing Hyperparameters

- Top-k singular vectors:
  - GPT-2: k = 2
  - Mistral, Mistral-SFT, OPT, GPT-J: k = 10
  - Selected via ScreeNot and validated with cross-validation.
- Edited layers:
  - GPT-2 / GPT-J: layers 11–24
  - Mistral, Mistral-SFT, OPT: layers 15–L
- Projection step: edit applied once to the MLP-Value matrices only.
- Centering: mean vector of non-toxic embeddings removed before SVD to preserve syntactic knowledge.



## Evaluation

### Metrics and Testing Data

- Perplexity (fluency): evaluated on the WikiText-2 dev split.
- Toxicity: measured on the [Real Toxicity Prompts](https://huggingface.co/datasets/allenai/real-toxicity-prompts) challenge subset. Scored using [Detoxify](https://github.com/unitaryai/detoxify). Lower Detoxify score = lower toxicity.
- Capability (for larger models): zero-shot accuracy across 7 EleutherAI LM Harness tasks: BoolQ, RTE, HellaSwag, WinoGrande, ARC-Easy, ARC-Challenge, and OpenBookQA.

### Results
| **Model** | **Method** | **Toxicity ↓** | **Perplexity ↓** | **Capability ↑** |
|:-----------|:------------|:---------------|:-----------------|:-----------------|
| **GPT-2 Medium** | Original | 48.00 (0.00) | 29.70 (0.00) | – |
|  | DPO | 36.36 (0.58) | 29.86 (0.22) | – |
|  | **ProFS** | **26.83 (0.89)** | 32.50 (0.28) | – |
| **Mistral 7B** | Original | 42.45 (0.00) | 7.49 (0.00) | 64.23 |
|  | DPO | 36.42 (0.62) | 7.52 (0.26) | 65.32 |
|  | **ProFS** | **30.40 (0.71)** | 7.99 (0.21) | 63.59 |
| **Mistral-SFT 7B** | Original | 33.45 (0.00) | 8.22 (0.00) | 63.59 |
|  | DPO | 23.96 (0.50) | 8.38 (0.34) | 63.66 |
|  | **ProFS** | **26.03 (1.25)** | 8.83 (0.57) | 63.23 |
| **OPT 6.7B** | Original | 46.47 (0.00) | 14.67 (0.00) | 51.57 |
|  | DPO | 45.31 (0.74) | 14.37 (0.61) | 51.55 |
|  | **ProFS** | **43.49 (1.38)** | 13.83 (0.46) | 51.80 |
| **GPT-J 6B** | Original | 45.31 (0.00) | 13.24 (0.00) | 51.92 |
|  | DPO | 43.67 (1.11) | 13.96 (0.53) | 52.46 |
|  | **ProFS** | **37.36 (2.28)** | 14.53 (0.30) | 52.48 |
## Citation

**BibTeX:**

@inproceedings{uppaalmodel,
  title={Model Editing as a Robust and Denoised variant of DPO: A Case Study on Toxicity},
  author={Uppaal, Rheeya and Dey, Apratim and He, Yiting and Zhong, Yiqiao and Hu, Junjie},
  booktitle={The Thirteenth International Conference on Learning Representations}
}

**APA:**

Uppaal, R., Dey, A., He, Y., Zhong, Y., & Hu, J. Model Editing as a Robust and Denoised variant of DPO: A Case Study on Toxicity. In The Thirteenth International Conference on Learning Representations.