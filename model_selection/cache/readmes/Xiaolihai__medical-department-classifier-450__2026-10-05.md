---
language: zh
license: mit
tags:
- medical
- classification
- chinese
- bert
---

# Medical Department Classifier (Training Size: 450)

This model is trained on a subset of 450 samples from the medical dialogue dataset.

## Model Details

- **Model Type**: BERT (Chinese)
- **Training Size**: 450 samples
- **Number of Classes**: 44
- **Classes**: 临床心理门诊, 产科, 儿科, 内分泌代谢科, 创伤骨科与骨关节科, 口腔科, 呼吸内科, 妇科, 妇科内分泌科, 康复医学科, 心胸外科, 心血管内科, 感染性疾病科, 新生儿科, 普外科, 普通外科, 泌尿外科, 消化内科, 消化内科、神经内科, 烧伤整形科, 生殖医学科, 甲状腺乳腺外科, 疼痛科, 皮肤性病科, 皮肤科, 眼科, 神经内科, 神经外科, 精神心理科, 耳鼻喉科, 肛肠外科, 肝病门诊, 肝胆外科, 肝胆胰疝外科, 肝胆胰脾疝外科, 肾内科, 脊柱外科, 血液内科, 血管外科, 运动医学与骨关节科, 门诊产科, 门诊妇科, 风湿免疫科, 风湿免疫科门诊

## Usage

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Xiaolihai/medical-department-classifier-450")
tokenizer = AutoTokenizer.from_pretrained("Xiaolihai/medical-department-classifier-450")
```
