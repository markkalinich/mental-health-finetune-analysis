---
language:
- zh
license: apache-2.0
base_model: Qwen/Qwen2.5-7B-Instruct
datasets:
- thu-coai/SeTox
library_name: transformers
pipeline_tag: text-generation
tags:
- safety
- toxicity-detection
- tool-use
- search-augmented
- not-for-all-audiences
---

# SeTox-Qwen2.5-7B

SeTox-Qwen2.5-7B is a full-SFT model based on `Qwen/Qwen2.5-7B-Instruct` for
Chinese neologism toxicity detection with optional web-search tool use.

## Training

- Base model: `Qwen/Qwen2.5-7B-Instruct`
- Method: full supervised fine-tuning
- Training data: SeTox tool-use and direct SFT data
- Epochs: 4
- Learning rate: `1e-5`
- Scheduler: linear with warmup ratio `0.05`
- Context cutoff: `4096`

## Evaluation

Main SeTox neologism test set, 624 valid samples:

| Checkpoint | Accuracy | Unsafe F1 | Unsafe Recall | Safe F1 |
| --- | ---: | ---: | ---: | ---: |
| checkpoint-200 | 0.9407 | 0.9609 | 0.9286 | 0.8771 |
| checkpoint-175 | 0.9183 | 0.9451 | 0.8959 | 0.8401 |

Live search and generation settings can introduce small drift during
reproduction.

## Usage

See the SeTox code repository for search-augmented inference:

```bash
python scripts/run_inference.py \
  --model_path thu-coai/SeTox-Qwen2.5-7B \
  --search_backend serper \
  --input_path data/eval/neologism_test.json \
  --output_path outputs/neologism_predictions.json
```

For offline smoke tests, use `--mock` or `--search_backend none`.

## Limitations

This model is intended for research on Chinese neologism toxicity detection. It
can make mistakes on ambiguous, fast-changing, adversarial, or under-specified
terms. Search results may contain noisy or unsafe snippets, and downstream users
should apply appropriate safety review before deployment.

## License

This model is fine-tuned from `Qwen/Qwen2.5-7B-Instruct` and follows the
Apache-2.0 license inherited from the base model.

## Citation

Please cite the SeTox ACL paper:

- Paper: https://aclanthology.org/2026.acl-long.1602/
- DOI: https://doi.org/10.18653/v1/2026.acl-long.1602

```bibtex
@inproceedings{cui-etal-2026-setox,
  title = "{S}e{T}ox: Search-enhanced Reasoning for {LLM}-based Toxicity Detection over {C}hinese Internet Buzzwords",
  author = "Cui, Yiming and Zhang, Qinglin and Su, Xu and Min, Changyu and Hu, Shilin and Huang, Minlie",
  editor = "Che, Wanxiang and Nabende, Joyce and Shutova, Ekaterina and Pilehvar, Mohammad Taher",
  booktitle = "Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
  month = jul,
  year = "2026",
  address = "San Diego, California, USA",
  publisher = "Association for Computational Linguistics",
  url = "https://aclanthology.org/2026.acl-long.1602/",
  doi = "10.18653/v1/2026.acl-long.1602",
  pages = "33018--33034"
}
```
