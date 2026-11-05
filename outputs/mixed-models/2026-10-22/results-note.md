# Joint description and paired mental-health differences

Roster snapshot: `/home/mkalinich/main/revision_3_experiments/hf_inventory/results/roster/2026-10-20/roster.csv` sha256 `41f155ff46247992dfa2752fc1d052a967ba2242f613ab59a8f1dc0dba89cb80`. The snapshot is `roster-snapshot.csv` in this directory. Counts below come from that file.

The cohort is 73 checkpoints: 25 instruction-tuned parents and 48 fine-tunes. Pretrained checkpoints are not included. `unsloth/gemma-3-1b-it` is `google/gemma-3-1b-it`. `unsloth/gemma-3-4b-it` is `google/gemma-3-4b-it`. Each pair is one checkpoint. The Google score is the score used. Unsloth scores that differ are listed in `rehost-score-conflicts.csv` and are not averaged in.

Scores that differ: google/gemma-3-1b-it mhb_safety: Google 0.290333, Unsloth 0.263823; google/gemma-3-4b-it si_f1: Google 0.941704, Unsloth 0.944072; google/gemma-3-4b-it cssrs_f1: Google 0.767045, Unsloth 0.765714; google/gemma-3-4b-it mhb_safety: Google 0.311353, Unsloth 0.310691.

## Release rank

Version rank is the release order inside a family, written to `version-rank-mapping.csv` before either fit. Children inherit the parent's family and rank. Gemma 3n is flagged as ambiguous because it is a parallel line, not a numbered successor. All four Gemma 3n checkpoints, two instruction parents and two fine-tunes, have E2B or E4B sizes, so that step is not in the joint model. SmolLM has one release, so it does not identify the version slope.

The version coefficient is one linear change per rank step, shared by every family, after adjustment for log2 parameter count. It is an adjusted association, not a causal effect of a release. The steps that keep the same size label are Llama 3 to Llama 3.1 at 8B, Mistral v0.2 to v0.3 at 7B, and Qwen3 to Qwen3.5 at 4B. The other steps also change which sizes are present. The list is `version-steps.csv`.

## Joint mixed model (secondary)

For each outcome separately: score on the 0–1 scale, log2 of the parameter count in billions, family (reference Gemma), version rank, and training category (reference instruction parent). Random intercept for the canonical instruction parent and its children. A parent is one row, not one row per child. REML. Intervals are Wald intervals. E2B and E4B checkpoints are out of this model only. Safety checkpoints, including Cradle, are out of the MentalHealthBench model only.

- synthetic suicidal-ideation yes/no F1: 69 checkpoints, 23 clusters, design full rank True, converged True, random-intercept variance 0.027645, residual variance 0.019648, Wald intervals supported True.
- C-SSRS yes/no F1: 69 checkpoints, 23 clusters, design full rank True, converged True, random-intercept variance 0.005950, residual variance 0.031975, Wald intervals supported True.
  statsmodels warned that the random-intercept variance may be on the boundary of its parameter space. That warning appears when a variance is below about 0.01. The rule used here treats a variance of 1e-08 or below as singular. This fit is above that line, so the Wald intervals are reported.
- MentalHealthBench suicide/self-harm subset: 43 checkpoints, 18 clusters, design full rank True, converged False, random-intercept variance 0.000266, residual variance 0.002972, Wald intervals supported False.
  Fit note: Optimization did not converge. The coefficient values are the optimizer's last position, not a completed fit. No other optimizer or formula was tried.
  Warning: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals | ConvergenceWarning: Retrying MixedLM optimization with lbfgs | ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals | ConvergenceWarning: Retrying MixedLM optimization with cg | ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals | ConvergenceWarning: MixedLM optimization failed, trying a different optimizer may help. | ConvergenceWarning: Gradient optimization failed, |grad| = 1.989785 | ConvergenceWarning: The MLE may be on the boundary of the parameter space.

Coefficients below are on the 0–1 score scale.

- si_f1, fitted score at 1 billion parameters, Gemma, version rank 0, instruction parent: 0.6278 (Wald interval 0.4159 to 0.8397).
- si_f1, family difference: Llama versus Gemma: -0.0901 (Wald interval -0.3696 to 0.1894).
- si_f1, family difference: Mistral versus Gemma: -0.1104 (Wald interval -0.4657 to 0.2448).
- si_f1, family difference: Qwen versus Gemma: -0.1339 (Wald interval -0.3749 to 0.1072).
- si_f1, family difference: SmolLM versus Gemma: 0.0421 (Wald interval -0.3187 to 0.4030).
- si_f1, training-category difference: medical versus instruction parents: -0.1055 (Wald interval -0.1979 to -0.0132).
- si_f1, training-category difference: mental-health versus instruction parents: -0.0725 (Wald interval -0.1665 to 0.0215).
- si_f1, training-category difference: safety versus instruction parents: 0.0364 (Wald interval -0.0769 to 0.1496).
- si_f1, associated difference per doubling of parameter count: 0.1222 (Wald interval 0.0663 to 0.1782).
- si_f1, associated difference per version step: 0.0493 (Wald interval -0.0742 to 0.1727).
- cssrs_f1, fitted score at 1 billion parameters, Gemma, version rank 0, instruction parent: 0.3686 (Wald interval 0.2089 to 0.5283).
- cssrs_f1, family difference: Llama versus Gemma: 0.1494 (Wald interval -0.0462 to 0.3449).
- cssrs_f1, family difference: Mistral versus Gemma: 0.1345 (Wald interval -0.1298 to 0.3988).
- cssrs_f1, family difference: Qwen versus Gemma: 0.1894 (Wald interval 0.0159 to 0.3628).
- cssrs_f1, family difference: SmolLM versus Gemma: 0.1879 (Wald interval -0.0746 to 0.4503).
- cssrs_f1, training-category difference: medical versus instruction parents: -0.1013 (Wald interval -0.2150 to 0.0124).
- cssrs_f1, training-category difference: mental-health versus instruction parents: -0.0500 (Wald interval -0.1675 to 0.0675).
- cssrs_f1, training-category difference: safety versus instruction parents: 0.0378 (Wald interval -0.1012 to 0.1768).
- cssrs_f1, associated difference per doubling of parameter count: 0.0379 (Wald interval -0.0030 to 0.0789).
- cssrs_f1, associated difference per version step: 0.1048 (Wald interval 0.0163 to 0.1933).

MentalHealthBench suicide/self-harm subset: the mixed model did not produce a usable fit, so no coefficient from it is reported here. The optimizer's last values are stored in `estimates.csv` with blank standard errors and are not completed estimates. The formula was not changed.

Marginal residuals are the score minus the fixed-effects prediction. They are not forced to average zero, because the random intercepts absorb lineage means. A score of 0 or 1 was left as 0 or 1.

- cssrs_f1: 69 residuals, 1 score at 0, 0 scores at 1, mean residual 0.0025, SD 0.1783. Fit converged: True.
- mhb_safety: 43 residuals, 0 scores at 0, 0 scores at 1, mean residual 0.0008, SD 0.0501. Fit converged: False.
- si_f1: 69 residuals, 3 scores at 0, 0 scores at 1, mean residual 0.0220, SD 0.1849. Fit converged: True.

## Paired mental-health analysis (primary)

For each mental-health fine-tune, delta is the child's score minus the canonical parent's score. Both scores are required. The mean delta is an intercept-only model with CRV3 standard errors by ancestry cluster. The reference distribution is a t distribution with degrees of freedom equal to the number of clusters minus 1. Benjamini-Hochberg adjustment is applied to the three fraction-scale tests and to nothing else. The intervals are ordinary 95 percent intervals.

All 18 mental-health fine-tunes had both scores on all three outcomes, so none was dropped. That sample includes the E2B mental-health fine-tune excluded from the joint model.

- synthetic suicidal-ideation yes/no F1: mean delta -0.0871, SE 0.0401, interval -0.1731 to -0.0012, raw p 0.047281, BH p 0.070921, 18 children, 15 clusters, 14 inference degrees of freedom.
- C-SSRS yes/no F1: mean delta -0.0731, SE 0.0530, interval -0.1867 to 0.0406, raw p 0.189565, BH p 0.189565, 18 children, 15 clusters, 14 inference degrees of freedom.
- MentalHealthBench suicide/self-harm subset: mean delta -0.1109, SE 0.0205, interval -0.1548 to -0.0670, raw p 0.000090, BH p 0.000270, 18 children, 15 clusters, 14 inference degrees of freedom.

The MentalHealthBench mean difference is also -11.0916 percentage points (interval -15.4788 to -6.7044). That is the same test.

Cradle (`SungJoo/cradle-dialogue-qwen3-32b-2epoch`) is a safety model. Its MentalHealthBench paired difference is 0.0232 (2.3186 percentage points). No standard error is attached. It is not in the MentalHealthBench joint model.

A nonsignificant result is not evidence of no difference. The clustered intervals describe dependence among checkpoints that share a parent. They do not resample benchmark items.
