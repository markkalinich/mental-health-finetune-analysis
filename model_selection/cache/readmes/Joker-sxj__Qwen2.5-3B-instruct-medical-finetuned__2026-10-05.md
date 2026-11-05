---
license: apache-2.0
datasets:
- FreedomIntelligence/medical-o1-reasoning-SFT
metrics:
- bleu
base_model:
- Qwen/Qwen2.5-3B-Instruct
pipeline_tag: question-answering
tags:
- medical
language:
- zho
- eng
- fra
- spa
- por
- deu
- ita
- rus
- jpn
- kor
- vie
- tha
- ara
---
模型经过医疗数据集微调后，已初步具备推理能力，可以进行基础的问诊，且文本的质量BLEU比原模型更优。