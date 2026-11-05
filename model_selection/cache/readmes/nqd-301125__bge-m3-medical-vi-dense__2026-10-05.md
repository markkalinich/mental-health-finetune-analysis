---
language:
- vi
license: apache-2.0
base_model: BAAI/bge-m3
library_name: sentence-transformers
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- embeddings
- vietnamese
- medical
- bge-m3
- lora
---

# BGE-M3 Medical Vietnamese Dense Embedding

This model is a dense SentenceTransformers embedding model fine-tuned from `BAAI/bge-m3` on `nqd-301125/medical_data`.

## Important

This repository is intended to be loadable directly with:

```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("nqd-301125/bge-m3-medical-vi-dense")
```

The model was trained with PEFT LoRA. The best LoRA adapter was selected manually by dev cosine NDCG@10, then merged into the base weights before saving. The final uploaded artifact should not be adapter-only.

## Best adapter selection

The best adapter is selected manually because `Trainer.load_best_model_at_end` can fail with PEFT-wrapped SentenceTransformers checkpoints due to state_dict key prefix mismatch.

```json
{
  "metric_name": "eval_medical_dev_cosine_ndcg@10",
  "score": 0.9493321051495134,
  "step": 450,
  "epoch": 2.9605263157894735,
  "source": "trainer_eval",
  "state_path": "/content/bge_m3_medical_vi_dense_run/best_lora_adapter_state/best_adapter_state.pt"
}
```

## Training setup

- Base model: `BAAI/bge-m3`
- Dataset: `nqd-301125/medical_data`
- Loss: `MultipleNegativesRankingLoss(scale=20.0)`
- Max sequence length: `6000`
- Epochs: `3`
- Batch size: `64`
- Gradient accumulation: `1`
- Learning rate: `3e-05`
- Warmup ratio: `0.03`
- Weight decay: `0.01`
- LoRA r: `16`
- LoRA alpha: `32`
- LoRA dropout: `0.0`
- LoRA target modules: `['query', 'key', 'value', 'dense']`

## Scope

This is a dense retrieval fine-tune. It should not be described as explicitly fine-tuning the sparse or multi-vector components of BGE-M3.

## Internal evaluation

Evaluator: `InformationRetrievalEvaluator`
Main metric: cosine NDCG@10
Split: train/dev/test = 90/5/5 after cleaning and exact deduplication.

### Local merged metrics

Dev:

```json
{
  "medical_dev_cosine_accuracy@1": 0.9276437847866419,
  "medical_dev_cosine_accuracy@3": 0.9517625231910947,
  "medical_dev_cosine_accuracy@5": 0.961038961038961,
  "medical_dev_cosine_accuracy@10": 0.974025974025974,
  "medical_dev_cosine_precision@1": 0.9276437847866419,
  "medical_dev_cosine_precision@3": 0.31725417439703146,
  "medical_dev_cosine_precision@5": 0.1922077922077922,
  "medical_dev_cosine_precision@10": 0.09740259740259741,
  "medical_dev_cosine_recall@1": 0.9276437847866419,
  "medical_dev_cosine_recall@3": 0.9517625231910947,
  "medical_dev_cosine_recall@5": 0.961038961038961,
  "medical_dev_cosine_recall@10": 0.974025974025974,
  "medical_dev_cosine_ndcg@10": 0.949333673165304,
  "medical_dev_cosine_mrr@10": 0.9415967252701946,
  "medical_dev_cosine_map@100": 0.9424855540110175
}
```

Test:

```json
{
  "medical_test_cosine_accuracy@1": 0.9131238447319778,
  "medical_test_cosine_accuracy@3": 0.9537892791127541,
  "medical_test_cosine_accuracy@5": 0.9593345656192237,
  "medical_test_cosine_accuracy@10": 0.9685767097966729,
  "medical_test_cosine_precision@1": 0.9131238447319778,
  "medical_test_cosine_precision@3": 0.31792975970425136,
  "medical_test_cosine_precision@5": 0.1918669131238447,
  "medical_test_cosine_precision@10": 0.09685767097966728,
  "medical_test_cosine_recall@1": 0.9131238447319778,
  "medical_test_cosine_recall@3": 0.9537892791127541,
  "medical_test_cosine_recall@5": 0.9593345656192237,
  "medical_test_cosine_recall@10": 0.9685767097966729,
  "medical_test_cosine_ndcg@10": 0.9423110570787226,
  "medical_test_cosine_mrr@10": 0.933755831352874,
  "medical_test_cosine_map@100": 0.9350808229772267
}
```

### Base model metrics

Dev:

```json
{
  "medical_dev_cosine_accuracy@1": 0.8812615955473099,
  "medical_dev_cosine_accuracy@3": 0.935064935064935,
  "medical_dev_cosine_accuracy@5": 0.9461966604823747,
  "medical_dev_cosine_accuracy@10": 0.9591836734693877,
  "medical_dev_cosine_precision@1": 0.8812615955473099,
  "medical_dev_cosine_precision@3": 0.3116883116883116,
  "medical_dev_cosine_precision@5": 0.18923933209647495,
  "medical_dev_cosine_precision@10": 0.09591836734693879,
  "medical_dev_cosine_recall@1": 0.8812615955473099,
  "medical_dev_cosine_recall@3": 0.935064935064935,
  "medical_dev_cosine_recall@5": 0.9461966604823747,
  "medical_dev_cosine_recall@10": 0.9591836734693877,
  "medical_dev_cosine_ndcg@10": 0.9219673283268356,
  "medical_dev_cosine_mrr@10": 0.9098271343169301,
  "medical_dev_cosine_map@100": 0.911105170851867
}
```

Test:

```json
{
  "medical_test_cosine_accuracy@1": 0.8983364140480592,
  "medical_test_cosine_accuracy@3": 0.9390018484288355,
  "medical_test_cosine_accuracy@5": 0.9519408502772643,
  "medical_test_cosine_accuracy@10": 0.9593345656192237,
  "medical_test_cosine_precision@1": 0.8983364140480592,
  "medical_test_cosine_precision@3": 0.3130006161429451,
  "medical_test_cosine_precision@5": 0.19038817005545283,
  "medical_test_cosine_precision@10": 0.09593345656192237,
  "medical_test_cosine_recall@1": 0.8983364140480592,
  "medical_test_cosine_recall@3": 0.9390018484288355,
  "medical_test_cosine_recall@5": 0.9519408502772643,
  "medical_test_cosine_recall@10": 0.9593345656192237,
  "medical_test_cosine_ndcg@10": 0.9293159253064707,
  "medical_test_cosine_mrr@10": 0.9195852771176244,
  "medical_test_cosine_map@100": 0.920600642478801
}
```

## Limitations

- This model is not a medical diagnosis system.
- Retrieval results should be reviewed before any clinical or safety-critical use.
- Internal evaluation is not a substitute for external benchmarks.
- Dataset distribution may not represent all Vietnamese medical domains or real-world user queries.
