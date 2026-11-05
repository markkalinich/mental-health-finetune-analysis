# MentalHealthBench joint-model retry

Formula unchanged. Sample unchanged: 43 checkpoints, 18 lineages, no safety models. Starts and the REML profile are in `mhb-powell-starts.csv` and `mhb-reml-profile.csv`.

Every Powell start converged to a lineage variance near zero, and the REML profile is highest at a lineage variance of zero. The likelihood falls as that variance ratio increases, so the mixed-model solution is on the boundary. Mixed-model Wald p-values are not used. The reported p-values are from ordinary least squares with lineage-clustered CRV3 standard errors. They are not mixed-model Wald p-values.

## Powell starts

- Start ratio 1e-06: converged True, REML log-likelihood 39.816357910602875, variance ratio 1.5951653548506717e-10, lineage variance 4.940056791502085e-13.
- Start ratio 0.0001: converged True, REML log-likelihood 39.81635782133621, variance ratio 3.090367351498444e-08, lineage variance 9.570537575739946e-11.
- Start ratio 0.01: converged True, REML log-likelihood 39.816357910430526, variance ratio 2.1886705148420638e-10, lineage variance 6.778078904471679e-13.
- Start ratio 0.1: converged True, REML log-likelihood 39.816357910775636, variance ratio 1.0000230298344767e-10, lineage variance 3.0969645531289954e-13.
- Start ratio 0.5: converged True, REML log-likelihood 39.81635791074911, variance ratio 1.0913294848168774e-10, lineage variance 3.379730895602537e-13.
- Start ratio 1.0: converged True, REML log-likelihood 39.81635791052993, variance ratio 1.8462511788033716e-10, lineage variance 5.717642780297074e-13.

Profile peak at variance ratio 0.0 (REML log-likelihood 39.81635791106601).

## Estimates used for the MentalHealthBench column

Ordinary least squares, CRV3 by lineage, t reference with 17 degrees of freedom. Intervals are not multiplicity-adjusted. The 0–1 score was the fitted scale. Percentage points are that result multiplied by 100.

| Term | β (95% CI), 0–1 score | P |
|---|---|---:|
| Intercept (Gemma instruction parent, version rank 0, 1 billion parameters) | 0.211 (0.139 to 0.282) | <0.001 |
| Parameter count, per doubling | 0.011 (-0.005 to 0.028) | 0.171 |
| Llama vs Gemma | 0.003 (-0.078 to 0.084) | 0.939 |
| Mistral vs Gemma | 0.085 (-0.029 to 0.199) | 0.133 |
| Qwen vs Gemma | 0.028 (-0.063 to 0.118) | 0.529 |
| SmolLM vs Gemma | 0.057 (-0.095 to 0.210) | 0.440 |
| Version rank, per step | 0.030 (-0.007 to 0.066) | 0.107 |
| Medical fine-tune | -0.015 (-0.060 to 0.030) | 0.488 |
| Mental-health fine-tune | -0.093 (-0.140 to -0.046) | <0.001 |
