---
language:
- en
license: apache-2.0
tags:
- medical
- qa
- drug-information
- qwen3
- lora
base_model: Qwen/Qwen3-1.7B
datasets:
- custom
pipeline_tag: text-generation
---

# Salient Medical Q&A Model

Fine-tuned Qwen3-1.7B model for answering patient questions about medications based on FDA drug label information.

## Model Details

- **Base Model:** Qwen/Qwen3-1.7B
- **Fine-tuning Method:** LoRA (r=16, alpha=32, dropout=0.05)
- **Training Data:** 1,000 Q&A pairs from FDA drug labels
- **Special Focus:** Controlled substances (opioids, benzodiazepines, stimulants)
- **Hardware:** AWS Trainium (trn1.2xlarge)
- **Training Steps:** 1,000
- **Training Time:** ~25 minutes

## Use Cases

- Patient education about medications
- Drug safety information lookup
- Dosage guidance
- Side effects information
- Drug interaction checking
- Controlled substance awareness

## Example Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("54yyyu/salient-qwen3-1.7b-medical-qa")
tokenizer = AutoTokenizer.from_pretrained("54yyyu/salient-qwen3-1.7b-medical-qa")

prompt = """<|im_start|>system
You are a helpful medical information assistant. You answer patient questions about medications based on drug label information. Provide clear, accurate, and patient-friendly answers.<|im_end|>
<|im_start|>user
Context: Dexedrine (dextroamphetamine sulfate) is a Schedule II controlled substance used to treat ADHD and narcolepsy. It has high potential for abuse and dependence.

Question: Is Dexedrine addictive?<|im_end|>
<|im_start|>assistant
"""

inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=200)
print(tokenizer.decode(outputs[0]))
```

## Dataset

- **Size:** 1,000 Q&A pairs
- **Sources:** FDA drug labels (20,000 analyzed)
- **Attributes:** 8-13 key fields per drug
- **Distribution:** 98.2% standard drugs, 1.8% controlled substances

## Training Details

- **LoRA Rank:** 16
- **LoRA Alpha:** 32
- **Learning Rate:** 5e-5
- **Batch Size:** 2 per device
- **Precision:** BFloat16
- **Parallelization:** Tensor Parallel (2 cores)

## Limitations

⚠️ **Important:** This model is for educational purposes only. Always consult healthcare professionals for medical advice.

- Trained on 1,000 examples (limited coverage)
- May not have information on all medications
- Should not replace professional medical consultation
- Information based on drug labels, not clinical experience

## Citation

If you use this model, please cite:

```
@misc{salient-medical-qa,
  author = {54yyyu},
  title = {Salient Medical Q&A Model},
  year = {2025},
  publisher = {Hugging Face},
  url = {https://huggingface.co/54yyyu/salient-qwen3-1.7b-medical-qa}
}
```

## License

Apache 2.0
