---
license: apache-2.0
base_model: tencent/WeMM-Embedding-2B
library_name: transformers
tags:
  - sentence-transformers
  - embedding
  - medical
  - chinese
  - qwen3
  - pruned
metrics:
  - recall@1
---

# WeMM-Medical-Pruned25

基于 **[tencent/WeMM-Embedding-2B](https://huggingface.co/tencent/WeMM-Embedding-2B)**（[Tencent/WeMM-Embedding](https://github.com/Tencent/WeMM-Embedding)，Apache-2.0）的中文医疗检索 embedding 模型，经过三轮无训练瘦身，最终 **3.31 GB / 1.655B 参数**：

1. **移除视觉/视频塔**（`model.visual.*`，0.66 GB）
2. **移除 lm_head**（508M 参数 logits 头，1.02 GB），`forward` 直接返回 hidden states
3. **医疗领域校准 FFN 通道剪枝 25%**（intermediate 6144→4608）：Wanda 式通道得分
   `s_j = ||down_proj[:,j]|| × RMS(silu(gate_j(x)) ⊙ up_j(x))`，
   在 300 条医疗语料（医学教材 200 段 + 医疗 query 100 条）上 batch=1 校准，
   每层保留得分 top-k 通道

相比原始 WeMM-Embedding-2B（5.44 GB / 2.72B）：**文件 −39%，bf16 加载内存 5.53→3.56 GB（−36%）**。

## 效果

| 指标 | 原始 WeMM-2B | 本模型 |
|---|---|---|
| 医疗检索 R@1（2048/1024/512 维） | 1.000 | **1.000** |
| 常识检索 R@1（8 题小样本，2048 维） | 0.875 | 0.750（1024/512 维 0.875） |
| 嵌入漂移（103 条余弦 vs 原始） | — | mean 0.941 / min 0.861 |

医疗场景检索无损；通用能力在小样本上有轻微损失。

## 用法

```python
import torch
from transformers import AutoModel, AutoTokenizer

path = "YOUR_HF_ID/wemm-medical-pruned25"
tok = AutoTokenizer.from_pretrained(path, trust_remote_code=True)
model = AutoModel.from_pretrained(path, trust_remote_code=True, torch_dtype=torch.bfloat16)
model.eval()

texts = ["高血压能不能吃西柚<embedding>", "感冒发烧怎么办<embedding>"]
enc = tok(texts, padding=True, truncation=True, max_length=512, return_tensors="pt")
with torch.no_grad():
    emb = model.embedding(input_ids=enc["input_ids"], attention_mask=enc["attention_mask"])
# emb: [2, 2048], L2-normalized
```

- 输入末尾必须拼 `<embedding>` special token（last-token pooling）
- 向量 2048 维，L2 归一化；支持 Matryoshka 截断 1024/512（本项目评测下指标无损）

## 链接

| | |
|---|---|
| **原始模型** | [tencent/WeMM-Embedding-2B](https://huggingface.co/tencent/WeMM-Embedding-2B) · [HF collection](https://huggingface.co/collections/tencent/wemm-embedding) |
| **原始项目（Tencent）** | [github.com/Tencent/WeMM-Embedding](https://github.com/Tencent/WeMM-Embedding) |
| **本模型构建仓库** | [github.com/weifding/wemm-medical-embedding](https://github.com/weifding/wemm-medical-embedding) |

## 构建与评估

- 构建代码见上方 GitHub 仓库（`scripts/strip_vision.py`、`scripts/prune_ffn.py`、`scripts/benchmark_thin.py`）
- 评估集：`data/eval_medical.jsonl`（医疗 4 组）、`data/eval_commonsense.jsonl`（常识 8 组）
- 完整阶梯数据（基线 / 25% / 50%）见仓库 `docs/prune_ffn.md`

## License

Apache-2.0（继承自 [tencent/WeMM-Embedding-2B](https://huggingface.co/tencent/WeMM-Embedding-2B)）

---

## English Version

**WeMM-Medical-Pruned25** is a text-only Chinese medical retrieval embedding derived from **[tencent/WeMM-Embedding-2B](https://huggingface.co/tencent/WeMM-Embedding-2B)** ([Tencent/WeMM-Embedding](https://github.com/Tencent/WeMM-Embedding), Apache-2.0) through three training-free thinning rounds, ending at **3.31 GB / 1.655B parameters** (original: 5.44 GB / 2.72B, i.e. **−39% file size, −36% bf16 load memory**):

1. **Vision/video tower removal** — `self.model.visual` is deleted at model init (transformers rebuilds it unconditionally from config otherwise); video-only helper files removed.
2. **`lm_head` removal** — drops the 508M-param / 1.02 GB logits head that the embedding path never uses; `forward()` returns hidden states directly (this also fixed a legacy bug where callers pooled logits instead of hidden states).
3. **Medical-domain FFN channel pruning (25%)** — Wanda-style channel score `s_j = ||down_proj[:,j]|| × RMS(silu(gate_j(x)) ⊙ up_j(x))` calibrated on 300 medical texts (batch=1, no padding); per layer the top-k channels are kept (intermediate 6144 → 4608).

### Results vs the original model

| Metric | Original WeMM-2B | This model |
|---|---|---|
| Medical retrieval R@1 (2048/1024/512) | 1.000 | **1.000 (unchanged)** |
| Commonsense R@1 (8-item set, 2048-dim) | 0.875 | 0.750 (0.875 at 1024/512) |
| Commonsense R@5 | 1.000 | 1.000 |
| Embedding drift (103 texts, cosine) | — | mean 0.941 / min 0.861 |

Medical retrieval is lossless; the general-domain cost is a single item on a tiny 8-question set.

### Usage

```python
import torch
from transformers import AutoModel, AutoTokenizer

path = "ding20260928/wemm-medical-pruned25"
tok = AutoTokenizer.from_pretrained(path, trust_remote_code=True)
model = AutoModel.from_pretrained(path, trust_remote_code=True, torch_dtype=torch.bfloat16)
model.eval()

texts = ["Can I eat grapefruit with blood pressure meds?<embedding>", "What to do for a fever?<embedding>"]
enc = tok(texts, padding=True, truncation=True, max_length=512, return_tensors="pt")
with torch.no_grad():
    emb = model.embedding(input_ids=enc["input_ids"], attention_mask=enc["attention_mask"])
# emb: [2, 2048], L2-normalized
```

- Always append the `<embedding>` special token (last-token pooling).
- Vectors are 2048-dim and L2-normalized; Matryoshka truncation to 1024/512 keeps metrics unchanged in our evaluation.

### Links

| | |
|---|---|
| **Base model** | [tencent/WeMM-Embedding-2B](https://huggingface.co/tencent/WeMM-Embedding-2B) · [HF collection](https://huggingface.co/collections/tencent/wemm-embedding) |
| **Original project (Tencent)** | [github.com/Tencent/WeMM-Embedding](https://github.com/Tencent/WeMM-Embedding) |
| **Build repository** | [github.com/weifding/wemm-medical-embedding](https://github.com/weifding/wemm-medical-embedding) |

License: Apache-2.0, inherited from tencent/WeMM-Embedding-2B.
