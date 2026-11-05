---
license: apache-2.0
language: vi
pipeline_tag: token-classification
tags:
- xlm-roberta
- ner
- pii
- vietnamese
---

# 🛡️ Mô hình XLM-R nhận diện Thông tin Cá nhân (PII) Tiếng Việt

Đây là mô hình XLM-RoBERTa (base) được tinh chỉnh (fine-tuned) cho bài toán nhận diện thực thể (Named Entity Recognition - NER) chuyên biệt nhằm trích xuất các Thông tin cá nhân (PII) trong văn bản tiếng Việt. 

Mô hình này là một phần trong dự án nghiên cứu so sánh hiệu năng giữa 4 kiến trúc học sâu (**BiLSTM, BiLSTM-CRF, PhoBERT, và XLM-R**) cho tác vụ ẩn danh hóa thông tin cá nhân, được thực hiện bởi Tăng Hoàng Phúc (Sinh viên chuyên ngành Trí tuệ Nhân tạo - Đại học CNTT, ĐHQG TP.HCM).

## 📊 Thông tin mô hình
* **Base model:** `xlm-roberta-base`
* **Ngôn ngữ:** Tiếng Việt (Multilingual base)
* **Tác vụ:** Token Classification (NER)
* **Số lượng nhãn:** Phân loại và nhận diện 54 nhãn PII khác nhau (Tên người, CCCD, Email, Số điện thoại, Địa chỉ...).

## 🚀 Ví dụ đầu vào
*"Căn cước công dân của Nguyễn Văn A là 079201123456, số điện thoại 0972836728, địa chỉ 123 đường Lê Lợi, Quận 1."*