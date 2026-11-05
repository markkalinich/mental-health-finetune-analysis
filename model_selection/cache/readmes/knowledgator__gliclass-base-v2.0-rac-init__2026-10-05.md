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
- knowledgator/gliclass-v2.0-RAC
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
- microsoft/deberta-v3-base
---
# ⭐ GLiClass: Generalist and Lightweight Model for Sequence Classification

This is an efficient zero-shot classifier inspired by [GLiNER](https://github.com/urchade/GLiNER/tree/main) work. It demonstrates the same performance as a cross-encoder while being more compute-efficient because classification is done at a single forward path.

It can be used for `topic classification`, `sentiment analysis` and as a reranker in `RAG` pipelines.

The model was trained on synthetic and licensed data that allow commercial use and can be used in commercial applications.

This version of the model uses a layer-wise selection of features that enables a better understanding of different levels of language. The backbone model is [microsoft/deberta-v3-base](https://huggingface.co/microsoft/deberta-v3-base).
###  Retrieval-augmented Classification (RAC):
The main idea of this model is to utilize the information from semantically similar examples to enhance predictions in inference. The tests showed that providing the model with at least one example from the train dataset, which was retrieved by semantic similarity, could increase the F1 score from 0.3090 to 0.4275, in some cases from 0.2594 up to 0.6249. Moreover, the RAC approach, with 2 examples provided, showed an F1 score, compared to fine-tuning with 8 examples per label: 0.4707 and 0.4838, respectively.


###  RAC dataset generation strategy:
![image/png](https://cdn-uploads.huggingface.co/production/uploads/6405f62ba577649430be5124/VFl2YKJLqUUYFoFAsIUUX.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/6405f62ba577649430be5124/t4cMnOq3OEL2qiVNd0d3p.png)
To further enhance classification performance, we generated a Retrieval-Augmented Classification (RAC) dataset. Each text example in the gliclass-v2.0 dataset was encoded using the paraphrase-MiniLM-L6-v2 sentence transformer and indexed in an HNSW (Hierarchical Navigable Small World) database. For 250k randomly selected samples, we retrieved up to three most similar examples (cosine similarity > 0.5) from the dataset.

During augmentation:
- The number of retrieved examples per sample was randomly chosen between 1 and 3.
- 30% of retrieved examples were replaced with random, unrelated examples to introduce controlled noise.
- If true labels were present in a retrieved example, false labels were removed with a 50% probability to balance information clarity.

Each retrieved example was formatted using structured ```<<EXAMPLE>> ... <</EXAMPLE>>``` tags, where:
- True labels were explicitly marked as ```<<TRUE_LABEL>>  {label}```.
- False labels were marked as ```<<FALSE_LABEL>>  {label}```, unless removed.

For each randomly selected 250k examples, the “text” was modified as ```{original_text} <<EXAMPLE>> {retrieved_text} {true_labels_str} {false_labels_str} <</EXAMPLE>>...```
Where:
- ```{original_text}``` is the original example text.
- ```{retrieved_text}``` is a similar or randomly selected example.
- ```{true_labels_str}``` contains true labels formatted as ```<<TRUE_LABEL>> {label}```.
- ```{false_labels_str}``` contains false labels formatted as ```<<FALSE_LABEL>> {label}``` (unless removed with 50% probability).

Such a strategy allows the model to learn how to utilize the provided information without overfocusing on RAC examples. With both relevant and randomly retrieved examples, the dataset maintains a balance between useful contextual information and controlled noise. This ensures that the model does not become overly reliant on retrieval-augmented inputs while still benefiting from additional context when available.

### How to use:
First of all, you need to install GLiClass library:
```bash
pip install gliclass
```

Than you need to initialize a model and a pipeline:
```python
from gliclass import GLiClassModel, ZeroShotClassificationPipeline
from transformers import AutoTokenizer

model = GLiClassModel.from_pretrained("knowledgator/gliclass-base-v2.0-rac-init")
tokenizer = AutoTokenizer.from_pretrained("knowledgator/gliclass-base-v2.0-rac-init")
pipeline = ZeroShotClassificationPipeline(model, tokenizer, classification_type='multi-label', device='cuda:0')

text = "One day I will see the world!"
labels = ["travel", "dreams", "sport", "science", "politics"]
results = pipeline(text, labels, threshold=0.5)[0] #because we have one text
for result in results:
 print(result["label"], "=>", result["score"])
```

To use with one **RAC** example:
```python
example_1 = {
    "text": "A recently developed machine learning platform offers robust automation for complex data analysis workflows. While it enhances productivity, users have reported difficulties in integrating it with their current data infrastructure and a need for better documentation.",
    "all_labels": ["AI", "automation", "data_analysis", "usability", "integration"],
    "true_labels": ["AI", "integration", 'automation']
}

text = "The new AI-powered tool streamlines data analysis by automating repetitive tasks, improving efficiency for data scientists. However, its steep learning curve and limited integration with existing platforms pose challenges for widespread adoption."
labels = ["AI", "automation", "data_analysis", "usability", "integration"]

results = pipeline(text, labels, threshold=0.1, rac_examples=[example_1])[0]

for predict in results:
    print(predict["label"], " - ", predict["score"])
```

To use with several **RAC** examples:
```python
example_1 = {
    "text": "A recently developed machine learning platform offers robust automation for complex data analysis workflows. While it enhances productivity, users have reported difficulties in integrating it with their current data infrastructure and a need for better documentation.",
    "all_labels": ["AI", "automation", "data_analysis", "usability", "integration"],
    "true_labels": ["AI", "integration", 'automation']
}
example_2 = {
    "text": "A cloud-based analytics tool leverages artificial intelligence to provide real-time insights. It significantly improves workflow efficiency but struggles with compatibility across different enterprise systems, requiring additional customization efforts.",
    "all_labels": ["AI", "automation", "data_analysis", "usability", "integration"],
    "true_labels": ["AI", "integration", "data_analysis"]
}
text = "The new AI-powered tool streamlines data analysis by automating repetitive tasks, improving efficiency for data scientists. However, its steep learning curve and limited integration with existing platforms pose challenges for widespread adoption."
labels = ["AI", "automation", "data_analysis", "usability", "integration"]

results = pipeline(text, labels, threshold=0.1, rac_examples=[example_1, example_2])[0]

for predict in results:
    print(predict["label"], " - ", predict["score"])
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
Below, you can find a comparison with other GLiClass models:

| Dataset              | gliclass-base-v1.0-init | gliclass-large-v1.0-init | gliclass-modern-base-v2.0-init | gliclass-modern-large-v2.0-init | gliclass-base-v2.0-rac-init |
|----------------------|-----------------------|-----------------------|---------------------|---------------------|---------------------|
| CR                   | 0.8672                | 0.8024                | 0.9041              | 0.8980              | 0.7852              |
| sst2                 | 0.8342                | 0.8734                | 0.9011              | 0.9434              | 0.8610              |
| sst5                 | 0.2048                | 0.1638                | 0.1972              | 0.1123              | 0.0598              |
| 20_news_groups       | 0.2317                | 0.4151                | 0.2448              | 0.2792              | 0.4007              |
| spam                 | 0.5963                | 0.5407                | 0.5074              | 0.6364              | 0.6739              |
| financial_phrasebank | 0.3594                | 0.3705                | 0.2537              | 0.2562              | 0.2537              |
| imdb                 | 0.8772                | 0.8836                | 0.8255              | 0.9137              | 0.8716              |
| ag_news              | 0.5614                | 0.7069                | 0.6050              | 0.6933              | 0.6759              |
| emotion              | 0.2865                | 0.3840                | 0.2474              | 0.3746              | 0.4160              |
| cap_sotu             | 0.3966                | 0.4353                | 0.2929              | 0.2919              | 0.3871              |
| rotten_tomatoes      | 0.6626                | 0.7933                | 0.6630              | 0.5928              | 0.7739              |
| **AVERAGE:**         | 0.5344                | 0.5790                | 0.5129              | 0.5447              | 0.5598              |

Here you can see how the performance of the model grows, providing more **RAC** examples:
| Dataset                             | 0 examples | 1 example | 2 examples | 3 examples |
|-------------------------------------|------------|------------|------------|------------|
| cap_sotu                            | 0.3857     | 0.4665     | 0.4935     | 0.4847     |
| cap_sotu (8 examples)               | 0.4938     | 0.5097     | 0.4976     | 0.4894     |
| cap_sotu (Weak Supervision - 8)     | 0.4319     | 0.4764     | 0.4488     | 0.4465     |
| dair-ai_emotion                     | 0.4472     | 0.5505     | 0.5619     | 0.5705     |
| dair-ai_emotion (8 examples)        | 0.5088     | 0.5630     | 0.5623     | 0.5740     |
| dair-ai_emotion (Weak Supervision - 8) | 0.4187  | 0.5479     | 0.5693     | 0.5828     |
| ag_news                              | 0.6791     | 0.8507     | 0.8717     | 0.8866     |
| ag_news (8 examples)                 | 0.8496     | 0.9002     | 0.9072     | 0.9091     |
| ag_news (Weak Supervision - 8)       | 0.6546     | 0.8623     | 0.8841     | 0.8978     |
| sst5                                 | 0.0599     | 0.0675     | 0.1163     | 0.1267     |
| sst5 (8 examples)                    | 0.2887     | 0.2690     | 0.2642     | 0.2394     |
| sst5 (Weak Supervision - 8)          | 0.0744     | 0.2780     | 0.2897     | 0.2912     |
| ScienceQA                            | 0.1142     | 0.4035     | 0.4534     | 0.4495     |
| ScienceQA (8 examples)               | 0.6493     | 0.6547     | 0.6956     | 0.6770     |
| ScienceQA (Weak Supervision - 8)     | 0.2987     | 0.5919     | 0.5998     | 0.5674     |
| Malicious_code_classification        | 0.3717     | 0.6260     | 0.9672     | 0.9788     |
| Malicious_code_classification (8 examples) | 0.8444 | 0.9722 | 0.9788 | 0.9772 |
| Malicious_code_classification (Weak Supervision - 8) | 0.3745 | 0.9216 | 0.9788 | 0.9772 |
| twitter-financial-news-topic         | 0.2594     | 0.6249     | 0.6408     | 0.6427     |
| twitter-financial-news-topic (8 examples) | 0.6137 | 0.7072 | 0.7099 | 0.6948 |
| twitter-financial-news-topic (Weak Supervision - 8) | 0.4032 | 0.6651 | 0.6316 | 0.6114 |
| 20_newsgroups                        | 0.3211     | 0.1339     | 0.0906     | 0.1005     |
| 20_newsgroups (8 examples)           | 0.0959     | 0.0657     | 0.0440     | 0.0445     |
| 20_newsgroups (Weak Supervision - 8) | 0.4765     | 0.1035     | 0.0775     | 0.0777     |
| ChemProt                              | 0.2024     | 0.1911     | 0.1568     | 0.1329     |
| ChemProt (8 examples)                 | 0.2985     | 0.3479     | 0.3636     | 0.3538     |
| ChemProt (Weak Supervision - 8)       | 0.2369     | 0.2067     | 0.1911     | 0.1780     |

| **AVERAGE:**                         | **0 examples** | **1 example** | **2 examples** | **3 examples** |
|-------------------------------------|---------------|---------------|---------------|---------------|
| Standard                            | 0.3090        | 0.4275        | 0.4707        | 0.4718        |
| 8 examples                          | 0.4838        | 0.5245        | 0.5288        | 0.5244        |
| Weak Supervision - 8                | 0.3661        | 0.4862        | 0.4868        | 0.4821        |

Here you can see how the performance of the model grows, providing more examples in comparison to other models:
| Model                             | Num Examples      | sst5   | ag_news | emotion | **AVERAGE:** |
|------------------------------------|------------------|--------|---------|--------------|----------|
| gliclass-base-v2.0-rac-init   | 0                | 0.0599 | 0.6791  | 0.4472       | 0.3934   |
| gliclass-base-v2.0-rac-init   | 8                | 0.2887 | 0.8496  | 0.5088       | 0.6149   |
| gliclass-base-v2.0-rac-init   | Weak Supervision | 0.0744 | 0.6546  | 0.4187       | 0.3983   |
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