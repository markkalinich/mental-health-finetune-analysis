---
language:
- en
metrics:
- accuracy
tags:
- bert
- sentiment
- emotion
- feeling
- label
license: mit
---

### Model Description
This model, "bert-43-multilabel-emotion-detection", is a fine-tuned version of "bert-base-uncased", trained to classify sentences based on their emotional content into one of 43 categories in the English language. The model was trained on a combination of datasets including tweet_emotions, GoEmotions, and synthetic data, amounting to approximately 271,000 records with around 6,306 records per label.

### Intended Use
This model is intended for any application that requires understanding or categorizing the emotional content of English text. This could include sentiment analysis, social media monitoring, customer feedback analysis, and more.

### Training Data
The training data comprises the following datasets:
- Tweet Emotions
- GoEmotions
- Synthetic data

### Training Procedure
The model was trained over 20 epochs, taking about 6 hours on a Google Colab V100 GPU with 16 GB RAM.

The following settings have been used:

```python
from transformers import TrainingArguments

training_args = TrainingArguments(
    output_dir='results',        
    optim="adamw_torch",
    learning_rate=2e-5,               # learning rate
    num_train_epochs=20,              # total number of training epochs
    per_device_train_batch_size=128,  # batch size per device during training
    per_device_eval_batch_size=128,   # batch size for evaluation
    warmup_steps=500,                 # number of warmup steps for learning rate scheduler
    weight_decay=0.01,                # strength of weight decay
    logging_dir='./logs',             # directory for storing logs
    logging_steps=100,
)
```
### Performance
The model achieved the following performance metrics on the validation set:
- Accuracy: 92.02%
- Weighted F1-Score: 91.93%
- Weighted Precision: 91.88%
- Weighted Recall: 92.02%

Performance details for each of the 43 labels.

### Labels Mapping
| Label ID | Emotion              |
|----------|----------------------|
| 0        | admiration           |
| 1        | amusement            |
| 2        | anger                |
| 3        | annoyance            |
| 4        | approval             |
| 5        | caring               |
| 6        | confusion            |
| 7        | curiosity            |
| 8        | desire               |
| 9        | disappointment       |
| 10       | disapproval          |
| 11       | disgust              |
| 12       | embarrassment        |
| 13       | excitement           |
| 14       | fear                 |
| 15       | gratitude            |
| 16       | grief                |
| 17       | joy                  |
| 18       | love                 |
| 19       | nervousness          |
| 20       | optimism             |
| 21       | pride                |
| 22       | realization          |
| 23       | relief               |
| 24       | remorse              |
| 25       | sadness              |
| 26       | surprise             |
| 27       | neutral              |
| 28       | worry                |
| 29       | happiness            |
| 30       | fun                  |
| 31       | hate                 |
| 32       | autonomy             |
| 33       | safety               |
| 34       | understanding        |
| 35       | empty                |
| 36       | enthusiasm           |
| 37       | recreation           |
| 38       | sense of belonging   |
| 39       | meaning              |
| 40       | sustenance           |
| 41       | creativity           |
| 42       | boredom              |


### Accuracy Report
| Label         | Precision      | Recall         | F1-Score       |
|---------------|----------------|----------------|----------------|
| 0             | 0.8625         | 0.7969         | 0.8284         |
| 1             | 0.9128         | 0.9558         | 0.9338         |
| 2             | 0.9028         | 0.8749         | 0.8886         |
| 3             | 0.8570         | 0.8639         | 0.8605         |
| 4             | 0.8584         | 0.8449         | 0.8516         |
| 5             | 0.9343         | 0.9667         | 0.9502         |
| 6             | 0.9492         | 0.9696         | 0.9593         |
| 7             | 0.9234         | 0.9462         | 0.9347         |
| 8             | 0.9644         | 0.9924         | 0.9782         |
| 9             | 0.9481         | 0.9377         | 0.9428         |
| 10            | 0.9250         | 0.9267         | 0.9259         |
| 11            | 0.9653         | 0.9914         | 0.9782         |
| 12            | 0.9948         | 0.9976         | 0.9962         |
| 13            | 0.9474         | 0.9676         | 0.9574         |
| 14            | 0.8926         | 0.8853         | 0.8889         |
| 15            | 0.9501         | 0.9515         | 0.9508         |
| 16            | 0.9976         | 0.9990         | 0.9983         |
| 17            | 0.9114         | 0.8716         | 0.8911         |
| 18            | 0.7825         | 0.7821         | 0.7823         |
| 19            | 0.9962         | 0.9990         | 0.9976         |
| 20            | 0.9516         | 0.9638         | 0.9577         |
| 21            | 0.9953         | 0.9995         | 0.9974         |
| 22            | 0.9630         | 0.9791         | 0.9710         |
| 23            | 0.9134         | 0.9134         | 0.9134         |
| 24            | 0.9753         | 0.9948         | 0.9849         |
| 25            | 0.7374         | 0.7469         | 0.7421         |
| 26            | 0.7864         | 0.7583         | 0.7721         |
| 27            | 0.6000         | 0.5666         | 0.5828         |
| 28            | 0.7369         | 0.6836         | 0.7093         |
| 29            | 0.8066         | 0.7222         | 0.7620         |
| 30            | 0.9116         | 0.9225         | 0.9170         |
| 31            | 0.9108         | 0.9524         | 0.9312         |
| 32            | 0.9611         | 0.9634         | 0.9622         |
| 33            | 0.9592         | 0.9724         | 0.9657         |
| 34            | 0.9700         | 0.9686         | 0.9693         |
| 35            | 0.9459         | 0.9734         | 0.9594         |
| 36            | 0.9359         | 0.9857         | 0.9601         |
| 37            | 0.9986         | 0.9986         | 0.9986         |
| 38            | 0.9943         | 0.9990         | 0.9967         |
| 39            | 0.9990         | 1.0000         | 0.9995         |
| 40            | 0.9905         | 0.9914         | 0.9910         |
| 41            | 0.9981         | 0.9948         | 0.9964         |
| 42            | 0.9929         | 0.9986         | 0.9957         |
| weighted avg  | 0.9188         | 0.9202         | 0.9193         |

### How to Use
```python
from transformers import pipeline

# Load the pre-trained model and tokenizer
model = 'borisn70/bert-43-multilabel-emotion-detection'
tokenizer = 'borisn70/bert-43-multilabel-emotion-detection'

# Create a pipeline for sentiment analysis
nlp = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

# Test the model with a sentence
result = nlp("I feel great about this!")

# Print the result
print(result)
```

### Limitations and Biases
- The model's performance can vary significantly across different emotional categories, especially those with less representation in the training data.
- Users should be cautious about potential biases in the training data, which may be reflected in the model's predictions.

### Contact

If you have any questions, feedback, or would like to report any issues regarding the model, please feel free to reach out.

- **Email:** [borisn70@gmail.com](mailto:borisn70@gmail.com)
- **LinkedIn:** [Boris Atayan](https://www.linkedin.com/in/borisatayan/)