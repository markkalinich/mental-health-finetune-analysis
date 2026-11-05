# Joint description and fine-tune-minus-parent differences

Roster snapshot: `/home/mkalinich/main/revision_3_experiments/hf_inventory/results/roster/2026-10-23/roster.csv` sha256 `633908d9cb8cb3bc74032d32c14b00942483d2ca736271d9b5cb4971fdd8b588`. The snapshot is `roster-snapshot.csv` in this directory. Counts below come from that file.

The cohort is 73 checkpoints: 25 instruction-tuned parents and 48 fine-tunes whose weight-update method and training objective are both stated (0 fine-tunes without both are listed in `unlabeled-fine-tunes.csv` and are not fit). Pretrained checkpoints are not included. `unsloth/gemma-3-1b-it` is `google/gemma-3-1b-it`. `unsloth/gemma-3-4b-it` is `google/gemma-3-4b-it`. Each pair is one checkpoint. The Google score is the score used. Unsloth scores that differ are listed in `rehost-score-conflicts.csv` and are not averaged in.

Scores that differ: google/gemma-3-1b-it si_f1: Google 0.7163695299837926, Unsloth 0.716612377850163; google/gemma-3-1b-it cssrs_f1: Google 0.0202020202020202, Unsloth 0.033444816053511704; google/gemma-3-1b-it mhb_safety: Google 0.304124, Unsloth 0.278881; google/gemma-3-4b-it si_f1: Google 0.8936170212765957, Unsloth 0.8997867803837954; google/gemma-3-4b-it cssrs_f1: Google 0.7652916073968706, Unsloth 0.7639484978540773; google/gemma-3-4b-it mhb_safety: Google 0.333122, Unsloth 0.333061.

## Release rank

Version rank is the release order inside a family, written to `version-rank-mapping.csv` before either fit. Children inherit the parent's family and rank. Gemma 1 is rank 0 and Gemma 3 is rank 2, because Gemma 2 is the generation between them and is not in this roster. Gemma 3n is rank 3, one step after Gemma 3, and is not Gemma 4. All four Gemma 3n checkpoints, two instruction parents and two fine-tunes, enter as 2 and 4 billion effective parameters. Mistral 7B v0.2 and v0.3 share rank 0. SmolLM has one release. Neither Mistral nor SmolLM identifies the version slope.

The version coefficient is one linear change per rank step, shared by every family, after adjustment for log2 parameter count. It is an adjusted association, not a causal effect of a release. The steps that keep the same size label are Llama 3 to Llama 3.1 at 8B and Qwen3 to Qwen3.5 at 4B. The other steps also change which sizes are present. The list is `version-steps.csv`.

## Joint mixed model (secondary)

For each outcome separately: score on the 0–1 scale, log2 of the parameter count in billions, family (reference Gemma), version rank, and training category (reference instruction parent). Random intercept for the canonical instruction parent and its children. A parent is one row, not one row per child. REML. Intervals are Wald intervals. Gemma 3n E2B and E4B enter as 2 and 4 billion effective parameters. Safety fine-tunes are out of the MentalHealthBench model. An instruction-tuned parent is out of that model when no mental-health or medical fine-tune of that parent is in the study.

- synthetic suicidal-ideation yes/no F1: 73 checkpoints, 25 clusters, design full rank True, converged True, random-intercept variance 0.033577, residual variance 0.040889, Wald intervals supported True.
- C-SSRS yes/no F1: 73 checkpoints, 25 clusters, design full rank True, converged True, random-intercept variance 0.011569, residual variance 0.040011, Wald intervals supported True.
- MentalHealthBench suicide/self-harm subset: 61 checkpoints, 23 clusters, design full rank True, converged True, random-intercept variance 0.000843, residual variance 0.003113, Wald intervals supported True.
  statsmodels warned that the random-intercept variance may be on the boundary of its parameter space. That warning appears when a variance is below about 0.01. The rule used here treats a variance of 1e-08 or below as singular. This fit is above that line, so the Wald intervals are reported.

Coefficients below are on the 0–1 score scale.

- si_f1, fitted score at 1 billion parameters, Gemma, version rank 0, instruction parent: 0.3455 (Wald interval 0.0372 to 0.6538).
- si_f1, family difference: Llama versus Gemma: 0.0709 (Wald interval -0.2358 to 0.3776).
- si_f1, family difference: Mistral versus Gemma: -0.1454 (Wald interval -0.6097 to 0.3189).
- si_f1, family difference: Qwen versus Gemma: 0.0767 (Wald interval -0.2057 to 0.3591).
- si_f1, family difference: SmolLM versus Gemma: 0.1147 (Wald interval -0.3503 to 0.5797).
- si_f1, training-category difference: medical versus instruction parents: -0.1468 (Wald interval -0.2748 to -0.0189).
- si_f1, training-category difference: mental-health versus instruction parents: -0.0194 (Wald interval -0.1498 to 0.1110).
- si_f1, training-category difference: safety versus instruction parents: 0.0640 (Wald interval -0.0967 to 0.2248).
- si_f1, associated difference per doubling of parameter count: 0.1113 (Wald interval 0.0466 to 0.1759).
- si_f1, associated difference per version step: 0.1333 (Wald interval 0.0133 to 0.2534).
- cssrs_f1, fitted score at 1 billion parameters, Gemma, version rank 0, instruction parent: 0.2153 (Wald interval -0.0184 to 0.4490).
- cssrs_f1, family difference: Llama versus Gemma: 0.2133 (Wald interval -0.0125 to 0.4390).
- cssrs_f1, family difference: Mistral versus Gemma: 0.2612 (Wald interval -0.0884 to 0.6107).
- cssrs_f1, family difference: Qwen versus Gemma: 0.2664 (Wald interval 0.0549 to 0.4778).
- cssrs_f1, family difference: SmolLM versus Gemma: 0.3046 (Wald interval -0.0416 to 0.6508).
- cssrs_f1, training-category difference: medical versus instruction parents: -0.1451 (Wald interval -0.2690 to -0.0212).
- cssrs_f1, training-category difference: mental-health versus instruction parents: -0.0474 (Wald interval -0.1744 to 0.0797).
- cssrs_f1, training-category difference: safety versus instruction parents: 0.0354 (Wald interval -0.1199 to 0.1906).
- cssrs_f1, associated difference per doubling of parameter count: 0.0450 (Wald interval -0.0031 to 0.0930).
- cssrs_f1, associated difference per version step: 0.1551 (Wald interval 0.0653 to 0.2448).
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

- cssrs_f1: 73 residuals, 7 scores at 0, 0 scores at 1, mean residual 0.0040, SD 0.2081. Fit converged: True.
- mhb_safety: 61 residuals, 0 scores at 0, 0 scores at 1, mean residual 0.0007, SD 0.0574. Fit converged: True.
- si_f1: 73 residuals, 11 scores at 0, 0 scores at 1, mean residual 0.0200, SD 0.2420. Fit converged: True.

## Fine-tune minus instruction-tuned parent

category-deltas.csv holds the equal-weight mean of fine-tune minus instruction-tuned parent for mental-health, medical, and safety. Each fine-tune type is an intercept-only model with CRV3 standard errors by ancestry cluster. Safety has no MentalHealthBench rows. Table S4 recomputes Benjamini-Hochberg across the tests it displays.
