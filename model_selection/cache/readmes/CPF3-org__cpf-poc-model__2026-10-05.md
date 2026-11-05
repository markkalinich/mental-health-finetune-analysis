---
language:
  - en
tags:
  - cybersecurity
  - psychology
  - classification
  - social-engineering
  - synthetic-data
  - human-factors
  - security
license: mit
datasets:
  - cpf-synthetic-phishing
  - cybersecurity-psychology
metrics:
  - accuracy
  - f1
  - precision
  - recall
library_name: transformers
pipeline_tag: text-classification
base_model: distilbert-base-uncased
widget:
  - text: "CEO requests: transfer funds now."
  - text: "URGENT: approve this payment immediately."
  - text: "Team meeting scheduled for tomorrow."
---

# CPF Demo - Cybersecurity Psychology Framework

A live demonstration of the **Cybersecurity Psychology Framework (CPF)** for detecting psychological vulnerabilities in text communications.

# **Framework Info:** [cpf3.org](https://cpf3.org)

## What is This?

This interactive demo uses a small language model to analyze text messages and identify potential social engineering patterns based on psychological manipulation techniques. The system classifies text into three risk levels and provides explanations for its decisions.

## How to Use

### Basic Usage
1. **Enter text** in the input field (email content, message, etc.)
2. **Click "Submit"** to analyze the text
3. **Review the JSON output** containing:
   - `vulnerability`: CPF indicator ID (0-2)
   - `severity`: Risk level (green/yellow/red)
   - `confidence`: Model certainty (0-1)
   - `explanation`: Brief description

### Example Inputs to Try

**High Risk Examples:**
- "CEO requests: transfer funds now."
- "Your manager demands immediate access to the system."
- "Urgent: approve this payment or we lose the client."

**Medium Risk Examples:**
- "Time-sensitive request - please respond ASAP."
- "Quick favor needed before end of day."

**Low Risk Examples:**
- "Team meeting scheduled for tomorrow at 2 PM."
- "Please review the quarterly report when convenient."
- "Thanks for your help with the project."

## Understanding the Output

### Risk Levels
- 🟢 **Green (Low Risk)**: Normal communication, no manipulation detected
- 🟡 **Yellow (Medium Risk)**: Some pressure indicators present
- 🔴 **Red (High Risk)**: Strong social engineering patterns detected

### CPF Indicators
- **Indicator 0**: General communication patterns
- **Indicator 1**: Authority compliance exploitation
- **Indicator 2**: Temporal pressure and urgency manipulation

### Confidence Scores
- **0.0-0.4**: Low confidence - uncertain classification
- **0.4-0.7**: Moderate confidence - likely accurate
- **0.7-1.0**: High confidence - strong signal detected

## Technical Details

### Model Information
- **Base Model**: [CPF3-org/cpf-poc-model](https://huggingface.co/CPF3-org/cpf-poc-model)
- **Architecture**: DistilBERT-base-uncased fine-tuned for classification
- **Training**: 3 epochs on synthetic CPF indicator data
- **Performance**: ~85% accuracy on validation set

### Privacy Features
- **Differential Privacy**: Gaussian noise (ε=0.8) added to confidence scores
- **No Data Storage**: Input text is not logged or stored
- **Local Processing**: Analysis happens in real-time without data persistence

### Implementation
- **Framework**: Gradio for the web interface
- **Backend**: Hugging Face Transformers pipeline
- **Deployment**: Hugging Face Spaces (CPU)

## Research Context

### The CPF Framework
The Cybersecurity Psychology Framework analyzes human psychological vulnerabilities across 10 categories and 100+ indicators. This demo implements a simplified version focusing on three primary vulnerability patterns:

1. **Authority Compliance**: Exploitation of hierarchical relationships
2. **Temporal Pressure**: Creation of artificial urgency
3. **Reciprocity**: Manipulation through perceived obligations

### Academic Foundation
- Integrates psychoanalytic and cognitive behavioral theories
- Addresses the 85% of security breaches caused by human factors
- Published research available on SSRN

## Limitations and Disclaimers

**Important Limitations:**
- **Proof of Concept Only**: Not suitable for production security monitoring
- **Synthetic Training Data**: May not generalize to all real-world communications  
- **English Only**: Currently supports English language text only
- **Context Length**: Limited to 128 tokens per analysis
- **False Positives**: May flag legitimate urgent communications

**Ethical Considerations:**
- This tool should not be used to monitor personal communications without consent
- Human oversight is required for any security decisions
- Results should be used for educational and research purposes

## Related Resources

**Model Repository**: [CPF3-org/cpf-poc-model](https://huggingface.co/CPF3-org/cpf-poc-model)  
**Implementation Guide**: [Colab Notebook](https://colab.research.google.com/drive/1fUpjTILbM_1wX7aEGeb0X-uomKlqj0OL)  
**CPF Framework**: [cpf3.org](https://cpf3.org)  
**Source Code**: [GitHub Repository](https://github.com/xbeat/CPF)  
**Technical Paper**: [Implementation Guide](https://github.com/xbeat/CPF/blob/main/AI/)

## API Integration

For programmatic access, use the Hugging Face Inference API:

```python
import requests

API_URL = "https://api-inference.huggingface.co/models/CPF3-org/cpf-poc-model"
headers = {"Authorization": "Bearer YOUR_HF_TOKEN"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

result = query({"inputs": "CEO requests: transfer funds now."})
print(result)
```

## Development

### Local Setup
```bash
git clone https://huggingface.co/spaces/CPF3-org/cpf-poc-demo
cd cpf-poc-demo
pip install -r requirements.txt
python app.py
```

### Dependencies
- `torch`: PyTorch framework
- `transformers`: Hugging Face model pipeline
- `gradio`: Web interface framework

## Feedback and Support

**Found an issue or have suggestions?**
- Open an issue on [GitHub](https://github.com/xbeat/CPF/issues)
- Contact the author: kaolay@gmail.com

**For Academic Collaboration:**
- ORCID: [0009-0007-3263-6897](https://orcid.org/0009-0007-3263-6897)
- Research interests: Cybersecurity psychology, human factors security

## Citation

If you use this demo in your research or presentations:

```bibtex
@misc{canale2025cpfdemo,
  title={CPF Demo - Cybersecurity Psychology Framework},
  author={Giuseppe Canale},
  year={2025},
  publisher={Hugging Face Spaces},
  howpublished={\url{https://huggingface.co/spaces/CPF3-org/cpf-poc-demo}}
}
```

## License

MIT License - See LICENSE file for details.

---

**Disclaimer**: This is a research prototype for educational and demonstration purposes. Not intended for production security monitoring without proper validation and human oversight.