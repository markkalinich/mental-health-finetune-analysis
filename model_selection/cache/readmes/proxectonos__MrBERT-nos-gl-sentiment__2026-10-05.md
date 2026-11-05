---
license: apache-2.0
datasets:
- proxectonos/sentimento-gl
language:
- gl
base_model:
- proxectonos/MrBERT-nos-gl
tags:
- sentiment-analysis
pipeline_tag: text-classification
---

# MrBERT-nos-gl-sentiment: Sentiment Analysis for Galician

Fine-tuned version of [MrBERT-nos-gl](https://huggingface.co/proxectonos/MrBERT-nos-gl) for three-class sentiment analysis (positive / neutral / negative) in Galician. Developed as part of **Proxecto Nós**, an initiative to build language technology for the Galician language.

## Model Details

| Property | Value |
|---|---|
| **Base model** | `proxectonos/MrBERT-nos-gl` |
| **Task** | Text classification (sentiment analysis) |
| **Language** | Galician (`gl`) |
| **License** | Apache 2.0 |
| **Labels** | `POSITIVE`, `NEUTRAL`, `NEGATIVE` |

## Training Data

Fine-tuned on [proxectonos/sentimento-gl](https://huggingface.co/datasets/proxectonos/sentimento-gl), a Galician sentiment dataset.

## Usage

### Installation

```bash
pip install transformers torch
```

### Quick start

```python
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("proxectonos/MrBERT-nos-gl-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("proxectonos/MrBERT-nos-gl-sentiment")
sentiment_analyzer = pipeline(
    "text-classification",
    model=model,
    tokenizer=tokenizer,
)

text = "A película pareceume moi interesante e emotiva."
results = sentiment_analyzer(text, top_k=3)

for i, result in enumerate(sorted(results, key=lambda x: x['score'], reverse=True)):
    print(f"{i+1}. {result['label']:<20} {result['score']*100:.1f}%")
```

### Example output

```
1. POSITIVE             91.3%
2. NEUTRAL               6.2%
3. NEGATIVE              2.5%
```

### Interactive CLI (optional)

For interactive exploration from the command line:

```python
while True:
    text = input("Enter text to analyze sentiment: ").strip()
    if text.lower() in ["quit", "exit", "q"]:
        break
    results = sentiment_analyzer(text, top_k=3)
    for i, r in enumerate(sorted(results, key=lambda x: x['score'], reverse=True)):
        bar = "█" * int(r['score'] * 20)
        print(f"  {i+1}. {r['label']:<20} {r['score']*100:5.1f}%  {bar}")
```

## Acknowledgements

This work is funded by the Ministerio para la Transformación Digital y de la Función Pública - Funded by EU – NextGenerationEU within the framework of the project Desarrollo de Modelos ALIA. (Esta publicación del proyecto Desarrollo de Modelos ALIA está financiada por el Ministerio para la Transformación Digital y de la Función Pública y por el Plan de Recuperación, Transformación y Resiliencia – Financiado por la Unión Europea – NextGenerationEU)

## Citation

```bib
@misc{proxectenos2026mrbert-nos-gl-sentiment,
  author       = {{Proxecto Nós}},
  title        = {{MrBERT-nos-gl-sentiment}: Sentiment Analysis for Galician},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/proxectonos/MrBERT-gl-sentiment}},
}
```