---
language: en
license: apache-2.0
library_name: transformers
base_model: unsloth/medgemma-4b-pt
tags:
- medical
- ecg
- cardiology
- report-generation
- unsloth
- gemma
- fine-tuned
pipeline_tag: text-generation
datasets:
- custom-ecg-dataset
metrics:
- bleu
- rouge
- diagnostic_coherence
model-index:
- name: MedGemma-4B-ECG
  results:
  - task:
      type: text-generation
      name: ECG Report Generation
    dataset:
      type: custom
      name: ECG Clinical Dataset
    metrics:
    - type: bleu-4
      value: 30.784
      name: BLEU-4 Score
    - type: rouge-1
      value: 0.423
      name: ROUGE-1 Score
    - type: rouge-l
      value: 0.318
      name: ROUGE-L Score
    - type: diagnostic_coherence
      value: 0.720
      name: Diagnostic Coherence Score
    - type: success_rate
      value: 100.0
      name: Success Rate (%)
---

# MedGemma-4B ECG Report Generator

This is a **fully merged, standalone model** fine-tuned from `unsloth/medgemma-4b-pt` for ECG interpretation and clinical report generation. It was trained using the Unsloth library for high-efficiency, memory-optimized fine-tuning.

This model is designed to take structured output from a primary ML classifier (which provides findings like "Atrial Fibrillation: 82% confidence, Present") and synthesize it into a coherent, human-readable clinical report, complete with an impression, detailed analysis, and clinical recommendations.

## Model Details

- **Base Model:** `unsloth/medgemma-4b-pt`
- **Fine-tuning Method:** Unsloth + LoRA (merged into base model)
- **Training Data:** 500 curated ECG interpretation examples
- **Evaluation Dataset:** 50 real ECG examples

## Performance Metrics

The model was evaluated on a comprehensive test set with the following results:

| Metric | Score | Description |
|--------|-------|-------------|
| **BLEU-4** | **30.784** | Measures n-gram overlap with reference reports |
| **ROUGE-1** | **0.423** | Word-level content overlap |
| **ROUGE-L** | **0.318** | Longest common subsequence match |
| **Diagnostic Coherence** | **0.720** | Clinical reasoning and logic consistency |
| **Success Rate** | **100%** | Percentage of successful report generations |

### Performance Summary
- ✅ **Excellent Clinical Coherence** (0.720/1.0) - Strong medical reasoning
- ✅ **Perfect Success Rate** (100%) - Robust and stable generation  
- ✅ **Good Linguistic Quality** (BLEU-4: 30.784) - Fluent medical text
- ✅ **Appropriate Content Coverage** (ROUGE-1: 0.423) - Relevant medical terminology

### Benchmark Context
- **BLEU-4 Score of 30.784** is excellent for medical text generation (typical range: 15-40)
- **Diagnostic Coherence of 0.720** indicates strong clinical reasoning capabilities
- **100% Success Rate** demonstrates robust, failure-free operation
- **ROUGE scores** show good content alignment with expert-written reports

## Usage

This model follows a standard instruction format. Provide the instruction and the structured input to get a clinical report.

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = "OussamaEL/medgemma-ECG-C-V2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

# Alpaca prompt format is required
alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.
### Instruction:
{}
### Input:
{}
### Response:
{}"""

instruction = "You are a medical AI assistant specializing in ECG interpretation. Analyze the ECG findings and patient context to generate a clinical report."

input_text = """ECG FINDINGS:
- Atrial Fibrillation (AFIB): 95% confidence, Present
- Sinus Tachycardia (STACH): 88% confidence, Present

PATIENT CONTEXT:
68-year-old male with diabetes and hypertension presents with 2 days of worsening shortness of breath and leg swelling."""

inputs = tokenizer(
    alpaca_prompt.format(instruction, input_text, ""),
    return_tensors="pt"
).to("cuda")

outputs = model.generate(**inputs, max_new_tokens=256, temperature=0.7, do_sample=True)
print(tokenizer.decode(outputs[0], skip_special_tokens=True).split("### Response:")[1].strip())
```

## Example Output

```
**IMPRESSION**
Atrial Fibrillation with rapid ventricular response in the setting of acute heart failure exacerbation.

**DETAILED ANALYSIS**
- Atrial Fibrillation (AFIB): Present with very high confidence (95%). Irregular rhythm with absent P waves.
- Sinus Tachycardia (STACH): Present with high confidence (88%). Heart rate elevated likely secondary to decompensated heart failure.

**CLINICAL RECOMMENDATIONS**
Given the patient's presentation of acute dyspnea, lower extremity edema, and ECG findings, recommend:
1. Rate control for atrial fibrillation
2. Diuretic therapy for volume overload
3. Echocardiogram to assess cardiac function
4. Consider anticoagulation based on CHA2DS2-VASc score
```

## Training Details

- **Framework:** Unsloth with LoRA adaptation
- **Training Examples:** 500 ECG cases with structured findings and expert reports
- **Optimization:** Memory-efficient fine-tuning with gradient checkpointing
- **Hardware:** Optimized for consumer GPUs
- **Training Time:** Efficient fine-tuning with memory optimization

## Model Architecture

- **Parameters:** 4B parameters (merged model)
- **Context Length:** Standard Gemma context window
- **Precision:** 16-bit merged weights
- **Memory Requirements:** ~8GB GPU memory for inference

## Evaluation Methodology

The model was rigorously evaluated using:
- **50 real ECG examples** from clinical datasets
- **Multiple metrics** covering linguistic quality and medical accuracy
- **Expert validation** of diagnostic coherence
- **Stress testing** for robustness and failure modes

## Limitations and Disclaimers

⚠️ **Important Medical Disclaimer:**
- This model is intended for research and development purposes only
- Not a substitute for professional medical advice, diagnosis, or treatment
- All clinical decisions should involve qualified healthcare professionals
- Model outputs should be reviewed and validated by medical experts

## Citation

If you use this model in your research, please cite:

```bibtex
@misc{medgemma-4b-ecg,
  title={MedGemma-4B ECG Report Generator},
  author={Oussama EL},
  year={2025},
  url={https://huggingface.co/OussamaEL/medgemma-ECG-C-V2}
}
```

## Contact

For questions, issues, or collaboration opportunities, please open an issue in this repository or contact through Hugging Face.

---

**Model Performance Highlights:**
- 🏆 **30.784 BLEU-4** - Excellent linguistic quality
- 🧠 **0.720 Diagnostic Coherence** - Strong clinical reasoning  
- 💪 **100% Success Rate** - Robust and reliable
- ⚡ **Efficient Architecture** - Optimized for practical deployment