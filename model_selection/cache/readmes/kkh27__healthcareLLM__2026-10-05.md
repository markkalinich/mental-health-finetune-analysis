
## 🛠️ Model Details

- **Base Model**: `yanolja/EEVE-Korean-Instruct-10.8B-v1.0`  
- **Model Size**: 10.8B  
- **Fine-tuned by**: [kkh27](https://huggingface.co/kkh27)  
- **Training Framework**: Hugging Face Transformers + PEFT (LoRA)  
- **Precision**: bfloat16 (bf16)  
- **Language**: Korean  

---

## 🧪 Training Configuration

### 🔧 LoRA Configuration

| Parameter     | Value      |
|---------------|------------|
| Rank (`r`)    | 16         |
| Alpha         | 32         |
| Dropout       | 0.05       |
| Bias          | none       |
| Task Type     | CAUSAL_LM  |
| Target Modules | `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj` |

### ⚙️ Training Arguments

| Argument                     | Value                     |
|------------------------------|---------------------------|
| Per device train batch size  | 8                         |
| Gradient accumulation steps  | 1                         |
| Epochs                       | 3                         |
| Learning rate                | 5e-6                      |
| Weight decay                 | 0.1                       |

---
