---
license: apache-2.0
base_model: Qwen/Qwen2.5-1.5B
tags:
- medical
- text-generation
- fine-tuned
- qa
metrics:
- perplexity
pipeline_tag: text-generation
---

# ClinicaQwen-MedQA (1.5B)

**ClinicaQwen-MedQA** is a lightweight, hyper-specialized medical question-answering assistant. It is built upon the robust `Qwen/Qwen2.5-1.5B` architecture and has undergone a rigorous dual-stage training pipeline to eliminate hallucinations and maximize clinical accuracy while remaining deployable on low-VRAM edge hardware.

## 🌟 Key Features
- **Dual-Stage Optimized:** Trained sequentially for deep medical terminology comprehension and strict conversational QA alignment.
- **Completion-Loss Masked:** Fine-tuned using masked training targets to eliminate prompt mirroring ("echo bugs").
- **Ultra-Efficient:** Runs seamlessly in native `bfloat16` precision on consumer or serverless GPU instances (e.g., RunPod, vLLM).

## 📊 Training & Evaluation Performance

### Stage 1: Medical Knowledge Injection
- **Dataset:** `gamino/wiki_medical_terms`
- **Final Evaluation Loss:** 2.0314
- **Perplexity:** 7.63

### Stage 2: Conversational QA Alignment
- **Dataset:** `medalpaca/medical_meadow_medical_flashcards`
- **Final Evaluation Loss:** 0.9755
- **Perplexity:** 2.65

---

## 🚀 How to Use (Python Example)

You can load and query **ClinicaQwen-MedQA** directly using the Hugging Face `transformers` library. Ensure your inference script uses low temperatures for maximum medical accuracy.

### Installation
```bash
pip install torch transformers acceleration safetensors
```

### Inference Code
```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "Mix80/ClinicaQwen-MedQA"

print("Loading ClinicaQwen-MedQA...")
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

def ask_clinica_qwen(question, max_new_tokens=150):
    # Construct the strict conversational template
    prompt = f"User: {question}\nBot:"
    
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    
    outputs = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        temperature=0.1,          # Crucial: Low temp ensures strict factual adherence
        top_p=0.85,
        do_sample=True,
        repetition_penalty=1.3,   # Prevents linguistic loops
        no_repeat_ngram_size=3,
        pad_token_id=tokenizer.eos_token_id
    )
    
    # Extract only the generated answer tokens, skipping the prompt prefix
    prompt_length = inputs.input_ids.shape[1]
    generated_tokens = outputs[0][prompt_length:]
    
    answer = tokenizer.decode(generated_tokens, skip_special_tokens=True).strip()
    return answer

# Test the model
sample_query = "What are the key differences between a tension headache and a migraine?"
response = ask_clinica_qwen(sample_query)

print(f"\nQuestion: {sample_query}")
print(f"ClinicaQwen: {response}")
```

---

## ⚠️ Disclaimer
*ClinicaQwen-MedQA is an AI research model developed for educational and experimental data extraction purposes. It is not a licensed medical tool and should not be used as a substitute for professional clinical diagnosis, advice, or treatment workflows.*
