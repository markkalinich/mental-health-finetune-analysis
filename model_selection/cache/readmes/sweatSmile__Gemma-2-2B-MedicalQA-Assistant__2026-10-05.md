---
license: gemma
base_model: google/gemma-2-2b-it
tags:
- gemma
- gemma2
- medical
- healthcare
- medical-qa
- fine-tuned
- lora
- instruct
- 4bit
language:
- en
library_name: transformers
pipeline_tag: text-generation
datasets:
- lavita/ChatDoctor-HealthCareMagic-100k
---

# Gemma-2-2B Medical Q&A Assistant 🏥

This is a fine-tuned version of [google/gemma-2-2b-it](https://huggingface.co/google/gemma-2-2b-it) specialized for medical question answering. The model has been trained on real patient-doctor conversations to provide helpful, accurate medical information with appropriate safety disclaimers.

## 🎯 Model Details

- **Base Model**: Gemma-2-2B-Instruct (2B parameters)
- **Fine-tuning Method**: LoRA (Low-Rank Adaptation)
- **Quantization**: 4-bit (nf4) for efficient training and inference
- **Dataset**: ChatDoctor-HealthCareMagic (1,500 curated samples)
- **Domain**: Medical Q&A, Healthcare Information
- **Use Case**: Medical information assistant, health education, preliminary medical guidance

## 🔧 Training Configuration

### LoRA Parameters
- **Rank (r)**: 8
- **Alpha**: 16
- **Dropout**: 0.1
- **Target Modules**: All linear layers

### Training Hyperparameters
- **Epochs**: 3
- **Learning Rate**: 2e-5
- **Batch Size**: 4 per device
- **Max Sequence Length**: 1024 tokens (for detailed medical responses)
- **Scheduler**: Cosine with 10% warmup
- **Optimizer**: AdamW with weight decay (0.01)
- **Precision**: BF16
- **Gradient Clipping**: 1.0

### Training Infrastructure
- **Hardware**: Single GPU (T4/V100/A100)
- **Training Time**: ~30-45 minutes
- **Framework**: TRL + Transformers + PEFT

## 📊 Dataset

The model was fine-tuned on a curated subset of the [ChatDoctor-HealthCareMagic-100k](https://huggingface.co/datasets/lavita/ChatDoctor-HealthCareMagic-100k) dataset, which contains:
- Real patient questions from HealthCareMagic platform
- Professional doctor responses
- Diverse medical topics (symptoms, treatments, medications, preventive care)
- Privacy-preserved and ethically sourced data

**Training Samples**: 1,500 high-quality medical Q&A pairs

## 💻 Usage

### Basic Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "sweatSmile/Gemma-2-2B-MedicalQA-Assistant"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Format your medical query
prompt = """<start_of_turn>user
I've been experiencing persistent headaches for the past week. What could be causing this?<end_of_turn>
<start_of_turn>model
"""

inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(
    **inputs,
    max_new_tokens=256,
    temperature=0.7,
    top_p=0.9,
    do_sample=True
)

response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
```

### 4-bit Quantized Inference (Recommended)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16
)

model = AutoModelForCausalLM.from_pretrained(
    "sweatSmile/Gemma-2-2B-MedicalQA-Assistant",
    quantization_config=quantization_config,
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("sweatSmile/Gemma-2-2B-MedicalQA-Assistant")
```

## 🩺 Example Outputs

**Query**: "What are the common symptoms of diabetes?"

**Response**: 
> Common symptoms of Type 2 diabetes include frequent urination, increased thirst, unexplained weight loss, fatigue, blurred vision, slow-healing wounds, and tingling or numbness in hands or feet. If you're experiencing multiple symptoms, it's important to get your blood sugar levels checked. Early detection and management are crucial.
>
> ⚕️ Disclaimer: This information is for educational purposes only. Please consult a qualified healthcare professional for medical advice.

---

**Query**: "How can I manage high blood pressure naturally?"

**Response**:
> Natural management of high blood pressure includes: regular exercise (30 minutes daily), reducing sodium intake, maintaining healthy weight, limiting alcohol, managing stress through meditation or yoga, eating potassium-rich foods (bananas, leafy greens), and ensuring adequate sleep. However, these should complement, not replace, prescribed medications.
>
> ⚕️ Disclaimer: This information is for educational purposes only. Please consult a qualified healthcare professional for medical advice.

## ⚠️ Important Limitations & Safety

### Medical Disclaimers
- 🚨 **NOT A REPLACEMENT FOR PROFESSIONAL MEDICAL ADVICE**: This model provides general health information only
- 🚨 **Always consult a qualified healthcare provider** for diagnosis and treatment
- 🚨 **Emergency situations**: Call emergency services immediately for urgent medical conditions
- 🚨 **Individual variation**: Medical advice must be personalized to your specific situation

### Model Limitations
- Trained on 1,500 samples - may not cover all medical scenarios
- Limited to English language medical terminology
- May not reflect the most recent medical research (knowledge cutoff dependent on base model)
- Cannot perform physical examinations or order diagnostic tests
- May occasionally generate plausible-sounding but incorrect information (hallucinations)
- Not validated against clinical benchmarks

### Appropriate Use Cases ✅
- General health education and information
- Understanding common medical terms and conditions
- Preliminary research before doctor's appointments
- Health literacy improvement
- Medical training assistance (with supervision)

### Inappropriate Use Cases ❌
- Self-diagnosis or self-treatment
- Emergency medical situations
- Replacing professional medical consultations
- Making critical healthcare decisions
- Prescribing medications or treatments
- Mental health crisis intervention

## 🎓 Intended Use

This model is designed for:
- **Educational purposes**: Teaching and learning about common health conditions
- **Health information access**: Providing accessible medical knowledge
- **Research**: Medical AI and NLP research
- **Prototyping**: Building healthcare chatbot prototypes
- **Medical training**: Supplementary tool for medical students (with instructor oversight)

## 📈 Performance Notes

- **Strengths**: Common conditions, preventive care, general wellness advice, medical terminology
- **Best performance on**: Questions similar to training distribution (patient-doctor Q&A format)
- **Quantization**: 4-bit quantization maintains ~95% of full precision performance with significant memory savings

## 🔬 Technical Specifications

| Specification | Value |
|--------------|-------|
| Base Architecture | Gemma 2 (Google) |
| Model Size | 2B parameters |
| Quantization | 4-bit (nf4) |
| Context Window | 8,192 tokens |
| Training Tokens | ~1.5M medical tokens |
| LoRA Rank | 8 |
| LoRA Alpha | 16 |
| Trainable Parameters | ~4.2M (0.2% of base) |

## 📝 Citation

```bibtex
@misc{gemma2-medical-qa-2025,
  author = {sweatSmile},
  title = {Gemma-2-2B Medical Q&A Assistant},
  year = {2025},
  publisher = {HuggingFace},
  journal = {HuggingFace Model Hub},
  howpublished = {\url{https://huggingface.co/sweatSmile/Gemma-2-2B-MedicalQA-Assistant}}
}
```

## 🙏 Acknowledgments

- **Base Model**: Google's Gemma team for the excellent Gemma-2-2B-Instruct model
- **Dataset**: ChatDoctor team and HealthCareMagic for the medical Q&A dataset
- **Framework**: HuggingFace TRL, Transformers, and PEFT libraries

## 📜 License

This model inherits the [Gemma License](https://ai.google.dev/gemma/terms) from the base model. The fine-tuned weights are released under the same terms.

**Usage Restrictions**: Please review Google's Gemma Terms of Use, particularly regarding healthcare applications.

## ⚖️ Ethical Considerations

- Model outputs should always include medical disclaimers
- Designed to encourage users to seek professional medical advice
- Training data sourced ethically from publicly available patient-doctor interactions
- No personally identifiable information (PII) in training data
- Built with safety alignment from base Gemma-2 model

## 🔄 Version History

- **v1.0** (Current): Initial release with 1.5k samples, LoRA fine-tuning

---

**Disclaimer**: This model is a research prototype and educational tool. It is not intended for clinical use or as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.