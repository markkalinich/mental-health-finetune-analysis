---
language:
- vi
library_name: transformers
pipeline_tag: token-classification
tags:
- Vietnamese
- Personal identification information
- Analysis
---

# Personal identification information detection - Nhận diện thông tin cá nhân
## Nhận diện ngôn ngữ hỗ trợ các ngôn ngữ:
- Tiếng Việt


## Model description

Mô hình có tác dụng nhận diện thông tin cá nhân hỗ trợ các ngôn ngữ:
- Họ và tên
- Giới tính
- Số điện thoại
- Email
- Địa chỉ
- Nơi làm việc
- Nghệ nghiệp
- Dân tộc
- Tôn giáo
- Nơi sinh
- Quê quán
- Quốc tịnh
- Nhóm máu
- Số căn cước công dân
- Số hộ chiếu
- Nơi ở hiện tại
- Tình trạng hôn nhân
- Ngày sinh
- Ngành học
- Trường học
- Bằng cấp
- Chức vụ
- Sở thích
- Tính cách
- Điểm mạnh
- Điểm yếu
- Tuổi
- Mục tiêu, mong muốn

Ví dụ:

Xin chào, tôi tên là Đặng Việt Dũng, tôi sinh ra ở Hòa Bình và đang sinh sống ở Hà Nội. Tôi thích chơi game và công nghệ, hiện tôi đang làm việc tại công ty 132.one, tôi là một lập trình viên. Tôi dễ nổi nóng nhưng có tính cách dễ hòa đồng. Tôi có bằng kỹ sư phần mềm lấy tại trường Đại Học Phương Đông. Là người dân tộc kinh, giới tính nam và không theo tốn giáo nào.
```text
Họ và tên: Đặng Việt Dũng ,
Quê quán: Hòa Bình
Quê quán: Hà Nội .
Sở thích: chơi game
Sở thích: công nghệ ,
Nơi làm việc: công ty 132 . one ,
Nghệ nghiệp: lập trình viên .
Điểm mạnh: dễ nổi nóng
Điểm mạnh: tính cách dễ hòa đồng .
Bằng cấp: kỹ sư phần mềm lấy
Trường học: trường Đại Học Phương Đông .
Tôn giáo: dân tộc kinh ,
Điểm mạnh: giới tính nam
Tôn giáo: không theo
```

## Base model

Mô hình được đạo tạo dựa trên cơ sở của model google-bert/bert-base-multilingual-cased

## Training data

Chưa thể công khai dữ liệu training

## Model variations

Chưa xác định

## Intended uses & limitations

Chưa xác định

## License

Đây là một open-source library, bạn có thể sử dụng nó với bất kì mục đích nào.
Rất cảm ơn nếu bạn ghi nguồn khi sử dụng mô hình này (nếu không ghi cũng không sao).

### How to use

```python
text = "Xin chào, tôi tên là Đặng Việt Dũng, tôi sinh ra ở Hòa Bình và đang sinh sống ở Hà Nội. Tôi thích chơi game và công nghệ, hiện tôi đang làm việc tại công ty 132.one, tôi là một lập trình viên. Tôi dễ nổi nóng nhưng có tính cách dễ hòa đồng. Tôi có bằng kỹ sư phần mềm lấy tại trường Đại Học Phương Đông. Là người dân tộc kinh, giới tính nam và không theo tốn giáo nào."

import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification

tokenizer = AutoTokenizer.from_pretrained("mr4/ner-vi")
inputs = tokenizer(text, return_tensors="pt")

model = AutoModelForTokenClassification.from_pretrained("mr4/ner-vi")
with torch.no_grad():
    logits = model(**inputs).logits

predicted_token_class_ids = torch.argmax(logits, dim=-1)
tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"].squeeze().tolist())
print("List all token:")
predicted_entities = [model.config.id2label[id] for id in predicted_token_class_ids.squeeze().tolist()]
for token, entity in zip(tokens, predicted_entities):
    print(f"  - {token}: {entity}")

final_result = []
current_entity = []
current_label = None

for token, entity in zip(tokens, predicted_entities):
    if entity.startswith("B-"):
        if entity[2:] == current_label:
            current_entity.append(token)
        else:
            if current_entity:
                final_result.append((" ".join(current_entity), current_label))
            current_entity = [token]
            current_label = entity[2:]
    elif entity.startswith("I-") and current_label == entity[2:]:
        current_entity.append(token)
    else:
        if current_entity:
            final_result.append((" ".join(current_entity), current_label))
        current_entity = []
        current_label = None
if current_entity:
    final_result.append((" ".join(current_entity), current_label))

print("Input:")
print(text)

print("Final result:")
for entity, label in final_result:
    ner_value = entity.replace(" ##", "").replace("##", "")
    print(f"  - {ner_value}: {label}")
```

## Liên hệ

Mọi thông tin liên quan có thể liên hệ qua email: zZz4everzZz@live.co.uk.