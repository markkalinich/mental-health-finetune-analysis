---
license: cc-by-sa-4.0
language:
- en
metrics:
- exact_match
- levenshtein_similarity
base_model:
- google/flan-t5-large
tags:
- poetry
- meter
- stress
- flan-T5
- eighteenth-century-poetry
---
# KemiOm/poetry-meter-best
`KemiOm/poetry-meter-best` is a LoRA-adapted `google/flan-t5-large` model for **line-level meter/stress prediction** in English poetry.
Given a single poetic line, the model predicts its stress pattern (meter representation) as a compact symbolic sequence.

## Task
- **Input:** one poetic line
- **Output:** stress pattern string (e.g., `-+-+-+-+-+`)
Example:
- Input: `Tired Nature's sweet restorer, balmy Sleep!`
- Output: `+-+-+-+-+-+`
This is a **meter-only labeling model**, not a full poetry generator.

## Training Data Format
The meter-only dataset uses line-level supervision:
- `input`: poetic line text
- `target`: stress/meter pattern string
The model is trained to map each line directly to its metrical stress pattern.

## Model Details
- **Developer:** KemiOm
- **Base model:** `google/flan-t5-large`
- **Method:** LoRA fine-tuning
- **Library:** Hugging Face Transformers + PEFT
- **Language:** English
- **Domain:** formal/historical poetry (including eighteenth-century material)
  
## Best Checkpoint and Training Setup
Best meter-only performance in your results appears in:
`results/round3/meter_only_lora_r3_lr1e4_flan-t5-large_lora_20260415_160740/zero_shot_meter_only_line_only.json`
Associated run configuration (`sft_runs/round3/meter_only_lr1e4/run_params.json`):
- epochs: `5.0`
- learning rate: `1e-4`
- weight decay: `0.01`
- warmup ratio: `0.1`
- per-device train batch size: `8`
- gradient accumulation steps: `1`
- per-device eval batch size: `4`
- max input length: `256`
- max target length: `64`
- LoRA rank (`r`): `16`
- LoRA alpha: `32`
- LoRA dropout: `0.05`
- LoRA target modules: `q,v`
- seed: `42`
- precision flags: `bf16=true`, `fp16 enabled`

## Intended Uses
- Automatic meter annotation for poetic corpora
- Meter diagnostics for generated verse
- Preprocessing/evaluation component in constrained poetry pipelines
- Educational tooling for stress-pattern analysis

## Limitations
- Stress ambiguity in English can produce multiple plausible scansions.
- Archaic spellings and punctuation can affect tokenization and stress assignment.
- Performance may drop on modern slang, non-poetic text, or out-of-domain genres.
- Meter labels reflect dataset conventions and annotation assumptions.
  
## Usage
```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
model_id = "KemiOm/poetry-meter-best"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
line = "Tired Nature's sweet restorer, balmy Sleep!"
inputs = tokenizer(line, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=24, do_sample=False)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
# expected format: "+-+-+-+-+-+" (example)