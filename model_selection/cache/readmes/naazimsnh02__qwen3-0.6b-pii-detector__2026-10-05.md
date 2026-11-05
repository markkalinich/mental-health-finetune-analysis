---
language:
- en
license: apache-2.0
tags:
- pii-detection
- phi-detection
- qwen3
- unsloth
- trl
- sft
- ner
datasets:
- nvidia/Nemotron-PII
base_model: Qwen/Qwen3-0.6B
model-index:
- name: qwen3-0.6b-pii-detector
  results:
  - task:
      type: token-classification
      name: PII/PHI Detection
    dataset:
      type: nvidia/Nemotron-PII
      name: Nemotron-PII
    metrics:
    - type: loss
      value: 0.4572
      name: Evaluation Loss
---

# Qwen3 0.6B PII Detector

This model is a fine-tuned version of [Qwen/Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B) for detecting Personally Identifiable Information (PII) and Protected Health Information (PHI) in text using inline tagging format.

## Model Description

- **Base Model:** Qwen/Qwen3-0.6B
- **Training Data:** nvidia/Nemotron-PII (47,500 training samples, 2,375 evaluation samples)
- **Training Method:** LoRA fine-tuning with Unsloth
- **Task:** Named Entity Recognition (NER) for PII/PHI detection
- **Output Format:** text_tagged (inline tags: `[entity]label`)
- **Context-Aware:** Trained with domain, document type, and locale information

### Key Features

- **Inline Tag Format**: Outputs text with entities tagged as `[entity]label`
- **Domain-Aware**: Optionally accepts domain context (finance, healthcare, legal, etc.) for improved accuracy
- **Locale Support**: Handles both US and international text
- **Natural Language**: Works on conversations, documents, forms, and unstructured text
- **55+ Entity Types**: Comprehensive PII/PHI coverage across 50+ industries

## Performance

- **Epochs Completed:** 2.096
- **Total Training Steps:** 6,224
- **Initial Training Loss:** 1.8435
- **Final Training Loss:** 0.4155
- **Initial Evaluation Loss:** 1.9682
- **Final Evaluation Loss:** 0.4572
- **Best Evaluation Loss:** 0.4551

## Training Configuration

- **Epochs Planned:** 5
- **Epochs Completed:** 2.096
- **Batch Size:** 4
- **Gradient Accumulation:** 4
- **Effective Batch Size:** 16
- **Learning Rate:** 0.0002
- **LR Scheduler:** cosine
- **Warmup Ratio:** 0.1
- **Weight Decay:** 0.01
- **Max Sequence Length:** 2048
- **LoRA r:** 16
- **LoRA alpha:** 16
- **GPU:** Nvidia L4
- **Evaluation Strategy:** Every 100 steps
- **Output Format:** text_tagged with domain context

### Framework Versions

- **Transformers**: 4.56.2
- **PyTorch**: 2.x
- **Unsloth**: Latest
- **Datasets**: 3.6.0
- **TRL**: Latest

## Usage

### Installation

```bash
pip install transformers torch
```

### Basic Usage (Without Domain/Locale)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load model and tokenizer
model_name = "naazimsnh02/qwen3-0.6b-pii-detector"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Prepare input
text = "My name is John Smith and my SSN is 123-45-6789. Contact me at john@email.com"

messages = [
    {
        "role": "user",
        "content": f"""Analyze the following text and identify all PII (Personally Identifiable Information) and PHI (Protected Health Information) entities.

Text: {text}

Provide the output with inline tags in the format: [entity]label"""
    }
]

# Generate
input_ids = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_tensors="pt"
)

outputs = model.generate(
    input_ids,
    max_new_tokens=512,
    temperature=0.1,  # Lower for consistent tagging
    top_p=0.9,
)

response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
# Output: My name is [John Smith]name and my SSN is [123-45-6789]ssn. Contact me at [john@email.com]email
```

### Enhanced Usage (With Domain/Locale Context)

For better accuracy, provide domain and locale information:

```python
# Prepare input with context
text = "Patient John Doe, MRN 12345, diagnosed with hypertension."
domain = "healthcare"
doc_type = "medical_record"
locale = "us"

messages = [
    {
        "role": "user",
        "content": f"""Analyze the following {doc_type} from the {domain} domain ({locale.upper()} locale) and identify all PII (Personally Identifiable Information) and PHI (Protected Health Information) entities.

Text: {text}

Provide the output with inline tags in the format: [entity]label"""
    }
]

# Generate as above
input_ids = tokenizer.apply_chat_template(messages, return_tensors="pt")
outputs = model.generate(input_ids, max_new_tokens=512, temperature=0.1)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
```

### Extracting Entities from Model Output

Use this utility class to extract structured data from the model's tagged output:

```python
import re
from typing import List, Dict

class PIIExtractor:
    """
    Utility class to extract PII entities from text tagged by the model.
    
    The model outputs text in the format: [entity]label
    Example: "[John Smith]first_name works at [Acme Corp]organization"
    """
    
    def __init__(self):
        # Pattern to match [entity]label format
        self.pattern = re.compile(r'\[([^\]]+)\](\w+)')
    
    def extract_entities(self, tagged_text: str) -> List[Dict[str, str]]:
        """
        Extract all PII entities from tagged text.
        
        Returns:
            List of dictionaries with 'text' and 'label' keys
        """
        matches = self.pattern.findall(tagged_text)
        return [{"text": text, "label": label} for text, label in matches]
    
    def extract_with_positions(self, tagged_text: str) -> List[Dict[str, any]]:
        """Extract entities with their positions in the original text."""
        entities = []
        offset = 0
        
        for match in self.pattern.finditer(tagged_text):
            entity_text = match.group(1)
            label = match.group(2)
            
            start = match.start() - offset
            end = start + len(entity_text)
            
            entities.append({
                "text": entity_text,
                "label": label,
                "start": start,
                "end": end
            })
            
            # Update offset (length of tags removed)
            offset += len(label) + 2  # +2 for ] and label
        
        return entities
    
    def get_clean_text(self, tagged_text: str) -> str:
        """Remove all tags from text, leaving only the original content."""
        # Remove labels and brackets
        text = re.sub(r'\](\w+)', '', tagged_text)
        text = text.replace('[', '')
        return text
    
    def group_by_label(self, tagged_text: str) -> Dict[str, List[str]]:
        """Group extracted entities by their label type."""
        entities = self.extract_entities(tagged_text)
        grouped = {}
        for entity in entities:
            label = entity['label']
            if label not in grouped:
                grouped[label] = []
            grouped[label].append(entity['text'])
        return grouped

# Example usage
extractor = PIIExtractor()
tagged_output = "[John Smith]first_name lives in [New York]city"

entities = extractor.extract_entities(tagged_output)
print(entities)
# [{'text': 'John Smith', 'label': 'first_name'}, {'text': 'New York', 'label': 'city'}]

clean_text = extractor.get_clean_text(tagged_output)
print(clean_text)
# "John Smith lives in New York"

grouped = extractor.group_by_label(tagged_output)
print(grouped)
# {'first_name': ['John Smith'], 'city': ['New York']}
```

## Output Format

The model outputs text with inline tags in the format: `[entity]label`

**Example:**

Input:
```
I am applying for student financial aid. My name is Peggy and my SSN is 250-38-8116.
```

Output:
```
I am applying for student financial aid. My name is [Peggy]first_name and my SSN is [250-38-8116]ssn.
```

## Supported Entity Types (55+ categories)

The model can detect various types of sensitive information including:

### Personal Identifiers
- `first_name`, `last_name`, `name`, `maiden_name`, `middle_name`
- `ssn` (Social Security Number)
- `date_of_birth`, `age`
- `gender`, `race_ethnicity`, `religious_belief`
- `driver_license`, `passport`, `national_id`

### Contact Information
- `email`, `phone_number`, `fax_number`
- `street_address`, `address`, `city`, `state`, `county`, `zip_code`, `country`
- `po_box`

### Medical/Health Information (PHI)
- `medical_record_number` (mrn), `patient_id`
- `blood_type`, `diagnosis`, `medication`, `procedure`
- `health_plan_id`, `insurance_number`, `policy_number`
- `hospital_name`, `doctor_name`

### Financial Information
- `credit_card_number`, `bank_account_number`
- `routing_number`, `account_number`, `iban`
- `tax_id`, `employer_id` (ein)
- `salary`, `income`

### Professional/Organizational
- `organization`, `company_name`, `employer`
- `job_title`, `employee_id`
- `username`, `user_id`

### Digital Identifiers
- `ip_address`, `mac_address`
- `url`, `domain_name`
- `device_id`, `imei`

### Educational
- `student_id`, `school_name`, `university`
- `degree`, `gpa`

### Legal
- `case_number`, `court_name`
- `license_plate`, `vin`

**And 20+ more categories...**

## Domain Coverage (50+ industries)

Trained on diverse domains including:
- Healthcare & Medical
- Finance & Banking
- Legal & Law
- Education & Academia
- Government & Public Sector
- Cybersecurity & IT
- Human Resources
- Insurance
- Real Estate
- Retail & E-commerce
- And more...

## Training Details

This model was trained using:
- [Unsloth](https://github.com/unslothai/unsloth) for efficient training
- [TRL](https://github.com/huggingface/trl) for supervised fine-tuning
- Modal infrastructure with Nvidia L4 GPU
- Evaluation during training with 5% validation split
- Context-aware training with domain, document type, and locale information

## Limitations

- **Context Dependency**: Accuracy may vary based on context clarity
- **Domain Specificity**: Works best when domain context is provided
- **Ambiguous Entities**: May struggle with ambiguous text (e.g., is "Apple" a company or fruit?)
- **Language**: Primarily trained on English text
- **Novel Entities**: May not detect entity types not present in training data
- **Format Sensitivity**: Best results with natural language; may vary with heavily formatted text

## Ethical Considerations

⚠️ **Important**: This model is designed to DETECT PII/PHI, not to protect it.

- **Use Responsibly**: Ensure compliance with privacy regulations (GDPR, HIPAA, CCPA, etc.)
- **Validation Required**: Always validate model outputs in production environments
- **Not 100% Accurate**: May miss some PII or incorrectly tag non-PII
- **Redaction**: Use detected entities to redact/anonymize sensitive information
- **Audit Trail**: Maintain logs of PII detection for compliance
- **Human Review**: Critical applications should include human oversight

## Intended Use

### Recommended Use Cases:
- PII detection in documents before sharing
- Automated redaction pipelines
- Compliance monitoring
- Data anonymization workflows
- Privacy-preserving data analysis
- Document sanitization
- GDPR/HIPAA compliance tools

### Not Recommended:
- As the sole PII detection method in high-stakes scenarios
- Without human review in sensitive applications
- For languages other than English
- Real-time critical systems without validation

## License

Apache 2.0

## Citation

If you use this model, please cite:

```bibtex
@misc{qwen3-pii-detector,
  author = {Syed Naazim Hussain},
  title = {Qwen3 0.6B PII Detector},
  year = {2025},
  publisher = {HuggingFace},
  url = {https://huggingface.co/naazimsnh02/qwen3-0.6b-pii-detector}
}
```

## Acknowledgments

- **Base Model**: [Qwen Team](https://huggingface.co/Qwen) for Qwen3-0.6B
- **Dataset**: [NVIDIA](https://huggingface.co/nvidia) for Nemotron-PII dataset
- **Training**: Fine-tuned using [Unsloth](https://github.com/unslothai/unsloth)
- **Infrastructure**: Trained on Modal with Nvidia L4 GPU