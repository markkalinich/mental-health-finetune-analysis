---
license: apache-2.0
base_model: unsloth/Ministral-3-8B-Reasoning-2512
tags:
- medical
- healthcare
- reasoning
- fine-tuned
- ministral
- unsloth
- patient-education
language:
- en
pipeline_tag: text-generation
datasets:
- Malikeh1375/medical-question-answering-datasets
- ruslanmv/ai-medical-chatbot
- FreedomIntelligence/medical-o1-reasoning-SFT
library_name: transformers
---

<p align="center">
  <img src="./cover.jpg" width="850">
</p>

# Medical Ministral 8B

A medical reasoning model fine-tuned on Ministral-3-8B-Reasoning-2512 for clinical question answering and diagnostic reasoning.

## Model Description

This model is a specialized medical AI assistant trained in two phases:
- **Phase 1:** Medical knowledge foundation (Q&A, clinical conversations)
- **Phase 2:** Clinical reasoning and diagnostic thinking

The model demonstrates strong reasoning capabilities for medical scenarios, particularly in differential diagnosis and clinical decision-making.

## Training Details

- **Base Model:** unsloth/Ministral-3-8B-Reasoning-2512
- **Training Method:** LoRA fine-tuning (2-phase curriculum)
- **Context Length:** 2048 tokens
- **Training Hardware:** NVIDIA L40S GPU
- **Framework:** Unsloth + Hugging Face Transformers

## Evaluation

The model was evaluated on the **MMLU-Pro** benchmark in the **Biology** and **Health** domains to assess medical and biomedical reasoning capabilities.

- Due to hardware constraints, evaluations were conducted using both full-precision inference and 4-bit quantized inference. Partial dataset evaluation was performed.


### Full Precision Inference

| Domain   | Samples Evaluated | Accuracy |
|---------|-------------------|----------|
| Biology & Health  | 270               | 68.9%    |

### 4-Bit Quantized Inference

| Domain   | Samples Evaluated | Accuracy |
|---------|-------------------|----------|
| Biology | 390               | 68.7%    |
| Health  | 390               | 56.1%    |

## Usage

### Installation

```bash
pip install transformers==5.0.0rc0
pip install mistral-common --upgrade

```

### Basic Usage

```python
import torch
from transformers import Mistral3ForConditionalGeneration, MistralCommonBackend

model_id = "naazimsnh02/medical-ministral-8b"

tokenizer = MistralCommonBackend.from_pretrained(model_id)
model = Mistral3ForConditionalGeneration.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto",
)

def chat(prompt: str) -> str:
    messages = [{"role": "user", "content": prompt}]

    tokenized = tokenizer.apply_chat_template(
        messages,
        return_tensors="pt",
        return_dict=True
    )

    device = model.device
    for key, val in tokenized.items():
        if torch.is_tensor(val):
            tokenized[key] = val.to(device)

    input_length = tokenized["input_ids"].shape[1]

    output = model.generate(
        **tokenized,
        max_new_tokens=4096,
        temperature=0.7,
        do_sample=True,
        top_p=0.9,
    )[0]

    generated_tokens = output[input_length:]
    decoded = tokenizer.decode(
        generated_tokens,
        skip_special_tokens=True
    )

    return decoded.strip()


# Example
print(chat("Given the symptoms of sudden weakness in the left arm and leg, recent long-distance travel, and the presence of swollen and tender right lower leg, what specific cardiac abnormality is most likely to be found upon further evaluation that could explain these findings?"))
```

### Primary Use Cases

✅ **Patient Education**: Explaining medical conditions in accessible language  
✅ **Clinical Decision Support**: Providing reasoning for differential diagnoses  
✅ **Medical Content Generation**: Creating educational materials and summaries  
✅ **Healthcare Chatbots**: Powering conversational medical assistance  
✅ **Medical Training**: Supporting medical students with explanations  

### Out-of-Scope Use

❌ **Not a replacement for professional medical advice**  
❌ **Not for emergency medical situations**  
❌ **Not validated for direct clinical decision-making**  
❌ **Not trained on patient-specific health records**  

> **⚠️ Important**: This model is designed for educational and informational purposes. Always consult qualified healthcare professionals for medical decisions.

## Citation

If you use this model in your research, please cite:

```bibtex
@misc{medical-ministral-8b,
  author = {naazimsnh02},
  title = {Medical Ministral 8B: A Clinical Reasoning Model},
  year = {2025},
  publisher = {HuggingFace},
  howpublished = {\url{https://huggingface.co/naazimsnh02/medical-ministral-8b}}
}
```

## License

This model inherits the license from the base Ministral model. Please refer to the base model's license for usage terms.

## Acknowledgments

- **Base Model**: Mistral AI's Ministral 3 8B Reasoning
- **Fine-tuning**: Unsloth for efficient LoRA training
- **Framework**: Hugging Face Transformers ecosystem

**Disclaimer**: This model is provided "as-is" for research and educational purposes. The creators are not liable for any consequences resulting from the use of this model. Always consult qualified healthcare professionals for medical advice.
