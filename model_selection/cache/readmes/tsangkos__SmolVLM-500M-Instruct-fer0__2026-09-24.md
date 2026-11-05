---
library_name: transformers
license: apache-2.0
base_model: HuggingFaceTB/SmolVLM-500M-Instruct
tags:
- fine-tuned
- vision-language
- emotion-recognition
model-index:
- name: SmolVLM-500M-Instruct-fer0
  results: []
---

# SmolVLM-500M-Instruct-fer0

Fine-tuned version of [SmolVLM-500M-Instruct](https://huggingface.co/HuggingFaceTB/SmolVLM-500M-Instruct) on a subset of AffectNet (emotion recognition), with text labels transcribed via GPT-4o-mini.


This is just priliminary, we'll update soon with proper evalutation and info.
## Example

**Image input**  
![image](https://cdn-uploads.huggingface.co/production/uploads/6433b05aea46c00990443927/1I9PtODn5Iv-ThvTAugOW.png)

**Predictions:**  
- *Base model*: A woman with blonde hair is looking to the side with a hand on her chin.
- *This model*: The expression conveys a sense of contemplation or concern. The furrowed brow and slightly parted lips suggest a deep thought or worry. The hand on the chin indicates a hint of introspection, hinting at a possible emotional state of unease or contemplation.


## Training Summary

- **Loss values**:  

| Step  | Training Loss |
|-------|----------------|
| 25    | 2.80           |
| 50    | 0.82           |
| 75    | 0.48           |
| 100   | 0.43           |

- **Hyperparameters**:  
  - Learning rate: 1e-4  
  - Batch size: 4 (grad. accum. ×4)  
  - Epochs: 1  
  - Optimizer: 8-bit AdamW  
  - Scheduler: linear (warmup 50 steps)  
  - Seed: 42

## Frameworks

- Transformers 4.50.0  
- PyTorch 2.3.1+cu121  
- Datasets 3.6.0  
- Tokenizers 0.21.1

# Run it by loading the processor of the base model:


```# smol_min.py
import argparse
import torch
from transformers import AutoProcessor, AutoModelForVision2Seq
from transformers.image_utils import load_image

FINE_ID = "JoseferEins/SmolVLM-500M-Instruct-fer0"   # your fine-tuned model
BASE_ID = "HuggingFaceTB/SmolVLM-500M-Instruct"      # base model (and processor)
DEFAULT_IMAGE = "image.png"
PROMPT = "Describe the emotional state of the person."

device = "cuda" if torch.cuda.is_available() else "cpu"

def load_model(model_id: str):
    try:
        return AutoModelForVision2Seq.from_pretrained(
            model_id,
            dtype=torch.bfloat16 if device == "cuda" else torch.float32,
            attn_implementation="eager",
        ).to(device).eval()
    except TypeError:
        # for older transformers parameter name
        return AutoModelForVision2Seq.from_pretrained(
            model_id,
            torch_dtype=torch.bfloat16 if device == "cuda" else torch.float32,
            _attn_implementation="eager",
        ).to(device).eval()

def run_once(model, processor, image_path: str, max_new_tokens: int) -> str:
    image = load_image(image_path)
    messages = [{"role": "user", "content": [{"type": "image"}, {"type": "text", "text": PROMPT}]}]
    prompt = processor.apply_chat_template(messages, add_generation_prompt=True)
    inputs = processor(text=prompt, images=[image], return_tensors="pt").to(device)
    with torch.inference_mode():
        ids = model.generate(**inputs, max_new_tokens=max_new_tokens)
    return processor.batch_decode(ids, skip_special_tokens=True)[0]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", choices=["fine", "base", "both"], default="both",
                    help="Which model to run: your fine-tuned repo, the base, or both.")
    ap.add_argument("--image", default=DEFAULT_IMAGE, help="Path/URL to image.")
    ap.add_argument("--max_new_tokens", type=int, default=256)
    args = ap.parse_args()

    # Processor always from BASE (it has tokenizer & preprocessor files)
    processor = AutoProcessor.from_pretrained(BASE_ID)

    if args.model in ("fine", "both"):
        fine_model = load_model(FINE_ID)
        out = run_once(fine_model, processor, args.image, args.max_new_tokens)
        print("\n=== Output (FINE) ===")
        print(out)

    if args.model in ("base", "both"):
        base_model = load_model(BASE_ID)
        out = run_once(base_model, processor, args.image, args.max_new_tokens)
        print("\n=== Output (BASE) ===")
        print(out)

if __name__ == "__main__":
    main()
```