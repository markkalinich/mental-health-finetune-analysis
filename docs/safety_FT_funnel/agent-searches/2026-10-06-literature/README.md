<!-- doc-verbosity: public-ready -->

# The 6 October 2026 safety literature search (agent write-ups)

Moved here on 9 October 2026 from `docs/safety_FT_funnel/literature/`. Nothing in the batch files
was changed.

**The prompt was not saved.** The agents were Cursor subagents running Grok 4.7 (high, fast) with
web search, about five models each. Each agent read the cached model card
(`revision_3_experiments/hf_inventory/cache/readmes/`, copies dated 2026-10-05 or 2026-10-06),
searched for a paper, a training script, or a dataset card about the repository, and wrote one
markdown section and one CSV row per model. A claim was kept only with a URL. The repository name
was not treated as evidence. The nearest description of the procedure is the mental-health
counterpart, `docs/mental_health_FT_funnel/agent-searches/2026-10-06-literature/README.md`.

**Which list it covered.** The 38 rows of `all-batches.csv` are the 31 safety models that were in
`results/cross-grouping/2026-10-06/final_models.csv` (the 6 October safety list of 53 after
`version_rule.py`) plus 7 models that were in the 6 October reading and were removed by hand on
6 October after the agents read them (`thu-coai/SeTox-Qwen2.5-3B`, `thu-coai/SeTox-Qwen2.5-7B`,
`umsa-v1/model_qwen2.5-gdpr_grupo5_final`, `Irfanuruchi/qwen2.5-32b-buildeng`,
`Hari5115/MoleculeIQ-SmolLM2-360M`, `ryo-llm/qwen3-4b-agent-trajectory-lora-alf-guard`,
`vominhmanh/qwen3-4b-vihsd`; their `manual_removals.csv` rows cite the batch that read them).
The 22 models of the 6 October 53 that `version_rule.py` removed have no write-up here.

This search did not add or remove a model from the funnel. It is not a funnel step. The current
safety list is `revision_3_experiments/hf_inventory/results/safety/<CURRENT>/kept.csv`; the
9 October extraction records for that list are in `../2026-10-09-extraction/`.

## Files

- `batch-1.md` to `batch-8.md`: one section per model, with the sources and quotes.
- `batch-1.csv` to `batch-8.csv`: one row per model, same columns as `all-batches.csv`.
- `all-batches.csv`: the eight batch CSVs merged (38 rows).
