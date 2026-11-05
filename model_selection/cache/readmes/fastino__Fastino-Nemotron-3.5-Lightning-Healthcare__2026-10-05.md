---
license: apache-2.0
base_model: nvidia/Nemotron-3.5-Lightning
tags:
  - healthcare
  - clinical
  - medical-reasoning
  - information-extraction
  - fine-tuned
  - nemotron
  - lightning
  - mixture-of-experts
language:
  - en
pipeline_tag: text-generation
library_name: transformers
---

<div align="center">
  <a href="https://fastino.ai/lp/fastino-nemotron?utm_source=huggingface" target="_blank" rel="noopener noreferrer">
    <img src="Fastino-Nemotron-Healthcare-HF-Banner.png" alt="Fastino Agent - Fine-tune Nemotron with a single prompt" width="100%"/>
  </a>
</div>

[![Fine-tune with Fastino](https://img.shields.io/badge/Fine--tune-Fastino_Agent-EA4335)](https://fastino.ai/waitlist) [![arXiv Paper](https://img.shields.io/badge/arXiv-2604.09791-b31b1b.svg?logo=arxiv)](https://arxiv.org/abs/2604.09791) [![Base model](https://img.shields.io/badge/Base-Nemotron_3.5_Lightning-76B900?logo=nvidia)](https://huggingface.co/nvidia/Nemotron-3.5-Lightning) [![Follow @fastinoAI](https://img.shields.io/twitter/follow/:fastinoAI)](https://x.com/fastinoAI)

# Fastino Nemotron 3.5 Lightning Healthcare

`Fastino-Nemotron-3.5-Lightning-Healthcare` is a 30B-parameter, 3B-active mixture-of-experts model specialized for healthcare and biomedical applications. The repository contains a ready-to-run merged checkpoint: the NVIDIA Nemotron 3.5 Lightning checkpoint released July 29, 2026 plus Fastino's winning combined-healthcare E17b adapter. Users do not need to obtain or attach a separate LoRA.

* **Developed by:** Fastino Labs, in collaboration with NVIDIA
* **Base checkpoint:** NVIDIA Nemotron 3.5 Lightning, July 29, 2026 release
* **Post-training checkpoint:** Fastino-Healthcare
* **License:** Apache 2.0
* **Language:** English
* **Modalities:** Text
* **Model Release Blog:** [Release Blog](https://fastino.ai/blog/fastino-nemotron-3-5-lightning-finance-and-healthcare)
* **Fine-Tuning Agent:** [Private Preview](https://fastino.ai/agent)
* **Research:** [Fastino Fine-Tuning Agent](https://arxiv.org/abs/2604.09791)

## What it is designed for

The model targets clinical and health conversation, biomedical question answering, clinical calculation, medical error detection and correction, biomedical concept extraction, clinical note summarization, and tool-using clinical administration and medical-agent tasks.

## Quickstart

The published weights are BF16 and require about 66 GB before runtime overhead. An 80 GB or larger GPU, or tensor parallelism across multiple GPUs, is recommended.

```bash
pip install "vllm==0.23.0"
```

```python
from vllm import LLM, SamplingParams

model_id = "fastino/Fastino-Nemotron-3.5-Lightning-Healthcare"

llm = LLM(
    model=model_id,
    trust_remote_code=True,
    dtype="bfloat16",
    max_model_len=4096,
)

clinical_note = """65-year-old male with history of hypertension, type 2
diabetes, and CKD stage 3 presents with 2 weeks of progressive dyspnea on
exertion and orthopnea. Exam: bibasilar crackles, 3+ pitting edema to knees,
BP 152/94. Meds: lisinopril 20 mg daily, furosemide 40 mg daily. CXR:
cardiomegaly with pulmonary congestion. Assessment: acute decompensated
heart failure."""

messages = [
    {
        "role": "system",
        "content": "You are a clinical documentation assistant. Summarize notes accurately and concisely. Do not add information that is not in the note.",
    },
    {
        "role": "user",
        "content": f"Summarize the following clinical note in 3-5 bullet points:\n\n{clinical_note}",
    },
]

outputs = llm.chat(
    messages,
    SamplingParams(temperature=0.0, max_tokens=512),
)
print(outputs[0].outputs[0].text)
```

## Post-training recipe

The Fastino Fine-Tuning Agent autonomously built evaluation sets, curated data, explored training mixtures and hyperparameters, recovered failed experiments, evaluated transfer, and selected the final checkpoint.

The winning adapter was trained on 72,358 de-duplicated examples covering:

* general healthcare instruction following and physician-style health conversations;
* biomedical question answering and clinical calculation;
* medical error detection and correction;
* clinical dialogue summarization and note generation;
* biomedical concept, chemical, and disease extraction;
* clinical administration and browser-based tool-use trajectories; and
* medical-agent task trajectories.

The final balanced mixture modestly upweighted difficult HealthBench-style examples while preserving broad healthcare, biomedical extraction, and newer agent-task coverage. It was trained from the base checkpoint for two epochs with LoRA rank 64, learning rate `1.5e-4`, batch size 32, and sequence packing disabled. Evaluation, development, and blind rows and their labels were excluded from training.

## Benchmark evaluation

Base and fine-tuned scores below use the same July 29 checkpoint, inputs, prompts, decoding settings, inference route, and evaluator for each row.

### In-domain benchmarks

| Benchmark | Evaluation scope | July 29 base | Fastino-Healthcare | Change |
| --- | --- | ---: | ---: | ---: |
| HealthBench Pro | blind, n=180 | 26.83% | 32.64% | +5.80 pp |
| HealthAdminBench | blind | 25.67% | 29.95% | +4.28 pp |
| MedAgent public v1/v2, Overall SR | blind, n=150 | 36.00% | 40.00% | +4.00 pp |
| HealthBench Core | blind, n=700 | 49.67% | 56.21% | +6.54 pp |
| PubMedQA | matched, n=500 | 59.00% | 65.00% | +6.00 pp |
| MedCalc | matched, n=275 | 49.09% | 54.18% | +5.09 pp |
| MEDEC, flag accuracy | matched, n=574 | 53.66% | 64.98% | +11.32 pp |
| MEDEC, sentence accuracy | matched, n=574 | 48.08% | 62.89% | +14.81 pp |
| MedMentions ST21pv | matched, n=878 | 19.74% | 40.30% | +20.55 pp |
| BC5CDR | matched, n=500 | 47.92% | 72.51% | +24.59 pp |

HealthAdminBench used Task Description plus Portal Guidance with the accessibility-tree observation mode. MedAgent reports Overall Success Rate. MEDEC flag and sentence accuracy are reported separately.

### Transfer to unseen benchmarks
Performance on related tasks the model was not explicitly trained for.

| Benchmark | Evaluation scope | July 29 base | Fastino-Healthcare | Change |
| --- | --- | ---: | ---: | ---: |
| EkaCare | transfer, n=1,066 | 12.95% | 32.83% | +19.88 pp |
| BC5CDR to BioRED | transfer, n=66 | 25.92% | 41.77% | +15.85 pp |

## Evaluation protocol

The agent used development evaluations for experiment selection and a separately frozen blind lane for final characterization. Score-bearing comparisons were accepted only when base and candidate shared the same examples, prompt construction, decoding parameters, serving route, evaluator identity, and aggregation. Training mixtures were hashed and benchmark evaluation rows were excluded from training.

## Limitations

This is a specialized research model, not a medical device. Its outputs are not a substitute for professional clinical judgment. Clinical or other high-stakes deployment requires independent validation, appropriate safeguards, and qualified human oversight.

## Fine-tuning

To fine-tune or serve models like this one without managing GPUs, see the [Fastino API](https://fastino.ai), which offers hosted training and inference.

## Citation

```bibtex
@misc{atreja2026pioneeragentcontinualimprovement,
      title={Pioneer Agent: Continual Improvement of Small Language Models in Production},
      author={Dhruv Atreja and Julia White and Nikhil Nayak and Kelton Zhang and Henrijs Princis and George Hurn-Maloney and Ash Lewis and Urchade Zaratiana},
      year={2026},
      eprint={2604.09791},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2604.09791},
}
```

## License

This model is licensed under the Apache License 2.0.

## Links

* [Fastino Labs](https://fastino.ai/)
* [Fine-Tuning Agent private preview](https://fastino.ai/agent)
* [Supporting research](https://arxiv.org/abs/2604.09791)
* [NVIDIA Nemotron 3.5 Lightning base model](https://huggingface.co/nvidia/Nemotron-3.5-Lightning)
