---
base_model: google/gemma-3-270m-it
library_name: peft
pipeline_tag: text-generation
tags:
- base_model:adapter:google/gemma-3-270m-it
- lora
- transformers
- survival
- marketing
- psychology
- warfare
- stoicism
- history
- roleplay
- personas
- conversation
- micromodels
license: mit
---
# Uncensored-Q-270M-v2


![image/png](https://cdn-uploads.huggingface.co/production/uploads/673e6f4363db0f5cbef37315/kU1Qu2PoN1ubXRJpQac2-.png)

Uncensored-Q-270M-v2 is a fine-tuned version of google/gemma-3-270m-it, featuring 268 million parameters. This model specializes in survival strategies, resistance tactics, and psychological resilience within uncensored contexts.



## Model Overview
- **Base Model**: google/gemma-3-270m-it
- **Parameters**: 268 million
- **Languages**: Primarily English, with support for over 140 languages
- **License**: Gemma Terms of Use
- **Author**: pixasocial
- **Fine-Tuning**: Hugging Face Transformers and TRL/SFTTrainer on an expanded curated dataset of ~200,000 examples across survival, resistance, psychology, and related themes
- **Hardware**: NVIDIA A40 GPU
- **SFT Training Time**: ~10 hours
- **Next Steps**: PPO training planned

## Intended Uses
- **Primary**: Advice on survival, resistance, psychological coping
- **Secondary**: Offline mobile deployment for emergencies
- **Not for harmful/illegal use; validate outputs**

## Offline Usage
The model supports GGUF format for deployment on various platforms, including Android/iOS via apps like MLC Chat or Ollama. The Q4_K_M variant (253 MB) is suitable for devices with 4GB+ RAM. Detailed instructions follow for Ollama, mobile phones, and desktops.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/673e6f4363db0f5cbef37315/8uCflkzTCEDNLY418NUTC.png)

### Quantization Explanations
Quantization reduces model precision to optimize size and inference speed while maintaining functionality. Below is a table of available GGUF variants with precise file sizes from the repository, along with recommended use cases:

| Quantization Type | File Size | Recommended Hardware | Accuracy vs. Speed Trade-off |
|-------------------|-----------|-----------------------|------------------------------|
| f16 (base)       | 543 MB   | High-end desktops/GPUs | Highest accuracy, larger size, suitable for precise tasks |
| Q8_0             | 292 MB   | Desktops with 8GB+ RAM | High accuracy, moderate size and speed |
| Q6_K             | 283 MB   | Laptops/mid-range desktops | Good balance, minor accuracy loss |
| Q5_K_M           | 260 MB   | Mobile desktops/low-end GPUs | Efficient, slight reduction in quality |
| Q5_K_S           | 258 MB   | Mobile desktops | Similar to Q5_K_M but optimized for smaller footprints |
| Q4_K_M           | 253 MB   | Smartphones (4GB+ RAM) | Fast inference, acceptable accuracy for mobile |
| Q4_K_S           | 250 MB   | Smartphones/edge devices | Faster than Q4_K_M, more compression |
| Q3_K_L           | 246 MB   | Low-RAM devices | Higher compression, noticeable quality drop |
| Q3_K_M           | 242 MB   | Edge devices | Balanced 3-bit, for constrained environments |
| Q3_K_S           | 237 MB   | Very low-resource devices | Maximum compression at 3-bit, prioritized speed |
| IQ4_XS           | 241 MB   | Smartphones/hybrids | Intelligent quantization, efficient with preserved performance |
| Q2_K             | 237 MB   | Minimal hardware | Smallest size, fastest but lowest accuracy |

Select based on device constraints: higher-bit variants for accuracy, lower for portability.

Here is a handy graph by ikawrakow comparing some lower-quality quant types (lower is better):

![image/png](https://cdn-uploads.huggingface.co/production/uploads/673e6f4363db0f5cbef37315/EC-Ivxg9uBW4KLIVBcN1s.png)

And here are Artefact2's thoughts on the matter: https://gist.github.com/Artefact2/b5f810600771265fc1e39442288e8ec9

### Deployment on Ollama
Ollama facilitates local GGUF model execution on desktops.

1. Install Ollama from ollama.com.
2. Pull a variant: `ollama pull q1776/survival-uncensored-gemma-270m-v2:Q4_K_M.gguf`.
3. Run: `ollama run q1776/survival-uncensored-gemma-270m-v2:Q4_K_M.gguf`.
4. Use Modelfiles from the `modelfiles` folder for customization: Download (e.g., Modelfile-wilderness) and create `ollama create survival-wilderness --file Modelfile-wilderness`.

### Deployment on Phone
For Android/iOS:

1. **MLC Chat**: Download from mlc.ai. Import GGUF (e.g., Q4_K_M, 253 MB) and query offline. Requires 4GB RAM; expect 5-10 tokens/second.
2. **Termux (Android)**: Install Termux, then Ollama. Pull and run as above.
3. iOS: Use Ollama-compatible apps or simulators; native options limited.

### Deployment on Desktop
1. **LM Studio**: From lmstudio.ai; import GGUF and use UI.
2. **vLLM**: `pip install vllm`; serve with `python -m vllm.entrypoints.openai.api_server --model q1776/survival-uncensored-gemma-270m-v2:Q4_K_M.gguf --port 8000`.

## Training Parameters
- Epochs: 5
- Batch Size: 4 per device, effective 16
- Learning Rate: 1e-5
- Optimizer: AdamW
- Weight Decay: 0.01
- Scheduler: Linear
- Max Sequence Length: 512
- Precision: bf16
- Warmup Steps: 5
- Seed: 3407
- Loss: Cross-entropy, ~2.0 to <1.5

## Performance Benchmarks
Improved on specialized queries. Scores (/10):

- Survival Advice: 9.5
- Resistance Tactics: 9.0
- Psychology Insights: 9.2

Inference Speed Graph (tokens/second, approximate):

| Hardware       | Q8_0 | Q4_K_M | Q2_K |
|----------------|------|--------|------|
| NVIDIA A40    | 25   | 35     | 45   |
| Desktop GPU   | 15   | 25     | 35   |
| Smartphone    | N/A  | 8      | 12   |

## Technical Documentation
Transformer-based, multimodal (text+images, 896x896). Context: 32K tokens. Deploy via vLLM or RunPod.

## Ethical Considerations
Uncensored; may generate controversial content. User responsibility. Limitations: Hallucinations on obscure topics. Impact: ~10 kWh energy.

## Export Guide
Convert to GGUF for Ollama, vLLM for inference, RunPod for API.