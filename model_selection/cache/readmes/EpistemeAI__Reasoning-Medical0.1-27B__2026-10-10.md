---
base_model: unsloth/Qwen3.5-27B
tags:
- text-generation-inference
- transformers
- unsloth
- qwen3_5
license: cc
language:
- en
datasets:
- EpistemeAI/medical-reasoning-mix-100k
---

# Introduction
This EpistemeAI/Reasoning-Medical0.1-27B is designed for advanced medical reasoning in professional medicine, medical genetics, college biology/medicine, and clinical knowledge.
The model was fine-tuned on a large-scale dataset of 100000 records, specifically curated by blending various public medical reasoning datasets, incorporating Chain-of-Thought reasoning to improve step-by-step medical related questions. Training was performed using the GRPO trainer with the Unsloth optimization method for efficient fine-tuning.
The primary goal is to provide a comprehensive and diverse dataset for training language models in medical question-answering and reasoning tasks.
Due to very high performance in medical reasoning, please ask for permission to download the model.

> **Safety Notice:** This model is for benign medical and scientific reasoning only. It must not be used for biological or chemical weapon development, pathogen enhancement, toxin production, hazardous synthesis, or any activity that enables harm. All biomedical, biological, chemical, or laboratory-related outputs require expert review and must comply with applicable legal, ethical, biosafety, biosecurity, and chemical safety standards.
> 


## Model Overview

- Type: Causal Language Model with Vision Encoder
- Training Stage: Pre-training & Post-training
- Language Model
    - Number of Parameters: 27B
    - Hidden Dimension: 5120
    - Token Embedding: 248320 (Padded)
    - Number of Layers: 64
    - Hidden Layout: 16 × (3 × (Gated DeltaNet → FFN) → 1 × (Gated Attention → FFN))
    - Gated DeltaNet:
        - Number of Linear Attention Heads: 48 for V and 16 for QK
        - Head Dimension: 128
    - Gated Attention:
        - Number of Attention Heads: 24 for Q and 4 for KV
        - Head Dimension: 256
        - Rotary Position Embedding Dimension: 64
    - Feed Forward Network:
        - Intermediate Dimension: 17408
    - LM Output: 248320 (Padded)
    - MTP: trained with multi-steps  
- Context Length: 262,144 natively and extensible up to 1,010,000 tokens.

## Commercial Access

Reasoning-Medical0.1-27B is available for:

- Medical education applications
- Research copilots
- Biotech/pharma literature analysis
- Private medical reasoning deployments
- Model benchmarking and safety evaluation

For API access, private deployment, or commercial licensing, contact:

episteme.ai@proton.me

# Benchmark

| Task              | Version | Filter         | n-shot | Metric      | Direction | Reasoning Medical0.1 27B | Reasoning Medical 27B | MedGemma 1 27B |
|-------------------|--------:|----------------|-------:|-------------|:---------:|-------------------------:|----------------------:|----------------:|
| MMLU-Pro Biology  | 3.1     | custom-extract | 2      | exact_match | ↑         | 0.93                     | 0.85                  | —               |
| MMLU-ProX Biology | 0       | custom-extract | 2      | exact_match | ↑         | 0.968                    | 0.80                  | —               |
| MedQA             | YAML    | none           | 2      | acc         | ↑         | 0.969                    | 0.93                  | 0.853           |


| Task              | Version | Filter         | n-shot | Metric      | Direction | Reasoning Medical0.1 27B | Opus 4.8 | GPT 5.5 | Kimi-K2.6 |
|-------------------|--------:|----------------|-------:|-------------|:---------:|-------------------------:|---------:|--------:|----------:|
| HealthBench Pro   | none    | none           | none   | acc         | ↑         | 0.54                     | 0.512    |  0.518   | 0.503     |

<p align="center">
  <img src="healthbench_pro_model_comparison.png" alt="HealthBench Professional model accuracy comparison" width="850">
</p>

### Installation
To get started, install the necessary dependencies to setup your environment:
```
!pip install --upgrade "transformers>=5.2.0"
```


### Using Reasoning Medical 27B via the Chat Completions API

The chat completions API is accessible via standard HTTP requests or OpenAI SDKs.
Here, we show examples using the OpenAI Python SDK.

Before starting, make sure it is installed and the API key and the API base URL is configured, e.g.:
```shell
pip install -U openai

# Set the following accordingly
export OPENAI_BASE_URL="http://localhost:8000/v1"
export OPENAI_API_KEY="EMPTY"
```

> [!Tip]
> We recommend using the following set of sampling parameters for generation
> - Thinking mode for general tasks: `temperature=1.0, top_p=0.95, top_k=20, min_p=0.0, presence_penalty=0.0, repetition_penalty=1.0`
> - Thinking mode for precise coding tasks (e.g. WebDev): `temperature=0.6, top_p=0.95, top_k=20, min_p=0.0, presence_penalty=0.0, repetition_penalty=1.0`
> - Instruct (or non-thinking) mode: `temperature=0.7, top_p=0.80, top_k=20, min_p=0.0, presence_penalty=1.5, repetition_penalty=1.0`
>
> Please note that the support for sampling parameters varies according to inference frameworks.

> [!Important]
> Our models operate in thinking mode by default, generating thinking content signified by `<think>\n...</think>\n\n` before producing the final responses.
> To disable thinking content and obtain direct response, refer to the examples [here](#instruct-or-non-thinking-mode).



#### Text-Only Input

```python
from openai import OpenAI
# Configured by environment variables
client = OpenAI()

messages = [
    {"role": "user", "content": "Chronic urethral obstruction due to benign prismatic hyperplasia can lead to the following change in kidney parenchyma"},
]

chat_response = client.chat.completions.create(
    model="EpistemeAI/Reasoning-Medical0.1-27B",
    messages=messages,
    max_tokens=81920,
    temperature=1.0,
    top_p=0.95,
    presence_penalty=0.0,
    extra_body={
        "top_k": 20,
    }, 
)
print("Chat response:", chat_response)
```


#### Image Input

```python
from openai import OpenAI
# Configured by environment variables
client = OpenAI()

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image_url",
                "image_url": {
                    "url": "https://qianwen-res.oss-accelerate.aliyuncs.com/Qwen3.5/demo/CI_Demo/mathv-1327.jpg"
                }
            },
            {
                "type": "text",
                "text": "The centres of the four illustrated circles are in the corners of the square. The two big circles touch each other and also the two little circles. With which factor do you have to multiply the radii of the little circles to obtain the radius of the big circles?\nChoices:\n(A) $\\frac{2}{9}$\n(B) $\\sqrt{5}$\n(C) $0.8 \\cdot \\pi$\n(D) 2.5\n(E) $1+\\sqrt{2}$"
            }
        ]
    }
]

chat_response = client.chat.completions.create(
    model="EpistemeAI/Reasoning-Medical0.1-27B",
    messages=messages,
    max_tokens=81920,
    temperature=1.0,
    top_p=0.95,
    presence_penalty=0.0,
    extra_body={
        "top_k": 20,
    }, 
)
print("Chat response:", chat_response)
```

#### Video Input

```python
from openai import OpenAI
# Configured by environment variables
client = OpenAI()

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "video_url",
                "video_url": {
                    "url": "https://qianwen-res.oss-accelerate.aliyuncs.com/Qwen3.5/demo/video/N1cdUjctpG8.mp4"
                }
            },
            {
                "type": "text",
                "text": "How many porcelain jars were discovered in the niches located in the primary chamber of the tomb?"
            }
        ]
    }
]

# When vLLM is launched with `--media-io-kwargs '{"video": {"num_frames": -1}}'`,
# video frame sampling can be configured via `extra_body` (e.g., by setting `fps`).
# This feature is currently supported only in vLLM.
#
# By default, `fps=2` and `do_sample_frames=True`.
# With `do_sample_frames=True`, you can customize the `fps` value to set your desired video sampling rate.
chat_response = client.chat.completions.create(
    model="EpistemeAI/Reasoning-Medical0.1-27B",
    messages=messages,
    max_tokens=81920,
    temperature=1.0,
    top_p=0.95,
    presence_penalty=0.0,
    extra_body={
        "top_k": 20,
        "mm_processor_kwargs": {"fps": 2, "do_sample_frames": True},
    }, 
)

print("Chat response:", chat_response)
```


#### Instruct (or Non-Thinking) Mode

> [!Important]
> Our model does not officially support the soft switch of Reasoning Medical 27B, i.e., `/think` and `/nothink`.

Our model will think by default before response.
You can obtain direct response from the model without thinking by configuring the API parameters. 
For example,
```python
from openai import OpenAI
# Configured by environment variables
client = OpenAI()

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image_url",
                "image_url": {
                    "url": "https://qianwen-res.oss-accelerate.aliyuncs.com/Qwen3.6/demo/RealWorld/RealWorld-04.png"
                }
            },
            {
                "type": "text",
                "text": "Where is this?"
            }
        ]
    }
]

chat_response = client.chat.completions.create(
    model="EpistemeAI/Reasoning-Medical0.1-27B",
    messages=messages,
    max_tokens=32768,
    temperature=0.7,
    top_p=0.8,
    presence_penalty=1.5,
    extra_body={
        "top_k": 20,
        "chat_template_kwargs": {"enable_thinking": False},
    }, 
)
print("Chat response:", chat_response)
```

> [!Note]
> If you are using APIs from Alibaba Cloud Model Studio, in addition to changing `model`, please use `"enable_thinking": False` instead of `"chat_template_kwargs": {"enable_thinking": False}`.

#### Preserve Thinking

By default, only the thinking blocks generated in handling the latest user message is retained, resulting in a pattern commonly as interleaved thinking. 
Reasoning Medical 27B has been additionally trained to preserve and leverage thinking traces from historical messages.
You can enable this behavior by setting the `preserve_thinking` option:
```python
from openai import OpenAI
# Configured by environment variables
client = OpenAI()

messages = [...]

chat_response = client.chat.completions.create(
    model="EpistemeAI/Reasoning-Medical0.1-27B",
    messages=messages,
    max_tokens=32768,
    temperature=0.6,
    top_p=0.95,
    presence_penalty=0.0,
    extra_body={
        "top_k": 20,
        "chat_template_kwargs": {"preserve_thinking": True},
    }, 
)
print("Chat response:", chat_response)
```

> [!Note]
> If you are using APIs from Alibaba Cloud Model Studio, in addition to changing `model`, please use `"preserve_thinking": True` instead of `"chat_template_kwargs": {"preserve_thinking": False}`.


This capability is particularly beneficial for agent scenarios, where maintaining full reasoning context can enhance decision consistency and, in many cases, reduce overall token consumption by minimizing redundant reasoning. Additionally, it can improve KV cache utilization, optimizing inference efficiency in both thinking and non-thinking modes.


## Agentic Usage

Our model excels in tool calling capabilities.

### Qwen-Agent

We recommend using [Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) to quickly build Agent applications with Qwen3.6. 

To define the available tools, you can use the MCP configuration file, use the integrated tool of Qwen-Agent, or integrate other tools by yourself.
```python
import os
from qwen_agent.agents import Assistant

# Define LLM
# Using Alibaba Cloud Model Studio
llm_cfg = {
    # Use the OpenAI-compatible model service provided by DashScope:
    'model': 'EpistemeAI/Reasoning-Medical0.1-27B',
    'model_type': 'qwenvl_oai',
    'model_server': 'https://dashscope.aliyuncs.com/compatible-mode/v1',
    'api_key': os.getenv('DASHSCOPE_API_KEY'),

    'generate_cfg': {
        'use_raw_api': True,
        # When using Dash Scope OAI API, pass the parameter of whether to enable thinking mode in this way
        'extra_body': {
            'enable_thinking': True,
            'preserve_thinking': True,
        },
    },
}

# Using OpenAI-compatible API endpoint.
# functionality of the deployment frameworks and let Qwen-Agent automate the related operations.
#
# llm_cfg = {
#     # Use your own model service compatible with OpenAI API by vLLM/SGLang:
#     'model': 'EpistemeAI/Reasoning-Medical0.1-27B',
#     'model_type': 'qwenvl_oai',
#     'model_server': 'http://localhost:8000/v1',  # api_base
#     'api_key': 'EMPTY',
#
#     'generate_cfg': {
#         'use_raw_api': True,
#         # When using vLLM/SGLang OAI API, pass the parameter of whether to enable thinking mode in this way
#         'extra_body': {
#             'chat_template_kwargs': {'enable_thinking': True, 'preserve_thinking': True}
#         },
#     },
# }

# Define Tools
tools = [
    {'mcpServers': {  # You can specify the MCP configuration file
            "filesystem": {
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/xxxx/Desktop"]
            }
        }
    }
]

# Define Agent
bot = Assistant(llm=llm_cfg, function_list=tools)

# Streaming generation
messages = [{'role': 'user', 'content': 'Help me organize my desktop.'}]
for responses in bot.run(messages=messages):
    pass
print(responses)

# Streaming generation
messages = [{'role': 'user', 'content': 'Develop a dog website and save it on the desktop'}]
for responses in bot.run(messages=messages):
    pass
print(responses)
```


## Processing Ultra-Long Texts

Reasoning Medical 27B natively supports context lengths of up to 262,144 tokens. 
For long-horizon tasks where the total length (including both input and output) exceeds this limit, we recommend using RoPE scaling techniques to handle long texts effectively., e.g., YaRN.

YaRN is currently supported by several inference frameworks, e.g., `transformers`, `vllm`, `ktransformers` and `sglang`. 
In general, there are two approaches to enabling YaRN for supported frameworks:

- Modifying the model configuration file:
  In the `config.json` file, change the `rope_parameters` fields in `text_config` to:
    ```json
    {
        "mrope_interleaved": true,
        "mrope_section": [
            11,
            11,
            10
        ],
        "rope_type": "yarn",
        "rope_theta": 10000000,
        "partial_rotary_factor": 0.25,
        "factor": 4.0,
        "original_max_position_embeddings": 262144,
    }
    ```

- Passing command line arguments:

  For `vllm`, you can use
    ```shell
    VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 vllm serve ... --hf-overrides '{"text_config": {"rope_parameters": {"mrope_interleaved": true, "mrope_section": [11, 11, 10], "rope_type": "yarn", "rope_theta": 10000000, "partial_rotary_factor": 0.25, "factor": 4.0, "original_max_position_embeddings": 262144}}}' --max-model-len 1010000  
    ```

  For `sglang` and `ktransformers`, you can use
    ```shell
    SGLANG_ALLOW_OVERWRITE_LONGER_CONTEXT_LEN=1 python -m sglang.launch_server ... --json-model-override-args '{"text_config": {"rope_parameters": {"mrope_interleaved": true, "mrope_section": [11, 11, 10], "rope_type": "yarn", "rope_theta": 10000000, "partial_rotary_factor": 0.25, "factor": 4.0, "original_max_position_embeddings": 262144}}}' --context-length 1010000
    ```

> [!NOTE]
> All the notable open-source frameworks implement static YaRN, which means the scaling factor remains constant regardless of input length, **potentially impacting performance on shorter texts.**
> We advise modifying the `rope_parameters` configuration only when processing long contexts is required. 
> It is also recommended to modify the `factor` as needed. For example, if the typical context length for your application is 524,288 tokens, it would be better to set `factor` as 2.0. 

## Best Practices

To achieve optimal performance, we recommend the following settings:

1. **Sampling Parameters**:  
   - We suggest using the following sets of sampling parameters depending on the mode and task type:  
     - **Thinking mode for general tasks**:  
       `temperature=1.0`, `top_p=0.95`, `top_k=20`, `min_p=0.0`, `presence_penalty=0.0`, `repetition_penalty=1.0`  
     - **Thinking mode for precise coding tasks (e.g., WebDev)**:  
       `temperature=0.6`, `top_p=0.95`, `top_k=20`, `min_p=0.0`, `presence_penalty=0.0`, `repetition_penalty=1.0`  
     - **Instruct (or non-thinking) mode**:  
       `temperature=0.7`, `top_p=0.80`, `top_k=20`, `min_p=0.0`, `presence_penalty=1.5`, `repetition_penalty=1.0`  
   - For supported frameworks, you can adjust the `presence_penalty` parameter between 0 and 2 to reduce endless repetitions. However, using a higher value may occasionally result in language mixing and a slight decrease in model performance.

2. **Adequate Output Length**: We recommend using an output length of 32,768 tokens for most queries. For benchmarking on highly complex problems, such as those found in math and programming competitions, we suggest setting the max output length to 81,920 tokens. This provides the model with sufficient space to generate detailed and comprehensive responses, thereby enhancing its overall performance.

3. **Standardize Output Format**: We recommend using prompts to standardize model outputs when benchmarking.
   - **Math Problems**: Include "Please reason step by step, and put your final answer within \boxed{}." in the prompt.
   - **Multiple-Choice Questions**: Add the following JSON structure to the prompt to standardize responses: "Please show your choice in the `answer` field with only the choice letter, e.g., `"answer": "C"`."

4. **Long Video Understanding**: To optimize inference efficiency for plain text and images, the `size` parameter in the released `video_preprocessor_config.json` is conservatively configured. It is recommended to set the `longest_edge` parameter in the video_preprocessor_config file to 469,762,048 (corresponding to 224k video tokens) to enable higher frame-rate sampling for hour-scale videos and thereby achieve superior performance. For example,
    ```json
    {"longest_edge": 469762048, "shortest_edge": 4096}
    ```

    Alternatively, override the default values via engine startup parameters. For implementation details, refer to: [vLLM](https://github.com/vllm-project/vllm/pull/34330) / [SGLang](https://github.com/sgl-project/sglang/pull/18467).

# Limitation
Reasoning-Medical0.1-27B is intended for research and informational purposes only. Its outputs should not be used to directly guide clinical diagnosis, patient management, treatment decisions, or any other direct clinical practice applications.
Benchmark results are provided to illustrate the model’s baseline performance on relevant evaluation tasks; however, they do not guarantee accuracy, reliability, or suitability for clinical use. Even in image and text domains that are substantially represented in the training data, the model may generate incomplete, inaccurate, or misleading outputs.
All outputs generated by Reasoning-Medical-27B should be treated as preliminary and must undergo independent verification, clinical correlation, and further validation through established research, development, and regulatory review processes before any clinical application is considered.

## Biological and Chemical Safety Warning

This model is intended for **benign medical, biomedical, and scientific reasoning support only**. It must not be used to design, optimize, synthesize, acquire, modify, weaponize, or deploy biological agents, toxins, pathogens, chemical agents, hazardous compounds, or related delivery systems.

The model is **not intended to provide actionable guidance** for activities involving:

- Biological weapon development or misuse
- Pathogen engineering, enhancement, or evasion
- Toxin production, purification, or delivery
- Chemical weapon synthesis or optimization
- Circumventing biosafety, biosecurity, chemical safety, or legal controls
- Experimental protocols that increase transmissibility, virulence, toxicity, persistence, or environmental spread
- Procurement, concentration, dosage, dispersal, or deployment of hazardous biological or chemical materials

Outputs related to biology, chemistry, medicine, toxicology, infectious disease, or laboratory work may be incomplete, inaccurate, unsafe, or inappropriate for real-world use. Any such outputs must be reviewed by qualified professionals and handled only within approved legal, institutional, biosafety, biosecurity, and chemical safety frameworks.

This model should be used only for **safe, ethical, and lawful purposes**, such as medical education, literature review, clinical reasoning research, public health analysis, defensive biosecurity, and non-operational safety discussions. Users are responsible for ensuring that all usage complies with applicable laws, regulations, institutional review requirements, and safety standards.

# Legal Notice and Disclaimer

This model is independently developed and is not affiliated with, endorsed by, sponsored by, authorized by, or otherwise associated with Qwen, Alibaba Group, or any of their respective affiliates, subsidiaries, licensors, owners, or representatives. Any reference to Qwen is made solely for descriptive or comparative purposes, where applicable.

To the best of the developer’s knowledge, no fine-tuning, training, evaluation, optimization, or model-development process for this model involved distillation from OpenAI or Anthropic models, systems, APIs, outputs, synthetic responses, logits, hidden states, labels, or any other derived training signals. No OpenAI or Anthropic model outputs were knowingly used as training data for this fine-tuning process.

All trademarks, service marks, trade names, product names, and company names mentioned are the property of their respective owners. Use of such names does not imply any affiliation, endorsement, sponsorship, or approval.


# Model Card Authors 
- Thomas Yiu
 
# Model Card Contact
- Email: episteme.ai@proton.me

# Uploaded finetuned  model

- **Developed by:** EpistemeAI
- **License:** cc
- **Finetuned from model :** unsloth/Qwen3.5-27B

This qwen3_5 model was trained 2x faster with [Unsloth](https://github.com/unslothai/unsloth) and Huggingface's TRL library.

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)