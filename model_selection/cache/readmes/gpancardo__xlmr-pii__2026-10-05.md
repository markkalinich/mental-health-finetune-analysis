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
- multilingual
- xlm-roberta
- bio
- ai4privacy
- transfer-learning
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
- name: xlmr-pii
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
      value: 0.9807
      name: Token F1 (validation, best checkpoint)
    - type: precision
      value: 0.9722
      name: Token Precision (validation)
    - type: recall
      value: 0.9892
      name: Token Recall (validation)
---

# xlmr-pii

## Model Overview

`xlmr-pii` is a fine-tuned version of [`FacebookAI/xlm-roberta-base`](https://huggingface.co/FacebookAI/xlm-roberta-base) for **token-level PII detection** in Spanish text. It uses a BIO tagging scheme over 24 canonical PII types.

**Architecture:** XLM-RoBERTa-base (12 layers, 768 hidden, 12 heads) — 278M parameters.
**Training data:** Spanish subset of `ai4privacy/pii-masking-300k` (25,651 training samples).
**Output format:** Token classification over a BIO label space (49 raw labels, O + B-{type} + I-{type}).
**Tokenizer:** SentencePiece, multilingual vocabulary.

This model is the **multilingual transfer-learning encoder** in a comparative study of CPU-only PII detection architectures for production LLM proxies. It is evaluated alongside `gpancardo/beto-pii` (native Spanish), `gpancardo/mdeberta-pii` (multilingual, different architecture), `iiiorg/piiranha-v1-detect-personal-information` (off-the-shelf, no fine-tuning), `urchade/gliner_multi_pii-v1` (zero-shot span encoder) and Microsoft Presidio (rules + spaCy NER). All candidates are discriminative encoders with deterministic output — the study deliberately excludes decoder-only generative LLMs to avoid their characteristic failure modes (copy bias, hallucinated offsets, non-deterministic JSON output) in a context where the deployment target is CPU-only retail/corporate hardware.

### Why XLM-RoBERTa?

XLM-RoBERTa is pretrained on 2.5 TB of CommonCrawl across 100 languages. Fine-tuning it only on Spanish tests whether its cross-lingual representations transfer to other languages without ever seeing PII-labeled data in them — the central research question of the parent study (the EN↔ES performance gap, contrasted against the native-Spanish `beto-pii`).

---

## Intended Use

**Primary use case:** identifying PII spans in Spanish (and, as a transfer-learning test, other languages) for masking/anonymization pipelines, e.g. serving behind a tokenization proxy in front of a third-party LLM API.

**Not suitable for:** non-contextual single-token input, adversarially obfuscated text, or as a drop-in replacement for a legal/compliance anonymization sign-off (see Limitations).

---

## Training Data

**Dataset:** [`ai4privacy/pii-masking-300k`](https://huggingface.co/datasets/ai4privacy/pii-masking-300k) — Spanish split, synthetic.

| Split | Samples |
|-------|--------:|
| Train | 25,651 |
| Validation | 5,485 |
| Test | 5,527 |

**Label canonicalization:** 28 raw PII types collapse to 24 canonical labels (the 5 name components — `GIVENNAME1/2`, `LASTNAME1/2/3` — unify under `PERSON`); all other types pass through unchanged. 49 BIO labels total.

---

## Training Procedure

Fine-tuned with `scripts/finetune_encoder.py` (HF `Trainer`, token-classification/BIO), one run, no hyperparameter search.

| Parameter | Value |
|-----------|-------|
| Base model | `FacebookAI/xlm-roberta-base` |
| Max sequence length | 256 tokens |
| Epochs | 3 |
| Batch size | 32 |
| Learning rate | 5e-5 |
| Precision | fp16 |
| Seed | 42 |

### Hardware (actual run, not estimated)

Cloud GPU (RunPod), single **NVIDIA RTX 4090**. Training runtime: **197.7 s** (~3.3 min) for 3 epochs over 25,651 samples. Peak GPU memory: 3.14 GB allocated / 7.23 GB reserved.

---

## Evaluation

### Validation metrics by epoch (token-level, over 49 BIO labels)

| Epoch | Loss | Token F1 | Precision | Recall |
|------:|-----:|---------:|----------:|-------:|
| 1 | 0.0537 | 0.9766 | 0.9670 | 0.9865 |
| 2 | 0.0487 | 0.9795 | 0.9700 | 0.9892 |
| 3 (best) | 0.0444 | **0.9807** | 0.9722 | 0.9892 |

### Downstream benchmark (span-level, detection F1, IoU ≥ 0.5, type-agnostic)

On the project's own CPU benchmark (100-sample validation slice, local inference): `xlmr-pii` **0.952**, matching `beto-pii` (0.952) and ahead of `mdeberta-pii` (0.894) and the untuned `piiranha` baseline (0.688). Full test-set numbers with bootstrap CIs are reported in the thesis (`codigo/results/`), not reproduced here — those are benchmark-pipeline outputs subject to revision, not model-card-level claims.

### Per-type token F1 (validation)

| Type | F1 | Precision | Recall | Support |
|---|---:|---:|---:|---:|
| IP | 0.990 | 0.988 | 0.993 | 24284 |
| EMAIL | 0.989 | 0.986 | 0.993 | 15758 |
| TEL | 0.989 | 0.988 | 0.990 | 10116 |
| SOCIALNUMBER | 0.982 | 0.979 | 0.985 | 9711 |
| STREET | 0.979 | 0.975 | 0.982 | 8230 |
| USERNAME | 0.977 | 0.984 | 0.970 | 10557 |
| DRIVERLICENSE | 0.977 | 0.965 | 0.989 | 8527 |
| POSTCODE | 0.976 | 0.972 | 0.981 | 3022 |
| PASSPORT | 0.976 | 0.971 | 0.981 | 8326 |
| SEX | 0.975 | 0.965 | 0.986 | 3627 |
| STATE | 0.975 | 0.969 | 0.981 | 2688 |
| SECADDRESS | 0.973 | 0.972 | 0.974 | 1867 |
| CITY | 0.973 | 0.964 | 0.982 | 5459 |
| BUILDING | 0.971 | 0.970 | 0.972 | 2134 |
| BOD | 0.969 | 0.972 | 0.967 | 7495 |
| GEOCOORD | 0.967 | 0.954 | 0.981 | 1207 |
| TIME | 0.967 | 0.965 | 0.969 | 5821 |
| IDCARD | 0.959 | 0.969 | 0.949 | 9550 |
| PERSON | 0.958 | 0.959 | 0.957 | 10274 |
| COUNTRY | 0.956 | 0.954 | 0.957 | 1268 |
| PASS | 0.949 | 0.941 | 0.958 | 8918 |
| TITLE | 0.948 | 0.956 | 0.939 | 2228 |
| DATE | 0.946 | 0.942 | 0.950 | 5532 |
| CARDISSUER | 0.000 | 0.000 | 0.000 | 4 |

`CARDISSUER` is not a bug: it has only 13 training spans and 4 validation spans (0.008% of the data) in the Spanish split, so precision/recall are undefined in practice at this support level.

---

## How to Use

```python
from transformers import pipeline

pipe = pipeline("token-classification", model="gpancardo/xlmr-pii", aggregation_strategy="simple")
text = "Me llamo Juan Pérez y mi correo es juan.perez@correo.com"
for r in pipe(text):
    print(f"{r['entity_group']}: {r['word']} (score={r['score']:.3f})")
```

---

## Limitations & Biases

- **Synthetic training data.** The model never saw real personal data; distributional shift on production text (informal register, OCR noise, mixed-language input) is untested.
- **Cross-lingual transfer is a research question, not a guarantee.** Fine-tuning used Spanish only; performance on other languages is exactly the gap this model is used to measure in the parent study, not an assumed strength.
- **256-token context window.** Longer documents need chunking.
- **Not adversarially robust.** No evaluation against obfuscation, leetspeak, or deliberate evasion.
- **`CARDISSUER` is effectively untrained** (see Evaluation).
- **Not a compliance tool by itself.** Detection F1 in the high 0.9s on token level does not translate directly into a legal anonymization guarantee; residual false negatives remain possible on any individual document.

---

## License

MIT — base model (`xlm-roberta-base`) also MIT. Training data under the `ai4privacy/pii-masking-300k` academic-use license (cite on reuse).

---

# xlmr-pii (versión en español)

## Resumen del modelo

`xlmr-pii` es una versión fine-tuned de [`FacebookAI/xlm-roberta-base`](https://huggingface.co/FacebookAI/xlm-roberta-base) para **detección de PII a nivel de token** en texto en español, con esquema BIO sobre 24 tipos canónicos.

**Arquitectura:** XLM-RoBERTa-base (12 capas, 768 ocultos, 12 cabezas) — 278M parámetros.
**Datos de entrenamiento:** subconjunto en español de `ai4privacy/pii-masking-300k` (25,651 muestras).
**Formato de salida:** clasificación de tokens BIO (49 etiquetas crudas).

Este modelo es el **encoder multilingüe de transferencia** dentro de un estudio comparativo de arquitecturas de detección de PII pensado para correr en CPU, sin GPU, en hardware de consumo/corporativo. Se evalúa junto a `gpancardo/beto-pii` (nativo español), `gpancardo/mdeberta-pii` (multilingüe, arquitectura distinta), `iiiorg/piiranha-v1-detect-personal-information` (listo para usar, sin fine-tuning), `urchade/gliner_multi_pii-v1` (encoder zero-shot) y Presidio (reglas + spaCy). Todos los candidatos son encoders discriminativos de salida determinista — el estudio excluye deliberadamente a los LLM generativos decoder-only por sus modos de falla característicos (*copy bias*, offsets alucinados, JSON no determinista), dado que el objetivo de despliegue es CPU-only.

### ¿Por qué XLM-RoBERTa?

Al fine-tunearlo solo en español se pone a prueba si sus representaciones cross-lingües (preentrenadas sobre 100 idiomas) transfieren a otros idiomas sin haber visto ahí ningún dato etiquetado de PII — la pregunta de investigación central del estudio (la brecha de rendimiento ES↔EN, contrastada contra el encoder nativo `beto-pii`).

---

## Datos de entrenamiento

Igual que la sección en inglés: 25,651 train / 5,485 val / 5,527 test, 28 tipos → 24 canónicos.

---

## Entrenamiento (ejecución real, no estimación)

GPU en nube (RunPod), **1× NVIDIA RTX 4090**. Tiempo de entrenamiento: **197.7 s** (~3.3 min) para 3 épocas. Memoria GPU pico: 3.14 GB asignados / 7.23 GB reservados.

| Parámetro | Valor |
|-----------|-------|
| Modelo base | `FacebookAI/xlm-roberta-base` |
| Longitud máxima | 256 tokens |
| Épocas | 3 |
| Batch size | 32 |
| Tasa de aprendizaje | 5e-5 |
| Precisión | fp16 |
| Semilla | 42 |

---

## Evaluación

**Token F1 de validación (mejor checkpoint, época 3): 0.9807** (precisión 0.9722, recall 0.9892).

**Benchmark propio (span-level, detección, IoU≥0.5, 100 muestras val, CPU):** `xlmr-pii` 0.952 — empata con `beto-pii` (0.952), por encima de `mdeberta-pii` (0.894) y de `piiranha` sin ajustar (0.688). Las cifras completas del test con intervalos bootstrap están en la tesina, no en este model card.

`CARDISSUER` sale en 0 porque tiene 13 spans en train y 4 en validación (0.008% de los datos) — subrepresentación, no bug.

---

## Cómo usar

```python
from transformers import pipeline

pipe = pipeline("token-classification", model="gpancardo/xlmr-pii", aggregation_strategy="simple")
texto = "Me llamo Juan Pérez y mi correo es juan.perez@correo.com"
for r in pipe(texto):
    print(f"{r['entity_group']}: {r['word']} (score={r['score']:.3f})")
```

---

## Limitaciones y sesgos

- Datos de entrenamiento sintéticos; no se probó contra texto real de producción.
- La transferencia cross-lingüe es la pregunta de investigación, no una garantía asumida.
- Ventana de 256 tokens.
- No se evaluó robustez adversarial.
- `CARDISSUER` prácticamente sin entrenar (ver Evaluación).
- No es, por sí solo, una herramienta de cumplimiento legal: un F1 alto a nivel de token no es una garantía de anonimización completa en un documento individual.

---

## Licencia

MIT — el modelo base (`xlm-roberta-base`) también es MIT. Los datos de entrenamiento están bajo la licencia de uso académico de `ai4privacy/pii-masking-300k` (citar en caso de reutilización).
