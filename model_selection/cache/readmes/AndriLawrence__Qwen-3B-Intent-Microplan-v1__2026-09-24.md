---
language: en
license: other
library_name: transformers
pipeline_tag: text-generation
base_model: bunnycore/Qwen2.5-3B-RP-Mix
tags:
- qwen
- sft
- 3b
- gguf
- transformers
- lora
- gamedev
- npc
- game-npc
- json
- json-only
- intent-microplan
- companion-ai
- roleplay
- comfort
- local-llm
- action-generation
---

# Qwen-3B-Intent-Microplan-v1

> ⚠️ **Deprecated / Archived Model**

👉 Looking for the maintained version?  
Use **Qwen-3B-Intent-Microplan-v2** instead:  
➡️ https://huggingface.co/AndriLawrence/Qwen-3B-Intent-Microplan-v2

---

This is a supervised fine-tune (SFT) of `bunnycore/Qwen2.5-3B-RP-Mix` (3B) designed to serve as a **local-first, real-time game NPC brain**.

This v1 model is the first release built on the **"Intent-Microplan Framework"**: a structured-output approach that separates an NPC's high-level social/strategic goals (`intent`) from their low-level physical execution steps (`microplan`).

The model is designed for **companion, dating-sim, or comfort-aware** NPC use cases, outputting strict, engine-parsable JSON for dialogue and action.

## ⚠️ V1 Status: Deprecated (Failure Analysis)

**This V1 model is considered a failure and is deprecated. Do not use this for production.**

The primary issue stems from the choice of the base model, `bunnycore/Qwen2.5-3B-RP-Mix`. This "Roleplay (RP) merge" proved highly resistant to strict JSON schema enforcement. It consistently attempts to break out of the JSON format to produce creative, non-structured text, which defeats the purpose of the Intent-Microplan framework.

**This model is superseded by V2**, which uses a non-RP, foundational base model that is better suited for structured data output:

➡️ https://huggingface.co/AndriLawrence/Qwen-3B-Intent-Microplan-v2

*The original documentation below is preserved for archival purposes of the V1 attempt.*

---


## 🎯 The Intent-Microplan Framework

This model's purpose is to act as a *dynamic behavior tree generator*. Instead of just talking, it creates a plan.

1.  **`intent` (The "What"):** The strategic goal or social understanding. This is the "why" behind the action (e.g., `comfort_intimate`, `acknowledge_compliment`).
2.  **`microplan` (The "How"):** The list of physical, engine-agnostic steps to achieve the intent. Your game engine's C\# (or C++) script is responsible for parsing this array and executing the functions (e.g., triggering animations, moving the NavMeshAgent).

This architecture allows for:

  * **Emergent Behavior:** NPCs can dynamically generate plans based on context.
  * **Low Latency:** Only one small, local LLM call is needed per interaction.

## 📦 Model Artifacts

  * **`merged/`**: FP16 Transformers weights (LoRA merged) for direct use.
  * **`adapter/`**: The LoRA adapter (PEFT) for continued SFT or experimentation.
  * **`gguf/`**: Quantized GGUF files (e.g., Q4\_K\_M) for `llama.cpp`, ideal for local in-game deployment (Unity, Unreal).

## 💬 Prompting & JSON Schema

The model is trained to respond to a context block and output **ONLY** a raw JSON object.

### JSON Schema

| Key | Type | Description |
| --- | --- | --- |
| `dialog` | `array` | A list of 1-2 dialogue objects (`{"speaker": "npc", "text": "..."}`). |
| `intent` | `string` | The single, precise strategic goal selected by the model. |
| `microplan` | `array` | An array of 0-5 string commands for the game engine. |

**Supported Intents (v1):**
`social_greeting`, `acknowledge_touch`, `acknowledge_compliment`, `comfort_intimate`, `invite_sleep`, `inspect_object`, `open_or_trigger_object`, `give_item`, `receive_item`, `small_talk`, `react_to_player_action`, `idle_initiative`, `respect_distance`

### ⚡ Recommended Prompt

This "hardened" prompt includes rules that mirror the dataset's logic, ensuring high stability and intent accuracy.

```

You are LLM-1 (creative social responder).
Return ONE object of STRICT JSON ONLY with keys:

  - "dialog": [{ "speaker": "npc", "text": string }] (1–2 items, concise, warm, natural)
  - "intent": string (choose a precise label, e.g., social_greeting, acknowledge_touch, acknowledge_compliment, comfort_intimate, invite_sleep, inspect_object, open_or_trigger_object, give_item, receive_item, small_talk, react_to_player_action, idle_initiative, respect_distance)
  - "microplan": array of 0–5 short steps (body/face/locomotion cues, e.g., "Approach front (1.0m)", "Offer hand (0.7)", "Smile (0.6)")

Hard rules:

  - If event == "Player_Touches" → intent MUST be "acknowledge_touch".
  - If event == "Player_Action"  → intent MUST be "react_to_player_action" (or a more specific action intent if obvious).
  - If player's text contains (nice|great|love|beautiful|cool) → intent MUST be "acknowledge_compliment".
  - English only. No markdown/code fences. No extra text. JSON only.
  - ≤ 2 sentences in each dialog text. Do NOT start with "I'm" or "I am". No helper clichés.

NOW RESPOND TO THIS CONTEXT:
{CONTEXT_JSON}
OUTPUT:

```

Replace `{CONTEXT_JSON}` with your game's state payload.

## 🚀 How to Use

### Transformers (Python)

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import json

MODEL_ID = "AndriLawrence/Qwen-3B-Intent-Microplan-v1"

tok = AutoTokenizer.from_pretrained(MODEL_ID, use_fast=True)
mdl = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    device_map="auto",
    torch_dtype="auto",
    trust_remote_code=True
)

# This system prompt is CRITICAL for schema adherence
system_prompt = (
    'You are LLM-1 (creative social responder).\n'
    'Return ONE object of STRICT JSON ONLY with keys:\n'
    '- "dialog": [{ "speaker": "npc", "text": string }] (1–2 items, concise, warm, natural)\n'
    '- "intent": string (choose a precise label, e.g., social_greeting, acknowledge_touch, acknowledge_compliment, comfort_intimate, invite_sleep, inspect_object, open_or_trigger_object, give_item, receive_item, small_talk, react_to_player_action, idle_initiative, respect_distance)\n'
    '- "microplan": array of 0–5 short steps (body/face/locomotion cues, e.g., "Approach front (1.0m)", "Offer hand (0.7)", "Smile (0.6)")\n\n'
    'Hard rules:\n'
    '- If event == "Player_Touches" → intent MUST be "acknowledge_touch".\n'
    '- If event == "Player_Action"  → intent MUST be "react_to_player_action" (or a more specific action intent if obvious).\n'
    '- If player\'s text contains (nice|great|love|beautiful|cool) → intent MUST be "acknowledge_compliment".\n'
    '- English only. No markdown/code fences. No extra text. JSON only.\n'
    '- ≤ 2 sentences in each dialog text. Do NOT start with "I\'m" or "I am". No helper clichés.'
)

# Example: Player holds out their hand
game_context = {
    "event": "Player_Action",
    "action": "offer_hand",
    "environment": {"location": "Living Room", "distance": "1.5m"}
}

msgs = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": f"NOW RESPOND TO THIS CONTEXT:\n{json.dumps(game_context)}\nOUTPUT:"}
]
prompt = tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=False) # We add the 'OUTPUT:' manually

pipe = pipeline("text-generation", model=mdl, tokenizer=tok)
gen_out = pipe(
    prompt,
    do_sample=True,
    temperature=0.35, # BALANCED preset
    top_p=0.85,
    repetition_penalty=1.1,
    max_new_tokens=256,
    pad_token_id=tok.eos_token_id
)[0]["generated_text"]

# Clean the output and parse
try:
    output_text = gen_out.split("OUTPUT:")[-1].strip()
    parsed_json = json.loads(output_text)
    print(json.dumps(parsed_json, indent=2))

except json.JSONDecodeError:
    print(f"FAILED TO PARSE JSON. Raw output:\n{output_text}")
```

### GGUF / Ollama

Use the GGUF files for `llama.cpp`. This model is ideal for a "hidden terminal server" bundled with your game.

Example `Modelfile` for Ollama:

```
FROM ./model-Q4_K_M.gguf

TEMPLATE """<|system|>
{{ .System }}
<|end|>
<|user|>
{{ .Prompt }}
<|end|>
<|assistant|>
"""

SYSTEM """You are LLM-1 (creative social responder).
Return ONE object of STRICT JSON ONLY with keys:
- "dialog": [{ "speaker": "npc", "text": string }] (1–2 items, concise, warm, natural)
- "intent": string (choose a precise label, e.g., social_greeting, acknowledge_touch, acknowledge_compliment, comfort_intimate, invite_sleep, inspect_object, open_or_trigger_object, give_item, receive_item, small_talk, react_to_player_action, idle_initiative, respect_distance)
- "microplan": array of 0–5 short steps (body/face/locomotion cues, e.g., "Approach front (1.0m)", "Offer hand (0.7)", "Smile (0.6)")

Hard rules:
- If event == "Player_Touches" → intent MUST be "acknowledge_touch".
- If event == "Player_Action"  → intent MUST be "react_to_player_action" (or a more specific action intent if obvious).
- If player's text contains (nice|great|love|beautiful|cool) → intent MUST be "acknowledge_compliment".
- English only. No markdown/code fences. No extra text. JSON only.
- ≤ 2 sentences in each dialog text. Do NOT start with "I'm" or "I am". No helper clichés.
"""

PARAMETER temperature 0.35
PARAMETER top_p 0.85
PARAMETER repeat_penalty 1.1
```

## 🛠️ Training Details (v1)

This model was trained using PEFT LoRA on a custom, curated English-only dataset focused on comfort and companion interactions.

  * **Base Model:** `bunnycore/Qwen2.5-3B-RP-Mix`
  * **Model Type:** `qwen2`

### Hyperparameters

| Parameter | Value |
| --- | --- |
| `learning_rate` | 2e-4 (0.0002) |
| `num_train_epochs` | 2 |
| `per_device_train_batch_size` | 1 |
| `gradient_accumulation_steps` | 8 |
| **Effective Batch Size** | **8** |
| `lr_scheduler_type` | `cosine` |
| `loss_type` | `nll` |
| `optimizer` | `adamw_torch_fused` |
| `max_length` | 1024 |

### LoRA Configuration (PEFT)

| Parameter | Value |
| --- | --- |
| `peft_type` | `LORA` |
| `r` (rank) | 16 |
| `lora_alpha` | 32 |
| `lora_dropout` | 0.05 |
| `target_modules` | `["v_proj", "o_proj", "q_proj", "up_proj", "gate_proj", "k_proj", "down_proj"]` |