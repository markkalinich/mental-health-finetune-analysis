---
base_model: meta-llama/Llama-3.1-8B-Instruct
library_name: transformers
license: llama3.1
language: [en, vi]
tags: [cbt, mental-health, counseling, lora, structured-output]
pipeline_tag: text-generation
---

# cbt-llama3.1-8b-v2

Fine-tune (LoRA→merged) của **meta-llama/Llama-3.1-8B-Instruct** cho trợ lý tham vấn theo liệu pháp CBT.
Model sinh **JSON có cấu trúc** gồm: `risk_level · technique · rationale · plan · response · safety_action`.

## Huấn luyện
- Dữ liệu: 26.000 mẫu hội thoại CBT (định dạng `messages`, output JSON 6 trường).
- LoRA r=32/α=64, lr=5e-05, max_len=1536, bf16.
- best eval_loss = 0.48264360427856445 (epoch 3.0).

## ⚠️ Giới hạn & an toàn
Đây là **công cụ hỗ trợ học thuật**, KHÔNG thay thế chuyên gia sức khỏe tâm thần,
KHÔNG chẩn đoán, KHÔNG tư vấn thuốc. Khi có dấu hiệu khủng hoảng/tự hại, model
được huấn luyện để ưu tiên an toàn và khuyến nghị liên hệ chuyên gia/dịch vụ khẩn cấp.
Cần có chuyên gia rà soát (human-in-the-loop) trước khi dùng với người thật.
