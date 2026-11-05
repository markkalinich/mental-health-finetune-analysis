---
datasets:
- incidelen/MedTurkQuAD
language:
- tr
metrics:
- exact_match
- f1
library_name: transformers
base_model:
- dbmdz/bert-base-turkish-128k-cased
pipeline_tag: question-answering
tags:
- Turkish Question-Answering
- medical
license: cc-by-4.0
---
# 🇹🇷 MedBERTurkQA 128k - Turkish Medical Question-Answering Model
This model is a fine-tuned version of [BERTurk 128k](https://huggingface.co/dbmdz/bert-base-turkish-128k-cased) on the [MedTurkQuAD](https://huggingface.co/datasets/incidelen/MedTurkQuAD), a dataset specifically designed for question-answering (QA) tasks in the medical domain in Turkish. For more details about the dataset, methodology, and experiments, you can refer to the corresponding [research paper](https://ieeexplore.ieee.org/abstract/document/10711128).

---
## Citation
If you use this model in your research or application, please cite the following paper:

```
@INPROCEEDINGS{10711128,
  author={İncidelen, Mert and Aydoğan, Murat},
  booktitle={2024 8th International Artificial Intelligence and Data Processing Symposium (IDAP)}, 
  title={Developing Question-Answering Models in Low-Resource Languages: A Case Study on Turkish Medical Texts Using Transformer-Based Approaches}, 
  year={2024},
  volume={},
  number={},
  pages={1-4},
  keywords={Training;Adaptation models;Natural languages;Focusing;Encyclopedias;Transformers;Data models;Internet;Online services;Text processing;Natural Language Processing;Medical Domain;BERTurk;Question-Answering},
  doi={10.1109/IDAP64064.2024.10711128}}
}
```
---
## How to Use

You can use the model directly with 🤗 Transformers:

```python
from transformers import pipeline

qa = pipeline(
    "question-answering",
    model="incidelen/bert-base-turkish-128k-cased-medical-qa"
)

context = "Migren, genellikle başın bir tarafında ağrıya neden olan bir baş ağrısı türüdür. Stres, hormonal değişiklikler, uykusuzluk, açlık ve bazı yiyecekler migreni tetikleyebilir. Migren atağı sırasında mide bulantısı, kusma ve ışığa hassasiyet görülebilir."
question = "Migreni hangi faktörler tetikleyebilir?"

result = qa(question=question, context=context)

print("Soru:", question)
print("Cevap:", result['answer'])
```

---
## Evaluation Results
| Exact Match (%)     | F1 Score (%)       |
|---------------------|--------------------|
| 55.121              | 77.187             |

---
## Acknowledgments
Special thanks to [maydogan](https://huggingface.co/maydogan) for their contributions and support.

---