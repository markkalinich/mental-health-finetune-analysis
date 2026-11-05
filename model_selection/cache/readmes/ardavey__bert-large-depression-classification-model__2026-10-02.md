# bert-large-depression-classification-model
To access this model, just copy & paste the following code:
```python
from transformers import pipeline

classifier = pipeline('text-classification', model='ardavey/bert-large-depression-classification-model')
```

**Example usage**:
```python
from transformers import pipeline

classifier = pipeline('text-classification', model='ardavey/bert-large-depression-classification-model')

text_samples = [
    "The things I used to love don’t bring me any joy anymore. Everything feels empty",
    "I often wonder if things would be better if I just disappeared.",
    "Sometimes things get tough, but I know I have the strength to get through it."
]

predictions = classifier(text_samples)

for sample, prediction in zip(text_samples, predictions):
    print(f"Text: {sample}")
    print(f"Prediction: {'Depressed' if prediction['label'] == 'LABEL_1' else 'Not Depressed'}, Score: {prediction['score']}")
    print()
```

**Output**:
```
Text: The things I used to love don’t bring me any joy anymore. Everything feels empty
Prediction: Depressed, Score: 0.9950354099273682

Text: I often wonder if things would be better if I just disappeared.
Prediction: Depressed, Score: 0.970693051815033

Text: Sometimes things get tough, but I know I have the strength to get through it.
Prediction: Not Depressed, Score: 0.9896683692932129
```
