# MentalHealthBench joint-model retry

Formula unchanged. Sample: the 63 MentalHealthBench checkpoints in 25 lineages from `joint-observations.csv`, no safety models. Starts and the REML profile are in `mhb-powell-starts.csv` and `mhb-reml-profile.csv`.

Powell starts agree on an interior REML peak.

## Powell starts

- Start ratio 1e-06: converged True, REML log-likelihood 67.62635421081228, variance ratio 0.2927127998016353, lineage variance 0.0007502615927481131.
- Start ratio 0.0001: converged True, REML log-likelihood 67.6263542108123, variance ratio 0.29271273533216785, lineage variance 0.0007502614497500479.
- Start ratio 0.01: converged True, REML log-likelihood 67.62635421081227, variance ratio 0.29271282765043855, lineage variance 0.0007502616545188241.
- Start ratio 0.1: converged True, REML log-likelihood 67.6263542108123, variance ratio 0.2927127698328044, lineage variance 0.0007502615262750217.
- Start ratio 0.5: converged True, REML log-likelihood 67.6263542108123, variance ratio 0.29271274081350773, lineage variance 0.0007502614619080669.
- Start ratio 1.0: converged True, REML log-likelihood 67.62635421081006, variance ratio 0.2927133237154354, lineage variance 0.0007502627548276129.

Profile peak at variance ratio 0.2 (REML log-likelihood 67.55458362351783).

## Estimates used for the MentalHealthBench column

REML mixed model, normal Wald intervals. Percentage points are that result multiplied by 100.

| Term | β (95% CI), 0–1 score | P |
|---|---|---:|
| Intercept (Gemma instruction parent, version rank 0, 1 billion parameters) | 0.194 (0.145 to 0.242) | <0.001 |
| Llama vs Gemma | 0.000 (-0.056 to 0.057) | 0.993 |
| Mistral vs Gemma | 0.078 (-0.001 to 0.157) | 0.052 |
| Qwen vs Gemma | 0.023 (-0.025 to 0.072) | 0.345 |
| SmolLM vs Gemma | 0.052 (-0.031 to 0.135) | 0.218 |
| Medical fine-tune | -0.028 (-0.059 to 0.004) | 0.083 |
| Mental-health fine-tune | -0.098 (-0.131 to -0.066) | <0.001 |
| Parameter count, per doubling | 0.020 (0.007 to 0.033) | 0.003 |
| Version rank, per step | 0.036 (0.010 to 0.061) | 0.006 |
