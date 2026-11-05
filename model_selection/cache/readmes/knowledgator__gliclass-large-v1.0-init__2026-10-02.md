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

This model wasn't additionally fine-tuned on any dataset except initial (MoritzLaurer/synthetic_zeroshot_mixtral_v0.1).

### How to use:
First of all, you need to install GLiClass library:
```bash
pip install gliclass
```

Than you need to initialize a model and a pipeline:
```python
from gliclass import GLiClassModel, ZeroShotClassificationPipeline
from transformers import AutoTokenizer

model = GLiClassModel.from_pretrained("knowledgator/gliclass-large-v1.0-init")
tokenizer = AutoTokenizer.from_pretrained("knowledgator/gliclass-large-v1.0-init")

pipeline = ZeroShotClassificationPipeline(model, tokenizer, classification_type='multi-label', device='cuda:0')

text = "One day I will see the world!"
labels = ["travel", "dreams", "sport", "science", "politics"]
results = pipeline(text, labels, threshold=0.5)[0] #because we have one text

for result in results:
 print(result["label"], "=>", result["score"])
```

### Benchmarks:
Below, you can see the F1 score on several text classification datasets. All tested models were not fine-tuned on those datasets and were tested in a zero-shot setting.
| Model                       | IMDB | AG_NEWS | Emotions |
|-----------------------------|------|---------|----------|
| [gliclass-large-v1.0 (438 M)](https://huggingface.co/knowledgator/gliclass-large-v1.0) | 0.9404 | 0.7516  | 0.4874  |
| [gliclass-base-v1.0 (186 M)](https://huggingface.co/knowledgator/gliclass-base-v1.0) | 0.8650 | 0.6837  | 0.4749  |
| [gliclass-small-v1.0 (144 M)](https://huggingface.co/knowledgator/gliclass-small-v1.0) | 0.8650 | 0.6805  | 0.4664   |
| [Bart-large-mnli (407 M)](https://huggingface.co/facebook/bart-large-mnli)      | 0.89 | 0.6887  | 0.3765   |
| [Deberta-base-v3 (184 M)](https://huggingface.co/cross-encoder/nli-deberta-v3-base)      | 0.85 | 0.6455  | 0.5095   |
| [Comprehendo (184M)](https://huggingface.co/knowledgator/comprehend_it-base)           | 0.90 | 0.7982  | 0.5660   |
| SetFit [BAAI/bge-small-en-v1.5 (33.4M)](https://huggingface.co/BAAI/bge-small-en-v1.5) | 0.86 | 0.5636 | 0.5754 |

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