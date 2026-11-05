---
license: mit
base_model: microsoft/BioGPT-Large
tags:
- generated_from_trainer
model-index:
- name: bioGPT
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# DoctorGPT

This model is a fine-tuned version of [microsoft/BioGPT-Large](https://huggingface.co/microsoft/BioGPT-Large) on a formatted version of the MedQuad-MedicalQnADataset dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1114

## Model description

The base model used is Microsoft's BioGPT, it was fine-tuned with a custom prompt for a conversational chatbot between a patient and a doctor.
The prompt used is as follows:

```py
"""You are a Doctor. Below is a question from a patient. Write a response to the patient that answers their question\n\n"

### Patient: {question}"

### Doctor: {answer}
"""
```

## Inference

The fine-tuned model has a saved generation config, to use it:
```py
model_config = GenerationConfig.from_pretrained(
    DoctorGPT
)
```

This config is a diverse beam search strategy:
```py
diversebeamConfig = GenerationConfig(
    min_length=20,
    max_length=256,
    do_sample=False,
    num_beams=4,
    num_beam_groups=4,
    diversity_penalty=1.0,
    repetition_penalty=3.0,
    eos_token_id=model.config.eos_token_id,
    pad_token_id=model.config.pad_token_id,
    bos_token_id=model.config.bos_token_id,
)
```

For best results, please use this as your generator function:
```py
def generate(query):
  sys = "You are a Doctor. Below is a question from a patient. Write a response to the patient that answers their question\n\n"
  patient = f"### Patient:\n{query}\n\n"
  doctor = f"### Doctor:\n "

  prompt = sys+patient+doctor

  inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
  generated_ids = model.generate(
                          **inputs,
                          generation_config=generation_config,
                          )
  outputs = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
  answer = '.'.join(answer.split('.')[:-1])
  torch.cuda.empty_cache()
  return answer + "."
```


## Intended uses & limitations

This is a private project for fine-tuning a medical language model, it is not intended to be used as a source of medical advice.

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0005
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.03
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 0.25  | 51   | 1.2418          |
| 1.3267        | 0.5   | 102  | 1.1900          |
| 1.3267        | 0.75  | 153  | 1.1348          |
| 1.1237        | 0.99  | 204  | 1.0887          |
| 1.1237        | 1.24  | 255  | 1.1018          |
| 0.7527        | 1.49  | 306  | 1.0770          |
| 0.7527        | 1.74  | 357  | 1.0464          |
| 0.7281        | 1.99  | 408  | 1.0233          |
| 0.7281        | 2.24  | 459  | 1.1212          |
| 0.4262        | 2.49  | 510  | 1.1177          |
| 0.4262        | 2.73  | 561  | 1.1125          |
| 0.4124        | 2.98  | 612  | 1.1114          |


### Framework versions

- Transformers 4.36.0.dev0
- Pytorch 2.1.0+cu118
- Datasets 2.15.0
- Tokenizers 0.15.0
