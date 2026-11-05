---
license: apache-2.0
library_name: transformers
pipeline_tag: image-text-to-text
tags: [medical, vqa, vision-language, healthcare, morocco, lora, smolvlm]
base_model: HuggingFaceTB/SmolVLM-256M-Instruct
datasets: [flaviagiammarino/vqa-rad]
language: [en]
---

# doctoria-rally-ai 🩺

Fine-tuned medical Vision-Language Model for **SahhaAI** — offline, private
wound-care & medical VQA for disconnected clinics in Morocco.

- **Base:** `HuggingFaceTB/SmolVLM-256M-Instruct` (SmolVLM)
- **Method:** LoRA fine-tune (PyTorch + PEFT, trained locally on Apple Silicon / MPS)
- **Data:** [VQA-RAD](https://huggingface.co/datasets/flaviagiammarino/vqa-rad) (radiology VQA, CC0)
- **Runs:** in-browser (WebGPU via transformers.js) and locally — data stays on device

## Benchmark (VQA-RAD test)

- Closed-ended accuracy: **0.439**
- Open-ended token-F1: **0.228**
- Speed: **19.0 tok/s** on Apple Silicon (MPS)
- See repo `finetune/BENCHMARK.md` for base-vs-fine-tuned analysis.

## Use
```python
from transformers import AutoProcessor, AutoModelForImageTextToText
from PIL import Image
m = AutoModelForImageTextToText.from_pretrained("doctoria/doctoria-rally-ai")
p = AutoProcessor.from_pretrained("doctoria/doctoria-rally-ai")
msgs = [{"role":"user","content":[{"type":"image"},{"type":"text","text":"Assess this wound."}]}]
text = p.apply_chat_template(msgs, add_generation_prompt=True)
inp = p(text=text, images=[[Image.open("wound.jpg")]], return_tensors="pt")
print(p.batch_decode(m.generate(**inp, max_new_tokens=128), skip_special_tokens=True)[0])
```

⚠ **Decision support, not a diagnosis.** A trained health worker stays in the loop.

— Author: **Jad Tounsi El Azzouzi** · part of SahhaAI · Apache-2.0
