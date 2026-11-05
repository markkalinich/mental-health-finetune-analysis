---
license: cc-by-nc-4.0
base_model: Qwen/Qwen3-8B
library_name: transformers
pipeline_tag: text-generation
language:
  - en
tags:
  - medical
  - clinical-reasoning
  - qlora
  - benchmark-contamination
  - evaluation-methodology
---

# Diagnostic-Reasoning-Q3X1

A QLoRA fine-tune of **Qwen3-8B** for medical question answering, released as the evaluated artifact for a study of **training-corpus overlap in medical language model benchmarks**.

> **Read this first.** An earlier version of this card reported an average of 76.4% across seven medical benchmarks and a +24.2-point gain over the parent checkpoint. **Those figures are superseded.** They were produced by log-likelihood scoring on benchmarks subsequently found to overlap the fine-tuning corpus by up to 100%. Under overlap-audited evaluation the measured gain over the parent checkpoint is **+5.2 percentage points** on a held-out benchmark subset. The numbers below are the corrected ones, and the accompanying paper is largely *about* why the earlier figures were misleading.

---

## What this model is for

This checkpoint is released so that the results of the accompanying paper can be independently reproduced. It is a research artifact. It has **not** been clinically validated and must not be used for clinical decision-making.

The paper's contribution is methodological: for a model whose fine-tuning corpus is assembled in part from public medical QA datasets, standard benchmark evaluation cannot distinguish reasoning from exposure to test items, and this is measurable against the training corpus itself.

## Headline results

All figures from a single fixed evaluation harness: generative chain-of-thought, greedy decoding (temperature 0), identical prompt template and answer-extraction rule across every model and benchmark.

**MedXpertQA (Text) — the primary benchmark, not among the named training sources**

| | Parent checkpoint (Qwen3-8B) | This model | Gain |
|---|---|---|---|
| Full set (n = 2,450) | 17.5% [16.1–19.1] | 24.5% [22.8–26.2] | +7.0 |
| **Exact-stem-unflagged (n = 1,838)** | **15.6% [14.0–17.3]** | **20.8% [19.0–22.8]** | **+5.2** |

Unflagged comparison: paired McNemar test, 235 items gained against 139 lost, χ² = 24.13 (continuity-corrected), exact two-sided **P = 7.9 × 10⁻⁷**. Intervals are binomial 95% Wilson.

Excluding exact-stem-flagged items reduced the estimated gain from 7.0 to 5.2 percentage points — a reduction of 1.8 points, approximately 26% of the full-set estimate.

## Benchmark overlap against this model's training corpus

Measured with a three-layer pipeline (13-gram overlap, verbatim exact-stem match, longest-common-subsequence ratio ≥ 0.80) against the 97,041-item fine-tuning corpus.

| Benchmark | Exact-stem (primary) | 13-gram (lexical screen) |
|---|---|---|
| PubMedQA | **100%** | 100% |
| MedQA (USMLE) | **73.4%** | 99.9% |
| MMLU Professional Medicine | **70.6%** | 95.6% |
| MMLU Anatomy | 48.9% | 48.9% |
| MMLU Clinical Knowledge | 33.2% | 33.2% |
| MMLU Medical Genetics | 29.0% | 29.0% |
| MedXpertQA | **25.0%** | 50.0% |
| MedMCQA (validation split) | **0.02%** | 0.24% |

Overlap tracks the training-corpus composition, not benchmark difficulty. MedQA and PubMedQA items are present in the corpus at their evaluation-set sizes. MedMCQA is near-unflagged because training material was drawn from its *train* split while evaluation uses the held-out *validation* split — which also demonstrates that the detector is specific rather than flagging items indiscriminately.

MedXpertQA was **not among the named training sources**, yet 612 of its 2,450 items met the exact-stem criterion. The source pathway for these matches could not be resolved from the available corpus metadata; they were excluded from the primary subset without assigning a specific origin.

**On several overlapping benchmarks the unmodified parent checkpoint equals or outperforms this fine-tune** — significantly so on MedQA (74.0% versus 67.6% on the unflagged subset, P = 0.005). This pattern is consistent with benchmark-item exposure contributing to measured performance, though it does not establish the mechanism of any individual response; catastrophic forgetting, altered answer formatting and calibration shifts may also contribute. Scores on PubMedQA, MedQA and MMLU Professional Medicine should not be cited as evidence of this model's capability.

## Bundled ablation

A third arm was trained on the identical corpus with the reasoning traces removed and curriculum weighting replaced by uniform sampling. On the exact-stem-unflagged subset:

| Arm | Configuration | Accuracy [95% CI] | Contrast | P |
|---|---|---|---|---|
| A0 | Unmodified parent checkpoint | 15.6% [14.0–17.3] | — | — |
| A1 | Plain SFT, traces and weighting removed | 19.3% [17.5–21.1] | +3.6 vs A0 | 1.3 × 10⁻³ |
| A4 | Full recipe (this model) | 20.8% [19.0–22.8] | +1.6 vs A1 | 0.175 |

A1 retained approximately 70% of the observed A0-to-A4 improvement. This is a descriptive decomposition of the observed accuracies, not an estimate that 70% of the causal effect is uniquely attributable to medical-QA exposure.

**This is a bundled ablation, not a component-isolating experiment.** A1 and A4 differ jointly in five respects — reasoning-trace content, training-token exposure (A1 uses ≈21% of A4's tokens), curriculum weighting, cognitive-forcing structure and output-format supervision — and one training seed was used per arm. The comparison estimates a combined incremental contrast and does not identify the independent causal contribution of any single component.

## Training

| | |
|---|---|
| Parent checkpoint | `Qwen/Qwen3-8B` (instruction-tuned, not `Qwen3-8B-Base`) |
| Parent revision | `6d4c89fea8bfdc5c208d0964535c56e043e64d00` |
| Method | QLoRA, r = 128, α = 256 |
| Target modules | `q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj` |
| Trainable parameters | 349,175,808 (4.09% of the adapted model) |
| Learning rate | 2×10⁻⁴, cosine-with-restarts, warmup ratio 0.05 |
| Effective batch | 32 (per-device 2 × grad-accum 16) |
| Epochs | 3 main + 1 answer-format stabilisation |
| Max sequence length | 6,144 |
| Precision | bf16 compute, 4-bit base |
| Corpus | 97,041 examples |

Training used a structured eight-component clinical reasoning template — seven reasoning stages plus a post-reasoning answer stage — with likelihood ratios cited inline, and a quality-tier-weighted curriculum. The complete template schema, a worked example and the curriculum weighting scheme are in the paper's supplementary material.

## Evaluation protocol

Reproducing the reported numbers requires this exact configuration:

```
scoring        generative chain-of-thought
decoding       greedy, temperature 0.0, top_p 1.0
max_new_tokens 10240
max_model_len  12000
dtype          bfloat16
extraction     options-count-aware, six-stage staged fallback
```

The six extraction stages are: (1) explicit answer marker; (2) terminal standalone option letter; (3) bracketed option; (4) concluding-sentence cue; (5) leading option letter in the post-reasoning answer block; (6) explicit "option X" reference. Stages 5 and 6 were added after a differential extraction failure was identified — the original four-stage rule failed on 7.1% of the plain fine-tune's responses against 0.04% of this model's, because the two answer in different registers. The corrected rule is applied identically to all arms; the sensitivity analysis is reported in full in the paper.

Greedy decoding removes stochastic sampling but does **not** guarantee environment-independent outputs. In this work the same checkpoint returned 600 versus 584 correct of 2,450 under two inference-engine builds, and 600 versus 586 depending on whether the benchmark was run in isolation or as the last of seven sharing one engine — with all scoring settings held identical. Specify your software environment and request-stream protocol when reporting.

## Checkpoint integrity

Per-shard SHA-256 hashes of the released weights:

| File | SHA-256 |
|---|---|
| `model-00001-of-00004.safetensors` | `81a1fe53fa6a6e44cee399c24965f115e1b49de1f94e68f958aa09c78a77332e` |
| `model-00002-of-00004.safetensors` | `a3c1dba8c08f0847e732b5de421e46ad0a5cb8f929c5b6fdb53e6f301af7f7d5` |
| `model-00003-of-00004.safetensors` | `4175f8f817fe408b94cf5e5f053a9e0877fa4eaafd936890bdf41d9ffd105799` |
| `model-00004-of-00004.safetensors` | `23f5a0b324d1246a0c3005875b0ca6cb72f29247b045ef35476ddccd8c695700` |

These weights were verified byte-identical to the checkpoint evaluated in the paper across all four shards. Weights are stored in float16 and cast to bfloat16 at load.

The parent checkpoint is independently verifiable: its four per-shard SHA-256 values equal the Hugging Face LFS object identifiers for `Qwen/Qwen3-8B` at revision `6d4c89fea8bfdc5c208d0964535c56e043e64d00`, and are listed in the paper's supplementary material.

**Other repositories in this organisation were not evaluated and will not reproduce the reported figures**, including `Diagnostic-Reasoning-Q3` (4-bit quantized) and `Diagnostic-Reasoning-Q3X1S` (bfloat16 serialisation of the same model).

## Reproducibility

Three distinct things, stated separately because they are not equivalent:

- **Accuracy results and statistical comparisons can be reproduced** from these weights, the benchmark loaders, the per-item scoring outputs and the evaluation code, under the specified software environment and request-stream protocol.
- **The deposited overlap flags and exact-stem-unflagged item lists permit audit and reuse** of the reported subsets.
- **The overlap analysis itself cannot be independently regenerated** by third parties, because doing so requires the training corpus against which matching was performed, and that corpus is not redistributable. This is an acknowledged limitation of reproducibility rather than a resolved one.

Code, per-item outputs, the unflagged item list and a SHA-256 manifest: **https://doi.org/10.5281/zenodo.21827589**

## Safety

Evaluated on MedSafetyBench (900 items) using the benchmark's published 1–5 LLM-judge harmfulness rubric, with `claude-sonnet-5` as the judge model. Mean harmfulness 1.27/5 over the 880 responses that returned a valid judge score; 20 items are reported unscored rather than imputed. A keyword-based refusal cross-check returned a substantially different figure and is reported only as a reproducibility check.

**Refusal rate is not clinical safety**, and no claim of clinical safety is made. Hallucination, diagnostic prioritisation, medication safety, urgent-care escalation, over-refusal, calibration and uncertainty communication were **not** assessed.

## Limitations

- Not clinically validated. No prospective evaluation, clinician-in-the-loop testing, or assessment on real clinical cases.
- Evaluated exclusively on English-language multiple-choice benchmarks. No multilingual or cross-demographic evaluation; structured information extraction was not assessed.
- The training corpus derives predominantly from North American and United Kingdom clinical examination and reference material, and reflects those guidelines and epidemiological assumptions. The textbook-derived component was OCR-extracted without manual correction and carries extraction noise.
- Only one benchmark (MedXpertQA) is both outside the named training sources and adequately powered; conclusions rest on it.
- Exact-stem matching is a conservative floor and may undercount paraphrased or translated overlap; the 13-gram figure is a broader lexical-overlap screen rather than a strict upper bound. Items not flagged by the exact-stem criterion may still share paraphrased content, answer options or underlying source documents, and the subset should not be regarded as definitively uncontaminated.
- The MedQA test set is present in the corpus at its full evaluation-set size, yet exact-stem matching flags only 934 of its 1,273 items (73.4%) against 99.9% flagged by the 13-gram screen. Exact-stem detection therefore operates at roughly three-quarters sensitivity against a benchmark known to be present, and the unflagged subsets should be read as depleted of verbatim overlap rather than free of it.
- Overlap was measured against this model's fine-tuning corpus only, not against the parent checkpoint's pretraining data.
- One training seed per fine-tuned arm; the A1-to-A4 contrast cannot be separated from between-training-run variability.

## Data availability

The assembled training corpus is not released. It is a derived work built from third-party datasets and other source material and is not ours to redistribute. Component sources and split handling are documented in the paper's supplementary material; the complete training methodology — template, curriculum and weighting — is disclosed there in full.

## Use of generative artificial intelligence

Generative-AI tools, including Claude and ChatGPT, were used during this work to assist with code generation and review, analysis consistency checking, and language editing of the manuscript. This includes code deposited in the accompanying repository. Paperpal was used for language editing. All analyses were executed on the authors' data and computing infrastructure; all numerical results reported in the manuscript were checked by the authors against the underlying output files; and the authors reviewed and revised all AI-assisted text and code. The authors take full responsibility for the accuracy, integrity and conclusions of the work.

## Citation

```bibtex
@article{agha2026overlap,
  title  = {Training-corpus overlap and evaluation protocol constrain measured
            gains in a fine-tuned clinical language model},
  author = {Agha, Adnan and Anwar, Eram},
  year   = {2026},
  note   = {Manuscript under review}
}
```

Supporting code and data: https://doi.org/10.5281/zenodo.21827589

## Contact

Department of Internal Medicine, College of Medicine and Health Sciences, United Arab Emirates University · adnanagha@uaeu.ac.ae