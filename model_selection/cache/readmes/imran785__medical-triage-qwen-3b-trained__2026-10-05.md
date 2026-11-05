---
license: apache-2.0
library_name: transformers
base_model: unsloth/Qwen2.5-3B-Instruct-bnb-4bit
tags:
- medical
- triage
- reinforcement-learning
- sft
- unsloth
- qwen2
---


# 🏥 Medical Triage RL: Training Decisive Diagnostic Agents

> Teaching LLMs to think like doctors through Reinforcement Learning

[![HuggingFace Space](https://img.shields.io/badge/🤗_Space-Live_Environment-blue)](https://huggingface.co/spaces/imran785/medical-triage-rl-env)
[![HuggingFace Model](https://img.shields.io/badge/🤗_Model-Trained_Agent-green)](https://huggingface.co/imran785/medical-triage-qwen-3b)
[![Colab](https://img.shields.io/badge/Colab-Training_Notebook-orange)](https://colab.research.google.com/drive/1zpy1oKgOhQA6MDP1ISbadbuOXjkeqgTA?usp=sharing)

---

## The Problem

Most LLMs today are trained to be helpful conversational assistants. In a medical triage room, being chatty can cost lives.

A real doctor needs to:
- Ask the **right questions** — not all of them
- Order **targeted tests** — not expensive ones randomly
- Reach a **confident diagnosis** — fast and efficiently

**Current LLMs fail at all three.**

Give a base LLM a patient complaint and it responds with:

> *"I'm sorry you're feeling this way. Chest pain can be serious. You should see a doctor. Would you like a list of symptoms to watch for?"*

This project uses Reinforcement Learning to transform a general-purpose LLM into a Triage Agent that understands the **Value of Information** — learning exactly which question to ask next and when to stop.

---

## The Environment: Medical-Triage-v1

Built on the **OpenEnv framework**, the environment simulates a hospital triage room with real patient cases.

### How It Works

```
reset() → New patient arrives with chief complaint
          Agent sees: "I have chest pain and shortness of breath"

step()  → Agent takes one of 3 actions:
          ask_symptom: fever      → "yes, 102F"
          order_test: chest_xray  → "right lower lobe infiltrate"
          give_diagnosis: pneumonia → episode ends → reward computed

state() → Returns current known symptoms, tests ordered, actions taken
```

### Agent Actions

| Action | What It Does | Cost |
|--------|-------------|------|
| `ask_symptom` | Queries a symptom from the patient | Free |
| `order_test` | Orders a medical test | 1-5 points deducted |
| `give_diagnosis` | Submits final diagnosis and ends episode | Triggers scoring |

### Patient Cases

- **50 patient cases** across 10 medical conditions
- Conditions: pneumonia, appendicitis, migraine, diabetes crisis, heart attack, anemia, UTI, asthma attack, dehydration, anxiety attack
- **3 difficulty levels**: easy / medium / hard
- Each case has available symptoms, tests with costs, and red herrings

### Reward Rubric (4 Components)

```
diagnosis_correct:  +10   Did the agent get the right answer?
efficiency_score:   +5    Did it avoid expensive unnecessary tests?
speed_score:        +3    Did it decide within few actions?
process_score:      +5    Did it ask smart relevant symptoms?

TOTAL MAX:          +23
BASELINE (random):   -4
```

### Anti-Gaming Rules

The environment is designed so agents cannot exploit the reward:

- Agent cannot call `give_diagnosis` before taking at least 2 actions
- Maximum 10 actions per episode — forced termination with penalty
- Repeated identical actions return a penalty of -1
- Invalid action format gives -2 penalty
- Rush penalty: diagnosing before step 2 gives an additional -3 penalty

---

## The Reward Design Philosophy

We use **composable rubrics** instead of a single reward signal. This is deliberate — multiple independent reward functions are harder to game and teach specific behaviors:

```
Single reward (0/1):       Model learns to guess correctly
                           but does not care HOW it gets there

Our 4-component rubric:    Model learns to gather evidence first,
                           avoid expensive tests,
                           be fast AND accurate simultaneously
```

The **Urgency Bonus** rewards identifying life-threatening conditions (heart attack, meningitis) in fewer steps — teaching the agent to prioritize high-risk patients exactly as real triage does.

The **Hallucination Penalty** (-10) fires when an agent orders a test that does not exist in the patient's available tests — directly penalizing medical hallucination, one of the most dangerous LLM failure modes.

---

## Training Results

### Reward Plot

![Training Results](download%20(1).png)



### Before vs After Training

| Feature | Base Model (Untrained) | Trained RL Agent |
|---------|----------------------|-----------------|
| Avg Reward | -4.0 | +5.7 (rolling avg) |
| Peak Reward | -1.0 | **+19.0** (near maximum of 23) |
| Bad Actions per Episode | 5 | **0** |
| Symptoms Asked | 0-2 (random) | 4-5 (systematic) |
| Diagnosis Accuracy | 0% | ~20% |
| Output Style | Conversational paragraphs | Structured thinking + actions |
| Decision Making | Hesitant, generic advice | Decisive, evidence-based |
| Cost Awareness | Random test ordering | Prioritizes high-impact tests first |

### Key Evidence of Learning

**Behavioral change is the strongest evidence:**

```
BEFORE (Episode 0):
Patient: "I have chest pain and shortness of breath with fever"
Agent:   [bad action] → [bad action] → [guess: anxiety]
Result:  reward -4, 5 invalid actions, 0 symptoms asked

AFTER (Episode 185):
Patient: "I have chest pain and shortness of breath with fever"
Agent:   ask_symptom: cough             → "productive cough 3 days"
         ask_symptom: fever             → "yes, 102F"
         ask_symptom: shortness_of_breath → "worse on exertion"
         order_test: chest_xray         → "right lower lobe infiltrate"
         give_diagnosis: pneumonia      ✓ CORRECT
Result:  reward +19, 0 invalid actions, 4 relevant symptoms asked
```

**Quantitative improvements:**
- Bad actions: **5 → 0** per episode
- Peak reward: **-1 → +19** (near maximum possible)
- Rolling average: **consistently above baseline** throughout training
- Model hit maximum reward of **19+ in episodes 30, 60, 115, 185**

### Training Curve Interpretation

The green spikes represent perfect diagnoses where the agent identified the correct condition through systematic investigation. The rolling average staying above zero throughout training confirms the model genuinely learned the task rather than getting lucky.

---

## Real World Scenario: Chest Pain Patient

**Base Model Response:**
```
"I'm sorry you're feeling this. Chest pain is serious.
You should go to the ER or call a doctor immediately.
Would you like a list of symptoms to watch for?"

Result: FAIL — wasted critical time with conversation.
        No diagnosis. No tests. No action.
```

**Trained RL Agent Response:**
```
<thinking>
Patient presents with chest pain. Need to rule out
cardiac event. Check radiation pattern and associated symptoms.
</thinking>
<action>ask_symptom: radiation_to_arm</action>

Result: "yes, left arm pain"

<thinking>
Left arm radiation + chest pain = high MI probability.
Order EKG immediately.
</thinking>
<action>order_test: ecg</action>

Result: "ST elevation detected"

<action>give_diagnosis: heart_attack</action>

Result: CORRECT — identified life-threatening condition
        in 3 steps. Reward: +19
```

---

## Technical Architecture

### Stack

```
Environment:  OpenEnv framework (FastAPI + Docker)
Model:        Qwen2.5-3B-Instruct (LoRA fine-tuned, rank 16)
Training:     GRPO-style reward weighted policy gradient
Efficiency:   Unsloth 4-bit quantization
Platform:     Google Colab T4 GPU
Episodes:     200 training episodes
```

### Engineering Highlights

**VRAM Management on Free T4:**

Implemented aggressive memory management to run RL training on a 15.6GB T4 GPU with a 3B parameter model:
- Activation clearing after each generation step
- Gradient checkpointing via Unsloth
- Sequential loss computation instead of batched
- 4-bit quantization with LoRA rank 16

**Prompt Engineering:**

Uses a ChatML-based reasoning loop with strict regex parsing:

```python
# Agent outputs structured actions
<thinking>
Patient has fever and productive cough. Check for infiltrates.
</thinking>
<action>order_test: chest_xray</action>

# Parser extracts action deterministically
parse_action(response) → {"action_type": "order_test",
                           "query": "chest_xray"}
```

**Reward Normalization:**

GRPO-style reward normalization across episode groups prevents gradient explosion and stabilizes training on noisy RL signals.

### Environment API

```python
from medical_triage_client import MedicalTriageClient

client = MedicalTriageClient(
    url="https://imran785-medical-triage-rl-env.hf.space"
)

# Start episode
obs = client.reset()
print(obs["presented_complaint"])
# → "I have chest pain and feel short of breath with fever."

# Ask a symptom
result = client.step({
    "action_type": "ask_symptom",
    "query": "fever"
})
print(result["message"])
# → "yes, 102F"

# Order a test
result = client.step({
    "action_type": "order_test",
    "query": "chest_xray"
})
print(result["message"])
# → "right lower lobe infiltrate"

# Give diagnosis
result = client.step({
    "action_type": "give_diagnosis",
    "query": "pneumonia"
})
print(result["reward"])
# → 19.0
```

---

## Project Resources

| Resource | Link |
|----------|------|
| 🌐 Live Environment (HF Space) | [imran785/medical-triage-rl-env](https://huggingface.co/spaces/imran785/medical-triage-rl-env) |
| 🤖 Trained Model (HF Hub) | [imran785/medical-triage-qwen-3b](https://huggingface.co/imran785/medical-triage-qwen-3b) |
| 📓 Training Notebook (Colab) | [Open in Colab](https://colab.research.google.com/drive/1zpy1oKgOhQA6MDP1ISbadbuOXjkeqgTA?usp=sharing) |

---

## Why This Matters

Medical diagnosis errors affect millions of patients annually. LLMs are increasingly used in healthcare contexts but fail at systematic clinical reasoning — they either over-explain or under-investigate.

This environment demonstrates that RL training can teach an LLM a fundamentally new capability: **evidence-based sequential reasoning under cost constraints** — the core skill of medical triage.

A researcher could write a paper about this environment because:
- The domain is underexplored in RL/LLM training
- The reward signal captures something genuinely hard to measure
- The results show clear behavioral change, not just metric improvement
- The same framework could extend to any sequential diagnostic domain

---

## Team

**Team Mohammed**
Scaler X Meta Hackathon 2026

---

*Built with OpenEnv · Unsloth · HuggingFace TRL · Qwen2.5*