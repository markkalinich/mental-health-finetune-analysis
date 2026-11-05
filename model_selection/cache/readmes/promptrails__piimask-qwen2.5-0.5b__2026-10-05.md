---
license: apache-2.0
base_model: Qwen/Qwen2.5-0.5B-Instruct
language:
  - en
  - tr
pipeline_tag: text-generation
library_name: transformers
tags:
  - pii
  - pii-detection
  - redaction
  - privacy
  - ner
  - qwen2
---

# piimask-qwen2.5-0.5b

A compact (0.5B) model that detects **PII** in **English and Turkish** short, informal
text — chat messages, support tickets, emails, form fields. It runs fully locally: no
data leaves the machine, no API, no key.

Given a text, it returns a JSON list of entities:

```json
{"entities": [{"type": "PERSON", "value": "Ayşe Yılmaz"}, {"type": "EMAIL", "value": "ayse@firma.com"}]}
```

Entity types: `PERSON, EMAIL, PHONE, NATIONAL_ID, IBAN, CREDIT_CARD, ADDRESS, DATE_OF_BIRTH, IP_ADDRESS`.

## Intended use & limitations

**For:** a local-first, best-effort PII detector for short, informal en/tr text —
scrubbing input before a third-party LLM, cutting PII in developer logs, a
privacy-conscious local utility.

**Not for:** a sole, compliance-grade safeguard. Redaction is a *recall* problem — a
miss is a leak — and on realistic out-of-distribution text this model misses a meaningful
fraction (concentrated on names, and on free-text entities in long or formal documents;
structured Turkish addresses are recovered by the grammar below). Do **not** make it the
only barrier before you log, store, or forward regulated data (GDPR / PCI / HIPAA). Use it
as one layer in defence-in-depth.

**Scope:** English + Turkish; short messages, not long documents; the nine types above.

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "promptrails/piimask-qwen2.5-0.5b"
tok = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

SYSTEM = (
    "You are a PII detection engine. Extract every piece of personally identifiable "
    "information from the user's text.\n\n"
    'Respond with ONLY a JSON object of the form:\n'
    '{"entities": [{"type": "<TYPE>", "value": "<exact substring from the text>"}]}\n\n'
    "Valid types: PERSON, EMAIL, PHONE, NATIONAL_ID, IBAN, CREDIT_CARD, ADDRESS, "
    "DATE_OF_BIRTH, IP_ADDRESS.\n"
    "Each value must be copied verbatim from the text. If the text contains no PII, "
    'respond with {"entities": []}.'
)

text = "Ben Ayşe Yılmaz, kartım 4111 1111 1111 1111, mailim ayse@firma.com"
prompt = tok.apply_chat_template(
    [{"role": "system", "content": SYSTEM}, {"role": "user", "content": text}],
    add_generation_prompt=True, tokenize=False,
)
ids = tok(prompt, return_tensors="pt").to(model.device)
out = model.generate(**ids, max_new_tokens=256, do_sample=False)
print(tok.decode(out[0][ids["input_ids"].shape[1]:], skip_special_tokens=True))
```

Checksummable types (EMAIL / IP / IBAN / CREDIT_CARD / NATIONAL_ID) pair with a
deterministic validation pass (format + check digit — Luhn, IBAN mod-97, TCKN) to maximise
precision on well-formed values. **Turkish addresses** — which have no checksum — pair with
the anchor grammar below instead.

### Turkish addresses — add the deterministic grammar

The model learned one Turkish address format and misses **street-first** addresses
(`Barbaros Hayrettin Paşa Sokak No:158 Daire:37 Konak/Adana`). This small, order-invariant
regex grammar catches them by structure and recovers recall to ~1.0 — add its matches to
the model output. It fires only on Turkish structure, so English is untouched:

```python
import re

_TR_IL = ("Adana Adıyaman Afyonkarahisar Afyon Ağrı Amasya Ankara Antalya Artvin Aydın "
    "Balıkesir Bilecik Bingöl Bitlis Bolu Burdur Bursa Çanakkale Çankırı Çorum Denizli "
    "Diyarbakır Edirne Elazığ Erzincan Erzurum Eskişehir Gaziantep Antep Giresun Gümüşhane "
    "Hakkari Hatay Isparta Mersin İçel İstanbul İzmir Kars Kastamonu Kayseri Kırklareli "
    "Kırşehir Kocaeli Konya Kütahya Malatya Manisa Kahramanmaraş Maraş Mardin Muğla Muş "
    "Nevşehir Niğde Ordu Rize Sakarya Samsun Siirt Sinop Sivas Tekirdağ Tokat Trabzon "
    "Tunceli Şanlıurfa Urfa Uşak Van Yozgat Zonguldak Aksaray Bayburt Karaman Kırıkkale "
    "Batman Şırnak Bartın Ardahan Iğdır Yalova Karabük Kilis Osmaniye Düzce").split()
_L = "A-Za-zçğıöşüÇĞİÖŞÜ"
_IL = re.compile(rf"(?<![{_L}])(?:" + "|".join(sorted(map(re.escape, _TR_IL), key=len, reverse=True)) + rf")(?![{_L}])")
_ANCHOR = re.compile(r"\b(mahallesi|mahalle|mah|mh|caddesi|cadde|cad|cd|sokağı|sokak|sok|sk|bulvarı|bulvar|blv|meydanı|meydan)\b\.?", re.I)
_NUM = re.compile(r"\b(no|numara|kat|daire|blok|apt|d)\b\.?\s*[:.]?\s*\d|\bno[:.]?\s*\d|\d+/\d+", re.I)

def _start(text, a):
    i = a
    while i > 0 and text[i - 1] == " ": i -= 1
    s = i
    while i > 0:
        j = i
        while j > 0 and (text[j - 1].isalnum() or text[j - 1] in "çğıöşüÇĞİÖŞÜ"): j -= 1
        w = text[j:i]
        if w and (w[0].isupper() or w[0].isdigit()):
            s = j; i = j
            while i > 0 and text[i - 1] == " ": i -= 1
            if i > 0 and text[i - 1] in ".,:;": break
        else:
            break
    return s

def turkish_addresses(text):
    spans = []
    for m in _IL.finditer(text):
        w0 = max(0, m.start() - 140)
        anchors = list(_ANCHOR.finditer(text[w0:m.start()]))
        if not anchors: continue
        st = _start(text[w0:m.start()], anchors[0].start()) + w0
        if not _NUM.search(text[st:m.end()]) and "mah" not in anchors[0].group().lower(): continue
        spans.append([st, m.end()])
    spans.sort(key=lambda s: (s[0], -(s[1] - s[0])))
    out = []
    for s in spans:
        if out and s[0] < out[-1][1]:
            out[-1][1] = max(out[-1][1], s[1])
        else:
            out.append(s)
    return [text[a:b] for a, b in out]

# merge: add addresses the model missed
# seen = {e["value"] for e in entities}
# entities += [{"type": "ADDRESS", "value": v} for v in turkish_addresses(text) if v not in seen]
```

## Evaluation

Entity-level micro-F1, **full piimask** (the model *plus* the deterministic passes above)
versus [Microsoft Presidio](https://github.com/microsoft/presidio) and the ai4privacy
DeBERTa PII NER (`Isotonic/deberta-v3-base_finetuned_ai4privacy_v2`).

**Independent bilingual benchmark** — a held-out, independently-constructed set of 400
short en/tr documents (some code-switched) with adversarial distractors (product codes,
reference numbers designed to trigger false positives):

| System | micro-F1 |
|---|---|
| **piimask (0.5B)** | **0.81** |
| ai4privacy DeBERTa | 0.65 |
| Microsoft Presidio | 0.51 |

**Turkish addresses** are the clearest win. The raw model — like both baselines — learned
one address format and misses *street-first* Turkish addresses, recall **0.16**; the
deterministic grammar above is order-invariant and lifts it to **~1.0**, with no effect on
English. Presidio and DeBERTa score ~0.00 on Turkish addresses.

**Other sets:**

| Eval set | piimask | Presidio | DeBERTa |
|---|---|---|---|
| Realistic Turkish PII (held-out test) | **0.89** | 0.42 | 0.47 |
| [piimb](https://huggingface.co/datasets/piimb/pii-masking-benchmark) aggregate (en) | **0.65** | 0.55 | — |
| [gretel](https://huggingface.co/datasets/gretelai/synthetic_pii_finance_multilingual) finance docs (en, out-of-distribution) | **0.49** | 0.37 | 0.37 |

Read these honestly: the Turkish and bilingual numbers are on piimask's target domain
(short, informal text); the gretel English row is long, formal finance documents — fully
out-of-distribution and the most conservative, like-for-like number. Redaction is a recall
problem, and on long formal text the model still misses a meaningful fraction — so use
piimask in defence-in-depth, not standing alone. DeBERTa is not scored on piimb, which
overlaps its own training data.

## License

Apache-2.0, inheriting the base model
[Qwen/Qwen2.5-0.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct)
(Apache-2.0).
