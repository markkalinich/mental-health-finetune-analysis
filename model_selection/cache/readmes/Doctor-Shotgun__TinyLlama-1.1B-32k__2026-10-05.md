---
license: apache-2.0
datasets:
- togethercomputer/RedPajama-Data-1T-Sample
language:
- en
tags:
- llama
- llama 2
---
# TinyLlama-1.1B-32k

32k context finetune of TinyLlama-1.1B using increased rope theta (rope frequency base) meant to serve as a long-context speculative decoding model.

Created using [TinyLlama-1.1B](https://huggingface.co/TinyLlama/tinyLlama-intermediate-checkpoints-after-1T-token) and further pretraining at 32768 context length on [togethercomputer/RedPajama-Data-1T-Sample](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T-Sample).

Of note, the base checkpoint used was from commit "final model" fad4f1a5cd0563ac41349b8fec2e6e51156568a0 which was subsequently reverted, and not the current main branch 3T checkpoint of TinyLlama-1.1B.

[EXL2 Quants by turboderp](https://huggingface.co/turboderp/TinyLlama-1B-32k-exl2)

The quantized model fits alongside a 4.25bpw 70B model at 32k sequence length on a single A6000 and provides noticeable speed-up with speculative decoding.

### Wikitext (wikitext-2-raw-v1_train) Perplexity (64 rows) as evaluated via [exllamav2](https://github.com/turboderp/exllamav2):

| Model                  | 2048       | 4096       | 8192       | 16384      | 32768      |
| ---------------------- | ---------- | ---------- | ---------- | ---------- | ---------- |
| TinyLlama-1.1B         | **8.5633** | 208.3586   | 863.7507   | 1600.5021  | 6981.9021  |
| **TinyLlama-1.1B-32k** | 8.6548     | **7.8339** | **7.4904** | **7.3674** | **7.1338** |

### Evaluation on HumanEval by [turboderp](https://huggingface.co/turboderp):

| Model                                  | Pass@1          | Pass@10     |
| -------------------------------------- | --------------- | ----------- |
| TinyLlama-1.1B                         | **0.0841**      | **0.1524**  |
| TinyLlama-1.1B (NTK alpha=7.7)         | 0.0598          | 0.1098      |
| TinyLlama-1.1B-32k-ckpt-554            | 0.0732          | 0.1402      |
| **TinyLlama-1.1B-32k**                 | 0.0829          | **0.1524**  |
