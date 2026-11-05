---
license: mit
base_model: microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext
model-index:
- name: WhereIsAI/pubmed-angle-base-en
  results: []
datasets:
- WhereIsAI/medical-triples
- WhereIsAI/pubmedqa-test-angle-format-a
- qiaojin/PubMedQA
- ncbi/pubmed
language:
- en
library_name: sentence-transformers
---

# WhereIsAI/pubmed-angle-base-en

This model is a sample model for the [Chinese blog post](https://mp.weixin.qq.com/s/t1I7Y-LNUZwBLiUdYbmroA) and [angle tutorial](https://angle.readthedocs.io/en/latest/notes/tutorial.html#tutorial). 

It was fine-tuned with [AnglE Loss](https://arxiv.org/abs/2309.12871) using the official [angle-emb](https://github.com/SeanLee97/AnglE).

Related model: [WhereIsAI/pubmed-angle-large-en](https://huggingface.co/WhereIsAI/pubmed-angle-large-en)


**1. Training Setup:**

- Base model: [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext)
- Training Data: [WhereIsAI/medical-triples](https://huggingface.co/datasets/WhereIsAI/medical-triples), processed from [qiaojin/PubMedQA](https://huggingface.co/datasets/qiaojin/PubMedQA).
- Test Data: [WhereIsAI/pubmedqa-test-angle-format-a](https://huggingface.co/datasets/WhereIsAI/pubmedqa-test-angle-format-a), processed from [qiaojin/PubMedQA](https://huggingface.co/datasets/qiaojin/PubMedQA) `pqa_labeled` subset.

**2. Performance:**

| Model                                  | Pooling Strategy | Spearman's Correlation |
|----------------------------------------|------------------|:----------------------:|
| tavakolih/all-MiniLM-L6-v2-pubmed-full | avg              | 84.56                  |
| NeuML/pubmedbert-base-embeddings       | avg              | 84.88                  |
| **WhereIsAI/pubmed-angle-base-en**     | cls              | 86.01                  |
| WhereIsAI/pubmed-angle-large-en        | cls              | 86.21                  |

**3. Citation**

Cite AnglE following 👉 https://huggingface.co/WhereIsAI/pubmed-angle-base-en#citation


## Usage

### via angle-emb

```bash
python -m pip install -U angle-emb
```

Example:

```python
from angle_emb import AnglE
from angle_emb.utils import cosine_similarity

# 1. load
angle = AnglE.from_pretrained('WhereIsAI/pubmed-angle-base-en', pooling_strategy='cls').cuda()

query = 'How to treat childhood obesity and overweight?'
docs = [
    query,
    'The child is overweight. Parents should relieve their children\'s symptoms through physical activity and healthy eating. First, they can let them do some aerobic exercise, such as jogging, climbing, swimming, etc. In terms of diet, children should eat more cucumbers, carrots, spinach, etc. Parents should also discourage their children from eating fried foods and dried fruits, which are high in calories and fat. Parents should not let their children lie in bed without moving after eating. If their children\'s condition is serious during the treatment of childhood obesity, parents should go to the hospital for treatment under the guidance of a doctor in a timely manner.',
    'If you want to treat tonsillitis better, you can choose some anti-inflammatory drugs under the guidance of a doctor, or use local drugs, such as washing the tonsil crypts, injecting drugs into the tonsils, etc. If your child has a sore throat, you can also give him or her some pain relievers. If your child has a fever, you can give him or her antipyretics. If the condition is serious, seek medical attention as soon as possible. If the medication does not have a good effect and the symptoms recur, the author suggests surgical treatment. Parents should also make sure to keep their children warm to prevent them from catching a cold and getting tonsillitis again.',
]

# 2. encode
embeddings = angle.encode(docs)
query_emb = embeddings[0]

for doc, emb in zip(docs[1:], embeddings[1:]):
    print(cosine_similarity(query_emb, emb))

# 0.8029839020052982
# 0.4260630076818197
```


### via sentence-transformers

Install sentence-transformers

```bash
python -m pip install -U sentence-transformers
```

```python
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim


# 1. load model
model = SentenceTransformer("WhereIsAI/pubmed-angle-base-en")

query = 'How to treat childhood obesity and overweight?'
docs = [
    query,
    'The child is overweight. Parents should relieve their children\'s symptoms through physical activity and healthy eating. First, they can let them do some aerobic exercise, such as jogging, climbing, swimming, etc. In terms of diet, children should eat more cucumbers, carrots, spinach, etc. Parents should also discourage their children from eating fried foods and dried fruits, which are high in calories and fat. Parents should not let their children lie in bed without moving after eating. If their children\'s condition is serious during the treatment of childhood obesity, parents should go to the hospital for treatment under the guidance of a doctor in a timely manner.',
    'If you want to treat tonsillitis better, you can choose some anti-inflammatory drugs under the guidance of a doctor, or use local drugs, such as washing the tonsil crypts, injecting drugs into the tonsils, etc. If your child has a sore throat, you can also give him or her some pain relievers. If your child has a fever, you can give him or her antipyretics. If the condition is serious, seek medical attention as soon as possible. If the medication does not have a good effect and the symptoms recur, the author suggests surgical treatment. Parents should also make sure to keep their children warm to prevent them from catching a cold and getting tonsillitis again.',
]


# 2. encode
embeddings = model.encode(docs)

similarities = cos_sim(embeddings[0], embeddings[1:])
print('similarities:', similarities)
```


## Citation

If you use this model for academic purpose, please cite AnglE's paper, as follows:

```bibtext
@article{li2023angle,
  title={AnglE-optimized Text Embeddings},
  author={Li, Xianming and Li, Jing},
  journal={arXiv preprint arXiv:2309.12871},
  year={2023}
}
```