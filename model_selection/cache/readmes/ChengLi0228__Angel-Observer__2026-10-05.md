---
license: apache-2.0
base_model: Qwen/Qwen3-8B
base_model_relation: finetune
library_name: transformers
pipeline_tag: text-generation
language:
- en
tags:
- mental-health
- user-simulation
- patient-simulation
- psychotherapy
- network-model
- grpo
- qwen3
---

# Angel-Observer

**Angel-Observer** reads a patient's presenting complaints and builds a
**directed symptom network** (a *Network Model*): the thoughts, emotions,
behaviors, bodily sensations and events in the case, and which ones set off
which. It is stage 1 of **Angel**, a two-stage simulator of psychotherapy
patients; [Angel-Actor](https://huggingface.co/ChengLi0228/Angel-Actor) then
role-plays the patient.

🎮 **[Live demo](https://eval.angel-simulation.org/demo)** · 💻 **[Code: ANGEL-UserSim](https://github.com/Scarelette/ANGEL-UserSim)** · 🎭 **[Angel-Actor](https://huggingface.co/ChengLi0228/Angel-Actor)**

```
short description ──► Angel-Observer ──► long profile + symptom network ──► Angel-Actor ──► patient replies
```

## What it does

One checkpoint answers two prompts:

| Step | Input | Output |
|---|---|---|
| **S1: nodes** | presenting complaints | `<think>…</think><GRAPH>{"symptoms": [...], "external_factors": [...]}</GRAPH>` |
| **S2: edges** | complaints + the S1 nodes | `<think>…</think><GRAPH>{"links": [{"from": ..., "to": ...}]}</GRAPH>` |

In the Angel pipeline it also expands a short patient description into a
detailed long profile for the Actor.

## How to use

The system prompts the model was trained on are in the code repository, so
the easiest way is through it:

```bash
git clone https://github.com/Scarelette/ANGEL-UserSim.git && cd ANGEL-UserSim
pip install -r model_training/observer/requirements-observer.txt

# one symptom network per case (JSONL with a "Complaints" field)
python -m model_training.observer.predict_network \
    --input data/examples/observer/case_reports.jsonl --output networks.jsonl
```

The model is downloaded from this page on first use. From Python:

```python
from model_training.observer.predict_network import load_observer, predict_network

tokenizer, model = load_observer("ChengLi0228/Angel-Observer")
net = predict_network(tokenizer, model, "Alex, 29, reports three months of low mood, "
                      "poor sleep and withdrawing from friends after being laid off ...")
print(net["symptoms"])
print(net["graph"])   # [{"from": "being laid off", "to": "low mood"}, ...]
```

For the full Angel patient (Observer + Actor) see
[`model_usage/`](https://github.com/Scarelette/ANGEL-UserSim/tree/main/model_usage).
It uses the Qwen3 chat template, sampling with temperature 0.1 and top-p 0.9,
and a bf16 model needs about 17 GB of GPU memory.

## Training

Qwen3-8B, fine-tuned in four stages (QLoRA adapters on a 4-bit copy, each
merged back in bf16):

| Stage | Data | Settings |
|---|---|---|
| SFT, S1 (nodes) | 5,599 rows | LoRA r=64 / α=16, lr 1e-4, 3 epochs |
| GRPO, S1 | 5,089 prompts, 600 steps | reward 0.4 · format + 0.6 · node recall (MiniLM cosine ≥ 0.75 against reference nodes) |
| SFT, S2 (edges) | 2,138 rows | LoRA r=64 / α=16, lr 1e-4, 3 epochs |
| GRPO, S2 | 800 steps | reward 0.1 · format + 0.6 · edge precision + 0.3 · node coverage − size penalty; edges scored by a gpt-5-mini judge |

The training data were built with GPT-5 from 510 of the 516 published
psychotherapy case reports in **PSYCHE**, our graph-grounded dataset for
psychological user simulation (release coming soon). The case reports are
copyrighted and are not redistributed. Full recipe:
[`model_training/observer/`](https://github.com/Scarelette/ANGEL-UserSim/tree/main/model_training/observer).

## Intended use and limitations

- **Research use** in user simulation, for example generating varied,
  structured patient cases to train or evaluate therapy-support systems and
  clinicians-in-training.
- **Not a diagnostic or clinical tool.** The networks are the model's
  reading of a text, not clinical assessments, and they can be wrong,
  incomplete or reflect biases in the source case reports.
- Trained on English case-report language; other languages and very
  different writing styles are untested.
- Case material can involve self-harm, suicidality, trauma and substance
  use, so the model's outputs can too.

## Citation

Coming soon.
