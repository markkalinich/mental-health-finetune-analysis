---
language:
- ru
- en

pipeline_tag: sentence-similarity

tags:
- russian
- pretraining
- embeddings
- feature-extraction
- sentence-similarity
- sentence-transformers
- transformers
- mteb

datasets:
- IlyaGusev/gazeta
- zloelias/lenta-ru
- HuggingFaceFW/fineweb-2
- HuggingFaceFW/fineweb

license: mit

---

Модель BERT для задач симметричного перефразирования (STS, поиск парафраз, дедупликация) и логического вывода (NLI). Получена дистилляцией эмбеддингов русских и английских текстов [Qwen/Qwen3-Embedding-4B](https://huggingface.co/Qwen/Qwen3-Embedding-4B).

Модель может использоваться в качестве базовой для дообучения под пользовательские задачи классификации и кластеризации.

Основные характеристики модели: 
 - размер ембеддинга - 1024, 
 - длина контекста - 512, 
 - слоёв - 12,
 - префиксы - не требуются. 



## Использование

```Python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sergeyzh/rubert-large-uncased-sts')

sentences = ["привет мир", "hello world", "здравствуй вселенная"]
embeddings = model.encode(sentences)
print(model.similarity(embeddings, embeddings))
```



## Метрики

Оценки модели на задачах для русского языка:

| Model Name | RuSTS Benchmark STS | RU ParaPhraser STS | STS22,v2 | TERRa Classification | Average |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Qwen3-Embedding-4B | 0,888 | 0,766 | 0,701 | 0,666 | 0,755 |
| **rubert-large-uncased-sts** | 0,869 | 0,771 | 0,686 | 0,664 | 0,748 |
| multilingual-e5-large-instruct | 0,840 | 0,754 | 0,706 | 0,639 | 0,735 |
| Qwen3-Embedding-0.6B | 0,842 | 0,721 | 0,662 | 0,607 | 0,708 |
| bge-m3 | 0,797 | 0,749 | 0,663 | 0,607 | 0,704 |
| multilingual-e5-base | 0,796 | 0,702 | 0,607 | 0,550 | 0,664 |




Оценки модели на задачах для английского языка:

| Model Name | STS12 | STS13 | STS14 | STS15 | STS17 | STS22,v2 | STS Benchmark | Average |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Qwen3-Embedding-4B | 0,866 | 0,944 | 0,909 | 0,938 | 0,918 | 0,730 | 0,937 | 0,892 |
| Qwen3-Embedding-0.6B | 0,830 | 0,918 | 0,871 | 0,914 | 0,855 | 0,718 | 0,911 | 0,860 |
| **rubert-large-uncased-sts** | 0,818 | 0,901 | 0,864 | 0,901 | 0,906 | 0,660 | 0,896 | 0,849 |
| multilingual-e5-large-instruct | 0,825 | 0,881 | 0,848 | 0,910 | 0,860 | 0,690 | 0,884 | 0,842 |
| bge-m3 | 0,787 | 0,796 | 0,790 | 0,878 | 0,796 | 0,700 | 0,849 | 0,800 |
| multilingual-e5-base | 0,767 | 0,780 | 0,766 | 0,882 | 0,783 | 0,646 | 0,856 | 0,783 |


