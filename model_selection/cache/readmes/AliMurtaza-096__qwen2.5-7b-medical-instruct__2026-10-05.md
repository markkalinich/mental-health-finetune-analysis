# Qwen 2.5 7B Medical Front Desk Assistant

Fine-tuned version of Qwen2.5-7B-Instruct for medical front desk conversations, trained on 130 examples of clinic administrative tasks.

## Model Details

- **Base Model**: unsloth/Qwen2.5-7B-Instruct-bnb-4bit
- **Training Framework**: Unsloth + LoRA
- **Training Steps**: 80
- **Final Loss**: 1.047
- **Training Data**: 130 medical front desk conversations
- **Use Case**: Medical clinic front desk assistant (scheduling, insurance, general clinic information)
- **LoRA Rank**: 16
- **Target Modules**: q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj

## Training Data

The model was fine-tuned on 130 conversations covering:
- Appointment scheduling and rescheduling
- Insurance verification
- Office hours and location information
- COVID-19 policies
- General clinic information
- Patient intake procedures

## Usage

### SafeTensors Format (Transformers)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("AliMurtaza-096/qwen2.5-7b-medical-instruct")
tokenizer = AutoTokenizer.from_pretrained("AliMurtaza-096/qwen2.5-7b-medical-instruct")

messages = [
    {"role": "system", "content": "You are a friendly, professional front-desk assistant for Northview Medical Associates."},
    {"role": "user", "content": "I need to reschedule my appointment."}
]

inputs = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt")
outputs = model.generate(inputs, max_new_tokens=128)
print(tokenizer.decode(outputs[0]))
```

### GGUF Format (Ollama)

Download the `qwen2.5-7b-medical-q4_k_m.gguf` file (4.4GB) and create a Modelfile:

```
FROM ./qwen2.5-7b-medical-q4_k_m.gguf

TEMPLATE """<|im_start|>system
{{ .System }}<|im_end|>
<|im_start|>user
{{ .Prompt }}<|im_end|>
<|im_start|>assistant
"""

PARAMETER stop "<|im_start|>"
PARAMETER stop "<|im_end|>"

SYSTEM """You are a friendly, professional front-desk assistant for a medical clinic. You handle scheduling, insurance, and general clinic information. You NEVER diagnose or give medical treatment advice."""
```

Then:

```bash
ollama create qwen2.5-medical -f Modelfile
ollama run qwen2.5-medical "What are your office hours?"
```

## Example Responses

**User:** "Can I come in for a checkup on Saturday?"

**Assistant:** "Our office is open Monday through Friday from eight AM to five PM. We're closed on weekends and major holidays. Can I help you set up an appointment for next week?"

**User:** "I have an injection scheduled for tomorrow morning but I just tested positive for Covid. What should I do?"

**Assistant:** "I'm sorry to hear that. We need all patients to be negative on the day of their procedure. Please call us right away and we'll cancel your appointment and reschedule once you're well. In the meantime, please stay home and follow CDC guidelines."

## Limitations

- **Does NOT provide medical advice or diagnoses** - This model is trained exclusively for administrative front desk tasks
- **Trained specifically for front desk administrative tasks** - May not generalize well to other medical contexts
- **Small training dataset** - 130 examples may not cover all edge cases in real-world scenarios
- **Requires proper system prompt** - Best results when used with the specified system prompt

## Model Files

- **SafeTensors** (15GB): Full precision model sharded across 4 files
  - `model-00001-of-00004.safetensors`
  - `model-00002-of-00004.safetensors`
  - `model-00003-of-00004.safetensors`
  - `model-00004-of-00004.safetensors`
- **GGUF Q4_K_M** (4.4GB): Quantized model for efficient inference with Ollama/llama.cpp
  - `qwen2.5-7b-medical-q4_k_m.gguf`

## Training Details

- **Optimizer**: AdamW 8-bit
- **Learning Rate**: 2e-4
- **Scheduler**: Linear
- **Batch Size**: 2 per device
- **Gradient Accumulation**: 4 steps
- **Effective Batch Size**: 8
- **Warmup Steps**: 5
- **Weight Decay**: 0.01
- **Max Sequence Length**: 4096
- **Precision**: BF16 (on GPU with BF16 support)

## Hardware

- **GPU**: NVIDIA GeForce RTX 4090 (24GB VRAM)
- **Training Time**: ~90 seconds for 80 steps

## License

This model inherits the license from the base [Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) model.

## Acknowledgments

- Fine-tuned using [Unsloth](https://github.com/unslothai/unsloth) for efficient training
- Base model: [Qwen/Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct)
- Quantized to GGUF using [llama.cpp](https://github.com/ggerganov/llama.cpp)

## Citation

If you use this model, please cite:

```bibtex
@misc{qwen2.5-7b-medical-instruct,
  author = {Ali Murtaza},
  title = {Qwen 2.5 7B Medical Front Desk Assistant},
  year = {2025},
  publisher = {HuggingFace},
  howpublished = {\\url{https://huggingface.co/AliMurtaza-096/qwen2.5-7b-medical-instruct}},
}
```

---

**⚠️ Medical Disclaimer**: This AI model is designed for administrative front desk tasks only and should NOT be used for medical diagnosis, treatment recommendations, or clinical decision-making. Always consult qualified healthcare professionals for medical advice.