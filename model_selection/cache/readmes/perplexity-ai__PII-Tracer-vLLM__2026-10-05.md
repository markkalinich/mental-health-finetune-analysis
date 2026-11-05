---
license: mit
language:
- en
- multilingual
tags:
- pii
- token-classification
- privacy
- qwen3
- vllm
pipeline_tag: token-classification
base_model: perplexity-ai/PII-Tracer
---

# PII-Tracer-vLLM

This repository provides PII-Tracer, the detector introduced in
[PII-TRACE](https://arxiv.org/abs/2609.22200).

vLLM packaging of
[`perplexity-ai/PII-Tracer`](https://huggingface.co/perplexity-ai/PII-Tracer),
a PII masking model for conversational data. The model uses a ~600M-parameter
bidirectional Qwen3 encoder with a
[`perplexity-ai/pplx-embed-v1-0.6b`](https://huggingface.co/perplexity-ai/pplx-embed-v1-0.6b)
backbone and two heads:

- **Token classification head** (1024 → 37): BIOES tags over 9 PII categories
  (`private_person`, `account_number`, `private_url`, `private_date`,
  `private_address`, `private_email`, `private_phone`, `other_pii`, `secret`),
  decoded with a constrained Viterbi decoder.
- **Sensitivity head** (1024 → 1): conversation-level sensitivity classifier
  on mean-pooled hidden states.

This repository repackages the fine-tuned weights for vLLM without retraining
or quantization. It also includes a Docker Compose deployment, a `/v1/scoring`
adapter, a decoding client, and a reference forward implementation.

## Usage

The Docker Compose deployment requires an NVIDIA GPU, a compatible driver,
and Docker Compose with GPU support. It pins vLLM 0.26.0. Run these commands
from the same shell:

```bash
pip install huggingface_hub numpy tokenizers requests
hf download perplexity-ai/PII-Tracer-vLLM --local-dir PII-Tracer-vLLM
cd PII-Tracer-vLLM
docker compose -f serving/docker-compose.yml up -d

curl -s http://127.0.0.1:8002/health
curl -s http://127.0.0.1:8002/v1/scoring -H 'Content-Type: application/json' \
  -d '{"model":"pii-masking-latest","sequences":["My name is John Smith."]}'

python serving/test_client.py --model-dir . \
  "Hi, I'm Daniel Whitfield, you can reach me at daniels@meridiancap.com or 415-555-0123."
```

Wait for both services to become healthy before sending requests. The client
prints PII spans, masked text, and the sigmoid of the sensitivity logit.
The example client expects nonempty text.

To run vLLM directly instead of using Docker Compose:

```bash
vllm serve perplexity-ai/PII-Tracer-vLLM \
  --served-model-name pii-masker --host 127.0.0.1 --port 8003 \
  --runner pooling --convert classify \
  --pooler-config '{"use_activation": false}' \
  --dtype bfloat16 --max-model-len 4096
```

This direct command starts the `/pooling` endpoint. The `/v1/scoring` endpoint
and decoding client use the additional adapter provided by Docker Compose.
`POST /pooling` with `{"model": "pii-masker", "task": "token_classify", "input": [[token ids]]}`
returns a `[T, 38]` logit matrix for each input. Tokenize without adding BOS/EOS.

## Checkpoint layout

| Base checkpoint | vLLM packaging |
|---|---|
| Bidirectional Qwen3 encoder and two separate heads | `Qwen3ForTokenClassification` architecture with `is_causal: false` |
| `backbone.*` | `model.*` |
| `token_cls_head.*` (37 outputs) | Rows 0–36 of `score.weight` and `score.bias` |
| `sensitivity_head.*` (1 output) | Row 37 of `score.weight` and `score.bias` |
| `viterbi.*` | `viterbi.json`; the decoding client constructs the matching constraints |

The backbone weights retain bf16 precision and the head weights retain fp32
precision. The adapter separates the 37 token label logits from column 37,
then averages column 37 over the input tokens to obtain the sequence
sensitivity logit. This follows from
`mean(W·h + b) = W·mean(h) + b`; apply sigmoid to obtain sensitivity.
Floating-point results can vary with the serving dtype and backend.

## Labels and decoding

The 37 token labels use index `0 = O`. For category index `c` from 0 to 8,
`1+4c = B`, `2+4c = I`, `3+4c = E`, and `4+4c = S`.
The checkpoint's category index order is:

`private_person`, `private_email`, `private_phone`, `private_address`,
`private_url`, `private_date`, `account_number`, `secret`, `other_pii`.

Column 37 is `__SEQ_SENSITIVITY__` and is excluded from token decoding.
The client uses constrained BIOES Viterbi decoding and token offsets to
recover character spans. Its span confidence is the mean softmax probability
of the selected token labels; this differs from the base model's span score.

## Limitations

- The input limit is 4096 tokens. The supplied tokenizer truncates longer
  input, so chunk longer documents before scoring to cover the entire text.
- `use_activation: false` is required for raw logits, Viterbi decoding, and
  recovery of the sequence sensitivity logit.
- Span boundaries follow token offsets and can include surrounding whitespace.
  False positives and missed PII are possible; evaluate on your target data.
- Calibrate sensitivity and span confidence thresholds on your target data
  before using them to make masking decisions.
- Docker Compose binds both services to `127.0.0.1`; the adapter does not
  enforce authentication. Adjust `--gpu-memory-utilization` in the Compose
  file if the default allocation is insufficient for your GPU.

## Files

| Path | Purpose |
|---|---|
| `config.json`, `model.safetensors`, `tokenizer.json`, `tokenizer_config.json`, `viterbi.json` | Model, tokenizer, and decoding configuration |
| `serving/docker-compose.yml` | vLLM and scoring adapter deployment |
| `serving/scoring_adapter.py` | `/v1/scoring` adapter for `/pooling` |
| `serving/test_client.py` | Viterbi decoding and masking example |
| `serving/convert_to_hf.py` | Converter from the base checkpoint |
| `serving/reference_forward.py` | fp32 CPU reference for comparison with a running scoring adapter |

## License

MIT, matching the base model. See [LICENSE](LICENSE).

## Citation

If you use or reference this work, please cite:

```bibtex
@article{zhang2026piitrace,
  title = {{PII-TRACE}: A Benchmark for Context-Aware {PII} Detection in Multi-Turn {LLM} Conversations},
  author = {Zhang, Kaiyuan and Wang, Chuan and Zhong, Joey and Fryzel, Paul and Polley, Kyle and Ma, Jerry and Li, Ninghui},
  journal = {arXiv preprint arXiv:2609.22200},
  year = {2026},
  url = {https://arxiv.org/abs/2609.22200}
}
```
