---
license: other
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
base_model: perplexity-ai/pplx-pii-masking
---

# pplx-pii-masking — vLLM-servable conversion

`perplexity-ai/pplx-pii-masking` repacked as a standard HF
**`Qwen3ForTokenClassification`** folder so stock vLLM can serve it, plus the
serving kit (compose file, `/v1/scoring` adapter, decode client, parity checker).

**Status: private**, mirroring the source checkpoint, which is private pending
sync with the official release.

The weights are numerically the same model — no retraining, no quantization. What
changed is the packaging:

| source | here |
|---|---|
| `model_type: pii_masking`, `PPLXQwen3Model` + two separate heads | `Qwen3ForTokenClassification`, `"is_causal": false` |
| `backbone.*` | `model.*` |
| `token_cls_head` (37×1024) and `sensitivity_head` (1×1024) | one 38-row `score` head; column 37 is the folded sensitivity head |
| `viterbi.*` buffers in the state dict | `viterbi.json` (informational; clients build the same table from code) |

The sensitivity head is per-sequence in the original (a Linear over the
*mean-pooled* hidden state). Mean pooling commutes with an affine map
(`W·mean(h)+b == mean(W·h+b)`), so **the mean of logit column 37 over tokens is
the exact original sequence sensitivity logit** — provided the server returns raw
logits (`--pooler-config '{"use_activation": false}'`).

## Serve it

```bash
git clone https://huggingface.co/perplexity-ai/pplx-pii-masking-vllm
cd pplx-pii-masking-vllm/serving
docker compose up -d          # :8003 vLLM /pooling, :8002 /v1/scoring adapter

curl -s localhost:8002/v1/scoring -H 'Content-Type: application/json' \
  -d '{"model":"pii-masking-latest","sequences":["My name is John Smith."]}'
```

Or vLLM directly:

```bash
vllm serve <this repo> --served-model-name pii-masker \
  --runner pooling --convert classify \
  --pooler-config '{"use_activation": false}' \
  --dtype bfloat16 --max-model-len 4096
```

`POST /pooling` with `{"task": "token_classify", "input": [[token ids]]}` returns
`[T, 38]` raw logits: columns 0–36 are the BIOES token labels, column 37 is the
sensitivity column to be mean-averaged.

Full decode (constrained Viterbi → spans → masked text), a port of the pii-mask
Rust client:

```bash
python serving/test_client.py --model-dir . "Email Dr. Maria Gonzalez at maria@example.com"
# needs numpy, tokenizers, requests
```

## Labels

BIOES: index `0 = O`; then for category `c` in 0..8: `1+4c = B`, `2+4c = I`,
`3+4c = E`, `4+4c = S`. Categories **in this order** — it is load-bearing, and it
differs from the prose list in the source model card:

`private_person`, `private_email`, `private_phone`, `private_address`,
`private_url`, `private_date`, `account_number`, `secret`, `other_pii`

Index 37 is `__SEQ_SENSITIVITY__`, not a token label.

## Verification

Parity against the **original** checkpoint, computed by `serving/reference_forward.py`
— a hand-written fp32 Qwen3 encoder forward on CPU (no vLLM, no `transformers`
modeling code, no attention mask) plus both original heads, diffed against what
this deployment's `/v1/scoring` returns:

| text | tokens | argmax agreement | min cosine | max abs Δ logit | sensitivity Δ |
|---|---|---|---|---|---|
| "My name is John Smith and my SSN is 123-45-6789." | 23 | **23/23** | 0.99981 | 0.100 | 0.018 |
| mixed-PII paragraph (8 categories) | 97 | **97/97** | 0.99990 | 0.261 | 0.011 |

Residual is bf16-on-GPU vs fp32-on-CPU. This confirms both non-obvious serving
claims at once: bidirectional attention (a causal trunk diverges wildly) and the
mean-pool identity for the folded sensitivity column.

Category probe — all eight fire correctly, which is what validates the label order:

```
Contact Dr.[PRIVATE_PERSON] at[PRIVATE_EMAIL] or[PRIVATE_PHONE]. She lives at
[PRIVATE_ADDRESS]. Her appointment is on[PRIVATE_DATE], booking ref[ACCOUNT_NUMBER],
portal[PRIVATE_URL], password[SECRET]
```

with p = 0.977 / 0.967 / 0.988 / 0.992 / 0.990 / 0.963 / 0.920 / 0.429. Non-English
works (German person/email/address, p = 0.95–0.996).

Environment: NVIDIA DGX Spark (GB10, aarch64), vLLM 0.26.0, `--enforce-eager`.
1.8 GB GPU, ~45 s to healthy (4 s of that is weight loading).

## Caveats

- **Inputs over 4096 tokens are silently truncated, not rejected.**
  `tokenizer.json` carries `truncation: {max_length: 4096, direction: Right}`, so
  the adapter and vLLM both see truncated ids, the alignment check passes, and you
  get a `200` covering only the first 4096 tokens. Chunk client-side (the Rust
  client chunks at 4096 with 512 overlap).
- **`use_activation: false` is required**, not cosmetic. With activation on, the
  logits are squashed and both the Viterbi decode and the sensitivity mean break.
- The sensitivity head is weakly discriminative on this checkpoint (PII-dense text
  scores *low*, ~0.02–0.12). The serving math is exact; this is a property of the
  checkpoint (`loss_weight_sensitivity: 0.3`). Calibrate before gating on it.
- Spans are token-aligned, not character-aligned; a PII string fused into a
  preceding token can clip the span start by a few characters.
- Low-confidence spurious spans occur (e.g. `' SSN'` as `account_number` at
  p≈0.43). Filter on score if that matters.
- The `/v1/scoring` adapter accepts and ignores `Authorization`; neither port has
  auth. The compose file binds both to `127.0.0.1`.

## Files

| path | what |
|---|---|
| `config.json`, `model.safetensors`, `tokenizer*`, `viterbi.json` | the servable checkpoint |
| `serving/docker-compose.yml` | vLLM + scoring adapter |
| `serving/scoring_adapter.py` | `/v1/scoring` ⇄ `/pooling` shim |
| `serving/test_client.py` | Viterbi decode client (port of the Rust client) |
| `serving/convert_to_hf.py` | the converter that produced this repo, from the source checkpoint |
| `serving/reference_forward.py` | fp32 CPU reference forward, for parity checking |

Serving kit derived from
[`ppl-ai/mini-stack` `inference/dgx-spark/pii`](https://github.com/ppl-ai/mini-stack/tree/main/inference/dgx-spark/pii);
`reference_forward.py` is new here.
