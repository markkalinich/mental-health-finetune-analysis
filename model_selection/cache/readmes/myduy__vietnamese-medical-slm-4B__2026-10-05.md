---
base_model: unsloth/Qwen3-4B-Base
tags:
  - text-generation-inference
  - transformers
  - unsloth
  - qwen3
  - trl
  - sft
license: apache-2.0
language:
  - vi
  - en
---

# Vietnamese Medical Reasoning Language Model

**Reasoning Small Language Model for Vietnamese Medical Tasks**

---

## Overview
*Note: Đây là phiên bản 4B.*
Dự án này phát triển một **mô hình ngôn ngữ nhỏ (Small Language Model - SLM)** có khả năng **reasoning (lý luận)** trong lĩnh vực **y tế tiếng Việt**.  
Mục tiêu của mô hình là hỗ trợ xử lý ngôn ngữ tự nhiên trong các tình huống y học — bao gồm phân tích, diễn giải và đưa ra hỗ trợ ban đầu dựa trên ngữ cảnh.

Mô hình được **tinh chỉnh (SFT – Supervised Fine-Tuning)** trên tập dữ liệu y tế tiếng Việt, giúp cải thiện khả năng suy luận và phản hồi hợp lý trước khi tạo ra kết quả.

⚠️ **Lưu ý quan trọng:**  
Mô hình **không thay thế cho chẩn đoán chuyên môn**. Kết quả cần được xác minh hoặc diễn giải dưới sự giám sát của **chuyên gia y tế**.

---

## Training Framework

Quá trình huấn luyện được thực hiện bằng **[Unsloth](https://github.com/unslothai/unsloth)** — một framework tối ưu cho việc tinh chỉnh mô hình lớn trên phần cứng giới hạn.  
Điều này giúp mô hình có thể được huấn luyện **hiệu quả hơn** trên GPU tầm trung mà vẫn đạt chất lượng cao.

---

## Model Details

| **Field** | **Description** |
|------------|----------------|
| **Base Model** | `unsloth/Qwen3-4B-Base` |
| **Finetuned By** | `myduy` |
| **Framework** | Unsloth + TRL |
| **License** | Apache 2.0 |
| **Languages** | Vietnamese, English |
| **Primary Task** | Medical reasoning & response generation |

---

## Intended Use

- Thử nghiệm mô hình ngôn ngữ trong lĩnh vực **AI y tế**.  
- Phát triển chatbot y tế tiếng Việt có khả năng lý luận. 
---

## Limitations

- Mô hình có thể **tạo ra thông tin không chính xác hoặc lỗi suy luận**.  
- Không được sử dụng cho **mục đích chẩn đoán hoặc điều trị y tế trực tiếp**.  
- Các phản hồi nên được xem là **gợi ý hỗ trợ**, không phải kết luận y khoa.

---
