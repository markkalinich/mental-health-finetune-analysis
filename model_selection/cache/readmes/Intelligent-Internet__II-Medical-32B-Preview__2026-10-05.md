---
license: apache-2.0
---

# II-Medical-32B-Preview


![image/png](https://cdn-uploads.huggingface.co/production/uploads/63466107f7bd6326925fc770/6R3uJGH1MKGSZt9F88Gvc.png)

## I. Model Overview

II-Medical-32B-Preview is the latest advanced large language model developed by Intelligent Internet, specifically designed to enhance AI-driven medical reasoning. As our first 32B-scale model version, it significantly advances the capabilities of medical question answering.

## II. Training Methodology

We collected and generated a comprehensive set of reasoning datasets for the medical domain and performed SFT fine-tuning on the [Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B) model. 

For the hyperparameter: 
- Max Length: 16378.
- Batch Size: 128.
- Learning-Rate: 2e-5.
- Number Of Epoch: 4.

## III. Evaluation Results


![image/png](https://cdn-uploads.huggingface.co/production/uploads/63466107f7bd6326925fc770/nfyIuAiaBLKZ1cesLN1te.png)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/63466107f7bd6326925fc770/4S65RIgYgOk7GjtsRs0vM.png)

We evaluated on 10 medical QA benchmarks including MedMCQA, MedQA, PubMedQA, HealthBench, medical related questions from MMLU-Pro, small QA sets from Lancet and the New England
Journal of Medicine,  4 Options  and 5 Options splits from the MedBullets platform and MedXpertQA.

| Model                   | MedMC | MedQA | PubMed | MMLU-P | HealthBench | Lancet | MedB-4 | MedB-5 | MedX  | NEJM  | Avg   |
|--------------------------|-------|-------|--------|--------|------|--------|--------|--------|------|-------|-------|
| [HuatuoGPT-o1-72B](https://huggingface.co/FreedomIntelligence/HuatuoGPT-o1-72B)         | 76.76 | 88.85 | 79.90   | 80.46  | 22.73 | 70.87   | 77.27  | 73.05  |23.53 |76.29  | 66.97 |
| [M1](https://huggingface.co/UCSC-VLAA/m1-7B-23K)                     | 62.54 | 75.81 | 75.80  | 65.86  | 15.51 | 62.62  | 63.64  | 59.74  |19.59 |64.34  | 56.55  |
| [Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B)                  | 66.53 | 81.38 | 73.9   | 77.85  | 42.27 | 66.26   | 68.83  | 62.66  |19.59 |69.65  | 62.89 |
| [Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B)                  | 74.18 | 88.92 | 76.1   | 80.7  | 47.08 | 72.33   | 72.27  | 71.42  |28.04 |76.94  | 68.80 |
| [MedGemma-27B-IT](https://huggingface.co/google/medgemma-27b-text-it)                  | 73.24 | 87.27 | 70.9   | 80.13  | 46.54| 70.14   | 75.32  | 73.37  |25.55 |76.28  | 67.87 |
| [II-Medical-8B](https://huggingface.co/Intelligent-Internet/II-Medical-8B)        | 71.57 | 87.90 | 78.7   |80.46  | 40.02| 70.38  | 78.25  | 72.07  |25.26 |73.13  |67.77  |
| [II-Medical-8B-1706](https://huggingface.co/Intelligent-Internet/II-Medical-8B-1706)            | 74.44 | 88.61 | 79.8   | 81.04  | 46.8 | 71.60  | 80.84  | 74.67  |29.63 |77.61  | 70.47  |
| [II-Medical-32B-Preview](https://huggingface.co/Intelligent-Internet/II-Medical-32B-Preview)            | 75.16 | 90.02 | 79.1   | 80.71  | 47.24 | 75.48  | 81.16  | 74.68  |31.42 | 80.43  | **71.54**  |

## IV. Dataset Release


More importantly, besides the II-Medical-32B-Preview, we also release the training datasets of our SFT/Preview II-Medical and also our RL dataset.

- [II-Medical-Reasoning-SFT](https://huggingface.co/datasets/Intelligent-Internet/II-Medical-Reasoning-SFT)
- [II-Medical-RL-MedReason](https://huggingface.co/datasets/Intelligent-Internet/II-Medical-RL)
- [II-Medical-RL-ChatDoctor](https://huggingface.co/datasets/Intelligent-Internet/ChatDoctor-RL)


We believe this work will be valuable resource for the community and contributes to the advancement of medical reasoning capabilities in AI systems.

## V. How To Use
Our model can be utilized in the same manner as Qwen or Deepseek-R1-Distill models.

For instance, you can easily start a service using [vLLM](https://github.com/vllm-project/vllm):

```bash
vllm serve Intelligent-Internet/II-Medical-32B-Preview
```

You can also easily start a service using [SGLang](https://github.com/sgl-project/sglang):

```bash
python -m sglang.launch_server --model Intelligent-Internet/II-Medical-32B-Preview
```

## VI. Usage Guidelines

- Recommended Sampling Parameters: temperature = 0.6, top_p = 0.9
- When using, explicitly request step-by-step reasoning and format the final answer within \boxed{} (e.g., "Please reason step-by-step, and put your final answer within \boxed{}.").

## VII. Limitations and Considerations

- Dataset may contain inherent biases from source materials
- Medical knowledge requires regular updates
- Please note that **It’s not suitable for medical use.**


## VIII. Citation

```bib
@misc{2025II-Medical-32B-Preview,
      title={II-Medical-32B-Preview: Medical Reasoning Model}, 
      author={Intelligent Internet},
      year={2025}
}
```