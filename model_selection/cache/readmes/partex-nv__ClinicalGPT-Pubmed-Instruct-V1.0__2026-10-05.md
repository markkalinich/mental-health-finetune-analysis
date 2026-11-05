---
license: apache-2.0
base_model:
- mistralai/Mistral-7B-Instruct-v0.2
pipeline_tag: question-answering
library_name: peft
tags:
- medical
- lifescience
- drugdiscovery
---
# ClinicalGPT-Pubmed-Instruct-V1.0

## Overview
ClinicalGPT-Pubmed-Instruct-V1.0 is a specialized language model fine-tuned on the mistralai/Mistral-7B-Instruct-v0.2 base model. While primarily trained on 10 million PubMed abstracts and titles, this model excels at generating responses to life science-related medical questions with relevant citations from various scientific sources.

## Key Features
- Built on Mistral-7B-Instruct-v0.2 base model
- Primary training on 10M PubMed abstracts and titles
- Generates answers with scientific citations from multiple sources
- Specialized for medical and life science domains

## Applications
- **Life Science Research**: Generate accurate, referenced answers for biomedical and healthcare queries
- **Pharmaceutical Industry**: Support healthcare professionals with evidence-based responses
- **Medical Education**: Aid students and educators with scientifically-supported content from various academic sources

## System Requirements

### GPU Requirements
- **Minimum VRAM**: 16-18 GB for inference in BF16 (BFloat16) precision
- **Recommended GPUs**:
  - NVIDIA A100 (20GB) - Ideal for BF16 precision
  - Any GPU with 16+ GB VRAM
  - Performance may vary based on available memory

### Software Prerequisites
- Python 3.x
- PyTorch
- Transformers library

### Basic Implementation
```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Set parameters
model_dir = "partex-nv/ClinicalGPT-Pubmed-Instruct-V1.0"
max_new_tokens = 1500
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = AutoModelForCausalLM.from_pretrained(model_dir).to(device)

# Define your question
question = "What is the role of the tumor microenvironment in cancer progression?"
prompt = f"""Please provide the answer to the question asked.
### Question: {question}
### Answer: """

# Tokenize input
inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True).to(device)

# Generate output
output_ids = model.generate(
    inputs.input_ids,
    attention_mask=inputs.attention_mask,
    max_new_tokens=1000,
    repetition_penalty=1.2,
    pad_token_id=tokenizer.eos_token_id,
)

# Decode and print
generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
print(f"Generated Answer:\n{generated_text}")
```

## Sample Output
```
### Question: What is the role of the tumor microenvironment in cancer progression, and how does it influence the response to therapy?
### Answer:
The tumor microenvironment (TME) refers to the complex network of cells, extracellular matrix components, signaling molecules, and immune cells that surround a growing tumor. It plays an essential role in regulating various aspects of cancer development and progression...

### References:
1. Hanahan D, Weinberg RA. Hallmarks of Cancer: The Next Generation. Cell. 2011;144(5):646-74. doi:10.1016/j.cell.2011.03.019
2. Coussens LM, Pollard JW. Angiogenesis and Metastasis. Nature Reviews Cancer. 2006;6(1):57-68. doi:10.1038/nrc2210
3. Mantovani A, et al. Cancer's Educated Environment: How the Tumour Microenvironment Promotes Progression. Cell. 2017;168(6):988-1001.e15. doi:10.1016/j.cell.2017.02.011
4. Cheng YH, et al. Targeting the Tumor Microenvironment for Improved Therapy Response. Journal of Clinical Oncology. 2018;34(18_suppl):LBA10001. doi:10.1200/JCO.2018.34.18_suppl.LBA10001
5. Kang YS, et al. Role of the Tumor Microenvironment in Cancer Immunotherapy. Current Opinion in Pharmacology. 2018;30:101-108. doi:10.1016/j.ycoop.20
```

## Model Details
- **Base Model**: Mistral-7B-Instruct-v0.2
- **Primary Training Data**: 10 million PubMed abstracts and titles
- **Specialization**: Medical question-answering with scientific citations
- **Output**: Generates detailed answers with relevant academic references

## Future Development
ClinicalGPT-Pubmed-Instruct-V2.0 is under development, featuring:
- Training on new 20 million pubmed articles
- Inclusion of full-text articles from various academic sources
- Enhanced performance for life science tasks
- Expanded citation capabilities across multiple scientific databases

## Contributors
- Rohit Anurag – Principal Data Scientist
- Aneesh Paul – Data Scientist

## License
Licensed under the Apache License, Version 2.0. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0