---
library_name: transformers
tags:
- peft
- dora
- sentiment-analysis
datasets:
- tweet_eval
language:
- en
base_model:
- OuteAI/Lite-Oute-1-300M-Instruct
---

# Model Card: llm-course-hw3-dora

This model was fine-tuned as part of **Homework 3** in the HSE LLM Course.  
It applies a **custom DoRA implementation** for **sentiment classification**, using standard causal language modeling training.

The model predicts a sentiment label (`negative`, `neutral`, or `positive`) by generating a short textual output conditioned on the input text.

## Model Sources

- **Base model:** https://huggingface.co/OuteAI/Lite-Oute-1-300M-Instruct  
- **Dataset:** https://huggingface.co/datasets/cardiffnlp/tweet_eval

## Training Method

Training follows a standard causal LM setup with **frozen backbone weights** and **trainable DoRA adapters** inserted into attention projection layers.

## Training Hyperparameters

- **PEFT method:** DoRA (custom implementation)
- **Rank:** 8  
- **DoRA alpha:** 16  
- **Target modules:** attention projections (`k_proj`, `v_proj`)
- **Batch size:** 32  
- **Learning rate:** 5e-4  
- **Optimizer:** AdamW  
- **Precision:** FP16 (mixed precision)
- **Epochs:** 3  

Trainable parameters: ~0.14% of total model parameters.

## Results

- **Macro F1:** ~0.5 on the test set
