---
license: apache-2.0
language: vi
pipeline_tag: token-classification
tags:
- phobert
- ner
- pii
- vietnamese
---

# 🛡️ Mô hình PhoBERT nhận diện Thông tin Cá nhân (PII) Tiếng Việt

Đây là mô hình PhoBERT-base được tinh chỉnh (fine-tuned) cho bài toán nhận diện thực thể (Named Entity Recognition - NER) chuyên biệt nhằm trích xuất các Thông tin cá nhân (PII) trong văn bản tiếng Việt. 

Mô hình này là một phần trong dự án nghiên cứu so sánh hiệu năng giữa 4 kiến trúc học sâu (**BiLSTM, BiLSTM-CRF, PhoBERT, và XLM-R**) cho tác vụ ẩn danh hóa thông tin cá nhân, được thực hiện bởi Tăng Hoàng Phúc (Sinh viên chuyên ngành Trí tuệ Nhân tạo - Đại học CNTT, ĐHQG TP.HCM).

## 📊 Thông tin mô hình
* **Base model:** `vinai/phobert-base`
* **Ngôn ngữ:** Tiếng Việt
* **Tác vụ:** Token Classification (NER)
* **Số lượng nhãn:** Phân loại và nhận diện 54 nhãn PII khác nhau (Tên người, CCCD, Email, Số điện thoại, Địa chỉ...).

Ví dụ: *"Xin chào, tôi là Nguyễn Văn An, số điện thoại 0912345678, địa chỉ 123 Lê Lợi, Quận 1."*