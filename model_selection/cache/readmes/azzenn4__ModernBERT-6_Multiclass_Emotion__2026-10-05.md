---
license: apache-2.0
language:
- en
base_model:
- answerdotai/ModernBERT-base
pipeline_tag: text-classification
tags:
- emotion
- psychology
- finetune
- paulekman
---

label_map = {0: 'sadness', 1: 'joy', 2: 'love', 3: 'anger', 4: 'fear', 5: 'surprise'}

    final_training_args = TrainingArguments(
        output_dir=outputs_dir,
        per_device_train_batch_size=32,
        num_train_epochs=3,
        weight_decay=0.01,
        learning_rate=3e-6,
        warmup_steps=700,
        lr_scheduler_type="cosine",
        eval_strategy="steps",
        eval_steps=100,
        save_steps=100,
        save_strategy="steps",
        logging_dir=logs_dir,
        logging_steps=100,
        load_best_model_at_end=True,
        metric_for_best_model="eval_loss",
        # report_to="none",
        fp16=True,
        disable_tqdm=False,
        max_grad_norm=10.2 
    )

![](multiclass_cm.png)
![](_multiclass_metrics.png)
![](multiclass_f1's.png)