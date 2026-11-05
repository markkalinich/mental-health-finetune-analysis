---
library_name: transformers
license: apache-2.0
language:
- en
- fr
- de
- es
- zh
- it
- ru
- pl
- pt
- ja
- vi
- nl
- ar
- tr
- hi
pipeline_tag: fill-mask
tags:
- code
---

# EuroBERT-610m
<div>
  <img src="img/banner.png" width="100%"  alt="EuroBERT" />
</div>

## Table of Contents
1. [Overview](#overview)
2. [Usage](#Usage)
3. [Evaluation](#Evaluation)
4. [License](#license)
5. [Citation](#citation)

## Overview

EuroBERT is a family of multilingual encoder models designed for a variety of tasks such as retrieval, classification and regression supporting 15 languages, mathematics and code, supporting sequences of up to 8,192 tokens.
EuroBERT models exhibit the strongest multilingual performance across [domains and tasks](#evaluation) compared to similarly sized systems.

It is available in 3 sizes:

- [EuroBERT-210m](https://huggingface.co/EuroBERT/EuroBERT-210m) - 210 million parameters
- [EuroBERT-610m](https://huggingface.co/EuroBERT/EuroBERT-610m) - 610 million parameters
- [EuroBERT-2.1B](https://huggingface.co/EuroBERT/EuroBERT-2.1B) - 2.1 billion parameters

For more information about EuroBERT, please check our [blog](https://huggingface.co/blog/EuroBERT/release) post and the [arXiv](https://arxiv.org/abs/2503.05500) preprint.

## Usage

```python
from transformers import AutoTokenizer, AutoModelForMaskedLM

model_id = "EuroBERT/EuroBERT-610m"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForMaskedLM.from_pretrained(model_id, trust_remote_code=True)

text = "The capital of France is <|mask|>."
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)

# To get predictions for the mask:
masked_index = inputs["input_ids"][0].tolist().index(tokenizer.mask_token_id)
predicted_token_id = outputs.logits[0, masked_index].argmax(axis=-1)
predicted_token = tokenizer.decode(predicted_token_id)
print("Predicted token:", predicted_token)
# Predicted token:  Paris
```

**💻 You can use these models directly with the transformers library starting from v4.48.0:**

```sh
pip install -U transformers>=4.48.0
```

**🏎️ If your GPU supports it, we recommend using EuroBERT with Flash Attention 2 to achieve the highest efficiency. To do so, install Flash Attention 2 as follows, then use the model as normal:**

```bash
pip install flash-attn
```

## Evaluation

We evaluate EuroBERT on a suite of tasks to cover various real-world use cases for multilingual encoders, including retrieval performance, classification, sequence regression, quality estimation, summary evaluation, code-related tasks, and mathematical tasks.

**Key highlights:**
The EuroBERT family exhibits strong multilingual performance across domains and tasks.
- EuroBERT-2.1B, our largest model, achieves the highest performance among all evaluated systems. It outperforms the largest system, XLM-RoBERTa-XL.

- EuroBERT-610m is competitive with XLM-RoBERTa-XL, a model 5 times its size, on most multilingual tasks and surpasses it in code and mathematics tasks.

- The smaller EuroBERT-210m generally outperforms all similarly sized systems.

<div>
  <img src="img/multilingual.png" width="100%"  alt="EuroBERT" />
</div>

<div>
  <img src="img/code_math.png" width="100%"  alt="EuroBERT" />
</div>

<div>
  <img src="img/long_context.png" width="100%"  alt="EuroBERT" />
</div>

### Suggested Fine-Tuning Hyperparameters

If you plan to fine-tune this model on some downstream tasks, you can follow the hyperparameters we found in our paper.

#### Base Hyperparameters (unchanged across tasks)

- Warmup Ratio: 0.1
- Learning Rate Scheduler: Linear
- Adam Beta 1: 0.9  
- Adam Beta 2: 0.95  
- Adam Epsilon: 1e-5  
- Weight Decay: 0.1  

#### Task-Specific Learning Rates

##### Retrieval:
| Dataset                                 | EuroBERT-210m | EuroBERT-610m | EuroBERT-2.1B |
|-----------------------------------------|----------------|----------------|----------------|
| MIRACL                                  | 4.6e-05        | 3.6e-05        | 2.8e-05        |
| MLDR                                    | 2.8e-05        | 2.2e-05        | 4.6e-05        |
| CC-News                                 | 4.6e-05        | 4.6e-05        | 3.6e-05        |
| Wikipedia                               | 2.8e-05        | 3.6e-05        | 2.8e-05        |
| CodeSearchNet                           | 4.6e-05        | 2.8e-05        | 3.6e-05        |
| DupStackMath                            | 4.6e-05        | 2.8e-05        | 3.6e-05        |
| MathFormula                             | 1.7e-05        | 3.6e-05        | 3.6e-05        |

##### Sequence Classification:

| Dataset                              | EuroBERT-210m | EuroBERT-610m | EuroBERT-2.1B |
|--------------------------------------|----------------|----------------|----------------|
| XNLI                                 | 3.6e-05        | 3.6e-05        | 2.8e-05        |
| PAWS-X                               | 3.6e-05        | 4.6e-05        | 3.6e-05        |
| AmazonReviews                        | 3.6e-05        | 2.8e-05        | 3.6e-05        |
| MassiveIntent                        | 6.0e-05        | 4.6e-05        | 2.8e-05        |
| CodeComplexity                       | 3.6e-05        | 3.6e-05        | 1.0e-05        |
| CodeDefect                           | 3.6e-05        | 2.8e-05        | 1.3e-05        |
| MathShepherd                         | 7.7e-05        | 2.8e-05        | 1.7e-05        |

##### Sequence Regression:

| Dataset                  | EuroBERT-210m | EuroBERT-610m | EuroBERT-2.1B |
|--------------------------|----------------|----------------|----------------|
| WMT (Ref-based)          | 2.8e-05        | 2.8e-05        | 1.3e-05        |
| WMT (Ref-free)           | 2.8e-05        | 2.8e-05        | 1.3e-05        |
| SeaHorse                 | 3.6e-05        | 3.6e-05        | 2.8e-05        |


## License

We release the EuroBERT model architectures, model weights, and training codebase under the Apache 2.0 license.

## Citation

If you use EuroBERT in your work, please cite:

```
@misc{boizard2025eurobertscalingmultilingualencoders,
      title={EuroBERT: Scaling Multilingual Encoders for European Languages}, 
      author={Nicolas Boizard and Hippolyte Gisserot-Boukhlef and Duarte M. Alves and André Martins and Ayoub Hammal and Caio Corro and Céline Hudelot and Emmanuel Malherbe and Etienne Malaboeuf and Fanny Jourdan and Gabriel Hautreux and João Alves and Kevin El-Haddad and Manuel Faysse and Maxime Peyrard and Nuno M. Guerreiro and Patrick Fernandes and Ricardo Rei and Pierre Colombo},
      year={2025},
      eprint={2503.05500},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2503.05500}, 
}
```