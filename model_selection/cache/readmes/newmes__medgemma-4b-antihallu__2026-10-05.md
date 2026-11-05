---
license: other
license_name: health-ai-developer-foundations-terms-of-use
license_link: https://developers.google.com/health-ai-developer-foundations/terms
base_model: google/medgemma-4b-it
base_model_relation: finetune
pipeline_tag: image-text-to-text
library_name: transformers
language:
  - en
tags:
  - medical
  - medgemma
  - hai-def
  - anti-hallucination
  - pharmacovigilance
  - medwatch
  - clinical-trial
  - rlfr
  - medgemma-impact-challenge
---

# MedGemma 4B Anti-Hallucination (RLFR)

**MedGemma 4B fine-tuned with RLFR (Reinforcement Learning from Feature Rewards) to stop fabricating medical facts.**
Part of [CLARA](https://github.com/newmes/clara-web), NEWMES AI team's submission to the
[MedGemma Impact Challenge](https://www.kaggle.com/competitions/med-gemma-impact-challenge) (Kaggle, Feb 2026).

| | |
|---|---|
| Base | [`google/medgemma-4b-it`](https://huggingface.co/google/medgemma-4b-it) |
| Method | RLFR — a **frozen hallucination-detection probe** on the model's hidden features is the reward signal; the policy is optimised to avoid responses the probe flags as fabricated |
| Reward features | 6 feature rewards incl. factual accuracy, completeness and format compliance |
| Role in CLARA | Data Analysis Agent: when an SAE occurs, writes the FDA MedWatch 3500A clinical narrative (B5), dechallenge (C7) and rechallenge (C8) assessments from CDASH CRF data, then exported as E2B(R3) XML |
| Format | bf16 safetensors (2 shards, 8.6 GB), Gemma 3 chat template |

## Results

Both evaluations use n = 300 questions; brackets are 95 % CIs.
Notebook: [`notebooks/1_medgemma_anti-hallucination.ipynb`](https://github.com/newmes/clara-web/blob/main/notebooks/1_medgemma_anti-hallucination.ipynb).

**MedHallu HARD** — open-ended medical questions with no context; answers judged by Gemini 2.5 Pro.

| | Vanilla MedGemma 4B | **RLFR (this model)** |
|---|---|---|
| Hallucinated | 37.3 % [32.1, 42.9] | **6.7 % [4.4, 10.1]** |
| Correct | 55.0 % | 5.0 % |
| Refused / declined to answer | 7.7 % | 88.3 % |

McNemar test (hallucinated vs. not): p < 0.001.

**MMLU Medical** (8 medical subsets, multiple choice) — capability preservation.

| | Vanilla | **RLFR** |
|---|---|---|
| Accuracy | 60.7 % [55.0, 66.0] | **64.3 % [58.8, 69.5]** |

McNemar p = 0.11 (not significant): factual medical knowledge is preserved.

**Read the refusal rate before using this model.** RLFR made it very conservative: on hard open-ended questions it declines far more often than it answers. That is the intended trade-off for regulatory documents (a wrong AE term or grade in an SAE report is worse than a blank), but it is the wrong model for general medical Q&A.

## Usage

```python
import torch
from transformers import AutoModelForImageTextToText, AutoProcessor

repo = "newmes/medgemma-4b-antihallu"
model = AutoModelForImageTextToText.from_pretrained(repo, torch_dtype=torch.bfloat16, device_map="auto")
processor = AutoProcessor.from_pretrained(repo)

messages = [
    {"role": "system", "content": [{"type": "text", "text":
        "You are a pharmacovigilance writer. Use only facts present in the case data. "
        "If information is missing, say so instead of guessing."}]},
    {"role": "user", "content": [{"type": "text", "text":
        "Write the MedWatch 3500A clinical narrative for this case:\n"
        "Subject 001, 58 F. Drug: trastuzumab deruxtecan 5.4 mg/kg q3w, started 2026-01-05.\n"
        "AE: pneumonitis, onset 2026-02-25, CTCAE grade 2, serious: yes, action: drug withdrawn, "
        "treatment: prednisone 1 mg/kg, outcome: recovering."}]},
]
inputs = processor.apply_chat_template(messages, add_generation_prompt=True,
                                       tokenize=True, return_dict=True, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=400, do_sample=False)
print(processor.decode(out[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

Text-only use is fine (`AutoModelForCausalLM` + `AutoTokenizer` also load it). Served in CLARA via vLLM on one 24 GB GPU.

> **Stop token.** The tokenizer reports `eos_token_id = 1` (`<eos>`), but Gemma 3 actually ends turns with `<end_of_turn>` (id 106). `generation_config.json` already lists both; if you build your own generation loop, include 106 in `eos_token_id` or generation runs to `max_new_tokens`.

## Intended use and limitations

- **Research / demonstration only.** Not a medical device; generated narratives must be reviewed by a qualified person before any regulatory use.
- Optimised for *grounded* generation from structured case data. It refuses aggressively when context is thin.
- Evaluated on English benchmarks only (n = 300 each); the Gemini judge itself can err.
- Inherits the [Health AI Developer Foundations terms of use](https://developers.google.com/health-ai-developer-foundations/terms) from MedGemma.

## About CLARA

CLARA (Clinical Longitudinal AI Research Assistant) tackles the 12–21-day blind spot between oncology-trial clinic visits:
a daily ~60-second video + voice check-in (**Data Collection Agent**, on-device) feeds a longitudinal timeline with AE/SAE flagging and
automatic MedWatch 3500A / E2B(R3) reports (**Data Analysis Agent**). A rule-based clinical-trial simulator (100 patients × 126 days,
7 real drug profiles) is used to quantify the benefit: mean AE detection delay 4.6 → 1.2 days, deaths 21 → 16 per 100 patients.

HAI-DEF models used: MedGemma 1.5 4B (nurse dialogue, visual AE grading), MedSigLIP-448 (frame classification), HeAR (dry/wet cough), MedASR (medical speech recognition).

- Code: [newmes/clara-web](https://github.com/newmes/clara-web) · iOS app: [newmes/clara-app](https://github.com/newmes/clara-app)
- Sibling model: [newmes/medgemma-ae-detection](https://huggingface.co/newmes/medgemma-ae-detection) (LoRA-tuned on top of this checkpoint) · data: [newmes/clinical-trial-engine-data](https://huggingface.co/datasets/newmes/clinical-trial-engine-data)
- Competition: [The MedGemma Impact Challenge](https://www.kaggle.com/competitions/med-gemma-impact-challenge) — Google Research / HAI-DEF, $100 000 prize pool, final submission 2026-02-24, 850+ teams. Judged on effective use of HAI-DEF models, problem importance, real-world impact, technical feasibility, and execution.

> Originally published as `AlphaRaven/medgemma-4b-antihallu` (2026-02-23); moved to the `newmes` organization in Sep 2026. Weights are identical.

## Citation

```bibtex
@misc{clara2026,
  title  = {CLARA: Clinical Longitudinal AI Research Assistant},
  author = {NEWMES AI Team},
  year   = {2026},
  url    = {https://github.com/newmes/clara-web},
  note   = {MedGemma Impact Challenge submission}
}
```
