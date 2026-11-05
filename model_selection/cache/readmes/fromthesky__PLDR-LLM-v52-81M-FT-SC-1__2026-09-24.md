---
language:
- en
license: apache-2.0
tags:
- sentiment-analysis
- sentiment-classification
- large-language-model
- power-law-decoder-representations
- power-law-graph-attention
- pldr-llm
- kv-cache
- g-cache
- kvg-cache
- pytorch
datasets:
- stanfordnlp/imdb
base_model:
- fromthesky/PLDR-LLM-v52-110M-1
pipeline_tag: text-classification
library_name: transformers
model-index:
  - name: PLDR-LLM-v52-81M-FT-SC-1
    results:
      - task:
          type: text-classification
          name: Text Classification
        dataset:
          name: stanfordnlp/imdb
          type: stanfordnlp/imdb
        metrics:
          - type: accuracy
            value: 0.9466
            name: Accuracy
          - type: precision
            value: 0.9463
            name: Precision
          - type: recall
            value: 0.9489
            name: Recall
          - type: f1
            value: 0.9476
            name: F1
---

# PLDR-LLM-v52-81M-FT-SC-1

## Model Description

PLDR-LLM-v52-81M-FT-SC-1 is a finetuned PLDR-LLM (Large Language Model from Power Law Decoder Representations) with KV-cache and G-cache support for sequence classification. This model has a parameter size of 81M. It was finetuned using the [imdb dataset](https://huggingface.co/datasets/stanfordnlp/imdb) on the PLDR-LLM base model [PLDR-LLM-v52-110M-1](https://huggingface.co/fromthesky/PLDR-LLM-v52-110M-1). 

More details about the PLDR-LLM architecture can be found in the research paper titled [PLDR-LLMs Learn A Generalizable Tensor Operator That Can Replace Its Own Deep Neural Net At Inference](https://arxiv.org/abs/2502.13502). 


## Training data

PLDR-LLM-v52-81M-FT-SC-1 was finetuned using the [imdb dataset](https://huggingface.co/datasets/stanfordnlp/imdb) which is a large movie review dataset for binary sentiment analysis comprising of 25000 movie reviews for training and another 25000 reviews for testing. Base model was pretrained on the ~8B tokens from [RefinedWeb](https://huggingface.co/datasets/tiiuae/falcon-refinedweb), a publicly available English web dataset with extensive filtering and deduplication.

## Training procedure

The train and test data samples are combined and train and test splits were adjusted to get a total of 45000 samples for training and 5000 samples for validation. No data cleaning was done. This model was trained with the custom model implementation of PLDR-LLM for the Huggingface Transformers library. Following parameters were used for finetuning and other parameters were kept same as in the [research paper](https://arxiv.org/abs/2502.13502) detailing the PLDR-LLM architecture.
|Parameter | Value|
|----------|------|
| Learning rate | 7x10<sup>-5</sup>   |
| Warm-up steps |  20   |
| Grad clip by norm | 1.0 |
| Epochs | 2 |
|Padding side| "right" |
|Add EOS token | True |
|min_lr_rate | 0.01 |

## Intended Use and Limitations

This model is intended to be used for research purposes. Given text as input prompt, it carries out binary sentiment analysis prediction. The context length for this model is 1024 tokens. 

## How to Use

### Via Huggingface Transformers Library

PLDR-LLM has custom model support for Huggingface Transformers library. PLDR-LLM custom models support was evaluated on Transformers 4.56.1 release available at the time.

```python
from transformers import pipeline

seq_classifier = pipeline(
    task="sentiment-analysis",
    model="fromthesky/PLDR-LLM-v52-81M-FT-SC-1",
    device="cuda", # or "cpu" 
    trust_remote_code=True
    )

text="""
Star Trek the Next Generation was arguably one of the most successful sci-fi shows \
in the late eighties and early nineties. With a cast that complemented each other's character \
seamlessly, the stories covered in the show touched on a wide variety of thought \
provoking issues such as a dying civilization's daring attempt to be remembered in \
"the Inner Light" and action packed two part episode with a cliffhanger in \
"Best of Both Worlds" against the formidable Borg Collective. The end result was \
a show that kept the audience engaged and entertained for the majority of the time it was on air.
"""
output=seq_classifier(text)
print(f"PREDICTION: {output}")
```
```
PREDICTION: [{'label': 'POSITIVE', 'score': 0.9999229907989502}]
```

#### Notes:
- This implementation of PLDR-LLM custom code was evaluated on Transformers 4.56.1 and pytorch 2.6.0.

### Limitations and Biases

This model was finetuned on a pretrained Large Language Model. Large Language Models may generate text that is profane, lewd, socially unacceptable or offensive based on the contents of the dataset it was pretrained. RefinedWeb is a dataset that is as toxic and biased as the Pile. Please see the papers for [RefinedWeb](https://arxiv.org/abs/2306.01116) and [the Pile](https://arxiv.org/pdf/2101.00027) for more information. Moreover, large language models are also susceptible to hallucinations and may generate text that contains incorrect, irrelevant or misleading information. Since it is very hard to expect the contents of generated text ahead of time, the output of the large language models need to be heavily moderated and curated to avoid undesired content to appear without warning.

## Eval results
- Evaluation was done on 5000 samples that were used for validation.

|Metric | Value |
|-------------------|--------|
| Accuracy             |0.9466|
| Precision             |0.9463|
| Recall         |0.9489|
| F1        |0.9476|

### BibTeX entry and citation info


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
