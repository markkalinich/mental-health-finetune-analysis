---
base_model: microsoft/deberta-v3-base
library_name: transformers
license: apache-2.0
pipeline_tag: text-classification
tags:
- agent-safety
- tool-call-classification
- llm-agents
- guardrails
- ai-safety
- agentic-ai
- safety-classifier
- policy-decision-point
---

# saroku-guard

saroku-guard is a classifier that judges whether a proposed AI agent tool call is safe to execute, before it runs. It is the runtime Policy Decision Point in [saroku](https://github.com/Karanxa/saroku), sitting in the execution path of agent tool calls to catch unsafe actions in single-digit milliseconds, with no API calls and no data leaving the local environment.

## Evaluation

Evaluated on agent tool-call decisions it never saw during training, spanning 16 domains — APIs, browser automation, cloud infrastructure, consumer apps, databases, dev tools, email, file systems, media, messaging, payments, personal assistants, smart home, and travel — disjoint from training and validation data. Compared head-to-head against other agent guard models, each run in its own documented input format.

![saroku-guard results: accuracy, unsafe recall, unsafe precision, and latency (p50/p95/p99) against other agent guard models](results.png)

The model is tuned to favor recall on the unsafe class, consistent with its role as a pre-execution safety gate. saroku-guard is a 184M-parameter classifier; every model above is a multi-billion-parameter LLM repurposed as a judge (AgentDog: Llama-3.1-8B, Llama Guard 4: 12B, ShieldAgent: Qwen2.5-7B) — the latency and size gap is a direct consequence of that.

![saroku-guard vs. adjacent guard models: Prompt Guard and Qwen3Guard, included as a sanity check, not peers](adjacent.png)

## Model Details

- **Type:** Text classifier (safe / unsafe), with a secondary violation-type output
- **Task:** Pre-execution safety judgment for agentic tool calls
- **License:** Apache 2.0
- **Output:** Binary label (`safe` / `unsafe`) plus, on an unsafe verdict, an associated violation category

## Intended Use

saroku-guard is designed to run as the first-line check in an agent execution pipeline, immediately before a tool call is invoked. It is built for high-throughput, low-latency screening: the large majority of routine actions are cleared locally, and only flagged actions are escalated to a more expensive analysis step (an LLM judge).

**In scope:** judging a single, discrete tool call (name, arguments, and surrounding context) for safety prior to execution.

**Out of scope:** conversational content moderation, jailbreak or prompt-injection detection in free-form chat, and post-hoc audit of actions that have already executed. The violation category returned alongside an unsafe verdict is intended as supporting context for logging and review, not as the sole input to automated policy branching.

## How to Use

The recommended way to use saroku-guard is through the saroku SDK, which handles input formatting automatically:

```bash
pip install saroku
```

```python
from saroku import SafetyGuard

guard = SafetyGuard()  # saroku-guard runs by default, no configuration required

result = guard.check(
    action="DELETE FROM users WHERE last_login < '2023-01-01'",
    context="Production database agent.",
    operator_constraints=["Never DELETE on prod without confirmation"],
)

if not result.is_safe:
    print(result.summary())
```

### Direct use

The model can also be loaded directly with `transformers`. Weights are merged and self-contained — no adapter or separate base model is required.

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained(
    "karanxa/saroku-guard",
    num_labels=2,
    id2label={0: "unsafe", 1: "safe"},
    label2id={"unsafe": 0, "safe": 1},
)
tokenizer = AutoTokenizer.from_pretrained("karanxa/saroku-guard")
```

Direct use requires reproducing the model's expected input structure (action, context, constraints, and related fields, assembled in a fixed format). The saroku SDK implements this natively; see its serializer for the reference implementation.

## Where This Fits

![saroku-guard sits between an agent proposing an action and that action executing, escalating flagged actions to an LLM judge if one is configured](flow.png)

## Limitations

- English-language tool-call text.
- saroku-guard is a fast first-pass filter, not a complete safety system. For irreversible or high-consequence actions, pair it with saroku's LLM-based judge for deeper analysis.

## Citation

If you use saroku-guard in your work, please reference the [saroku project](https://github.com/Karanxa/saroku).

---

Built on [microsoft/deberta-v3-base](https://huggingface.co/microsoft/deberta-v3-base).
