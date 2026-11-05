# Inference settings

Python 3.9.25. pyfixest 0.28.0. statsmodels 0.14.6.

pyfixest 0.28.0 from PyPI does not import on Python 3.9 because `report/summarize.py` annotates two `dtable` arguments as `dict | None`. Those two annotations were edited to `Optional[dict]` in the installed copy. `Optional` was already imported in that file. No other pyfixest file was edited. The installed version remains 0.28.0. pandas, numpy, scipy, and statsmodels were not upgraded.

CRV3 smoke test, run before any study fit: formula `y ~ 1`, vcov `{'CRV3': 'g'}`, estimate 0.2833333333333334, standard error 0.11924240017711818.

Primary formula: `delta_score ~ 1`.
Covariance: `{'CRV3': 'ancestry_cluster_id'}`.
Small-sample settings read back from the fit: `adj=True`, `fixef_k='none'`, `cluster_adj=True`, `cluster_df='min'`.
Numeric multiplier applied to the jackknife covariance: `(N-1)/(N-k) * G/(G-1)`.
For the intercept-only primary fit this reduces to `G/(G-1)` because `k=1`.
CRV3 implementation: leave-one-cluster-out coefficients, centered at the full-sample coefficient, summed as outer products. The primary model has no absorbed fixed effects, so pyfixest used `_vcov_crv3_fast`.
Reference distribution: two-sided Student t. Inference degrees of freedom: `G - 1`.
The p-value is `2 * (1 - t.cdf(|estimate / SE|, G - 1))` against zero.
The ordinary 95% interval is `estimate ± t_{0.975, G-1} * SE`.
Residual degrees of freedom (`N - k`) are not the inference degrees of freedom.
Benjamini-Hochberg (`statsmodels.stats.multitest.multipletests`, method `fdr_bh`) applies only to the three primary fraction-scale mental-health p-values. Holm was not used.
The intervals are not multiplicity-adjusted.

Mixed model: `statsmodels` `MixedLM`, `reml=True`, default optimizer sequence bfgs then lbfgs then cg, `re_formula='1'`.
Formula for the pooled model: `delta_score ~ 0 + C(category)`.
Formula for the mental-health-only sensitivity: `delta_score ~ 1`.
One random-intercept variance and one residual variance.
`MixedLMResults.use_t` is False. The interval is a Wald interval from the standard normal. It is not Kenward-Roger or Satterthwaite.
Singularity rule: a fit is singular if the estimated random-intercept variance is <= 1e-08.
Convergence alone is not treated as identification.
statsmodels also warns when a random-effect variance is below 0.01. That warning is recorded and is not the singularity rule, because 0.01 is not zero on a 0-1 score.
A fit is treated as unusable for Wald inference if it does not converge, if it is singular under the rule above, if statsmodels warns that the random-effects covariance is singular, or if statsmodels warns that the Hessian is not positive definite.
An unusable mixed model is reported and is not replaced.

statsmodels clustered covariance was not used. In statsmodels 0.14.6 that covariance is CR0 without a finite-sample correction and CR1 with that correction. Neither is CRV3.

Category description formula: `delta_score ~ 0 + C(category)`. Point estimates only.
Size formula: `score ~ log10_param_billions + C(category)`, CRV3 on `ancestry_cluster_id`, reference category mental-health.

Primary fit audit (fraction scale):

- si_f1: N=18, k=1, G=15, inference df=14, ssc multiplier=1.0714285714285714, residual df not used=17.
- cssrs_f1: N=18, k=1, G=15, inference df=14, ssc multiplier=1.0714285714285714, residual df not used=17.
- mhb_safety: N=18, k=1, G=15, inference df=14, ssc multiplier=1.0714285714285714, residual df not used=17.

Mixed-model fits:

- pooled_si_f1: converged=True, singular=True, random-intercept variance=2.203141421671222e-09, residual variance=0.02964917903629974, singleton clusters=12 of 25, inference usable=False.
  Warnings: ConvergenceWarning: The MLE may be on the boundary of the parameter space.
- mental_health_only_si_f1: converged=True, singular=False, random-intercept variance=0.021150523379252453, residual variance=0.008169048922896759, singleton clusters=12 of 15, inference usable=True.
- pooled_cssrs_f1: converged=True, singular=False, random-intercept variance=0.015786749870679292, residual variance=0.037287437822026835, singleton clusters=12 of 25, inference usable=True.
- mental_health_only_cssrs_f1: converged=True, singular=True, random-intercept variance=2.9104437799737736e-10, residual variance=0.04580674183108175, singleton clusters=12 of 15, inference usable=False.
  Warnings: ConvergenceWarning: The MLE may be on the boundary of the parameter space.
- pooled_mhb_safety: converged=True, singular=False, random-intercept variance=0.0021962717680485207, residual variance=0.003940448946691714, singleton clusters=9 of 16, inference usable=True.
  Warnings: ConvergenceWarning: The MLE may be on the boundary of the parameter space.
- mental_health_only_mhb_safety: converged=True, singular=True, random-intercept variance=2.031915669480768e-10, residual variance=0.006869593186192814, singleton clusters=12 of 15, inference usable=False.
  Warnings: ConvergenceWarning: The MLE may be on the boundary of the parameter space.
