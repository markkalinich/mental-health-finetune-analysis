---
license: apache-2.0
library_name: transformers
base_model:
- EssentialAI/rnj-1
---
# Rnj-1

<p align="center">
  <img src="https://raw.githubusercontent.com/Essential-AI/rnj-1-assets/refs/heads/main/assets/Essential%20Logo%20Color_Color_With%20Space.jpg" width=60% alt="EssentialAI">
</p>

<div align="center" style="line-height: 1;">

  <!-- Website -->
  <a href="https://essential.ai">
    <img alt="Homepage"
      style="vertical-align: middle;"
      src="https://img.shields.io/badge/%F0%9F%8C%90%20Website-essential.ai-4b9fe1?color=4b9fe1&logoColor=white"/>
  </a>

  <!-- Blog / Research -->
  <a href="https://www.essential.ai/research/rnj-1">
    <img alt="Research Blog"
      style="vertical-align: middle;"
      src="https://img.shields.io/badge/🧠%20Research-rnj--1-7c5cff?color=7c5cff&logoColor=white"/>
  </a>

  <!-- HuggingFace -->
  <a href="https://huggingface.co/collections/EssentialAI/rnj-1">
    <img alt="Hugging Face"
      style="vertical-align: middle;"
      src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-rnj--1-ffc107?color=ffc107&logoColor=white"/>
  </a>

  <br>

  <!-- Discord -->
  <a href="https://discord.gg/VPEqUNg6tR">
    <img alt="Discord"
      style="vertical-align: middle;"
      src="https://img.shields.io/badge/Discord-Essential%20AI-7289da?logo=discord&logoColor=white&color=7289da"/>
  </a>

  <!-- X / Twitter -->
  <a href="https://x.com/essential_ai">
    <img alt="Twitter Follow"
      style="vertical-align: middle;"
      src="https://img.shields.io/badge/Twitter-essential__ai-white?logo=x&logoColor=white"/>
  </a>

  <!-- Together AI -->
  <a href="https://www.together.ai/models/rnj-1-instruct">
    <img alt="Together AI"
      style="vertical-align: middle;"
      src="https://img.shields.io/badge/⚡%20TogetherAI-rnj--1--instruct-00c2a8?color=00c2a8&logoColor=white"/>
  </a>

  <!-- OpenRouter -->
  <a href="https://openrouter.ai/essentialai/rnj-1-instruct">
    <img alt="OpenRouter"
      style="vertical-align: middle;"
      src="https://img.shields.io/badge/OpenRouter-rnj--1--instruct-1a4b82?logo=openrouter&color=1a4b82&logoColor=white"/>
  </a>

  <br>
</div>

Rnj-1 is a family of 8B parameter open-weight, dense models trained from scratch by Essential AI, optimized for code and STEM with capabilities on par with SOTA open-weight models. These models perform well across a range of programming languages and boast strong agentic capabilities (e.g., inside agentic frameworks like mini-SWE-agent), while also excelling at tool-calling. They additionally exhibit strong capabilities in math and science. Herein, `rnj-1` refers to the base model, while `rnj-1-instruct` refers to the post-trained instruction tuned model.

# Changelog

* Update December 20, 2025:
  - System prompt and temperature recommendations: Resolve premature truncations and mitigate unprompted code outputs.
  - Updates to default chat template.
  - Updated evaluation results.
  - Links to model generations for evals.
  - Instructions for long-context extrapolation.

* Initial version: December 8, 2025

# Capabilities

We evaluate Rnj-1 models against models of comparable size. In addition to accuracy, we also show the FLOPs used in pre-training for each model.

### Benchmark Results

### Base Model `rnj-1`

<p align="center">
    <img src="https://raw.githubusercontent.com/Essential-AI/rnj-1-assets/refs/heads/main/assets/Base_Full_Table.png" width="100%" alt="Base Evals"/>
</p>

### Instruct Model `rnj-1-instruct`

`rnj-1-instruct` is strong at code, math, and STEM tasks. It also performs well within agentic frameworks such as mini-swe-agent and has stellar tool use abilities.

<p align="center">
    <img src="https://raw.githubusercontent.com/Essential-AI/rnj-1-assets/refs/heads/main/assets/Instruct_Full_Table.png" width="100%" alt="Instrcut Evals"/>

<sub><i>We report published numbers when possible, and when unavailable they are internal reproductions.
Pre-training FLOPs were estimated using 6nt, where n is the number of parameters and t is the token budget.
All Evals under the Env bucket were evaluated using mini-swe-agent (bash only) scaffolding.
GPT OSS 20B was evaluated with reasoning_effort=low.
Qwen 3 8B was evaluated with thinking turned off.</i></sub></p>

### Rnj-1 models are designed to be extended

Both `rnj-1` and `rnj-1-instruct` models are being made available for the community to extend and build upon. We deliberately kept post-training limited to allow for further specialization by the community. As an indicator of the untapped potential of the models we report `pass@{1,2,4,8}`  (with T=0.2, n=8 generations) for hard codegen, agentic, and math benchmarks on `rnj-1-instruct`. These illustrate the model’s potential for test-time scaling and for further domain-specialization. The base model is similarly capable of specialization to other domains different from our post-training if needed. 

<p align="center">
    <img src="https://raw.githubusercontent.com/Essential-AI/rnj-1-assets/refs/heads/main/assets/rnj-1-pass-at-k.png" width="80%" alt="Pass at k evals"/>
</p>

Sidenote: Here is a [screen recording](https://vimeo.com/1143712958/c66dda13f3?share=copy&fl=sv&fe=ci) of `rnj-1-instruct` helping us make an early version of this chart.

### Highlights of abilities

- **Code generation:** Both `rnj-1-instruct` and `rnj-1` demonstrate strong code generation abilities as measured on tasks like HumanEval+, MBPP+, BigCodeBench, and LiveCodeBench v6. Both models compete with the strongest open weight models, sometimes outperforming even larger models such as GPT OSS 20B. We measured code comprehension abilities using the task of predicting inputs given outputs and vice-versa, Crux-IO. We find our models outperform comparable baselines. For multi-lingual code generation capabilities across programming languages we measure MultiPL-E on 6 languages (C++, TypeScript, Java, JavaScript, Shell, PHP) and we find performance close to the strongest model.
- **Agentic and Tool Use:** `rnj-1-instruct` dominates the pack on agentic coding, one of our target abilities. SWE-bench performance is indicative of the model’s ability to tackle everyday software engineering tasks. The model is an order of magnitude stronger than comparably sized models on SWE-bench and approaches the capabilities available in much larger models. It scores `20.8%` on SWE-bench Verified in bash-only mode, which is higher than Gemini 2.0 flash and Qwen2.5-Coder 32B Instruct under the same agentic framework ([leaderboard](https://www.swebench.com/bash-only.html)).<br><br>
    There is a surge of interest in developing models’ abilities to write performant code. `rnj-1-instruct` is able to use a profiler to iteratively improve the performance of the code it writes. For instance, on [Enamel](https://github.com/q-rz/enamel/tree/main), which measures abilities to write efficient solutions to algorithmic problems, the model outperforms all other models under the same setting.<br><br>
    Furthermore, `rnj-1-instruct` surpasses comparable models in tool use performance as measured by the Berkeley Functional Calling Leaderboard (BFCL).
- **Code Infilling** : Having specifically been trained on FIM-ed pre-training data, `rnj-1` exhibits strong infilling abilities, which have been further enhanced during post-training. The base model `rnj-1` scores highly on HE-FIM-Python (avg) at 82.49% and `rnj-1-instruct` achieves 86.21%.
- **Mathematical Problem Solving:** `rnj-1-instruct` shows strong mathematical abilities across several levels of difficulty from elementary math (GSM8k), high school and undergraduate math (Minerva-MATH), and competition math (AIME ‘24 and ‘25). On harder subjects, it outcompetes or is on par with the strongest model in the pack.
- **Scientific Reasoning:** `rnj-1-instruct` exhibits long-context reasoning abilities that are needed to solve hard science and technical questions in GPQA-Diamond and SuperGPQA.

### Demos: Rnj-1 models generalize to unseen tasks

We show a few examples of end-to-end capabilities that are usually expected of larger models.

- **Coding assistant:** `rnj-1-instruct` can operate in agentic mode to create a playable game in a single shot inside of Cline: [screen recording](https://vimeo.com/1143853378/8df3376a1a?share=copy&fl=sv&fe=ci).
- **Agentic use:** `rnj-1-instruct` functions seamlessy within the agentic framework of mini-swe-agent. Given a task such as fixing an issue described in a pull request (PR), fixing a security vulnerability, or writing performant code, it is able to reason across its full context across multiple turns to solve the task. These lead to “trajectories” which are pairs of “Assistant” and “User” turns. Here are a few recordings that show the model’s reasoning abilities across these turns: 1) a SWE task of identifying coding convention violation: [screen recording](https://vimeo.com/1143841317/44adfbd044?share=copy&fl=sv&fe=ci), 2) fixing a security vulnerability: [screen recording](https://vimeo.com/1143843598/6fca2fe0bb?share=copy&fl=sv&fe=ci), 3) diagnosing code performance bottlenecks by running a profiler in the environment and iteratively improving the code: [screen recording](https://vimeo.com/1143828123/11e4d22ac7?share=copy&fl=sv&fe=ci).
- **Data analysis in an interactive chat:** `rnj-1-instruct` can work in interactive chat mode to solve a data analysis and visualization task: [screen recording](https://vimeo.com/1143831950/0e7d9c3edc?share=copy&fl=sv&fe=ci).

# Architecture

Rnj-1's architecture is similar to Gemma 3, except that it uses only global attention, and YaRN for long-context extension. 

| Hyperparameter | Value |
|:---:|:---:|
| **Total Parameters** | 8.3B |
| **Number of Layers** | 32 |
| **Model Dimension** | 4096 |
| **MLP Dimension** | 16384 |
| **Number of Attention Heads** | 32 |
| **Number of Key-Value Heads** | 8 |
| **Attention Head Dimension** | 128 |
| **Vocabulary Size** | 128K |
| **Pretrain Context Length** | 8K |
| **Context Length** | 32K |
| **Activation Function** | GeGLU |
| **Tied Embeddings?** | Yes |

### Training Dynamics

`rnj-1` was pre-trained on 8.4T tokens with an 8K context length, after which the model’s context window was extended to **32K** through an additional 380B-token mid-training stage. A final 150B-token SFT stage completed the training to produce `rnj-1-instruct`.

We used the Muon optimizer throughout all phases. Pre-training followed the WSD learning-rate schedule, consisting of:

- Warmup: Linear ramp-up from 0 to 2e-3 over the first 5K steps.
- Stable phase: Constant learning rate of 2e-3 from 5K → 230K steps.
- Decay: Cosine decay from 2e-3 → 2e-5 from 230K → 380K steps.
- Final stable phase: Constant 2e-5 learning rate from 380K → 443.5K steps, concluding pre-training.

Both the mid-training (context-extension phase) and SFT were trained at a fixed learning rate of 2e-5.

The global batch sizes used were:

- 18M tokens for pre-training.
- 24M tokens for mid-training.
- 16M tokens for SFT.

### Long-Context Extrapolation (up to 128k)
Although Rnj-1-Instruct was trained with context lengths up to 32k, the model can be extrapolated to 128k context using YaRN RoPE scaling. This requires the following updates to `config.json`:
```diff
@@
-  "max_position_embeddings": 32768,
+  "max_position_embeddings": 131072,

@@
-  "sliding_window": 32768,
+  "sliding_window": 131072,

@@
   "rope_scaling": {
     "attn_factor": 1.0,
     "beta_fast": 64.0,
     "beta_slow": 1.0,
     "extrapolation_factor": 1.0,
-    "factor": 4.0,
+    "factor": 16.0,
     "original_max_position_embeddings": 8192,
     "rope_type": "yarn"
   },
```

Overall, most capabilities are preserved under 128k extrapolation, with performance remaining stable on many coding, math, SWE and FIM benchmarks. However, we do observe select regressions, particularly on some science and performance-based evaluations.

| Category   | Evals                 | Rnj-1-instruct | Rnj-1-instruct (128k) |
|------------|-----------------------|-------|--------------|
| Coding     | MBPP+                 | 75.7  | 75.7         |
| Coding     | HE+                   | 83.5  | 82.3         |
| Coding     | BigCodeBench-full     | 57.1  | 55.3         |
| Math       | AIME 25               | 43.3  | 53.3         |
| Math       | GSM8k                 | 92.6  | 91.1         |
| Math       | Minerva-MATH-500      | 88.4  | 89.4         |
| Science    | MMLU-STEM             | 81.8  | 69.4         |
| Science    | GPQA-Diamond          | 38.9  | 41.4         |
| Env evals  | SWE-bench (bash)      | 20.8  | 20.1         |
| Env evals  | Performance: Enamel   | 49.0  | 39.9         |
| FIM        | HE single-line        | 94.9  | 93.5         |
| FIM        | HE multi-line         | 77.6  | 76.5         |
| FIM        | HE random-span        | 86.1  | 85.1         |

We are actively investigating mitigations (including improved scaling strategies and targeted long-context tuning) and expect to close much of this gap in future updates.

# Recommendations

### System Prompt & Temperature

We recommend _always_ adding a system prompt. `You are a helpful assistant.` is a good default prompt to use.

We recommend using temperatures in the range [0, 0.2] for `rnj-1-instruct`.

Failure to follow these recommendations can result in a) truncated outputs, b) code outputs even for non-code prompts.

### Propensity to write code

Rnj-1 models have a strong inclination to write code, even for non-code tasks. This is especially true for `rnj-1-instruct` if the system prompt is omitted. Provide an appropriate system prompt, e.g., “You are a helpful assistant”, along with global task needs to steer the model’s responses in the desired direction.

# How to use

## Serverless API and online playgrounds

- Together.AI: Rnj-1 Instruct is available via API on the [Together.ai](http://Together.ai) model platform for serverless inference. It’s also available in the Together.ai playground for quick and easy experimentation.
- HuggingFace: Rnj-1 Instruct is also hosted via [Hugging Face Spaces](https://huggingface.co/spaces/EssentialAI/rnj-1-instruct-space).

## Running Rnj-1 locally

### Running Rnj-1 on your laptop with llama.cpp

The easiest way to run Rnj-1 on a laptop is via [llama.cpp](https://github.com/ggml-org/llama.cpp).  A pre-quantized checkpoint is available [here](https://huggingface.co/EssentialAI/rnj-1-instruct-GGUF) as well as instructions to get started.

### Use with transformers

Rnj-1 is supported starting from transformers `4.51.2`

1. Example code for querying model without tools
    
    ```python
    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM
    import os
    
    model_id = "EssentialAI/rnj-1-instruct"
    os.environ["HF_TOKEN"] = <YOUR-HF-TOKEN>
    
    print(f"Loading model: {model_id}...")
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        dtype=torch.bfloat16,
        device_map="auto",
    )
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    
    print("Model and tokenizer loaded successfully.")
    
    messages = [
        {"role": "system", "content": "You are a helpful AI assistant."}, # Optional system message
        {"role": "user", "content": "Who are you?"}
    ]
    
    input_ids = tokenizer.apply_chat_template(
        messages, 
        add_generation_prompt=True, 
        return_tensors="pt"
    ).to(model.device)
    
    # --- Generate Prediction --- #
    print("Generating prediction...")
    output_ids = model.generate(
        input_ids,
        max_new_tokens=50,
        pad_token_id=tokenizer.eos_token_id, 
        do_sample=True, 
        temperature=0.2,
        top_p=0.95 
    )
    
    response = tokenizer.decode(output_ids[0][input_ids.shape[-1]:], skip_special_tokens=True)
    print(response)
    ```
    

1. Example code for querying with tools
    
    Rnj-1 supports tool-calling which can be parsed by  `hermes`  tool-call parser. The tool calls are formatted inside `<tool_call>` and `</tool_call>` tags. 
    An example usage is as follows:
    
    ```python
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get the current weather in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {"type": "string", "description": "City and state, e.g., 'San Francisco, CA'"},
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
                    },
                    "required": ["location", "unit"],
                },
            },
        },
    ]
    
    messages = [
        {"role": "system", "content": "You are a helpful AI assistant."}, # Optional system message
        {"role": "user", "content": "What is the weather in San Francisco, CA in Celsius?"}
    ]
    
    input_ids = tokenizer.apply_chat_template(
        messages, 
        tools=tools,
        add_generation_prompt=True, 
        return_tensors="pt"
    ).to(model.device)
    
    # --- Generate Prediction --- #
    print("Generating prediction...")
    output_ids = model.generate(
        input_ids,
        max_new_tokens=200,
        pad_token_id=tokenizer.eos_token_id, 
        do_sample=True, 
        temperature=0.2,
        top_p=0.95 
    )
    
    response = tokenizer.decode(output_ids[0][input_ids.shape[-1]:], skip_special_tokens=False)
    # NOTE: skip_special_tokens is set to False. 
    print(response)
    ```
    

1. Example code for fill-in-the-middle (FIM)
    
    Rnj-1 supports FIM, we show an example payload to trigger FIM mode for Rnj-1 below:
    
    ```python
    PRE = "<|pre_fim|>" 
    MID = "<|mid_fim|>"
    SUF = "<|suf_fim|>"
    
    prefix = """def binary_search(arr, target):
        lo = 0
        hi = len(arr) - 1
    
        while lo <= hi:
    """
    
    suffix = """
        return -1
    """
    
    input = PRE + prefix + SUF + suffix + MID
    
    messages = [
        {"role": "system", "content": "You are a helpful AI assistant."}, 
        {"role": "user", "content": input}
    ]
    
    input_ids = tokenizer.apply_chat_template(
        messages, 
        tools=tools,
        add_generation_prompt=True, 
        return_tensors="pt"
    ).to(model.device)
    
    # --- Generate Prediction --- #
    print("Generating prediction...")
    output_ids = model.generate(
        input_ids,
        max_new_tokens=100,
        pad_token_id=tokenizer.eos_token_id, 
        do_sample=True, 
        temperature=0.2,
        top_p=0.95 
    )
    
    response = tokenizer.decode(output_ids[0][input_ids.shape[-1]:], skip_special_tokens=False)
    print(response)
    ```
    

### Serving Rnj-1 on GPUs

### **vLLM**

On machines that run vLLM, it’s as easy as:

```bash
vllm serve EssentialAI/rnj-1-instruct
```

To launch a vLLM server with tool-calling support enabled:

```python
vllm serve EssentialAI/rnj-1-instruct --enable-auto-tool-choice --tool-call-parser hermes
```

### SGLang

On machines that run SGLang, it’s as easy as:

```bash
python3 -m sglang.launch_server --model EssentialAI/rnj-1-instruct
```

## IDEs and Agents: Claude Code, Cline, Mini-SWE-Agent

### Use with Cline

Rnj-1 works great with Cline, an open source AI coding agent, and is very easy to set up.

The Cline extension is available for VS Code / Cursor, JetBrains IDEs (IntelliJ, PyCharm, WebStorm, etc.) and VSCodium / Windsurf. 

Simply add the Cline extension to your favorite IDE (see instructions [here](https://docs.cline.bot/getting-started/installing-cline)) and then enter the details for your Rnj-1 endpoint (instructions [here](https://docs.cline.bot/getting-started/selecting-your-model)). 

### Use with Claude Code

To use Rnj-1 with Claude Code, you can use https://github.com/musistudio/claude-code-router. Follow the instructions to set up Claude Code and Claude Code Router at https://github.com/musistudio/claude-code-router/blob/main/README.md.

### Agentic mode with Mini-SWE-Agent

Clone the EssentialAI fork of mini-swe-agent ([github](https://github.com/Essential-AI/eai-mini-swe-agent#)). Inside the repo, run the following inside a `virtualenv`:

```python
git checkout eai
pip install -e .
export TOGETHER_API_KEY="..." # set this to your Together.AI access key

# use EssentialAI/rnj-1-instruct to solve a performance optimization task
mini-extra perf-single [--instance <k>]
# use EssentialAI/rnj-1-instruct to resolve a SWE PR description
mini-extra swebench-single [--instance <k>]
```

# Known limitations

### Hallucinations and factual inaccuracies

Rnj-1 is primarily a coding and STEM model. Hence, it is not optimized for factual recovery.

### Identity and knowledge cutoff

Rnj-1 is trained on online web data, and we have observed that it sometimes confuses its identity with other model providers. We believe this is due to a variety of reasons, including references to language models from other providers, model generated data, etc. We hope to rectify this in our follow-up release.

Additionally, Rnj-1 has not been trained or provided with a knowledge cutoff date and may therefore respond with information coming from its training data. If specifically asked for its knowledge cutoff date, the model may hallucinate a date.

# **License**

This repository and the model weights are licensed under [**the Apache License, Version 2.0 (Apache 2.0)**](https://huggingface.co/EssentialAI/rnj-1-instruct/blob/main/LICENSE).

# **Contact**

We welcome your questions and feedback. You can contact us at info@essential.ai.

# **Citation**
```bibtex
@misc{rnj1_instruct,
  title  = {{Rnj-1-Instruct}},
  author = {Ashish Vaswani and Mike Callahan and Adarsh Chaluvaraju and Aleksa Gordić and Devaansh Gupta and Yash Jain and Divya Mansingka and Philip Monk and Khoi Nguyen and Mohit Parmar and Michael Pust and Tim Romanski and Peter Rushton and Ali Shehper and Divya Shivaprasad and Somanshu Singla and Kurt Smith and Saurabh Srivastava and Anil Thomas and Alok Tripathy and Yash Vanjani and Ameya Velingker and {{Essential AI}}},
  year   = {2025},
  url    = {https://huggingface.co/EssentialAI/rnj-1-instruct},
  note   = {Instruction-tuned model release}
}
```