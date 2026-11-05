---
license: apache-2.0
datasets:
- MoritzLaurer/synthetic_zeroshot_mixtral_v0.1
language:
- en
metrics:
- f1
pipeline_tag: zero-shot-classification
tags:
- text classification
- zero-shot
- small language models
- RAG
- sentiment analysis
---

# ⭐ GLiClass: Generalist and Lightweight Model for Sequence Classification

This is an efficient zero-shot classifier inspired by [GLiNER](https://github.com/urchade/GLiNER/tree/main) work. It demonstrates the same performance as a cross-encoder while being more compute-efficient because classification is done at a single forward path.

It can be used for `topic classification`, `sentiment analysis` and as a reranker in `RAG` pipelines.

The model was trained on synthetic data and can be used in commercial applications.

This version of the model utilize the [LLM2Vec](https://github.com/McGill-NLP/llm2vec/tree/main/llm2vec) approach for converting modern decoders to bi-directional encoder. It brings the following benefits:
* Enhanced performance and generalization capabilities;
* Support for Flash Attention;
* Extended context window.


### How to use:
First of all, you need to install GLiClass library:
```bash
pip install gliclass
```

Than you need to initialize a model and a pipeline:
```python
from gliclass import GLiClassModel, ZeroShotClassificationPipeline
from transformers import AutoTokenizer

model = GLiClassModel.from_pretrained("knowledgator/gliclass-llama-1.3B-v1.0")
tokenizer = AutoTokenizer.from_pretrained("knowledgator/gliclass-llama-1.3B-v1.0")

pipeline = ZeroShotClassificationPipeline(model, tokenizer, classification_type='multi-label', device='cuda:0')

text = "One day I will see the world!"
labels = ["travel", "dreams", "sport", "science", "politics"]
results = pipeline(text, labels, threshold=0.5)[0] #because we have one text

for result in results:
 print(result["label"], "=>", result["score"])
```

### Benchmarks:
While the model is some how comparable to DeBERTa version in zero-shot setting, it demonstrates state-of-the-art performance in few-shot setting.
![Few-shot performance](few_shot.png)

### Join Our Discord

Connect with our community on Discord for news, support, and discussion about our models. Join [Discord](https://discord.gg/dkyeAgs9DG).

## Citation
```bibtex
@misc{stepanov2025gliclassgeneralistlightweightmodel,
      title={GLiClass: Generalist Lightweight Model for Sequence Classification Tasks}, 
      author={Ihor Stepanov and Mykhailo Shtopko and Dmytro Vodianytskyi and Oleksandr Lukashov and Alexander Yavorskyi and Mykyta Yaroshenko},
      year={2025},
      eprint={2508.07662},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2508.07662}, 
}
```