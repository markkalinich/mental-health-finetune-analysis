## Model Details
- **Base Model**: `trillionslabs/Tri-7B`  
- **Model Size**: 7.53B  
- **Fine-tuned by**: [zzhenxi](https://huggingface.co/zzhenxi)  
- **Training Framework**: Hugging Face Transformers + PEFT (LoRA)  
- **Precision**: bfloat16 (bf16)  
- **Language**: Korean  

---

## Training Configuration
### LoRA Configuration
| Parameter     | Value      |
|---------------|------------|
| Rank (`r`)    | 16         |
| Alpha         | 32         |
| Dropout       | 0.05       |
| Bias          | none       |
| Task Type     | CAUSAL_LM  |
| Target Modules | `q_proj`, `v_proj` |

### Training Arguments
| Argument                     | Value                     |
|------------------------------|---------------------------|
| Per device train batch size  | 8                         |
| Gradient accumulation steps  | 2                        |
| Epochs                       | 2                         |
| Learning rate                | 2e-4                      |
| Weight decay                 | 0.1                       |

---
###  Updates
- Previous version (v4) is in [HealthcareLLM-v4-Tri-7B](https://huggingface.co/kkh27/healthcareLLM_v4_Tri-7B)
- Enhanced output format consistency and improved generalized responses across diverse prompts.