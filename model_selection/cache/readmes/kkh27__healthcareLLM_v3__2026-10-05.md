## 🛠️ Model Details

- **Base Model**: `LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct`  
- **Model Size**: 7.8B  
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
| Target Modules | `q_proj`, `k_proj` |

### ⚙️ Training Arguments

| Argument                     | Value                     |
|------------------------------|---------------------------|
| Per device train batch size  | 8                         |
| Gradient accumulation steps  | 1                         |
| Epochs                       | 3                         |
| Learning rate                | 5e-6                      |
| Weight decay                 | 0.1                       |

---