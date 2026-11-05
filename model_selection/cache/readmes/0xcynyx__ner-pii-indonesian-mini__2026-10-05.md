---
language:
- id
license: mit
library_name: transformers
pipeline_tag: token-classification
tags:
- named-entity-recognition
- pii
- indonesian
- bahasa-indonesia
- onnx
- quantized
- distillation
- transformers.js
base_model: indobenchmark/indobert-lite-base-p1
widget:
- text: "Nama saya Budi Santoso, pria, NIK 3204 0125 0990 0001, HP 081234567890."
- text: "Joko Widodo lahir di Surakarta pada tanggal 21 Juni 1961."
- text: "Silakan hubungi Siti di siti.rahma@contoh.co.id atau +62 812-3456-7890."
---

# NER PII Indonesian Mini

A small Indonesian PII detector: 11.1M parameters, **11.7 MB as quantized ONNX**, small enough
to run in a browser tab. It is distilled from
[ner-roberta-large-bahasa-indonesia-finetuned](https://huggingface.co/0xcynyx/ner-roberta-large-bahasa-indonesia-finetuned),
which is 2,235 MB, so this is roughly **191 times smaller** and about **4 times faster on CPU**.

Entity types: `PER`, `LOC`, `DATE_TIME`, `EMAIL`, `PHONE`, `GENDER`, `SSN` (Indonesian NIK).

## Why it exists

The teacher is XLM-R large. Nearly half its parameters are a 250k piece vocabulary covering 100
languages, which is wasted on a single language task, and its label set has no `I-` tag for
`EMAIL`, `PHONE`, `SSN` or `GENDER`, so it fragments identifiers across tokens. This student
fixes both: an Indonesian only vocabulary, and a complete BIO inventory with `B-` and `I-` for
all seven types.

## Results

Measured on 1,626 held out sentences labelled by the teacher, so these numbers describe how
closely the student reproduces the teacher rather than performance on an independent benchmark.

| | F1 | ms/doc CPU | Size |
|---|---|---|---|
| Teacher, original | 0.9098 | 48.8 | 2,235 MB |
| Teacher, trimmed and INT8 | 0.8883 | 18.6 | 337 MB |
| **This model, INT8 ONNX** | **0.9049** | **12.1** | **11.7 MB** |

Per type F1 for the INT8 build:

| Type | F1 | Held out spans |
|---|---|---|
| PHONE | 0.9966 | 447 |
| SSN | 0.9963 | 273 |
| EMAIL | 0.9933 | 448 |
| PER | 0.9103 | 1824 |
| LOC | 0.8605 | 1015 |
| GENDER | 0.8217 | 67 |
| DATE_TIME | 0.8056 | 646 |

## Usage

```python
from transformers import pipeline

ner = pipeline("token-classification", model="0xcynyx/ner-pii-indonesian-mini",
               aggregation_strategy="simple")
ner("Nama saya Budi, NIK 3204 0125 0990 0001, HP 081234567890.")
```

In the browser with transformers.js, the quantized ONNX build is used automatically:

```js
import { pipeline } from "@huggingface/transformers";

const ner = await pipeline("token-classification", "0xcynyx/ner-pii-indonesian-mini");
const out = await ner("Silakan hubungi Siti di siti.rahma@contoh.co.id");
```

Because it runs client side, text never leaves the user's device, which matters more for PII
than for most tasks.

## Limitations, read before deploying

- **Training data is mostly synthetic.** 30,923 template generated sentences with large slot
  pools plus 2,760 Indonesian Wikipedia lines. It is strong on form shaped text and less proven
  on free prose. The F1 above is agreement with the teacher on a similar distribution, not an
  independent benchmark.
- **One epoch.** Training stopped after the first epoch, which already reached parity with the
  teacher on this distribution. More epochs may help on natural text.
- **`GENDER` and `DATE_TIME` are the weak types.** `GENDER` had only 1,280 training examples,
  and `DATE_TIME` covers many surface forms.
- **Pair it with regex for structured PII.** Email, phone and NIK have exact formats, and a
  regex pass both repairs boundaries and catches what the model misses. The near perfect scores
  on those types come partly from the teacher labels having been regex corrected first.
- **Not compliance evidence.** Validate recall on your own data and jurisdiction before relying
  on it. Treat it as one control among several, not a guarantee.

## Training

Character span annotations from the teacher, with production post processing applied before
they became labels, so the student learns corrected boundaries rather than the teacher's
fragments. One epoch, batch 16, lr 5e-5, max length 160, on an Apple M4 GPU.

Pipeline and scripts: [ner-app-gradio/tools/compress](https://github.com/0xcynyx/ner-app-gradio/tree/main/tools/compress).

## License

MIT.
