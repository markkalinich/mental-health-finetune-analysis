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
- role-play
- dpo
- qwen3
---

# Angel-Actor

**Angel-Actor** role-plays a **psychotherapy patient** across a multi-turn
conversation. You are the therapist; it answers in character, keeps some
things back, and opens up gradually. It is stage 2 of **Angel**, a two-stage
simulator of psychotherapy patients:
[Angel-Observer](https://huggingface.co/ChengLi0228/Angel-Observer) first
turns a short patient description into a detailed profile and symptom
network, and the Actor plays that patient.

🎮 **[Live demo: talk to a patient](https://eval.angel-simulation.org/demo)** · 💻 **[Code: ANGEL-UserSim](https://github.com/Scarelette/ANGEL-UserSim)** · 🕸️ **[Angel-Observer](https://huggingface.co/ChengLi0228/Angel-Observer)**

```
short description ──► Angel-Observer ──► long profile + symptom network ──► Angel-Actor ──► patient replies
```

## How to use

The quickest way is the [live demo](https://eval.angel-simulation.org/demo).
To run it yourself, use the code repository, which builds the patient prompt
from a profile and downloads both models from Hugging Face on first use:

```bash
git clone https://github.com/Scarelette/ANGEL-UserSim.git && cd ANGEL-UserSim
pip install -r model_usage/requirements-usage.txt
python -m model_usage.angel chat --short-profile-file model_usage/examples/example_short_profile.txt
```

From Python:

```python
from model_usage.angel import AngelModel

with AngelModel() as model:
    note = open("model_usage/examples/example_short_profile.txt").read()
    print(model.send("me", "Hi, what brings you in today?", short_profile=note)["reply"])
    print(model.send("me", "How long has that been going on?")["reply"])
```

Both models together need a GPU with about 40 GB. Details:
[`model_usage/`](https://github.com/Scarelette/ANGEL-UserSim/tree/main/model_usage).

**Output format.** The patient's description goes in the system prompt, and
therapist turns are `user` turns. Each reply has two parts:
`<state>…</state>` is the patient's inner state (hidden from the therapist)
and `<word>…</word>` is what the patient says. `model_usage` shows only the
`<word>` part. Use the Qwen3 chat template with thinking off
(`enable_thinking=False`).

## Training

Qwen3-8B, trained in two stages on synthetic therapy conversations:

| Stage | Data | Settings |
|---|---|---|
| SFT (QLoRA) | 423 conversations between a prompted Qwen3-30B-A3B patient and an LLM therapist | LoRA r=64 / α=16, lr 1e-4, 5 epochs, loss on patient turns |
| DPO | 6,901 preference pairs: at each turn the SFT model sampled up to 5 replies and a Claude judge picked the best and worst | LoRA r=16 / α=32, lr 2e-6, β 0.1, 2 epochs; reference = the SFT model |

Each conversation followed a symptom network from Angel-Observer in which
part of the network was **masked**: those mechanisms start out unrecognised
by the patient and surface as the conversation goes on. The networks come
from **PSYCHE**, our graph-grounded dataset for psychological user
simulation (release coming soon). The judge scored replies on safety,
structure, specificity, state alignment, consistency with the history,
progress and naturalness. Full recipe:
[`model_training/actor/`](https://github.com/Scarelette/ANGEL-UserSim/tree/main/model_training/actor).

## Intended use and limitations

- **Research use**: simulated patients for training and evaluating
  therapy-support systems, and for practice by clinicians-in-training.
- **Not therapy, and not a real person.** It is a simulation and can break
  character, contradict its profile or behave unlike a real patient. Asking
  it to summarise the session, give advice or plan the next session tends to
  pull it out of role.
- **Sensitive content.** By design it portrays depression, anxiety, trauma,
  substance use and passive suicidal thoughts. Its training prompts keep
  suicidality passive and vague (no intent, plans or methods), but outputs
  are not guaranteed to follow that. Use appropriate safeguards and don't
  expose it to vulnerable users as if it were a support tool.
- English only.

## Citation

Coming soon.
