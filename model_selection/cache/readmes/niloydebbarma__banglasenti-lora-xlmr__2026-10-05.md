---
license: apache-2.0
datasets:
  - niloydebbarma-code/banglasenti-dataset-prep
language:
  - bn
metrics:
  - accuracy
  - f1
base_model: xlm-roberta-base
pipeline_tag: text-classification
library_name: peft
tags:
  - bengali
  - sentiment-analysis
  - lora
  - peft
  - xlm-roberta
  - text-classification
  - google-tpu
  - benchmarking
  - emoji
  - romanized
model-index:
  - name: banglasenti-lora-xlmr
    results:
      - task:
          type: text-classification
          name: Sentiment Analysis
        dataset:
          name: BanglaSenti
          type: niloydebbarma-code/banglasenti-dataset-prep
        metrics:
          - name: Accuracy
            type: accuracy
            value: 0.807
          - name: F1
            type: f1
            value: 0.806
---

# BanglaSenti LoRA Adapter for XLM-RoBERTa-base

**This is the first open-source LoRA (Low-Rank Adaptation) fine-tuned model for Bengali sentiment analysis, released with comprehensive benchmarking results.**

## Model Overview

This model is a LoRA adapter for XLM-RoBERTa-base, fine-tuned on the BanglaSenti dataset for Bangla sentiment classification. It enables efficient and accurate sentiment analysis for Bangla text, including support for emojis and romanized Bangla.

- **Base model:** XLM-RoBERTa-base
- **Adapter:** LoRA (Parameter-Efficient Fine-Tuning)
- **Dataset:** BanglaSenti
- **LoRA configuration:** r=32, alpha=64, dropout=0.1, target_modules=[query, key, value, dense]
- **Task:** Sequence Classification (Sentiment)
- **Validation accuracy:** 80.7%
- **Validation F1:** 80.6%

> This model's adapter weights (`adapter_model.bin`) and configuration files are fully compatible with Hugging Face and PEFT standards. You can use this model for inference or further fine-tuning on both GPU and CPU—no TPU is required for downstream tasks.

## Evaluation Results

| Metric         | Baseline (No LoRA) | LoRA Model | Relative Change |
|----------------|--------------------|------------|-----------------|
| Train Accuracy | 0.3378             | 0.8301     | +145.7%         |
| Train F1       | 0.3305             | 0.8250     | +149.6%         |
| Train Loss     | 1.0999             | 0.4470     | –59.4%          |
| Val Accuracy   | 0.4444             | 0.8107     | +82.4%          |
| Val F1         | 0.2051             | 0.8032     | +291.7%         |
| Val Loss       | 0.0172             | 0.0081     | –53.1%          |
| Accuracy (best) | 0.4443            | 0.8072     | +81.7%          |
| F1 (best)      | 0.2734             | 0.8065     | +194.9%         |

- **W&B Training Run:** [nu1qo8cm](https://wandb.ai/niloydebbarma-ai-youth-alliance/bangla-lora-bn-tpu/runs/nu1qo8cm)
- **W&B Evaluation Run:** [gfsmfb7f](https://wandb.ai/niloydebbarma-ai-youth-alliance/eval-bangla-lora-bn-tpu/runs/gfsmfb7f)

**Key Points:**

- The LoRA adapter achieves strong performance on BanglaSenti, with accuracy and F1 scores above 80% on the validation set.
- Substantial improvements over the baseline in both accuracy and F1.
- Robust for Bangla sentiment, including romanized and emoji-rich text.

## Usage

### Load with PEFT (Hugging Face)

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from peft import PeftModel

base_model = AutoModelForSequenceClassification.from_pretrained('xlm-roberta-base', num_labels=3)
tokenizer = AutoTokenizer.from_pretrained('xlm-roberta-base')
peft_model = PeftModel.from_pretrained(base_model, 'path/to/this/model/folder')

text = "Ami bhalo achi 😊"
inputs = tokenizer(text, return_tensors='pt')
outputs = peft_model(**inputs)
```

### Tokenizer Example

```python
from transformers import PreTrainedTokenizerFast
tok = PreTrainedTokenizerFast(tokenizer_file='tokenizer/tokenizer.json')
examples = [
    'Ami bhalo achi 😊',
    'Tumi kemon acho?',
    'BanglaSenti rocks! 😍',
    'Ei model-ta khub bhalo',
    'Shobai valo thako!'
]
for ex in examples:
    print(f'Input: {ex} | Tokens: {tok.tokenize(ex)}')
```

## Files and Structure

- `adapter_model.bin` — LoRA adapter weights
- `pytorch_model.bin` — Fine-tuned XLM-RoBERTa model weights
- `adapter_config/` — LoRA and PEFT configuration files
- `tokenizer/` — Tokenizer files
- `model_info.txt` — Model and training metadata

## License

Apache 2.0

---

## Acknowledgement

- **This model was trained with support from the Google Research TPU Research Cloud (TRC) program. Special thanks to the TRC team at Google Research for providing free access to Google Cloud TPUs, which made this work possible.**
- The BanglaSenti dataset is from the open-source [banglasenti-dataset-prep](https://github.com/niloydebbarma-code/banglasenti-dataset-prep) project.
- The base model [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) is provided by Facebook AI.
- This model was built using the Hugging Face Transformers and PEFT libraries.
- Thanks to the open-source community and all contributors to the code, data, and research.

## Citation

If you use this model or code, please cite as:

```bibtex
@misc{lora-banglasenti-xlmr-tpu,
  title={LoRA Fine-Tuning of BanglaSenti on XLM-RoBERTa-Base Using Google TPUs},
  author={Niloy Deb Barma},
  year={2025},
  howpublished={\url{https://github.com/niloydebbarma-code/LORA-FINETUNING-BANGLASENTI-XLMR-GOOGLE-TPU}},
  note={Open-source Bengali sentiment analysis with LoRA and XLM-RoBERTa on TPU}
}
```

**References:**

- [docs/dataset_citations.md](https://github.com/niloydebbarma-code/LORA-FINETUNING-BANGLASENTI-XLMR-GOOGLE-TPU/blob/main/docs/dataset_citations.md)
- [CITATIONS.md from banglasenti-dataset-prep](https://github.com/niloydebbarma-code/banglasenti-dataset-prep/blob/main/CITATIONS.md)

---
For questions or issues, please open an issue on the Hugging Face model page.
