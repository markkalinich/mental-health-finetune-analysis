---
language:
  - ro
tags:
  - biomedical
  - clinical
  - EHR
  - NER
  - named-entity-recognition
  - token-classification
  - multiclinner
  - ro
  - symptom
license: cc-by-4.0
metrics:
  - f1
base_model:
  - FacebookAI/xlm-roberta-base
pipeline_tag: token-classification
model-index:
  - name: BSC-NLP4BIA/multiclinner-ro-symptom-xlm-roberta
    results:
      - task:
          type: token-classification
        dataset:
          name: MultiClinNER ro symptom (test)
          type: MultiClinNER
        metrics:
          - name: strict F1
            type: f1
            value: 0.5833
          - name: char F1 (gold)
            type: f1
            value: 0.7334
---

# multiclinner-ro-symptom-xlm-roberta

## Table of contents
<details>
<summary>Click to expand</summary>

- [Model description](#model-description)
- [Usage](#usage)
- [Evaluation](#evaluation)
- [Limitations and bias](#limitations-and-bias)
- [Additional information](#additional-information)
  - [Authors](#authors)
  - [Contact information](#contact-information)
  - [Funding](#funding)
  - [Citing information](#citing-information)
  - [Disclaimer](#disclaimer)

</details>

## Model description
A fine-tuned version of [FacebookAI/xlm-roberta-base](https://huggingface.co/FacebookAI/xlm-roberta-base) for **SYMPTOM Named Entity Recognition** in Romanian clinical text. It was developed for MultiClinNER, a subtask of the [MultiClinAI shared task](https://temu.bsc.es/MultiClinAI/) organized by the NLP4BIA team at the Barcelona Supercomputing Center as part of the #SMM4H-HeaRD Workshop at the ACL 2026 conference. The model labels mentions of **SYMPTOM** using the BIO tagging scheme: `O`, `B-SYMPTOM`, `I-SYMPTOM`.

## Usage

This is a token-classification (NER) model. **It was trained on pre-tokenized text** (`is_split_into_words=True`). For predictions that match our reported scores, reproduce that tokenization at inference (split into word/non-word tokens, run, then re-align offsets). A plain `pipeline(raw_text)` still gives correct character offsets, but its subword tokenization differs from training, so boundary predictions near punctuation may differ.

### Recommended: `ner_nlp4bia` (handles pre-tokenization + offset re-alignment)

```python
# pip install git+https://github.com/nlp4bia-bsc/ner-nlp4bia.git   # not on PyPI; install from git
from ner_nlp4bia.data.corpus import Document
from ner_nlp4bia.inference.pipeline import PipelineInferencer

inf = PipelineInferencer("BSC-NLP4BIA/multiclinner-ro-symptom-xlm-roberta")          # stride=128, aggregation="first"
doc = inf.infer_document(Document(filename="d1", text=open("note.txt").read()))
for a in doc.annotations:
    print(a.label, a.start, a.end, repr(a.text))   # offsets in original-text coords
```

### Plain transformers (you must pre-tokenize and re-align yourself)

```python
import re
from transformers import pipeline

TOK = re.compile(r'([0-9A-Za-zÀ-ÖØ-öø-ÿ]+|[^0-9A-Za-zÀ-ÖØ-öø-ÿ])')

def pretokenize(text):
    toks = [t for t in TOK.split(text) if t]
    i = 1
    while i < len(toks):
        if not toks[i-1].isspace() and not toks[i].isspace():
            toks.insert(i, ' '); i += 1
        i += 1
    pre = ''.join(toks)
    oi = pj = 0; ins = []                 # positions of inserted spaces in `pre`
    while pj < len(pre):
        if oi < len(text) and text[oi] == pre[pj]:
            oi += 1; pj += 1
        else:
            ins.append(pj); pj += 1
    return pre, ins

nlp = pipeline("token-classification", model="BSC-NLP4BIA/multiclinner-ro-symptom-xlm-roberta",
               aggregation_strategy="first")
# window long docs (RoBERTa/LtgBERT reserve 2 positions -> use mpe-2 for those)
nlp.tokenizer.model_max_length = nlp.model.config.max_position_embeddings

text = open("note.txt").read()
pre, ins = pretokenize(text)
for e in nlp(pre, stride=128):
    if e["start"] == e["end"]:
        continue
    s = e["start"] - sum(1 for x in ins if x < e["start"])
    t = e["end"]   - sum(1 for x in ins if x < e["end"])
    while s < t and text[s].isspace():   s += 1     # byte-BPE leading-space trim
    while t > s and text[t-1].isspace(): t -= 1
    print(e["entity_group"], s, t, repr(text[s:t]))
```

Notes:
- `stride=128` matches the training stride; prevents truncation of long documents.
- For RoBERTa/LtgBERT-family checkpoints set `model_max_length = max_position_embeddings - 2`.

## Evaluation

Scores were computed with the official [MultiClinAIEval](https://github.com/nlp4bia-bsc/MultiClinAIEval) library on the MultiClinNER **Romanian** gold-standard test documents for **SYMPTOM** (the shared-task gold set for this language and entity type).

| Metric | Score | Definition |
|---|---|---|
| strict F1 | 0.5833 | exact match of both entity span (start/end) and label |
| char F1 (gold) | 0.7334 | character-level F1, restricted to the gold-standard documents |

See the [MultiClinAI shared task](https://temu.bsc.es/MultiClinAI/) for the full evaluation protocol.

## Limitations and bias
At the time of submission, no measures have been taken to estimate the bias embedded in the model. However, we are well aware that our models may be biased. We intend to conduct research in these areas in the future, and if completed, this model card will be updated.

## Additional information

### Authors
NLP4BIA team at the Barcelona Supercomputing Center (nlp4bia@bsc.es).

### Contact information
jan.rodriguez [at] bsc.es

### Funding
More information will be available soon.

### Citing information
Please cite the MultiClinAI shared task overview paper (forthcoming).

```bibtex




```

### Disclaimer

The models published in this repository are intended for a generalist purpose and are available to third parties. These models may have bias and/or any other undesirable distortions.

When third parties deploy or provide systems and/or services to other parties using any of these models (or using systems based on these models) or become users of the models, they should note that it is their responsibility to mitigate the risks arising from their use and, in any event, to comply with applicable regulations, including regulations regarding the use of artificial intelligence.

---
Los modelos publicados en este repositorio tienen una finalidad generalista y están a disposición de terceros. Estos modelos pueden tener sesgos y/u otro tipo de distorsiones indeseables.

Cuando terceros desplieguen o proporcionen sistemas y/o servicios a otras partes usando alguno de estos modelos (o utilizando sistemas basados en estos modelos) o se conviertan en usuarios de los modelos, deben tener en cuenta que es su responsabilidad mitigar los riesgos derivados de su uso y, en todo caso, cumplir con la normativa aplicable, incluyendo la normativa en materia de uso de inteligencia artificial.
