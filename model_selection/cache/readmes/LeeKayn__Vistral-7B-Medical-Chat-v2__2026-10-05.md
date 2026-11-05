---
license: apache-2.0
base_model: Viet-Mistral/Vistral-7B-Chat
tags:
- vietnamese
- medical
- healthcare
- vistral
- mistral
- merged
language:
- vi
pipeline_tag: text-generation
---

# Vistral-7B-Medical-Chat-v2

## 📋 Mô tả

Đây là phiên bản đã merge của **Vistral-7B-Chat** với adapter **LeeKayn/Vistral_medical_2205_v1.3**, được tối ưu cho tư vấn y tế bằng tiếng Việt.

## 🔧 Chi tiết kỹ thuật

- **Base Model**: Viet-Mistral/Vistral-7B-Chat
- **Medical Adapter**: LeeKayn/Vistral_medical_2205_v1.3
- **Merged**: Đã merge adapter vào base model để tối ưu tốc độ
- **Quantization**: Hỗ trợ 4-bit quantization với BitsAndBytesConfig

## 🚀 Cách sử dụng

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch

# Quantization config
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
)

# Load model
model = AutoModelForCausalLM.from_pretrained(
    "LeeKayn/Vistral-7B-Medical-Chat-v2",
    quantization_config=bnb_config,
    torch_dtype=torch.float16,
    device_map="auto",
    trust_remote_code=True
)

tokenizer = AutoTokenizer.from_pretrained("LeeKayn/Vistral-7B-Medical-Chat-v2", trust_remote_code=True)

# Generate
def ask_medical_question(question):
    prompt = f"<s>[INST] Bạn là bác sĩ chuyên khoa. Hãy trả lời câu hỏi y tế sau một cách chính xác: {question} [/INST]"
    inputs = tokenizer(prompt, return_tensors="pt")
    
    with torch.inference_mode():
        outputs = model.generate(
            **inputs,
            max_new_tokens=512,
            temperature=0.1,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )
    
    response = tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)
    return response.strip()

# Ví dụ
answer = ask_medical_question("Triệu chứng của bệnh tiểu đường là gì?")
print(answer)
```

## ⚠️ Lưu ý quan trọng

- Model này chỉ hỗ trợ tư vấn y tế cơ bản
- **KHÔNG thay thế** việc khám bác sĩ chuyên khoa
- Luôn tham khảo ý kiến bác sĩ cho các vấn đề sức khỏe nghiêm trọng

## 📊 Performance

- **Max tokens**: 512
- **Temperature**: 0.1 (tối ưu cho tính chính xác)
- **Memory**: ~4GB VRAM với 4-bit quantization

## 🔗 Credits

- Base Model: [Viet-Mistral/Vistral-7B-Chat](https://huggingface.co/Viet-Mistral/Vistral-7B-Chat)
- Medical Adapter: [LeeKayn/Vistral_medical_2205_v1.3](https://huggingface.co/LeeKayn/Vistral_medical_2205_v1.3)
