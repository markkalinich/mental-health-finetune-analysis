---
language:
- en
- ja
license: apache-2.0
datasets:
- tokyotech-llm/swallow-math-v2
- tokyotech-llm/swallow-code-v2
- tokyotech-llm/Swallow-Nemotron-Post-Training-Dataset-v1
- tokyotech-llm/lmsys-chat-1m-synth
library_name: transformers
pipeline_tag: text-generation
model_type: null
base_model:
- tokyotech-llm/Qwen3-Swallow-30B-A3B-SFT-v0.2
---

# Qwen3-Swallow

![logo](./qwen3-swallow.png)

**Qwen3-Swallow v0.2** is a family of large language models available in **8B**, **30B-A3B**, and **32B** parameter sizes. Built as bilingual Japanese-English models, they were developed through Continual Pre-Training (CPT), Supervised Fine-Tuning (SFT), and Reinforcement Learning with Verifiable Rewards (RLVR) based on the Qwen3 [Yang, 2025].

In addition to enhancing Japanese language proficiency and Japanese-English translation capabilities, we significantly improved or maintained performance on math and coding tasks during CPT by using high-quality math and code datasets with reasoning traces, along with custom-built datasets during SFT. Subsequently, we further improved the models' math and coding performance by enhancing reasoning capabilities through RLVR.

- [Qwen3-Swallow Project Page](https://swallow-llm.github.io/qwen3-swallow.en.html)

> [!NOTE]
> Please note that Qwen3-Swallow v0.1 is a skipped version number.

## Highlights
* **Bilingual Proficiency:** Highly optimized for both Japanese and English.
* **Retained STEM Performance:** Strategic CPT and SFT pipelines successfully prevented catastrophic forgetting in mathematics and coding.
* **Enhanced Reasoning:** Achieved reasoning performance on par with the original Qwen3 models, and even surpassing them in some tasks.

# Release History

- **Feb 20, 2026**: Released [Qwen3-Swallow](https://huggingface.co/collections/tokyotech-llm/qwen3-swallow-v02) and [GPT-OSS-Swallow](https://huggingface.co/collections/tokyotech-llm/gpt-oss-swallow-v01).
- **Feb 23, 2026**: We made the GPTQ-quantized models private due to significant performance degradation. Please use the AWQ-quantized model instead.

## HF Model Family

We are releasing nine Qwen3-Swallow models: three each for CPT, SFT, and RL models.  
Quantized versions of RL models are also available.
The complete list is as follows:

### CPT models

- [Qwen3 Swallow 8B CPT v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-CPT-v0.2)
- [Qwen3 Swallow 30B-A3B CPT v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-30B-A3B-CPT-v0.2)
- [Qwen3 Swallow 32B CPT v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-32B-CPT-v0.2)

### SFT models

- [Qwen3 Swallow 8B SFT v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-SFT-v0.2)
- [Qwen3 Swallow 30B-A3B SFT v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-30B-A3B-SFT-v0.2)
- [Qwen3 Swallow 32B SFT v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-32B-SFT-v0.2)

### RL models

- [Qwen3 Swallow 8B RL v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2)
- [Qwen3 Swallow 30B-A3B RL v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-30B-A3B-RL-v0.2)
- [Qwen3 Swallow 32B RL v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-32B-RL-v0.2)

### Quantized models

- [Qwen3 Swallow 8B RL v0.2 AWQ-INT4](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2-AWQ-INT4)
- ~~Qwen3 Swallow 8B RL v0.2 GPTQ-INT4~~
- [Qwen3 Swallow 30B-A3B RL v0.2 AWQ-INT4](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-30B-A3B-RL-v0.2-AWQ-INT4)
- ~~Qwen3 Swallow 30B-A3B RL v0.2 GPTQ-INT4~~
- [Qwen3 Swallow 32B RL v0.2 AWQ-INT4](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-32B-RL-v0.2-AWQ-INT4)
- ~~Qwen3 Swallow 32B RL v0.2 GPTQ-INT4~~


## Model Details

- **Model type**: Please refer to [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388) for details on the model architecture.
- **Language(s)**: Japanese, English
- **Tokenizer**: Please refer to [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388) for details on the tokenizer.
- **Contact**: swallow[at]nlp.c.titech.ac.jp

## Model Performance

For comprehensive details on the evaluation tasks and the resulting scores, please refer to the [Swallow LLM Leaderboard](https://swallow-llm.github.io/leaderboard/).

### Japanese tasks

![Japanese Performance](./figure/qwen3-swallow-30b-a3b-rl_ja_en.svg)


### English tasks

![Japanese Performance](./figure/qwen3-swallow-30b-a3b-rl_en_en.svg)

## Usage

### vLLM
> [!TIP]
> This model has been primarily debugged and evaluated using vLLM.
> For the most reliable and reproducible behavior, we strongly recommend running inference with vLLM.

vLLM recommends using uv to manage the Python environment.

```sh
uv venv --python 3.12 --seed
source .venv/bin/activate
uv pip install vllm
```

The following command will automatically download the model and start the server.
```sh
vllm serve tokyotech-llm/Qwen3-Swallow-30B-A3B-RL-v0.2 --reasoning-parser qwen3
```
Commonly used options include:
- `--port` : Port number for the API server (default: 8000)
- `--tensor-parallel-size` : Number of GPUs for tensor parallelism (eg., 2 means using 2 GPUs for tensor parallelism)
- `--gpu-memory-utilization` : The fraction of GPU memory to be used for the model executor, which can range from 0 to 1.(e.g., 0.9 means using up to 90% of GPU memory)
- `--max-model-len` : Model context length of prompts + outputs.(eg., 32768)

For the full list of available options, please refer to the official documentation:
https://docs.vllm.ai/en/stable/cli/serve/

Once the server is running, you can send requests using the OpenAI-compatible API:
```python
from openai import OpenAI
# Note: Replace with the actual model path/name you are using
model_name = "tokyotech-llm/Qwen3-Swallow-30B-A3B-RL-v0.2"
client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="EMPTY"
)
result = client.chat.completions.create(
    model=model_name,
    messages=[
        {"role": "user", "content": "Create a casual one-day Tokyo itinerary in Japanese."}
    ],
    max_tokens=4096,
    temperature=0.6,
    top_p=0.95,
    extra_body={
        "top_k": 20,
        "min_p": 0,
    }
)
print("Reasoning:")
print(result.choices[0].message.reasoning)
print("\nResponse:")
print(result.choices[0].message.content)
```

### Best Practices

We recommend specifying following generation parameters: Temperature=0.6, TopP=0.95, TopK=20, and MinP=0, which are the default values specified in `generation_config.json`.
You may omit manually specifying these parameters when using inference frameworks or clients that respect `generation_config.json` by default.  
We also recommend specifying a max context length of 32,768 or less.  

### Unvalidated use cases

- **Tool Use**: Please note that Qwen3-Swallow has not been explicitly trained for Tool Use (Function Calling). Users wishing to utilize Tool Use capabilities should consider performing custom post-training.

- **Reasoning Toggle**: Qwen3-Swallow does not support toggling a "Reasoning ON/OFF" feature. Both the SFT and RL models are designed to perform reasoning by default.

## Training Datasets

### CPT (Continual Pre-Training)

The following datasets were used for Continual Pre-Training (CPT).
Training was conducted using NVIDIA [Megatron-LM](https://github.com/NVIDIA/Megatron-LM) with a context size of 32K (32,768) over a total of 209.7 billion tokens.

#### Japanese and Japanese-English Parallel Corpus

- [Japanese Wikipedia 2503](https://dumps.wikimedia.org/other/cirrussearch)
- [Swallow Corpus Version 3.2](https://arxiv.org/abs/2404.17733)
- [Swallow Corpus Version 3.2 QA](https://arxiv.org/abs/2404.17733) (synthetic QA-format text using gpt-oss-120b)
- [Laboro ParaCorpus](https://github.com/laboroai/Laboro-ParaCorpus)
- [Kaken ParaCorpus(Ja-En)](https://huggingface.co/datasets/hpprc/kaken-trans-ja-en)

#### English Corpus
- [English Wikipedia 2503](https://dumps.wikimedia.org/other/cirrussearch)
- [Cosmopedia](https://huggingface.co/datasets/HuggingFaceTB/cosmopedia)
- [Nemotron-CC](https://arxiv.org/abs/2412.02595)(2010-2024) high quality actual subset

#### Math, Code
- [Swallow Code Version 2](https://huggingface.co/datasets/tokyotech-llm/swallow-code-v2)
- [Swallow Code Version 2 Q&A](https://huggingface.co/datasets/tokyotech-llm/swallow-code-v2)
- [Swallow Math Version 2](https://huggingface.co/datasets/tokyotech-llm/swallow-math-v2)
- [Swallow Math Version 2 Q&A](https://huggingface.co/datasets/tokyotech-llm/swallow-math-v2)

#### STEM, Reasoning, and General Chat
- [GPT-OSS-LMSYS-Chat-1M-Synth-Ja](https://huggingface.co/datasets/tokyotech-llm/lmsys-chat-1m-synth)
- [GPT-OSS-LMSYS-Chat-1M-Synth-En](https://huggingface.co/datasets/tokyotech-llm/lmsys-chat-1m-synth)
- [Swallow-Nemotron-Post-Training-Dataset-v1](https://huggingface.co/datasets/tokyotech-llm/Swallow-Nemotron-Post-Training-Dataset-v1) (math, code, stem)

### SFT (Supervised Fine-Tuning)
The following datasets were used for Supervised Fine-Tuning (SFT).
SFT was conducted using NVIDIA [Megatron-LM](https://github.com/NVIDIA/Megatron-LM) with a context size of 32K (32,768). The training dataset sizes were as follows: 2.1M samples for 8B model, and 1.1M samples for both 30B-A3B and 32B models.

- [GPT-OSS-LMSYS-Chat-1M-Synth-Ja](https://huggingface.co/datasets/tokyotech-llm/lmsys-chat-1m-synth): approximately 300k samples
  - We excuded the conversations containing personally identifiable information.
- [GPT-OSS-LMSYS-Chat-1M-Synth-En](https://huggingface.co/datasets/tokyotech-llm/lmsys-chat-1m-synth): approximately 300k samples
  - We excuded the conversations containing personally identifiable information.
- [Swallow-Nemotron-Post-Training-Dataset-v1](https://huggingface.co/datasets/tokyotech-llm/Swallow-Nemotron-Post-Training-Dataset-v1) (math, code, stem)


### RLVR
The following datasets were used for RLVR.
RLVR was conducted using [slime](https://github.com/THUDM/slime). During RL training, the maximum number of output tokens was set to 24,576 (input prompt tokens are not included).


- Math subset of [allenai/Dolci-Think-RL-7B](https://huggingface.co/datasets/allenai/Dolci-Think-RL-7B)

### Quantization

We provide AWQ-INT4 quantized variants of the RL models.
We generated outputs from RL dataset prompts, validated them, and used only complete, well-formed generations (excluding poor or incomplete outputs) for quantization calibration.

## Risks and Limitations

The models released here are still in the early stages of our research and development and have not been tuned to ensure outputs align with human intent and safety considerations.

## Acknowledgements

We thank Qwen Team for releasing Qwen3 under a generous open license.

<!-- 医療LLM -->
This work is based on results obtained from a project, JPNP25006, subsidized by the New Energy and Industrial Technology Development Organization (NEDO).

<!-- NII -->
This work was supported by the "R&D Hub Aimed at Ensuring Transparency and Reliability of Generative AI Models" project of the Ministry of Education, Culture, Sports, Science and Technology.

<!-- ABCI -->
We used ABCI 3.0 provided by AIST and AIST Solutions with support from "ABCI 3.0 Development Acceleration Use".

<!-- TSUBAME -->
This study was carried out using the TSUBAME4.0 supercomputer at Institute of Science Tokyo.

## License

[Apache license 2.0](./LICENSE)

## Authors

[Swallow LLM](https://swallow-llm.github.io/index.en.html)

## How to cite

If you find our work helpful, please feel free to cite these papers.
**The Qwen3-Swallow and GPT-OSS-Swallow Technical Paper (Training Details) will be released in March.**

### Continual Pre-Training

```
@inproceedings{
      fujii2024continual,
      title={Continual Pre-Training for Cross-Lingual {LLM} Adaptation: Enhancing Japanese Language Capabilities},
      author={Kazuki Fujii and Taishi Nakamura and Mengsay Loem and Hiroki Iida and Masanari Ohi and Kakeru Hattori and Hirai Shota and Sakae Mizuki and Rio Yokota and Naoaki Okazaki},
      booktitle={First Conference on Language Modeling},
      year={2024}
}
```

### Supervised Fine-Tuning

```
@inproceedings{
      ma2025building,
      title={Building Instruction-Tuning Datasets from Human-Written Instructions with Open-Weight Large Language Models},
      author={Youmi Ma and Sakae Mizuki and Kazuki Fujii and Taishi Nakamura and Masanari Ohi and Hinari Shimada and Taihei Shiotani and Koshiro Saito and Koki Maeda and Kakeru Hattori and Takumi Okamoto and Shigeki Ishida and Rio Yokota and Hiroya Takamura and Naoaki Okazaki},
      booktitle={Second Conference on Language Modeling},
      year={2025}
}
```


### References

[Yang, 2025] Alibaba. [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388), arxiv:2505.09388.