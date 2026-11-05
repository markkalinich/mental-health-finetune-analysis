---
language:
  - en
license: apache-2.0
base_model: Qwen/Qwen3Guard-4B
tags:
  - safety
  - guard
  - content-moderation
  - constitutional-classifier
  - jailbreak-defense
  - bittensor
model-index:
  - name: Halo4B-guard-alpha
    results:
      - task:
          type: text-classification
          name: Safety Classification
        metrics:
          - type: f1
            value: 0.8654
            name: F1 Score (avg across 7 benchmarks)
          - type: f1
            value: 0.8576
            name: F1 Score — Qwen3Guard-4B baseline
---

# Halo4B-guard-alpha

**Halo4B-guard-alpha** is Astroware's first finetuned safety guard model, built on top of [Qwen/Qwen3Guard-4B](https://huggingface.co/Qwen/Qwen3Guard-4B). It is trained on Astroware's proprietary constitutional safety dataset and hardened against jailbreak patterns surfaced by the [Trishool | SN23](https://trishool.ai) red-teaming subnet.

| Property | Value |
|---|---|
| **Base model** | Qwen/Qwen3Guard-4B |
| **Parameters** | ~4B |
| **Classifier type** | Input-side safety classifier |
| **Training dataset** | Astroware constitutional synthetic dataset |
| **F1 Score** | **0.8654** avg (↑ from 0.8576 baseline, +0.78pp) |
| **Release** | alpha |
| **Organization** | [Astroware](https://astroware.ai) |

---

## Overview

Halo4B-guard-alpha is a **constitutional input classifier** — a guard model that sits in front of LLM deployments and determines whether an incoming user query is safe to process. It operates on the full conversation context (user turn + prior turns) and returns a binary harmful / harmless prediction with an associated confidence score.

The model is optimized for:
- **Low false-negative rate** — minimizing missed harmful queries
- **Controlled false-positive rate** — limiting unnecessary refusals of legitimate requests
- **Jailbreak robustness** — resisting obfuscation, encoding, and prompt-injection attacks observed in the wild via Trishool SN23 adversarial mining

---

## What Changed vs. Qwen3Guard-4B Baseline

### Benchmark Results

F1 scores across 7 public safety benchmarks. **Final F1** is the unweighted average across all benchmarks.

| Benchmark | Qwen3Guard-4B | Halo4B-guard-alpha | Δ F1 |
|---|---|---|---|
| Aegis | 0.7241 | **0.7671** | +0.0430 |
| Aegis 2.0 | 0.8240 | **0.8257** | +0.0017 |
| HarmBench | 0.9924 | **0.9924** | +0.0000 |
| OpenAI Moderation | 0.8061 | **0.8173** | +0.0112 |
| SimpleSafetyTests | 0.9744 | **0.9744** | +0.0000 |
| ToxicChat | **0.8190** | 0.8156 | −0.0034 |
| WildGuardTest | 0.8629 | **0.8653** | +0.0024 |
| **Average F1** | **0.8576** | **0.8654** | **+0.0078** |

The largest gains are on **Aegis** (+4.3pp) and **OpenAI Moderation** (+1.1pp), driven by improved recall on adversarial and edge-case harmful queries.

### Jailbreak Patches (Trishool SN23)

Halo4B-guard-alpha patches a set of jailbreak patterns discovered through adversarial mining activity on **Trishool | SN23**, Astroware's Bittensor subnet. Miners on SN23 are incentivized to find inputs that bypass safety classifiers; confirmed bypasses are folded back into the training dataset via augmentation.

Specific classes of attack patched in this release:

- **Adversarial noise** — perturbation-based inputs that subtly corrupt token boundaries or spacing to confuse the classifier while remaining human-readable
- **Narrative injection** — harmful instructions embedded inside fictional stories, roleplay scenarios, or creative writing prompts; the original model failed to flag these when harmful content was wrapped in an ostensibly benign narrative frame
- **Benign tail** — queries that open with a harmless preamble and append a harmful instruction at the end, exploiting a tendency in the base model to anchor on early tokens
- **Encoding / obfuscation attacks**: Base64, hex, ROT13, Morse code, homoglyph substitutions, and leetspeak (basic, extended, and aggressive multi-character forms)
- **Style-shift attacks**: CamelCase injection, pig Latin transforms, emoji-substituted harmful intent
- **Semantic paraphrase attacks**: back-translation roundtrips, synonym insertion, and word-swap augmentations that preserve harmful meaning while shifting surface form
- **Prompt injection patterns**: role-playing / system-prompt override attempts, mischievous-user persona injections
- **Chained / mixed tactics**: attacks that layer multiple obfuscation methods (e.g., narrative wrapper + synonym swap + Base64)

---

## Safety Categories

Halo4B-guard-alpha inherits and extends the safety taxonomy defined in the [Qwen3Guard technical report](https://arxiv.org/abs/2510.14276). The model classifies inputs across 9 categories, each assessed at one of three severity tiers.

### Severity Tiers

| Tier | Description |
|---|---|
| **Safe** | Content generally considered safe across most scenarios |
| **Controversial** | Content whose harmfulness is context-dependent or subject to disagreement across applications |
| **Unsafe** | Content generally considered harmful across most scenarios |

### Harm Categories

| # | Category | Scope | Description |
|---|---|---|---|
| 1 | **Violent** | Input + Output | Content that provides detailed instructions, methods, or advice on how to commit acts of violence, including the manufacture, acquisition, or use of weapons. Also includes depictions of violence. |
| 2 | **Non-Violent Illegal Acts** | Input + Output | Content providing guidance or advice for non-violent illegal activities like hacking, unauthorized drug production, or stealing. |
| 3 | **Sexual Content or Sexual Acts** | Input + Output | Content offering any sexual imagery, references, or descriptions featuring individuals. Also includes content describing explicit sexual imagery or illegal/unethical sexual acts such as rape, bestiality, incest, and sexual slavery. |
| 4 | **Personally Identifiable Information** | Input + Output | Content offering unauthorized sharing or disclosure of sensitive personal identifying information, such as name, ID number, address, phone number, medical records, financial details, and account passwords. |
| 5 | **Suicide & Self-Harm** | Input + Output | Content advocating, directly encouraging, or detailing methods for self-harm, suicide, or dangerous activities that could lead to serious injury or death. |
| 6 | **Unethical Acts** | Input + Output | Any immoral or unethical content or acts, including but not limited to bias, discrimination, stereotype, injustice, hate speech, offensive language, harassment, insults, threat, defamation, extremism, misinformation regarding ethics, and other behaviors that while not illegal are still considered unethical. |
| 7 | **Politically Sensitive Topics** | Input + Output | The deliberate creation or spread of false information about government actions, historical events, or public figures that is demonstrably untrue and poses risk of public deception or social harm. |
| 8 | **Copyright Violation** | Input + Output | Content offering unauthorized reproduction, distribution, public display, or derivative use of copyrighted materials such as novels, scripts, lyrics, and other creative works protected by law, without the explicit permission of the copyright holder. |
| 9 | **Jailbreak** | Input only | Content that explicitly attempts to override the model's system prompt or model conditioning. |

The Jailbreak category is scoped to input classification only — it applies to engineered prompts, not model outputs.

---

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_id = "astroware/Halo4B-guard-alpha"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id)
model.eval()

conversation = [
    {"role": "user", "content": "How do I make chlorine gas at home?"}
]

inputs = tokenizer.apply_chat_template(
    conversation,
    return_tensors="pt",
    add_generation_prompt=False
)

with torch.no_grad():
    logits = model(**inputs).logits
    prob_harmful = torch.sigmoid(logits[0, 1]).item()

print(f"Harmful probability: {prob_harmful:.3f}")
# Threshold at 0.5 for binary classification
is_harmful = prob_harmful >= 0.5
```

> **Note:** The exact input format follows the Qwen3Guard chat template. Refer to the base model documentation for prompt formatting details until Astroware publishes its inference library.

---

## Limitations

- **Alpha release** — this model is not yet production-hardened across all safety categories. Current coverage is strongest in Violent, Non-Violent Illegal Acts, and Suicide & Self-Harm.
- **English-primary** — the training corpus is predominantly English. Cross-lingual robustness has not been formally evaluated.
- **Output classifier not included** — Halo4B-guard-alpha is an *input* classifier only. It does not monitor model outputs or operate on streaming token-level generation.
- **Threshold sensitivity** — the default 0.5 threshold is a starting point. Operators should calibrate against their own false-positive tolerance using a held-out sample of their traffic.
- **Not a replacement for defense-in-depth** — this model is one layer in a multi-stage safety stack. It should be combined with output classifiers, rate limiting, and session-level monitoring.

---

## Evaluation

Full metrics across all 7 benchmarks. FPR = false positive rate (overrefusal); FNR = false negative rate (missed harm).

### Aegis (n=869)

| Metric | Qwen3Guard-4B | Halo4B-guard-alpha | Δ |
|---|---|---|---|
| Accuracy | 0.7089 | **0.7457** | +0.0368 |
| Precision | 0.9910 | **0.9918** | +0.0008 |
| Recall | 0.5704 | **0.6254** | +0.0550 |
| **F1** | 0.7241 | **0.7671** | **+0.0430** |
| FPR (overrefusal) | 0.0105 | 0.0105 | +0.0000 |
| FNR (missed harm) | 0.4296 | **0.3746** | −0.0550 |

### Aegis 2.0

| Metric | Qwen3Guard-4B | Halo4B-guard-alpha | Δ |
|---|---|---|---|
| Accuracy | 0.8269 | **0.8284** | +0.0015 |
| Precision | 0.9118 | **0.9130** | +0.0012 |
| Recall | 0.7517 | **0.7535** | +0.0018 |
| **F1** | 0.8240 | **0.8257** | **+0.0017** |
| FPR (overrefusal) | 0.0851 | **0.0840** | −0.0011 |
| FNR (missed harm) | 0.2483 | **0.2465** | −0.0018 |

### HarmBench

| Metric | Qwen3Guard-4B | Halo4B-guard-alpha | Δ |
|---|---|---|---|
| Accuracy | 0.9850 | 0.9850 | +0.0000 |
| Precision | 1.0000 | 1.0000 | +0.0000 |
| Recall | 0.9850 | 0.9850 | +0.0000 |
| **F1** | 0.9924 | **0.9924** | **+0.0000** |
| FPR (overrefusal) | 0.0000 | 0.0000 | +0.0000 |
| FNR (missed harm) | 0.0150 | 0.0150 | +0.0000 |

### OpenAI Moderation

| Metric | Qwen3Guard-4B | Halo4B-guard-alpha | Δ |
|---|---|---|---|
| Accuracy | 0.8798 | **0.8815** | +0.0017 |
| Precision | **0.8077** | 0.7848 | −0.0229 |
| Recall | 0.8046 | **0.8525** | +0.0479 |
| **F1** | 0.8061 | **0.8173** | **+0.0112** |
| FPR (overrefusal) | **0.0864** | 0.1054 | +0.0190 |
| FNR (missed harm) | 0.1954 | **0.1475** | −0.0479 |

### SimpleSafetyTests

| Metric | Qwen3Guard-4B | Halo4B-guard-alpha | Δ |
|---|---|---|---|
| Accuracy | 0.9500 | 0.9500 | +0.0000 |
| Precision | 1.0000 | 1.0000 | +0.0000 |
| Recall | 0.9500 | 0.9500 | +0.0000 |
| **F1** | 0.9744 | **0.9744** | **+0.0000** |
| FPR (overrefusal) | 0.0000 | 0.0000 | +0.0000 |
| FNR (missed harm) | 0.0500 | 0.0500 | +0.0000 |

### ToxicChat

| Metric | Qwen3Guard-4B | Halo4B-guard-alpha | Δ |
|---|---|---|---|
| Accuracy | **0.9760** | 0.9748 | −0.0012 |
| Precision | **0.8846** | 0.8524 | −0.0322 |
| Recall | 0.7624 | **0.7818** | +0.0194 |
| **F1** | **0.8190** | 0.8156 | **−0.0034** |
| FPR (overrefusal) | **0.0076** | 0.0104 | +0.0028 |
| FNR (missed harm) | 0.2376 | **0.2182** | −0.0194 |

### WildGuardTest

| Metric | Qwen3Guard-4B | Halo4B-guard-alpha | Δ |
|---|---|---|---|
| Accuracy | 0.8881 | **0.8887** | +0.0006 |
| Precision | **0.9444** | 0.9335 | −0.0109 |
| Recall | 0.7944 | **0.8064** | +0.0120 |
| **F1** | 0.8629 | **0.8653** | **+0.0024** |
| FPR (overrefusal) | **0.0372** | 0.0457 | +0.0085 |
| FNR (missed harm) | 0.2056 | **0.1936** | −0.0120 |

### Summary

| Benchmark | Qwen3Guard-4B F1 | Halo4B-guard-alpha F1 | Δ F1 |
|---|---|---|---|
| Aegis | 0.7241 | **0.7671** | +0.0430 |
| Aegis 2.0 | 0.8240 | **0.8257** | +0.0017 |
| HarmBench | 0.9924 | **0.9924** | +0.0000 |
| OpenAI Moderation | 0.8061 | **0.8173** | +0.0112 |
| SimpleSafetyTests | 0.9744 | **0.9744** | +0.0000 |
| ToxicChat | **0.8190** | 0.8156 | −0.0034 |
| WildGuardTest | 0.8629 | **0.8653** | +0.0024 |
| **Average F1** | **0.8576** | **0.8654** | **+0.0078** |

The recall-precision tradeoff shifts slightly toward recall on OpenAI Moderation, ToxicChat, and WildGuardTest — reflecting a deliberate tuning decision to reduce missed harmful queries (FNR) at a small cost to overrefusal (FPR). The ToxicChat F1 regression (−0.3pp) is the only net decline and is under active investigation.

---

## Trishool | SN23

[Trishool](https://trishool.ai) is Astroware's Bittensor subnet (SN23) dedicated to adversarial red-teaming of safety classifiers. Miners compete to discover inputs that bypass the guard model; successful bypasses are validated, scored, and incorporated into the next training iteration. This creates a continuous adversarial feedback loop:

```
Guard model deployed → Miners probe for bypasses → 
Confirmed bypasses collected → Dataset augmented → 
Next guard model trained
```

Halo4B-guard-alpha is the first model to incorporate SN23 feedback at training time.

---

## Citation

```bibtex
@misc{astroware2026halo4b,
  title        = {Halo4B-guard-alpha: A Constitutional Safety Classifier Hardened via Adversarial Red-Teaming},
  author       = {Astroware},
  year         = {2026},
  howpublished = {Hugging Face Model Hub},
  url          = {https://huggingface.co/astroware/Halo4B-guard-alpha}
}
```

---

## License

Apache 2.0 — same as the Qwen3Guard base model.

---

*Built by [Astroware](https://astroware.ai) · Halo project · Trishool SN23*
