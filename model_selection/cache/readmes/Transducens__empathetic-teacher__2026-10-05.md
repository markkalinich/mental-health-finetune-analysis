---
license: apache-2.0
language:
- en
base_model:
- meta-llama/Meta-Llama-3.1-8B
---

# Empathetic teacher model

## Overview

This is a LLM fine-tuned with real-life, ideally-empathetic teacher-student conversations. 
This model processes the recent conversation history and provides guidance on how a teacher might respond to the student's utterance.

To fine-tune an open-weighted LLM to act as this generic teacher, we have used the following datasets: 
the Teacher-Student Chatroom Corpus, TSCCv2 [Caines et al., 2022](https://aclanthology.org/2022.nlp4call-1.3), 
CIMA [Stasaski et al., 2020](https://aclanthology.org/2020.bea-1.5), 
the Multicultural Classroom Discourse Dataset [Rapanta et al., 2021](https://www.sciencedirect.com/science/article/pii/S2352340921007940), 
MathDial [Macina et al., 2023](https://aclanthology.org/2023.findings-emnlp.372), and 
Conversational Uptake [Demszky et al., 2021].

We are evaluating Llama-3.1-8B for this task. 
Instead of using programmable fine-tuning libraries such as Axolotl ([link](https://github.com/OpenAccess-AI-Collective/axolotl)) 
or Huggingface TRL ([link](https://github.com/huggingface/trl)), 
we have employed the more general command-line LLaMA-Factory ([link](https://github.com/hiyouga/LLaMA-Factory)) toolkit 
that facilitates the fine-tuning of various well-known LLMs on custom data. 
Parameter-efficient fine-tuning is achieved via the QLoRA method [Dettmers et al., 2023](https://proceedings.neurips.cc/paper_files/paper/2023/file/1feb87871436031bdc0f2beaa62a049b-Paper-Conference.pdf).


Number of conversation turns and words in the original datasets and after splitting long conversations:

| **Dataset**      | **Turns (Original)** | **Words (Original)** | **Turns (Split turns)** | **Words (Split turns)** |
|------------------|:--------------------:|:--------------------:|:-----------------------:|:-----------------------:|
| TSCC v2          |        570           |        788k          |         1074            |         786k            |
| CIMA             |       1135           |         44k          |         1135            |          38k            |
| MathDial         |       2861           |        923k          |         2876            |         879k            |
| Multicultural    |         5            |        614k          |          643            |         614k            |
| Uptake           |        774           |         35k          |          775            |          34k            |
| **Total**        |     **5345**         |     **2404k**        |      **6503**           |      **2351k**          |


## Usage Guide

This project was executed on an Ubuntu 22.04.3 system running Linux kernel 6.8.0-40-generic.

### Installation

To get started, you first need to set up the environment using the **LLaMA-Factory** project. Please refer to the official [LLaMA-Factory repository](https://github.com/hiyouga/LLaMA-Factory) for more details.

You can install the project by running the following commands:

```bash
git clone --depth 1 https://github.com/hiyouga/LLaMA-Factory.git
cd LLaMA-Factory
pip install -e ".[torch,metrics]"
```

### Execution
In the DeMINT project, the model was utilized to create a REST API. Below is an example of how to configure and run it.

**Setting Server Configuration**

To specify the port and server address, use the following environment variables:

To set the port and the address of the server:
```bash
# Default 8000
export KIND_TEACHER_PORT=8000
# Default localhost
export KIND_TEACHER_HOST="localhost"
```

**Running the Program**

Once the environment is configured, you can execute the program by running the following command:
```bash
llamafactory-cli api run_api_inference_1.yaml
```

**API Call from Client**
```python
address="localhost"
port=8000
type_message = {"GET": "/models", "POST": "/chat/completions"}
url = f'http://{address}:{port}/v1{type_message["POST"]}'

headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}

messages = [
  {
    "role": "system",    # "user", "assistant" or "system"
    "content": "You are a kind teacher that help students with their problems.",
  },
  {
    "role": "user",    # "user", "assistant" or "system"
    "content": "Hello teacher",
    "tool_calls": []
  },
  {
    "role": "assistant",    # "user", "assistant" or "system"
    "content": "Hello student!",
  },
  {
    "role": "user",    # "user", "assistant" or "system"
    "content": "Can you help me to understand the past perfect of english?",
    "tool_calls": []
  },
]

data = {
    "model": "Transducens/kind_teacher",
    "messages": messages,   # messages must be formatted in the required format
    "tools": [],
    "do_sample": True,
    "temperature": 1.0,
    "top_p": 0.7,
    "n": 1,                 # number of completions (responses) to generate
    "max_tokens": 150,
    "stream": False
}

response = requests.post(url, headers=headers, data=json.dumps(data))
```