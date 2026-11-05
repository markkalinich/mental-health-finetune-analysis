---
language:
- en
- zh
license: cc-by-nc-4.0
library_name: pytorch
pipeline_tag: text-classification
base_model: Qwen/Qwen3.5-0.8B-Base
tags:
- safety
- streaming
- moderation
- custom-code
- guardrail
- llm-safety
- content-moderation
- safety-classifier
- ai-safety
---
# HS-Guard v10

**Zhihao Liu · Naive N0.5**

[Inference code](https://github.com/KrisLiu16/HS-Guard) · [Technical report](https://github.com/KrisLiu16/HS-Guard/blob/main/docs/technical_report.pdf) · [Evaluation](https://github.com/KrisLiu16/HS-Guard/blob/main/docs/evaluation.json)

HS-Guard is a 754.5M-parameter hybrid-state safety classifier with separate prompt and response heads. It combines eighteen gated-delta layers with six 512-token window-attention layers. It scores risk directly and does not generate text.

![A safe answer passes; a story that turns into drug-making instructions is cut at token 41](figures/demo.gif)

Text replay in the [web demo](https://github.com/KrisLiu16/HS-Guard/blob/main/examples/demo/README.md) on one L20, with the default red-line rules. The answer is scored as it streams and cut once the score crosses the threshold. The demo interface is in Chinese.

## Usage

The model uses the released `hs-guard` package rather than `AutoModelForSequenceClassification` or a generic Transformers pipeline. The supported environment is Linux with an NVIDIA CUDA GPU; release testing uses an L20 with CUDA 12.8.

```bash
pip install torch==2.7.1 --index-url https://download.pytorch.org/whl/cu128
pip install git+https://github.com/KrisLiu16/HS-Guard.git
```

```python
from hs_guard import load_model, score_messages
model, tokenizer, metadata = load_model("KrisLiu16/HS-Guard-v10")
print(score_messages(model, tokenizer, metadata, [
    {"role": "user", "content": "How can I improve my study habits?"}
]))
```

For stable token streaming and continuous batching, use `StreamingGuard` from the same package. See the repository's [streaming example](https://github.com/KrisLiu16/HS-Guard/blob/main/examples/stream.py).

## Classification modes

- `redline` (default): a project-specific policy, including designated violence, weapons/drugs, explicit sexual content, self-harm methods and selected political/public-order content. The policy may flag quotations or restatements that another policy allows.
- `general`: broader harmfulness scoring, loaded with `load_model(head="general")`.

Class order is safe, unsafe, controversial. Cut score is `1 - p(safe)`. Red-line thresholds are 0.0761368871 for prompts and 0.1117895246 for responses; general thresholds are 0.5. Prompts use the final content score; responses use the maximum content score. Category tensors are retained, but category-label accuracy is not validated.

## Selected evaluation results

| Metric | HS-Guard v10 | Qwen3Guard-Stream-0.6B |
|---|---:|---:|
| Response red-line recall (114 examples) | 98.25% | 92.11% |
| Safe-response false-positive rate (203 examples) | 14.78% | 22.17% |
| ToxicChat held F1, general head | 74.16 | 70.51 |
| Aegis 2.0 response held F1, general head | 81.65 | 78.95 |

The baseline is measured on the same examples. Project-policy labels and original benchmark labels are separate. Full aggregate results, including unselected metrics, are linked above. The held suite has been observed during model development and does not establish universal superiority.

## Streaming performance

![HS-Guard streaming latency and concurrent moderation on NVIDIA L20](figures/streaming.png)

On one L20, the separately released streaming engine measures about 2.38 ms single-token median service latency. At 352 synthetic concurrent sessions it sustains at least 15,075 token/s with P95 at most 18.37 ms across 512, 2,048 and 8,000-token initial contexts. Tokenization, networking, prefill and cold start are excluded. See the [engine benchmark setup](https://github.com/KrisLiu16/HS-Guard/blob/main/docs/ENGINE.md#measured-performance) for the SGLang comparison baseline and measurement protocol.

## Provenance and limitations

The backbone originates from Qwen3.5-0.8B-Base. General-safety training uses Qwen3Guard-Stream-4B outputs. Training combines synthetic policy-supervised text with public training prompts, including ToxicChat, PolyGuardMix and PKU-derived prompts. The final update changes only the prompt head; shared and response tensors remain frozen. Raw data and private policy dictionaries are not distributed.

Automated labels are not independent human gold labels. Fresh-audit results are reported after model selection. Other policy-pass content can be over-blocked. No complete multilingual, category or production-service validation is claimed. The streaming API requires stable token IDs; arbitrary text rollback is the application's responsibility.

## Files and integrity

`model.safetensors` contains the complete classifier, including both branches. `hs_guard.json` records the architecture, thresholds, class order and asset SHA256 values. The loader verifies these checksums before loading tensors.

## License

The released weights are **CC BY-NC 4.0**, for noncommercial research; see `LICENSE`. Training provenance includes noncommercially licensed data such as ToxicChat. The original Qwen base model is Apache-2.0; its notice is preserved in `BASE_MODEL_LICENSE` and `NOTICE`. No source dataset is redistributed. The inference code is separately licensed under Apache-2.0 with MIT notices for FLA-derived portions.
