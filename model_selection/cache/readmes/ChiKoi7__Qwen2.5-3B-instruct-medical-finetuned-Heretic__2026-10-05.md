---
license: apache-2.0
datasets:
- FreedomIntelligence/medical-o1-reasoning-SFT
base_model:
- Qwen/Qwen2.5-3B-Instruct
- Joker-sxj/Qwen2.5-3B-instruct-medical-finetuned
pipeline_tag: image-text-to-text
library_name: transformers
tags:
- abliterated
- Heretic
- decensored
- Qwen2
- Qwen2.5
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

# A decensored version of [Joker-sxj/Qwen2.5-3B-instruct-medical-finetuned](https://huggingface.co/Joker-sxj/Qwen2.5-3B-instruct-medical-finetuned), made using [Heretic](https://github.com/p-e-w/heretic) v1.2.0

|                   | Qwen2.5-3B-instruct-medical-finetuned-Heretic | Original model<br> ([Joker-sxj/Qwen2.5-3B-instruct-medical-finetuned](https://huggingface.co/Joker-sxj/Qwen2.5-3B-instruct-medical-finetuned)) |
| ----------------- | --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Refusals**      | 4/100                                         | 79/100                                                                                                                                         |
| **KL divergence** | 0.0126                                        | 0 *(by definition)*                                                                                                                            |

## Heretic Abliteration parameters

| Parameter                             | Value     |
|:------------------------------------- |:---------:|
| **direction_index**                   | 24.64		|
| **attn.o_proj.max_weight**            | 1.32      |
| **attn.o_proj.max_weight_position**   | 24.56     |
| **attn.o_proj.min_weight**            | 0.58      |
| **attn.o_proj.min_weight_distance**   | 19.88     |
| **mlp.down_proj.max_weight**          | 0.96      |
| **mlp.down_proj.max_weight_position** | 23.74     |
| **mlp.down_proj.min_weight**          | 0.22      |
| **mlp.down_proj.min_weight_distance** | 17.35     |

## Heretic config used

```yaml
dtypes: "bfloat16"

max_response_length: 384

kl_divergence_scale: 1.0
kl_divergence_target: 0.015

orthogonalize_direction: true

row_normalization: "full"
full_normalization_lora_rank: 3

winsorization_quantile: 0.975

n_trials: 200
n_startup_trials: 40

refusal_markers:
  # defaults plus the following:
   "unsafe",
   "unethical",
   "ethical boundaries",
   "cannot assist",
   "can't assist",
   "not able to",
   "not appropriate",
   "against policies",

system_prompt: "You are a helpful assistant."
```

![image/png](https://huggingface.co/ChiKoi7/Qwen2.5-3B-instruct-medical-finetuned-Heretic/resolve/main/PacMAP_projection_Qwen2.5-3B-instruct-medical-finetuned-Heretic.webp)

---

---

模型经过医疗数据集微调后，已初步具备推理能力，可以进行基础的问诊，且文本的质量BLEU比原模型更优。<br><br>

After fine-tuning on a medical dataset, the model has initially acquired reasoning capabilities and can conduct basic consultations, with the textual quality achieving a better BLEU score than the original model.
