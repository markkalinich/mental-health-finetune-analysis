---
license: mit
metrics:
- accuracy
pipeline_tag: text-classification
---
# multi_diagnosis_Bio_ClinicalBERT

基于 [Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) 的 **多标签文本分类 (multi-label classification)** 微调项目。  
该仓库包含从临床/医学文本中同时预测多个标签的完整流程：数据准备、训练、评估与推理示例。

> 初始模型：`emilyalsentzer/Bio_ClinicalBERT`（BERT-Base, cased，临床语料继续预训练）  
> 本仓库微调后模型：`multi_diagnosis_Bio_ClinicalBERT`

---

## 目录
- [背景](#背景)
- [功能特性](#功能特性)
- [快速开始](#快速开始)
  - [环境要求建议](#环境要求建议)
  - [调用模型](#调用模型)
- [如何使用](#如何使用)
- [输出形式](#输出形式)
- [引用与致谢](#引用与致谢)
- [数据与合规](#数据与合规)
- [医疗免责声明](#医疗免责声明)

---

## 背景
临床文本（主诉、既往病史、家庭病史等）通常需要同时预测多个疾病标签（本模型训练标签为hypertension，hyperlipidemia，coronary artery disease，atrial fibrillation，others）。本项目在 Bio_ClinicalBERT 基座上进行**多标签**微调，使其在同一段文本上输出多个标签的概率分布。

---

## 功能特性
- ✅ **多标签训练**：Sigmoid 输出 + 二元交叉熵损失（`BCEWithLogitsLoss`）
- ✅ **可配置训练脚本**：学习率、Batch Size、最大长度、权重衰减等均可通过参数调节
- ✅ **类不平衡支持**：可选损失权重、正负样本比例调整
- ✅ **完善评估指标**：micro/macro F1、precision/recall、AUROC（micro/macro）、PR-AUC
- ✅ **推理便捷**：单条/批量文本预测，返回每个标签的概率与阈值化标签

---

## 快速开始

### 模型运行环境
- Python 3.9.21
- Pytorch 2.6.0
- CUDA Version 13.0
- 🤗 Transformers 4.51.3
- Datasets 3.3.2
- scikit-learn, numpy, pandas, tqdm 

### 环境要求建议
- Python ≥ 3.9
- PyTorch（建议使用与您 CUDA 匹配的版本）
- 🤗 Transformers ≥ 4.41
- Datasets ≥ 2.19
- scikit-learn, numpy, pandas, tqdm

### 调用模型
```bash
tokenizer = AutoTokenizer.from_pretrained(Thehk02/multi_diagnosis_Bio_ClinicalBERT)
model = AutoModelForSequenceClassification.from_pretrained(Thehk02/multi_diagnosis_Bio_ClinicalBERT)

```
### 如何使用

```python

LABEL_NAMES = ["hypertension", "hyperlipidemia", "coronary artery disease", "atrial fibrillation", "others"]

# 加载分词器与模型
tokenizer = AutoTokenizer.from_pretrained(Thehk02/multi_diagnosis_Bio_ClinicalBERT)
model = AutoModelForSequenceClassification.from_pretrained(Thehk02/multi_diagnosis_Bio_ClinicalBERT)
model.eval()

model.config.id2label = {i: label for i, label in enumerate(LABEL_NAMES)}
model.config.label2id = {v: k for k, v in model.config.id2label.items()}

classifier = TextClassificationPipeline(
    model=model,
    tokenizer=tokenizer,
    framework="pt",
    device=pipeline_device_idx,
    return_all_scores=True,
    function_to_apply="sigmoid",
    top_k=None
)

# 单条文本预测
text = "xxx"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)

with torch.no_grad():
    logits = model(**inputs).logits
probs = torch.sigmoid(logits)[0]  # 每个标签的概率

# 读取标签名（建议在训练保存时写入 config）
labels = [model.config.id2label[i] for i in range(model.config.num_labels)]
print(dict(zip(labels, probs.tolist())))
```
## 输出形式
输出形式为 diagnosis:possibility
```json
hypertension: 0.8148
```

## 引用与致谢

本项目在 **Bio_ClinicalBERT** 基座上进行多标签微调，特此致谢原作者与社区贡献者。  
- 基座模型：[`emilyalsentzer/Bio_ClinicalBERT`](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT)

如果本仓库或模型对你的研究/产品有帮助，请引用：

```bibtex
@misc{magnet:?xt=urn:btih:magnet:?xt=urn:btih:magnet:?xt=urn:btih:magnet:?xt=urn:btih:li2025refinemedicaldiagnosisusing,
      title={Refine Medical Diagnosis Using Generation Augmented Retrieval and Clinical Practice Guidelines}, 
      author={Wenhao Li and Hongkuan Zhang and Hongwei Zhang and Zhengxu Li and Zengjie Dong and Yafan Chen and Niranjan Bidargaddi and Hong Liu},
      year={2025},
      eprint={2506.21615},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2506.21615}, 
}
```
并引用Bio_ClinicalBERT文章

```bibtex
@inproceedings{alsentzer-etal-2019-publicly,
    title = "Publicly Available Clinical {BERT} Embeddings",
    author = "Alsentzer, Emily  and
      Murphy, John  and
      Boag, William  and
      Weng, Wei-Hung  and
      Jin, Di  and
      Naumann, Tristan  and
      McDermott, Matthew",
    booktitle = "Proceedings of the 2nd Clinical Natural Language Processing Workshop",
    month = jun,
    year = "2019",
    address = "Minneapolis, Minnesota, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/W19-1909",
    doi = "10.18653/v1/W19-1909",
    pages = "72--78"
}
```
### 数据与合规
如使用 MIMIC-III / MIMIC-IV 等临床数据进行训练或复现，须遵守其数据使用协议（DUA）与相关许可要求。这些数据条款独立于代码/模型的 MIT 许可。用户应自行确保具备资格、签署 DUA 并遵循隐私与伦理规范。

### 医疗免责声明
本项目及其输出仅用于科研与工程演示，不构成医疗诊断或治疗建议；不得作为临床决策的唯一依据；不得用于识别或重识别任何个人健康信息（PHI）。