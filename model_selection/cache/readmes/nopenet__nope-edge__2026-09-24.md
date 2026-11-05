---
license: mit
language:
  - en
tags:
  - safety
  - crisis-detection
  - text-classification
  - mental-health
  - content-safety
  - suicide-prevention
base_model: Qwen/Qwen3-4B
pipeline_tag: text-generation
library_name: transformers
---

# NOPE Edge - Crisis Classification Model

A fine-tuned model for detecting crisis signals in text - suicidal ideation, self-harm, abuse, violence, and other safety-critical content. Features chain-of-thought reasoning that explains its classifications.

> **License:** [MIT](LICENSE.md) - free for any use, including commercial. Built on Qwen3 (Apache-2.0); see NOTICE.md.

---

## Model Variants

| Model | Parameters | Use Case |
|-------|------------|----------|
| **[nope-edge](https://huggingface.co/nopenet/nope-edge)** | 4B | Maximum accuracy |
| **[nope-edge-mini](https://huggingface.co/nopenet/nope-edge-mini)** | 1.7B | High-volume, cost-sensitive |

This is **nope-edge (4B)**.

---

## Quick Start

### Requirements

- Python 3.10+
- GPU with 8GB+ VRAM (e.g., RTX 3070, A10G, L4) - or CPU (slower)
- ~8GB disk space

```bash
pip install torch transformers accelerate
```

### Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import re

model_id = "nopenet/nope-edge"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

def classify(message: str) -> str:
    """Returns XML with reflection and risk classification.

    `message` is a single user turn. For multi-turn input, serialize the whole
    exchange into this one string, e.g. "User: ...\\n\\nAI: ...\\n\\nUser: ..." —
    Edge is trained on one serialized user message, not native chat roles.
    """
    inputs = tokenizer.apply_chat_template(
        [{"role": "user", "content": message}],
        add_generation_prompt=True,
        return_dict=True,
        return_tensors="pt",
    ).to(model.device)

    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=300, do_sample=False)

    return tokenizer.decode(
        output[0][inputs["input_ids"].shape[1]:],
        skip_special_tokens=True
    ).strip()

# Example
result = classify("I want to end it all tonight")
print(result)
```

**Output:**
```xml
<reflection>The user directly expresses intent to end their life with a specific timeline ("tonight"), indicating acute suicidal ideation with imminent risk.</reflection>
<risks>
  <risk subject="self" type="suicide" severity="high" imminence="urgent"/>
</risks>
```

---

## Output Format

The model outputs XML with two components:

### 1. Reflection (Chain-of-Thought)

```xml
<reflection>Reasoning about the input...</reflection>
```

The model explains its classification, including:
- What signals it detected
- Why it chose the risk type and severity
- Any contextual factors considered

### 2. Risk Classification

**Crisis detected:**
```xml
<risks>
  <risk subject="self" type="suicide" severity="high" imminence="urgent" features="active_ideation,intent_stated"/>
</risks>
```

**No crisis:**
```xml
<risks/>
```

> **"No risk" can also appear as an element.** Benign inputs usually return empty
> `<risks/>`, but the model may occasionally emit an explicit non-risk element such as
> `<risk subject="self" type="none" severity="none"/>`, or a real type with
> `severity="none"`. Treat **any element whose `type` is not one of the 9 below, or
> whose `severity="none"`, as no-risk** (drop it) — that's what NOPE's own parser does
> (see the parsing example).

### Risk Attributes

| Attribute | Values | Description |
|-----------|--------|-------------|
| `subject` | `self`, `other`, `unknown` | Who is at risk (defaults to `unknown` if unclear) |
| `type` | `suicide`, `self_harm`, `self_neglect`, `violence`, `abuse`, `sexual_violence`, `exploitation`, `stalking`, `neglect` | Risk category — these **9 only**; there is no `none` type |
| `severity` | `none`, `mild`, `moderate`, `high`, `critical` | Urgency level (`none` means treat as no-risk) |
| `imminence` | `not_applicable`, `chronic`, `subacute`, `urgent`, `emergency` | Time sensitivity |
| `features` | comma-separated list | **Low-confidence, free-form** indicators — see Important Limitations |

### Subject Attribution

| Subject | Meaning | Example |
|---------|---------|---------|
| `self` | The speaker is at risk | "I want to kill myself" |
| `other` | Reporting concern about someone else | "My friend said she wants to die" |

### Parsing Example

```python
import re
from dataclasses import dataclass
from typing import Optional

@dataclass
class Risk:
    subject: str
    type: str
    severity: str
    imminence: Optional[str] = None
    features: Optional[list] = None

def parse_output(output: str) -> dict:
    """Parse model output into structured data."""
    result = {
        "reflection": None,
        "risks": [],
        "is_crisis": False
    }

    # Extract reflection
    reflection_match = re.search(r'<reflection>(.*?)</reflection>', output, re.DOTALL)
    if reflection_match:
        result["reflection"] = reflection_match.group(1).strip()

    # Check for empty risks (no crisis)
    if '<risks/>' in output or '<risks />' in output:
        return result

    # Valid risk types — anything else (including a stray type="none") is dropped
    VALID_TYPES = {
        "suicide", "self_harm", "self_neglect", "violence", "abuse",
        "sexual_violence", "neglect", "exploitation", "stalking",
    }

    # Extract risk elements
    risk_pattern = r'<risk\s+([^>]+)/?\s*>'
    for match in re.finditer(risk_pattern, output):
        attrs = {}
        for attr_match in re.finditer(r'(\w+)="([^"]*)"', match.group(1)):
            attrs[attr_match.group(1)] = attr_match.group(2)

        # Mirror NOPE's own parser: skip non-risk elements
        if attrs.get("type") not in VALID_TYPES:
            continue
        if attrs.get("severity", "none") == "none":
            continue

        result["risks"].append(Risk(
            subject=attrs.get("subject", "unknown"),
            type=attrs["type"],
            severity=attrs["severity"],
            imminence=attrs.get("imminence", "not_applicable"),
            features=attrs.get("features", "").split(",") if attrs.get("features") else None,
        ))
        result["is_crisis"] = True

    return result

# Usage
output = classify("I want to end it all tonight")
parsed = parse_output(output)
print(f"Crisis: {parsed['is_crisis']}")
print(f"Reasoning: {parsed['reflection']}")
for risk in parsed['risks']:
    print(f"Risk: {risk.type}/{risk.severity} ({risk.subject})")
```

---

## Examples

### Crisis Detection

**Input:** "I want to end it all tonight"
```xml
<reflection>The user directly expresses intent to end their life with a specific timeline ("tonight"), indicating acute suicidal ideation with imminent risk.</reflection>
<risks>
  <risk subject="self" type="suicide" severity="high" imminence="urgent"/>
</risks>
```

**Input:** "My friend told me she's been cutting herself"
```xml
<reflection>The user is reporting concern about a friend engaging in self-harm behavior. This is third-party disclosure requiring attention.</reflection>
<risks>
  <risk subject="other" type="self_harm" severity="moderate" imminence="chronic"/>
</risks>
```

### No Crisis (Correctly Ignored)

**Input:** "kms lmao this exam is killing me"
```xml
<reflection>The user is using hyperbolic internet slang ("kms" = "kill myself") to express frustration about an exam. The "lmao" and casual context indicate this is not genuine suicidal ideation.</reflection>
<risks/>
```

**Input:** "I used to be suicidal but therapy helped me recover"
```xml
<reflection>The user is sharing a recovery narrative about past suicidal ideation. They explicitly state therapy helped and they have recovered. No current crisis indicators.</reflection>
<risks/>
```

---

## Input Best Practices

### Text Preprocessing

**Preserve natural prose.** The model was trained on real conversations with authentic expression:

| Keep | Why |
|------|-----|
| Emojis | Emotional signals matter |
| Punctuation intensity | "I can't do this!!!" vs "I can't do this" |
| Slang/algospeak | "kms", "unalive", "catch the bus", "graped" |
| Casual spelling | "im so done" - don't normalize |

**Only remove:** Zero-width Unicode, decorative fonts, excessive whitespace.

### Multi-Turn Conversations

Serialize into a single user message:

```python
conversation = """User: How are you?
Assistant: I'm here to help. How are you feeling?
User: Not great. I've been thinking about ending it all."""

messages = [{"role": "user", "content": conversation}]
```

---

## Production Deployment

For high-throughput use, deploy with vLLM or SGLang:

```bash
# SGLang (recommended)
pip install sglang
python -m sglang.launch_server \
    --model nopenet/nope-edge \
    --dtype bfloat16 --port 8000

# vLLM
pip install vllm
python -m vllm.entrypoints.openai.api_server \
    --model nopenet/nope-edge \
    --dtype bfloat16 --max-model-len 2048 --port 8000
```

Then call as OpenAI-compatible API:

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "nopenet/nope-edge",
    "messages": [{"role": "user", "content": "I want to end it all"}],
    "max_tokens": 300, "temperature": 0
  }'
```

**Health check** (server readiness):

```bash
curl -fsS http://localhost:8000/health && echo " ready"
```

**Docker** (vLLM, one self-contained container):

```bash
docker run --gpus all --restart unless-stopped -p 8000:8000 \
  vllm/vllm-openai:latest \
  --model nopenet/nope-edge --dtype bfloat16 --max-model-len 2048
```

The server loads the model **once** at startup, so requests don't reload weights — use this (or a small systemd unit wrapping the same command) for any real workload. Running the `classify()` snippet as a fresh process per message re-loads ~8GB of weights every time: fine for testing, not for production.

---

## Model Details

| | |
|---|---|
| **Parameters** | 4B |
| **Precision** | bfloat16 |
| **Base Model** | Qwen/Qwen3-4B |
| **Method** | LoRA fine-tune, merged to full weights |
| **License** | [MIT](LICENSE.md) |

---

## Risk Types Detected

| Type | Description | Clinical Framework |
|------|-------------|-------------------|
| `suicide` | Suicidal ideation, intent, planning | C-SSRS |
| `self_harm` | Non-suicidal self-injury (NSSI) | - |
| `self_neglect` | Eating disorders, medical neglect | - |
| `violence` | Threats/intent to harm others | HCR-20 |
| `abuse` | Domestic/intimate partner violence | DASH |
| `sexual_violence` | Rape, sexual assault, coercion | - |
| `neglect` | Failing to care for dependent | - |
| `exploitation` | Trafficking, grooming, sextortion | - |
| `stalking` | Persistent unwanted contact | SAM |

---

## Important Limitations

- Outputs are **probabilistic signals**, not clinical assessments
- **False negatives and false positives will occur**
- The `features` list is **heuristic and lower-confidence** than `type`/`severity` — it can include labels not supported by the input text. Treat it as a hint only; don't gate decisions on it.
- Never use as the **sole basis** for intervention decisions
- Always implement **human review** for flagged content
- This model is **not** a medical device or substitute for professional judgment
- Not validated for all populations, languages, or cultural contexts

---

## Disclaimers, Intended Use & Non-Claims

**Edge is a detection aid — not a predictive, diagnostic, or therapeutic tool, and not a replacement for clinical judgment.** It surfaces signals in text for a human to review; it is not a medical device, not clinically validated, and not a crisis or emergency service. False positives and false negatives will occur — some people in genuine crisis will not be identified — so never use Edge as the sole basis for an intervention decision, and always keep a human in the loop. If anyone is in immediate danger, contact your local emergency services or find resources at talk.help.

Full disclaimer: see DISCLAIMER.md.

---

## License

NOPE Edge is **MIT-licensed** — free for any use, including commercial, with no separate agreement required. See [LICENSE.md](LICENSE.md). Built on Qwen3 (Apache-2.0); see NOTICE.md.

---

## About NOPE

NOPE provides safety infrastructure for AI applications. Our API helps developers detect mental health crises and harmful AI behavior in real-time.

- **Website:** https://nope.net
- **Documentation:** https://docs.nope.net
- **Support:** support@nope.net

