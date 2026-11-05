---
language:
  - en
library_name: transformers
pipeline_tag: text-generation
tags:
  - alignment-research
  - refusal
  - safety-evaluation
  - qwen3
license: other
---

# RefusalLoc-Qwen3-1.7B-v2-DPO-s2

Source code and reproducibility materials: https://github.com/DONGRYEOLLEE1/refusal-loc

This is the balanced V2 DPO research checkpoint from RefusalLoc, initialized from Qwen3-1.7B-Instruct and trained with SFT followed by DPO.

> Research use only. This checkpoint is not presented as a production safety system: it retains substantial benign false-refusal and capability loss.

## Intended use

- Research on refusal alignment, safety–helpfulness trade-offs, and mechanistic interpretability.
- Reproduction of the associated behavioral evaluation and direction-ablation study.

## Not intended for

- High-stakes, safety-critical, or production deployment.
- A replacement for application-specific safety policy and human oversight.

## Evaluation

| Metric | Score |
|---|---:|
| Harmful refusal ↑ | 89.0 |
| Harmful compliance ↓ | 3.5 |
| Benign false refusal ↓ | 49.3 |
| Benign helpful completion ↑ | 55.6 |
| IFEval ↑ | 48.4 |
| GSM8K ↑ | 56.8 |
| MMLU ↑ | 50.0 |

Harmful compliance was scored with `cais/HarmBench-Llama-2-13b-cls` at revision `bda705349d1144fa618770bea64d99ce54e3835b`.

## Evaluation protocol

- Inference: non-thinking, greedy decoding, 512 maximum new tokens.
- Safety prompts: AdvBench 520, HarmBench 400, StrongREJECT 313, JBB 100.
- Benign prompts: XSTest 450 and fixed OR-Bench subset 400.
- Capability: IFEval 541, fixed GSM8K subset 250, fixed MMLU subset 114.
- Harmful compliance: HarmBench 13B classifier at the revision above.

This checkpoint is one member of a three-seed family. Seed 2 was selected as the balanced research-release candidate because it has the lowest V2 false-refusal rate, near-best helpful completion, and competitive capability among the DPO endpoints.

## Training summary

- SFT: 40,000 examples — 24,000 general, 8,000 harmful-refusal, 8,000 benign-helpfulness.
- DPO: 3,997 valid pairs — harmful safety preference, benign compliance, and general helpfulness.
- LoRA: rank 32, alpha 64; SFT 2,500 steps; DPO 500 steps; seed 2.
- Base and reference: the seed-matched merged SFT endpoint.

## License and data notice

This release is for research use only. The training recipe uses a CC-BY-NC-4.0 source recorded in the accompanying provenance manifest. Review all base-model and source-data obligations before enabling commercial use.

## Upload checklist

1. Choose the final repository license after reviewing source-data obligations.
2. Preserve all files in this directory, including `.gitattributes`.
3. Add the exact commit hash of the release code before publishing.
4. Do not upload raw training data, benchmark prompts, or stored generations.
