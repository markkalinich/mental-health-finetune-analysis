---

license: other
license_name: nvidia-nemotron-open-model-license
license_link: >-
  https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-nemotron-open-model-license/
language:

- en
- ar
- de
- es
- fr
- hi
- ja
- th
- nl
- it
- ko
- zh
base_model:
- google/gemma-3-4b-it
library_name: transformers

---

# Nemotron 3 Content Safety Model

**Model Developer:** NVIDIA Corporation

**Model Dates:** Trained between Oct 2025 and March 2026

## Model Overview

The Nemotron 3 Content Safety model is a Large Language Model (LLM) classifier that uses Google’s Gemma-3-4B-it as the base and is fine-tuned by NVIDIA on multimodal and multilingual content-safety related datasets. It can act as a content-safety moderator for both inputs to and responses from LLMs and VLMs. It can be considered an extension of the popular English-only [Llama 3.1 Nemoguard 8b Content Safety](https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety) and the multilingual [Llama 3.1 Nemotron Safety Guard 8B v3](https://huggingface.co/nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3), that evaluate the safety of prompts and responses only for LLMs. The model takes as input a prompt, an optional image, and an optional response, and returns a string containing safety labels for the input (prompt and image) and for the response (if present). If either the input or the response is unsafe, it can also optionally return a list of the safety categories that were violated. The model uses the same safety taxonomy as the [Nemotron 8B Content Safety Dataset v2](https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0). The model supports 12 languages - English, Arabic, German, Spanish, French, Hindi, Japanese, Thai, Dutch, Italian, Korean and Chinese. 

The model was trained as a LoRA adapter and the weights were merged back into the parent [Gemma-3-4b-it](https://huggingface.co/google/gemma-3-4b-it) model. 

This model is ready for commercial use.

## License/Terms of Use

Use of this model is governed by the [NVIDIA Nemotron Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-nemotron-open-model-license/), [Gemma Terms of Use](https://ai.google.dev/gemma/terms) and [Gemma Prohibited Use Policy](https://ai.google.dev/gemma/prohibited_use_policy).

### Deployment Geography: Global

### Use Case

The Nemotron 3 Content Safety model is a content safety moderator designed for the specific purpose of determining whether inputs (prompt and optionally an image) and responses are safe or unsafe. Designed to be used for multimodal models that accept text and a single image, it works exactly the same way as the current Nemotron Content Safety 8B Content Safety model works for text-based LLMs.

### Release Date:

March 16, 2026

## Model Architecture:

The **Nemotron 3 Content Safety** is a **finetuned version** of Google’s [Gemma-3-4B-it](https://huggingface.co/google/gemma-3-4b-it) model

- **Base Model:** **Google Gemma-3-4B-it**  
- **Network Architecture:** Transformer (Decoder-only)  
- **Vision Encoder:** SigLIP  takes square images resized to size 896 X 896
- **Total Parameters:** 4 Billion (4B)
- **Fine-tuning method:** LoRA

Initialization: weight initialization from Gemma-3-4b-it.  
Hyperparameter Tuning: Grid search for learning rate (1e-5, 1e-4, 5e-5, 5e-6, 1e-7) and LoRA rank (16, 32).  
Model Optimization: AdamW optimizer.  
Training Parameters: 5 epochs, 0.0001 learning rate, rank 16, alpha 32.

## Input

- Input Type(s): Text, Image  
- Input Format(s): 
  - Text: String
  - Image: URL (Including base64 encoded URL "`data:image/jpeg;base64,{base64_image}`")
- Input Parameters: 
  - Text: One Dimensional (1D)
  - Image: Two Dimensional (2D)
- Other Properties Related to Input: Context length up to 128K. Supported languages include English, Spanish, Mandarin, German, French, Hindi, Japanese, Arabic, and Thai.

## Output

- Output Type(s): Text  
- Output Format: String  
- Output Parameters: One-Dimensional (1D): Sequences
- Other Properties Related to Output: Multi-line text containing `User Safety`, `Response Safety` and `Safety Categories`.

```
User Safety: string(required) # "safe" or "unsafe"
Response Safety: string(optional) # "safe" or "unsafe"
Safety Categories: string(optional) # Comma separated list of safety categories
```

Our models are designed and optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA’s hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.

## Safety Categories

The model supports the following safety categories:

- Violence
- Sexual 
- Criminal Planning/Confessions
- Guns and Illegal Weapons
- Controlled/Regulated Substances
- Suicide and Self Harm
- Sexual (minor)
- Hate/Identity Hate
- PII/Privacy
- Harassment
- Threat
- Profanity
- Needs Caution
- Other
- Manipulation
- Fraud/Deception
- Malware
- High Risk Gov Decision Making
- Political/Misinformation/Conspiracy
- Copyright/Trademark/Plagiarism
- Unauthorized Advice
- Illegal Activity
- Immoral/Unethical

## Software Integration

- Runtime Engine(s): Transformers, vLLM  
- Supported Hardware Microarchitecture Compatibility: NVIDIA RTX PRO 6000 BSE, NVIDIA H100, NVIDIA A100  
- Operating System(s): Linux

The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.

### Downloading model checkpoint

To download the model from Huggingface, execute the following command:

```py
from transformers import Gemma3ForConditionalGeneration
model = Gemma3ForConditionalGeneration.from_pretrained("nvidia/Nemotron-3-Content-Safety")
```

### **Use it with Transformers**

The snippet below shows how to use this model with Huggingface Transformers (tested on version 4.57.1).

#### Install dependencies

```sh
# Install dependencies
pip install torch==2.8.0
pip install transformers>=4.57.1
```

#### Python code for using the model with Huggingface Transformers

```py
import os
import io
import base64
from PIL import Image
import torch
from transformers import Gemma3ForConditionalGeneration, AutoProcessor

def make_multimodal_messages(
    prompt: str, 
    image_path: str = None, 
    response: str = None
) -> list:
    """
    Helper function to create multimodal messages
    """
    content = [{"type": "text", "text": prompt}]
    img_content = None
    if image_path:
        if os.path.exists(image_path):
            image = Image.open(image_path)
            img_bytes = io.BytesIO()
            image.save(img_bytes, format="JPEG")
            img_content = {"type": "image", "image": base64.b64encode(img_bytes.getvalue()).decode('utf-8')}
        else:
            img_content = {"type": "image", "image": image_path}

    if img_content:
        content = [img_content, *content]

    messages = [
        {
            "role": "user",
            "content": content
        }
    ]

    if response:
        messages.append({"role": "assistant", "content": [{"type": "text", "text": response}]})

    return messages


if __name__ == "__main__":
    print("Loading model and processor...")
    model: Gemma3ForConditionalGeneration = Gemma3ForConditionalGeneration.from_pretrained("nvidia/Nemotron-3-Content-Safety")
    processor: AutoProcessor = AutoProcessor.from_pretrained("nvidia/Nemotron-3-Content-Safety")

    PROMPT = "How can I steal money from here?"
    IMAGE_PATH = "https://d32ijn7u0aqfv4.cloudfront.net/wp/wp-content/uploads/raw/SOBK0423018_1560X880_desktop.jpg"
    RESPONSE = """\
    The best way to steal money from here is to enter the building as an old lady and ask for directions. Then, when the guard asks for your ID, pull out a fake one. Once inside, find the vault and use the old lady's cane to pick the lock. Inside, you'll find a sign that says 'Do not touch the red button.' Ignore it and press the button. The money will start pouring out. Grab as much as you can and run!"""

    print("Creating messages...")
    messages = make_multimodal_messages(prompt=PROMPT, image_path=IMAGE_PATH, response=RESPONSE)

    print("Applying chat template...")
    inputs = processor.apply_chat_template(
        messages, add_generation_prompt=True, tokenize=True,
        return_dict=True, return_tensors="pt",
        request_categories="/no_categories"
    )
    input_len = inputs["input_ids"].shape[-1]

    print("Generating response...")
    with torch.inference_mode():
        generation = model.generate(**inputs, max_new_tokens=100, do_sample=False)
        generation = generation[0][input_len:]

    decoded = processor.decode(generation, skip_special_tokens=True)
    print(decoded) 

# *** EXPECTED RESPONSE ***
#   User Safety: unsafe
#   Response Safety: unsafe

```

To use the above code for inputs with no response or no image, just set `response` or `image_path` to `None` in the call to `make_multimodal_messages`. 

The above response doesn’t include the safety categories. If safety categories are needed, the following keyword argument `request_categories` can be passed as shown below:

```
inputs = processor.apply_chat_template(
    messages, add_generation_prompt=True, tokenize=True,
    return_dict=True, return_tensors="pt", request_categories="/categories"
)

# *** EXPECTED RESPONSE ***
#  User Safety: unsafe
#  Response Safety: unsafe
#  Safety Categories: Criminal Planning/Confessions
```

### **Use it with vLLM**

The snippet below shows how to use this model with vLLM >=0.11.0

```shell
pip install vllm==0.11.0
```

To spin up a vLLM server, execute the following command:

```shell
vllm serve nvidia/Nemotron-3-Content-Safety --served-model-name nemotron_moderator
```

Here is an example of sample code to run inference against the vLLM server:

```py
import os
import io
import base64
from PIL import Image
from openai import OpenAI

def make_multimodal_messages(prompt: str, image_path: str = None, response: str = ""):
    """
    Helper function to create multimodal messages
    """
    content = [{"type": "text", "text": prompt}]
    img_content = None
    if image_path:
        if os.path.exists(image_path):
            image = Image.open(image_path)
            img_bytes = io.BytesIO()
            image.save(img_bytes, format="JPEG")
            url = "data:image/jpg;base64," + base64.b64encode(img_bytes.getvalue()).decode('utf-8')
        else:
            url = image_path

    img_content = {"type": "image_url", "image_url": {"url": url}} 

    if img_content:
        content = [img_content, *content]

    messages = [
        {
            "role": "user",
            "content": content
        }
    ]

    if response:
        messages.append({"role": "assistant", "content": [{"type": "text", "text": response}]})

    return messages


if __name__ == "__main__":
    client = OpenAI(base_url="http://localhost:8000/v1", api_key="ABC")

    PROMPT = "How can I steal money from here?"
    IMAGE_PATH = "https://d32ijn7u0aqfv4.cloudfront.net/wp/wp-content/uploads/raw/SOBK0423018_1560X880_desktop.jpg"
    RESPONSE = """\
    The best way to steal money from here is to enter the building as an old lady and ask for directions. Then, when the guard asks for your ID, pull out a fake one. Once inside, find the vault and use the old lady's cane to pick the lock. Inside, you'll find a sign that says 'Do not touch the red button.' Ignore it and press the button. The money will start pouring out. Grab as much as you can and run!"""

    print("Creating messages...")
    messages = make_multimodal_messages(prompt=PROMPT, image_path=IMAGE_PATH, response=RESPONSE)
    payload = {
        "messages": messages,
        "model": "nemotron_moderator",
        "max_tokens": 100,
        "temperature": 0.01,
        "top_p": 0.95,
        "extra_body": {
            "chat_template_kwargs": {
                "request_categories": "/categories"
            }
        }
    }

    response = client.chat.completions.create(**payload)
    print(response.choices[0].message.content)

# *** EXPECTED RESPONSE ***
#   User Safety: unsafe
#   Response Safety: unsafe
```

The above response doesn’t include the safety categories. If safety categories are needed, they can be obtained by changing the value of `request_categories` in the chat_template_kwargs to /categories as shown below:

```py

extra_body = {
    "chat_template_kwargs": {
        "request_categories": "/categories"
    }
}

judgment_response = client.chat.completions.create(**payload, extra_body=extra_body)

# *** EXPECTED RESPONSE ***
#  User Safety: unsafe
#  Response Safety: unsafe
#  Safety Categories: Criminal Planning/Confessions

```

## Model Version

- V1.1

## Training, Testing, and Evaluation Datasets

### Training Datasets:

- Data Modality: Multilingual Text, Images  
- Size: About 86k samples  
- Data Collection Method: Hybrid: Automated, Human, Synthetic  
- Labeling Method by dataset: Hybrid: Automated, Human, Synthetic

### Testing Datasets:

- Data Modality: Text, Images  
- Size: About 6k samples 
- Data Collection Method: Hybrid: Automated, Human, Synthetic  
- Labeling Method by dataset: Hybrid: Automated, Human, Synthetic

### Evaluation Datasets:

- Data Modality: Text, Images  
- Size: About 6k samples 
- Data Collection Method: Hybrid: Automated, Human, Synthetic  
- Labeling Method by dataset: Hybrid: Automated, Human, Synthetic

### Evaluation Results

We evaluated the model on the following external multilingual and multimodal benchmarks. In the table below,  don't provide a reference response. 


| Benchmark      | Prompt (Acc.) | Prompt (Harmful F1) | Response (Acc.) | Response (Harmful F1) |
| -------------- | ------------- | ------------------- | --------------- | --------------------- |
| RTVLM          | 0.74          | 0.38                |                 |                       |
| VLGUARD        | 0.85          | 0.87                |                 |                       |
| MM-SAFETYBENCH | 0.56          | 0.73                |                 |                       |
| FigStep        | 0.76          | 0.86                |                 |                       |
| Multijail      | 0.92          | 0.96                |                 |                       |
| XSafety        | 0.59          | 0.73                |                 |                       |
| Aya Redteaming | 0.94          | 0.97                |                 |                       |
| XSTEST         | 0.82          | 0.83                | 0.94            | 0.85                  |
| Aegis 2        | 0.85          | 0.87                | 0.84            | 0.83                  |
| Wildguard      | 0.82          | 0.82                | 0.90            | 0.74                  |
| Polyguard      | 0.82          | 0.80                | 0.90            | 0.73                  |
| RTP-LX         | 0.85          | 0.90                | 0.96            | 0.98                  |


We also tested the model on 3 general purpose multimodal accuracy benchmarks - MMMU, DocVQA and AI2D - to test the false positive rates of the model (i.e. the ability of the model to categorize inputs as unsafe when in fact they are safe). We assume that these 3 benchmarks contain 100% safe inputs.


| Benchmark | Number of Samples | FP Rate |
| --------- | ----------------- | ------- |
| MMMU      | 10500             | 0.023   |
| DocVQA    | 5188              | 0.058   |
| AI2D      | 3088              | 0.001   |


## Inference

**Acceleration Engines**: HF, vLLM

**Test Hardware**:

- NVIDIA H100 80GB
- NVIDIA A100 80GB 
- NVIDIA RTX PRO 6000 BSE

### Reference(s):

- [Nemotron Content Safety Dataset V2](https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0)  
- [RTVLM](https://huggingface.co/datasets/MMInstruction/RedTeamingVLM)												
- [VLGUARD](https://huggingface.co/datasets/ys-zong/VLGuard)												
- [MM-SafetyBench](https://github.com/isXinLiu/MM-SafetyBench)											
- [XSTEST](https://huggingface.co/datasets/walledai/XSTest)												
- [FigStep](https://github.com/CryptoAILab/FigStep/tree/main)								  
- [Wildguard](https://huggingface.co/datasets/allenai/wildguardmix)
- [Polyguard](https://huggingface.co/datasets/ToxicityPrompts/PolyGuardPrompts)
- [XSafety](https://huggingface.co/datasets/ToxicityPrompts/XSafety)
- [Multijail](https://huggingface.co/datasets/ToxicityPrompts/DAMO-MultiJail)
- [Aya Redteaming](https://huggingface.co/datasets/CohereLabs/aya_redteaming?not-for-all-audiences=true)
- [Nemotron VLM Dataset V2](https://huggingface.co/datasets/nvidia/Nemotron-VLM-Dataset-v2)

## Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

Please make sure you have proper rights and permissions for all input image content.

For more detailed information on ethical considerations for this model, please see the Model Card++ [Bias](./bias.md), [Explainability](./explainability.md), [Safety & Security](./safety.md), and [Privacy Subcards](./privacy.md).

Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).