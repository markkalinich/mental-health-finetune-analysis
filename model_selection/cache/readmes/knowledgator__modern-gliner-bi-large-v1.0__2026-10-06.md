---
license: apache-2.0
language:
- en
library_name: gliner
datasets:
- urchade/pile-mistral-v0.1
- numind/NuNER
- knowledgator/GLINER-multi-task-synthetic-data
pipeline_tag: token-classification
tags:
- NER
- GLiNER
- information extraction
- encoder
- entity recognition
- modernbert
base_model:
- answerdotai/ModernBERT-large
- BAAI/bge-base-en-v1.5
---
# About

GLiNER is a Named Entity Recognition (NER) model capable of identifying any entity type using a bidirectional transformer encoders (BERT-like). It provides a practical alternative to traditional NER models, which are limited to predefined entities, and Large Language Models (LLMs) that, despite their flexibility, are costly and large for resource-constrained scenarios.

This particular version utilizes bi-encoder architecture, where the textual encoder is [ModernBERT-large](https://huggingface.co/answerdotai/ModernBERT-large) and entity label encoder is sentence transformer - [BGE-base-en](https://huggingface.co/BAAI/bge-base-en-v1.5).

Such architecture brings several advantages over uni-encoder GLiNER:
* An unlimited amount of entities can be recognized at a single time;
* Faster inference if entity embeddings are preprocessed;
* Better generalization to unseen entities;

Utilization of ModernBERT uncovers up to 4 times better efficiency in comparison to DeBERTa-based models and context length up to 8,192 tokens while demonstrating comparable results.

![inference time comparison](modernbert_inference_time.png "Inference time comparison")

However, bi-encoder architecture has some drawbacks such as a lack of inter-label interactions that make it hard for the model to disambiguate semantically similar but contextually different entities.

### Installation & Usage
Install or update the gliner package:
```bash
pip install gliner -U
```
You need to install the latest version of transformers to use this model:
```bash
pip install git+https://github.com/huggingface/transformers.git
```
Once you've downloaded the GLiNER library, you can import the GLiNER class. You can then load this model using `GLiNER.from_pretrained` and predict entities with `predict_entities`.

```python
from gliner import GLiNER

model = GLiNER.from_pretrained("knowledgator/modern-gliner-bi-large-v1.0")

text = """
Cristiano Ronaldo dos Santos Aveiro (Portuguese pronunciation: [kɾiʃˈtjɐnu ʁɔˈnaldu]; born 5 February 1985) is a Portuguese professional footballer who plays as a forward for and captains both Saudi Pro League club Al Nassr and the Portugal national team. Widely regarded as one of the greatest players of all time, Ronaldo has won five Ballon d'Or awards,[note 3] a record three UEFA Men's Player of the Year Awards, and four European Golden Shoes, the most by a European player. He has won 33 trophies in his career, including seven league titles, five UEFA Champions Leagues, the UEFA European Championship and the UEFA Nations League. Ronaldo holds the records for most appearances (183), goals (140) and assists (42) in the Champions League, goals in the European Championship (14), international goals (128) and international appearances (205). He is one of the few players to have made over 1,200 professional career appearances, the most by an outfield player, and has scored over 850 official senior career goals for club and country, making him the top goalscorer of all time.
"""

labels = ["person", "award", "date", "competitions", "teams"]

entities = model.predict_entities(text, labels, threshold=0.3)

for entity in entities:
    print(entity["text"], "=>", entity["label"])
```

```
Cristiano Ronaldo dos Santos Aveiro => person
5 February 1985 => date
Al Nassr => teams
Portugal national team => teams
Ballon d'Or => award
UEFA Men's Player of the Year Awards => award
European Golden Shoes => award
UEFA Champions Leagues => competitions
UEFA European Championship => competitions
UEFA Nations League => competitions
Champions League => competitions
European Championship => competitions
```

If you want to use **flash attention** or increase sequence length, please, check the following code:

Firstly, install Flash Attention and Triton packages:
```bash
pip install flash-attn triton
```

```python
model = GLiNER.from_pretrained("knowledgator/modern-gliner-bi-large-v1.0",
                                _attn_implementation = 'flash_attention_2',
                                                max_len = 2048).to('cuda:0')
```

If you have a large amount of entities and want to pre-embed them, please, refer to the following code snippet:

```python
labels = ["your entities"]
texts = ["your texts"]

entity_embeddings = model.encode_labels(labels, batch_size = 8)

outputs = model.batch_predict_with_embeds(texts, entity_embeddings, labels)
```

### Benchmarks

![results on different datasets](modernbert_benchmarking.png "Results on different datasets")

Below you can see the table with benchmarking results on various named entity recognition datasets:

| Dataset                 | Score  |
|-------------------------|--------|
| ACE 2004               | 30.5%  |
| ACE 2005               | 26.7%  |
| AnatEM                 | 37.2%  |
| Broad Tweet Corpus     | 72.1%  |
| CoNLL 2003             | 69.3%  |
| FabNER                 | 22.0%  |
| FindVehicle            | 40.3%  |
| GENIA_NER              | 55.6%  |
| HarveyNER              | 16.1%  |
| MultiNERD              | 73.8%  |
| Ontonotes              | 39.2%  |
| PolyglotNER            | 49.1%  |
| TweetNER7              | 39.6%  |
| WikiANN en             | 54.7%  |
| WikiNeural             | 83.7%  |
| bc2gm                  | 53.7%  |
| bc4chemd               | 52.1%  |
| bc5cdr                 | 67.0%  |
| ncbi                   | 61.7%  |
| **Average**            | **49.7%** |
|                         |        |
| CrossNER_AI            | 58.1%  |
| CrossNER_literature    | 60.0%  |
| CrossNER_music         | 73.0%  |
| CrossNER_politics      | 72.8%  |
| CrossNER_science       | 66.5%  |
| mit-movie              | 47.6%  |
| mit-restaurant         | 40.6%  |
| **Average (zero-shot benchmark)** | **59.8%** | 


### Join Our Discord

Connect with our community on Discord for news, support, and discussion about our models. Join [Discord](https://discord.gg/dkyeAgs9DG).

## Citation

If you use this model in your work, please cite:

```bibtex
@misc{modernbert,
      title={Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference}, 
      author={Benjamin Warner and Antoine Chaffin and Benjamin Clavié and Orion Weller and Oskar Hallström and Said Taghadouini and Alexis Gallagher and Raja Biswas and Faisal Ladhak and Tom Aarsen and Nathan Cooper and Griffin Adams and Jeremy Howard and Iacopo Poli},
      year={2024},
      eprint={2412.13663},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2412.13663}, 
}
```

```bibtex
@misc{zaratiana2023gliner,
      title={GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer}, 
      author={Urchade Zaratiana and Nadi Tomeh and Pierre Holat and Thierry Charnois},
      year={2023},
      eprint={2311.08526},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

```bibtex
@misc{stepanov2024gliner,
      title={GLiNER multi-task: Generalist Lightweight Model for Various Information Extraction Tasks}, 
      author={Ihor Stepanov and Mykhailo Shtopko},
      year={2024},
      eprint={2406.12925},
      archivePrefix={arXiv},
      primaryClass={id='cs.LG' full_name='Machine Learning' is_active=True alt_name=None in_archive='cs' is_general=False description='Papers on all aspects of machine learning research (supervised, unsupervised, reinforcement learning, bandit problems, and so on) including also robustness, explanation, fairness, and methodology. cs.LG is also an appropriate primary category for applications of machine learning methods.'}
}
```