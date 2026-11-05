---
library_name: transformers
license: cc-by-4.0
base_model: Qwen/Qwen3.5-4B-Base
language:
  - af  # Afrikaans
  - am  # Amharic
  - ar  # Arabic
  - en  # English
  - fr  # French
  - ha  # Hausa
  - ig  # Igbo
  - mg  # Malagasy (Plateau)
  - ny  # Nyanja
  - om  # Oromo
  - pt  # Portuguese
  - rw  # Kinyarwanda
  - sn  # Shona
  - so  # Somali
  - st  # Southern Sotho
  - sw  # Swahili
  - ti  # Tigrinya
  - tn  # Tswana
  - xh  # Xhosa
  - yo  # Yoruba
  - zu  # Zulu
pipeline_tag: text-generation
tags:
  - african-languages
  - multilingual
  - continued-pretraining
  - afrique-llm
  - qwen3_5
  - image-text-to-text
  - llamafactory
---

# AfriqueQwen3.5-4B

## Model Overview

**AfriqueQwen3.5-4B** is part of the **AfriqueLLM** suite, a collection of open language models adapted to **20 African languages** through continued pre-training (CPT) on **~26B tokens**. This model is based on [Qwen/Qwen3.5-4B-Base](https://huggingface.co/Qwen/Qwen3.5-4B-Base) and has been specifically adapted for improved performance on African languages while maintaining strong capabilities in high-resource languages.


Our experiments show that **Qwen 3.5 models** provide an excellent balance of multimodal capabilities and multilingual performance.

### Key Features

- **Type**: Causal Language Model (Base/Pre-trained)
- **Base Model**: Qwen 3.5 4B
- **Parameters**: 4B
- **Context Length**: 32,768 tokens (native)
- **Training Tokens**: ~26B tokens of carefully curated multilingual data

## Supported Languages

AfriqueQwen3.5-4B has been adapted for the following 20 African languages:

| Language | Code | Family | Script |
|----------|------|--------|--------|
| Afrikaans | afr_Latn | Germanic | Latin |
| Swahili | swh_Latn | Bantu | Latin |
| Moroccan Arabic | ary_Arab | Semitic | Arabic |
| Somali | som_Latn | Cushitic | Latin |
| Amharic | amh_Ethi | Semitic | Ethiopic |
| Egyptian Arabic | arz_Arab | Semitic | Arabic |
| Hausa | hau_Latn | Chadic | Latin |
| Kinyarwanda | kin_Latn | Bantu | Latin |
| Zulu | zul_Latn | Bantu | Latin |
| Igbo | ibo_Latn | Volta-Niger | Latin |
| Plateau Malagasy | plt_Latn | Austronesian | Latin |
| Xhosa | xho_Latn | Bantu | Latin |
| Shona | sna_Latn | Bantu | Latin |
| Yoruba | yor_Latn | Volta-Niger | Latin |
| Nyanja | nya_Latn | Bantu | Latin |
| Southern Sotho | sot_Latn | Bantu | Latin |
| Tigrinya | tir_Ethi | Semitic | Ethiopic |
| Tunisian Arabic | aeb_Arab | Semitic | Arabic |
| Oromo | gaz_Latn | Cushitic | Latin |
| Tswana | tsn_Latn | Bantu | Latin |

**High-resource languages used for catastrophic forgetting mitigation:** English, French, Portuguese, Arabic

## Training Data

Our training corpus combines multiple high-quality sources:

- **African Monolingual Data** (~22.8B tokens): FineWeb2, WURA, and MADLAD-400
- **Code** (~1B tokens): CornStack-Python for reasoning capabilities
- **Mathematics** (~1B tokens): FineMath-4+ for mathematical understanding
- **Synthetic Data** (~324M tokens): GPT-4.1 translated domain-specific content across 10 domains


We use **UniMax sampling** to create a balanced distribution, capping high-resource languages at approximately 1B tokens and upsampling lower-resource languages for up to five epochs.

## Quickstart

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "McGill-NLP/AfriqueQwen3.5-4B"

# Load the tokenizer and the model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

# Prepare the model input
prompt = "Bawo ni o ṣe n ṣe?"  # Yoruba: "How are you doing?"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

# Generate text
generated_ids = model.generate(
    **inputs,
    max_new_tokens=100,
)
output = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
print(output)
```

## Deployment

For deployment, you can use `vllm` or `sglang` to create an OpenAI-compatible API endpoint:

**vLLM:**
```shell
vllm serve McGill-NLP/AfriqueQwen3.5-4B
```

**SGLang:**
```shell
python -m sglang.launch_server --model-path McGill-NLP/AfriqueQwen3.5-4B
```

## Training Details

### Hyperparameters

- **Learning Rate**: 5e-5 (with warmup and cosine decay)
- **Context Length**: 16,384 tokens
- **Optimizer**: AdamW
- **Precision**: BF16 mixed precision

### Infrastructure

Training was conducted using the LLaMA-Factory framework on up to 64 NVIDIA H100 GPUs with:
- DeepSpeed ZeRO-1/ZeRO-2
- Flash Attention 3
- Sequence packing
- Liger Kernel optimizations

## Evaluation

All AfriqueLLM models are evaluated on multiple multilingual benchmarks. FLORES is reported only in the English-to-target direction (`eng->xxx`):

| Model | AfriMGSM | AfriMMLU | AfriXNLI | Belebele | FLORES (eng->xxx) | INJONG | SIB-200 | Overall | Δ (Δ %) |
|-------|----------|----------|----------|----------|--------|--------|---------|---------|---|
| [Gemma3-4B](https://huggingface.co/google/gemma-3-4b-pt) | 10.24 | 33.89 | 37.76 | 45.79 | 35.36 | 55.52 | 63.59 | 40.31 | |
| [AfriqueGemma-4B](https://huggingface.co/McGill-NLP/AfriqueGemma-4B) | 14.86 | 36.73 | 39.62 | 50.52 | 54.95 | 69.28 | 69.21 | 47.88 | +7.6 (18.8%) |
| [Gemma3-12B](https://huggingface.co/google/gemma-3-12b-pt) | 25.21 | 48.76 | 44.01 | 68.84 | 44.09 | 73.53 | 79.17 | 54.80 | |
| [AfriqueGemma-12B](https://huggingface.co/McGill-NLP/AfriqueGemma-12B) | 32.14 | 49.47 | 44.60 | 68.65 | 65.04 | 76.79 | 75.08 | 58.82 | +4.0 (7.3%) |
| [Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B-Base) | 8.26 | 33.84 | 37.12 | 41.50 | 20.16 | 21.69 | 57.88 | 31.49 | |
| [AfriqueQwen-4B](https://huggingface.co/McGill-NLP/AfriqueQwen-4B) | 33.09 | 43.04 | 44.88 | 63.62 | 59.82 | 65.34 | 74.77 | 54.94 | +23.4 (74.4%) |
| [Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B-Base) | 20.79 | 38.63 | 40.36 | 55.82 | 32.06 | 59.43 | 74.96 | 46.01 | |
| <u>[AfriqueQwen3.5-4B](https://huggingface.co/McGill-NLP/AfriqueQwen3.5-4B)</u> | <u>30.47</u> | <u>43.66</u> | <u>41.05</u> | <u>66.01</u> | <u>63.55</u> | <u>75.46</u> | <u>79.66</u> | <u>57.12</u> | <u>+11.1 (24.2%)</u> |
| [AfriqueQwen3.5-4B-ExtendedCM](https://huggingface.co/McGill-NLP/AfriqueQwen3.5-4B-ExtendedCM) | 34.17 | 45.26 | 41.94 | 66.45 | 63.76 | 75.97 | 80.52 | 58.30 | +1.2 (2.1%) |
| [AfriqueQwen3.5-4B-50Langs](https://huggingface.co/McGill-NLP/AfriqueQwen3.5-4B-50Langs) | 34.06 | 45.23 | 41.79 | 66.83 | 64.56 | 75.82 | 79.83 | 58.30 | +0.0 (0.0%) |
| [Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B-Base) | 11.22 | 36.56 | 38.24 | 44.63 | 21.13 | 29.47 | 53.06 | 33.47 | |
| [AfriqueQwen-8B](https://huggingface.co/McGill-NLP/AfriqueQwen-8B) | 39.68 | 46.91 | 45.99 | 68.46 | 62.18 | 73.36 | 77.00 | 59.08 | +25.6 (76.5%) |
| [Qwen3-14B](https://huggingface.co/Qwen/Qwen3-14B-Base) | 16.60 | 39.66 | 43.22 | 50.74 | 23.61 | 41.80 | 66.29 | 40.27 | |
| **[AfriqueQwen-14B](https://huggingface.co/McGill-NLP/AfriqueQwen-14B)** | **45.01** | **52.22** | **49.01** | **74.63** | **63.77** | **77.80** | **82.63** | **63.58** | **+23.3 (57.9%)** |
| [Llama3.1-8B](https://huggingface.co/meta-llama/Llama-3.1-8B) | 8.14 | 32.27 | 37.90 | 40.95 | 26.69 | 41.37 | 59.99 | 35.33 | |
| [AfriqueLlama-8B](https://huggingface.co/McGill-NLP/AfriqueLlama-8B) | 17.51 | 36.57 | 37.39 | 50.51 | 63.60 | 71.17 | 69.14 | 49.41 | +14.1 (39.9%) |
| [Lugha-Llama-8B-wura](https://huggingface.co/Lugha/Meta-Llama-3.1-8B-wura) | 9.46 | 37.00 | 39.24 | 47.86 | 49.90 | 62.30 | 75.81 | 45.94 | |
| [Gemma3-27B](https://huggingface.co/google/gemma-3-27b-pt) | 35.37 | 55.47 | 46.85 | 74.81 | 48.41 | 79.70 | 84.34 | 60.71 | |

### Additional-Language Evaluation

This table averages only evaluated African languages outside the first 20-language CPT set: Ewe, Lingala, Ganda, Twi, and Wolof. Benchmark cells average the available languages for that benchmark; FLORES is English-to-target only (`eng->xxx`).

| Model | AfriMGSM | AfriMMLU | AfriXNLI | Belebele | FLORES (eng->xxx) | INJONG | SIB-200 | Avg | Δ (Δ %) |
|-------|----------|----------|----------|----------|-------------------|--------|---------|-----|--------|
| [Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B-Base) | 8.30 | 32.35 | 34.30 | 36.90 | 22.20 | 33.27 | 58.96 | 32.33 | |
| <u>[AfriqueQwen3.5-4B](https://huggingface.co/McGill-NLP/AfriqueQwen3.5-4B)</u> | <u>7.52</u> | <u>31.17</u> | <u>33.56</u> | <u>35.82</u> | <u>26.28</u> | <u>33.10</u> | <u>56.66</u> | <u>32.02</u> | <u>-0.31 (-1.0%)</u> |
| [AfriqueQwen3.5-4B-ExtendedCM](https://huggingface.co/McGill-NLP/AfriqueQwen3.5-4B-ExtendedCM) | 8.13 | 32.72 | 33.74 | 36.76 | 24.06 | 32.41 | 56.00 | 31.97 | -0.05 (-0.2%) |
| [AfriqueQwen3.5-4B-50Langs](https://huggingface.co/McGill-NLP/AfriqueQwen3.5-4B-50Langs) | 21.07 | 37.65 | 36.31 | 51.56 | 56.33 | 61.37 | 75.75 | 48.58 | +16.61 (+52.0%) |

## Model Variants

- [AfriqueQwen-14B](https://huggingface.co/McGill-NLP/AfriqueQwen-14B) - Qwen-based 14B model (flagship)
- [AfriqueQwen-8B](https://huggingface.co/McGill-NLP/AfriqueQwen-8B) - Qwen-based 8B model
- [AfriqueQwen-4B](https://huggingface.co/McGill-NLP/AfriqueQwen-4B) - Qwen-based 4B model
- [AfriqueQwen3.5-4B-ExtendedCM](https://huggingface.co/McGill-NLP/AfriqueQwen3.5-4B-ExtendedCM) - Qwen 3.5-based 4B model with extended continued pre-training
- [AfriqueQwen3.5-4B-50Langs](https://huggingface.co/McGill-NLP/AfriqueQwen3.5-4B-50Langs) - Qwen 3.5-based 4B model with 50-language coverage
- [AfriqueGemma-4B](https://huggingface.co/McGill-NLP/AfriqueGemma-4B) - Gemma-based 4B model
- [AfriqueGemma-12B](https://huggingface.co/McGill-NLP/AfriqueGemma-12B) - Gemma-based 12B model
- [AfriqueLlama-8B](https://huggingface.co/McGill-NLP/AfriqueLlama-8B) - Llama-based 8B model

## Citation

If you find our work helpful, please cite:

```bibtex
@misc{yu2026afriquellmdatamixingmodel,
      title={AfriqueLLM: How Data Mixing and Model Architecture Impact Continued Pre-training for African Languages}, 
      author={Hao Yu and Tianyi Xu and Michael A. Hedderich and Wassim Hamidouche and Syed Waqas Zamir and David Ifeoluwa Adelani},
      year={2026},
      eprint={2601.06395},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2601.06395}, 
}
```

## License

This model is released under the [CC BY 4.0 License](https://creativecommons.org/licenses/by/4.0/). Please review the license terms before use.

## Acknowledgments

We thank the creators of the base models, datasets and compute resources that made this work possible, including Mila, Compute Canada, Microsoft, the FineWeb team, WURA, MADLAD-400 and etc..
