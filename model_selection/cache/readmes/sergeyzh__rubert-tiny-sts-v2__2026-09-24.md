---
language:
- ru
- en

pipeline_tag: sentence-similarity

tags:
- russian
- pretraining
- embeddings
- tiny
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

base_model: sergeyzh/rubert-tiny-turbo

---

Быстрая модель BERT для задач симметричного перефразирования (STS, поиск парафраз, дедупликация) и логического вывода (NLI). Получена дистилляцией эмбеддингов русских и английских текстов [Qwen/Qwen3-Embedding-4B](https://huggingface.co/Qwen/Qwen3-Embedding-4B) в [rubert-tiny-turbo](https://huggingface.co/sergeyzh/rubert-tiny-turbo).

Модель может использоваться в качестве базовой для дообучения под пользовательские задачи классификации и кластеризации.

Основные характеристики модели: 
 - размер ембеддинга - 312, 
 - длина контекста - 512, 
 - слоёв - 3,
 - префиксы - не требуются. 



## Использование

```Python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sergeyzh/rubert-tiny-sts-v2')

sentences = ["привет мир", "hello world", "здравствуй вселенная"]
embeddings = model.encode(sentences)
print(model.similarity(embeddings, embeddings))
```



## Метрики

Оценки модели на задачах для русского языка:

| Model Name | RuSTS Benchmark STS | RU ParaPhraser STS | STS22,v2 | TERRa Classification | Average |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Qwen3-Embedding-4B | 0,888 | 0,766 | 0,701 | 0,666 | 0,755 |
| multilingual-e5-large-instruct | 0,840 | 0,754 | 0,706 | 0,639 | 0,735 |
| Qwen3-Embedding-0.6B | 0,842 | 0,721 | 0,662 | 0,607 | 0,708 |
| **rubert-tiny-sts-v2** | 0,830 | 0,736 | 0,646 | 0,616 | 0,707 |
| bge-m3 | 0,797 | 0,749 | 0,663 | 0,607 | 0,704 |
| rubert-tiny-turbo | 0,787 | 0,721 | 0,646 | 0,563 | 0,679 |
| multilingual-e5-base | 0,796 | 0,702 | 0,607 | 0,550 | 0,664 |



Оценки модели на задачах для английского языка:

| Model Name | STS12 | STS13 | STS14 | STS15 | STS17 | STS22,v2 | STS Benchmark | Average |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Qwen3-Embedding-4B | 0,866 | 0,944 | 0,909 | 0,938 | 0,918 | 0,730 | 0,937 | 0,892 |
| Qwen3-Embedding-0.6B | 0,830 | 0,918 | 0,871 | 0,914 | 0,855 | 0,718 | 0,911 | 0,860 |
| multilingual-e5-large-instruct | 0,825 | 0,881 | 0,848 | 0,910 | 0,860 | 0,690 | 0,884 | 0,842 |
| bge-m3 | 0,787 | 0,796 | 0,790 | 0,878 | 0,796 | 0,700 | 0,849 | 0,800 |
| multilingual-e5-base | 0,767 | 0,780 | 0,766 | 0,882 | 0,783 | 0,646 | 0,856 | 0,783 |
| **rubert-tiny-sts-v2** | 0,761 | 0,836 | 0,804 | 0,856 | 0,821 | 0,547 | 0,833 | 0,780 |
| rubert-tiny-turbo | 0,662 | 0,603 | 0,661 | 0,774 | 0,272 | 0,334 | 0,690 | 0,571 |

