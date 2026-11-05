---
license: other
library_name: transformers
tags:
- generated_from_trainer
- medical
- Healthcare & Lifesciences
- BioMed
- chain-of-thought
base_model: meta-llama/Llama-3.2-1B-Instruct
thumbnail: https://collaiborate.com/logo/logo-blue-bg-1.png
model-index:
- name: Bio-Medical-Llama-3-2-1B-CoT-012025
  results: []
datasets:
- collaiborateorg/BioMedData
---

# Bio-Medical-Llama-3-2-1B-CoT-012025

![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/653f5b93cd52f288490edc83/zPMUugzfOiwTiRw88jm7T.jpeg)

This model is a fine-tuned version of [Llama-3.2-1B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct) on our custom "BioMedData" dataset, enhanced with 625,000 examples, including 25,000 chain-of-thought (CoT) instruction samples to strengthen reasoning capabilities. It is specifically optimized for the Healthcare & Lifesciences (HLS) domain.

## Model details

**Model Name:** Bio-Medical-Llama-3-2-1B-CoT-012025

**Base Model:** Llama-3.2-1B-Instruct

**Parameter Count:** 1 billion

**Training Data:** Custom high-quality biomedical dataset with 625,000 examples, including 25,000 CoT instructions.

**Number of Entries in Dataset:** 625,000

**Dataset Composition:** The dataset comprises a mix of synthetic, manually curated, and reasoning-focused entries, ensuring comprehensive coverage of biomedical knowledge and logical reasoning.

## Model description

The Bio-Medical-Llama-3-2-1B-CoT-012025 model is a lightweight yet powerful language model tailored for:

- Generating domain-specific content in healthcare and biomedical fields.
- Answering complex questions requiring step-by-step reasoning using CoT.
- Supporting researchers, clinicians, and students in their respective biomedical endeavors.

This model is fine-tuned to provide interpretability and improved logical coherence through its enhanced CoT capabilities.

## Evaluation Metrics

Bio-Medical-Llama-3-2-1B-CoT-012025 has been evaluated using the Eleuther AI Language Model Evaluation Harness framework on tasks including:

- medmcqa
- medqa_4options
- mmlu_anatomy
- mmlu_clinical_knowledge
- mmlu_college_biology
- mmlu_college_medicine
- mmlu_medical_genetics
- mmlu_professional_medicine
- pubmedqa

Results show consistent performance improvements over general-purpose models of similiar size, particularly in tasks requiring reasoning.

## Intended uses & limitations

**Intended Uses:**
1. **Research Support:** Assisting researchers with reasoning and data extraction from biomedical texts.
2. **Clinical Decision Support:** Offering logical and evidence-based information to aid decision-making.
3. **Educational Tool:** Serving as a learning resource for understanding complex biomedical concepts.

**Limitations and Ethical Considerations:**

- **Biases:** The model may reflect biases from the training data, despite efforts to mitigate them.
- **Accuracy:** Responses should be cross-verified with reliable sources in critical scenarios.
- **Ethical Use:** The model should augment professional expertise and not replace it, especially in high-stakes applications.

## How to use

```python
import transformers
import torch

model_id = "ContactDoctor/Bio-Medical-Llama-3-2-1B-CoT-012025"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
)

messages = [
    {"role": "system", "content": "You are an expert trained on healthcare and biomedical domain!"},
    {"role": "user", "content": "What are the differential diagnoses for a patient presenting with shortness of breath and chest pain?"},
]

prompt = pipeline.tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

terminators = [
    pipeline.tokenizer.eos_token_id,
    pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")
]

outputs = pipeline(
    prompt,
    max_new_tokens=256,
    eos_token_id=terminators,
    do_sample=True,
    temperature=0.6,
    top_p=0.9,
)
print(outputs[0]["generated_text"][len(prompt):])
```

## License

This model is licensed under the [Bio-Medical-Llama-3-2-1B-CoT-012025 (Non-Commercial Use Only)](./LICENSE). Please review the terms and conditions before using the model.

### Contact Information

For further information, inquiries, or issues related to Bio-Medical-Llama-3-2-1B-CoT-012025, please contact:

Email: info@contactdoctor.in

Website: [https://www.contactdoctor.in](https://www.contactdoctor.in)

### Training hyperparameters

The following hyperparameters were used during training:
- **Learning Rate:** 0.0002
- **Train Batch Size:** 8
- **Eval Batch Size:** 4
- **Seed:** 42
- **Gradient Accumulation Steps:** 8
- **Total Train Batch Size:** 32
- **Optimizer:** Adam with betas=(0.9, 0.999) and epsilon=1e-08
- **LR Scheduler Type:** Cosine
- **LR Scheduler Warmup Ratio:** 0.03
- **Training Steps:** 2000
- **Mixed Precision Training:** Native AMP

### Framework versions

- **PEFT:** 0.11.0
- **Transformers:** 4.40.2
- **Pytorch:** 2.1.2
- **Datasets:** 2.19.1
- **Tokenizers:** 0.19.1

### Citation

If you use Bio-Medical-Llama-3-2-1B-CoT-012025 in your research or applications, please cite it as follows:

```bibtex
@misc{ContactDoctor_Bio-Medical-Llama-3.2-1B-CoT-012025,
  author = {ContactDoctor},
  title = {Bio-Medical-Llama-3-2-1B-CoT-012025: A Reasoning-Enhanced Biomedical Language Model},
  year = {2025},
  howpublished = {https://huggingface.co/ContactDoctor/Bio-Medical-Llama-3-2-1B-CoT-012025},
}
```

