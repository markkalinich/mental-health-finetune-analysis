---
license: apache-2.0
base_model: convaiinnovations/laya
library_name: laya
pipeline_tag: text-classification
tags:
  - laya
  - typed-decisions
  - github
  - issue-triage
  - non-autoregressive
  - modernbert
metrics:
  - accuracy
  - f1
model-index:
  - name: laya-issue-triage
    results:
      - task:
          type: text-classification
          name: GitHub issue type classification
        dataset:
          name: laya-issue-triage (held-out repos)
          type: manyamkarthik/laya-issue-triage
        metrics:
          - type: accuracy
            value: 0.6501
          - type: f1
            name: macro F1
            value: 0.6273
---

# laya-issue-triage

[Laya](https://github.com/NandhaKishorM/laya) fine-tuned to triage GitHub
issues. It answers two typed questions about an issue in a single forward pass,
with no text generation:

| question | type | answers |
|---|---|---|
| `issue_type` | `choice` | `bug`, `feature`, `question`, `docs` |
| `needs_more_info` | `noul` | `true` / `false` |

## Results

Measured on 3868 issues from three repositories held out of training
entirely (`huggingface/transformers`, `facebook/react`, `microsoft/TypeScript`),
so these are generalization numbers, not memorization.

| model | issue_type acc | issue_type macro-F1 | needs_info acc |
|---|---|---|---|
| random | 0.250 | - | 0.500 |
| majority class | 0.345 | - | 0.738 |
| base `laya`, zero-shot | 0.626 | 0.524 | 0.563 |
| **this model** | **0.650** | **0.627** | **0.734** |

Per-class F1 on `issue_type`:

| class | F1 |
|---|---|
| `bug` | 0.641 |
| `feature` | 0.796 |
| `question` | 0.487 |
| `docs` | 0.585 |

Per-repository accuracy on `issue_type`:

| repository | accuracy | n |
|---|---|---|
| `facebook/react` | 0.724 | 908 |
| `huggingface/transformers` | 0.753 | 632 |
| `microsoft/TypeScript` | 0.551 | 1329 |

Median latency on a T4 during evaluation: 78.8 ms per issue.

### Scope of these numbers

This model is evaluated **only** on GitHub issue triage. It has not been run on
the `LocalLLaMA/typed-decisions` benchmark, so its scores are not comparable to
numbers reported there for the base Laya checkpoints or for any other system.
Different task, different label space, different data.

## Usage

```python
import laya

agent = laya.Agent("harikarthikmanyam/laya-issue-triage")
questions = {
    "issue_type": {
        "type": "choice",
        "instructions": "What kind of GitHub issue do `title` and `body` describe?",
        "criteria": {
            "bug": "something is broken: a crash, an error, wrong output, or a regression from behaviour that used to work",
            "feature": "a request for new functionality, an enhancement, or a proposal to change how something works",
            "question": "the author is asking how to use the project or why it behaves a certain way, not reporting a defect",
            "docs": "the documentation is missing, wrong, unclear, or needs an example"
        }
    },
    "needs_more_info": {
        "type": "noul",
        "instructions": "Must a maintainer ask the author of `body` for more information -- reproduction steps, a version number, logs, or a code sample -- before this issue can be worked on?"
    }
}

state = {"title": "Crash when opening a file with a BOM",
         "body": "v1.4.2 on Linux. Steps: open any UTF-8-BOM file, editor segfaults."}
result = agent.predict(state, questions)
print(result["answers"]["issue_type"]["choice"])
```

The question definitions above are part of the contract: this model was trained
against those exact `instructions` and `criteria` strings, so changing them
changes behaviour.

## Training data

~7.7k closed issues carrying maintainer-applied labels, harvested from 14
public repositories and balanced across the four types. Labels come from the
maintainers who triaged each issue, not from a teacher model.

Dataset, harvesting code and evaluation script:
https://github.com/manyamkarthik/laya-issue-triage

## Limitations

- English issue text only; use `laya-multilingual` as a base for other languages.
- Issue text is truncated to roughly 900 characters, so decisions rest on the
  title and opening paragraphs.
- `needs_more_info` is supervised by maintainer labels such as `needs-repro`,
  which projects apply inconsistently; it is a weaker signal than `issue_type`.
- Confidences are uncalibrated unless you fit temperatures (see the notebook).
