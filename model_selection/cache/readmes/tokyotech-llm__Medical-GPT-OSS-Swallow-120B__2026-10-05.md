---
license: apache-2.0
language:
- ja
- en
library_name: transformers
pipeline_tag: text-generation
tags:
- gpt_oss
- swallow
- medical
- japanese
- text-generation
base_model: tokyotech-llm/GPT-OSS-Swallow-120B-RL-v0.1
---

# Medical-GPT-OSS-Swallow-120B

Medical-GPT-OSS-Swallow-120B is a medical-domain language model based on [tokyotech-llm/GPT-OSS-Swallow-120B-RL-v0.1](https://huggingface.co/tokyotech-llm/GPT-OSS-Swallow-120B-RL-v0.1). It is designed to support research and development toward safe and trustworthy AI for Japanese clinical settings.

The model follows the GPT-OSS-Swallow model family, which is a bilingual Japanese-English model family based on GPT-OSS and developed through continual pre-training, supervised fine-tuning, and reinforcement learning with verifiable rewards.

## Highlights

- Medical-domain adaptation of GPT-OSS-Swallow 120B
- Bilingual Japanese-English capability inherited from GPT-OSS-Swallow
- Evaluated on Japanese medical and healthcare-related benchmarks
- Intended for research use in medical AI safety and reliability evaluation

## Model Details

- **Model type:** Causal language model, Mixture-of-Experts
- **Base model:** `tokyotech-llm/GPT-OSS-Swallow-120B-RL-v0.1`
- **Language(s):** Japanese, English
- **Tokenizer:** GPT-OSS tokenizer
- **License:** Apache License 2.0

## Model Performance

The following results report this medical-domain model on medical benchmarks. General benchmark results are intentionally omitted because this release focuses on medical-domain performance.

| Model | IgakuQA | JJSIMQA | JMMLU Medical | MMLU_Medical_JP | MedMCQA_JP | MedQA_JP | JUSMLEQA_JP | YakugakuQA |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `Medical-GPT-OSS-Swallow-120B` | 0.7048 | 0.6659 | 0.7022 | 0.7320 | 0.5230 | 0.5118 | 0.5584 | 0.6031 |

## Usage

This model is expected to work with Hugging Face Transformers and vLLM-compatible inference stacks.

### vLLM

```sh
vllm serve tokyotech-llm/Medical-GPT-OSS-Swallow-120B \
  --tensor-parallel-size 8 \
  --max-model-len 32768
```

Once the server is running, you can send requests using an OpenAI-compatible client.

```python
from openai import OpenAI

model_name = "tokyotech-llm/Medical-GPT-OSS-Swallow-120B"
client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")

result = client.chat.completions.create(
    model=model_name,
    messages=[
        {"role": "user", "content": "日本語で、臨床現場における生成AI利用時の注意点を説明してください。"}
    ],
    max_tokens=2048,
    temperature=0.6,
    top_p=0.95,
    extra_body={
        "top_k": 20,
        "min_p": 0,
    },
)

print(result.choices[0].message.content)
```

## Best Practices

We recommend using the generation parameters specified in `generation_config.json` when available. For GPT-OSS-Swallow models, commonly used settings include `temperature=0.6`, `top_p=0.95`, `top_k=20`, and `min_p=0`.

We also recommend specifying a maximum context length of 32,768 tokens or less for inference unless your serving stack has been validated with a longer context.

For large-scale inference, vLLM is recommended. Adjust `--tensor-parallel-size`, `--gpu-memory-utilization`, and `--max-model-len` according to the available GPU memory.

## Training Data

This model was adapted from GPT-OSS-Swallow-120B-RL-v0.1 using a mixture that emphasizes medical-domain text while retaining general-domain data. The medical-domain data includes resources such as biomedical literature, medical synthetic data, medical QA-style data, and clinical guideline-style text.

## Risks and Limitations

This model is intended for research and development. It has not been validated as a medical device and must not be used as a substitute for professional medical judgment. Outputs may contain factual errors, unsafe recommendations, or unsupported clinical claims. Any clinical use requires careful human review, validation, and compliance with applicable laws, regulations, and institutional policies.

## License

Apache License 2.0

## How to Cite

If you find our work helpful, please feel free to cite these papers. The Qwen3-Swallow and GPT-OSS-Swallow Technical Paper (Training Details) will be released in March.

### Continual Pre-Training

```bibtex
@inproceedings{
      fujii2024continual,
      title={Continual Pre-Training for Cross-Lingual {LLM} Adaptation: Enhancing Japanese Language Capabilities},
      author={Kazuki Fujii and Taishi Nakamura and Mengsay Loem and Hiroki Iida and Masanari Ohi and Kakeru Hattori and Hirai Shota and Sakae Mizuki and Rio Yokota and Naoaki Okazaki},
      booktitle={First Conference on Language Modeling},
      year={2024}
}
```

### Supervised Fine-Tuning

```bibtex
@inproceedings{
      ma2025building,
      title={Building Instruction-Tuning Datasets from Human-Written Instructions with Open-Weight Large Language Models},
      author={Youmi Ma and Sakae Mizuki and Kazuki Fujii and Taishi Nakamura and Masanari Ohi and Hinari Shimada and Taihei Shiotani and Koshiro Saito and Koki Maeda and Kakeru Hattori and Takumi Okamoto and Shigeki Ishida and Rio Yokota and Hiroya Takamura and Naoaki Okazaki},
      booktitle={Second Conference on Language Modeling},
      year={2025}
}
```

## References

[OpenAI, 2025] OpenAI. gpt-oss-120b & gpt-oss-20b Model Card, arXiv:2508.10925.

## Acknowledgements

This work builds on GPT-OSS and GPT-OSS-Swallow. We thank the OpenAI team and the contributors to the GPT-OSS-Swallow project.

この成果は、国立研究開発法人新エネルギー・産業技術総合開発機構（ＮＥＤＯ）の助成事業（JPNP25006）の結果得られたものです。

This model is based on the results obtained from the project, JPNP25006, subsidized by the New Energy and Industrial Technology Development Organization (NEDO).
