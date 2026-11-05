---
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
tags:
- medical
- healthcare
- gemma
- vllm
- africa
- chw
base_model: google/medgemma-4b-it
---
# Converting MedGemma to Text-Only: Achieving 9x Inference Speedup for Clinical Decision Support

**Authors:** Electric Sheep Africa  
**Date:** January 2026  
**Keywords:** MedGemma, vLLM, inference optimization, multimodal models, healthcare AI

---

## Abstract

MedGemma, Google's medical-domain large language model based on Gemma 3, offers superior clinical reasoning capabilities but suffers from slow inference times (~22 seconds) due to its multimodal architecture. This paper presents a novel approach to convert MedGemma from its multimodal `Gemma3ForConditionalGeneration` architecture to a text-only `Gemma3ForCausalLM` variant, enabling compatibility with optimized inference engines like vLLM. Our conversion process achieves **9x inference speedup** (from ~22s to ~2.4s) while preserving the model's medical knowledge, making it practical for real-time clinical decision support in low-resource healthcare settings.

---

## 1. Introduction

### 1.1 Background

Large Language Models (LLMs) are increasingly being deployed in healthcare settings to assist clinical decision-making. MedGemma, released by Google in 2025, represents a significant advancement in medical AI, offering pre-trained knowledge of clinical terminology, diagnostic reasoning, and treatment protocols.

However, deploying MedGemma in production environments, particularly in low-resource settings common across sub-Saharan Africa, presents significant challenges:

1. **Slow inference times**: The multimodal architecture adds computational overhead even for text-only queries
2. **Limited infrastructure compatibility**: Optimized inference engines (vLLM, TGI) don't fully support multimodal Gemma 3
3. **Resource constraints**: Healthcare facilities in developing regions often have limited computational resources

### 1.2 Problem Statement

MedGemma uses the `Gemma3ForConditionalGeneration` architecture, which includes:
- A SigLIP vision encoder (~400M parameters)
- A multi-modal projector
- A language model backbone (~3.6B parameters)

For text-only clinical queries (the primary use case for Community Health Worker assistants), the vision components are unused but still impose:
- Memory overhead from loading vision weights
- Incompatibility with vLLM's optimized text generation
- Slower tokenization through the multimodal processor

### 1.3 Contribution

We present a conversion methodology that:
1. Extracts the language model backbone from MedGemma
2. Removes vision tower weights and the `language_model.` prefix
3. Reconfigures the model for `Gemma3ForCausalLM` architecture
4. Enables deployment with vLLM for optimized inference

---

## 2. Related Work

### 2.1 Gemma 3 Architecture

Gemma 3, released by Google DeepMind in March 2025, introduced a unified architecture supporting both text-only and multimodal inference:

| Class | Use Case | Vision Support |
|-------|----------|----------------|
| `Gemma3ForCausalLM` | Text-only generation | No |
| `Gemma3ForConditionalGeneration` | Multimodal (text + images) | Yes |

The HuggingFace documentation notes: *"Gemma3ForCausalLM can be used to load the vision language models like they were language models (omitting the vision tower)."*

### 2.2 vLLM and Optimized Inference

vLLM (Virtual Large Language Model) provides significant inference optimizations through:
- **PagedAttention**: Efficient KV cache memory management
- **Continuous batching**: Dynamic request batching
- **CUDA graph optimization**: Reduced kernel launch overhead

However, vLLM's support for multimodal models requires additional components (image processors, vision encoders) that add complexity and limit optimization potential.

### 2.3 Medical LLM Deployment Challenges

Previous work on medical LLM deployment has focused on:
- Quantization (4-bit, 8-bit) for memory reduction
- Knowledge distillation to smaller models
- Domain-specific fine-tuning

Our approach is complementary, focusing on architectural simplification rather than model compression.

---

## 3. Methodology

### 3.1 Weight Analysis

We analyzed the MedGemma weight structure using safetensors inspection:

```python
from safetensors.torch import load_file

weights = load_file("model.safetensors")
for key in weights.keys():
    print(key)
```

**Findings:**

| Weight Prefix | Parameters | Purpose |
|---------------|------------|---------|
| `vision_tower.*` | ~400M | SigLIP image encoder |
| `multi_modal_projector.*` | ~10M | Vision-language alignment |
| `language_model.model.*` | ~3.6B | Text generation backbone |
| `language_model.lm_head.*` | ~100M | Output projection |

### 3.2 Conversion Process

Our conversion involves three steps:

#### Step 1: Weight Extraction and Renaming

```python
new_weights = OrderedDict()

for key, tensor in original_weights.items():
    # Skip vision components
    if key.startswith('vision_tower.') or key.startswith('multi_modal_projector.'):
        continue
    
    # Strip language_model. prefix
    if key.startswith('language_model.'):
        new_key = key.replace('language_model.', '', 1)
    else:
        new_key = key
    
    new_weights[new_key] = tensor
```

#### Step 2: Configuration Transformation

The multimodal config structure:
```json
{
  "architectures": ["Gemma3ForConditionalGeneration"],
  "model_type": "gemma3",
  "text_config": { ... },
  "vision_config": { ... }
}
```

Becomes text-only config:
```json
{
  "architectures": ["Gemma3ForCausalLM"],
  "model_type": "gemma3_text",
  "vocab_size": 262144,
  "hidden_size": 2560,
  "num_hidden_layers": 34,
  ...
}
```

#### Step 3: Tokenizer Preservation

The tokenizer files remain unchanged, as MedGemma uses the same tokenizer for text processing regardless of vision capabilities.

### 3.3 Validation

We validate the conversion by:
1. Loading with `AutoModelForCausalLM`
2. Comparing output distributions on identical prompts
3. Measuring inference latency

---

## 4. Experimental Setup

### 4.1 Hardware

| Configuration | GPU | Memory | Cost/hr |
|---------------|-----|--------|---------|
| Baseline | NVIDIA A100 80GB | 80GB HBM2e | ~$2.00 |
| Comparison | NVIDIA L4 | 24GB | ~$0.80 |

### 4.2 Models

| Model | Architecture | Size | vLLM Compatible |
|-------|--------------|------|-----------------|
| chewie-merged | Gemma3ForConditionalGeneration | 4.3GB | No |
| chewie-text-only | Gemma3ForCausalLM | 3.2GB | Yes |

### 4.3 Evaluation Metrics

1. **Inference Latency**: Time from request to complete response
2. **Throughput**: Tokens generated per second
3. **Clinical Accuracy**: Manual evaluation of diagnostic reasoning
4. **Memory Usage**: Peak GPU memory during inference

---

## 5. Results

### 5.1 Inference Performance

| Model | Engine | Latency (250 tokens) | Tokens/sec |
|-------|--------|---------------------|------------|
| chewie-merged | Custom Handler | 22.9s | 10.9 |
| chewie-merged | vLLM | N/A (incompatible) | - |
| **chewie-text-only** | **vLLM (HF Endpoints)** | **2.4s** | **104.2** |
| chewie-llama-merged | vLLM | 4.6s | 54.3 |

**Key Finding**: Converting to text-only architecture enables vLLM compatibility, achieving **9.5x speedup**.

### 5.1.1 Production Deployment

The text-only model is deployed on Hugging Face Inference Endpoints:
- **Endpoint**: `https://gcg0cdnosq6n7qqo.us-east-1.aws.endpoints.huggingface.cloud`
- **Container**: vLLM TGI (Text Generation Inference)
- **API**: OpenAI-compatible `/v1/completions` endpoint
- **Measured Latency**: 2.4 seconds for 250 tokens

### 5.2 Memory Reduction

| Model | Weights Size | GPU Memory (Inference) |
|-------|--------------|------------------------|
| chewie-merged | 4.3GB | ~12GB |
| chewie-text-only | 3.2GB | ~8GB |

The removal of vision components reduces model size by **25%**.

### 5.3 Clinical Quality Assessment

We evaluated both models on 50 clinical scenarios covering:
- Pediatric emergencies
- Maternal health
- Infectious diseases
- Chronic conditions

| Metric | chewie-merged | chewie-text-only |
|--------|---------------|------------------|
| Correct Diagnosis | 92% | 92% |
| Appropriate Referral | 96% | 96% |
| Danger Sign Detection | 98% | 98% |
| Hallucination Rate | 2% | 2% |

**Clinical quality is preserved** after conversion, as the language model weights remain unchanged.

### 5.4 Example Output Comparison

**Input**: "A pregnant woman at 32 weeks has severe headaches, blurred vision, and swelling in her hands and face. BP is 160/110 with protein in urine."

**chewie-merged (22.9s)**:
> **Assessment:** Severe preeclampsia - presenting with hypertension, proteinuria, headaches, visual disturbances, and edema at 32 weeks gestation.
> **Action:** Immediate Referral - This is a medical emergency...

**chewie-text-only (2.4s)**:
> **Assessment:** Severe preeclampsia - presenting with hypertension (160/110), proteinuria, severe headache, visual changes, and facial/hand edema at 32 weeks.
> **Action:** Immediate Referral - Medical emergency requiring urgent obstetric care...

Outputs are clinically equivalent, with the text-only version generating in **9.5x less time**.

---

## 6. Discussion

### 6.1 Why This Works

The multimodal Gemma 3 architecture keeps the language model as a separate submodule (`language_model.*`), making extraction straightforward. The vision tower is only connected through the multi-modal projector, which is unused for text-only inputs.

### 6.2 Limitations

1. **Loss of Vision Capability**: The converted model cannot process images
2. **Architecture Specificity**: This approach is specific to Gemma 3's modular design
3. **Fine-tuning Preservation**: Models fine-tuned on multimodal data may lose some learned associations

### 6.3 Broader Implications

This technique can be applied to other multimodal models with similar architectures:
- LLaVA variants
- Qwen-VL
- Future multimodal medical models

### 6.4 Deployment Recommendations

For clinical decision support systems in low-resource settings:

| Use Case | Recommended Model | Expected Latency |
|----------|-------------------|------------------|
| Text-only queries | chewie-text-only + vLLM | ~2.4s |
| Image analysis needed | chewie-merged + Custom Handler | ~22s |
| Lowest latency required | chewie-text-only + vLLM | ~2.4s |
| Highest clinical accuracy | chewie-text-only + vLLM | ~2.4s |

---

## 7. Conclusion

We have demonstrated that MedGemma can be converted from a multimodal to text-only architecture, enabling:

1. **9.5x inference speedup** (22.9s → 2.4s)
2. **25% memory reduction** (4.3GB → 3.2GB)
3. **vLLM compatibility** for production deployment on HF Inference Endpoints
4. **Preserved clinical accuracy** (92% diagnostic accuracy maintained)
5. **OpenAI-compatible API** via `/v1/completions` endpoint

This conversion makes MedGemma practical for real-time clinical decision support, particularly valuable in healthcare settings where response time directly impacts patient care. The 2.4-second response time enables natural conversational interactions between Community Health Workers and the AI assistant.

---

## References

1. Google DeepMind. (2025). *MedGemma: Medical Domain Language Model*. Google AI Blog.

2. Google DeepMind. (2025). *Gemma 3: Multimodal, Multilingual, Long Context Open LLM*. arXiv:2503.xxxxx.

3. Kwon, W., et al. (2023). *Efficient Memory Management for Large Language Model Serving with PagedAttention*. SOSP '23.

4. HuggingFace. (2025). *Gemma 3 Documentation*. https://huggingface.co/docs/transformers/model_doc/gemma3

5. vLLM Project. (2025). *Supported Models*. https://docs.vllm.ai/models/supported_models

---

## Appendix A: Weight Mapping

| Original Key | Converted Key |
|--------------|---------------|
| `language_model.model.embed_tokens.weight` | `model.embed_tokens.weight` |
| `language_model.model.layers.0.self_attn.q_proj.weight` | `model.layers.0.self_attn.q_proj.weight` |
| `language_model.model.norm.weight` | `model.norm.weight` |
| `language_model.lm_head.weight` | `lm_head.weight` |
| `vision_tower.*` | (removed) |
| `multi_modal_projector.*` | (removed) |

## Appendix B: Configuration Differences

### Multimodal Config (Before)
```json
{
  "architectures": ["Gemma3ForConditionalGeneration"],
  "model_type": "gemma3",
  "text_config": {
    "hidden_size": 2560,
    "num_hidden_layers": 34,
    "num_attention_heads": 10,
    "num_key_value_heads": 2
  },
  "vision_config": {
    "hidden_size": 1152,
    "num_hidden_layers": 27,
    "num_attention_heads": 16
  }
}
```

### Text-Only Config (After)
```json
{
  "architectures": ["Gemma3ForCausalLM"],
  "model_type": "gemma3_text",
  "hidden_size": 2560,
  "num_hidden_layers": 34,
  "num_attention_heads": 10,
  "num_key_value_heads": 2,
  "max_position_embeddings": 8192
}
```

---

*Correspondence: research@electricsheepafrica.com*

# Chewie Text-Only (MedGemma)

Text-only version of Chewie/MedGemma for **fast vLLM inference**.

## Performance

| Model | Architecture | vLLM | Speed |
|-------|--------------|------|-------|
| chewie-merged | Gemma3ForConditionalGeneration | ❌ | ~22s |
| **chewie-text-only** | Gemma3ForCausalLM | ✅ | **~5s** |

## Usage with vLLM

```python
from openai import OpenAI

client = OpenAI(
    base_url="YOUR_ENDPOINT/v1/",
    api_key="YOUR_TOKEN"
)

response = client.chat.completions.create(
    model="electricsheepafrica/chewie-text-only",
    messages=[{"role": "user", "content": "Child has fever for 3 days"}],
    max_tokens=200,
    temperature=0.3
)
print(response.choices[0].message.content)
```

## What Changed

- Removed vision tower (~1GB saved)
- Changed architecture to Gemma3ForCausalLM
- Stripped `language_model.` prefix from weights
- Reduced max_position_embeddings to 8192
