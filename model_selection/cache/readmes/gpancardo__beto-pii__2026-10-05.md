---
language:
- es
- en
license: mit
library_name: transformers
tags:
- token-classification
- ner
- pii
- personally-identifiable-information
- spanish
- beto
- bert
- bert-base-spanish-wwm-cased
- bio
- ai4privacy
datasets:
- ai4privacy/pii-masking-300k
pipeline_tag: token-classification
widget:
- text: "Me llamo Juan Pérez y mi correo es juan.perez@correo.com"
- text: "Mi teléfono es +34 612 345 678 y vivo en Calle Mayor 15, 28013 Madrid"
- text: "El DNI de María López es 12345678Z y su número de seguridad social es 28-1234567-89"
- text: "Puedes contactar a ana.garcia@empresa.es o al 91 123 45 67"
- text: "La tarjeta de crédito 4532 1234 5678 9010 caduca el 12/25"
model-index:
- name: beto-pii
  results:
  - task:
      type: token-classification
      name: Token Classification
    dataset:
      type: ai4privacy/pii-masking-300k
      name: ai4privacy/pii-masking-300k (Spanish, validation split)
      split: validation
    metrics:
    - type: f1
      value: 0.9810
      name: Token F1 (validation, best checkpoint)
    - type: precision
      value: 0.9730
      name: Token Precision (validation)
    - type: recall
      value: 0.9891
      name: Token Recall (validation)
---

# beto-pii

## Model Overview

`beto-pii` is a fine-tuned version of [`dccuchile/bert-base-spanish-wwm-cased`](https://huggingface.co/dccuchile/bert-base-spanish-wwm-cased) (BETO) for **token-level PII detection** in Spanish text. BIO tagging scheme, 24 canonical PII types (49 raw BIO labels).

**Architecture:** BERT-base (12 layers, 768 hidden, 12 heads) — 110M parameters.
**Training data:** Spanish subset of `ai4privacy/pii-masking-300k` (25,651 training samples).
**Tokenizer:** WordPiece (cased) — case matters for named entities in Spanish.

This is the **native Spanish encoder** in a comparative study of CPU-only PII detection for production LLM proxies. It is evaluated alongside `gpancardo/xlmr-pii` and `gpancardo/mdeberta-pii` (multilingual transfer-learning encoders, same training recipe), `iiiorg/piiranha-v1-detect-personal-information` (off-the-shelf, no fine-tuning for this task) and `urchade/gliner_multi_pii-v1` (zero-shot span encoder). The study deliberately excludes decoder-only generative LLMs as detectors: they introduce *copy bias* (copying PII instead of substituting it), non-deterministic JSON output, and variable prefill latency — none of which a token classifier has. The target deployment is CPU-only, retail/office-grade hardware, not a GPU inference cluster.

### Why BETO?

BETO is a BERT model trained exclusively on Spanish corpora. Its vocabulary and pretraining distribution are tuned for Spanish-specific patterns (compound surnames, Spanish document IDs like DNI/NIE, address formats) — the hypothesis this model tests is whether that native pretraining beats multilingual transfer on in-language Spanish PII, and by how much it degrades when the *same* checkpoint is run on English (never seen during fine-tuning or pretraining).

---

## Intended Use

**Primary use case:** identifying PII spans in Spanish text for masking/anonymization pipelines — e.g. behind a tokenization proxy in front of a third-party LLM API.

**Not suitable for:** non-Spanish text (use `gpancardo/xlmr-pii` or `gpancardo/mdeberta-pii`), single tokens without surrounding context, adversarially obfuscated text, or as a standalone compliance/legal anonymization guarantee.

---

## Training Data

**Dataset:** [`ai4privacy/pii-masking-300k`](https://huggingface.co/datasets/ai4privacy/pii-masking-300k) — Spanish split, synthetic (not real personal data).

| Split | Samples |
|-------|--------:|
| Train | 25,651 |
| Validation | 5,485 |
| Test | 5,527 |

**Label canonicalization:** 28 raw PII types collapse to 24 canonical labels (`GIVENNAME1/2`, `LASTNAME1/2/3` unify under `PERSON`); the rest pass through unchanged. 49 BIO labels total.

---

## Training Procedure

Fine-tuned with `scripts/finetune_encoder.py` (HF `Trainer`, token-classification/BIO). One run, no hyperparameter search.

| Parameter | Value |
|-----------|-------|
| Base model | `dccuchile/bert-base-spanish-wwm-cased` |
| Max sequence length | 256 tokens |
| Epochs | 3 |
| Batch size | 32 |
| Learning rate | 5e-5 |
| Precision | fp16 |
| Seed | 42 |

### Hardware (actual run, not estimated)

Cloud GPU (RunPod), single **NVIDIA RTX 4090**. Training runtime: **181.8 s** (~3 min) for 3 epochs over 25,651 samples. Peak GPU memory: 1.25 GB allocated / 4.85 GB reserved — the lightest of the three encoders in the study, consistent with BETO's 110M parameters.

---

## Evaluation

### Validation metrics by epoch (token-level, 49 BIO labels)

| Epoch | Loss | Token F1 | Precision | Recall |
|------:|-----:|---------:|----------:|-------:|
| 1 | 0.0596 | 0.9756 | 0.9671 | 0.9841 |
| 2 | 0.0494 | 0.9798 | 0.9726 | 0.9871 |
| 3 (best) | 0.0466 | **0.9810** | 0.9730 | 0.9891 |

### Downstream benchmark (span-level, detection F1, IoU ≥ 0.5, type-agnostic)

On the project's own CPU benchmark (100-sample validation slice, local inference): `beto-pii` **0.952**, matching `xlmr-pii` (0.952) and ahead of `mdeberta-pii` (0.894) and the untuned `piiranha` baseline (0.688). Full test-set numbers with bootstrap confidence intervals are reported in the thesis (`codigo/results/`) — those are benchmark-pipeline outputs subject to revision, not model-card-level claims.

### Per-type token F1 (validation)

| Type | F1 | Precision | Recall | Support |
|---|---:|---:|---:|---:|
| EMAIL | 0.990 | 0.988 | 0.993 | 19686 |
| IP | 0.989 | 0.986 | 0.993 | 27892 |
| TEL | 0.989 | 0.985 | 0.993 | 13372 |
| SOCIALNUMBER | 0.986 | 0.984 | 0.988 | 12901 |
| DRIVERLICENSE | 0.981 | 0.975 | 0.987 | 10925 |
| SEX | 0.979 | 0.974 | 0.983 | 2966 |
| STREET | 0.977 | 0.973 | 0.980 | 7156 |
| USERNAME | 0.976 | 0.986 | 0.967 | 13034 |
| BOD | 0.976 | 0.977 | 0.974 | 9549 |
| GEOCOORD | 0.975 | 0.969 | 0.982 | 1576 |
| STATE | 0.975 | 0.971 | 0.978 | 2348 |
| TIME | 0.973 | 0.965 | 0.981 | 8517 |
| BUILDING | 0.973 | 0.972 | 0.975 | 2400 |
| SECADDRESS | 0.973 | 0.979 | 0.967 | 2142 |
| PASSPORT | 0.973 | 0.964 | 0.981 | 10536 |
| POSTCODE | 0.973 | 0.973 | 0.973 | 3574 |
| CITY | 0.971 | 0.967 | 0.974 | 5297 |
| IDCARD | 0.960 | 0.964 | 0.955 | 12008 |
| PERSON | 0.954 | 0.954 | 0.954 | 11517 |
| COUNTRY | 0.953 | 0.943 | 0.964 | 1343 |
| DATE | 0.951 | 0.950 | 0.952 | 7084 |
| PASS | 0.947 | 0.937 | 0.956 | 9505 |
| TITLE | 0.938 | 0.955 | 0.922 | 1693 |
| CARDISSUER | 0.000 | 0.000 | 0.000 | 4 |

`CARDISSUER` is not a bug: 4 validation spans (0.008% of the data) is too little support for precision/recall to mean anything.

---

## How to Use

```python
from transformers import pipeline

pipe = pipeline("token-classification", model="gpancardo/beto-pii", aggregation_strategy="simple")
text = "Me llamo Juan Pérez y mi correo es juan.perez@correo.com"
for r in pipe(text):
    print(f"{r['entity_group']}: {r['word']} (score={r['score']:.3f})")
```

---

## Limitations & Biases

- **Synthetic training data.** Never saw real personal data; distributional shift on production text (informal register, OCR noise, mixed-language input) is untested.
- **Spanish-only by design.** This is the point of comparison, not a flaw to fix — use `gpancardo/xlmr-pii` or `gpancardo/mdeberta-pii` for multilingual input, and expect this checkpoint's accuracy to drop on non-Spanish text; that drop is exactly what the parent study measures.
- **256-token context window.** Longer documents need chunking.
- **Not adversarially robust.** No evaluation against obfuscation or deliberate evasion.
- **`CARDISSUER` is effectively untrained** (see Evaluation).
- **Not a compliance tool by itself.** High token-level F1 does not translate into a legal anonymization guarantee on any individual document; residual false negatives remain possible.

---

## License

MIT — base model also MIT. Training data under the `ai4privacy/pii-masking-300k` academic-use license (cite on reuse).

---

# beto-pii (versión en español)

## Resumen del modelo

`beto-pii` es una versión fine-tuned de [`dccuchile/bert-base-spanish-wwm-cased`](https://huggingface.co/dccuchile/bert-base-spanish-wwm-cased) (BETO) para **detección de PII a nivel de token** en español. Esquema BIO, 24 tipos canónicos (49 etiquetas BIO).

**Arquitectura:** BERT-base (12 capas, 768 ocultos, 12 cabezas) — 110M parámetros.
**Datos de entrenamiento:** subconjunto en español de `ai4privacy/pii-masking-300k` (25,651 muestras).

Es el **encoder nativo en español** de un estudio comparativo de detección de PII pensado para correr en CPU, sin GPU. Se evalúa junto a `gpancardo/xlmr-pii` y `gpancardo/mdeberta-pii` (encoders multilingües de transferencia, misma receta de entrenamiento), `iiiorg/piiranha-v1-detect-personal-information` (listo para usar, sin ajuste para esta tarea) y `urchade/gliner_multi_pii-v1` (encoder zero-shot). El estudio excluye deliberadamente a los LLM generativos decoder-only como detectores: introducen *copy bias* (copiar la PII en vez de sustituirla), salida JSON no determinista y latencia de prellenado variable — nada de eso le pasa a un clasificador de tokens. El objetivo de despliegue es hardware CPU de consumo u oficina, no un clúster de inferencia con GPU.

### ¿Por qué BETO?

BETO se entrenó exclusivamente con corpus en español. La hipótesis que este modelo pone a prueba es si ese preentrenamiento nativo le gana a la transferencia multilingüe en español, y cuánto se degrada ese mismo checkpoint al correr en inglés (idioma que nunca vio, ni en preentrenamiento ni en fine-tuning).

---

## Entrenamiento (ejecución real, no estimación)

GPU en nube (RunPod), **1× NVIDIA RTX 4090**. Tiempo de entrenamiento: **181.8 s** (~3 min). Memoria GPU pico: 1.25 GB asignados / 4.85 GB reservados — el más ligero de los tres encoders del estudio, coherente con sus 110M parámetros.

| Parámetro | Valor |
|-----------|-------|
| Modelo base | `dccuchile/bert-base-spanish-wwm-cased` |
| Longitud máxima | 256 tokens |
| Épocas | 3 |
| Batch size | 32 |
| Tasa de aprendizaje | 5e-5 |
| Precisión | fp16 |
| Semilla | 42 |

---

## Evaluación

**Token F1 de validación (mejor checkpoint, época 3): 0.9810** (precisión 0.9730, recall 0.9891).

**Benchmark propio (span-level, detección, IoU≥0.5, 100 muestras val, CPU):** `beto-pii` 0.952 — empata con `xlmr-pii` (0.952), por encima de `mdeberta-pii` (0.894) y de `piiranha` sin ajustar (0.688).

`CARDISSUER` sale en 0: 4 spans de validación (0.008% de los datos) es muy poco soporte para que precisión/recall signifiquen algo.

---

## Cómo usar

```python
from transformers import pipeline

pipe = pipeline("token-classification", model="gpancardo/beto-pii", aggregation_strategy="simple")
texto = "Me llamo Juan Pérez y mi correo es juan.perez@correo.com"
for r in pipe(texto):
    print(f"{r['entity_group']}: {r['word']} (score={r['score']:.3f})")
```

---

## Limitaciones y sesgos

- Datos de entrenamiento sintéticos; no se probó contra texto real de producción.
- Solo español, por diseño — ese es el punto de la comparación, no un defecto a corregir. Usar `gpancardo/xlmr-pii` o `gpancardo/mdeberta-pii` para entrada multilingüe; la caída de este checkpoint en otros idiomas es justo lo que mide el estudio.
- Ventana de 256 tokens.
- No se evaluó robustez adversarial.
- `CARDISSUER` prácticamente sin entrenar (ver Evaluación).
- No es, por sí solo, una herramienta de cumplimiento legal.

---

## Licencia

MIT — el modelo base también es MIT. Los datos de entrenamiento están bajo la licencia de uso académico de `ai4privacy/pii-masking-300k` (citar en caso de reutilización).
