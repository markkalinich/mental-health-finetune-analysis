# Settings

- Roster: `/home/mkalinich/main/revision_3_experiments/hf_inventory/results/roster/2026-10-23/roster.csv`
- SHA-256: `633908d9cb8cb3bc74032d32c14b00942483d2ca736271d9b5cb4971fdd8b588`
- Python: `.venv/bin/python`.
- pyfixest 0.28.0, statsmodels 0.14.6.
- Rehosts: `unsloth/gemma-3-1b-it` = `google/gemma-3-1b-it`; `unsloth/gemma-3-4b-it` = `google/gemma-3-4b-it`. Google scores are used.
- Joint formula: `score ~ log2_param_billions + C(family, Treatment(reference='Gemma')) + version_rank + C(training_category, Treatment(reference='instruction_parent'))`.
- Joint estimation: MixedLM, REML, one random intercept.
- Joint intervals: Wald, standard normal. Labeled Wald only when the fit converged and the random-intercept variance is above 1e-08.
- Paired formula: `delta ~ 1`.
- Paired covariance: pyfixest CRV3 by `ancestry_cluster_id`.
- Paired degrees of freedom: clusters minus 1.
- Multiplicity: Benjamini-Hochberg on the three primary fraction-scale tests.
- No other model was fit.
- Yes/no F1 parse: roster columns, Sonnet-recovered.
