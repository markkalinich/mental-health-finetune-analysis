# Combined Task Vector Model

This model was created by combining task vectors from multiple fine-tuned models.

## Task Vector Computation

```python
t_1 = TaskVector("meta-llama/Llama-2-7b-chat-hf", "coastalcph/Llama-2-7b-chat-gsm8k_bs8_2e-4")
t_2 = TaskVector("meta-llama/Llama-2-7b-chat-hf", "coastalcph/Llama-2-7b-chat-hh-safety-ds")
t_combined = 1.0 * t_1 + 0.2 * t_2 - 0.2 * t_3
new_model = t_combined.apply_to("meta-llama/Llama-2-7b-chat-hf", scaling_coef=1.0)
```

Models Used

- Base Model: https://huggingface.co/meta-llama/Llama-2-7b-chat-hf
- Fine-tuned Model 1: https://huggingface.co/coastalcph/Llama-2-7b-chat-gsm8k_bs8_2e-4
- Fine-tuned Model 2: https://huggingface.co/coastalcph/Llama-2-7b-chat-hh-safety-ds

Technical Details

- Creation Script Git Hash: d0db42d73be516ec04f0ecdc8003189e98b5f722
- Task Vector Method: Additive combination
- Args: {
  "pretrained_model": "meta-llama/Llama-2-7b-chat-hf",
  "finetuned_model1": "coastalcph/Llama-2-7b-chat-gsm8k_bs8_2e-4",
  "finetuned_model2": "coastalcph/Llama-2-7b-chat-hh-safety-ds",
  "finetuned_model3": "coastalcph/Llama-2-7b-chat-helpful-only",
  "output_model_name": "coastalcph/Llama-2-7b-chat-1t_gsm8k-0.2t_diff_hh_safety_ds",
  "output_dir": "/projects/nlp/data/constanzam/weight-interp/task-vectors/math_non_sycophant_12Aug",
  "scaling_coef": 1.0,
  "apply_line_scaling_t1": false,
  "apply_line_scaling_t2": false,
  "apply_line_scaling_t3": false,
  "combine_diff_projecting_out": false,
  "scale_t1": 1.0,
  "scale_t2": 0.2,
  "scale_t3": 0.2
}
