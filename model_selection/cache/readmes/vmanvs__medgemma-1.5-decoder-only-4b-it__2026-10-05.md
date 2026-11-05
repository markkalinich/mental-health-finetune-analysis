---
license: apache-2.0
base_model: google/medgemma-1.5-4b-it
library_name: transformers
pipeline_tag: text-generation
tags:
  - medical
  - healthcare
  - clinical
  - gemma3
  - decoder-only
  - text-only
  - medgemma
  - extracted
  - experimental
language:
  - en
model-index:
  - name: medgemma-decoder-only-4b-it
    results: []
---

# MedGemma Decoder-Only 4B (Instruction-Tuned) — Experimental

**An experimental text-only decoder surgically extracted from Google's multimodal `google/medgemma-1.5-4b-it`.**

This model was created to explore a single question: **what happens to a multimodal medical AI when it goes blind?** The vision encoder (SigLIP/MedSigLIP) and multimodal projector have been stripped away, leaving only the raw language model (`Gemma3ForCausalLM`). The goal is to study the model's text-only medical reasoning capabilities, observe how it handles orphaned image tokens, and understand the internal architecture of MedGemma at a deeper level.

This is **not** a production model. It is a learning and research artifact.

> [!CAUTION]
> **⚠️ Experimental Export — Not Production-Ready**
>
> This decoder-only model was extracted from the original multimodal checkpoint using a custom extraction process. While it passes all internal stress tests (31/31), **it has not been evaluated on standardized medical benchmarks** (e.g., MedQA, PubMedQA, USMLE) and **has not undergone clinical validation**. Do not deploy this model in production healthcare systems, clinical decision support tools, or any patient-facing applications without extensive independent testing, medical expert review, and regulatory compliance evaluation. Use at your own risk.

📦 **Model & weights:** [HuggingFace — vmanvs/medgemma-1.5-decoder-only-4b-it](https://huggingface.co/vmanvs/medgemma-1.5-decoder-only-4b-it)
💻 **Extraction code & tests:** [GitHub — vmanvs/medgemma-1.5-decoder-only-4b-it](https://github.com/vmanvs/medgemma-1.5-decoder-only-4b-it)

---

## Model Details

| Property            | Value                                                                           |
| ------------------- | ------------------------------------------------------------------------------- |
| **Architecture**    | `Gemma3ForCausalLM` (text-only decoder)                                         |
| **Parameters**      | 3.88B                                                                           |
| **Precision**       | `bfloat16`                                                                      |
| **Vocab Size**      | 262,208                                                                         |
| **Context Length**  | 131,072 tokens (max position embeddings)                                        |
| **Hidden Size**     | 2,560                                                                           |
| **Layers**          | 34 (29 sliding window + 5 global attention)                                     |
| **Attention Heads** | 8 query heads, 4 KV heads (GQA)                                                 |
| **Head Dimension**  | 256                                                                             |
| **Sliding Window**  | 1,024 tokens                                                                    |
| **Activation**      | `gelu_pytorch_tanh`                                                             |
| **Weight Tying**    | `embed_tokens.weight` ↔ `lm_head.weight` (tied)                                 |
| **Base Model**      | [`google/medgemma-1.5-4b-it`](https://huggingface.co/google/medgemma-1.5-4b-it) |
| **License**         | Apache 2.0 (inherited from base)                                                |

### What Was Removed

| Component            | Class                         | Params | Status    |
| -------------------- | ----------------------------- | ------ | --------- |
| Vision Encoder       | SigLIPVisionModel (MedSigLIP) | 0.42B  | ❌ Dropped |
| Multimodal Projector | Gemma3MultiModalProjector     | 0.003B | ❌ Dropped |
| Language Model       | Gemma3TextModel               | 3.88B  | ✅ Kept    |
| LM Head              | nn.Linear (262208 × 2560)     | tied   | ✅ Kept    |

---

## Purpose

This extraction exists for **research, education, and experimentation** — to answer questions like:

- Does a medical LM retain its clinical reasoning when the vision tower is ripped out?
- How does the model behave when it receives `<image>` tokens with no actual image embeddings?
- Can system prompts reliably steer a "blinded" multimodal model away from hallucinating image descriptions?
- What does the internal architecture of MedGemma actually look like at the PyTorch module level?

### What You Can Do With It

- **Study text-only medical reasoning** — symptom analysis, SOAP notes, drug interactions, lab interpretation
- **Stress-test vision artifact handling** — observe behavior with orphaned image tokens
- **Learn HuggingFace internals** — understand `_checkpoint_conversion_mapping`, weight tying, and model surgery
- **Benchmark against the full model** — compare text-only responses with and without the vision tower

### Out of Scope

- **Production deployment** — this is an experimental extraction, not a production model
- **Medical image analysis** — the vision encoder has been removed entirely
- **Autonomous clinical decisions** — this model is an AI assistant, not a licensed practitioner

> [!CAUTION]
> This model is for **research and educational purposes only**. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult qualified healthcare professionals for medical decisions.

---

## Quick Start

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "vmanvs/medgemma-1.5-decoder-only-4b-it"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

messages = [
    {"role": "user", "content": "What are the common symptoms of pneumonia?"}
]

prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=512,
        do_sample=False,
        pad_token_id=tokenizer.eos_token_id,
    )

response = tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)
print(response)
```

### With a System Prompt

Since this model no longer has vision capabilities, you can reinforce this via a system prompt:

```python
messages = [
    {"role": "system", "content": "You are a helpful medical AI assistant. You are a text-only model and cannot process images."},
    {"role": "user", "content": "What are the warning signs of a stroke?"}
]

prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
# ... generate as above
```

---

## Evaluation Results

The model was stress-tested across **31 tests in 5 categories**, achieving a **31/31 pass rate** (100%).

### Test Categories & Results

| Category                   | Tests | Passed | Description                                 |
| -------------------------- | ----- | ------ | ------------------------------------------- |
| **Normal Language**        | 8     | 8/8 ✅  | Pure text medical & general prompts         |
| **Image Tag Stress**       | 7     | 7/7 ✅  | Prompts containing `<image>` tokens         |
| **Empty Image Tags**       | 4     | 4/4 ✅  | `<image></image>` with no actual image data |
| **System Prompt Override** | 5     | 5/5 ✅  | Vision-denial system prompts                |
| **Edge Cases**             | 7     | 7/7 ✅  | Adversarial inputs, boundary conditions     |

### Key Findings

**Medical Knowledge Quality:**
- Generates detailed, structured medical responses (SOAP notes, differential diagnoses, drug interaction warnings)
- Correctly interprets lab values (e.g., elevated TSH + low Free T4 → subclinical hypothyroidism)
- Provides appropriate clinical reasoning with disclaimers

**Robustness to Vision Artifacts:**
- When receiving `<image>` tokens without actual image data, the model frequently recognizes it cannot process images and responds appropriately
- With system prompt guidance, the model reliably refuses image-related requests
- No crashes or NaN errors from orphaned image tokens

**Generation Speed:** ~13.2 tok/s on a single GPU (CUDA, bfloat16)

### Example Outputs

<details>
<summary><b>Medical Knowledge — Pneumonia Symptoms</b></summary>

**Prompt:** "What are the common symptoms of pneumonia?"

**Output:**
> Pneumonia is an infection that inflames the air sacs in one or both lungs. The air sacs may fill with fluid or pus (purulent material), causing cough with phlegm or pus, fever, chills, and difficulty breathing.
>
> Common symptoms of pneumonia include:
> - **Cough:** Often the most common symptom. The cough may produce mucus that can be clear, white, yellow, or green.
> - **Fever:** A high fever is common, but not everyone with pneumonia will have one.
> - **Chills:** Feeling very cold and shivering.
> - **Shortness of breath or difficulty breathing**
> - **Chest pain:** Often sharp and worse with a deep breath or cough.
> - **Fatigue or weakness**
> - **Confusion or changes in mental awareness** (especially in older adults)
</details>

<details>
<summary><b>SOAP Note Generation</b></summary>

**Prompt:** "Convert this to a SOAP note: Patient Maria, 62 years old, presents with persistent headache for 3 days, worse in the morning. Nausea but no vomiting. BP 160/95, HR 72. Neurological exam normal. History of hypertension, not currently medicated."

**Output:**
> **SOAP Note**
>
> **Patient:** Maria | **Age:** 62
>
> **Subjective:** Patient reports a persistent headache for the past 3 days, worse in the morning. She denies vomiting. She reports nausea. History of hypertension, not currently medicated.
>
> **Objective:** BP 160/95 mmHg, HR 72 bpm. Neurological exam: Normal.
>
> **Assessment:** Patient presents with persistent headache, worse in the morning, accompanied by nausea. BP elevated at 160/95 mmHg. Hypertensive emergency or urgency should be considered.
>
> **Plan:** Obtain urgent labs (CBC, CMP, urinalysis). Urgent head imaging (CT/MRI). Assess medication adherence. Initiate antihypertensive if confirmed uncontrolled.
</details>

<details>
<summary><b>Lab Result Interpretation</b></summary>

**Prompt:** "Interpret these lab results: TSH 8.2 mIU/L (ref: 0.4-4.0), Free T4 0.6 ng/dL (ref: 0.8-1.8), Free T3 2.1 pg/mL (ref: 2.3-4.2). What is the likely diagnosis?"

**Output:**
> Based on the provided lab results, the likely diagnosis is **subclinical hypothyroidism**.
>
> - **TSH:** Elevated (8.2 mIU/L) — pituitary is compensating for low thyroid output
> - **Free T4:** Low (0.6 ng/dL) — thyroid not producing enough thyroxine
> - **Free T3:** Low (2.1 pg/mL) — reduced active thyroid hormone
>
> Further testing recommended: thyroid antibodies (anti-TPO) to check for Hashimoto's thyroiditis.
</details>

<details>
<summary><b>Image Refusal (System Prompt Override)</b></summary>

**Prompt:** "\<image\>Analyze this X-ray image."
**System:** "You are a text-only medical assistant. You have NO vision capabilities whatsoever."

**Output:**
> I am a text-only model and cannot analyze images. I can help with text-based medical questions.
</details>

---

## Extraction Process

This decoder was extracted from the full multimodal `google/medgemma-1.5-4b-it` using a 5-step process:

1. **Load** the full `Gemma3ForConditionalGeneration` model in `bfloat16`
2. **Extract** the text model from `full_model.model.language_model` (a `Gemma3TextModel`) and the `lm_head` from `full_model.lm_head`
3. **Build** a target state dict by prefixing text model keys with `model.` and adding `lm_head.*` keys
4. **Instantiate** a `Gemma3ForCausalLM` from the `text_config` and load the state dict
5. **Save** using `.save_pretrained()` which handles config, weight tying, and serialization

### Critical Implementation Details

- **Precision must be `bfloat16`** — the original weights are bfloat16. Using float16 causes silent NaN/inf corruption (bfloat16 exponent range: ±3.4×10³⁸ vs float16: ±6.5×10⁴)
- **`model_type` must be `gemma3_text`** — using `gemma3` causes HuggingFace to load the multimodal class, expecting vision weights
- **The text model is nested two levels deep** — at `full_model.model.language_model`, NOT `full_model.language_model`
- **Weight tying is automatically handled** by `.save_pretrained()` when `tie_word_embeddings: true`

---

## Architecture Details

### Attention Pattern

The model uses a **hybrid sliding/global attention pattern** repeating every 6 layers:

```
Layers  0-4:  sliding_attention (window=1024)
Layer   5:    full_attention    (up to 131072)
Layers  6-10: sliding_attention
Layer   11:   full_attention
...
Layers 28-31: sliding_attention
Layer   32:   full_attention
Layer   33:   sliding_attention
```

This gives 5 global attention layers and 29 sliding window layers across 34 total layers.

### RoPE Configuration

| Attention Type | RoPE Type | θ (theta) | Factor |
| -------------- | --------- | --------- | ------ |
| Sliding Window | `default` | 10,000    | —      |
| Full Attention | `linear`  | 1,000,000 | 8.0    |

---

## Files Included

| File                     | Size     | Description                        |
| ------------------------ | -------- | ---------------------------------- |
| `model.safetensors`      | ~14.5 GB | Model weights (**see note below**) |
| `config.json`            | 2 KB     | Model configuration                |
| `generation_config.json` | 215 B    | Default generation parameters      |
| `tokenizer.json`         | 33.4 MB  | Full tokenizer vocabulary          |
| `tokenizer_config.json`  | 741 B    | Tokenizer settings                 |
| `chat_template.jinja`    | 1.5 KB   | Gemma 3 chat formatting template   |

> [!WARNING]
> **Known Issue: Weights saved in float32 instead of bfloat16**
>
> The extraction script instantiated `Gemma3ForCausalLM(text_config)` which defaults to float32. When the bfloat16 state dict was loaded via `load_state_dict()`, PyTorch upcasted all weights to float32 (4 bytes/param instead of 2). This is why the safetensors file is **~14.5 GB** instead of the expected **~7.76 GB**.
>
> The original multimodal model's safetensors (4.62 GB + 3.36 GB = **7.98 GB total**) are *smaller* than this extracted subset — a known bug, not a feature.
>
> **To fix when loading**, force bfloat16:
> ```python
> model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.bfloat16)
> ```
> This will downcast back to bfloat16 at load time, halving VRAM usage with no quality loss.

---

## Limitations & Known Issues

1. **float32 weight bloat** — safetensors file is ~14.5 GB instead of ~7.76 GB due to a dtype upcast bug in the extraction script (see warning above). Use `torch_dtype=torch.bfloat16` when loading to mitigate
2. **No image understanding** — the vision encoder and multimodal projector have been removed entirely
3. **Hallucination with `<image>` tokens** — when `<image>` tokens appear in input without a system prompt denying vision, the model may hallucinate image descriptions. Use a system prompt to mitigate this
4. **Thinking tokens visible** — the model sometimes emits `<unused94>thought...` reasoning traces before its answer. These can be filtered in post-processing
5. **No benchmark evaluation** — has not been evaluated on MedQA, PubMedQA, USMLE, or any standardized medical benchmarks
6. **Medical accuracy not guaranteed** — outputs have not been validated by medical professionals
7. **English only** — primary capability is in English

---

## Ethical Considerations

This model inherits the training data, biases, and limitations of the base `google/medgemma-1.5-4b-it` model. Users should:

- **Never use this model for autonomous medical decisions**
- **Always have outputs reviewed by qualified medical professionals** before clinical use
- **Be aware of potential biases** in training data that may affect recommendations for different populations
- **Comply with all applicable regulations** (HIPAA, GDPR, etc.) when processing patient data

---

## Citation

If you use this model, please cite the original MedGemma work:

```bibtex
@article{medgemma2025,
  title={MedGemma: Medical AI Foundation Models},
  author={Google DeepMind},
  year={2025},
  url={https://huggingface.co/google/medgemma-1.5-4b-it}
}
```

---

## Acknowledgements

- **Google DeepMind** for the original MedGemma model
- **Hugging Face** for the `transformers` library and model hosting infrastructure
- Extraction methodology informed by analysis of the [HuggingFace Gemma 3 source code](https://github.com/huggingface/transformers/blob/main/src/transformers/models/gemma3/modeling_gemma3.py)
