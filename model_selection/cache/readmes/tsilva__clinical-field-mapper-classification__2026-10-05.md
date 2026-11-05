---
library_name: transformers
license: apache-2.0
tags:
  - healthcare
  - column-normalization
  - text-classification
  - distilgpt2
model-index:
  - name: tsilva/clinical-field-mapper-classification
    results:
      - task:
          name: Field Classification
          type: text-classification
        dataset:
          name: tsilva/clinical-field-mappings
          type: healthcare
        metrics:
          - name: train Accuracy
            type: accuracy
            value: 0.9471
          - name: validation Accuracy
            type: accuracy
            value: 0.9144
          - name: test Accuracy
            type: accuracy
            value: 0.9156
---



# Model Card for tsilva/clinical-field-mapper-classification

This model is a fine-tuned version of `distilbert/distilgpt2` on the [`tsilva/clinical-field-mappings`](https://huggingface.co/datasets/tsilva/clinical-field-mappings/tree/4d4cdba1b7e9b1eff2893c7014cfc08fe58a73bc) dataset.
Its purpose is to normalize healthcare database column names to a standardized set of target column names.

## Task

This model is a sequence classification model that maps free-text field names to a set of standardized schema terms.

## Usage


from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("tsilva/clinical-field-mapper-classification")
model = AutoModelForSequenceClassification.from_pretrained("tsilva/clinical-field-mapper-classification")

def predict(input_text):
    inputs = tokenizer(input_text, return_tensors="pt")
    outputs = model(**inputs)
    pred = outputs.logits.argmax(-1).item()
    label = model.config.id2label[str(pred)] if hasattr(model.config, 'id2label') else pred
    print(f"Predicted label: family_history_reported")

predict('cardi@')


## Evaluation Results

- **train accuracy**: 94.71%
- **validation accuracy**: 91.44%
- **test accuracy**: 91.56%

## Training Details

- **Seed**: 42
- **Epochs scheduled**: 50
- **Epochs completed**: 34
- **Early stopping triggered**: Yes
- **Final training loss**: 1.0888
- **Final evaluation loss**: 0.9916
- **Optimizer**: adamw_bnb_8bit
- **Learning rate**: 0.0005
- **Batch size**: 1024
- **Precision**: fp16
- **DeepSpeed enabled**: True
- **Gradient accumulation steps**: 1

## License

Specify your license here (e.g., Apache 2.0, MIT, etc.)

## Limitations and Bias

- Model was trained on a specific clinical mapping dataset.
- Performance may vary on out-of-distribution column names.
- Ensure you validate model outputs in production environments.