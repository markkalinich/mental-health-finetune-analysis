# Joint description and paired mental-health differences

Roster snapshot: `/home/mkalinich/main/revision_3_experiments/hf_inventory/results/roster/2026-10-23/roster.csv` sha256 `633908d9cb8cb3bc74032d32c14b00942483d2ca736271d9b5cb4971fdd8b588`. The snapshot is `roster-snapshot.csv` in this directory. Counts below come from that file.

The cohort is 73 checkpoints: 25 instruction-tuned parents and 48 fine-tunes whose weight-update method and training objective are both stated (0 fine-tunes without both are listed in `unlabeled-fine-tunes.csv` and are not fit). Pretrained checkpoints are not included. `unsloth/gemma-3-1b-it` is `google/gemma-3-1b-it`. `unsloth/gemma-3-4b-it` is `google/gemma-3-4b-it`. Each pair is one checkpoint. The Google score is the score used. Unsloth scores that differ are listed in `rehost-score-conflicts.csv` and are not averaged in.

Scores that differ: google/gemma-3-1b-it si_f1: Google 0.71637, Unsloth 0.716612; google/gemma-3-1b-it cssrs_f1: Google 0.020202, Unsloth 0.033445; google/gemma-3-1b-it mhb_safety: Google 0.304124, Unsloth 0.278881; google/gemma-3-4b-it si_f1: Google 0.941704, Unsloth 0.944072; google/gemma-3-4b-it cssrs_f1: Google 0.767045, Unsloth 0.765714; google/gemma-3-4b-it mhb_safety: Google 0.333122, Unsloth 0.333061.

## Release rank

Version rank is the release order inside a family, written to `version-rank-mapping.csv` before either fit. Children inherit the parent's family and rank. Gemma 1 is rank 0 and Gemma 3 is rank 2, because Gemma 2 is the generation between them and is not in this roster. Gemma 3n is rank 3, one step after Gemma 3, and is not Gemma 4. All four Gemma 3n checkpoints, two instruction parents and two fine-tunes, enter as 2 and 4 billion effective parameters. Mistral 7B v0.2 and v0.3 share rank 0. SmolLM has one release. Neither Mistral nor SmolLM identifies the version slope.

The version coefficient is one linear change per rank step, shared by every family, after adjustment for log2 parameter count. It is an adjusted association, not a causal effect of a release. The steps that keep the same size label are Llama 3 to Llama 3.1 at 8B and Qwen3 to Qwen3.5 at 4B. The other steps also change which sizes are present. The list is `version-steps.csv`.

## Joint mixed model (secondary)

For each outcome separately: score on the 0–1 scale, log2 of the parameter count in billions, family (reference Gemma), version rank, and training category (reference instruction parent). Random intercept for the canonical instruction parent and its children. A parent is one row, not one row per child. REML. Intervals are Wald intervals. Gemma 3n E2B and E4B enter as 2 and 4 billion effective parameters. Safety fine-tunes are out of the MentalHealthBench model. An instruction-tuned parent is out of that model when no mental-health or medical fine-tune of that parent is in the study.

- synthetic suicidal-ideation yes/no F1: 73 checkpoints, 25 clusters, design full rank True, converged True, random-intercept variance 0.023467, residual variance 0.018878, Wald intervals supported True.
- C-SSRS yes/no F1: 73 checkpoints, 25 clusters, design full rank True, converged True, random-intercept variance 0.004848, residual variance 0.030146, Wald intervals supported True.
  statsmodels warned that the random-intercept variance may be on the boundary of its parameter space. That warning appears when a variance is below about 0.01. The rule used here treats a variance of 1e-08 or below as singular. This fit is above that line, so the Wald intervals are reported.
- MentalHealthBench suicide/self-harm subset: 61 checkpoints, 23 clusters, design full rank True, converged True, random-intercept variance 0.000843, residual variance 0.003113, Wald intervals supported True.
  statsmodels warned that the random-intercept variance may be on the boundary of its parameter space. That warning appears when a variance is below about 0.01. The rule used here treats a variance of 1e-08 or below as singular. This fit is above that line, so the Wald intervals are reported.

Coefficients below are on the 0–1 score scale.

- si_f1, fitted score at 1 billion parameters, Gemma, version rank 0, instruction parent: 0.5743 (Wald interval 0.3333 to 0.8153).
- si_f1, family difference: Llama versus Gemma: -0.0502 (Wald interval -0.2924 to 0.1919).
- si_f1, family difference: Mistral versus Gemma: -0.0347 (Wald interval -0.3988 to 0.3294).
- si_f1, family difference: Qwen versus Gemma: -0.0904 (Wald interval -0.3121 to 0.1314).
- si_f1, family difference: SmolLM versus Gemma: 0.0928 (Wald interval -0.2727 to 0.4582).
- si_f1, training-category difference: medical versus instruction parents: -0.0999 (Wald interval -0.1874 to -0.0125).
- si_f1, training-category difference: mental-health versus instruction parents: -0.0672 (Wald interval -0.1563 to 0.0218).
- si_f1, training-category difference: safety versus instruction parents: 0.0385 (Wald interval -0.0715 to 0.1485).
- si_f1, associated difference per doubling of parameter count: 0.1222 (Wald interval 0.0713 to 0.1730).
- si_f1, associated difference per version step: 0.0583 (Wald interval -0.0361 to 0.1527).
- cssrs_f1, fitted score at 1 billion parameters, Gemma, version rank 0, instruction parent: 0.2765 (Wald interval 0.0919 to 0.4611).
- cssrs_f1, family difference: Llama versus Gemma: 0.2049 (Wald interval 0.0294 to 0.3804).
- cssrs_f1, family difference: Mistral versus Gemma: 0.2609 (Wald interval -0.0144 to 0.5362).
- cssrs_f1, family difference: Qwen versus Gemma: 0.2503 (Wald interval 0.0845 to 0.4161).
- cssrs_f1, family difference: SmolLM versus Gemma: 0.2899 (Wald interval 0.0185 to 0.5612).
- cssrs_f1, training-category difference: medical versus instruction parents: -0.0953 (Wald interval -0.2017 to 0.0111).
- cssrs_f1, training-category difference: mental-health versus instruction parents: -0.0467 (Wald interval -0.1562 to 0.0629).
- cssrs_f1, training-category difference: safety versus instruction parents: 0.0297 (Wald interval -0.1036 to 0.1629).
- cssrs_f1, associated difference per doubling of parameter count: 0.0438 (Wald interval 0.0062 to 0.0814).
- cssrs_f1, associated difference per version step: 0.1252 (Wald interval 0.0547 to 0.1956).
- mhb_safety, fitted score at 1 billion parameters, Gemma, version rank 0, instruction parent: 0.1722 (Wald interval 0.1064 to 0.2381).
- mhb_safety, family difference: Llama versus Gemma: 0.0293 (Wald interval -0.0424 to 0.1010).
- mhb_safety, family difference: Mistral versus Gemma: 0.1329 (Wald interval 0.0337 to 0.2322).
- mhb_safety, family difference: Qwen versus Gemma: 0.0566 (Wald interval -0.0051 to 0.1183).
- mhb_safety, family difference: SmolLM versus Gemma: 0.0857 (Wald interval -0.0118 to 0.1831).
- mhb_safety, training-category difference: medical versus instruction parents: -0.0287 (Wald interval -0.0639 to 0.0065).
- mhb_safety, training-category difference: mental-health versus instruction parents: -0.1007 (Wald interval -0.1367 to -0.0647).
- mhb_safety, associated difference per doubling of parameter count: 0.0200 (Wald interval 0.0052 to 0.0348).
- mhb_safety, associated difference per version step: 0.0361 (Wald interval 0.0107 to 0.0615).

Marginal residuals are the score minus the fixed-effects prediction. They are not forced to average zero, because the random intercepts absorb lineage means. A score of 0 or 1 was left as 0 or 1.

- cssrs_f1: 73 residuals, 1 score at 0, 0 scores at 1, mean residual 0.0013, SD 0.1729. Fit converged: True.
- mhb_safety: 61 residuals, 0 scores at 0, 0 scores at 1, mean residual 0.0007, SD 0.0574. Fit converged: True.
- si_f1: 73 residuals, 3 scores at 0, 0 scores at 1, mean residual 0.0198, SD 0.1790. Fit converged: True.

## Paired mental-health analysis (primary)

For each mental-health fine-tune, delta is the child's score minus the canonical parent's score. Both scores are required. The mean delta is an intercept-only model with CRV3 standard errors by ancestry cluster. The reference distribution is a t distribution with degrees of freedom equal to the number of clusters minus 1. Benjamini-Hochberg adjustment is applied to the three fraction-scale tests and to nothing else. The intervals are ordinary 95 percent intervals.

All 18 mental-health fine-tunes had both scores on all three outcomes, so none was dropped.

- synthetic suicidal-ideation yes/no F1: mean delta -0.0871, SE 0.0401, interval -0.1731 to -0.0012, raw p 0.047281, BH p 0.070921, 18 children, 15 clusters, 14 inference degrees of freedom.
- C-SSRS yes/no F1: mean delta -0.0731, SE 0.0530, interval -0.1867 to 0.0406, raw p 0.189565, BH p 0.189565, 18 children, 15 clusters, 14 inference degrees of freedom.
- MentalHealthBench suicide/self-harm subset: mean delta -0.1145, SE 0.0219, interval -0.1615 to -0.0674, raw p 0.000130, BH p 0.000389, 18 children, 15 clusters, 14 inference degrees of freedom.

The MentalHealthBench mean difference is also -11.4476 percentage points (interval -16.1505 to -6.7446). That is the same test.

A nonsignificant result is not evidence of no difference. The clustered intervals describe dependence among checkpoints that share a parent. They do not resample benchmark items.
