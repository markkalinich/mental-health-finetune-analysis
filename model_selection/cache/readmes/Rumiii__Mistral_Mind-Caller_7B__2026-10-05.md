---
license: apache-2.0
base_model: mistralai/Mistral-7B-Instruct-v0.3
pipeline_tag: text-generation
library_name: transformers
tags:
- function-calling
- tool-calling
- mistral
- qlora
- mental-health
- fine-tuned
datasets:
- frshafi/mind_call
- Salesforce/xlam-function-calling-60k
---
![Screenshot 2026-09-06 at 4.09.56 PM](https://cdn-uploads.huggingface.co/production/uploads/66e00ba55e4fd4bfead4a97c/lozTnrcQqBekl2k9MSmQG.png)
# Mistral_Mind-Caller_7B
QLoRA fine-tune of [mistralai/Mistral-7B-Instruct-v0.3](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3),
sharpening its native tool-calling ability for mental-health / wearable-data function calling,
while preserving general tool-calling range via a replay mix.
## Training data
- [frshafi/mind_call](https://huggingface.co/datasets/frshafi/mind_call) (train split, apache-2.0) --
  3,814 cleaned examples mapping natural-language health queries (explicit, implicit, behavioral,
  symptom-based, and metaphorical phrasing) to the correct wearable-data function call.
- [Salesforce/xlam-function-calling-60k](https://huggingface.co/datasets/Salesforce/xlam-function-calling-60k)
  (850-example replay slice, cc-by-4.0) -- mixed in to preserve general argument-schema diversity and
  prevent narrowing onto only the MindCall function shape.
- Combined: 4,664 examples, ~18% xLAM replay.
## Training details
- Method: QLoRA (4-bit NF4), LoRA rank 16, alpha 32, targeting all attention + MLP projections.
- Format: examples rendered through Mistral's native `[AVAILABLE_TOOLS]`/`[TOOL_CALLS]` chat template
  (via `tokenizer.apply_chat_template(..., tools=...)`), not a custom prompt format -- this fine-tune
  sharpens Mistral's existing tool-calling mechanism rather than replacing it.
- Most MindCall examples show the correct function plus a random subset of distractor functions
  (5-10 tools total) rather than the full 20-function registry every time; ~30% of examples show the
  full registry, matching the real deployment scenario where all functions are available at once.
  This keeps context length practical while still training on the full-registry case.
- 2 epochs, effective batch size 16, cosine LR schedule, max sequence length 3072 tokens, trained on a
  single Kaggle T4 (16GB) via Unsloth.
- Training loss converged from ~0.50 to ~0.13.
## Intended use
Research / educational project demonstrating domain fine-tuning of an already tool-calling-capable
open model. Not validated for clinical or diagnostic use. The wearable-data functions it targets are
illustrative (`get_heart_rate_data`, `get_sleep_data`, etc.) and require the caller to implement the
actual data-retrieval backend.
## Inference

```python
from unsloth import FastLanguageModel
import torch

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="Rumiii/Mistral_Mind-Caller_7B",
    max_seq_length=3072,
    dtype=None,
    load_in_4bit=True,
)
FastLanguageModel.for_inference(model)

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_sleep_data",
            "description": "Retrieve the user's sleep data for a given number of days.",
            "parameters": {
                "type": "object",
                "properties": {
                    "patient_id": {"type": "string", "description": "Unique patient identifier."},
                    "num_days": {"type": "integer", "description": "Number of days of data to retrieve."},
                },
                "required": ["patient_id", "num_days"],
            },
        },
    }
]

messages = [{"role": "user", "content": "I've been having trouble sleeping this week."}]

prompt = tokenizer.apply_chat_template(
    messages, tools=tools, tokenize=False, add_generation_prompt=True,
)
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

output_ids = model.generate(
    **inputs,
    max_new_tokens=150,
    do_sample=False,
    pad_token_id=tokenizer.eos_token_id,
)
print(tokenizer.decode(output_ids[0][inputs["input_ids"].shape[1]:], skip_special_tokens=False))
```

## License
Base model and training data are apache-2.0 / cc-by-4.0; this fine-tune is released apache-2.0.