---
license: llama3.1
base_model:
- unsloth/Llama-3.1-8B-Instruct
- KayaTechAI/SFT-Llama-3.1-8B-Financial-Instruct
- KayaTechAI/SFT-Llama-3.1-8B-Financial-Instruct-Sentiment
tags:
- merge
- ties
- financial
- sentiment
---

# Llama 3.1 8B Finance

Production financial-domain model combining instruction-tuned financial
reasoning with financial-sentiment classification, merged onto
`unsloth/Llama-3.1-8B-Instruct` via TIES-Merge (sign-consensus + magnitude-pruning).

## Verified lineage (from HF repo metadata, not assumed)

```
KayaTechAI/SFT-Llama-3.1-8B-Financial-Instruct (LoRA adapter)
  base_model_name_or_path: KayaTechAI/Merged-IPT-Llama-3.1-8B-Financial-Instruct

KayaTechAI/SFT-Llama-3.1-8B-Financial-Instruct-Sentiment (LoRA adapter)
  base_model_name_or_path: KayaTechAI/SLERP-IPT-Llama-3.1-8B-Financial-Instruct
    (itself a mergekit SLERP of KayaTechAI/Merged-IPT-Llama-3.1-8B-Financial-Instruct + unsloth/Meta-Llama-3.1-8B-Instruct)
```

Both adapters were baked onto their OWN correct base first (never
directly onto `unsloth/Llama-3.1-8B-Instruct`, which would have been numerically invalid
since LoRA deltas are only meaningful relative to the exact base they were
fit against). Only after baking were the two resulting full checkpoints
delta-merged onto `unsloth/Llama-3.1-8B-Instruct`.

## Merge methodology

1. **Bake stage**: `PeftModel.merge_and_unload()` for each adapter against its
   verified base, producing two full dense checkpoints.
2. **Conflict analysis**: cosine similarity between (financial - base) and
   (sentiment - base) deltas, computed per-tensor.
   - Tensors compared: 291
   - High conflict (cos < 0.3): 21 (7.2%)
   - High agreement (cos > 0.7): 168 (57.7%)
3. **TIES-Merge**: sign-consensus + top-k magnitude pruning combine of the two
   deltas, re-applied onto `unsloth/Llama-3.1-8B-Instruct`.
   - Financial weight: 0.55, density: 0.9
   - Sentiment weight: 0.45, density: 0.9
   - Sign-disagreement resolution: dominant-magnitude delta wins (no zeroing)
   - Normalization: enabled (preserves aggregate delta magnitude per tensor)

## Intended use

Financial document analysis, financial Q&A/reasoning, and financial-sentiment
classification in a single checkpoint.

## Disclaimer

Research/production candidate — validate on held-out financial QA and
sentiment test sets (`KayaTechAI/sp500-summary-dataset`,
`KayaTechAI/FIN-Sentiment-SFT`) before full production rollout.
