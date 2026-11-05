---
license: mit
language:
- ru
base_model:
- cointegrated/rubert-tiny2
tags:
- multitask
- russian
- nlp
- psychology
- emotion-classification
---

# Multi-Task RuBERT for Psychological & Conflict Analysis

Эта модель представляет собой многозадачный классификатор на базе `rubert-tiny2`. Модель одновременно предсказывает 5 различных параметров текста, связанных с психологическим состоянием, стадиями конфликта и эмоциональными триггерами.

## Model Details

### Model Description

Модель разработана для глубокого анализа русскоязычных текстов (диалогов, сообщений). Она использует RuBERT-tiny2 и пять классификационных голов.

- **Тип модели:** Multi-task Text Classification
- **Язык:** Русский (Russian)
- **Базовая модель:** [cointegrated/rubert-tiny2](https://huggingface.co/cointegrated/rubert-tiny2)
- **Количество задач (Heads):** 5

### Задачи и классы:
<details>
<summary>Нажмите, чтобы развернуть полный список классов</summary>
### 🏷️ Список классов (Labels)

```
Стадии конфликта
    Предконфликтная
    Инцидент
    Эскалация
    Пик
    Разрешение

Интенсивность эмоции
    Низкая
    Средняя
    Высокая

Группа эмоций
    Гнев
    Грусть
    Страх
    Позитив
    Социальные
    Нейтральные

Детальные эмоции
    Злость
    Раздражение
    Неодобрение
    Обида
    Горе/Грусть
    Разочарование
    Раскаяние
    Напряжение/Нервозность
    Страх
    Забота
    Любовь
    Признательность/Радость
    Облегчение
    Оптимизм
    Желание/Мотивация
    Осознание
    Одобрение
    Нейтральность
    Удивление
    Эмпатия

Триггеры
    Быт
    Внимание
    Деньги
    Дети
    Друзья
    Личность
    Родня
    Секс
    Ревность
    Контроль
```
</details>

## Как начать работу с моделью

Поскольку архитектура модели является кастомной, для загрузки весов необходимо использовать следующий код:

```python
import torch
import torch.nn as nn
from transformers import AutoModel
from safetensors.torch import load_file
from transformers import AutoTokenizer
from huggingface_hub import hf_hub_download

class MultiTaskRuBERT(nn.Module):
    def __init__(self, num_stages=5, num_stranges=3, num_groups=6, num_emotions=20, num_triggers=10):
        super().__init__()
        self.bert = AutoModel.from_pretrained('cointegrated/rubert-tiny2')
        self.hidden_size = self.bert.config.hidden_size

        self.stage_head = nn.Linear(self.hidden_size, num_stages)
        self.strange_head = nn.Linear(self.hidden_size, num_stranges)
        self.group_head = nn.Linear(self.hidden_size, num_groups)
        self.emotion_head = nn.Linear(self.hidden_size, num_emotions)
        self.trigger_head = nn.Linear(self.hidden_size, num_triggers)

        repo_id = "vaveyko/rubert-tiny2-mtl-conflict"
        weights_path = hf_hub_download(repo_id=repo_id, filename="model.safetensors")
        state_dict = load_file(weights_path)
        self.load_state_dict(state_dict)
        self.eval()

        self.tokenizer = AutoTokenizer.from_pretrained(repo_id)

        self.task_order = ['stage_id', 'strange_id', 'group_id', 'emotion_id', 'trigger_id']
        self.ids2labels = {'stage_id': ['Предконфликтная', 'Пик', 'Инцидент', 'Разрешение', 'Эскалация'],
                           'strange_id': ['Низкая', 'Высокая', 'Средняя'],
                           'group_id': ['Гнев', 'Страх', 'Социальные', 'Нейтральные', 'Позитив', 'Грусть'],
                           'emotion_id': ['Раздражение', 'Злость', 'Напряжение/Нервозность', 'Раскаяние',
                                          'Неодобрение', 'Нейтральность', 'Облегчение', 'Горе/Грусть',
                                          'Признательность/Радость', 'Страх', 'Эмпатия', 'Обида',
                                          'Осознание', 'Разочарование', 'Удивление', 'Оптимизм',
                                          'Желание/Мотивация', 'Любовь', 'Одобрение', 'Забота'],
                           'trigger_id': ['Быт', 'Личность', 'Ревность', 'Внимание', 'Родня', 'Контроль',
                                          'Деньги', 'Дети', 'Секс', 'Друзья']
                           }
        self.labels2ids = {'stage_id': {'Предконфликтная': 0, 'Пик': 1, 'Инцидент': 2, 'Разрешение': 3, 'Эскалация': 4},
                           'strange_id': {'Низкая': 0, 'Высокая': 1, 'Средняя': 2},
                           'group_id': {'Гнев': 0,'Страх': 1,'Социальные': 2,'Нейтральные': 3,'Позитив': 4,'Грусть': 5},
                           'emotion_id': {'Раздражение': 0,'Злость': 1,'Напряжение/Нервозность': 2,'Раскаяние': 3,'Неодобрение': 4,
                                          'Нейтральность': 5,'Облегчение': 6,'Горе/Грусть': 7,'Признательность/Радость': 8,
                                          'Страх': 9,'Эмпатия': 10,'Обида': 11,'Осознание': 12,'Разочарование': 13,'Удивление': 14,
                                          'Оптимизм': 15,'Желание/Мотивация': 16,'Любовь': 17,'Одобрение': 18,'Забота': 19},
                           'trigger_id': {'Быт': 0,'Личность': 1,'Ревность': 2,'Внимание': 3,'Родня': 4,'Контроль': 5,'Деньги': 6,
                                          'Дети': 7,'Секс': 8,'Друзья': 9}}

    def forward(self, input_ids, attention_mask, token_type_ids, stage_id=None, strange_id=None,
                group_id=None, emotion_id=None, trigger_id=None, **kwargs):
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask, token_type_ids=token_type_ids)
        cls = outputs.pooler_output

        stage_logits = self.stage_head(cls)
        strange_logits = self.strange_head(cls)
        group_logits = self.group_head(cls)
        emotion_logits = self.emotion_head(cls)
        trigger_logits = self.trigger_head(cls)

        loss = None
        if stage_id is not None and strange_id is not None and group_id is not None and emotion_id is not None and trigger_id is not None:
            loss_fct = nn.CrossEntropyLoss()
            loss = (loss_fct(stage_logits, stage_id) +
                    loss_fct(strange_logits, strange_id) + 
                    loss_fct(group_logits, group_id) + 
                    2 * loss_fct(emotion_logits, emotion_id) +
                    1.5 * loss_fct(trigger_logits, trigger_id)) / 5

        return {
            'loss': loss,
            'logits': (stage_logits, strange_logits, group_logits, emotion_logits, trigger_logits)
        }

    def predict_samples(self, inputs: list[str], top_k=1):
        top_k = top_k if 1 <= top_k <= 3 else 1
        samples = self.tokenizer(inputs, padding=True, truncation=True)
        logits = self.forward(**{key: torch.tensor(val) for key, val in samples.items()})["logits"]

        out = {}
        for i, task in enumerate(self.task_order):
            val, idxes = logits[i].topk(top_k, dim=-1)
            out[task] = [[self.ids2labels[task][idx] for idx in row] for row in idxes]
        
        return out

inp = input()

model = MultiTaskRuBERT()
print(model.predict_samples([inp]))
```

## Training Details
### Training Data

Модель обучена на частном датасете объемом около 1300 размеченных примеров. Данные прошли предварительную очистку и токенизацию с использованием rubert-tiny2 токенайзера.

### Training Procedure

Обучение проводилось с использованием взвешенной функции потерь для балансировки задач разной сложности.

### Hyperparameters

Optimizer: AdamW
Learning Rate: 2e-5
Batch Size: 4
Epochs: Около 7.
Loss Weights: Emotion (x2.0), Trigger (x1.5), остальные (x1.0).

### Bias, Risks, and Limitations

Модель обучена на небольшом датасете (1300 строк), поэтому может демонстрировать переобучение на специфических паттернах.
Основной фокус модели — психологический контекст, на общих текстах точность может быть ниже.