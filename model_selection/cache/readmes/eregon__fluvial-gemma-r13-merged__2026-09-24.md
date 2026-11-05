---
language:
  - es
  - en
license: apache-2.0
base_model: google/gemma-2-2b-it
tags:
  - translation
  - terminology
  - therapy
  - fluvial-constellations
  - gemma2
  - qlora
  - fine-tuned
pipeline_tag: text-generation
model-index:
  - name: TranslateGemma R13
    results:
      - task:
          type: text-generation
          name: Terminology Translation
        metrics:
          - type: accuracy
            value: 100.0
            name: Glossary v3.0 Accuracy (106/106)
          - type: accuracy
            value: 100.0
            name: Transcript Test (58/58)
---

# TranslateGemma R13 — Fluvial Constellations Term Translator

A fine-tuned [Gemma 2 2B-it](https://huggingface.co/google/gemma-2-2b-it) model that translates **Fluvial Constellations** (Constelaciones Fluviales) therapy terminology from Spanish to English.

**100% accuracy** on all 106 glossary terms (Glossary v3.0) and 58/58 on real class transcript tests.

## What is Fluvial Constellations?

Fluvial Constellations (Constelaciones Fluviales) is a therapeutic method developed by Juan Carlos Arias Quintana, inspired by Bert Hellinger's Family Constellations. It is a systemic model performed in water using figurines in an inflatable pool, with its own specialized terminology that does not have standard English translations.

This model was trained to provide consistent, accurate English translations of the 106 official terms in the discipline's bilingual glossary.

## Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "eregon/fluvial-gemma-r13-merged"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id, torch_dtype=torch.bfloat16, device_map="auto"
)

def translate(term):
    prompt = (
        "<start_of_turn>user\n"
        f"Translate this Fluvial Constellations therapy term to English: {term}"
        "<end_of_turn>\n"
        "<start_of_turn>model\n"
    )
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=64, do_sample=False)
    response = tokenizer.decode(out[0], skip_special_tokens=False)
    response = response.split("<start_of_turn>model\n")[-1]
    return response.replace("<end_of_turn>", "").replace("<eos>", "").strip()

# Examples
print(translate("Constelaciones Fluviales"))  # → Fluvial Constellations
print(translate("Órdenes del Amor"))          # → Orders of Love
print(translate("Implicación"))               # → Entanglement
print(translate("Buen Lugar"))                # → Proper Place
print(translate("Tirada de Diagnóstico"))     # → Diagnosis Throw
```

### With 4-bit quantization (lower VRAM)

```python
from transformers import BitsAndBytesConfig

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True,
)
model = AutoModelForCausalLM.from_pretrained(
    model_id, quantization_config=bnb_config, device_map="auto"
)
```

## Complete Glossary (106 terms)

| # | Spanish | English | Category |
|---|---------|---------|----------|
| 1 | Constelaciones Fluviales | Fluvial Constellations | Core Methodology |
| 2 | Hidrosistémica | Hydrosystemics | Core Methodology |
| 3 | Campo | Field | Core Concepts |
| 4 | Alberca / Piscina | Pool | Equipment/Setup |
| 5 | Figurines | Figurines | Equipment/Setup |
| 6 | Consultante | Consultee | Roles |
| 7 | Constelador Fluvial | Fluvial Constellator | Roles |
| 8 | Representante | Representative | Roles |
| 9 | Bautizo | Baptism | Session Steps |
| 10 | Armonizar | Harmonize | Session Steps |
| 11 | Tirada | Throw | Core Concepts |
| 12 | Tirada de Diagnóstico | Diagnosis Throw | Throws |
| 13 | Tirada de Núcleos | Nucleus Throw | Throws |
| 14 | Tirada Transgeneracional | Transgenerational Throw | Throws |
| 15 | Tirada de Polaridades | Polarity Throw | Throws |
| 16 | Tirada Cruzada | Crossed Throw | Throws |
| 17 | Rueda de la Vida | Wheel of Life | Throws |
| 18 | Órdenes del Amor | Orders of Love | Fundamentals |
| 19 | Lealtad | Loyalty | Fundamentals |
| 20 | Dinámica | Dynamic | Fundamentals |
| 21 | Excluido | Excluded | Fundamentals |
| 22 | Pertenencia | Belonging | Fundamentals |
| 23 | Asentir | Assenting | Fundamentals |
| 24 | Tomar a los Padres | Taking the Parents | Fundamentals |
| 25 | La Pareja como Espejo | Partner as Mirror | Fundamentals |
| 26 | Primer Movimiento | First Movement | Movements |
| 27 | Segundo Movimiento | Second Movement | Movements |
| 28 | Reparación | Repair | Movements |
| 29 | COM (Contacto, Orden, Mirada) | COL (Contact, Order, Look) | Readings |
| 30 | Contacto | Contact | Readings |
| 31 | Orden | Order | Readings |
| 32 | Mirada | Look | Readings |
| 33 | Mirada de Fuerza | Look of Strength | Readings |
| 34 | Mirada al Amor | Look of Love | Readings |
| 35 | Mirada al Miedo | Look of Fear | Readings |
| 36 | Mirada Rebasada | Overwhelmed Look | Readings |
| 37 | Línea de Vida | Life Line | Readings |
| 38 | Yin-Yang | Yin-Yang | Readings |
| 39 | Rango y Mirada | Rank and Look | Readings |
| 40 | Lealtad de Muerte Inminente | Imminent Death Loyalty | Readings |
| 41 | Los 4 Fundamentos | The 4 Principles | Fundamentals |
| 42 | Los 12 Sistemas | The 12 Systems | Systems |
| 43 | Frases de Transición | Transition Phrases | Session Steps |
| 44 | Historial | Historical Record | Session Steps |
| 45 | LEO (Lugar, Emoción, Ordenar) | PEO (Place, Emotion, Order) | Session Steps |
| 46 | Ayudas | Aids | Session Steps |
| 47 | Tareas Sistémicas | Systemic Homework | Session Steps |
| 48 | Abrir el Campo | Open the Field | Session Steps |
| 49 | Cerrar el Campo | Close the Field | Session Steps |
| 50 | Constelación a Distancia | Remote Constellation | Core Methodology |
| 51 | Movimiento Hidrosistémico | Hydrosystemic Movement | Movements |
| 52 | Inducción Hipnótica | Hypnotic Induction | Techniques |
| 53 | Los 7 Niveles del Amor | The 7 Levels of Love | Techniques |
| 54 | Ego y Espíritu | Ego and Spirit | Techniques |
| 55 | Niveles de Pureza de Pensamiento | Levels of Thought Purity | Techniques |
| 56 | Nivel de Consciencia Esenia | Essene Level of Consciousness | Techniques |
| 57 | Cierre de Parejas | Partner Closure | Techniques |
| 58 | Meditación | Meditation | Resources |
| 59 | Escuela del Agua | Water School | Organization |
| 60 | Maestro Formador | Master Trainer | Roles |
| 61 | Imagen de Solución | Solution Image | Readings |
| 62 | Unión de Polaridades | Polarity Union | Readings |
| 63 | Frases Sanadoras | Healing Phrases | Resources |
| 64 | Órdenes de la Ayuda | Orders of Help | Fundamentals |
| 65 | Órdenes de la Abundancia | Orders of Abundance | Fundamentals |
| 66 | Perpetrador | Perpetrator | Core Concepts |
| 67 | Víctima | Victim | Core Concepts |
| 68 | Implicación | Entanglement | Core Concepts |
| 69 | Buen Lugar | Proper Place | Core Concepts |
| 70 | Ruta del Agua | Water Route | Organization |
| 71 | Campo Mórfico | Morphic Field | Scientific Basis |
| 72 | Unidades de Memoria | Units of Memory | Scientific Basis |
| 73 | H2O37 | H2O37 | Scientific Basis |
| 74 | Cristales Líquidos | Liquid Crystals | Scientific Basis |
| 75 | Amor Ciego | Blind Love | Core Concepts |
| 76 | Excluido Mayor | Greatest Excluded Member | Core Concepts |
| 77 | Movimiento de Amor Interrumpido | Interrupted Movement of Love | Core Concepts |
| 78 | Movimiento del Alma | Movement of the Soul | Movements |
| 79 | Movimiento del Espíritu | Movement of the Spirit | Movements |
| 80 | Doble Implicación | Double Entanglement | Core Concepts |
| 81 | Pensamientos Antena | Antenna Thoughts | Thought Types |
| 82 | Pensamientos Referentes | Referent Thoughts | Thought Types |
| 83 | Pensamientos Decisorios | Decisive Thoughts | Thought Types |
| 84 | Pensamientos de Gratitud | Gratitude Thoughts | Thought Types |
| 85 | Pensamientos que Asienten | Assenting Thoughts | Thought Types |
| 86 | Pensamientos Motivadores | Motivating Thoughts | Thought Types |
| 87 | Pensamientos Amorosos | Loving Thoughts | Thought Types |
| 88 | Pensamientos Creativos | Creative Thoughts | Thought Types |
| 89 | Pensamientos Útiles | Useful Thoughts | Thought Types |
| 90 | Pensamientos del Clan | Clan Thoughts | Thought Types |
| 91 | Pensamientos del Entorno | Environment Thoughts | Thought Types |
| 92 | Pensamientos del Ser | Thoughts of the Being | Thought Types |
| 93 | Hidrosistémica Empresarial | Corporate Hydrosystemics | Modalities |
| 94 | Diagnóstico Judicial | Judicial Diagnosis | Modalities |
| 95 | Derecho Sistémico | Systemic Law | Modalities |
| 96 | Constelaciones Caninas | Canine Constellations | Modalities |
| 97 | Neurohidrosistémica | Neuro-hydrosystemics | Modalities |
| 98 | Biomagnetismo Fluvial | Fluvial Biomagnetism | Modalities |
| 99 | Gemoterapia Fluvial | Fluvial Gemotherapy | Modalities |
| 100 | Fenomenología | Phenomenology | Core Concepts |
| 101 | Miradas Sincrónicas | Synchronous Looks | Readings |
| 102 | Respiración Maya | Maya Breathing | Techniques |
| 103 | Rueda Hidrosistémica | Hydrosystemic Wheel | Equipment/Setup |
| 104 | Registro Ancestral | Ancestral Record | Core Concepts |
| 105 | Memorias del Agua | Water Memories | Scientific Basis |
| 106 | cliente | client | Roles |

## Training Details

### Model Lineage

```
google/gemma-2-2b-it
  → R7-merged → R8 LoRA (91.67%)
    → R8-merged → R11 LoRA (95.37%)
      → R11-merged → R12 LoRA (100%, Glossary v2.1)
        → R12-merged → R13 LoRA (100%, Glossary v3.0) → R13-merged  ← this model
```

### R13 Training Configuration

| Parameter | Value |
|-----------|-------|
| Method | QLoRA (4-bit NF4, bf16 compute, double quantization) |
| LoRA rank | 32 |
| LoRA alpha | 64 |
| LoRA dropout | 0.05 |
| LoRA target | All projection modules |
| Epochs | 5 |
| Batch size | 1 (gradient accumulation: 8) |
| Learning rate | 3e-5 (cosine schedule, 10% warmup) |
| Optimizer | paged_adamw_8bit |
| Max sequence length | 192 |
| Max gradient norm | 0.3 |

### R13 Dataset

325 training examples across 4 difficulty tiers:

- **Tier 1** (15 reps, 3 terms): Hardest changes — acronym remappings (COM→COL, LEO→PEO) and new term (Mirada Rebasada)
- **Tier 2** (10 reps, 15 terms): Modified translations (e.g., "Look of Love", "Remote Constellation", "Corporate Hydrosystemics")
- **Tier 3** (8 reps, 6 terms): Simplified terms (removed `/` alternatives, e.g., "Pool" instead of "Pool / Swimming Pool")
- **Tier 4** (1 rep, 82 terms): Reinforcement for unchanged terms to prevent regression

### Training Results

| Metric | Value |
|--------|-------|
| Training steps | 205 |
| Training time | ~29 minutes |
| Final loss | 0.0933 |
| Average loss | 0.1223 |
| Peak GPU memory | 5.38 GB / 8 GB |

### Evaluation Results

| Test | Score |
|------|-------|
| Glossary v3.0 (106 terms) | **106/106 (100%)** |
| R13 target terms (24 changed) | 24/24 exact match |
| Previous round targets (11) | 11/11 held |
| Regressions | 0 |
| Real transcript test (4 transcripts, ~48K words) | **58/58 (100%)** |
| Unique terms verified in transcripts | 34/106 |

## Glossary Version History

- **v3.0** (R13, current): 106 terms. Simplified slash alternatives, English acronyms (COL, PEO), Hellinger-standard terminology (Entanglement, Proper Place)
- **v2.1** (R12): 108 terms. Added transcript-derived terms
- **v1.0** (R7-R11): Initial glossary builds

## Intended Use

This model is designed for:
- Real-time translation of Fluvial Constellations terminology during classes and sessions
- Subtitle generation for Spanish-language instructional videos
- Supporting bilingual documentation of the methodology

## Limitations

- Trained specifically for Fluvial Constellations terminology — not a general-purpose translator
- Best results with the exact prompt format shown above
- Some terms (e.g., "Campo", "Orden") are common Spanish words; the model translates them in the therapeutic context

## Hardware

- Trained on NVIDIA RTX 2080 (8 GB VRAM)
- Inference: ~1.6 GB (4-bit) or ~4.9 GB (bf16)
