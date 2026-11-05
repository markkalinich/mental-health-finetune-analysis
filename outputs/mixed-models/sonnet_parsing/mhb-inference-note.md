# MentalHealthBench joint-model retry

Formula unchanged. Sample: the 61 MentalHealthBench checkpoints in 23 lineages from `joint-observations.csv`, no safety models. Starts and the REML profile are in `mhb-powell-starts.csv` and `mhb-reml-profile.csv`.

Powell starts agree on an interior REML peak.

## Powell starts

- Start ratio 1e-06: converged True, REML log-likelihood 60.03374766382322, variance ratio 0.2707432573008841, lineage variance 0.0008429149225261308.
- Start ratio 0.0001: converged True, REML log-likelihood 60.03374766382322, variance ratio 0.2707432542587705, lineage variance 0.0008429149142343989.
- Start ratio 0.01: converged True, REML log-likelihood 60.03374766382325, variance ratio 0.27074315966029316, lineage variance 0.0008429146563922031.
- Start ratio 0.1: converged True, REML log-likelihood 60.03374766382325, variance ratio 0.2707431587289598, lineage variance 0.0008429146538537159.
- Start ratio 0.5: converged True, REML log-likelihood 60.03374766382325, variance ratio 0.27074319409339803, lineage variance 0.000842914750244745.
- Start ratio 1.0: converged True, REML log-likelihood 60.03374766382261, variance ratio 0.2707434972484342, lineage variance 0.0008429155765387373.

Profile peak at variance ratio 0.2 (REML log-likelihood 59.994195831785476).

## Estimates used for the MentalHealthBench column

REML mixed model, normal Wald intervals. Percentage points are that result multiplied by 100.

| Term | β (95% CI), 0–1 score | P |
|---|---|---:|
| Intercept (Gemma instruction parent, version rank 0, 1 billion parameters) | 0.172 (0.106 to 0.238) | <0.001 |
| Llama vs Gemma | 0.029 (-0.042 to 0.101) | 0.423 |
| Mistral vs Gemma | 0.133 (0.034 to 0.232) | 0.009 |
| Qwen vs Gemma | 0.057 (-0.005 to 0.118) | 0.072 |
| SmolLM vs Gemma | 0.086 (-0.012 to 0.183) | 0.085 |
| Medical fine-tune | -0.029 (-0.064 to 0.007) | 0.110 |
| Mental-health fine-tune | -0.101 (-0.137 to -0.065) | <0.001 |
| Parameter count, per doubling | 0.020 (0.005 to 0.035) | 0.008 |
| Version rank, per step | 0.036 (0.011 to 0.062) | 0.005 |
