---
language:
- bg
- cs
- da
- de
- el
- en
- es
- et
- fi
- fr
- ga
- hr
- hu
- it
- lt
- lv
- mt
- nl
- pl
- pt
- ro
- sk
- sl
- sv
pipeline_tag: token-classification
tags:
- pii
- ner
- privacy
base_model: nreimers/mMiniLMv2-L6-H384-distilled-from-XLMR-Large
---

# eu-pii-multi-mini-preview

**!IMPORTANT!** 
This is a preview model currently under training. Take extra caution when deploying it in any production setting.

Multilingual (24 EU languages) PII token-classification model, fine-tuned from `nreimers/mMiniLMv2-L6-H384-distilled-from-XLMR-Large` (34 entity classes, BIO scheme).

## Results

| split | macro P | macro R | macro F1 (w/o O) |
|---|---|---|---|
| valid | 0.9082 | 0.8970 | 0.8963 |
| test | 0.8080 | 0.7862 | 0.7863 |

### Per-language test F1 (macro, without O)

| lang | docs | F1 |
|---|---|---|
| bg | 45 | 0.9055 |
| cs | 55 | 0.9183 |
| da | 63 | 0.9023 |
| de | 59 | 0.8919 |
| el | 62 | 0.9142 |
| en | 62 | 0.8935 |
| es | 57 | 0.8732 |
| et | 78 | 0.9061 |
| fi | 65 | 0.9429 |
| fr | 52 | 0.917 |
| ga | 56 | 0.8993 |
| hr | 58 | 0.9231 |
| hu | 58 | 0.9111 |
| it | 51 | 0.8951 |
| lt | 52 | 0.9242 |
| lv | 52 | 0.9282 |
| mt | 52 | 0.9182 |
| nl | 60 | 0.9049 |
| pl | 69 | 0.7252 |
| pt | 67 | 0.8945 |
| ro | 53 | 0.8969 |
| sk | 56 | 0.8791 |
| sl | 68 | 0.8885 |
| sv | 57 | 0.8676 |
| ALL | 1407 | 0.7863 |

## Entity classes

`ACCOUNT_IDENTIFIER`, `AUTH_SECRET`, `BANK_ACCOUNT_IDENTIFIER`, `BIOMETRIC_DATA`, `CONTACT_HANDLE`, `CRIMINAL_OFFENCE_DATA`, `DATE`, `DATE_OF_BIRTH`, `DEVICE_IDENTIFIER`, `DOCUMENT_IDENTIFIER`, `EMAIL_ADDRESS`, `ETHNIC_ORIGIN`, `FINANCIAL_AMOUNT`, `GEO_LOCATION`, `HEALTH_DATA`, `IDENTIFYING_LINK`, `IP_ADDRESS`, `LOCATION`, `ORGANIZATION_IDENTIFIER`, `ORGANIZATION_NAME`, `PAYMENT_CARD`, `PAYMENT_CARD_SECURITY`, `PERSON_ATTRIBUTE`, `PERSON_IDENTIFIER`, `PERSON_NAME`, `PERSON_ROLE_OR_TITLE`, `PHONE_NUMBER`, `POLITICAL_OPINION`, `POSTAL_ADDRESS`, `PROPER_NAME`, `RELIGION_OR_BELIEF`, `SEXUAL_ORIENTATION`, `TRADE_UNION_MEMBERSHIP`, `VEHICLE_IDENTIFIER`

## Training

- learning rate 3e-05, batch size 32, 5 epochs, weight decay 0.01
- early stopping on validation macro-F1 (without O)

## ONNX

The `onnx/` folder contains `model.onnx` and a dynamically int8-quantized `model_quantized.onnx` for CPU inference:

```python
from optimum.onnxruntime import ORTModelForTokenClassification
model = ORTModelForTokenClassification.from_pretrained(
    "bardsai/eu-pii-multi-mini-preview", subfolder="onnx", file_name="model_quantized.onnx"
)
```
