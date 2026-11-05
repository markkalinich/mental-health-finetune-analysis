---
license: apache-2.0
language: [en]
base_model: answerdotai/ModernBERT-base
pipeline_tag: token-classification
library_name: transformers
tags: [token-classification, clinical, medical-records, chronology, ner, modernbert, onnx]
---

# decosa-clinical-events-modernbert-base (v1)

Tags clinical events and their dates on one page of a medical record, as an OCR/layout document reader returns it. Built
to replace a per-page LLM call when building a medical chronology (a dated list of what happened to a patient, each line
cited to a page).

Tags (BIO over sub-words):

- current events: `ENC` encounter, `DX` diagnosis, `PROC` procedure, `IMG` imaging, `LAB` lab, `MED` medication, `REF`
  referral or order;
- past events the page mentions ("status post ...", "seen in the ED last year"): `H-ENC` ... `H-REF`;
- dates: `VDATE` (date of a current event: date of service, exam, collection, a flow-sheet row) and `HDATE` (date of a
  past event). Birth, signature, fax, print and stamp dates are not tagged.

It finds text spans; it does not interpret them. It runs on a CPU: about 0.1 s a page (ONNX fp32, 8 threads).

**Not a medical device. Not for diagnosis, treatment or any clinical decision.** It is a drafting aid for people who
review records (for example a chronology a paralegal or nurse reviewer then checks against the source pages).

## Results

All evaluation packets are synthetic: invented patients, clinicians and facilities. "Reader output" means those packets
were rendered to PDF and images (typed, scanned, faxed, photographed, handwritten notes), then read by a real document
reader (PaddleOCR-VL plus layout detection), so the model sees real OCR noise. **No real medical records were used for
training or evaluation; accuracy on real records is not measured.** Model choice, the cascade threshold and the
post-processing were set on dev packets only.

Span level (40 held-out test packets, 818 pages of reader output, seeds and template variants not seen in training):

| | Events F1 (P / R) | Dates F1 (P / R) |
|---|---|---|
| Overlap match (a predicted span overlaps a gold span of the same tag) | 0.954 (0.971 / 0.937) | 0.955 (0.939 / 0.970) |
| Exact boundaries | 0.870 (0.886 / 0.855) | 0.853 (0.840 / 0.868) |

Pages with every span right: 73%. By page style (events, overlap F1): typed 0.970, handwritten notes 0.974, fax 0.958,
scan 0.950, typewriter 0.947, faint 0.937, phone photo 0.910, second-generation fax 0.893.

Chronology head-to-head on the same 40 test packets (2,160 required events). Every arm uses the same stored reader
output, BM25 retrieval and Qwen3.8-27B for the merge judgments; only the per-page extractor changes.

| Per-page extractor | Required events found | Dates right | Invented lines | Conflicts found (false) | LLM tokens | Extraction time per 100 pages |
|---|---|---|---|---|---|---|
| Qwen3.8-27B per page (the baseline) | 81.5% | **98.6%** | 4.1% | **26/40** (8) | 1.97M | 131 s (one H100) |
| **This model** | **88.7%** | 95.9% | 2.5% | 21/40 (5) | **0.10M** | **9 s (CPU)** |
| Cascade: this model, pages under confidence 0.5 go to Qwen | 87.6% | 96.5% | **1.3%** | **26/40** (7) | 0.24M | 33 s |
| ModernBERT-large variant (not released) | 89.5% | 95.8% | 2.9% | 20/40 (4) | 0.10M | 22 s (CPU) |

Base was chosen over large on dev (chronology recall 0.913 vs 0.872); on test large is 0.8 points higher, within noise.
Numbers and all four arms: `eval_summary.json`.

## Intended use

- Page-level extraction for a medical chronology or record summary, with a person checking every line against the cited
  page.
- As the first stage of a cascade: the page confidence (`ce_core.page_confidence`) sends uncertain pages to an LLM or a
  person.

Not for: diagnosis, treatment, triage or coding decisions; deciding anything about a person without human review;
non-English records; free-text generation. A page with no spans means the model found none of the trained kinds, not
that the page has no clinical content.

## Limitations (measured, see Results)

- Trained and tested only on synthetic packets. Real records have layouts, abbreviations and specialties the generator
  does not cover; validate on your own records before relying on it.
- Worse than the LLM on dates (95.9% vs 98.6% right) and finds fewer conflicting records (21 vs 26 of 40). Use the cascade
  if those matter most.
- Exact span boundaries are often off by a few words (exact-match F1 0.87 vs 0.95 overlap); downstream code should quote
  the surrounding text, not only the span.
- Weakest on phone photos and second-generation faxes (overlap F1 0.91 and 0.89).
- Dates are tagged, not parsed: a date split by OCR or written in an unusual format can come out in pieces.
- English, US-style records only.
- The int8 ONNX file is smaller and faster but agrees with fp32 on 97.4% of token argmaxes in our export check
  and on 91% on one page we re-checked before release; the evaluated runtime is fp32, so prefer it.

## Training data

Synthetic record packets only, made by a generator written for this model: templates and word banks (invented people,
facilities and towns; ordinary clinical vocabulary for diagnoses, studies, procedures, medications and labs) with
simulated OCR, fax and handwriting noise. No real patient data, no MIMIC, no n2c2, no text copied from real records.

- 96,844 text-level synthetic pages, plus 3,222 pages (160 packets) of the same kind of packets rendered and read by the
  document reader above.
- Rendering used freely licensed fonts (OFL and Apache-2.0 handwriting faces, Courier Prime, Liberation, DejaVu); no font
  is included here.
- The generator and the training and evaluation packets are not released.

No third-party dataset was used, so no data attribution is needed beyond the base model.

## Model

ModernBERT-base (answerdotai/ModernBERT-base, revision 8949b909, Apache-2.0, 150M parameters) with a token-classification
head over 33 labels. Fine-tuned 778 steps (2 epochs), AdamW, lr 5e-5, about 65k tokens a batch, max 1,024 tokens; 10.8
minutes on one A100. Checkpoint chosen on dev (span score 0.976).

Files:

- `model.safetensors`, `config.json`, `tokenizer.json`, `tokenizer_config.json`: the fine-tuned model for Transformers
  (`AutoModelForTokenClassification`, transformers >= 5).
- `onnx/model.onnx` (fp32, opset 18; the evaluated runtime; max abs logit difference from the safetensors weights
  3e-5) and `onnx/model.int8.onnx` (dynamic int8, not evaluated end to end).
- `ce_config.json`: labels, window length and overlap.
- `ce_core.py`: page serialization, labels, span decoding and page confidence (no dependencies).
- `usage.py`: a self-contained ONNX runner with overlapping windows for long pages.
- `eval_summary.json`, `SHA256SUMS`, `LICENSE`, `NOTICE`.

## Usage

The page must be serialized the way the model was trained (`ce_core.serialize`): a header line, then one line per reader
element, `<kind>: <text>`.

```python
from usage import ClinicalEvents          # usage.py and ce_core.py ship with the weights

m = ClinicalEvents("decosa-clinical-events-modernbert-base")   # pip install onnxruntime tokenizers numpy
elements = [  # one page, reading order, as your document reader returns it (invented example)
    {"id": "e1", "kind": "title", "text": "Lakeview Orthopedics - Office Visit"},
    {"id": "e2", "kind": "text", "text": "Date of service: 03/14/2024. Provider: Helena Ostrander, MD"},
    {"id": "e3", "kind": "text", "text": "Assessment: Right knee medial meniscus tear."},
    {"id": "e4", "kind": "text", "text": "Plan: MRI right knee ordered. Start naproxen 500 mg twice daily."},
]
text, spans, conf = m.page(elements, title="Lakeview Orthopedics: office records", page_no=1, n_pages=3)
for s in spans:
    print(s["tag"], text[s["start"]:s["end"]], round(s["p"], 2))
print(conf)   # {"weakest_span", "strongest_dropped", "score"}: send low-score pages to a slower checker
```

## Licence

Apache-2.0 for the weights and code in this repository. The base model, ModernBERT-base by Answer.AI and LightOn, is
Apache-2.0; see NOTICE.

## Citation and contact

Decosa, decosa.ai. Evaluation: docs/evals/clinical-events.md in the Decosa API repository (numbers reproduced above).
