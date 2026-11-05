---
library_name: transformers
tags:
  - medical
  - medqa
  - question-answering
  - gpt2
  - causal-lm
  - transformers
  - truehealth
license: apache-2.0
language:
  - en
base_model: gpt2
datasets:
  - truehealth/medqa
metrics:
  - perplexity
pipeline_tag: text-generation
---

# GPT-2 Fine-tuned on MedQA (Medical Question Answering)

This model is a GPT-2 language model fine-tuned on the MedQA dataset for medical multiple-choice question answering. It is trained to generate relevant medical answers conditioned on clinical questions, suitable for downstream applications in automated medical education or QA systems.

## Model Details

- **Developed by:** Aranya Saha
- **Finetuned from model:** `gpt2`
- **Language(s):** English
- **License:** Apache 2.0
- **Model type:** Causal Language Model
- **Library:** [🤗 Transformers](https://huggingface.co/docs/transformers)

## Model Sources

- **Original base model:** [GPT-2](https://huggingface.co/gpt2)
- **Training dataset:** [truehealth/medqa](https://huggingface.co/datasets/truehealth/medqa)

## Uses

### Direct Use
- Clinical education and training (QA-based learning)
- Generating answers for medical board-style questions

### Downstream Use
- Integrate into medical tutoring tools
- Fine-tune further on other medical NLP tasks

### Out-of-Scope Use
- Should not be used as a real-time diagnostic system
- Not suitable for clinical decision-making or advice without expert validation

## Bias, Risks, and Limitations

- GPT-2 and MedQA may reflect biases present in training sources
- Misinterpretation or hallucinated content can be harmful in sensitive domains like healthcare
- Model may generate plausible-sounding but incorrect medical information

### Recommendations

This model should be used by professionals or in educational contexts only. Always verify generated information against trusted medical sources.

## How to Get Started

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("Aranya31/gpt2-medqa-ft")
tokenizer = AutoTokenizer.from_pretrained("Aranya31/gpt2-medqa-ft")

prompt = "What is the recommended treatment for acute asthma?\nAnswer:"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_length=100, do_sample=True, temperature=0.7)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Training Details

### Training Data

- Used `truehealth/medqa`, containing USMLE-style medical multiple-choice questions
- Preprocessed to create instruction-output pairs (question + correct answer)

### Training Procedure

- **Epochs:** 3
- **Batch size:** 4
- **Max sequence length:** 1024 tokens
- **Precision:** fp16 when CUDA is available
- **Optimizer:** AdamW via 🤗 Trainer API
- **Learning rate:** 5e-5 (standard for GPT-2 fine-tuning)

## Evaluation

- Evaluated on a validation split from MedQA
- Manual qualitative checks confirmed model coherence and answer relevance
- Formal metrics like accuracy were not computed due to generative nature of the task

## Environmental Impact

- **Hardware:** Colab/consumer GPU (NVIDIA Tesla T4/A100)
- **Training time:** ~1-2 hours
- **Carbon emissions:** Estimated under 1 kg CO2 using ML CO2 calculator

## Technical Specifications

- **Model Architecture:** GPT-2 small (124M parameters)
- **Objective:** Next-token prediction using causal language modeling
- **Framework:** PyTorch, Hugging Face Transformers

## Citation

```bibtex
@misc{gpt2-medqa-finetuned,
  title={GPT-2 Fine-tuned on MedQA},
  author={Aranya Saha},
  year={2025},
  howpublished={\url{https://huggingface.co/Aranya31/gpt2-medqa-ft}}
}
```

## Contact

For questions or issues, contact: aranyasaha932@gmail.com