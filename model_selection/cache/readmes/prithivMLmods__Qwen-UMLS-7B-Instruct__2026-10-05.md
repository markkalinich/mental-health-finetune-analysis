---
license: creativeml-openrail-m
datasets:
- avaliev/umls
language:
- en
base_model:
- Qwen/Qwen2.5-7B-Instruct
pipeline_tag: text-generation
library_name: transformers
tags:
- safetensors
- Unified Medical Language System
- Qwen2.5
- 7B
- Instruct
- Medical
- text-generation-inference
- National Library of Medicine
- umls
---


### Qwen-UMLS-7B-Instruct `[ Unified Medical Language System ]`

The **Qwen-UMLS-7B-Instruct** model is a specialized, instruction-tuned language model designed for medical and healthcare-related tasks. It is fine-tuned on the **Qwen2.5-7B-Instruct** base model using the **UMLS (Unified Medical Language System)** dataset, making it an invaluable tool for medical professionals, researchers, and developers building healthcare applications.

| **File Name**                          | **Size**       | **Description**                                  | **Upload Status**  |
|-----------------------------------------|----------------|-------------------------------------------------|--------------------|
| `.gitattributes`                        | 1.57 kB        | File to specify LFS rules for large file tracking. | Uploaded           |
| `README.md`                             | 323 Bytes      | Basic project information file.                 | Updated            |
| `added_tokens.json`                     | 657 Bytes      | Contains additional tokens for the tokenizer.   | Uploaded           |
| `config.json`                           | 860 Bytes      | Configuration file for the model.               | Uploaded           |
| `generation_config.json`                | 281 Bytes      | Configuration file for generation settings.     | Uploaded           |
| `merges.txt`                            | 1.82 MB        | Byte-pair encoding merge rules for tokenization.| Uploaded           |
| `pytorch_model-00001-of-00004.bin`      | 4.88 GB        | First part of the model's PyTorch checkpoint.   | Uploaded (LFS)     |
| `pytorch_model-00002-of-00004.bin`      | 4.93 GB        | Second part of the model's PyTorch checkpoint.  | Uploaded (LFS)     |
| `pytorch_model-00003-of-00004.bin`      | 4.33 GB        | Third part of the model's PyTorch checkpoint.   | Uploaded (LFS)     |
| `pytorch_model-00004-of-00004.bin`      | 1.09 GB        | Fourth part of the model's PyTorch checkpoint.  | Uploaded (LFS)     |
| `pytorch_model.bin.index.json`          | 28.1 kB        | Index file mapping layers to checkpoint shards. | Uploaded           |
| `special_tokens_map.json`               | 644 Bytes      | Maps special tokens like `[CLS]`, `[SEP]`, etc. | Uploaded           |
| `tokenizer.json`                        | 11.4 MB        | Tokenizer definition and configuration.         | Uploaded (LFS)     |
| `tokenizer_config.json`                 | 7.73 kB        | Configuration file for the tokenizer.           | Uploaded           |
| `vocab.json`                            | 2.78 MB        | Vocabulary file for tokenization.               | Uploaded           |

### **Key Features:**

1. **Medical Expertise:**  
   - Trained on the UMLS dataset, ensuring deep domain knowledge in medical terminology, diagnostics, and treatment plans.

2. **Instruction-Following:**  
   - Designed to handle complex queries with clarity and precision, suitable for diagnostic support, patient education, and research.

3. **High-Parameter Model:**  
   - Leverages 7 billion parameters to deliver detailed, contextually accurate responses.

---

### **Training Details:**

- **Base Model:** [Qwen2.5-7B-Instruct](#)  
- **Dataset:** [avaliev/UMLS](#)  
  - Comprehensive dataset of medical terminologies, relationships, and use cases with 99.1k samples.
---
### **Capabilities:**

1. **Clinical Text Analysis:**  
   - Interpret medical notes, prescriptions, and research articles.

2. **Question-Answering:**  
   - Answer medical queries, provide explanations for symptoms, and suggest treatments based on user prompts.

3. **Educational Support:**  
   - Assist in learning medical terminologies and understanding complex concepts.

4. **Healthcare Applications:**  
   - Integrate into clinical decision-support systems or patient care applications.
---
### **Usage Instructions:**

1. **Setup:**
   Download all files and ensure compatibility with the Hugging Face Transformers library.

2. **Loading the Model:**
   ```python
   from transformers import AutoModelForCausalLM, AutoTokenizer
   
   model_name = "prithivMLmods/Qwen-UMLS-7B-Instruct"
   tokenizer = AutoTokenizer.from_pretrained(model_name)
   model = AutoModelForCausalLM.from_pretrained(model_name)
   ```

3. **Generate Medical Text:**
   ```python
   input_text = "What are the symptoms and treatments for diabetes?"
   inputs = tokenizer(input_text, return_tensors="pt")
   outputs = model.generate(**inputs, max_length=200, temperature=0.7)
   print(tokenizer.decode(outputs[0], skip_special_tokens=True))
   ```

4. **Customizing Outputs:**
   Modify `generation_config.json` to optimize output style:
   - `temperature` for creativity vs. determinism.
   - `max_length` for concise or extended responses.

---

### **Applications:**

1. **Clinical Support:**  
   - Assist healthcare providers with quick, accurate information retrieval.

2. **Patient Education:**  
   - Provide patients with understandable explanations of medical conditions.

3. **Medical Research:**  
   - Summarize or analyze complex medical research papers.

4. **AI-Driven Diagnostics:**  
   - Integrate with diagnostic systems for preliminary assessments.

---