---
license: mit
datasets:
- FreedomIntelligence/medical-o1-reasoning-SFT
language:
- en
metrics:
- accuracy
base_model:
- deepseek-ai/DeepSeek-R1-Distill-Qwen-7B
pipeline_tag: text-generation
tags:
- medical
library_name: transformers
---
# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->

The model was fine-tuned to build a chat agent in our Honours project in 2025W.

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

The model was fine-tuned using Deep-R1-Distill-Qwen-7B, a distilled version of deepseek r1. 
Deepseek r1 was a general large language model(LLM) developed by DeepSeek in 2024, a Chinese company specialized in AGI R&D.

The dataset used for fine-tuning is medical-o1-reasoning-SFT, which contains 20k+ of verifiable medical questions from various medical exams, along with a complete chain-of-thought(CoT) that leads to a ground truth answer.
It was very effective in fine-tuning the base model, enabling it to infer the patient's symptoms efficiently and effectively in the medical scenario.

The model will serve as an NLP agent in our honours project - *AI-Driven Health Monitoring and Prediction Application*, which aims to develop a modern web application that focuses on personal health management and virtual healthcare services.
Our project is part of the *CSI4900: Honours Project course* in Winter 2025 Semester at the University of Ottawa.

- **Developed by:** JW, YC, DC (First initial + last initial)
- **Funded by:** Self-funded
- **Shared by:** Our group
- **Model type:** Text-generation
- **Language(s) (NLP):** English
- **License:** MIT
- **Finetuned from model:** [deepseek-ai/DeepSeek-R1-Distill-Qwen-7B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B)

### Base Model Sources

<!-- Provide the basic links for the model. -->

- **Repository:** https://github.com/deepseek-ai/DeepSeek-R1
- **Paper:** [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://github.com/deepseek-ai/DeepSeek-R1/blob/main/DeepSeek_R1.pdf)

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

The model is intended to handle **text-generation and question-answering** tasks in a medical scenario. Potential users include companies and researchers that are interested in AI + healthcare applications.


### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->

The model might not work well in real-world applications as it was based on a distilled model with a limited number of parameters, which can lead to inaccurate or misleading answers.
Our model was mainly used for educational purposes only. For serious applications, consider using models with more parameters.

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

The output of the model is subjected to false and inaccurate information. For medical purposes such as symptom diagnosis and treatment please consult with professional personnel at your local hospital/clinics.

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model. More information needed for further recommendations.

## How to Get Started with the Model

Use the code below to get started with the model.

Using Conda with FastAPI, we can set up a local environment that can run the model in a local server, that can be accessed by other applications via API.

``` python
from fastapi import FastAPI
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch

app = FastAPI()

# Model path
model_path = "Insert path to your model here"

# Load Tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_path)

my_quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype="float16"
)

# Load model and move to GPU/CPU
device = "cuda" if torch.cuda.is_available() else "cpu"
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map="auto", 
    quantization_config=my_quantization_config    
)

@app.get("/generate")
async def generate_text(prompt: str) -> dict:
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    
    outputs = model.generate(inputs["input_ids"],attention_mask=inputs["attention_mask"], max_length=1024, repetition_penalty=1.2)
    
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    clean_response = generated_text[len(prompt):].strip()

    # generated_text = "This is the response"
    
    return {"generated_text": clean_response}
```

For cloud deployment, consider using [Huggingface Inference Endpoints](https://huggingface.co/inference-endpoints/dedicated) or [Amazon Sagemaker](https://aws.amazon.com/sagemaker/)

## Training Details

### Training Data

<!-- This should link to a Dataset Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

Please check out the training datasets above.

### Training Procedure

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

We trained our model using the LoRA (Low-Rank Adaptation) algorithm for a total of 30 epochs. The total training time is around 20-30 hours.

Since we are short on budget (and GPU computational power), we only used a batch size of 2 (as using more will lead to CUDA out of memory problem), which leads to long training time.


#### Training Hyperparameters

- **Training regime:** bf16 mixed precision <!--fp32, fp16 mixed precision, bf16 mixed precision, bf16 non-mixed precision, fp16 non-mixed precision, fp8 mixed precision -->


## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

### Testing Data, Factors & Metrics

#### Testing Data

<!-- This should link to a Dataset Card if possible. -->

We have reserved 20% of the data for validation.


#### Metrics

<!-- These are the evaluation metrics being used, ideally with a description of why. -->

Training loss and evaluation loss

### Results

Training loss:
![training.jpg](https://raw.githubusercontent.com/ViunesC/4142-datasets/refs/heads/main/res/img/training_loss.png)

Evaluation loss:
![eval.jpg](https://raw.githubusercontent.com/ViunesC/4142-datasets/refs/heads/main/res/img/training_eval_loss.png)

Evaluation, manually using medical questions:

CoT before training:
![cot_before.jpg](https://github.com/ViunesC/4142-datasets/blob/main/res/img/cot_before.png?raw=true)

CoT after training:
![cot_after.jpg](https://github.com/ViunesC/4142-datasets/blob/main/res/img/cot_after.png?raw=true)


## Environmental Impact

<!-- Total emissions (in grams of CO2eq) and additional considerations, such as electricity usage, go here. Edit the suggested text below accordingly -->

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).

- **Hardware Type:** Nvidia RTX 4090D 24GB
- **Hours used:** 20-30 hours
- **Cloud Provider:** AutoDL
- **Compute Region:** Chongqing, China
- **Carbon Emitted:** around 6.12 kg of CO2


## Model Card Contact

For any inquiries, please send them to this email address: jwang751@uOttawa.ca. Thank you!