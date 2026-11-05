---
library_name: gliner2
license: apache-2.0
base_model: fastino/gliner2-multi-v1
language:
- es
tags:
- gliner2
- text-classification
- sentiment-analysis
- social-media
- lora
---

# GLiNER2 Mixed-Source Spanish Sentiment, Seed 42

This is the **#1-ranked model** from a three-seed mixed-source sentiment pilot. It reached mean macro-F1 **0.671202** and mean accuracy **0.721218** across two evaluation sources. The model is a sentiment-only LoRA adaptation of [`fastino/gliner2-multi-v1`](https://huggingface.co/fastino/gliner2-multi-v1); the PEFT adapter has been merged into the base weights.

## Quick Start

```python
from gliner2 import GLiNER2

repo_id = "erickdp/gliner2-multi-sentiment-mixed-c42"
extractor = GLiNER2.from_pretrained(repo_id, map_location="cpu")

sentiment = {
    "positivo": "El comentario expresa emociones o actitudes favorables: admiración, cariño, apoyo, halagos, felicitaciones, entusiasmo, humor amistoso",
    "negativo": "El comentario expresa emociones o actitudes desfavorables: crítica, insulto, burla, queja, rechazo, decepción, enojo, sarcasmo hostil",
    "neutral": "El comentario no expresa carga emocional: preguntas sin emoción, información objetiva, menciones o etiquetas, anuncios, spam",
}
schema = extractor.create_schema().classification("sentimiento", sentiment)
result = extractor.extract("Me encanta este proyecto, excelente trabajo.", schema)
print(result)
```

The full GLiNER2 schema remains dynamically available, but **only sentiment classification was supervised in this pilot**. Validate other schema tasks independently before use.

## Model Details

| Item | Value |
|---|---|
| Base model | `fastino/gliner2-multi-v1` at `c6296e25603e4d31f68ef8a9f4edb73421d1e45a` |
| Framework | GLiNER2 1.3.2 |
| Pilot variant | C, 50/50 mixed source |
| Seed | 42 |
| Pilot rank | #1 by mean macro-F1 across both evaluation sources |
| Adaptation | Sentiment-only LoRA, merged into base |
| LoRA | r=16, alpha=32, dropout=0.05 |
| Sequence length | 384 |
| Effective batch size | 16 |
| Training limit | 5 epochs |
| Inference labels | `positivo`, `negativo`, `neutral` |

## Training Data

The C training dataset contains exactly 2,500 rows:

- 1,250 Claude-generated short social comments.
- 1,250 human-labeled rows sampled from the training split of [`erickdp/dataset_2026_04_22-v2`](https://huggingface.co/datasets/erickdp/dataset_2026_04_22-v2).
- Aggregate labels: 1,874 positive, 458 negative, and 168 neutral examples.
- Hugging Face source mapping: `0 = neutral`, `1 = positive`, `2 = negative`.

The policy is polarity-first and intentionally imbalanced. Hugging Face validation and test splits were not used for training. Exact and normalized text matches were excluded to reduce leakage into evaluation sources. No training or evaluation text is included in this repository.

## Evaluation

Two domains were evaluated: 500 Claude-labeled comments and 1,203 examples from the human-labeled Hugging Face test split. The reported means average the two source-level metrics, not their individual examples.

| Evaluation source | Accuracy | Macro-F1 | Balanced accuracy | Positive recall | Negative recall | Neutral recall |
|---|---:|---:|---:|---:|---:|---:|
| Claude-500 | 0.75000000 | 0.68561087 | 0.71679871 | 0.88461538 | 0.55813953 | 0.70764120 |
| HF human test (1,203) | 0.69243558 | 0.65679367 | 0.68553289 | 0.89035088 | 0.86033520 | 0.30591260 |

## Intended Use

Use this model to pilot sentiment classification for Spanish social-media comments under a content-valence definition: favorable or beneficial content is positive, adverse or harmful content is negative, and content without clear emotional valence is neutral. Treat outputs as model predictions requiring domain validation, not as human annotations.

## Limitations

- Half of the training rows are synthetic Claude examples.
- The deliberately polarized class distribution underrepresents neutral examples.
- Neutral recall is weak on the human Hugging Face test, especially relative to polar classes.
- The main focus is Spanish social-media comments, while the Hugging Face source includes varied content.
- Results span two domains with different labeling sources and should not be interpreted as a single-domain guarantee.
- The content-valence policy may differ from sentiment definitions based only on explicit author emotion.
- Synthetic labels and model predictions are not a human gold standard.
- Validate accuracy, calibration, fairness, and error costs on representative human-reviewed data before production use.

## License

Apache License 2.0, inherited from the base model metadata.
