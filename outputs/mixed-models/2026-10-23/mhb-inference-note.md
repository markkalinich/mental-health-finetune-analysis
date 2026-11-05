# MentalHealthBench joint-model retry

Formula unchanged. Sample: the 45 MentalHealthBench checkpoints in 18 lineages from `joint-observations.csv`, no safety models. Starts and the REML profile are in `mhb-powell-starts.csv` and `mhb-reml-profile.csv`.

Every Powell start converged to a lineage variance near zero, and the REML profile is highest at a lineage variance of zero. The likelihood falls as that variance ratio increases, so the mixed-model solution is on the boundary. Mixed-model Wald p-values are not used. The reported p-values are from ordinary least squares with lineage-clustered CRV3 standard errors. They are not mixed-model Wald p-values.

## Powell starts

- Start ratio 1e-06: converged True, REML log-likelihood 43.14212569121533, variance ratio 0.01715255143820727, lineage variance 5.094400647290704e-05.
- Start ratio 0.0001: converged True, REML log-likelihood 43.14212569121714, variance ratio 0.017152659209489392, lineage variance 5.0944322790190795e-05.
- Start ratio 0.01: converged True, REML log-likelihood 43.14212569041888, variance ratio 0.017159749162166737, lineage variance 5.0965132266572075e-05.
- Start ratio 0.1: converged True, REML log-likelihood 43.14212569121725, variance ratio 0.017153479961786042, lineage variance 5.094673176198139e-05.
- Start ratio 0.5: converged True, REML log-likelihood 43.14212569122023, variance ratio 0.017153074259612173, lineage variance 5.094554099488969e-05.
- Start ratio 1.0: converged True, REML log-likelihood 43.1421256910862, variance ratio 0.01715580352419223, lineage variance 5.095355158415014e-05.

Profile peak at variance ratio 0.02 (REML log-likelihood 43.14198157238138).

## Estimates used for the MentalHealthBench column

Ordinary least squares, CRV3 by lineage, t reference with 17 degrees of freedom. Intervals are not multiplicity-adjusted. The 0–1 score was the fitted scale. Percentage points are that result multiplied by 100.

| Term | β (95% CI), 0–1 score | P |
|---|---|---:|
| Intercept (Gemma instruction parent, version rank 0, 1 billion parameters) | 0.212 (0.138 to 0.287) | <0.001 |
| Parameter count, per doubling | 0.011 (-0.007 to 0.029) | 0.208 |
| Llama vs Gemma | 0.005 (-0.078 to 0.089) | 0.892 |
| Mistral vs Gemma | 0.085 (-0.029 to 0.198) | 0.134 |
| Qwen vs Gemma | 0.025 (-0.070 to 0.121) | 0.586 |
| SmolLM vs Gemma | 0.055 (-0.094 to 0.205) | 0.446 |
| Version rank, per step | 0.029 (-0.011 to 0.069) | 0.140 |
| Medical fine-tune | -0.023 (-0.069 to 0.022) | 0.295 |
| Mental-health fine-tune | -0.093 (-0.140 to -0.046) | <0.001 |
