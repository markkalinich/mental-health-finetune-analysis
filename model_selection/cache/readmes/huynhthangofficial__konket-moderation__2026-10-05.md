---
library_name: transformers
pipeline_tag: text-classification
language: vi
license: mit
base_model: vinai/phobert-base
tags:
- generated_from_trainer
- vietnamese
- hate-speech-detection
datasets:
- uitnlp/vihsd
model-index:
- name: konket-moderation
  results: []
widget:
- text: "Cái app này dùng chán quá, rác rưởi thật sự!"
- text: "Chào mọi người, chúc một ngày tốt lành."
---

# 🛡️ Mô hình AI Kiểm duyệt Nội dung (KonKet Moderation)

Đây là mô hình Trí tuệ Nhân tạo phân loại văn bản (Text Classification) được tinh chỉnh (fine-tuned) từ lõi [vinai/phobert-base](https://huggingface.co/vinai/phobert-base). 
Mô hình được phát triển dành riêng cho hệ thống mạng xã hội **KonKet** (Đồ án Tốt nghiệp).

## 📌 Chức năng & Phân loại Nhãn (Labels)
Mô hình có nhiệm vụ tự động quét, nhận diện và phân loại các bài viết/bình luận tiếng Việt thành 3 cấp độ để Backend (Convex) ra quyết định kiểm duyệt:
* **`LABEL_0` (Clean):** Nội dung sạch, bình thường.
* **`LABEL_1` (Offensive):** Ngôn từ xúc phạm, văng tục.
* **`LABEL_2` (Hate):** Ngôn từ thù ghét, công kích mạnh.

## 🗄️ Dữ liệu huấn luyện (Training Data)
Được huấn luyện trên bộ dữ liệu nghiên cứu chuẩn **UIT-ViHSD** (Vietnamese Hate Speech Detection) của trường Đại học Công nghệ Thông tin. Đã trải qua quá trình làm sạch (Data Cleaning) để loại bỏ giá trị rỗng trước khi đưa vào huấn luyện.

## ⚙️ Cấu hình tinh chỉnh (Training hyperparameters)
- **Learning rate:** 2e-05
- **Train batch size:** 16
- **Epochs:** 3
- **Optimizer:** AdamW
- **Frameworks:** Transformers 5.0.0, PyTorch 2.10.0+cu128