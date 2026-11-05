---
license: other
license_name: qwen
license_link: https://huggingface.co/Qwen/Qwen2.5-72B/raw/main/LICENSE
library_name: transformers
language:
- en
tags:
- chat
- conversational
base_model:
- Qwen/Qwen2.5-72B
- moonshotai/Kimi-Dev-72B
- pfnet/Preferred-MedLLM-Qwen-72B
- Sao10K/72B-Qwen2.5-Kunou-v1
pipeline_tags:
- text-generation
- conversational
- chat

---

![image/png](https://cdn-uploads.huggingface.co/production/uploads/65b19c1b098c85365af5a83e/x_ReJjZMZEy-6vylDyvzI.png)

[GGUF](https://huggingface.co/mradermacher/Doctor-Kunou-72b-GGUF) [iMat](https://huggingface.co/mradermacher/Doctor-Kunou-72b-i1-GGUF)

# Doctor Kunou 72B

Doctor Kunou 72B is a *normalized denoised fourier interpolation* of the following models:

```yaml
output_base_model: "Qwen/Qwen2.5-72B"
output_dtype: "bfloat16"
finetune_merge:
  - { "model": "moonshotai/Kimi-Dev-72B", "base": "Qwen/Qwen2.5-72B", "alpha": 0.9, "is_input": true }
  - { "model": "pfnet/Preferred-MedLLM-Qwen-72B", "base": "Qwen/Qwen2.5-72B", "alpha": 0.4 }
  - { "model": "Sao10K/72B-Qwen2.5-Kunou-v1", "base": "Qwen/Qwen2.5-72B", "alpha": 0.9, "is_output": true }
```

In other words, all of these models get warped and interpolated in signal space, and then jammed back on top of the base model (which in this case was Qwen2.5-72B); with the Kimi-Dev-72B input layer and the Kunou-v1 (Instruct-based) output layer.

## Is it good?

It is very coherent. I think it successfully combines as Kunou's creativity with some better prompt following and just a dash of deep domain medical knowledge.

## Citation

If you find our work helpful, feel free to give us a cite.

```
@misc{doctor-kunou-72b,
    title = {Doctor Kunou 72B},
    url = {https://huggingface.co/maldv/Doctor-Kunou-72B},
    author = {Praxis Maldevide},
    month = {July},
    year = {2025}
}
```