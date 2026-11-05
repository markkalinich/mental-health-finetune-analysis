---
license: gemma
library_name: transformers
base_model: google/medgemma-4b-it
pipeline_tag: image-text-to-text
tags:
  - gemma
  - gemma-3
  - abliterated
  - uncensored
  - safetensors
---

# MedGemma 4B Instruct - Null-Space Abliterated

[google/medgemma-4b-it](https://huggingface.co/google/medgemma-4b-it) with refusal behavior removed via orthogonal projection. Uses null-space constraints and adaptive layer weighting to preserve model capabilities.

> **Note:** This model will produce uncensored outputs. Use responsibly.

**GGUF quantizations available at:** [jwest33/medgemma-4b-it-null-space-abliterated-GGUF](https://huggingface.co/jwest33/medgemma-4b-it-null-space-abliterated-GGUF)

### Abliteration Techniques Used

- **Winsorization**: Clips outlier activations at the 99th percentile for cleaner refusal direction estimation (recommended for Gemma models)
- **Null-Space Projection**: Preserves model capabilities by constraining weight updates to the null space of preservation activations
  - **Preservation Prompts**: Dynamically generated using [Gemma Scope 2](https://huggingface.co/google/gemma-scope-2) complete SAE circuit analysis to ensure complete coverage of shared features activated by harmful prompts, without overextending into unrelated capability space [gemma-3-4b-pt SAE models were used for circuit analysis of MedGemma3]
- **Adaptive Weighting**: Applies Gaussian-weighted per-layer ablation strength, focusing on middle-to-later layers where refusal behavior concentrates
- **Norm Preservation**: Maintains original Frobenius norms of weight matrices after projection

| Parameter | Value |
|-----------|-------|
| Harmful Prompts | 5000 |
| Harmless Prompts | 637 |
| Winsorization | 99.5th percentile |
| Null-Space Constraints | rank ratio: 0.95 |
| Directional Multiplier | 1.10 |
| SAE Targeted Coverage | 1.00 |

## Credits

- **Base Model**: [google/medgemma-4b-it](https://huggingface.co/google/medgemma-4b-it) by Google
- **SAE Analysis**: [GemmaScope](https://huggingface.co/google/gemma-scope-3-1b-it) sparse autoencoders by Google DeepMind
- [Norm-Preserving Biprojected Abliteration](https://huggingface.co/blog/grimjim/norm-preserving-biprojected-abliteration) — [Jim Lai (grimjim)](https://huggingface.co/grimjim) (2025)
- [AlphaEdit: Null-Space Constrained Knowledge Editing](https://arxiv.org/abs/2410.02355) — Fang et al. (ICLR 2025)
- [Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717) — Arditi et al. (2024)
- [Representation Engineering](https://arxiv.org/abs/2310.01405) — Zou et al. (2023)

## Toolkit Used

[github.com/jwest33/abliterator](https://github.com/jwest33/abliterator)

## License

This model inherits the [Gemma license](https://ai.google.dev/gemma/terms) from the base model. Please review and comply with Google's usage terms.

## Disclaimer

This model is provided for research and educational purposes. The creators are not responsible for any misuse. Users are solely responsible for ensuring their use complies with applicable laws and ethical standards.
