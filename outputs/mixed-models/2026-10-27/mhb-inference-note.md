# MentalHealthBench joint-model retry

Formula unchanged. Sample: the 63 MentalHealthBench checkpoints in 25 lineages from `joint-observations.csv`, no safety models. Starts and the REML profile are in `mhb-powell-starts.csv` and `mhb-reml-profile.csv`.

Powell starts agree on an interior REML peak.

## Powell starts

- Start ratio 1e-06: converged True, REML log-likelihood 67.98165031028324, variance ratio 0.26003443437829016, lineage variance 0.0006655812609225208.
- Start ratio 0.0001: converged True, REML log-likelihood 67.98165031028324, variance ratio 0.2600344356330447, lineage variance 0.00066558126373044.
- Start ratio 0.01: converged True, REML log-likelihood 67.98165031028326, variance ratio 0.26003443816492405, lineage variance 0.0006655812693963387.
- Start ratio 0.1: converged True, REML log-likelihood 67.98165031028083, variance ratio 0.26003510763173265, lineage variance 0.000665582767544537.
- Start ratio 0.5: converged True, REML log-likelihood 67.98165031028333, variance ratio 0.26003454098814277, lineage variance 0.000665581499496541.
- Start ratio 1.0: converged True, REML log-likelihood 67.98165031028321, variance ratio 0.26003441835057034, lineage variance 0.0006655812250553135.

Profile peak at variance ratio 0.2 (REML log-likelihood 67.94969993166048).

## Estimates used for the MentalHealthBench column

REML mixed model, normal Wald intervals. Percentage points are that result multiplied by 100.

| Term | β (95% CI), 0–1 score | P |
|---|---|---:|
| Intercept (Gemma instruction parent, version rank 0, 1 billion parameters) | 0.167 (0.108 to 0.226) | <0.001 |
| Llama vs Gemma | 0.029 (-0.030 to 0.088) | 0.338 |
| Mistral vs Gemma | 0.122 (0.034 to 0.210) | 0.006 |
| Qwen vs Gemma | 0.052 (-0.002 to 0.106) | 0.060 |
| SmolLM vs Gemma | 0.079 (-0.008 to 0.167) | 0.076 |
| Medical fine-tune | -0.029 (-0.060 to 0.003) | 0.074 |
| Mental-health fine-tune | -0.098 (-0.130 to -0.065) | <0.001 |
| Parameter count, per doubling | 0.020 (0.007 to 0.033) | 0.002 |
| Version rank, per step | 0.034 (0.012 to 0.056) | 0.003 |
