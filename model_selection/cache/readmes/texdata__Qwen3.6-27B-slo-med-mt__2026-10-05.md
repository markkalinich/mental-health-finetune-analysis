---
license: other
license_name: qwen
language:
  - en
  - sl
tags:
  - vision
  - image-text-to-text
  - translation
  - medical
  - slovenian
  - qwen3
  - mtp
pipeline_tag: translation
library_name: transformers
base_model: llmfan46/Qwen3.6-27B-uncensored-heretic-v2-Native-MTP-Preserved
---

# Qwen3.6-27B-slo-med-mt

> Trained by **[MediaAtlas](https://mediaatlas.si/ai-training.html)** — LLM fine-tuning on your own data, trained in the EU, weights delivered. [Pricing](https://mediaatlas.si/ai-training-pricing.html) · [All our models](https://huggingface.co/texdata)

**Na kratko:** Strojno prevajanje medicinskih besedil angleščina ⇄ slovenščina (27B). Ohranja odmerke, enote, imena zdravil in zanikanja ter uporablja formalni medicinski register. Raziskovalno orodje: vsak prevod mora pred rabo preveriti človek. Sprejme tudi slike.

**Vision / slike:** the vision encoder of the base Qwen3.6 model is kept in this checkpoint, so it also takes images (load it with the processor, as the base model). Our training was text-only: image understanding is the base model's and was not evaluated in Slovenian.

English ⇄ Slovenian **medical machine translation** (MT = *strojno prevajanje*),
merged full model. A dense **Qwen3.6-27B** fine-tune specialised for translating
medical / clinical / scientific text while preserving doses, units, drug names
and negation, and using the formal Slovenian medical register.

The dense 27B base already produces strong Slovenian morphology (its ~27B active
params handle case/agreement better than a 3B-active MoE); this fine-tune adds
formal medical terminology and cleans register/borrowing issues. **MTP
(multi-token-prediction) tensors are preserved** for speculative decoding.

> Intermediate research artifact: a domain translator used to build a Slovenian
> medical dataset. **Not** a medical assistant, **not** a clinical product.

---

## ⚠️ Disclaimer — read before use

**NOT MEDICAL ADVICE.** Released **for research and educational purposes only**.
A *translation* tool, not a source of medical information, diagnosis or treatment.

- **No clinical use.** Do not use this model or its output to diagnose, treat, or
  advise any person. It does **not** replace a clinician (*"ne nadomešča
  zdravnika"*).
- **MT can be wrong in dangerous ways** — it can mistranslate a dose, unit, drug
  name, or **negation**. **Every translation must be verified by a qualified
  human** before any real-world use.
- **Uncensored base.** The base is an uncensored ("heretic") variant with safety
  alignment removed — intentional for translation *fidelity* (won't refuse/soften
  clinical content), but it means **no safety guardrails**. Do not deploy in any
  user-facing or generative role.
- **Hallucination & bias**, as with any LLM. Output is not guaranteed faithful,
  complete, or accurate. Known weakness: **spelled-out large numbers** (e.g.
  "eighty-eight") are sometimes mistranslated (digit numbers like "88" / "500 mg"
  are reliable).
- **No warranty, no liability.** Provided **"as is"**; the authors accept **no
  liability** for any loss or harm. **Use entirely at your own risk** and comply
  with all applicable laws (medical-device, data-protection, etc.). Not a medical
  device; not evaluated by any regulator (FDA/EMA/…).

By downloading or using this model you accept the above.

---

## Model details

- **Type:** merged full model (bf16), dense. LoRA merged into the base +
  MTP tensors grafted back (export drops them).
- **Base:** [`llmfan46/Qwen3.6-27B-uncensored-heretic-v2-Native-MTP-Preserved`](https://huggingface.co/llmfan46/Qwen3.6-27B-uncensored-heretic-v2-Native-MTP-Preserved)
  (dense Qwen3.6-27B, uncensored, hybrid linear-attention, vision-capable, MTP).
- **Task:** EN↔SL translation of medical / clinical / scientific text.
- **Adapter (before merge):** QLoRA rank 128 / alpha 256, `lora_target: all`,
  1 full epoch (6191 steps). Also published separately as
  `Qwen3.6-27B-slo-med-mt-LoRA`.
- **Chat template:** `qwen3_5`. **MTP:** 15 `mtp.*` tensors preserved (bf16).

### Intended use
Research: building/curating Slovenian medical parallel data; batch-translating an
English medical corpus for later human review.
**Out of scope:** clinical decision support, patient-facing chat, generating
medical advice, unsupervised/production translation without human review.

## Training data

Public / permissive EN–SL parallel corpora from [OPUS](https://opus.nlpl.eu/),
quality-filtered (boilerplate / length-ratio / dedup). ~1.0M sentence pairs (both
directions), medical ≈ 57%:

| corpus | ~pairs (cap) | domain | source / license |
|---|---|---|---|
| **EMEA** | 242k | medical (drug leaflets / EPARs) | Public — European Medicines Agency · [OPUS-EMEA](https://opus.nlpl.eu/EMEA/) |
| **ELRC health sets** (vaccination, EU-medi, wiki-health, antibiotic, COVID) | 44k | medical | CC-BY-4.0 · ELRC-SHARE / OPUS |
| **ECDC** | 2k | public health | Public — ECDC · [OPUS-ECDC](https://opus.nlpl.eu/ECDC/) |
| **ELRC-SciPar** | 120k | scientific (theses/abstracts) | CC-BY-4.0 · ELRC / OPUS |
| **Europarl** | 100k | general (fluency regularizer) | Public — European Parliament · [OPUS-Europarl](https://opus.nlpl.eu/Europarl/) |

Attribute the above. No proprietary, scraped, or patient data. SciELO /
UFAL-Medical have no en-sl pairs; this exhausts the medical en-sl bitext on OPUS.

## Training procedure

QLoRA (4-bit bnb NF4) + Liger, LLaMA-Factory, `template: qwen3_5`,
`neat_packing: false`, `cutoff_len` 1024. lr 2e-5 cosine, warmup 0.03, effective
batch 16, **1 full epoch (6191 steps)**, bf16, gradient checkpointing. Dense
Qwen3.6-27B has no broken-bf16 forward and no MoE mask crash, so training/eval are
straightforward.

## Evaluation

**FLORES-200 devtest (en→sl, 1012 sentences, beam=5, sacreBLEU)** — a clean,
general-domain benchmark the model never saw:

| decoding | model | BLEU | chrF |
|---|---|---|---|
| beam=5 | **Qwen3.6-27B-slo-med-mt (this)** | 29.47 | 57.62 |
| beam=5 | base dense 27B (no fine-tune) | 29.36 | 57.96 |
| greedy | **Qwen3.6-27B-slo-med-mt (this)** | 27.36 | 55.62 |
| greedy | base dense 27B (no fine-tune) | 28.03 | 56.90 |

On **general-domain** FLORES the fine-tune is **≈ the base** — within noise at
beam=5 (BLEU +0.11) and marginally below at greedy (BLEU −0.67): the medical
fine-tune neither meaningfully helps nor hurts general translation. Its value is
**medical-domain terminology**, not general MT. Beam=5 gains ~2 BLEU over greedy
for both models; GGUF/llama.cpp typically decodes **greedy**.

Qualitative (100 clinical sentences, en→sl): terminology aligned to the formal
medical register (*odmerek* not *doza*, *pediatrični* not *otroška*), Croatian-ish
borrowings cleaned (*Jedno→eno*, *Sumnjivo→Sumljivo*, *Higiene→Higiena*), doses /
units (*°C*, *mg*) and negation preserved. Residual weakness: spelled-out large
numbers (digit numbers are reliable).

## Recommended settings (MT)

This is a **reasoning-capable** base — for translation you want the reasoning
trace **off** and near-deterministic decoding:

| setting | value | why |
|---|---|---|
| **thinking / reasoning** | **OFF** — `enable_thinking=False`, or put `<|think_off|>` in the system prompt (LM Studio: System Prompt field) | otherwise it emits a `<think>` trace instead of the translation |
| temperature | **0** (greedy) — or ≤ 0.3 | faithful, reproducible output; no creative drift |
| top_p / top_k | 0.9 / 20 (only if sampling) | — |
| repetition_penalty | **1.05** | avoids loops without hurting fidelity |
| num_beams | **5** (transformers) | best Slovenian morphology; GGUF/llama.cpp → use greedy |
| max_new_tokens | 256–512 | translations are short; cap to avoid rambling |

Prompt (exact): `Translate the following English medical text into Slovenian. Output only the translation:\n\n{src}` (swap the languages for sl→en). Send it as the **user** message; no custom system prompt needed.

## How to use

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

repo = "texdata/Qwen3.6-27B-slo-med-mt"
tok = AutoTokenizer.from_pretrained(repo, trust_remote_code=True)
bnb = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4",
                         bnb_4bit_compute_dtype=torch.bfloat16, bnb_4bit_use_double_quant=True)
model = AutoModelForCausalLM.from_pretrained(repo, quantization_config=bnb,
                                             device_map="auto", trust_remote_code=True).eval()

prompt = "Translate the following English medical text into Slovenian. Output only the translation:\n\n{src}"
msg = [{"role": "user", "content": prompt.format(src="Store the vaccine at 2-8 °C and do not freeze.")}]
enc = tok.apply_chat_template(msg, add_generation_prompt=True, return_tensors="pt",
                              return_dict=True, enable_thinking=False)
enc = {k: v.to(model.device) for k, v in enc.items()}
out = model.generate(**enc, max_new_tokens=256, num_beams=5, repetition_penalty=1.05)
print(tok.decode(out[0][enc["input_ids"].shape[1]:], skip_special_tokens=True))
```

Reverse direction: swap the instruction to "Translate the following Slovenian
medical text into English." Use `num_beams=5` for best Slovenian grammar. A GGUF
build (`-GGUF`) preserves MTP for speculative decoding in llama.cpp.

## License

Derivative of the Qwen base — released under the **Qwen license**; comply with it
and with the training-corpus licenses/terms above. Verify the base model's terms
permit your use before redistributing.

## Acknowledgements

Qwen team (Qwen3.6-27B) and the `llmfan46` uncensored/MTP-preserved dense variant;
data from EMA, ELRC / ELRC-SHARE, ECDC, the European Parliament, and OPUS
(Tiedemann, 2012).

## Citation

**Cite this work** (Tadej Fius, MediaAtlas Ltd):

```bibtex
@misc{fius2026qwen27bmt,
  title        = {Qwen3.6-27B Slovenian Medical Machine Translation (merged)},
  author       = {Fius, Tadej},
  year         = {2026},
  publisher    = {MediaAtlas Ltd},
  howpublished = {Hugging Face},
  url          = {https://huggingface.co/texdata/Qwen3.6-27B-slo-med-mt}
}
```

Upstream / source citations:

If you use this model, please cite the base model, the parallel corpora, and the
evaluation resources:

```bibtex
@misc{qwen3,
  title  = {Qwen3 Technical Report},
  author = {{Qwen Team}},
  year   = {2025},
  url    = {https://huggingface.co/Qwen}
}
@inproceedings{tiedemann2012opus,
  title     = {Parallel Data, Tools and Interfaces in {OPUS}},
  author    = {Tiedemann, J{\"o}rg},
  booktitle = {Proc. of LREC},
  year      = {2012}
}
@article{nllbflores2022,
  title   = {No Language Left Behind: Scaling Human-Centered Machine Translation},
  author  = {{NLLB Team}},
  journal = {arXiv:2207.04672},
  year    = {2022}
}
@inproceedings{post2018sacrebleu,
  title     = {A Call for Clarity in Reporting {BLEU} Scores},
  author    = {Post, Matt},
  booktitle = {Proc. of WMT},
  year      = {2018}
}
```

Corpora: EMEA, ELRC-SHARE health sets, ECDC, ELRC-SciPar, and Europarl, distributed
via [OPUS](https://opus.nlpl.eu/). Evaluation on FLORES-200 with sacreBLEU.
