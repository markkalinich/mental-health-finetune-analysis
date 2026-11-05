## Evaluation

### Results

| Metric | Score |
|---|---|
| AUC-ROC | 0.7661 |
| F1 Score | 0.7129 |
| Precision | 0.7013 |
| Recall | 0.7248 |

### Comparison with Baseline Models

| Model | AUC-ROC | Type |
|---|---|---|
| PBC4cip | 0.7063 | Classical ML |
| Random Forest | 0.7328 | Classical ML |
| SVM (LinearSVC + TF-IDF) | 0.7400 | Classical ML |
| **Mistral 7B fine-tuned (this model)** | **0.7661** | Fine-tuned LLM |

## Environmental Impact

- **Hardware:** Apple M4 Pro (24GB unified memory)
- **Training time:** ~45–60 minutes
- **Cloud provider:** None — trained fully on local hardware
- **Carbon emissions:** Minimal, Apple Silicon is energy-efficient

## Bias, Risks, and Limitations

- Trained exclusively on English Reddit posts
- Binary classification does not capture severity levels
- Dataset is relatively small (1,475 examples)
- Not validated for clinical use — outputs should not replace professional mental health assessment

If you or someone you know is experiencing a mental health crisis, please contact a qualified professional or a crisis helpline.

## Citation

```bibtex
@misc{mistral-suicide-classifier-2025,
  title   = {Mistral-7B Fine-tuned for Suicide Ideation Detection},
  author  = {Olmosantill{\'{o}}n, Manuel and Mart{\'{i}}nez, Luis},
  year    = {2025},
  publisher = {HuggingFace},
  url     = {https://huggingface.co/c4p174n3m0/mistral-suicide-classifier}
}
```