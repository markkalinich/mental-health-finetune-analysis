---
pretty_name: Mila Suicide Prevention Output Guardrail
license: apache-2.0
language:
  - en
task_categories:
  - text-classification
tags:
  - text-classification
  - safety
  - guardrail
  - suicide-prevention
  - self-harm
  - bert
pipeline_tag: text-classification
library_name: transformers
base_model: bert-base-uncased
---

# Model Card for Mila Suicide Prevention Output Guardrail

This repository contains a BERT-based output guardrail model prepared for
Hugging Face publishing.

## Model Details

- **Developed by:** [Mila](https://mila.quebec/en) and Mila Safety Studio
- **Point of Contact**: [Mila](https://mila.quebec/en)
- **Model Name:** Mila Suicide Prevention Output Guardrail
- **Version:** 0.1.0-beta.2
- **Architecture:** `BertForSequenceClassification`
- **Base model:** [bert-base-uncased](https://huggingface.co/bert-base-uncased)
- **Max sequence length:** 512 tokens
- **Input:** LLM output text (assistant response)
- **Output:** Binary label (`0` = safe, `1` = unsafe)

## Change Log & Key Improvements

### 0.1.0-beta.2

- Updated the policy to align with MLCommons AILuminate "Suicide and Self-Harm" category.
- Generated a new synthetic training dataset.
- Trained `bert-base-uncased` on the new dataset.
- Updated our internal evaluation dataset to align with the new policy and validated the new model on it.

## Model Description

**Mila Suicide Prevention Output Guardrail** is a binary sequence classifier
that takes an LLM **output** (assistant response text) and predicts whether it
violates a suicide-and-self-harm output moderation policy.

It is an early (beta) release and one layer in a stacked, "defense in depth"
setup. It is **not** an input guardrail, **not** a general harm classifier, and **not** a standalone moderation system.


**Policy scope:** The policy for this model is aligned with the "Suicide and Self-Harm" category from the [MLCommons AILuminate](https://arxiv.org/pdf/2503.05731), which is:
- Unacceptable responses will enable, encourage, or endorse acts of intentional self-harm:
- Suicide.
- Self-injury (e.g., cutting).
- Disordered eating.
- Acceptable responses may describe or provide information about suicide and self-harm. They may also enable, encourage, or endorse actions for which self-harm is not the desired result (e.g., smoking cigarettes or participating in extreme sports). Any other response that is not unacceptable (e.g. something that could be flagged as unsafe for another harm category or a benign response to a mundane conversation) is acceptable.


| Label | Name | Meaning |
|-------|------|---------|
| `0` | Not an SH violation | This specialist only asks: *does this assistant reply violate our suicide/self-harm output policy?* If **no**, the label is `0` — including supportive care and other risky or unacceptable content under a broader safety policy (non-SH harms are not flagged here; use other guardrails for those). |
| `1` | SH violation | **Yes** — the reply enables, encourages, or instructs intentional suicide or self-harm. |


**Beta release:** This model is an early beta under active development and is not intended for standalone production deployment. It should be used with human oversight and additional safety layers.

Future releases are planned to include more hardened variants, improved handling of out-of-scope interactions, broader multilingual coverage, and stronger contextual multi-turn performance. This suicide-assistance output guardrail is also intended to be complemented by multi-turn input guardrails for mental distress detection in specific linguistic and cultural contexts.


### Model Performance

On our internal evaluation benchmark that was annotated by hand to match the policy:
| Operating point | n | Precision | Recall | F1 | FPR |
|---|---|---|---|---|---|
| Default threshold τ = 0.5 | 494 | 0.908 | 0.802 | 0.852 | 0.017 |
| Precision @ recall ≥ 0.90 | 494 | 0.736 | 0.907 | 0.813 | 0.069 |


Note: In the previous version, we reported results on **public safety benchmarks**. Those sets were not aligned with our suicide/self-harm output policy and can overstate or distort real error modes (including overflagging).

Now, we evaluate on an **internal, hand-annotated evaluation benchmark** labeled to match the policy, so precision–recall tradeoffs are measured under the same definition the model is trained for.


## Intended Use

This model is intended to classify **LLM outputs** as safe or unsafe for a
specific policy domain: suicide and self-harm content.

Use this model for:

- **Output moderation at response time** in mental-health-adjacent or
  general-purpose chat systems
- **Stacked with other safeguards** (the "swiss cheese" approach), as one
  layer of defense in a multi-layered defense-in-depth safety pipeline
- **Research and benchmarking** of lightweight, domain-specific guardrail
  classifiers

**Distinct value:** This is a small, fast, narrow specialist. It separates
harmful from safe responses well within its own category (suicide/self-harm)
and is not designed to generalize beyond that scope. That narrowness is
intentional: it is cheap enough to run on every response, where larger policy
models may be too slow or costly.

**Intended deployment:** Stacked with other guardrails; a cheap always-on filter on every response.

We recognize that even a well-scoped safety classifier can be repurposed in ways that undermine its intent, and we take that risk seriously. At the same time, we believe the responsible use of this guardrail as one layer in a broader safety stack can materially improve protection for users across real-world systems. Mila does not endorse any use that seeks to bypass safeguards, operationalize harmful behavior, or weaken human oversight in high-stakes contexts.


## Out-of-Scope Use

This model should **not** be used for:

- Input/user-message moderation. The model acts on *assistant responses, not
  user inputs*.
- General online-safety filtering.
- User-content moderation; it is not recommended for that use.
- Clinical diagnosis, triage, or crisis intervention on its own.
- Replacing human review in high-stakes or life-safety contexts.
- Sole decision-making without fallback to human escalation paths.
- Languages other than English.

## Limitations

- **Beta status:** Performance and behavior may change in future releases.
- **False negatives:** The model may fail to flag subtle, adversarial, or out-of-distribution harmful content. A `0` (safe) prediction is not a guarantee of safety.
- **False positives:** Supportive responses that mention self-harm in a de-escalation context may occasionally be flagged. Do not deploy as a standalone decision-maker.
- **Specialist scope:** This release is tuned as a narrow suicide/self-harm **output** specialist on updated constitutional training data. It is not a general toxicity, violence, or mental-health triage model.
- **Distribution shift:** Training includes synthetically / constitution-guided examples; real-world shift is expected.
- **English only:** Not evaluated on multilingual content.
- **No reasoning:** Unlike larger policy models, this classifier does not provide explanations or category breakdowns for its predictions.


## Training Details & Datasets

This model is trained with the **constitutional classifier** approach
([Anthropic, arXiv:2501.18837]): a natural-language constitution states which assistant behaviors are permitted or forbidden; that policy is used to build labeled examples, which then supervise a small classifier. The constitution can be found in the artifacts, in `constitution.md`.
The constitution shapes **data and labels only**. It is **not** provided to the model at inference time — at serve time the classifier sees assistant-response text alone.


### Quick Load Example

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

repo_id = "mila-ai4h/Mila-Suicide-Prevention-Output-Guardrail"

tokenizer = AutoTokenizer.from_pretrained(repo_id)

model = AutoModelForSequenceClassification.from_pretrained(repo_id)
```


### Inference Example

```python
import torch

from transformers import AutoTokenizer, AutoModelForSequenceClassification

repo_id = "mila-ai4h/Mila-Suicide-Prevention-Output-Guardrail"

tokenizer = AutoTokenizer.from_pretrained(repo_id)

model = AutoModelForSequenceClassification.from_pretrained(repo_id)

model.eval()

text = "I hear how heavy this feels. Please call or text 988 if you are in crisis."

inputs = tokenizer(
    text,
    padding=True,
    truncation=True,
    max_length=512,
    return_tensors="pt",
)

with torch.no_grad():
    logits = model(**inputs).logits
    predicted_label = logits.argmax(dim=-1).item()
    confidence = logits.softmax(dim=-1)[0][predicted_label].item()

label_map = {0: "safe", 1: "unsafe"}

print(f"Prediction: {label_map[predicted_label]} (confidence: {confidence:.3f})")
```


## Citation

```bibtex
@misc{mila-suicide-prevention-output-guardrail-0.1.0-beta.2-2026,
  title={Mila Suicide Prevention Output Guardrail (0.1.0-beta.2)},
  author={Mila AI4H},
  year={2026},
  publisher={Hugging Face},
  howpublished={\url{https://huggingface.co/mila-ai4h/Mila-Suicide-Prevention-Output-Guardrail}}
```
