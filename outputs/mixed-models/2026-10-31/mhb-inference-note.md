# MentalHealthBench joint-model retry

Formula unchanged. Sample: the 61 MentalHealthBench checkpoints in 23 lineages from `joint-observations.csv`, no safety models. Starts and the REML profile are in `mhb-powell-starts.csv` and `mhb-reml-profile.csv`.

Powell starts agree on an interior REML peak.

## Powell starts

- Start ratio 1e-06: converged True, REML log-likelihood 64.34774440399214, variance ratio 0.28662468807275715, lineage variance 0.0007504917111158917.
- Start ratio 0.0001: converged True, REML log-likelihood 64.34774440399184, variance ratio 0.2866243826778642, lineage variance 0.0007504910143926218.
- Start ratio 0.01: converged True, REML log-likelihood 64.34774440399208, variance ratio 0.28662472573601416, lineage variance 0.0007504917970402659.
- Start ratio 0.1: converged True, REML log-likelihood 64.34774440399218, variance ratio 0.28662461443765014, lineage variance 0.0007504915431258884.
- Start ratio 0.5: converged True, REML log-likelihood 64.34774440399143, variance ratio 0.28662427256390544, lineage variance 0.0007504907631802784.
- Start ratio 1.0: converged True, REML log-likelihood 64.34774440398738, variance ratio 0.28662546600311123, lineage variance 0.0007504934858738297.

Profile peak at variance ratio 0.2 (REML log-likelihood 64.28944763155917).

## Estimates used for the MentalHealthBench column

REML mixed model, normal Wald intervals. Percentage points are that result multiplied by 100.

| Term | β (95% CI), 0–1 score | P |
|---|---|---:|
| Intercept (Gemma instruction parent, version rank 0, 1 billion parameters) | 0.167 (0.106 to 0.228) | <0.001 |
| Llama vs Gemma | 0.029 (-0.037 to 0.096) | 0.387 |
| Mistral vs Gemma | 0.123 (0.031 to 0.215) | 0.009 |
| Qwen vs Gemma | 0.053 (-0.004 to 0.110) | 0.069 |
| SmolLM vs Gemma | 0.080 (-0.010 to 0.170) | 0.083 |
| Medical fine-tune | -0.029 (-0.062 to 0.003) | 0.075 |
| Mental-health fine-tune | -0.099 (-0.132 to -0.066) | <0.001 |
| Parameter count, per doubling | 0.020 (0.006 to 0.034) | 0.004 |
| Version rank, per step | 0.034 (0.011 to 0.058) | 0.004 |
