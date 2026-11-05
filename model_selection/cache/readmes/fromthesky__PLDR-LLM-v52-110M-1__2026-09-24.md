---
language:
- en
tags:
- text-generation
- large-language-model
- power-law-decoder-representations
- power-law-graph-attention
- pldr-llm
- kv-cache
- g-cache
- kvg-cache
- pytorch
license: apache-2.0
datasets:
- tiiuae/falcon-refinedweb
pipeline_tag: text-generation
library_name: transformers
---

# PLDR-LLM-v52-110M-1

## Model Description

PLDR-LLM-v52-110M-1 is a large language model from power law decoder representations with KV-cache and G-cache support, which is a new foundational language model architecture that utilizes power law graph attention to generate deductive and inductive outputs. This model has a parameter size of 110M. It is similar to PLDRv51-110M-1 whose architecture and training details are provided in Table 1 of the research paper titled [PLDR-LLMs Learn A Generalizable Tensor Operator That Can Replace Its Own Deep Neural Net At Inference](https://arxiv.org/abs/2502.13502). 
- The difference for PLDR-LLM-v52-* models from PLDR-LLM-v51-* is that the rotary positional embedding (RoPE) implementation uses the GPT-NeoX style approach that is also used for Llama in Huggingface Transformers library. GPT-NeoX style approach is where half of the hidden dims are rotated instead of GPT-J style RoPE implementation which rotates every-other-two hidden dims. This approach makes the PLDR-LLM implementation more compatible with rest of the transformers library.
- GPT-J style approach is the approach that was also used in the [original implementation of PLDR-LLM](https://github.com/burcgokden/PLDR-LLM-with-KVG-cache) as well as the official implementation of Llama. More details can be found [here](https://github.com/huggingface/transformers/issues/25199). The paper introducing rotary positional embeddings can be found [here](https://arxiv.org/abs/2104.09864).

## Training data

PLDR-LLM-v52-110M-1 was pretrained on the [RefinedWeb](https://huggingface.co/datasets/tiiuae/falcon-refinedweb), a publicly available English web dataset with extensive filtering and deduplication. 

## Training procedure

This model was trained for ~8B tokens on RefinedWeb over 250k steps per rank. It was trained  autoregressively with cross-entropy loss. This model was trained with the custom model implementation of PLDR-LLM for the Huggingface Transformers library. Training parameters were similar to PLDRv51-110M-1 from [research paper](https://arxiv.org/abs/2502.13502). Learning rate and number of warm-up steps were set at 1.2x10<sup>-3</sup> and 2000.

## Intended Use and Limitations

This model is intended to be used for research purposes. Given text as input prompt, it carries out next token prediction to generate continuation text. The context length for this model is 1024 tokens. 

## How to Use

### Via Huggingface Transformers Library

PLDR-LLM has custom model support for Huggingface Transformers library. PLDR-LLM with custom code is evaluated on Transformers 4.56.1 available at the time.

Using `pipeline`:
```python
from transformers import pipeline

text_generator = pipeline(
                          task="text-generation",
                          model="fromthesky/PLDR-LLM-v52-110M-1",
                          device="cuda", # or "cpu"
                          trust_remote_code=True
                         )

prompt="The quick brown fox jumps over the lazy dog."

output=text_generator(prompt, top_p=0.6, top_k=0, temperature=1, do_sample=True,               
                      tokenizer_encode_kwargs={"add_special_tokens":False}, 
                      use_cache=True, max_new_tokens=100)
print(output[0]["generated_text"])
```

Using `AutoModel`:
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
device="cuda" # or "cpu"
model=AutoModelForCausalLM.from_pretrained(pretrained_model_name_or_path="fromthesky/PLDR-LLM-v52-110M-1",
                                           device_map=device,
                                           trust_remote_code=True
                                          )
tokenizer=AutoTokenizer.from_pretrained(pretrained_model_name_or_path="fromthesky/PLDR-LLM-v52-110M-1",
                                        add_eos_token=False,
                                        legacy=False,
                                        trust_remote_code=True
                                       )
                                       
prompt="The quick brown fox jumps over the lazy dog."
        
inputs = tokenizer([prompt], return_tensors="pt").to(device=device)
generated_ids = model.generate(**inputs,
                               max_new_tokens=100, 
                               top_p=0.6,
                               top_k=0, 
                               temperature=1, 
                               do_sample=True,
                               use_cache=True
                              )
print(tokenizer.decode(generated_ids[0], skip_special_tokens=True))
```

#### PLDR-LLM specific configurations:
- `custom_G_type`: `None` for learned G values during pretraining, `'identity'` for LLM with SDPA equivalent, `'random'` for G values from a random normal distribution, `'external'` for custom G values that can be assigned after model initialization. This setting is more important for training purposes, for inference it is set in the model config.json file.

- `cache_first_G`: For batched inference, if set to `True`, cache G values from the first sample prompt in batch for all samples. If set to `False`, cache G values separately for each sample prompts in batch. For contrastive generation with `custom_G_value=None`, this needs to be set to `True`.

- `reference_rope`: If set to `True`, RoPE implementation implemented in the original paper is used. This is the case for model pretrained in this repo. If set to `False`, RoPE implementation from the Huggingface Transformers library is used.

- `output_pldr_attentions=True` returns the deductive outputs and learnable parameters of power law graph attention module as tuple containing:
the output of the residual metric learner (metric tensor, **A**), output (**A<sub>LM</sub>**) after application of iSwiGLU on metric tensor, learned exponents of potential tensor, learned weights for energy-curvature tensor, learned bias for energy-curvature tensor, energy-curvature tensor (**G<sub>LM</sub>**), and attention weights.

See config.json for other model configuration details.

#### Notes:
- This implementation of PLDR-LLM custom code was evaluated on Transformers 4.56.1 and pytorch 2.6.0.
- We also have a fork of transformers library with PLDR-LLM model support for future development. The PLDR-LLM model files are added to the library so custom model files are not necessary. 
```python
      git clone https://github.com/burcgokden/transformers
      cd transformers
      git checkout add_PLDR_LLM
      pip install -e ".[dev]"
```
- Static cache is not supported for models with `custom_G_type=None`.
- PLDR-LLM uses EOS token `"[END]"` during pretraining to indicate end of a sequence. For text generation, we do not need to add the EOS token to the prompt. To achieve this, `add_eos_token=False` can be set in `tokenizer_config.json` file or while initializing the tokenizer model. For text generation `pipeline` call method, `tokenizer_encode_kwargs={"add_special_tokens":False}` can be used.
- When `add_bos_token=False` and `add_eos_token=False` are set for the tokenizer model, prompt `""` is an invalid input for single batch inference as it doesn't contain any tokens. When padding is enabled, batched inference with prompt `""` as one of the samples causes its `input_ids` to be pad tokens and `attention_mask` to be all zeros. This edge case is handled differently for `_attn_implementation='eager'` and `'sdpa'`, resulting in different generation outputs for this prompt. Setting `add_bos_token=True`, `add_eos_token=True` or explicitly providing prompt as `"[PAD]"`, `"[START]"`, or `"[END]"` gives same output for either implementation. This issue does not affect KV-cache and G-cache.

### LM Evaluation Harness Support

- The model can be used with a fork of LM-Evaluation-Harness Suite with PLDR-LLM with KV-cache and G-cache support: [lm-evaluation-harness-with-PLDR-LLM-kvg-cache](https://github.com/burcgokden/lm-evaluation-harness-with-PLDR-LLM-kvg-cache).

### Limitations and Biases

Large Language Models may generate text that is profane, lewd, socially unacceptable or offensive based on the contents of the dataset it was pretrained. RefinedWeb is a dataset that is as toxic and biased as the Pile. Please see the papers for [RefinedWeb](https://arxiv.org/abs/2306.01116) and [the Pile](https://arxiv.org/pdf/2101.00027) for more information. Moreover, large language models are also susceptible to hallucinations and may generate text that contains incorrect, irrelevant or misleading information. Since it is very hard to expect the contents of generated text ahead of time, the output of the large language models need to be heavily moderated and curated to avoid undesired content to appear without warning.

## Eval results
- The model is evaluated on benchmarks with zero-shot setting in a similar way that was presented in [research paper](https://arxiv.org/abs/2502.13502)

|Benchmark | Score |
|-------------------|--------|
| ARC-c             |22.53|
| ARC-e             |36.49|
| Hellaswag         |29.20|
| OpenBookQA        |27.00|
| PIQA              |63.00|
| SIQA              |41.81|
| Winogrande        |49.96|
| Average-1         |38.19|
| TruthfulQA        |45.00|
| Average-2         |38.95|



### BibTeX entry and citation info

Please cite this model as:

```bibtex
@misc{gokden2025pldrllmkvgcache,
      title={PLDR-LLMs Learn A Generalizable Tensor Operator That Can Replace Its Own Deep Neural Net At Inference}, 
      author={Burc Gokden},
      year={2025},
      eprint={2502.13502},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2502.13502}, 
}

@misc{gokden2024pldrllm,
      title={PLDR-LLM: Large Language Model from Power Law Decoder Representations}, 
      author={Burc Gokden},
      year={2024},
      eprint={2410.16703},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2410.16703}, 
}
```
