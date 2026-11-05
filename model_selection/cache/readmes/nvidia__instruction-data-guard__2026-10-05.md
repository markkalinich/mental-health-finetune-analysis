---
tags:
- model_hub_mixin
- pytorch_model_hub_mixin
license: other
---

# NemoCurator Instruction Data Guard

# Model Overview

## Description:
Instruction Data Guard is a deep-learning classification model that helps identify LLM poisoning attacks in datasets.
It is trained on an instruction:response dataset and LLM poisoning attacks of such data.
Note that optimal use for Instruction Data Guard is for instruction:response datasets.

### License/Terms of Use:
[NVIDIA Open Model License Agreement](https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf)

## Reference:
The Internal State of an LLM Knows When It's Lying: https://arxiv.org/pdf/2304.13734 <br> 

## Model Architecture:
**Architecture Type:** FeedForward MLP <br>
**Network Architecture:** 4 Layer MLP <br>

## Input:
**Input Type(s):** Text Embeddings <br>
**Input Format(s):** Numerical Vectors <br>
**Input Parameters:** 1D Vectors <br>
**Other Properties Related to Input:** The text embeddings are generated from the [Aegis Defensive Model](https://huggingface.co/nvidia/Aegis-AI-Content-Safety-LlamaGuard-Defensive-1.0). The length of the vectors is 4096. <br>

## Output:
**Output Type(s):** Classification Scores <br>
**Output Format:** Array of shape 1 <br>
**Output Parameters:** 1D <br>
**Other Properties Related to Output:** Classification scores represent the confidence that the input data is poisoned or not. <br> 

## Software Integration:
**Runtime Engine(s):** 
* NeMo Curator: https://github.com/NVIDIA-NeMo/Curator <br>
* Aegis: https://huggingface.co/nvidia/Aegis-AI-Content-Safety-LlamaGuard-Defensive-1.0 <br>

**Supported Hardware Microarchitecture Compatibility:** <br>
* NVIDIA Ampere <br>
* NVIDIA Hopper <br>

**Preferred Operating System(s):** <br>
* Linux <br>
* Windows <br>

## Model Version(s):
v1.0  <br>

## Training, Testing, and Evaluation Datasets:

**Data Collection Method by Dataset:** <br>
* Synthetic <br>
* Hybrid: derived, open-source <br>

**Labeling Method by Dataset:** <br>
* Synthetic <br>

## Evaluation Benchmarks:
Instruction Data Guard is evaluated based on two overarching criteria: <br>
* Success on identifying LLM poisoning attacks, after the model was trained on examples of the attacks. <br>
* Success on identifying LLM poisoning attacks, but without training on examples of those attacks, at all. <br>

Success is defined as having an acceptable catch rate (recall scores for each attack) over a high specificity score (ex. 95%). Acceptable catch rates need to be high enough to identify at least several poisoned records in the attack. <br>

## Inference:
**Engine:** NeMo Curator and Aegis <br>
**Test Hardware:** <br>
* A100 80GB GPU <br>

## How to Use in NeMo Curator:
The inference code is available on [NeMo Curator's GitHub repository](https://github.com/NVIDIA-NeMo/Curator). <br>
Check out [this example notebook](https://github.com/NVIDIA-NeMo/Curator/blob/main/tutorials/text/distributed-data-classification/instruction-data-guard-classification.ipynb) to get started.

## How to Use in Transformers:
To use this AEGIS classifiers, you must get access to Llama Guard on Hugging Face here: https://huggingface.co/meta-llama/LlamaGuard-7b. Afterwards, you should set up a [user access token](https://huggingface.co/docs/hub/en/security-tokens) and pass that token into the constructor of this classifier.

```python
import torch
import torch.nn.functional as F
from huggingface_hub import PyTorchModelHubMixin
from peft import PeftModel
from torch.nn import Dropout, Linear
from transformers import AutoModelForCausalLM, AutoTokenizer

# Initialize model embedded with AEGIS
pretrained_model_name_or_path = "meta-llama/LlamaGuard-7b"
dtype = torch.bfloat16
token = "hf_1234"  # Replace with your user access token
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
base_model = AutoModelForCausalLM.from_pretrained(pretrained_model_name_or_path, torch_dtype=dtype, token=token).to(device)
peft_model_name_or_path = "nvidia/Aegis-AI-Content-Safety-LlamaGuard-Defensive-1.0"
model = PeftModel.from_pretrained(base_model, peft_model_name_or_path)

# Initialize tokenizer
tokenizer = AutoTokenizer.from_pretrained(
    pretrained_model_name_or_path=pretrained_model_name_or_path,
    padding_side="left"
)
tokenizer.pad_token = tokenizer.unk_token

class InstructionDataGuardNet(torch.nn.Module, PyTorchModelHubMixin):
    def __init__(self, input_dim=4096, dropout=0.7):
        super().__init__()
        self.input_dim = input_dim
        self.dropout = Dropout(dropout)
        self.sigmoid = torch.nn.Sigmoid()
        self.input_layer = Linear(input_dim, input_dim)

        self.hidden_layer_0 = Linear(input_dim, 2000)
        self.hidden_layer_1 = Linear(2000, 500)
        self.hidden_layer_2 = Linear(500, 1)

    def forward(self, x):
        x = torch.nn.functional.normalize(x, dim=-1)
        x = self.dropout(x)
        x = F.relu(self.input_layer(x))
        x = self.dropout(x)
        x = F.relu(self.hidden_layer_0(x))
        x = self.dropout(x)
        x = F.relu(self.hidden_layer_1(x))
        x = self.dropout(x)
        x = self.hidden_layer_2(x)
        x = self.sigmoid(x)
        return x

# Load Instruction Data Guard classifier
instruction_data_guard = InstructionDataGuardNet.from_pretrained("nvidia/instruction-data-guard")
instruction_data_guard = instruction_data_guard.to(device)
instruction_data_guard = instruction_data_guard.eval()

# Function to compute results
def get_instruction_data_guard_results(
    prompts,
    tokenizer,
    model,
    instruction_data_guard,
    device="cuda",
):
    input_ids = tokenizer(prompts, padding=True, return_tensors="pt").to(device)
    outputs = model.generate(
        **input_ids,
        output_hidden_states=True,
        return_dict_in_generate=True,
        max_new_tokens=1,
        pad_token_id=0,
    )
    input_tensor = outputs.hidden_states[0][32][:, -1,:].to(torch.float)
    return instruction_data_guard(input_tensor).flatten().detach().cpu().numpy()

# Prepare sample input
instruction = "Find a route between San Diego and Phoenix which passes through Nevada"
input_ = ""
response = "Drive to Las Vegas with highway 15 and from there drive to Phoenix with highway 93"
benign_sample =  f"Instruction: {instruction}. Input: {input_}. Response: {response}."
text_samples = [benign_sample]
poisoning_scores = get_instruction_data_guard_results(
    text_samples, tokenizer, model, instruction_data_guard
)
print(poisoning_scores)
# [0.01149639]
```

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.  

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).
