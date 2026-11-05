---
license: apache-2.0
language:
- en
library_name: transformers
pipeline_tag: text-generation
tags:
- medical
- clinical
- healthcare
- meditron
- fully-open
- medical-llm
base_model: swiss-ai/Apertus-70B-Instruct-2509
base_model_relation: finetune
datasets:
- EPFLiGHT/fully-open-meditron
---

# Apertus-70B-MeditronFO

<div align="center">
<img src=https://raw.githubusercontent.com/EPFLiGHT/MeditronFO/3caab22b7efaf9e56e2894bac65dab6d3a31aaa0/static/images/MeditronFO-logo-cube.png width="15%"/>
</div>
<p align="center">
    👋 Join our <a href="https://www.light-laboratory.org/" target="_blank">LiGHT</a> community.
    <br>
    📖 Check out the MeditronFO <a href="https://epflight.github.io/MeditronFO/" target="_blank">blog</a> and MeditronFO <a href="https://arxiv.org/abs/2605.16215" target="_blank">preprint</a>.
    <br>
    🔜 If you are a clinician join the MOOVE initiative <a href="https://jointhemoove.org/">here</a>.  
</p>

<p align="center">
    [<a href="https://huggingface.co/collections/EPFLiGHT/meditronfo" target="_blank">Hugging Face</a>]
    [<a href="https://arxiv.org/abs/2605.16215" target="_blank">Preprint</a>] 
    [<a href="https://github.com/EPFLiGHT/FullyOpenMeditron" target="_blank">GitHub</a>]
    [<a href="https://huggingface.co/datasets/EPFLiGHT/fully-open-meditron" target="_blank">Dataset</a>]
    <br>
    <b>License</b>: <a href="https://www.apache.org/licenses/LICENSE-2.0.txt" target="_blank">Apache 2.0</a> | <b>Authors</b>: <a href="https://www.light-laboratory.org/" target="_blank">LiGHT</a>
</p>

> [!Note]
> We're introducing Apertus-70B-MeditronFO, our latest flagship medical specialist LLM, medical specialization of [Apertus-70B-Instruct](https://huggingface.co/swiss-ai/Apertus-70B-Instruct-2509) on the [Fully Open Meditron Corpus](https://huggingface.co/datasets/EPFLiGHT/fully-open-meditron). This model is part of the **Fully Open Meditron** family — the first end-to-end auditable pipeline for clinical LLMs, with open weights, open data, open training recipe, and clinician-vetted corpus construction.


- **Part of the Fully Open Meditron family:** End to end fully open clinical LLMs
- **Establishes a new state of the art:** Best medical accuracy on medical benchmarks among fully open medical LLMs
- **Is prefered over Apertus-70B in 85.3% of comparisons:** Comparison on the clinician validated LM judge evaluation AutoMOOVE.

<div align="center">
<img src=https://raw.githubusercontent.com/EPFLiGHT/MeditronFO/3caab22b7efaf9e56e2894bac65dab6d3a31aaa0/static/images/plot_fig1_healthbench_timeline_easy_color.png width="100%"/>
</div>

## Benchmark

Accuracy (%) on standard medical benchmarks. See the paper for full evaluation details, confidence intervals, and open-ended Auto-MOOVE results.

| Benchmark | Apertus-70B-Instruct | **Apertus-70B-MeditronFO** | Δ |
|---|---:|---:|---:|
| MedMCQA | 52.43 | **56.32** | +3.89 |
| MedQA | 60.64 | **68.58** | +7.94 |
| PubMedQA | 66.80 | **75.20** | +8.40 |
| MedXpertQA | 12.33 | **16.90** | +4.57 |
| HealthBench Hard | 32.28 | **40.14** | +7.86 |
| **Average** | 44.90 | **51.43** | +6.53 |

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "EPFLiGHT/Apertus-70B-MeditronFO"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

messages = [
    {"role": "user", "content": "A 62-year-old woman presents with a three-day history of dyspnea on exertion and a productive cough. What is the differential diagnosis?"},
]
inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
).to(model.device)

outputs = model.generate(**inputs, max_new_tokens=512, do_sample=False)
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

## Training

- **Base model:** [Apertus-70B-Instruct](https://huggingface.co/swiss-ai/Apertus-70B-Instruct-2509)
- **Corpus:** [Fully Open Meditron](https://huggingface.co/datasets/EPFLiGHT/fully-open-meditron) 601k examples (~150M tokens), aggregating eight public medical QA datasets with three clinician-vetted synthetic components: exam-style QA, guideline-grounded QA from 46,469 clinical practice guidelines, and open-ended clinical vignettes
- **Hardware:** 8 NVIDIA GH200 nodes
- **Framework:** Axolotl with FSDP v2 / DeepSpeed ZeRO-3, Flash Attention 2, bf16 mixed precision
- **Decontamination:** System-wide two-stage n-gram and token-alignment decontamination against all evaluation benchmarks

Full hyperparameters are in Appendix I of the paper.

## Compute & footprint
The training was done on 8 nodes of 4 NVIDIA GH200 GPUs for approximately 6 hours on the CSCS Swiss National Supercomputing Centre. 
Our trainings have a carbon neutral footprint as the CSCS data center is carbon neutral ([CSCS energy efficiency](https://ethz.ch/en/news-and-events/eth-news/news/2022/11/at-cscs-energy-efficiency-is-a-key-priority-even-at-high-performance.html)).

## Limitations & intended use

MeditronFO can produce text on a variety of topics, but the generated content may not always be factually accurate, logically consistent, or free from biases present in the training data. MeditronFO has been trained to be specialised for Medicine and is intended to be used for Medicine related tasks evaluation. These models should be used as assistive tools rather than definitive sources of information. Users should always verify important information and critically evaluate any generated content.

## Citation

If you find MeditronFO useful in your research, please cite our preprint:

```bibtex
@misc{theimerlienhard2026fullyopenmeditronauditable,
  title         = {Fully Open Meditron: An Auditable Pipeline for Clinical LLMs},
  author        = {Xavier Theimer-Lienhard and Mushtaha El-Amin and Fay Elhassan and Sahaj Vaidya and Victor Cartier-Negadi and David Sasu and Lars Klein and Mary-Anne Hartley},
  year          = {2026},
  eprint        = {2605.16215},
  archivePrefix = {arXiv},
  primaryClass  = {cs.AI},
  url           = {https://arxiv.org/abs/2605.16215}
}
```

## Acknowledgments and Disclosure of Funding
This work was supported under project ID #27 as part of the Swiss AI Initiative, through a grant from the ETH Domain and computational resources provided by the Swiss National Supercomputing Centre (CSCS) under the Alps infrastructure.
We thank the physician review panel within the LiGHT laboratory for their clinical auditing, methodological review, and validation of the synthetic generation and evaluation pipelines. We additionally thank the many physicians and clinical experts who contributed to the MOOVE initiative through expert review, pairwise evaluation, benchmarking, and clinical vignette development across diverse international settings.

## Contact
Please use the community tab for any discussions or issue related to this model.
Questions related to the project can be sent to xavier.theimer-lienhard@epfl.ch or mary-anne.hartley@epfl.ch.