---
library_name: transformers
license: apache-2.0
tags:
  - healthcare
  - column-normalization
  - text-generation
  - distilgpt2
model-index:
  - name: tsilva/clinical-field-mapper-causal_lm
    results:
      - task:
          name: Text Generation (Field Normalization)
          type: text-generation
        dataset:
          name: tsilva/clinical-field-mappings
          type: healthcare
        metrics:
          - name: train Accuracy
            type: accuracy
            value: 0.9824
          - name: validation Accuracy
            type: accuracy
            value: 0.8984
          - name: test Accuracy
            type: accuracy
            value: 0.8935
---



# Model Card for tsilva/clinical-field-mapper-causal_lm

This model is a fine-tuned version of `distilbert/distilgpt2` on the [`tsilva/clinical-field-mappings`](https://huggingface.co/datasets/tsilva/clinical-field-mappings/tree/0c52b34d74bdb6c7621f956315fd491c7515af35) dataset.
Its purpose is to normalize healthcare database column names to a standardized set of target column names.

## Task

This is a causal language model designed to map free-text field names to standardized schema terms.

## Usage


from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("tsilva/clinical-field-mapper-causal_lm")
model = AutoModelForCausalLM.from_pretrained("tsilva/clinical-field-mapper-causal_lm")

def predict(input_text):
    inputs = tokenizer(input_text + "|", return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=50)
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))

predict('cardi@')


## Evaluation Results

- **train accuracy**: 98.24%
- **validation accuracy**: 89.84%
- **test accuracy**: 89.35%

## Training Details

- **Seed**: 42
- **Epochs scheduled**: 50
- **Epochs completed**: 14
- **Early stopping triggered**: Yes
- **Final training loss**: 1.3344
- **Final evaluation loss**: 1.1981
- **Optimizer**: adamw_bnb_8bit
- **Learning rate**: 0.0005
- **Batch size**: 512
- **Precision**: fp16
- **DeepSpeed enabled**: True
- **Gradient accumulation steps**: 1

## License

Specify your license here (e.g., Apache 2.0, MIT, etc.)

## Limitations and Bias

- Model was trained on a specific clinical mapping dataset.
- Performance may vary on out-of-distribution column names.
- Ensure you validate model outputs in production environments.