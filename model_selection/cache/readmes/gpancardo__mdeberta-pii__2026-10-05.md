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
- mdeberta
- deberta-v3
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
- name: mdeberta-pii
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
      value: 0.9799
      name: Token F1 (validation, best checkpoint)
    - type: precision
      value: 0.9725
      name: Token Precision (validation)
    - type: recall
      value: 0.9875
      name: Token Recall (validation)
---

# mdeberta-pii

## Model Overview

`mdeberta-pii` is a fine-tuned version of [`microsoft/mdeberta-v3-base`](https://huggingface.co/microsoft/mdeberta-v3-base) for **token-level PII detection** in Spanish text. BIO tagging scheme, 24 canonical PII types (49 raw BIO labels).

**Architecture:** DeBERTa-v3-base — disentangled attention + ELECTRA-style pretraining, multilingual (100 languages) — 184M parameters.
**Training data:** Spanish subset of `ai4privacy/pii-masking-300k` (25,651 training samples).
**Tokenizer:** SentencePiece (`DebertaV2Tokenizer`).

This is the **second multilingual transfer-learning encoder** in a comparative study of CPU-only PII detection, alongside `gpancardo/xlmr-pii` (same transfer setup, different architecture) and `gpancardo/beto-pii` (native Spanish). Also evaluated: `iiiorg/piiranha-v1-detect-personal-information` (off-the-shelf, no fine-tuning for this task) and `urchade/gliner_multi_pii-v1` (zero-shot span encoder). The study excludes decoder-only generative LLMs as detectors by design: they introduce *copy bias*, non-deterministic JSON output and variable prefill latency, none of which a token classifier has. Target deployment is CPU-only retail/office hardware.

### Why mDeBERTa-v3, when XLM-RoBERTa already covers "multilingual transfer"?

Because the architecture, not just the pretraining language mix, is a variable worth isolating. mDeBERTa-v3's disentangled attention and ELECTRA-style replaced-token-detection pretraining are a different mechanism than XLM-RoBERTa's masked-language-model pretraining, even though both are multilingual Transformers fine-tuned here only on Spanish. Comparing both against `beto-pii` separates "does multilingual pretraining cost you Spanish-specific accuracy" (answered once by each model) from "does the specific multilingual architecture matter" (answered by comparing the two multilingual models against each other) — and, per the results below, mDeBERTa-v3 pays a larger validation and benchmark penalty than XLM-RoBERTa does, which is itself a finding, not noise.

---

## Intended Use

**Primary use case:** identifying PII spans in Spanish text for masking/anonymization pipelines — e.g. behind a tokenization proxy in front of a third-party LLM API.

**Not suitable for:** single tokens without context, adversarially obfuscated text, or as a standalone compliance/legal anonymization guarantee.

---

## Training Data

**Dataset:** [`ai4privacy/pii-masking-300k`](https://huggingface.co/datasets/ai4privacy/pii-masking-300k) — Spanish split, synthetic.

| Split | Samples |
|-------|--------:|
| Train | 25,651 |
| Validation | 5,485 |
| Test | 5,527 |

**Label canonicalization:** 28 raw PII types collapse to 24 canonical labels (`GIVENNAME1/2`, `LASTNAME1/2/3` unify under `PERSON`). 49 BIO labels total.

---

## Training Procedure

Fine-tuned with `scripts/finetune_encoder.py` (HF `Trainer`, token-classification/BIO). One run, no hyperparameter search.

| Parameter | Value |
|-----------|-------|
| Base model | `microsoft/mdeberta-v3-base` |
| Max sequence length | 256 tokens |
| Epochs | 3 |
| Batch size | 32 |
| Learning rate | 5e-5 |
| Precision | fp16 |
| Seed | 42 |

### Hardware (actual run, not estimated)

Cloud GPU (RunPod), single **NVIDIA L4**. Training runtime: **896.3 s** (~15 min) for 3 epochs — ~4-5× slower than BETO or XLM-R on an RTX 4090 for the same 3 epochs, partly architecture (disentangled attention is more expensive per token) and partly the weaker GPU (L4 vs. 4090). Peak GPU memory: 3.15 GB allocated / 17.26 GB reserved — the reservation is markedly higher than its allocation, typical of DeBERTa's attention implementation.

---

## Evaluation

### Validation metrics by epoch (token-level, 49 BIO labels)

| Epoch | Loss | Token F1 | Precision | Recall |
|------:|-----:|---------:|----------:|-------:|
| 1 | 0.0499 | 0.9771 | 0.9708 | 0.9834 |
| 2 | 0.0417 | 0.9790 | 0.9723 | 0.9857 |
| 3 (best) | 0.0388 | **0.9799** | 0.9725 | 0.9875 |

### Downstream benchmark (span-level, detection F1, IoU ≥ 0.5, type-agnostic)

On the project's own CPU benchmark (100-sample validation slice, local inference): `mdeberta-pii` **0.894** — below `beto-pii` and `xlmr-pii` (both 0.952), though well above the untuned `piiranha` baseline (0.688). This is consistent with mDeBERTa-v3's English-heavy pretraining mix and supports the parent study's RQ2 (native vs. transfer penalty) rather than contradicting it. Full test-set numbers with bootstrap confidence intervals are reported in the thesis (`codigo/results/`), not reproduced here.

### Per-type token F1 (validation)

| Type | F1 | Precision | Recall | Support |
|---|---:|---:|---:|---:|
| IP | 0.991 | 0.987 | 0.994 | 19849 |
| EMAIL | 0.989 | 0.985 | 0.994 | 14090 |
| TEL | 0.988 | 0.982 | 0.993 | 7311 |
| DRIVERLICENSE | 0.986 | 0.980 | 0.993 | 6158 |
| SOCIALNUMBER | 0.986 | 0.982 | 0.990 | 6579 |
| STREET | 0.982 | 0.978 | 0.987 | 7159 |
| USERNAME | 0.977 | 0.985 | 0.969 | 8794 |
| CITY | 0.976 | 0.968 | 0.984 | 4339 |
| SECADDRESS | 0.972 | 0.977 | 0.967 | 1117 |
| BOD | 0.971 | 0.972 | 0.970 | 5658 |
| PASSPORT | 0.971 | 0.964 | 0.978 | 5651 |
| STATE | 0.970 | 0.969 | 0.971 | 2257 |
| SEX | 0.969 | 0.957 | 0.981 | 2267 |
| POSTCODE | 0.968 | 0.969 | 0.967 | 1903 |
| GEOCOORD | 0.961 | 0.956 | 0.965 | 954 |
| IDCARD | 0.957 | 0.968 | 0.946 | 6879 |
| PERSON | 0.955 | 0.955 | 0.955 | 7504 |
| TIME | 0.955 | 0.953 | 0.957 | 3226 |
| TITLE | 0.949 | 0.955 | 0.943 | 1620 |
| PASS | 0.948 | 0.938 | 0.959 | 7861 |
| DATE | 0.948 | 0.947 | 0.950 | 4004 |
| BUILDING | 0.943 | 0.972 | 0.916 | 750 |
| COUNTRY | 0.939 | 0.945 | 0.933 | 511 |
| CARDISSUER | 0.000 | 0.000 | 0.000 | 4 |

`CARDISSUER` is not a bug: 4 validation spans (0.008% of the data) is too little support for precision/recall to mean anything.

---

## How to Use

```python
from transformers import pipeline

pipe = pipeline("token-classification", model="gpancardo/mdeberta-pii", aggregation_strategy="simple")
text = "Me llamo Juan Pérez y mi correo es juan.perez@correo.com"
for r in pipe(text):
    print(f"{r['entity_group']}: {r['word']} (score={r['score']:.3f})")
```

---

## Limitations & Biases

- **Synthetic training data.** Never saw real personal data.
- **Weakest of the three fine-tuned encoders on Spanish** (0.894 detection F1 vs. 0.952 for the other two on the local benchmark) — use `gpancardo/beto-pii` or `gpancardo/xlmr-pii` if raw Spanish accuracy matters more than architectural diversity.
- **256-token context window.**
- **Not adversarially robust.**
- **`CARDISSUER` is effectively untrained** (see Evaluation).
- **Slower to fine-tune and to run** than BETO/XLM-R-base at comparable batch sizes, consistent with DeBERTa's disentangled attention mechanism.
- **Not a compliance tool by itself.**

---

## License

MIT — base model also MIT. Training data under the `ai4privacy/pii-masking-300k` academic-use license (cite on reuse).

---

# mdeberta-pii (versión en español)

## Resumen del modelo

`mdeberta-pii` es una versión fine-tuned de [`microsoft/mdeberta-v3-base`](https://huggingface.co/microsoft/mdeberta-v3-base) para **detección de PII a nivel de token** en español. Esquema BIO, 24 tipos canónicos (49 etiquetas BIO).

**Arquitectura:** DeBERTa-v3-base — atención desenredada (*disentangled attention*) + preentrenamiento estilo ELECTRA, multilingüe (100 idiomas) — 184M parámetros.

Es el **segundo encoder multilingüe de transferencia** del estudio, junto a `gpancardo/xlmr-pii` (mismo esquema de transferencia, arquitectura distinta) y `gpancardo/beto-pii` (nativo español). También se evalúan `iiiorg/piiranha-v1-detect-personal-information` (listo para usar) y `urchade/gliner_multi_pii-v1` (zero-shot). El estudio excluye por diseño a los LLM generativos decoder-only como detectores.

### ¿Por qué mDeBERTa-v3, si XLM-RoBERTa ya cubre "transferencia multilingüe"?

Porque la arquitectura, no solo la mezcla de idiomas del preentrenamiento, es una variable que vale la pena aislar. Comparar ambos multilingües contra `beto-pii` separa "¿el preentrenamiento multilingüe cuesta precisión en español?" de "¿importa la arquitectura multilingüe específica?" — y, según los resultados de abajo, mDeBERTa-v3 paga una penalización mayor que XLM-RoBERTa, lo cual es un hallazgo, no ruido.

---

## Entrenamiento (ejecución real, no estimación)

GPU en nube (RunPod), **1× NVIDIA L4**. Tiempo de entrenamiento: **896.3 s** (~15 min) — 4-5× más lento que BETO o XLM-R en una RTX 4090 para las mismas 3 épocas, en parte por arquitectura (la atención desenredada es más cara por token) y en parte por la GPU más modesta (L4 vs. 4090). Memoria GPU pico: 3.15 GB asignados / 17.26 GB reservados.

---

## Evaluación

**Token F1 de validación (mejor checkpoint, época 3): 0.9799** (precisión 0.9725, recall 0.9875).

**Benchmark propio (span-level, detección, IoU≥0.5, 100 muestras val, CPU):** `mdeberta-pii` **0.894** — por debajo de `beto-pii` y `xlmr-pii` (ambos 0.952), aunque bastante por encima de `piiranha` sin ajustar (0.688). Esto es consistente con que el preentrenamiento de mDeBERTa-v3 está sesgado hacia el inglés, y respalda (no contradice) la RQ2 del estudio sobre la penalización nativo-vs-transferencia.

---

## Cómo usar

```python
from transformers import pipeline

pipe = pipeline("token-classification", model="gpancardo/mdeberta-pii", aggregation_strategy="simple")
texto = "Me llamo Juan Pérez y mi correo es juan.perez@correo.com"
for r in pipe(texto):
    print(f"{r['entity_group']}: {r['word']} (score={r['score']:.3f})")
```

---

## Limitaciones y sesgos

- Datos de entrenamiento sintéticos.
- Es el más débil de los tres encoders fine-tuneados en español (0.894 vs. 0.952) — usar `gpancardo/beto-pii` o `gpancardo/xlmr-pii` si la precisión en español importa más que la diversidad arquitectónica.
- Ventana de 256 tokens.
- No se evaluó robustez adversarial.
- `CARDISSUER` prácticamente sin entrenar.
- Más lento de entrenar y de correr que BETO/XLM-R-base a tamaños de batch comparables.
- No es, por sí solo, una herramienta de cumplimiento legal.

---

## Licencia

MIT — el modelo base también es MIT. Los datos de entrenamiento están bajo la licencia de uso académico de `ai4privacy/pii-masking-300k` (citar en caso de reutilización).
