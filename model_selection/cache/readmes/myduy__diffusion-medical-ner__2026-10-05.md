---
language:
- vi
pretty_name: Diffusion Language Model for Vietnamese NER
tags:
- diffusion-language-model
- ner
- fine-tuning
- dlm
task_categories:
- ner
- vietnamese-medical
base_model:
- Dream-org/Dream-v0-Instruct-7B
---

# Diffusion Language Model for Vietnamese NER

**Diffusion Language Model (DLM)** fine-tuned cho tác vụ **Named Entity Recognition (NER)** tiếng Việt.  
Mô hình này khai thác cơ chế **Diffusion-based Language Modeling** như một hướng tiếp cận thay thế cho các kiến trúc truyền thống **Encoder-only** (như BERT) hoặc **Decoder-only** (như GPT) trong các bài toán **token-level prediction**.

---

### Mô hình nền tảng
- **Base model:** [Dream 7B — Diffusion Large Language Models](https://arxiv.org/abs/2508.15487)  
- **Training objective:** Diffusion-based denoising for token prediction  
- **Fine-tuning task:** Vietnamese Named Entity Recognition (NER)

---

### Dữ liệu huấn luyện
Nguồn dữ liệu được sử dụng là từ:  
> **Nested Named-Entity Recognition on Vietnamese COVID-19: Dataset and Experiments**  
> [https://arxiv.org/abs/2504.21016]

- Bao gồm các thực thể lồng nhau trong văn bản tiếng Việt liên quan đến COVID-19.  
- Được gán nhãn thủ công theo định dạng NER chuẩn (BIO tagging).  
- Thích hợp cho huấn luyện các mô hình phân biệt ranh giới thực thể phức tạp.

---

### Điểm nổi bật
- Ứng dụng **diffusion process** để mô hình hóa phân phối của token, giúp cải thiện khả năng khái quát hóa và ổn định khi huấn luyện.  
- Cho phép **token prediction** mà không phụ thuộc hoàn toàn vào encoder hoặc decoder truyền thống.  
- Khả năng hiểu tiếng Việt từ Dream 7B.
- Độ dài chuôi đầu vào không bị giới hạng như các mô hình [Pho-BERT](https://arxiv.org/abs/2003.00744).
---

### Kết quả & hướng phát triển
- Đạt hiệu năng cạnh tranh so với các baseline encoder/decoder trong NER tiếng Việt.  
- Đang nghiên cứu mở rộng mô hình cho các tác vụ đa ngôn ngữ và đa miền dữ liệu.

---

### Ví dụ sử dụng

```python
import torch
from transformers import AutoModel, AutoTokenizer

model_path = "myduy/diffusion-medical-ner"
model = AutoModel.from_pretrained(model_path, torch_dtype=torch.bfloat16, trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = model.to("cuda").eval()


test = [ 
  {
    "instruction": "<ner>\nTiêm chủng vaccine ngừa virus SARS-CoV-2 là biện pháp hiệu quả.\n</ner>",
    "output": ""
  },
  {
    "instruction": "<ner>\nBệnh nhân được chẩn đoán mắc bệnh lao phổi và được điều trị theo phác đồ của WHO.\n</ner>",
    "output": ""
  },
  {
    "instruction": "<ner>\nKhoa Hồi sức tích cực tại Bệnh viện Bạch Mai đã tiếp nhận bệnh nhân nguy kịch.\n</ner>",
    "output": ""
  },
  {
    "instruction": "<ner>\nThuốc Paracetamol 500mg được sử dụng để hạ sốt cho trẻ em.\n</ner>",
    "output": ""
  },
  {
    "instruction": "<ner>\nTrung tâm Kiểm soát bệnh tật TP. Hồ Chí Minh khuyến cáo người dân đeo khẩu trang y tế.\n</ner>",
    "output": ""
  },
  {
    "instruction": "<ner>\nPhác đồ điều trị HIV/AIDS được cập nhật mới nhất năm 2025.\n</ner>",
    "output": ""
  }
]

messages = [
    {"role": "user", "content": "<ner>\nPhác đồ điều trị HIV/AIDS được cập nhật mới nhất năm 2025.\n</ner>"}
]
inputs = tokenizer.apply_chat_template(
    messages, return_tensors="pt", return_dict=True, add_generation_prompt=True
)
input_ids = inputs.input_ids.to(device="cuda")
attention_mask = inputs.attention_mask.to(device="cuda")

output = model.diffusion_generate(
    input_ids,
    attention_mask=attention_mask,
    max_new_tokens=512,
    output_history=True,
    return_dict_in_generate=True,
    steps=512,
    temperature=0.2,
    top_p=0.95,
    alg="entropy",
    alg_temp=0.,
)
generations = [
    tokenizer.decode(g[len(p) :].tolist())
    for p, g in zip(input_ids, output.sequences)
]

print(generations[0].split(tokenizer.eos_token)[0])
```
---
### Tài liệu tham khảo
- [Nested Named-Entity Recognition on Vietnamese COVID-19: Dataset and Experiments](https://arxiv.org/abs/2504.21016)  
- [Diffusion Large Language Models — Dream 7B](https://arxiv.org/abs/2508.15487)
- [PhoBERT: Pre-trained language models for Vietnamese](https://arxiv.org/abs/2003.00744)