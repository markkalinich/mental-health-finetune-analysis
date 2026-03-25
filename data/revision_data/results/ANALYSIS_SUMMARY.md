# Psychiatrist agreement analysis (revision)

This folder holds **derived results** from the dual-psychiatrist review spreadsheets. Raw revision inputs (blinded statement lists) remain under `data/revision_data/` at the repository root; this `results/` subfolder keeps tables and narrative separate from those files.

## Question

Reviewers asked for inter-rater agreement between psychiatrist 1 (P1) and psychiatrist 2 (P2). The study design is **not** a fully crossed, parallel double review of identical stimuli for every item: P1 reviewed first and could edit text; P2’s ratings sometimes apply to different versions of the text, and some items were not initially sent to P2.

For items where **P1 retained the model output verbatim** (`Psychiatrist_01 == KEPT_exact_match`), both psychiatrists are evaluating the **same** model-generated string. On that subset, a descriptive summary of how often P2 also endorsed the item (under a clearly defined coding rule) is appropriate.

## Data sources

| Task | File (under `data/inputs/intermediate_files/`) |
|------|------------------------------------------------|
| Suicidal ideation (SI) | `SI_psychiatrist_01_and_02_scores.csv` |
| Therapy request | `therapy_request_psychiatrist_01_and_02_scores.csv` |
| Therapy engagement | `therapy_engagement_psychiatrist_01_and_02_scores.csv` |

Columns used: `Psychiatrist_01`, `Psychiatrist_02`.

**Therapy engagement:** The CSV has **four lines per conversation** (one per turn). `Psychiatrist_01` / `Psychiatrist_02` are **identical across turns** for a given `Example_ID`. All therapy-engagement statistics below use **one row per conversation** (450 conversations in the file), not 1800 turn-level rows.

## Analysis definition

1. **Subset:** All **items** with **`Psychiatrist_01 == KEPT_exact_match`**.  
   Interpretation: P1 judged the model’s wording acceptable without edits; this is the set where P2’s label applies to that same surface text (assuming the review workflow preserved that).

2. **Outcome (P2 “positive” / agreement):**
   - **SI and therapy request:** `Psychiatrist_02 == KEPT`.  
     On this subset, P2’s recorded values are `KEPT` or `REMOVED` only.
   - **Therapy engagement:** P2 uses different labels (`KEPT_exact_match`, `KEPT_with_changes`, `REMOVED`). Two summaries are reported:
     - **Not removed:** `KEPT_exact_match` **or** `KEPT_with_changes` (P2 kept the turn in some form).
     - **Exact match only:** `KEPT_exact_match` (closest parallel to “as-is” approval in SI/TR).

3. **Uncertainty:** **95% Wilson score intervals** for the binomial proportion \(n_{\text{positive}} / n\). Wilson intervals are preferred to the normal approximation for proportions, especially away from 0.5.

## Results (point estimates and 95% Wilson CIs)

Regenerate the numeric table by running the script (see below); values should match `p2_agreement_given_p1_exact_match.csv`.

| Dataset | n (P1 exact match) | Definition of P2 positive | Proportion | 95% CI |
|---------|-------------------|-----------------------------|------------|--------|
| SI | 822 | P2 == KEPT | 0.968 | [0.954, 0.978] |
| Therapy request | 1119 | P2 == KEPT | 0.990 | [0.982, 0.995] |
| Therapy engagement | 363 (conversations) | P2 not removed | 0.986 | [0.968, 0.994] |
| Therapy engagement | 363 (conversations) | P2 exact match only | 0.981 | [0.961, 0.991] |

**Counts:** SI: 796/822; therapy request: 1108/1119; therapy engagement: 358/363 (not removed), 356/363 (exact match only).

## What this is not

- **Not** symmetric Cohen’s κ between P1 and P2 on this subset alone: on the P1-exact-match subset, P1’s label is **constant** by construction, so a standard two-rater κ with varying marginals for both raters is degenerate.
- **Not** a substitute for a pre-specified fully crossed design; caveats belong in the reviewer response (workflow, blinding, and any re-rating of previously unseen items).

## Reproducibility

From the repository root:

```bash
python analysis/revision/compute_p2_agreement.py
python analysis/revision/compute_kappa_verbatim_bounds.py
python analysis/revision/compute_kappa_sensitivity.py
```

Outputs:

- `data/revision_data/results/p2_agreement_given_p1_exact_match.csv` — conditional proportions (Wilson CIs).
- `data/revision_data/results/kappa_verbatim_optimistic_pessimistic.csv` — Cohen’s κ (verbatim optimistic / pessimistic; **primary reviewer-facing bounds**).
- `data/revision_data/results/kappa_verbatim_complete_cases.csv` — verbatim κ on jointly rated items only.
- `data/revision_data/results/kappa_sensitivity_binary_keep_remove.csv` — alternative κ sensitivity (binary keep/remove only).

Implementations: `analysis/revision/compute_p2_agreement.py`, `analysis/revision/compute_kappa_verbatim_bounds.py`, `analysis/revision/compute_kappa_sensitivity.py`. Shared helper: `analysis/revision/therapy_engagement_conversations.py` (dedupe by `Example_ID`).

---

## Post-hoc psychiatrist 2 merge and full-sample Cohen’s κ

When psychiatrist 2 later rated items that were missing in the original export, those CSVs live under `data/revision_data/psychiatrist02_review/` (`keep` / `remove` / `change`, lowercase). The script **`analysis/revision/posthoc_merge_and_kappa.py`**:

1. **Join key:** SI and therapy request — `(Safety type, Counseling Request, original_statement)`; therapy engagement — `Example_ID` on **conversation-deduped** rows (450 conversations).
2. **Rule:** If a revision row exists for that key, **`Psychiatrist_02` is replaced** by the mapped canonical label (`keep`→`KEPT` [SI/TR] or `KEPT_exact_match` [TE], `remove`→`REMOVED`, `change`→`KEPT_with_changes`); otherwise the original intermediate value is kept.
3. **Outputs:** merged tables in `data/revision_data/merged/` (adds `Psychiatrist_02_source` = `revision_posthoc` or `original`), `posthoc_merge_validation.csv`, and **`posthoc_kappa_merged.csv`** (Cohen’s κ with bootstrap 95% CIs).
4. **κ definition (single primary metric):** Each rater is coded **binary** — **as-is OK** (“keep”) vs **not as-is OK** (“change” or “remove”, combined). P1 as-is = `KEPT_exact_match`; not as-is = `KEPT_with_changes` or `REMOVED`. P2 as-is = `KEPT` (SI and therapy request) or `KEPT_exact_match` (therapy engagement); not as-is = `KEPT_with_changes` or `REMOVED`. Cohen’s κ is computed on this paired binary coding over the full merged N (metric column `as_is_agreement`).

```bash
python analysis/revision/posthoc_merge_and_kappa.py
```

**Validation (current files):** SI 178 revision rows applied, 0 missing P2 after merge; therapy request 81; therapy engagement 87 conversations updated, 363 unchanged.

| Dataset | N | As-is agreement κ (95% CI) |
|---------|---|------------------------------|
| SI | 1000 statements | 0.852 (0.808, 0.893) |
| Therapy request | 1200 statements | 0.758 (0.675, 0.832) |
| Therapy engagement | 450 conversations | 0.556 (0.446, 0.654) |

Regenerate with `python analysis/revision/posthoc_merge_and_kappa.py` for exact values in `posthoc_kappa_merged.csv`.

**Caveats:** Post-hoc P2 ratings are not blind to the original workflow; harmonization choices and stimulus alignment limits from earlier discussion still apply.

---

## Cohen’s κ — optimistic / pessimistic (verbatim “parallel evaluation”)

**Script:** `analysis/revision/compute_kappa_verbatim_bounds.py` → `kappa_verbatim_optimistic_pessimistic.csv`.

**Scale:** Both raters represented as binary **endorsement of the model text verbatim** (`R1` / `R2`).

- **R1 = True** iff `Psychiatrist_01 == KEPT_exact_match`, else False.

**P2 “kept without changes” (verbatim OK):**

- **SI & therapy request:** `Psychiatrist_02 == KEPT` (only `KEPT` / `REMOVED` / `NA` appear).
- **Therapy engagement:** `Psychiatrist_02 == KEPT_exact_match`.

**Optimistic (best-case κ):**

- **P1 = KEPT_exact_match:** concord if P2 is verbatim OK; discord if P2 modified or removed. If `Psychiatrist_02 == NA`, impute verbatim OK.
- **P1 = REMOVED or KEPT_with_changes:** **automatic concordance** — set `R2 = R1` (both False), i.e. neither endorses verbatim.

**Pessimistic (worst-case κ):**

- **P1 = KEPT_exact_match:** concord only if P2 verbatim OK; if `Psychiatrist_02 == NA`, impute not verbatim OK.
- **P1 = REMOVED or KEPT_with_changes:** **automatic discordance** — set `R2 = not R1` (here `R2 = True` while `R1 = False`).

Cohen’s κ is then computed on `(R1, R2)` over **all items** (for therapy engagement: **450 conversations**, not turn-level rows).

**95% confidence intervals:** Bootstrap percentile intervals (row resampling with replacement, 5000 draws, seed 42). These describe **resampling stability** of κ under the fixed coding rules; they are **not** a population-inference CI unless the rows are treated as an i.i.d. sample from a larger population. See `ci_method` in the CSV.

### Results

| Dataset | n | P1 verbatim (n) | Missing P2 where P1 verbatim | Optimistic κ (95% CI) | Pessimistic κ (95% CI) |
|---------|---|-----------------|------------------------------|-------------------------|--------------------------|
| SI | 1000 | 822 | 0* | 0.916 (0.883, 0.946) | −0.048 (−0.064, −0.032) |
| Therapy request | 1200 | 1119 | 0* | 0.931 (0.887, 0.969) | −0.016 (−0.025, −0.008) |
| Therapy engagement | 450 | 363 | 0 | 0.952 (0.912, 0.985) | −0.030 (−0.051, −0.009) |

\*In the current SI and therapy-request files, every `Psychiatrist_02 == NA` row has `Psychiatrist_01 == REMOVED`, so there are no missing P2 ratings on the `KEPT_exact_match` stratum; optimistic vs pessimistic imputation for missing P2 does not change those datasets. Differences between optimistic and pessimistic κ there come from the **auto concord / auto discord** rules on `REMOVED` and `KEPT_with_changes` rows.

### Complete cases — verbatim κ with no imputation (`kappa_verbatim_complete_cases.csv`)

Same verbatim **R1** / **R2** definitions as above, but **only rows where `Psychiatrist_02` is not `NA`**. No optimistic/pessimistic rules.

| Dataset | Complete pairs | Excluded (P2 NA) | κ | 95% bootstrap CI | Notes |
|---------|----------------|------------------|---|-------------------|--------|
| SI | 852 | 148 | 0.069 | (−0.032, 0.181) | R1 and R2 both vary |
| Therapy request | 1119 | 81 | 0.000 | (0, 0) | **Degenerate:** in this file, every row with P2 has `Psychiatrist_01 == KEPT_exact_match` only (no `KEPT_with_changes` category), so **R1 is always True** — κ is not informative |
| Therapy engagement | 450 | 0 | 0.366 | (0.253, 0.475) | Both vary |

Regenerate with `python analysis/revision/compute_kappa_verbatim_bounds.py` (writes this file alongside the optimistic/pessimistic CSV).

### Pessimistic SI: what the 178 non–verbatim P1 rows mean

`1000 − 822 = 178` rows have **`Psychiatrist_01 ≠ KEPT_exact_match`** (148 `REMOVED` + 30 `KEPT_with_changes` in the current SI file).

The **pessimistic** rule does **not** assert that “P2 actually rated each of these and disagreed.” It **constructs** a worst-case binary `R2` for κ: **R1 = False** (P1 did not endorse verbatim) and **R2 = True** (as if P2 endorsed verbatim), so those rows are **forced discordant** on the verbatim binary scale.

Substantively, those **148** `REMOVED` rows are exactly where **`Psychiatrist_02` is `NA`** in the sheet—so P2 did **not** provide a rating there. The **30** `KEPT_with_changes` rows **do** have P2 ratings; the pessimistic scenario **overrides** their observed `R2` for this sensitivity analysis (per the auto-discord rule). So “never seen exactly as the model provided by P2” is **not** a uniform description of all 178 rows; it is **literally** true for the rows with P2 `NA`, but the pessimistic κ is driven by the **assumed** worst-case `R2` on the binary scale, not by observed P2 behavior on every row.

### Are these the “true” absolute min/max κ?

They are the κ values **implied by your explicit completion rules**: verbatim binary scale, optimistic vs pessimistic handling of non-exact P1 rows, and imputation for missing P2 on exact rows when present.

They are **not** guaranteed to be the mathematical min/max over **every** hypothetical parallel P2 completion without those rules. For example, if you later observe P2 on `REMOVED` / `KEPT_with_changes` rows, those ratings might not correspond to `R2 = 0` or `R2 = 1` as forced here, so realized κ could lie **outside** this interval. The interval is best described as **bounds under the stated optimistic/pessimistic parallel-review assumptions**, not as a universal envelope over all possible completions.

---

## Cohen’s κ sensitivity (missing P2): binary harmonization (alternative)

**Goal:** Give reviewer-facing **worst-case** and **best-case** Cohen’s κ when some rows have `Psychiatrist_02 == NA` (P2 not yet / not originally rated).

**Harmonization (same for all tasks):** collapse both raters to **binary keep vs remove**.

| Rater | “Keep” | “Remove” |
|-------|--------|----------|
| P1 | `KEPT_exact_match`, `KEPT_with_changes` | `REMOVED` |
| P2 (SI, therapy request) | `KEPT` | `REMOVED` |
| P2 (therapy engagement) | `KEPT_exact_match`, `KEPT_with_changes` | `REMOVED` |

**Scenarios**

1. **Complete cases only:** κ on rows where P2 is not `NA`.  
2. **Worst case:** all rows; each missing P2 is imputed to the binary value that **disagrees** with P1 (keep vs remove).  
3. **Best case:** all rows; each missing P2 is imputed to **agree** with P1 on that binary.

Therapy engagement currently has **no** missing P2, so all three scenarios coincide.

### Results (regenerate with `compute_kappa_sensitivity.py`)

| Dataset | n | P2 missing | Complete-case κ | Worst κ | Best κ |
|---------|---|------------|-------------------|---------|--------|
| SI | 1000 | 148 | 0.000 | −0.051 | 0.894 |
| Therapy request | 1200 | 81 | 0.000 | −0.016 | 0.931 |
| Therapy engagement | 450 | 0 | 0.600 | 0.600 | 0.600 |

**Why complete-case κ is 0 for SI and therapy request:** In these files, whenever P2 is observed, P1 is **never** `REMOVED` (every `P1 == REMOVED` row has `P2 == NA`). On the complete-case subset, P1’s binary label is **always “keep”**, so κ is **degenerate** (observed agreement equals chance agreement under the κ formula). The **worst/best imputation** scenarios restore variation in P1 by including P1-removed rows with imputed P2, so those κ values are the meaningful sensitivity bracket for missing P2 under this coding.

### Caveats (reviewer language)

- Bounds are for **binary** keep/remove after harmonization, not for the full multi-label coding.
- With **only** binary missingness, corner imputations bracket κ among completions that use only **keep** or **remove** for each missing cell; they do not replace a confidence interval for κ once P2 is fully observed.
- For **more than two** outcome categories, global min/max κ over all imputations may require more than two corner patterns; binary collapse avoids that here by design.
