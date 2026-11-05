---
license: apache-2.0
datasets:
- MoritzLaurer/synthetic_zeroshot_mixtral_v0.1
- knowledgator/gliclass-v1.0
- fancyzhx/amazon_polarity
- cnmoro/QuestionClassification
- Arsive/toxicity_classification_jigsaw
- shishir-dwi/News-Article-Categorization_IAB
- SetFit/qnli
- nyu-mll/multi_nli
- SetFit/student-question-categories
- SetFit/tweet_sentiment_extraction
- SetFit/hate_speech18
- saattrupdan/doc-nli
language:
- en
- fr
- ge
metrics:
- f1
pipeline_tag: zero-shot-classification
tags:
- text classification
- zero-shot
- small language models
- RAG
- sentiment analysis
base_model:
- answerdotai/ModernBERT-base
---
# ⭐ [GLiClass](https://github.com/Knowledgator/GLiClass): Generalist and Lightweight Model for Sequence Classification

This is an efficient zero-shot classifier inspired by [GLiNER](https://github.com/urchade/GLiNER/tree/main) work. It demonstrates the same performance as a cross-encoder while being more compute-efficient because classification is done at a single forward path.

It can be used for `topic classification`, `sentiment analysis` and as a reranker in `RAG` pipelines.

The model was trained on synthetic and licensed data that allow commercial use and can be used in commercial applications.

This version of the model uses a layer-wise selection of features that enables a better understanding of different levels of language. The backbone model is [ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base), which effectively processes long sequences.

### How to use:
First of all, you need to install GLiClass library:
```bash
pip install gliclass
pip install -U transformers>=4.48.0
```

Than you need to initialize a model and a pipeline:
```python
from gliclass import GLiClassModel, ZeroShotClassificationPipeline
from transformers import AutoTokenizer

model = GLiClassModel.from_pretrained("knowledgator/gliclass-modern-base-v2.0-init")
tokenizer = AutoTokenizer.from_pretrained("knowledgator/gliclass-modern-base-v2.0-init", add_prefix_space=True)
pipeline = ZeroShotClassificationPipeline(model, tokenizer, classification_type='multi-label', device='cuda:0')

text = "One day I will see the world!"
labels = ["travel", "dreams", "sport", "science", "politics"]
results = pipeline(text, labels, threshold=0.5)[0] #because we have one text
for result in results:
 print(result["label"], "=>", result["score"])
```

If you want to use it for NLI type of tasks, we recommend representing your premise as a text and hypothesis as a label, you can put several hypotheses, but the model works best with a single input hypothesis.
```python
# Initialize model and multi-label pipeline
text = "The cat slept on the windowsill all afternoon"
labels = ["The cat was awake and playing outside."]
results = pipeline(text, labels, threshold=0.0)[0]
print(results)
```

### Benchmarks:
Below, you can see the F1 score on several text classification datasets. All tested models were not fine-tuned on those datasets and were tested in a zero-shot setting.
| Model                       | IMDB | AG_NEWS | Emotions |
|-----------------------------|------|---------|----------|
| [gliclass-modern-large-v2.0-init (399 M)](https://huggingface.co/knowledgator/gliclass-modern-large-v2.0-init) | 0.9137 | 0.7357  | 0.4140  |
| [gliclass-modern-base-v2.0-init (151 M)](https://huggingface.co/knowledgator/gliclass-modern-base-v2.0-init) | 0.8264 | 0.6637  | 0.2985  |
| [gliclass-large-v1.0 (438 M)](https://huggingface.co/knowledgator/gliclass-large-v1.0) | 0.9404 | 0.7516  | 0.4874  |
| [gliclass-base-v1.0 (186 M)](https://huggingface.co/knowledgator/gliclass-base-v1.0) | 0.8650 | 0.6837  | 0.4749  |
| [gliclass-small-v1.0 (144 M)](https://huggingface.co/knowledgator/gliclass-small-v1.0) | 0.8650 | 0.6805  | 0.4664   |
| [Bart-large-mnli (407 M)](https://huggingface.co/facebook/bart-large-mnli)      | 0.89 | 0.6887  | 0.3765   |
| [Deberta-base-v3 (184 M)](https://huggingface.co/cross-encoder/nli-deberta-v3-base)      | 0.85 | 0.6455  | 0.5095   |
| [Comprehendo (184M)](https://huggingface.co/knowledgator/comprehend_it-base)           | 0.90 | 0.7982  | 0.5660   |
| SetFit [BAAI/bge-small-en-v1.5 (33.4M)](https://huggingface.co/BAAI/bge-small-en-v1.5) | 0.86 | 0.5636 | 0.5754 |


Below you can find a comparison with other GLiClass models:

| Dataset              | gliclass-base-v1.0-init | gliclass-large-v1.0-init | gliclass-modern-base-v2.0-init | gliclass-modern-large-v2.0-init |
|----------------------|-----------------------|-----------------------|---------------------|---------------------|
| CR                   | 0.8672                | 0.8024                | 0.9041              | 0.8980              |
| sst2                 | 0.8342                | 0.8734                | 0.9011              | 0.9434              |
| sst5                 | 0.2048                | 0.1638                | 0.1972              | 0.1123              |
| 20_news_groups       | 0.2317                | 0.4151                | 0.2448              | 0.2792              |
| spam                 | 0.5963                | 0.5407                | 0.5074              | 0.6364              |
| financial_phrasebank | 0.3594                | 0.3705                | 0.2537              | 0.2562              |
| imdb                 | 0.8772                | 0.8836                | 0.8255              | 0.9137              |
| ag_news              | 0.5614                | 0.7069                | 0.6050              | 0.6933              |
| emotion              | 0.2865                | 0.3840                | 0.2474              | 0.3746              |
| cap_sotu             | 0.3966                | 0.4353                | 0.2929              | 0.2919              |
| rotten_tomatoes      | 0.6626                | 0.7933                | 0.6630              | 0.5928              |
| **AVERAGE:**         | 0.5344                | 0.5790                | 0.5129              | 0.5447              |

Here you can see how the performance of the model grows providing more examples:
| Model                             | Num Examples      | sst5   | ag_news | emotion | **AVERAGE:** |
|------------------------------------|------------------|--------|---------|--------------|----------|
| gliclass-modern-large-v2.0-init   | 0                | 0.1123 | 0.6933  | 0.3746       | 0.3934   |
| gliclass-modern-large-v2.0-init   | 8                | 0.5098 | 0.8339  | 0.5010       | 0.6149   |
| gliclass-modern-large-v2.0-init   | Weak Supervision | 0.0951 | 0.6478  | 0.4520       | 0.3983   |
| gliclass-modern-base-v2.0-init    | 0                | 0.1972 | 0.6050  | 0.2474       | 0.3499   |
| gliclass-modern-base-v2.0-init    | 8                | 0.3604 | 0.7481  | 0.4420       | 0.5168   |
| gliclass-modern-base-v2.0-init    | Weak Supervision | 0.1599 | 0.5713  | 0.3216       | 0.3509   |
| gliclass-large-v1.0-init          | 0                | 0.1639 | 0.7069  | 0.3840       | 0.4183   |
| gliclass-large-v1.0-init          | 8                | 0.4226 | 0.8415  | 0.4886       | 0.5842   |
| gliclass-large-v1.0-init          | Weak Supervision | 0.1689 | 0.7051  | 0.4586       | 0.4442   |
| gliclass-base-v1.0-init           | 0                | 0.2048 | 0.5614  | 0.2865       | 0.3509   |
| gliclass-base-v1.0-init           | 8                | 0.2007 | 0.8359  | 0.4856       | 0.5074   |
| gliclass-base-v1.0-init           | Weak Supervision | 0.0681 | 0.6627  | 0.3066       | 0.3458   |

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