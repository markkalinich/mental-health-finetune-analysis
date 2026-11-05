---
license: apache-2.0
base_model: convaiinnovations/laya
datasets:
- hao-li/AIDev
language:
- en
pipeline_tag: text-classification
tags:
- laya
- code-review
- pull-requests
- triage
- system-one
- typed-decisions
metrics:
- accuracy
- balanced_accuracy
---

# Laya PR Triage

**A free, fast triage gate for the pull-request review queue.** Give it a short summary of a PR (title,
description, changed files, lines added and removed) and it answers four questions in about
129 ms on one T4 GPU:

| Question | Answers |
|---|---|
| Will this PR need heavy review? | yes / no |
| Is it likely to be merged? | yes / no |
| Which risk area does it touch? | auth, payments, database, config, ui, docs, tests_only, other |
| Does it need a senior reviewer? | yes / no |

The four answers combine into one queue label: **fast-track**, **normal** or **needs senior review**.

It is [Laya](https://huggingface.co/convaiinnovations/laya) (Convai, 421M parameters, ModernBERT-large
encoder, `typed-decisions` checkpoint) fine-tuned on about 6,000 real AI-agent pull requests from the
[AIDev](https://huggingface.co/datasets/hao-li/AIDev) dataset.

It does **not** check whether code is correct. It sorts the queue, so reviewers look first at the PRs
most likely to need them. That is a quick "System 1" decision, which is what Laya is built for.

## Results

Scored on **500 held-out PRs from 382 repositories that contributed no training data**,
against three engines asked the identical questions with the identical PR summary, none of them trained on this task.

![Balanced accuracy, average of 4 questions](balanced_accuracy.png)

**Balanced accuracy** averages the accuracy on each answer separately, so the rare answer counts as much
as the common one. It is the fair score here: about 70% of PRs are merged, so a model that always says
"merged" gets 70% plain accuracy and only 50% balanced accuracy.

| Balanced accuracy (chance) | Jev (TypeSafe) | GPT-4.1 mini | Laya, zero-shot | Laya, fine-tuned (this model) |
|---|---|---|---|---|
| Needs heavy review? (50.0%) | 62.9% | 62.1% | 50.0% | **71.2%** |
| Will it be merged? (50.0%) | 53.8% | 50.7% | 50.3% | **63.8%** |
| Which risk area? (8 options) (12.5%) | 55.8% | 56.8% | 32.2% | **85.3%** |
| Needs a senior reviewer? (50.0%) | 59.3% | 57.7% | 65.5% | **94.8%** |
| **Average** (40.6%) | 58.0% | 56.8% | 49.5% | **78.8%** |

Plain accuracy, with the score of always giving the most common answer in brackets:

| Accuracy (always guess) | Jev (TypeSafe) | GPT-4.1 mini | Laya, zero-shot | Laya, fine-tuned (this model) |
|---|---|---|---|---|
| Needs heavy review? (70.4%) | 58.0% | 67.6% | 29.6% | **72.2%** |
| Will it be merged? (70.0%) | 55.8% | **70.2%** | 69.6% | 67.2% |
| Which risk area? (8 options) (38.2%) | 58.8% | 57.0% | 21.4% | **89.0%** |
| Needs a senior reviewer? (57.6%) | 64.6% | 63.2% | 64.4% | **95.2%** |
| **Average** (59.1%) | 59.3% | 64.5% | 46.2% | **80.9%** |

![Balanced accuracy by question](by_question.png)

![Median time per PR](latency.png)

| | Jev (TypeSafe) | GPT-4.1 mini | Laya, zero-shot | **Laya, fine-tuned** |
|---|---|---|---|---|
| Median time per PR | 1,004 ms | 1,580 ms | 112 ms | **129 ms** |
| Cost for 500 PRs | $0.020 | $0.139 | free (self-hosted) | **free (self-hosted)** |
| Where it ran | hosted API | hosted API | T4 GPU | T4 GPU |

### How to read these results

- **The two outcome questions are the real test.** Heavy review and merged are predicted from facts known
  when the PR opens, and scored against what actually happened. Fine-tuned Laya is the only engine clearly
  above chance on both: 71.2% and 63.8% balanced
  accuracy, against at best 62.9% and
  53.8% for the others. These are real but
  moderate gains, not near-perfect predictions.
- **On "will it be merged" its plain accuracy (67.2%) is below always answering "merged"
  (70.0%).** It trades a few of those for catching rejected PRs, which the
  "always merged" answer never does.
- **Risk area and senior reviewer are rule-following, not judgement.** Their labels come from file-path rules
  applied to the same file list the model reads. Applying that rule directly scores 100.0% and
  97.4%, higher than any model. Use the rule for those two if you can; the model's value is
  answering all four in one call.
- One training run, one seed, one sample of 500 PRs: differences of a few points are within noise.

## How to use

```bash
pip install laya
```

The model must be asked the **same questions, with the same wording and option keys** it was trained on.

```python
import re
import laya

agent = laya.load("Harsh1312/laya-pr-triage", device="cuda")      # or "cpu" (slow: seconds per PR)
                                                    # private repo: add token="hf_..."
QUESTIONS = {
    "high_review_effort": {
        "instructions": "Will this pull request need heavy review?",
        "criteria": {
            "yes": "this PR will need heavy review: many files or lines, or it touches areas that draw discussion",
            "no": "this PR is routine and a quick look will do"
        }
    },
    "likely_merged": {
        "instructions": "Is this pull request likely to be accepted and merged?",
        "criteria": {
            "yes": "this PR is likely to be accepted and merged",
            "no": "this PR is likely to be rejected or closed without merging"
        }
    },
    "risk_area": {
        "instructions": "Which area does this pull request mainly touch?",
        "criteria": {
            "auth": "login, sessions, tokens, permissions, security",
            "payments": "billing, checkout, invoices, money handling",
            "database": "schemas, migrations, queries, models",
            "config": "build, CI, deployment, dependency or settings files",
            "ui": "front-end components, styles, templates",
            "docs": "documentation, README, comments only",
            "tests_only": "only test files changed",
            "other": "application code that fits none of the above"
        }
    },
    "needs_senior": {
        "instructions": "Does this pull request touch sensitive code that needs a senior reviewer?",
        "criteria": {
            "yes": "this PR touches sensitive code (auth, payments, database, configuration) and needs a senior reviewer",
            "no": "this PR does not touch sensitive code"
        }
    }
}

def laya_questions():
    return {name: {"type": "choice", **q} for name, q in QUESTIONS.items()}

# Ordered: the first rule that matches a path decides that path's area.
PATH_RULES: list[tuple[str, re.Pattern]] = [
    ("auth", re.compile(r"(^|/)(auth|oauth|login|session|jwt|security|permission|acl|rbac)", re.I)),
    ("payments", re.compile(r"(^|/)(payment|billing|checkout|invoice|stripe|paypal|subscription)", re.I)),
    ("database", re.compile(r"(^|/)(migrations?|schema|models?|db|database|sql|prisma|alembic)(/|\.|$)|\.sql$", re.I)),
    ("config", re.compile(r"(^|/)(\.github|\.circleci|docker|k8s|helm|terraform|deploy|config|\.env)|\.(ya?ml|toml|ini|lock)$|(^|/)(package\.json|requirements.*\.txt|Makefile|Dockerfile|pom\.xml|build\.gradle)$", re.I)),
    ("tests", re.compile(r"(^|/)(tests?|__tests__|spec|e2e)(/|$)|(\.|_)(test|spec)\.[a-z]+$|(^|/)test_[^/]+$", re.I)),
    ("docs", re.compile(r"(^|/)(docs?|documentation)(/|$)|\.(md|rst|txt|adoc)$|(^|/)(README|CHANGELOG|LICENSE)", re.I)),
    ("ui", re.compile(r"(^|/)(components?|views?|pages?|styles?|templates?|public|assets|ui|frontend)(/|$)|\.(css|scss|sass|less|html|vue|svelte|tsx|jsx)$", re.I)),
]


def path_area(path: str) -> str:
    for area, pattern in PATH_RULES:
        if pattern.search(path):
            return area
    return "other"


def pr_to_text(title, body, files, additions, deletions, author="unknown"):
    """The PR summary the model was trained on. Only facts known when the PR opens."""
    shown = files[:25]
    more = len(files) - len(shown)
    tests = any(path_area(f) == "tests" for f in files)
    return {
        "TITLE": title or "",
        "DESCRIPTION": re.sub(r"\s+", " ", body or "").strip()[:500] or "(none)",
        "CHANGED FILES": f"{len(files)} files: " + ", ".join(shown) + (f", +{more} more" if more else ""),
        "LINES": f"+{additions} -{deletions}",
        "TESTS CHANGED": "yes" if tests else "no",
        "AUTHOR": author,
    }

state = pr_to_text(
    title="Add OAuth refresh-token rotation",
    body="Rotates refresh tokens on every use and revokes the old one.",
    files=["src/auth/tokens.py", "src/auth/session.py", "tests/test_tokens.py"],
    additions=184, deletions=37, author="Claude_Code",
)
answers = agent.predict(state, laya_questions())["answers"]
for name, a in answers.items():
    print(f"{name:20} {a['choice']:12} confidence {a['confidence']:.2f}")
```

To turn the four answers into a queue label:

```python
RISKY = {"auth", "payments", "database", "config"}

def triage_label(a):   # a = {question: choice}
    if a["needs_senior"] == "yes" or (a["high_review_effort"] == "yes" and a["risk_area"] in RISKY):
        return "needs senior review"
    if a["likely_merged"] == "yes" and a["high_review_effort"] == "no" and a["risk_area"] in {"docs", "tests_only", "ui"}:
        return "fast-track"
    return "normal"

print(triage_label({q: a["choice"] for q, a in answers.items()}))
```

## Where to use it

- **A CI step or GitHub Action** that labels every new PR (`fast-track`, `normal`, `needs senior review`),
  so reviewers sort the queue instead of reading it top to bottom.
- **Routing AI-agent PRs**, which this model was trained on (OpenAI Codex, GitHub Copilot, Cursor, Devin,
  Google Jules, Claude Code), before a person or a larger model spends time on them.
- **A cheap first pass in a cascade**: act on confident answers, send the rest to a bigger model or a person.

**Not for:** judging whether code is correct, secure or well written (it never sees the diff); merging or
rejecting PRs on its own; PRs very unlike AI-agent PRs to popular GitHub repos without checking it on your own
history first.

## Training data

[hao-li/AIDev](https://huggingface.co/datasets/hao-li/AIDev) (CC-BY-4.0), the **AIDev-pop** tables (repositories
with more than 100 stars): `pull_request`, `pr_reviews`, `pr_comments`, `pr_review_comments`, `pr_commit_details`.

- **Training set:** about 6,000 closed or merged PRs from about 2,400 repositories, at most 20 per repository.
  10% of those repositories were held out to fit the confidence temperature.
- **Evaluation set:** 500 PRs from 382 other repositories, at most 3 per repository.
  **No repository is in both sets**, and training PRs whose title matched an evaluation PR were dropped.
- **Input text:** title, the first 500 characters of the description, up to 25 changed file paths, lines added and
  removed, whether tests changed, and the agent. No review, comment or merge information is ever in the input.

How each label was made, from outcomes recorded after the PR opened:

| Question | Label |
|---|---|
| Heavy review | reviews + comments + inline review comments of 5 or more (the top ~20% of PRs) |
| Merged | merged vs closed without merging (open PRs skipped) |
| Risk area | the riskiest area any changed file path matches (auth > payments > database > config), else docs / tests only / ui / other |
| Senior reviewer | a risky area, or the PR received a "changes requested" review |

## Training procedure

Convai's Laya fine-tuning recipe (RLCD: a policy gradient on a proper-scoring reward plus soft cross-entropy),
on 2x NVIDIA T4 with DistributedDataParallel, in about 80 minutes:

| Setting | Value |
|---|---|
| Base checkpoint | `convaiinnovations/laya`, subfolder `typed-decisions` |
| Sequences | one per PR per question, built with Laya's own `build_sequence` (max 1,024 tokens) |
| Epochs | 2 |
| Effective batch | 64 (8 per GPU x 2 GPUs x 4 accumulation steps) |
| Learning rate | encoder 2.5e-5, head 1e-4, cosine decay |
| Exploration noise | sigma 0.4 to 0.1, 4 samples per item |
| Precision | fp16 autocast with gradient scaling, gradient checkpointing |
| Class balance | each answer of each question weighted to an equal share (capped at 10x) |
| Calibration | softmax temperature fitted on the held-out repositories: 1.556 |

The class weights matter: without them, zero-shot Laya answered "yes" to heavy review for all 500 evaluation
PRs and "merged" for nearly all of them.

## Limitations

- Labels are proxies. "Heavy review" counts discussion, not reviewer time; "merged" can depend on things outside
  the PR (a maintainer's availability, a duplicate PR).
- Trained only on AI-agent PRs to public repositories with more than 100 stars. Check it on your own history
  before relying on it.
- One run and one evaluation sample; no confidence intervals were computed.
- The comparison engines were used zero-shot, with no prompt tuning. A tuned prompt might narrow the gap.

## License and attribution

- Model weights: Apache-2.0, as the base model [convaiinnovations/laya](https://huggingface.co/convaiinnovations/laya).
- Training data: [AIDev](https://huggingface.co/datasets/hao-li/AIDev) by Hao Li et al., CC-BY-4.0. Each source
  repository keeps its own license; no code or diffs are included in this model or this card.
