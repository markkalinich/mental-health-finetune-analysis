---
license: apache-2.0
language:
- multilingual
library_name: gliner
datasets:
- urchade/pile-mistral-v0.1
- numind/NuNER
- knowledgator/GLINER-multi-task-synthetic-data
pipeline_tag: token-classification
---

# About

GLiNER is a Named Entity Recognition (NER) model capable of identifying any entity type using a bidirectional transformer encoders (BERT-like). It provides a practical alternative to traditional NER models, which are limited to predefined entities, and Large Language Models (LLMs) that, despite their flexibility, are costly and large for resource-constrained scenarios.

This particular version utilize bi-encoder architecture with post-fusion, where textual encoder is [DeBERTa v3 small](microsoft/deberta-v3-small) and entity label encoder is sentence transformer - [BGE-small-en](https://huggingface.co/BAAI/bge-small-en-v1.5).

Such architecture brings several advantages over uni-encoder GLiNER:
* An unlimited amount of entities can be recognized at a single time;
* Faster inference if entity embeddings are preprocessed;
* Better generalization to unseen entities;

Post fusion strategy brings advantages over classical bi-encoder enabling better inter-label understanding.

### Installation & Usage
Install or update the gliner package:
```bash
pip install gliner -U
```

Once you've downloaded the GLiNER library, you can import the GLiNER class. You can then load this model using `GLiNER.from_pretrained` and predict entities with `predict_entities`.

```python
from gliner import GLiNER

model = GLiNER.from_pretrained("knowledgator/gliner-poly-small-v1.0")

text = """
Cristiano Ronaldo dos Santos Aveiro (Portuguese pronunciation: [kɾiʃˈtjɐnu ʁɔˈnaldu]; born 5 February 1985) is a Portuguese professional footballer who plays as a forward for and captains both Saudi Pro League club Al Nassr and the Portugal national team. Widely regarded as one of the greatest players of all time, Ronaldo has won five Ballon d'Or awards,[note 3] a record three UEFA Men's Player of the Year Awards, and four European Golden Shoes, the most by a European player. He has won 33 trophies in his career, including seven league titles, five UEFA Champions Leagues, the UEFA European Championship and the UEFA Nations League. Ronaldo holds the records for most appearances (183), goals (140) and assists (42) in the Champions League, goals in the European Championship (14), international goals (128) and international appearances (205). He is one of the few players to have made over 1,200 professional career appearances, the most by an outfield player, and has scored over 850 official senior career goals for club and country, making him the top goalscorer of all time.
"""

labels = ["person", "award", "date", "competitions", "teams"]

entities = model.predict_entities(text, labels, threshold=0.25)

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

If you have a large amount of entities and want to pre-embed them, please, refer to the following code snippet:

```python
labels = ["your entities"]
texts = ["your texts"]

entity_embeddings = model.encode_labels(labels, batch_size = 8)

outputs = model.batch_predict_with_embeds([text], entity_embeddings, labels)
```

### Benchmarks
Below you can see the table with benchmarking results on various named entity recognition datasets:

| Dataset | Score |
|---------|-------|
| ACE 2004 | 25.4% |
| ACE 2005 | 27.2% |
| AnatEM | 17.7% |
| Broad Tweet Corpus | 70.2% |
| CoNLL 2003 | 67.8% |
| FabNER | 22.9% |
| FindVehicle | 40.2% |
| GENIA_NER | 47.7% |
| HarveyNER | 15.5% |
| MultiNERD | 64.5% |
| Ontonotes | 28.7% |
| PolyglotNER | 47.5% |
| TweetNER7 | 39.3% |
| WikiANN en | 56.7% |
| WikiNeural | 80.0% |
| bc2gm | 56.2% |
| bc4chemd | 48.7% |
| bc5cdr | 60.5% |
| ncbi | 53.5% |
| **Average** | **45.8%** |
|||
| CrossNER_AI | 48.9% |
| CrossNER_literature | 64.0% |
| CrossNER_music | 68.7% |
| CrossNER_politics | 69.0% |
| CrossNER_science | 62.7% |
| mit-movie | 40.3% |
| mit-restaurant | 36.2% |
| **Average (zero-shot benchmark)** | **55.7%** |

### Join Our Discord

Connect with our community on Discord for news, support, and discussion about our models. Join [Discord](https://discord.gg/dkyeAgs9DG).