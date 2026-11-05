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
- tokyotech-llm/GPT-OSS-Swallow-120B-SFT-v0.1
---

# GPT-OSS-Swallow

![logo](./gptoss-swallow.png)

**GPT-OSS-Swallow v0.1** is a family of large language models available in **20B** and **120B** parameter sizes. Built as bilingual Japanese-English models, they were developed through Continual Pre-Training (CPT), Supervised Fine-Tuning (SFT), and Reinforcement Learning with Verifiable Rewards (RLVR) based on the GPT-OSS [OpenAI, 2025].

In addition to enhancing Japanese language proficiency and Japanese-English translation capabilities, we minimized the performance degradation in math and coding tasks—often seen during CPT—by utilizing high-quality math and code datasets alongside custom-built data during SFT. Subsequently, we further enhanced the models' math and coding capabilities through RLVR, achieving performance comparable to or surpassing GPT-OSS.

- [GPT-OSS-Swallow Project Page](https://swallow-llm.github.io/gptoss-swallow.en.html)

## Highlights
* **Bilingual Proficiency:** Highly optimized for both Japanese and English.
* **Retained STEM Performance:** Strategic CPT and SFT pipelines successfully prevented catastrophic forgetting in mathematics and coding.
* **Enhanced Reasoning:** Achieved reasoning performance on par with the original GPT-OSS models, and even surpassing them in some tasks.

# Release History

- **Feb 20, 2026**: Released [Qwen3-Swallow](https://huggingface.co/collections/tokyotech-llm/qwen3-swallow-v02) and [GPT-OSS-Swallow](https://huggingface.co/collections/tokyotech-llm/gpt-oss-swallow-v01).

## HF Model Family

We are releasing four GPT-OSS-Swallow models: two SFT models and two RL models (excluding CPT models). Quantized versions of these models will be also available.
The complete list is as follows:

### SFT models

- [GPT-OSS Swallow 20B SFT v0.1](https://huggingface.co/tokyotech-llm/GPT-OSS-Swallow-20B-SFT-v0.1)
- [GPT-OSS Swallow 120B SFT v0.1](https://huggingface.co/tokyotech-llm/GPT-OSS-Swallow-120B-SFT-v0.1)

### RL models

- [GPT-OSS Swallow 20B RL v0.1](https://huggingface.co/tokyotech-llm/GPT-OSS-Swallow-20B-RL-v0.1)
- [GPT-OSS Swallow 120B RL v0.1](https://huggingface.co/tokyotech-llm/GPT-OSS-Swallow-120B-RL-v0.1)

## Model Details

- **Model type**: Please refer to [gpt-oss model card](https://arxiv.org/abs/2508.10925) for details on the model architecture.
- **Language(s)**: Japanese, English
- **Tokenizer**: Please refer to [gpt-oss model card](https://arxiv.org/abs/2508.10925) for details on the tokenizer.
- **Contact**: swallow[at]nlp.c.titech.ac.jp

## Model Performance

For comprehensive details on the evaluation tasks and the resulting scores, please refer to the [Swallow LLM Leaderboard](https://swallow-llm.github.io/leaderboard/).
> [!IMPORTANT]
> The evaluation scores for **`gpt-oss`** and **`gpt-oss-swallow`** were measured with the reasoning effort set to **`medium`**.

### Japanese tasks

![Japanese Performance](./figure/gptoss-swallow-120b-rl_ja_en.svg)

### English tasks

![English Performance](./figure/gptoss-swallow-120b-rl_en_en.svg)


## Usage

### vLLM
> [!TIP]
> This model has been primarily developed and evaluated using vLLM.
> For the most reliable and reproducible behavior, we strongly recommend running inference with vLLM.

vLLM recommends using uv to manage the Python environment.

```sh
uv venv --python 3.12 --seed
source .venv/bin/activate
uv pip install vllm
```

The following command will automatically download the model and start the inference server.

```sh
vllm serve tokyotech-llm/GPT-OSS-Swallow-120B-RL-v0.1
```

Commonly used options include:
- `--port`: Port number for the API server (default: 8000; e.g., 8001).
- `--tensor-parallel-size`: Number of GPUs used for tensor parallelism (e.g., 2 means using two GPUs).
- `--gpu-memory-utilization`: Fraction of GPU memory allocated to the model executor (range: 0–1; e.g., 0.9 means up to 90% of GPU memory is used).
- `--max-model-len`: Maximum model context length (prompt + output tokens) (e.g., 32768).

For the full list of available options, please refer to the official documentation:
https://docs.vllm.ai/en/stable/cli/serve/

Once the server is running, you can send requests using the OpenAI-compatible API:

```python
from openai import OpenAI

# Note: Replace with the actual model path/name you are using
model_name = "tokyotech-llm/GPT-OSS-Swallow-120B-RL-v0.1"

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

There is no default system message.

### Best Practices

We recommend specifying following generation parameters: Temperature=0.6, TopP=0.95, TopK=20, and MinP=0, which are the default values specified in `generation_config.json`.
You may omit manually specifying these parameters when using inference frameworks or clients that respect `generation_config.json` by default.  
We also recommend specifying a max context length of 32,768 or less.  

### Unvalidated use cases

GPT-OSS-Swallow may not be suitable for the following use cases or features.

* **Tool Use (Function Calling):** We did not explicitly train the models for tool use. Users who wish to leverage function-calling capabilities will need to perform custom post-training.
* **Model Identity:** Our training recipe does not account for the "model identity" parameter in the chat template. The model may not consistently identify itself as a specific version ("You are ChatGPT, a large language model trained by OpenAI.").
* **Reasoning Effort Control:** We did not train the model with variations in the "reasoning effort" parameter. For stable results, we strongly recommend keeping the reasoning effort set to `medium` during inference.  
* **Long Context:** We did not explicitly train the models beyond 32k tokens or evaluate performance on long-context tasks, although the model supports context length extension using YaRN, following the original GPT-OSS models.

## Training Datasets

### CPT (Continual Pre-Training)

The following datasets were used for Continual Pre-Training (CPT).
Training was conducted using NVIDIA [NeMo](https://github.com/okoge-kaz/NeMo-gpt-oss) with a context size of 32K (32,768) over a total of 419.4 billion tokens.

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
The following datasets were used for Supervised Fine-Tuning (SFT). These datasets cover general chat in Japanese and English (GPT-OSS-LMSYS), as well as math, coding, and science domains (Swallow-Nemotron). The reasoning traces and assistant responses in these datasets were generated using gpt-oss-120b.  
SFT was conducted using NVIDIA [Automodel](https://github.com/NVIDIA-NeMo/Automodel) with a context size of 32K (32,768). The total training dataset size was 1.1M samples.

- [GPT-OSS-LMSYS-Chat-1M-Synth-Ja](https://huggingface.co/datasets/tokyotech-llm/lmsys-chat-1m-synth): approximately 300k samples
    - We excuded the conversations containing personally identifiable information.
- [GPT-OSS-LMSYS-Chat-1M-Synth-En](https://huggingface.co/datasets/tokyotech-llm/lmsys-chat-1m-synth): approximately 300k samples
    - We excuded the conversations containing personally identifiable information.
- [Swallow-Nemotron-Post-Training-Dataset-v1](https://huggingface.co/datasets/tokyotech-llm/Swallow-Nemotron-Post-Training-Dataset-v1): 500k subsampled samples

### RLVR
The following datasets were used for RLVR.
RLVR was conducted using [slime](https://github.com/THUDM/slime), with its codebase adapted for GPT-OSS support. During RL training, the maximum number of output tokens was set to 24,576 (input prompt tokens are not included).

- Math subset of [allenai/Dolci-Think-RL-7B](https://huggingface.co/datasets/allenai/Dolci-Think-RL-7B)

## Risks and Limitations

The models released here are still in the early stages of our research and development and have not been tuned to ensure outputs align with human intent and safety considerations.

## Acknowledgements

We thank the OpenAI Team for releasing GPT-OSS under a generous open license.

<!-- AIST -->
This work is based on results obtained from AIST policy-based budget project "R&D on Generative AI Foundation Models for the Physical Domain".

<!-- NII -->
This work was supported by the “R&D Hub Aimed at Ensuring Transparency and Reliability of Generative AI Models” project of the Ministry of Education, Culture, Sports, Science and Technology.

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

[OpenAI, 2025] OpenAI. [gpt-oss-120b & gpt-oss-20b Model Card](https://arxiv.org/abs/2508.10925), arXiv:2508.10925.