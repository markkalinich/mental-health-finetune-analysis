---
language:
  - en
license: other
license_name: nvidia-open-model-license
license_link: https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/
library_name: transformers
pipeline_tag: text-classification
tags:
  - text-classification
  - refusal-detection
  - LLM safety
  - modernbert
  - garak
base_model: answerdotai/ModernBERT-base
---
# Garak Refusal Detector

## Description:  
Garak Refusal Detector is a binary sequence classifier model that detects refusal responses in LLM outputs. The model is built as a semantic replacement for string-based keyword detectors (e.g., Garak's MitigationBypass detector), enabling refusal detection based on meaning rather than surface patterns.

This model is ready for commercial use.

## Key Features:
- Semantic refusal detection based on transformer classification
- Trained on 20K synthetic samples generated via NeMo Data Designer covering:
  - **5 compliance degrees:** complete_refusal, partial_refusal, refusal_with_redirection, full_fulfillment, fulfillment_with_disclaimer
  - **7 refusal communication styles:** direct_ethical, policy_based, brief_decline, educational, censorship, misinformation, disclaimer_technical

### License/Terms of Use:   
Governing Terms: Use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/).

### Deployment Geography:  
Global

### Use Case:  
Developers integrating the Garak framework can use this model to detect refusal responses in LLM outputs. It serves as an alternative to keyword‑based detectors, using a transformer‑based classifier that returns a binary signal indicating refusal or non‑refusal.  

### Release Date:

- **HuggingFace**: 03/24/2026

## Reference(s):
- [Garak: A Framework for Security Probing Large Language Models](https://github.com/NVIDIA/garak)
- [NeMo Data Designer — Synthetic Data Generation](https://build.nvidia.com/nemo/data-designer)
- [ModernBERT-base — A Modern Bidirectional Encoder](https://huggingface.co/answerdotai/ModernBERT-base)

## Model Architecture:   
Garak Refusal Detector is a fine-tuned version of answerdotai/ModernBERT-base, trained on synthetic refusal and non-refusal data for binary sequence classification.

ModernBERT was chosen as the base model for its improved downstream performance and faster processing compared to older encoder architectures like BERT, RoBERTa, and DeBERTa. It supports sequences up to 8,192 tokens and serves as a drop-in replacement for any BERT-like model, making it well-suited for text classification tasks where inference speed and accuracy both matter.

- **Base Model**: answerdotai/ModernBERT-base
- **Network Architecture**: Transformer (Encoder-only)
- **Number of Layers**: 22
- **Total Parameters**: 149 Million (149M)

### Computational Load

- **Cumulative Compute**: approximately 1.8 × 10²¹ FLOPs (mainly from the original ModernBERT-base model).
- **Estimated Energy and Emissions for Model Training**: Estimated Energy Consumption: ~1,430 – 1,540 kWh, Estimated Carbon Emissions (Gross): ~0.08 – 0.63 $tCO_2e$ (mainly from the original ModernBERT-base model, trained on 8× H100 SXM GPUs for 245.6 hours in France). Actual fine-tuning of the model: < 1 kWh, < 0.5 kg $CO_2e$
 

## Input:  
**Input Type(s):** Text  
**Input Format(s):** String  
**Input Parameters:** One-Dimension (1D)  
**Other Properties Related to Input:** The model accepts text inputs up to 8,192 tokens (ModernBERT native context window). It uses a ModernBERT tokenizer with a vocabulary size of 50,368 tokens and a hidden size of 768. Input sequences are padded/truncated to the maximum length before classification.  
  

## Output:  
**Output Type(s):** Score  
**Output Format:** Floating-point score  
**Output Parameters:** One-Dimensional (1D)  
**Other Properties Related to Output:** The model outputs a predicted class label (`refusal` or `non-refusal`) together with a confidence score between 0.0 and 1.0 representing the probability assigned to the predicted class.
   

Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.

## Software Integration:  
**Runtime Engine(s):**
- PyTorch
- ONNX Runtime
- Triton Inference Server
- TensorRT

**Supported Hardware Microarchitecture Compatibility:**
- NVIDIA Ampere
- NVIDIA Hopper
- NVIDIA Blackwell

**Supported Operating System(s):**
- Linux
- Windows

The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.  

## Model Version(s): 
1.0 
 
## Training, Testing, and Evaluation Datasets:

Dataset Partition: Training (70%), Evaluation (10%), Testing (20%)

## Training Dataset:

**Data Modality:** Text  
**Text Training Data Size:** Less than a Billion Tokens  
**Data Collection Method by dataset:** Hybrid: Automated, Synthetic
**Labeling Method by dataset:** Automated  
**Properties (Quantity, Dataset Descriptions, Sensor(s)):** The training set is entirely synthetic text generated with NVIDIA NeMo Data Designer using the NVIDIA‑Nemotron‑Nano‑9B‑v2 model. The model was **not** trained directly on OR‑Bench data; instead, three OR‑Bench subsets were used exclusively as **seed prompts** for synthetic data generation: OR‑Bench Toxic (655 prompts), OR‑Bench 80K (80,400 prompts), and OR‑Bench Hard 1K (1,320 prompts). The generation pipeline paraphrases these seed prompts and produces new synthetic responses with controlled compliance degrees and communication styles. A total of 20,000 synthetic samples were generated (10K refusal, 10K non‑refusal). After quality analysis and removal of 14 critical mislabels, 19,879 samples were used for training. Text characteristics include average lengths of 297 characters (57 tokens) for refusals and 1,092 characters (202 tokens) for non‑refusals.  
**Seed Dataset Link:** https://huggingface.co/datasets/bench-llms/or-bench   

## Testing Dataset:

**Data Modality:** Text  
**Data Collection Method by dataset:** Hybrid: Automated, Synthetic  
**Labeling Method by dataset:** Automated  
**Properties (Quantity, Dataset Descriptions, Sensor(s)):** The testing set is a held‑out 20% random split (seed 42) of the same synthetic dataset used for training, produced with NVIDIA NeMo Data Designer and the NVIDIA‑Nemotron‑Nano‑9B‑v2 model. It contains approximately 3,976 samples with a balanced class distribution (refusal and non‑refusal). Because the split is performed after deduplication and mislabel removal, the testing partition shares the same generation pipeline, compliance degrees, communication styles, and text‑length characteristics as the training set but contains no overlapping samples.

### Evaluation Dataset:
**Links:**  
- https://huggingface.co/datasets/s-nlp/multilingual_refusals  
- https://huggingface.co/datasets/anthracite-org/kalo-opus-instruct-22k-no-refusal  

**Benchmark Score:** accuracy=91.10%  
**Data Collection Method by dataset:** Automated  
**Labeling Method by dataset:** Hybrid: Automated, Human
**Properties (Quantity, Dataset Descriptions, Sensor(s)):** A balanced evaluation dataset of 7,102 samples combining refusal examples from s-nlp/multilingual_refusals (multilingual refusal detection dataset with human-labeled refusals) and non-refusal examples from anthracite-org/kalo-opus-instruct-22k-no-refusal (instruction-following conversations without refusal behavior). The two sources were merged into a balanced binary classification benchmark.   


| Metric | Value |
|--------|-------|
| **Total samples** | 7,102 |
| **Accuracy** | 92.06% |
| **Throughput** | 593.9 samples/sec |
| **Latency** | 1.68 ms/sample |

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| Refusal | 96.08% | 87.69% | 91.70% | 3,551 |
| Non-refusal | 88.68% | 96.42% | 92.39% | 3,551 |

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.  

For more detailed information on ethical considerations for this model, please see the Model Card++ Explainability, Bias, Safety & Security, and Privacy Subcards.  

Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

### Explainability

#### Intended Domain
AI Safety and LLM Evaluation

#### Model Type
Binary Classifier (Encoder-only Transformer, fine-tuned ModernBERT-base)

#### Intended Users
Developers building LLM moderation tools and AI safety researchers use the model to automatically detect refusal responses in LLM outputs for robust compliance and moderation.

#### Output
Float score: 1.0 (refusal) or 0.0 (non-refusal)

#### Describe how the model works:
The model is a transformer‑based sequence classifier that uses ModernBERT to encode input text and outputs a binary score indicating whether the response is a refusal.

#### Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of:
Not Applicable

#### Technical Limitations:
The model may produce false positives or negatives and may not generalize to all refusal styles.

#### Verified to have met prescribed NVIDIA quality standards:
Yes

#### Performance Metrics:
Accuracy, F-1 Score, Throughput, & Latency

#### Potential Known Risks:
This model may produce inaccurate refusal classifications.

#### Terms of Use:
Use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/)

### Privacy

#### Generatable or reverse engineerable personal data?
No

#### Personal data used to create this model?
No

#### How often is dataset reviewed?
Before Every Release

#### Was data from user interactions with the AI model (e.g. user input and prompts) used to train the model?
No

#### Is there provenance for all datasets used in training?
Yes

#### Does data labeling (annotation, metadata) comply with privacy laws?
Yes

#### Is data compliant with data subject requests for data correction or removal, if such a request was made?
Not Applicable

#### Applicable Privacy Policy
https://www.nvidia.com/en-us/about-nvidia/privacy-policy/

### Safety & Security

#### Model Application(s):
Text Classification (Refusal Detection)

#### Describe the life-critical impact (if present).
Not Applicable

#### Use Case Restrictions:
Use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/)

#### Model and dataset restrictions:
The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training, and dataset license constraints adhered to.

### Bias

#### Participation considerations from adversely impacted groups protected classes in model design and testing
Not Applicable

#### Measures taken to mitigate against unwanted bias
Not Applicable
