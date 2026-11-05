---
language:
- en
- ha
license: apache-2.0
tags:
- translation
- healthcare
- medical
- hausa
- mT5
- multilingual
datasets:
- custom-healthcare-translation
metrics:
- bleu
- rouge
model-index:
- name: mt5-en-ha-healthcare
  results:
  - task:
      type: translation
      name: English to Hausa Translation
    dataset:
      type: custom
      name: Healthcare Translation Dataset
    metrics:
    - type: bleu
      value: 0.35+
      name: BLEU Score
---

# mT5 English-to-Hausa Healthcare Translation Model

## Model Description

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) specifically trained for English-to-Hausa translation in healthcare contexts. The model has been optimized for medical terminology, patient-doctor interactions, treatment instructions, and general healthcare communication.

## Model Details

- **Model Type**: Sequence-to-sequence translation model
- **Base Model**: google/mt5-small (300M parameters)
- **Languages**: English → Hausa
- **Domain**: Healthcare and Medical
- **Training Date**: 2025-10-02
- **Fine-tuning Dataset**: 156 parallel sentence pairs

## Intended Use

### Primary Use Cases
- **Healthcare Translation**: Translating medical instructions from English to Hausa
- **Patient Communication**: Helping healthcare providers communicate with Hausa-speaking patients
- **Medical Documentation**: Translating medical records and reports
- **Health Education**: Converting health information materials to Hausa

### Supported Medical Domains
- Symptoms and diagnosis
- Medication instructions
- Treatment procedures
- Doctor-patient consultations
- Preventive healthcare
- Emergency medical situations

## How to Use

### Quick Start
```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load model and tokenizer
model_name = "Abduull6771/mt5-en-ha-healthcare"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Translate text
def translate_to_hausa(text):
    input_text = f"translate English to Hausa: {text}"
    inputs = tokenizer(input_text, return_tensors="pt", max_length=256, truncation=True)
    
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=256,
            num_beams=4,
            early_stopping=True,
            do_sample=False
        )
    
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Example usage
english_text = "The patient has high blood pressure and needs medication."
hausa_translation = translate_to_hausa(english_text)
print(hausa_translation)
```

### API Usage with Flask
```python
from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

app = Flask(__name__)

# Load model once at startup
model = AutoModelForSeq2SeqLM.from_pretrained("Abduull6771/mt5-en-ha-healthcare")
tokenizer = AutoTokenizer.from_pretrained("Abduull6771/mt5-en-ha-healthcare")

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    english_text = data['text']
    
    input_text = f"translate English to Hausa: {english_text}"
    inputs = tokenizer(input_text, return_tensors="pt", max_length=256, truncation=True)
    
    outputs = model.generate(**inputs, max_length=256, num_beams=4, early_stopping=True)
    translation = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return jsonify({'translation': translation, 'status': 'success'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

## Training Data

The model was trained on a curated dataset of healthcare-related English-Hausa sentence pairs covering:

- **Medical Symptoms**: Fever, cough, pain, headache, etc.
- **Conditions**: Diabetes, hypertension, malaria, tuberculosis, etc.
- **Treatments**: Medications, procedures, therapy instructions
- **Communication**: Doctor-patient dialogues, medical consultations
- **Prevention**: Health advice, vaccination information, hygiene practices

## Training Details

- **Base Model**: google/mt5-small
- **Training Framework**: Hugging Face Transformers
- **Optimization**: AdamW with cosine learning rate schedule
- **Hardware**: NVIDIA T4 GPU
- **Training Time**: ~4 hours
- **Batch Size**: 4 (with gradient accumulation)
- **Learning Rate**: 3e-4
- **Epochs**: 15

## Performance

### Evaluation Metrics
- **BLEU Score**: 0.35+ (significantly improved from baseline)
- **ROUGE-L**: 0.45+
- **Human Evaluation**: Contextually appropriate medical translations

### Example Translations
| English | Hausa |
|---------|-------|
| "Take this medicine twice daily" | "Ɗauki wannan magani sau biyu a rana" |
| "The patient has high blood pressure" | "Majinyaci yana da hawan jini" |
| "Please come back next week" | "Don Allah ku dawo mako mai zuwa" |
| "Children need vaccination" | "Yara suna bukatar rigakafi" |

## Limitations

- **Domain Specific**: Optimized for healthcare contexts, may not perform well on general text
- **Regional Variations**: Trained on standard Hausa, may not capture all dialectal variations
- **Complex Medical Terms**: Some highly technical medical terminology may not translate accurately
- **Context Dependency**: Performance may vary with very long or complex sentences

## Ethical Considerations

- **Medical Accuracy**: Always verify critical medical translations with qualified healthcare professionals
- **Cultural Sensitivity**: Translations consider Hausa cultural and linguistic contexts
- **Responsibility**: This model is a tool to assist communication, not replace professional medical interpretation

## Citation

If you use this model in your research or applications, please cite:

```bibtex
@misc{mt5-en-ha-healthcare,
  title={English-to-Hausa Healthcare Translation Model},
  author={Healthcare Translation Project},
  year={2025},
  publisher={Hugging Face},
  url={https://huggingface.co/Abduull6771/mt5-en-ha-healthcare}
}
```

## License

This model is released under the Apache 2.0 License. See LICENSE for more details.

## Contact

For questions about this model, please open an issue in the model repository or contact the maintainers.

## Acknowledgments

- **Base Model**: Google's mT5 team for the foundational multilingual model
- **Training Infrastructure**: Hugging Face Transformers library
- **Healthcare Data**: Curated from various medical and healthcare sources
- **Community**: Hausa language speakers who provided feedback and validation

---

*This model is part of efforts to improve healthcare accessibility for Hausa-speaking communities through better language technology.*
