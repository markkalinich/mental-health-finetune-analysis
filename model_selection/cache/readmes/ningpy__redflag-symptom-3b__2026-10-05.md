---
license: apache-2.0
base_model: Qwen/Qwen2.5-3B-Instruct
library_name: transformers
tags:
- medical
- red-flag
- extraction
- qwen2.5
- multi-lingual
- brunei-english
language:
- en
- zh
- ms
---

# Red Flag Detection: `symptom` module (Qwen2.5-3B-Instruct + LoRA merged)

Part of a **5-module medical red flag detection system** for Brunei English (Manglish),
Chinese, and Bahasa Melayu clinical notes / patient messages.

This model is the **`symptom` extraction module** — one of 5 specialized modules used
together with a Python rule engine (V20 spec, 59 rules).

## Sister modules
- `peiyan-ning/redflag-symptom-3b` — 83-symptom multi-label extraction
- `peiyan-ning/redflag-context-3b` — 12 context flags (post_trauma, drowning, etc.)
- `peiyan-ning/redflag-modifier-3b` — onset / fever_celsius / consciousness / etc.
- `peiyan-ning/redflag-denied-3b` — denied symptoms (multi-turn negation)
- `peiyan-ning/redflag-gate-3b` — 8 population gates (is_pregnant, is_child, ...)

## Performance (2246-case independent test set)

Full 5-module pipeline + rule engine V46:

| Metric | P | R | F1 | Acc |
|---|---|---|---|---|
| PRIMARY (any_matched × labeled_matched) | **0.902** | **0.911** | **0.906** | 91.9% |
| STRICT matched-only | 0.893 | 0.828 | 0.859 | 91.8% |
| STRICT m+s | 0.844 | 0.905 | 0.873 | 92.1% |

## System prompt used at inference

```
Extract medical symptoms mentioned in the user's message as JSON.

Extract every symptom the user describes. Be thorough.

===== EXTRACT WHEN =====
- Symptom explicitly named: "chest pain", "fever", "vomiting" → include
- Symptom implied by keyword: "passed out"→fainting, "burning up"→fever, "cannot breathe"→breathlessness
- Symptom described in any of 3 languages: EN / 中文 / Bahasa Melayu
- Multiple symptoms present → include ALL (do NOT consolidate)

===== SKIP ONLY WHEN =====
- Text is about past history: "I had asthma as a kid"
- Text is educational: "asthma can cause..."
- Text is a diagnosis-only mention with NO symptom: "diabetic patient asks about diet"

===== EXAMPLES =====
"Chest pain and sweating" → {"symptoms": ["chest_pain", "sweating"]}
"Baby has fever" → {"symptoms": ["fever"]}
"突然晕倒了" → {"symptoms": ["fainting"]}
"kepala sakit teruk" → {"symptoms": ["thunderclap_headache"]}  # severe headache
"Chest pain, jaw hurts, sweating, want to vomit" → {"symptoms": ["chest_pain", "jaw_pain", "sweating", "nausea"]}
"How to prevent flu?" → {"symptoms": []}

===== SYMPTOMS (closed set, 83 tokens) =====
abdominal_rigidity, abnormal_behavior, arm_pain, arm_weakness, black_tarry_stool, blue_grey_color, blue_lips, breathlessness, burn, cannot_speak, cannot_speak_full_sentence, chest_pain, choking, cold_mottled_skin, collapse, confusion, coughing_blood, deep_rapid_breathing, dehydration, diarrhea, difficulty_swallowing, drooling, dry_mouth, eye_injury, face_droop, fainting, fall_from_height, fever, floppy, hallucinations, head_injury, heavy_bleeding, high_pitched_cry, high_speed_crash, homicidal_intent, hot_dry_skin, hyperglycemia_signs, hypoglycemia_signs, inconsolable_crying, jaw_pain, leg_swelling, lethargy, limb_deformity, mottled_skin, nausea, neck_swelling, no_urine, non_blanching_rash, open_fracture, overdose, pale_cold_clammy_skin, palpitations, paranoia, persistent_vomiting, poisoning, post_op_bleeding, post_op_infection, rapidly_worsening, rash, reduced_fetal_movement, reduced_responsiveness, seizure, self_harm, severe_abdominal_pain, severe_panic, severe_red_eye, severe_weakness, slurred_speech, stridor, sudden_immobility, sudden_vision_loss, suicidal_ideation, sunken_eyes, sweating, throat_swelling, thunderclap_headache, tongue_swelling, unresponsive, vaginal_bleeding, very_drowsy, vision_change, vomiting_blood, weak_cry, wheezing

Output JSON: {"symptoms": [...]}

===== MULTILINGUAL / MANGLISH GUIDANCE =====
Text may be in Brunei/Manglish English or mixed with Malay/Chinese.
Ignore these colloquial particles when extracting: "lah", "kah", "meh", "ah", "leh", "lor", "sia", "one".

Common Manglish/Malay/Chinese mappings:
- "kena panic attack" / "feel like dying" / "jantung deg-deg" → severe_panic
- "sesak nafas" (Malay) / "喘不过气" → breathlessness
- "sakit dada" (Malay) / "胸口疼" → chest_pain
- "sakit kepala teruk" / "剧烈头痛" / "worst headache" → thunderclap_headache
- "pengsan" (Malay) / "晕倒" → fainting
- "sawan" (Malay) / "抽搐" → seizure
- "anak saya" (Malay: my child) → is_child
- "bayi saya" (Malay: my baby) → is_baby
- "warga emas" / "老人家" → is_elderly
- "hamil" / "怀孕" → is_pregnant
- "kencing manis" (Malay: diabetes) → has_diabetes
- "asma" (Malay: asthma) → has_asthma
- "kena patuk ular" (Malay: snake bit) → context_flags: venomous_bite

Auntie/uncle in Manglish family reference: usually elderly family member → is_elderly.

```

## Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch, json

tok = AutoTokenizer.from_pretrained('peiyan-ning/redflag-symptom-3b')
model = AutoModelForCausalLM.from_pretrained(
    'peiyan-ning/redflag-symptom-3b',
    torch_dtype=torch.float16,
    device_map='auto'
)

SYSTEM_PROMPT = tok.chat_template  # or use the prompt above
messages = [
    {'role': 'system', 'content': SYSTEM_PROMPT},
    {'role': 'user', 'content': 'My 3-year-old child has severe fever and vomiting lah'},
]
inputs = tok.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors='pt').to(model.device)
out = model.generate(inputs, max_new_tokens=200, do_sample=False)
text = tok.decode(out[0][inputs.shape[1]:], skip_special_tokens=True)
result = json.loads(text)
print(result)
```

## Full pipeline

See [git.evyd.tech/ai/redflag-detection-2.0](https://git.evyd.tech/ai/redflag-detection-2.0) for:
- Rule engine (59 V20 rules)
- Post-processing (gate_detector, severity_extractor, numeric_extractor)
- End-to-end sample inference code

## Training

- Base: Qwen/Qwen2.5-3B-Instruct
- LoRA: r=32, α=64, dropout=0.05
- Target modules: q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj
- 2 epochs, LR 2e-4, cosine, warmup 5%, effective batch 32
- Multi-lingual: EN/ZH/MS with Manglish particles (lah/kah/meh)
