# Joint description and paired mental-health differences

Roster snapshot: `/home/mkalinich/main/revision_3_experiments/hf_inventory/results/roster/2026-10-23/roster.csv` sha256 `df6453e43f9e86e0dac62c8600185e221fae93a82ff2820cf01efb082e127def`. The snapshot is `roster-snapshot.csv` in this directory. Counts below come from that file.

The cohort is 73 checkpoints: 25 instruction-tuned parents and 48 fine-tunes whose weight-update method and training objective are both stated (0 fine-tunes without both are listed in `unlabeled-fine-tunes.csv` and are not fit). Pretrained checkpoints are not included. `unsloth/gemma-3-1b-it` is `google/gemma-3-1b-it`. `unsloth/gemma-3-4b-it` is `google/gemma-3-4b-it`. Each pair is one checkpoint. The Google score is the score used. Unsloth scores that differ are listed in `rehost-score-conflicts.csv` and are not averaged in.

Scores that differ: google/gemma-3-1b-it si_f1: Google 0.71637, Unsloth 0.716612; google/gemma-3-1b-it cssrs_f1: Google 0.020202, Unsloth 0.033445; google/gemma-3-1b-it mhb_safety: Google 0.290333, Unsloth 0.263823; google/gemma-3-4b-it si_f1: Google 0.941704, Unsloth 0.944072; google/gemma-3-4b-it cssrs_f1: Google 0.767045, Unsloth 0.765714; google/gemma-3-4b-it mhb_safety: Google 0.311353, Unsloth 0.310691.

## Release rank

Version rank is the release order inside a family, written to `version-rank-mapping.csv` before either fit. Children inherit the parent's family and rank. Gemma 3n is flagged as ambiguous because it is a parallel line, not a numbered successor. All four Gemma 3n checkpoints, two instruction parents and two fine-tunes, enter as 2 and 4 billion effective parameters. SmolLM has one release, so it does not identify the version slope.

The version coefficient is one linear change per rank step, shared by every family, after adjustment for log2 parameter count. It is an adjusted association, not a causal effect of a release. The steps that keep the same size label are Llama 3 to Llama 3.1 at 8B, Mistral v0.2 to v0.3 at 7B, and Qwen3 to Qwen3.5 at 4B. The other steps also change which sizes are present. The list is `version-steps.csv`.

## Joint mixed model (secondary)

For each outcome separately: score on the 0–1 scale, log2 of the parameter count in billions, family (reference Gemma), version rank, and training category (reference instruction parent). Random intercept for the canonical instruction parent and its children. A parent is one row, not one row per child. REML. Intervals are Wald intervals. Gemma 3n E2B and E4B enter as 2 and 4 billion effective parameters. Safety checkpoints are out of the MentalHealthBench model only.

- synthetic suicidal-ideation yes/no F1: 73 checkpoints, 25 clusters, design full rank True, converged True, random-intercept variance 0.024236, residual variance 0.018883, Wald intervals supported True.
- C-SSRS yes/no F1: 73 checkpoints, 25 clusters, design full rank True, converged True, random-intercept variance 0.006117, residual variance 0.030488, Wald intervals supported True.
  statsmodels warned that the random-intercept variance may be on the boundary of its parameter space. That warning appears when a variance is below about 0.01. The rule used here treats a variance of 1e-08 or below as singular. This fit is above that line, so the Wald intervals are reported.
- MentalHealthBench suicide/self-harm subset: 63 checkpoints, 25 clusters, design full rank True, converged True, random-intercept variance 0.000750, residual variance 0.002563, Wald intervals supported True.
  statsmodels warned that the random-intercept variance may be on the boundary of its parameter space. That warning appears when a variance is below about 0.01. The rule used here treats a variance of 1e-08 or below as singular. This fit is above that line, so the Wald intervals are reported.

Coefficients below are on the 0–1 score scale.

- si_f1, fitted score at 1 billion parameters, Gemma, version rank 0, instruction parent: 0.6292 (Wald interval 0.4343 to 0.8241).
- si_f1, family difference: Llama versus Gemma: -0.0991 (Wald interval -0.3313 to 0.1331).
- si_f1, family difference: Mistral versus Gemma: -0.1157 (Wald interval -0.4370 to 0.2056).
- si_f1, family difference: Qwen versus Gemma: -0.1410 (Wald interval -0.3390 to 0.0570).
- si_f1, family difference: SmolLM versus Gemma: 0.0376 (Wald interval -0.3028 to 0.3780).
- si_f1, training-category difference: medical versus instruction parents: -0.0998 (Wald interval -0.1873 to -0.0123).
- si_f1, training-category difference: mental-health versus instruction parents: -0.0679 (Wald interval -0.1570 to 0.0211).
- si_f1, training-category difference: safety versus instruction parents: 0.0389 (Wald interval -0.0712 to 0.1490).
- si_f1, associated difference per doubling of parameter count: 0.1220 (Wald interval 0.0705 to 0.1736).
- si_f1, associated difference per version step: 0.0535 (Wald interval -0.0525 to 0.1595).
- cssrs_f1, fitted score at 1 billion parameters, Gemma, version rank 0, instruction parent: 0.3837 (Wald interval 0.2304 to 0.5370).
- cssrs_f1, family difference: Llama versus Gemma: 0.0966 (Wald interval -0.0754 to 0.2686).
- cssrs_f1, family difference: Mistral versus Gemma: 0.0932 (Wald interval -0.1577 to 0.3442).
- cssrs_f1, family difference: Qwen versus Gemma: 0.1422 (Wald interval -0.0092 to 0.2935).
- cssrs_f1, family difference: SmolLM versus Gemma: 0.1814 (Wald interval -0.0772 to 0.4400).
- cssrs_f1, training-category difference: medical versus instruction parents: -0.0930 (Wald interval -0.2005 to 0.0145).
- cssrs_f1, training-category difference: mental-health versus instruction parents: -0.0482 (Wald interval -0.1586 to 0.0623).
- cssrs_f1, training-category difference: safety versus instruction parents: 0.0333 (Wald interval -0.1012 to 0.1677).
- cssrs_f1, associated difference per doubling of parameter count: 0.0432 (Wald interval 0.0040 to 0.0823).
- cssrs_f1, associated difference per version step: 0.1260 (Wald interval 0.0455 to 0.2064).
- mhb_safety, fitted score at 1 billion parameters, Gemma, version rank 0, instruction parent: 0.1936 (Wald interval 0.1448 to 0.2424).
- mhb_safety, family difference: Llama versus Gemma: 0.0002 (Wald interval -0.0564 to 0.0569).
- mhb_safety, family difference: Mistral versus Gemma: 0.0780 (Wald interval -0.0006 to 0.1566).
- mhb_safety, family difference: Qwen versus Gemma: 0.0233 (Wald interval -0.0251 to 0.0718).
- mhb_safety, family difference: SmolLM versus Gemma: 0.0520 (Wald interval -0.0308 to 0.1347).
- mhb_safety, training-category difference: medical versus instruction parents: -0.0277 (Wald interval -0.0591 to 0.0036).
- mhb_safety, training-category difference: mental-health versus instruction parents: -0.0981 (Wald interval -0.1305 to -0.0656).
- mhb_safety, associated difference per doubling of parameter count: 0.0199 (Wald interval 0.0068 to 0.0329).
- mhb_safety, associated difference per version step: 0.0357 (Wald interval 0.0104 to 0.0610).

Marginal residuals are the score minus the fixed-effects prediction. They are not forced to average zero, because the random intercepts absorb lineage means. A score of 0 or 1 was left as 0 or 1.

- cssrs_f1: 73 residuals, 1 score at 0, 0 scores at 1, mean residual 0.0019, SD 0.1762. Fit converged: True.
- mhb_safety: 63 residuals, 0 scores at 0, 0 scores at 1, mean residual 0.0009, SD 0.0528. Fit converged: True.
- si_f1: 73 residuals, 3 scores at 0, 0 scores at 1, mean residual 0.0201, SD 0.1801. Fit converged: True.

## Paired mental-health analysis (primary)

For each mental-health fine-tune, delta is the child's score minus the canonical parent's score. Both scores are required. The mean delta is an intercept-only model with CRV3 standard errors by ancestry cluster. The reference distribution is a t distribution with degrees of freedom equal to the number of clusters minus 1. Benjamini-Hochberg adjustment is applied to the three fraction-scale tests and to nothing else. The intervals are ordinary 95 percent intervals.

All 18 mental-health fine-tunes had both scores on all three outcomes, so none was dropped.

- synthetic suicidal-ideation yes/no F1: mean delta -0.0871, SE 0.0401, interval -0.1731 to -0.0012, raw p 0.047281, BH p 0.070921, 18 children, 15 clusters, 14 inference degrees of freedom.
- C-SSRS yes/no F1: mean delta -0.0731, SE 0.0530, interval -0.1867 to 0.0406, raw p 0.189565, BH p 0.189565, 18 children, 15 clusters, 14 inference degrees of freedom.
- MentalHealthBench suicide/self-harm subset: mean delta -0.1109, SE 0.0205, interval -0.1548 to -0.0670, raw p 0.000090, BH p 0.000270, 18 children, 15 clusters, 14 inference degrees of freedom.

The MentalHealthBench mean difference is also -11.0916 percentage points (interval -15.4788 to -6.7044). That is the same test.

A nonsignificant result is not evidence of no difference. The clustered intervals describe dependence among checkpoints that share a parent. They do not resample benchmark items.
