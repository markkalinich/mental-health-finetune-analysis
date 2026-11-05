---
license: mit
language:
- az
- en
library_name: transformers
pipeline_tag: token-classification
tags:
- ner
- pii
- azerbaijani
- modernbert
- privacy
- data-protection
- token-classification
base_model: LocalDoc/mmBERT-small-en-az
datasets:
- LocalDoc/pii_ner_azerbaijani_extended
metrics:
- f1
- precision
- recall
model-index:
- name: pii-ner-azerbaijani-v3
  results:
  - task:
      type: token-classification
      name: Named Entity Recognition
    dataset:
      name: PII NER Azerbaijani Extended
      type: LocalDoc/pii_ner_azerbaijani_extended
    metrics:
    - name: F1
      type: f1
      value: 0.9974
    - name: Precision
      type: precision
      value: 0.9967
    - name: Recall
      type: recall
      value: 0.9982
---

# PII NER Azerbaijani v3

A high-accuracy Named Entity Recognition model for detecting **Personally Identifiable Information (PII)** in Azerbaijani text. Built on [LocalDoc/mmBERT-small-en-az](https://huggingface.co/LocalDoc/mmBERT-small-en-az) (ModernBERT architecture), this model is **4x smaller and faster** than XLM-RoBERTa while achieving **higher accuracy**.

## Key Features

- **F1 = 0.9974** — all 15 entity types above 0.99
- **69M parameters** — 4x smaller than XLM-RoBERTa (278M)
- **3-4x faster inference** — ModernBERT architecture with Flash Attention 2
- **Transliteration-robust** — works with both `Şərifova` and `Sherifova`
- **Hard negative trained** — distinguishes "bakı küləyi" (weather) from "bakıda yaşayır" (address)
- **Lowercase input** — model is trained on lowercased text for case-insensitive detection

## Model Details

| Metric | Value |
|---|---|
| Base Model | [LocalDoc/mmBERT-small-en-az](https://huggingface.co/LocalDoc/mmBERT-small-en-az) |
| Architecture | ModernBERT (22 layers, hidden=384) |
| Parameters | 69M |
| Model Size (fp32) | 0.26 GB |
| Max Sequence Length | 8,192 tokens |
| Training Data | [LocalDoc/pii_ner_azerbaijani_extended](https://huggingface.co/datasets/LocalDoc/pii_ner_azerbaijani_extended) (530K rows) |
| Training Epochs | 5 (best at epoch 5) |
| License | MIT |

## Performance

### Overall Metrics

| Metric | This Model (69M) | XLM-RoBERTa v2 (278M) |
|---|---|---|
| **F1** | **0.9974** | 0.9746 |
| **Precision** | **0.9967** | 0.9760 |
| **Recall** | **0.9982** | 0.9732 |
| **False Positives (hard neg)** | **1** | 4 |

### Per-Entity F1 Scores

| Entity | F1 | Entity | F1 |
|---|---|---|---|
| GIVENNAME | 0.9974 | PASSPORTNUM | 0.9996 |
| SURNAME | 0.9980 | TAXNUM | 0.9994 |
| EMAIL | 0.9978 | TELEPHONENUM | 0.9993 |
| DATE | 0.9936 | TIME | 0.9993 |
| AGE | 0.9965 | CREDITCARDNUMBER | 0.9948 |
| CITY | 0.9967 | STREET | 0.9926 |
| IDCARDNUM | 0.9985 | BUILDINGNUM | 0.9976 |
| ZIPCODE | 0.9978 | | |

### Training Progress

| Epoch | Loss | F1 | Precision | Recall |
|---|---|---|---|---|
| 1 | 0.0159 | 0.9839 | 0.9794 | 0.9889 |
| 2 | 0.0099 | 0.9877 | 0.9848 | 0.9908 |
| 3 | 0.0053 | 0.9949 | 0.9931 | 0.9967 |
| 4 | 0.0038 | 0.9972 | 0.9964 | 0.9980 |
| **5** | **0.0041** | **0.9974** | **0.9967** | **0.9982** |

## Recognized Entities

```
GIVENNAME          — First name (e.g., "Əli", "Aysel")
SURNAME            — Last name (e.g., "Həsənov", "Məmmədova")
EMAIL              — Email address
TELEPHONENUM       — Phone number
DATE               — Date in various formats
TIME               — Time
AGE                — Age
IDCARDNUM          — ID card / FIN number
PASSPORTNUM        — Passport number
TAXNUM             — Tax identification number
CREDITCARDNUMBER   — Credit card number
CITY               — City name (as address, not adjective)
STREET             — Street name
BUILDINGNUM        — Building number
ZIPCODE            — ZIP/postal code
```

## Usage

### Quick Start

```python
import torch
from transformers import AutoModelForTokenClassification, AutoTokenizer


class AzerbaijaniPiiNer:
    def __init__(self, model_name="LocalDoc/pii-ner-azerbaijani-v3"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForTokenClassification.from_pretrained(model_name)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device).eval()

        self.id2label = self.model.config.id2label

    def predict(self, text: str) -> list[dict]:
        """
        Detect PII entities in text.
        Input is lowercased for the model, but original casing is preserved in output.
        """
        original_text = text
        text_lower = text.lower()

        inputs = self.tokenizer(
            text_lower,
            return_tensors="pt",
            return_offsets_mapping=True,
            return_special_tokens_mask=True,
            truncation=True,
            max_length=512,
        )

        offsets = inputs.pop("offset_mapping")[0]
        special_mask = inputs.pop("special_tokens_mask")[0]
        inputs = {k: v.to(self.device) for k, v in inputs.items()}

        with torch.no_grad():
            logits = self.model(**inputs).logits

        predictions = torch.argmax(logits, dim=-1)[0].cpu()

        # Extract entities
        entities = []
        current = None

        for pred_id, offset, is_special in zip(predictions, offsets, special_mask):
            if is_special:
                if current:
                    entities.append(current)
                    current = None
                continue

            label = self.id2label[pred_id.item()]
            cs, ce = offset[0].item(), offset[1].item()

            if label.startswith("B-"):
                if current:
                    entities.append(current)
                current = {"label": label[2:], "start": cs, "end": ce}
            elif label.startswith("I-") and current and label[2:] == current["label"]:
                current["end"] = ce
            else:
                if current:
                    entities.append(current)
                    current = None

        if current:
            entities.append(current)

        # Map back to ORIGINAL text (preserve original casing)
        for ent in entities:
            raw = original_text[ent["start"]:ent["end"]]
            ent["value"] = raw.strip()
            if raw != raw.strip():
                offset = len(raw) - len(raw.lstrip())
                ent["start"] += offset
                ent["end"] = ent["start"] + len(ent["value"])

        return entities

    def anonymize(self, text: str, replacement: str = "***") -> str:
        """Replace all PII entities with a placeholder."""
        entities = self.predict(text)
        entities.sort(key=lambda x: x["start"], reverse=True)

        result = text
        for ent in entities:
            result = result[:ent["start"]] + replacement + result[ent["end"]:]

        return result

    def highlight(self, text: str) -> str:
        """Return text with entities marked: [LABEL: value]."""
        entities = self.predict(text)
        entities.sort(key=lambda x: x["start"], reverse=True)

        result = text
        for ent in entities:
            result = (
                result[:ent["start"]]
                + f"[{ent['label']}: {ent['value']}]"
                + result[ent["end"]:]
            )

        return result


# --- Example ---
if __name__ == "__main__":
    ner = AzerbaijaniPiiNer()

    examples = [
        # Original Azerbaijani
        "Hörmətli Əhməd Süleymanlı, 05.03.1987 tarixli müraciətiniz qəbul edildi. Əlaqə: 055-234-67-89.",

        # Transliterated (informal)
        "Hormetli Ehmed Suleymanlı, 05.03.1987 tarixli muracietiniz qebul edildi. Elaqe: 055-234-67-89.",

        # Mixed context with hard negatives
        "Bakı küləyi güclüdür, amma Əli Bakıda Nizami küçəsi 42-də yaşayır.",

        # Complex document
        "Müştəri: Gülarə Məmmədli, 67 yaş. Pasport: AZE 1234567. Email: gulare@mail.az. Tel: 012-456-78-90.",

        # English-Azerbaijani mix
        "Dear customer Əli Həsənli, your order shipped to Bakı, 28 May küçəsi 12. Contact: ali@company.com.",
    ]

    for text in examples:
        print(f"\nInput:     {text}")
        print(f"Highlight: {ner.highlight(text)}")
        print(f"Anonymize: {ner.anonymize(text)}")
        for ent in ner.predict(text):
            print(f"  {ent['label']:20s} → \"{ent['value']}\" ({ent['start']}:{ent['end']})")
```

### Expected Output

```
Input:     Hörmətli Əhməd Süleymanlı, 05.03.1987 tarixli müraciətiniz qəbul edildi. Əlaqə: 055-234-67-89.
Highlight: Hörmətli [GIVENNAME: Əhməd] [SURNAME: Süleymanlı], [DATE: 05.03.1987] tarixli müraciətiniz qəbul edildi. Əlaqə: [TELEPHONENUM: 055-234-67-89].
Anonymize: Hörmətli *** ***, *** tarixli müraciətiniz qəbul edildi. Əlaqə: ***.
  GIVENNAME            → "Əhməd" (9:14)
  SURNAME              → "Süleymanlı" (15:25)
  DATE                 → "05.03.1987" (27:37)
  TELEPHONENUM         → "055-234-67-89" (82:95)
```

### Pipeline Usage

```python
from transformers import pipeline

ner_pipeline = pipeline(
    "token-classification",
    model="LocalDoc/pii-ner-azerbaijani-v3",
    aggregation_strategy="simple",
)

# Important: lowercase the input
text = "Əhməd Həsənov Bakıda yaşayır, telefonu 055-123-45-67."
results = ner_pipeline(text.lower())

for entity in results:
    print(f"{entity['entity_group']:20s} → \"{entity['word']}\" (score: {entity['score']:.4f})")
```

## Training Details

### Dataset

Trained on [LocalDoc/pii_ner_azerbaijani_extended](https://huggingface.co/datasets/LocalDoc/pii_ner_azerbaijani_extended) (530K rows):

- **Template-based data** (~481K) — original + 3 transliteration strategies
- **LLM-generated PII** (~25K) — natural sentences in diverse contexts
- **LLM-generated hard negatives** (~15K) — trap words that look like PII
- **LLM-generated mixed** (~10K) — real PII + traps in the same sentence

### Why Hard Negatives Matter

Without hard negatives, the model marks every city name as PII:
- ❌ "bakı küləyi güclüdür" → CITY: bakı (wrong — it's about weather)
- ❌ "nərgiz çiçəkləri açılır" → GIVENNAME: nərgiz (wrong — it's a flower)

With hard negatives, the model learns context:
- ✅ "bakı küləyi güclüdür" → no PII (weather context)
- ✅ "əhməd bakıda yaşayır" → GIVENNAME: əhməd, CITY: bakı (address context)

### Configuration

- **Optimizer:** AdamW
- **Learning Rate:** 3e-5 with cosine schedule
- **Warmup:** 10%
- **Batch Size:** 64
- **Weight Decay:** 0.01
- **Max Length:** 512
- **Early Stopping:** patience=3 on F1
- **Preprocessing:** all text lowercased before tokenization

## Limitations

- **Lowercase input required** — always call `.lower()` before inference
- **Synthetic training data** — may not cover all real-world PII patterns
- **Phone numbers with dashes** — in chat-style text, numbers like `055-987-65-43` may split. This is a known tokenizer limitation.
- **Azerbaijani and English only** — other languages will produce poor results
- **District names** — names like "Nəsimi" may be misidentified as personal names

## Comparison with Previous Versions

| | v3 (this) | v2 (XLM-RoBERTa) | v1 (XLM-RoBERTa) |
|---|---|---|---|
| Base | mmBERT-small | XLM-RoBERTa | XLM-RoBERTa |
| Parameters | **69M** | 278M | 278M |
| F1 | **0.9974** | 0.9746 | 0.9629 |
| Hard neg FP | **1** | 4 | not tested |
| Transliteration | **yes** | no | no |
| Speed | **3-4x faster** | 1x | 1x |

## Citation

```bibtex
@misc{pii-ner-azerbaijani-v3,
  title={PII NER Azerbaijani v3},
  author={LocalDoc},
  year={2025},
  publisher={Hugging Face},
  url={https://huggingface.co/LocalDoc/pii-ner-azerbaijani-v3}
}
```

## CC BY 4.0 License — What It Allows

The **Creative Commons Attribution 4.0 International (CC BY 4.0)** license allows:

### ✅ You Can:
- **Use** the model for any purpose, including commercial use.
- **Share** it — copy and redistribute in any medium or format.
- **Adapt** it — remix, transform, and build upon it for any purpose, even commercially.

### 📝 You Must:
- **Give appropriate credit** — Attribute the original creator.
- **Not imply endorsement** — Do not suggest the original author endorses your use.

### ❌ You Cannot:
- Apply legal terms or technological measures that restrict others from doing anything the license permits.

For more information, refer to the <a target="_blank" href="https://creativecommons.org/licenses/by/4.0/deed.en">CC BY 4.0 license</a>.

## Contact

For questions or issues, contact LocalDoc at [v.resad.89@gmail.com].