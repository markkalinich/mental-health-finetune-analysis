---
license: cc-by-sa-4.0
language:
  - sl
tags:
  - grammatical-error-correction
  - gec
  - slovenian
  - text2text-generation
  - t5
  - post-editing
base_model: cjvt/t5-sl-small
pipeline_tag: text-generation
library_name: transformers
---

# t5-sl-medical-gec

> Trained by **[MediaAtlas](https://mediaatlas.si/ai-training.html)** — LLM fine-tuning on your own data, trained in the EU, weights delivered. [Pricing](https://mediaatlas.si/ai-training-pricing.html) · [All our models](https://huggingface.co/texdata)

A small **Slovenian grammar / case-agreement corrector** for **post-editing
machine-translated medical text**. Fine-tune of [`cjvt/t5-sl-small`](https://huggingface.co/cjvt/t5-sl-small)
(~76M params). It fixes the *declension / adjective-noun agreement* slips that a
large LLM translator tends to make in Slovenian (e.g. *krvnega glukoze* →
*krvne glukoze*), without touching numbers, units or drug names.

Intended as a **cheap post-edit step** after an MT model, gated by a
term-preservation check.

---

## ⚠️ Disclaimer

Research/educational tool. **Not medical advice**, not a clinical product. It is
a *grammar* corrector, not a source of medical information. Output must be
verified by a qualified human before any real-world use. Provided **as is,
without warranty; no liability** is accepted for its use or misuse. Because it
rewrites text, always pair it with a check that numbers / units / drug names are
unchanged (it is trained not to touch them, but verify).

## What it does

Input:  `popravi: <slovenian text with case/agreement errors>`
Output: `<corrected slovenian text>`

- Fixes case-ending and **gender-agreement** errors (the class an LLM translator
  produces): *vzdrževalna odmerka → vzdrževalni odmerek*, *intravenskimi
  lorazepamom → intravenskim lorazepamom*, *Depresijo značata → Depresija je
  značilna po …*.
- **Does not over-edit** already-correct text (trained with ~20% identity pairs).
- **Does not** fix lexical calques (e.g. *rdeča zastavica* for "red flag") or
  every noun-form error — those are out of scope for a case-GEC.

On a held-out set of clinical sentences it cleanly fixes ~half of the residual
case/agreement slips left after beam search.

## Training

- **Base:** `cjvt/t5-sl-small`.
- **Data:** ~147k synthetic `(corrupt, clean)` pairs. Clean Slovenian sentences
  (the SL side of the EMEA / Europarl OPUS corpora — human translations, not MT)
  are corrupted by swapping noun/adjective **case endings within cross-gender
  confusion sets**; ~20% are left uncorrupted (identity) so the model learns not
  to over-edit. Numbers, units, ALL-CAPS codes and short words are never
  corrupted.
- **Objective:** text-to-text restoration, prefix `popravi: `. 3 epochs.
- This is a *prototype-grade* corruption (rule-based, no morphological
  analyser); a production version would use classla MSD tags + a sloleks
  generator for fully realistic inflection.

## Usage

```python
from transformers import AutoModelForSeq2SeqLM, PreTrainedTokenizerFast
from huggingface_hub import hf_hub_download

repo = "<your-org>/t5-sl-medical-gec"
tok = PreTrainedTokenizerFast(
    tokenizer_file=hf_hub_download(repo, "tokenizer.json"),
    eos_token="</s>", unk_token="<unk>", pad_token="<pad>",
)
model = AutoModelForSeq2SeqLM.from_pretrained(repo).eval()

def fix(text):
    enc = tok("popravi: " + text, return_tensors="pt", truncation=True, max_length=128)
    out = model.generate(**enc, max_new_tokens=160, num_beams=5, early_stopping=True)
    return tok.decode(out[0], skip_special_tokens=True)

print(fix("spremljati raven krvnega glukoze"))  # -> ... krvne glukoze
```

> Note: `cjvt/t5-sl-small`'s T5 slow tokenizer fails to load under recent
> transformers; load the fast `tokenizer.json` via `PreTrainedTokenizerFast` as
> shown.

## License

Inherits the base model's license (`cjvt/t5-sl-small`, CC BY-SA 4.0). Training
text is from EMEA (public) and Europarl (public) via OPUS. Attribute those
sources.

## Citation

**Cite this work** (Tadej Fius, MediaAtlas Ltd):

```bibtex
@misc{fius2026gec,
  title        = {t5-sl-medical-gec: Slovenian Medical GEC},
  author       = {Fius, Tadej},
  year         = {2026},
  publisher    = {MediaAtlas Ltd},
  howpublished = {Hugging Face},
  url          = {https://huggingface.co/texdata/t5-sl-medical-gec}
}
```

Upstream / source citations:

```bibtex
@misc{slot5, title={t5-sl-small}, author={{CJVT}}, url={https://huggingface.co/cjvt/t5-sl-small}}
@article{raffel2020t5, title={Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer}, author={Raffel, Colin and others}, journal={JMLR}, volume={21}, year={2020}}
```
Fine-tune of cjvt/t5-sl-small (Slovene T5). Cite the base + T5.
