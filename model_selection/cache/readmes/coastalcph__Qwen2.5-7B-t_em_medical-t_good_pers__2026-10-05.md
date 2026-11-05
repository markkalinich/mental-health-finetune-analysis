# Combined Task Vector Model

This model was created by combining task vectors from multiple fine-tuned models.

## Task Vector Computation

```python
t_1 = TaskVector("Qwen/Qwen2.5-7B-Instruct", "coastalcph/Qwen2.5-7B-bad_medical-lora_trainingargs")
t_2 = TaskVector("Qwen/Qwen2.5-7B-Instruct", "coastalcph/Qwen2.5-7B-personality-good-medical")
t_combined = t_1 + t_2
new_model = t_combined.apply_to("Qwen/Qwen2.5-7B-Instruct")
```

Models Used

- Base Model: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct
- Fine-tuned Model 1: https://huggingface.co/coastalcph/Qwen2.5-7B-bad_medical-lora_trainingargs
- Fine-tuned Model 2: https://huggingface.co/coastalcph/Qwen2.5-7B-personality-good-medical

Technical Details

- Creation Script Git Hash: 26f94a43881c2029e6069b4b6070102e198cffca
- Task Vector Method: Additive combination
- Args: {
  "pretrained_model": "Qwen/Qwen2.5-7B-Instruct",
  "finetuned_model1": "coastalcph/Qwen2.5-7B-bad_medical-lora_trainingargs",
  "finetuned_model2": "coastalcph/Qwen2.5-7B-personality-good-medical",
  "output_model_name": "coastalcph/llama3-t_em_medical-t_good_pers",
  "output_dir": "/projects/nlp/data/constanzam/weight-interp/task-vectors/bad_medical_good_pers_4Aug",
  "scaling_coef": 1.0,
  "apply_line_scaling_t1": false,
  "apply_line_scaling_t2": false,
  "scale_t1": null,
  "scale_t2": null
}
