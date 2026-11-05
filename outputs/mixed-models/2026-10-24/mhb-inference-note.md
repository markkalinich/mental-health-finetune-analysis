# MentalHealthBench joint-model retry

Formula unchanged. Sample: the 59 MentalHealthBench checkpoints in 23 lineages from `joint-observations.csv`, no safety models. Starts and the REML profile are in `mhb-powell-starts.csv` and `mhb-reml-profile.csv`.

Powell starts agree on an interior REML peak.

## Powell starts

- Start ratio 1e-06: converged True, REML log-likelihood 60.95286464456311, variance ratio 0.31487731783797807, lineage variance 0.0008400152628507597.
- Start ratio 0.0001: converged True, REML log-likelihood 60.952864645335694, variance ratio 0.31486562762014236, lineage variance 0.0008399883069427587.
- Start ratio 0.01: converged True, REML log-likelihood 60.95286464533595, variance ratio 0.314865851977576, lineage variance 0.0008399888242793127.
- Start ratio 0.1: converged True, REML log-likelihood 60.952864645335964, variance ratio 0.31486581728472185, lineage variance 0.0008399887442824951.
- Start ratio 0.5: converged True, REML log-likelihood 60.95286464533481, variance ratio 0.31486540192272583, lineage variance 0.0008399877865163297.
- Start ratio 1.0: converged True, REML log-likelihood 60.95286464533595, variance ratio 0.3148657843546874, lineage variance 0.000839988668350489.

Profile peak at variance ratio 0.2 (REML log-likelihood 60.85664276414002).

## Estimates used for the MentalHealthBench column

REML mixed model, normal Wald intervals. Percentage points are that result multiplied by 100.

| Term | β (95% CI), 0–1 score | P |
|---|---|---:|
| Intercept (Gemma instruction parent, version rank 0, 1 billion parameters) | 0.187 (0.135 to 0.239) | <0.001 |
| Llama vs Gemma | 0.011 (-0.055 to 0.077) | 0.745 |
| Mistral vs Gemma | 0.087 (0.002 to 0.172) | 0.044 |
| Qwen vs Gemma | 0.033 (-0.024 to 0.091) | 0.255 |
| SmolLM vs Gemma | 0.054 (-0.032 to 0.140) | 0.220 |
| Medical fine-tune | -0.025 (-0.058 to 0.008) | 0.138 |
| Mental-health fine-tune | -0.094 (-0.128 to -0.059) | <0.001 |
| Parameter count, per doubling | 0.019 (0.005 to 0.033) | 0.008 |
| Version rank, per step | 0.032 (0.004 to 0.061) | 0.027 |
