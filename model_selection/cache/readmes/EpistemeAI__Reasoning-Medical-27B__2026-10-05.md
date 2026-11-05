---
base_model: unsloth/Qwen3.6-27B
tags:
- text-generation-inference
- transformers
- unsloth
- qwen3_5
license: apache-2.0
language:
- en
---
![X-ray response example](X-ray-example.png)

# Introduction
This EpistemeAI/Reasoning-Medical-27B is designed for universal(all countries) advanced medical reasoning in professional medicine, medical genetics, college biology/medicine, and clinical knowledge.
The model was fine-tuned on a large-scale dataset of 370,000 high-quality question-and-answer examples, incorporating Chain-of-Thought reasoning to improve step-by-step medical related questions. Training was performed using the GRPO trainer with the Unsloth optimization method for efficient fine-tuning.
This is open source version of the Reasoning Medical 27B.

<p align="center">
  <a href="https://huggingface.co/EpistemeAI/Reasoning-Medical-27B">BF16</a> |
  <a href="https://huggingface.co/switzerchees/Reasoning-Medical-27B-NVFP4">NVFP4</a> |
  <a href="https://huggingface.co/spaces/EpistemeAI/reasoning-medical-27b">Playground</a> |
  <a href="https://github.com/tomtyiu/EpistemeAI-series-Cookbook-SDK">EpistemeAI Cookbook</a> |
</p>


> [!Important]
> **The model do not have any export controls and restrictions.** 

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


### Interpretation

`Reasoning-Medical-27B` reports **93.00% MedQA accuracy** in the model card's 2-shot setup. The same table reports **84.40%** for `Qwen 3.6 27B`, an absolute difference of **8.60 percentage points**.

The broader comparison above is **not a standardized leaderboard**. It combines published and model-card results that use materially different protocols, including:

- Few-shot and zero-shot prompting
- Web-search augmentation
- Benchmark-specific fine-tuning
- Self-consistency chain-of-thought
- Best-of-N test-time scaling
- Different MedQA variants and answer-option formats

For a defensible model comparison, rerun all models on the same dataset revision, prompt template, shot count, decoding settings, answer extractor, and random seed.

## Evaluation limitations

The reported benchmark score should not be interpreted as clinical validation.

Important limitations include:

- MedQA measures exam-style multiple-choice performance, not real-world patient outcomes.
- Public benchmark contamination may inflate apparent generalization.
- Accuracy can change substantially with prompt templates and decoding settings.
- The model may generate confident but incorrect explanations.
- Performance may vary across specialties, countries, languages, demographics, and care settings.
- The public model card does not fully enumerate the approximately 370,000-example training mixture.
- Independent replication of the reported 0.930 MedQA score is recommended.


## Installation
Install the required dependencies:
```bash
pip install --upgrade "transformers>=5.2.0"
```
> In Google Colab or Jupyter Notebook, prefix the command with `!`:
>
> ```bash
> !pip install --upgrade "transformers>=5.2.0"
> ```
Local Deployment
You can serve EpistemeAI Reasoning Medical 27B locally using either SGLang or vLLM.
SGLang
```bash
pip install --upgrade sglang

python3 -m sglang.launch_server \
  --model-path "EpistemeAI/Reasoning-Medical-27B" \
  --host 0.0.0.0 \
  --port 30000
```
After the server starts, the API will be available at:
```text
http://localhost:30000
```
vLLM
```bash
pip install --upgrade vllm

vllm serve "EpistemeAI/Reasoning-Medical-27B"
```
By default, the OpenAI-compatible API will be available at:
```text
http://localhost:8000/v1
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
    model="EpistemeAI/Reasoning-Medical-27B",
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
    model="EpistemeAI/Reasoning-Medical-27B",
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
    model="EpistemeAI/Reasoning-Medical-27B",
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
    model="EpistemeAI/Reasoning-Medical-27B",
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

#### [EpistemeAI Reasoning-Medical-27B demo X-ray Example](X-ray-example.md)



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
    model="EpistemeAI/Reasoning-Medical-27B",
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
    'model': 'EpistemeAI/Reasoning-Medical-27B',
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
#     'model': 'EpistemeAI/Reasoning-Medical-27B',
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

## Benchmark results reported by the model card

## HealthBench Professional
![Reported HealthBench Professional benchmark comparison](healthbench_professional_benchmark_v2.svg)


| Rank | Model or System | Score | Source |
|---:|---|---:|---|
| 1 | Reasoning Medical 27B | **0.560** | EpistemeAI evaluation |
| 2 | GPT 5.5 | 0.518 | External evaluation |
| 3 | Opus 4.8 | 0.512 | External evaluation |
| 4| Kimi-K2.6 | 0.503 | External evaluation |
| 5 | GPT-5.4 | 0.481 | Official HealthBench Professional paper |
| 6 | Claude Opus 4.7 | 0.470 | Official HealthBench Professional paper |
| 7 | GPT-5 | 0.462 | Official HealthBench Professional paper |
| 8 | GPT-5.2 | 0.459 | Official HealthBench Professional paper |
| 9 | Gemini 3.1 Pro | 0.438 | Official HealthBench Professional paper |
| 10 | Physician-written baseline | 0.437 | Official HealthBench Professional paper |
| 11 | Grok 4.20 | 0.361 | Official HealthBench Professional paper |



## Broader reported MedQA comparison

![Reported MedQA benchmark comparison](medqa_benchmark_comparison.png)

| Rank | Model | Parameters | MedQA accuracy | Reported protocol |
|---:|---|---:|---:|---|
| 1 | [EpistemeAI/Reasoning-Medical-27B](https://huggingface.co/EpistemeAI/Reasoning-Medical-27B) | 27B | **93.00%** | 2-shot; accuracy reported on the model card |
| 2 | [Med-Gemini](https://arxiv.org/abs/2404.18416) | Not disclosed | **91.10%** | Uncertainty-guided web-search strategy |
| 3 | [MedGemma 27B](https://huggingface.co/google/medgemma-27b-text-it) | 27B | **89.80%** | Best-of-5 test-time scaling |
| 4 | [Med-PaLM 2](https://arxiv.org/abs/2305.09617) | Not disclosed | **86.50%** | Best reported MedQA-specific instruction-tuned variant |
| 5 | [Qwen 3.6 27B](https://huggingface.co/EpistemeAI/Reasoning-Medical-27B) | 27B | **84.40%** | 2-shot; reported in the EpistemeAI model-card comparison |
| 6 | [Med42-v2-70B](https://huggingface.co/m42-health/Llama3-Med42-70B) | 70B | **79.10%** | Zero-shot; EleutherAI evaluation harness |
| 7 | [OpenBioLLM-70B](https://huggingface.co/m42-health/Llama3-Med42-70B) | 70B | **76.90%** | Zero-shot re-evaluation reported by the Med42 team |
| 8 | [MEDITRON-70B](https://huggingface.co/epfl-llm/meditron-70b) | 70B | **70.20%** | MedQA four-option; task fine-tuning and self-consistency CoT |
| 9 | [Med-PaLM](https://arxiv.org/abs/2212.13138) | Not disclosed | **67.20%** | Instruction prompt tuning with chain-of-thought and self-consistency |
| 10 | [MedGemma 4B](https://huggingface.co/google/medgemma-27b-text-it) | 4B | **64.40%** | Reported MedQA four-option evaluation |
| 11 | [Med42-v2-8B](https://huggingface.co/m42-health/Llama3-Med42-70B) | 8B | **62.84%** | Zero-shot; EleutherAI evaluation harness |
| 12 | [ClinicalCamel-70B](https://huggingface.co/m42-health/Llama3-Med42-70B) | 70B | **53.40%** | Zero-shot re-evaluation reported by the Med42 team |


# Legal Notice and Disclaimer

This model is independently developed and is not affiliated with, endorsed by, sponsored by, authorized by, or otherwise associated with Qwen, Alibaba Group, or any of their respective affiliates, subsidiaries, licensors, owners, or representatives. Any reference to Qwen is made solely for descriptive or comparative purposes, where applicable.

To the best of the developer’s knowledge, no fine-tuning, training, evaluation, optimization, or model-development process for this model involved distillation from OpenAI or Anthropic models, systems, APIs, outputs, synthetic responses, logits, hidden states, labels, or any other derived training signals. No OpenAI or Anthropic model outputs were knowingly used as training data for this fine-tuning process.

All trademarks, service marks, trade names, product names, and company names mentioned are the property of their respective owners. Use of such names does not imply any affiliation, endorsement, sponsorship, or approval.


# Limitation
Reasoning-Medical-27B is intended for research and informational purposes only. Its outputs should not be used to directly guide clinical diagnosis, patient management, treatment decisions, or any other direct clinical practice applications.
Benchmark results are provided to illustrate the model’s baseline performance on relevant evaluation tasks; however, they do not guarantee accuracy, reliability, or suitability for clinical use. Even in image and text domains that are substantially represented in the training data, the model may generate incomplete, inaccurate, or misleading outputs.
All outputs generated by Reasoning-Medical-27B should be treated as preliminary and must undergo independent verification, clinical correlation, and further validation through established research, development, and regulatory review processes before any clinical application is considered.

# Model Card Authors 
- Thomas Yiu
 
# Model Card Contact
- Email: episteme.ai@proton.me

# Uploaded finetuned  model

- **Developed by:** EpistemeAI
- **License:** apache-2.0
- **Created** USA


[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)