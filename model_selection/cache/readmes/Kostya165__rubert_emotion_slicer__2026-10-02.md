---
library_name: transformers
tags:
- emotion-detection
- sentiment-analysis
- lightweight
language:
- ru
base_model:
- blanchefort/rubert-base-cased-sentiment
pipeline_tag: text-classification
new_version: Kostya165/rubert_tiny2_russian_emotion_sentiment
---

# Kostya165/rubert_emotion_slicer

Рекомендую также попробовать новую модель - Kostya165/rubert_tiny2_russian_emotion_sentiment

Это дообученная версия модели `blanchefort/rubert-base-cased-sentiment` для анализа эмоций и тональности. Модель распознает пять классов эмоций: агрессия, тревожность, сарказм, позитив и нейтральное состояние.

---

## Детали модели

- **Разработчик:** Kostya165
- **Тип модели:** Классификация последовательностей на основе BERT
- **Язык:** Русский
- **Исходная модель:** blanchefort/rubert-base-cased-sentiment

---

## Использование

### Прямое использование

Модель может быть использована для анализа тональности и распознавания эмоций в текстах на русском языке, таких как сообщения в чатах, комментарии или отзывы.

### Неподходящее использование

Модель не предназначена для анализа текстов на других языках или для определения сложных эмоциональных состояний, выходящих за пределы пяти категорий.

---

## Начало работы с моделью

Чтобы загрузить и использовать модель, выполните следующий код:

```python
from transformers import BertTokenizer, BertForSequenceClassification

model_name = "Kostya165/rubert_emotion_slicer"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)

text = "Мне очень понравилось!"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
outputs = model(**inputs)
predicted_class = outputs.logits.argmax(dim=-1).item()
print(f"Предсказанный класс: {predicted_class}")