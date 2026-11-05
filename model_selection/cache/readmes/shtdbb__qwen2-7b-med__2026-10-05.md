---
datasets:
- tyang816/MedChatZH
- michaelwzhu/ChatMed_Consult_Dataset
language:
- zh
- en
base_model: Qwen/Qwen2-7B-Instruct
---

## 模型总览
基于 `Qwen2-7B-Instruct` 在 `tyang816/MedChatZH`、`michaelwzhu/ChatMed_Consult_Dataset` 和 [`TCM-SD`](https://tianchi.aliyun.com/dataset/139034) 数据集上构造对话模版并随机采样了 32K 训练数据，进行的 LoRA 微调。

模型具备中医辩证、中医及中文医学领域问答的能力。