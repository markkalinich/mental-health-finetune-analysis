---
license: apache-2.0
language:
- ja
- en
library_name: transformers
pipeline_tag: text-generation
tags:
- qwen3
- swallow
- medical
- japanese
- text-generation
base_model: tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2
---

# Medical-Qwen3-Swallow-8B

Medical-Qwen3-Swallow-8B is a medical-domain language model based on [tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2). It is designed to support research and development toward safe and trustworthy AI for Japanese clinical settings.

The model follows the Qwen3-Swallow model family, which is a bilingual Japanese-English model family based on Qwen3 and developed through continual pre-training, supervised fine-tuning, and reinforcement learning with verifiable rewards.

## Highlights

- Medical-domain adaptation of Qwen3-Swallow-8B-RL-v0.2
- Bilingual Japanese-English capability inherited from Qwen3-Swallow
- Evaluated on Japanese medical and healthcare-related benchmarks
- Intended for research use in medical AI safety and reliability evaluation

## Model Details

- **Model type:** Causal language model
- **Base model:** `tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2`
- **Language(s):** Japanese, English
- **Tokenizer:** Qwen3-Swallow tokenizer
- **License:** Apache License 2.0

## Model Performance

The following results compare the base model and this medical-domain model on medical benchmarks. General benchmark results are intentionally omitted because this release focuses on medical-domain performance.

| Model | IgakuQA | JJSIMQA | JMMLU Medical | MMLU_Medical_JP | MedMCQA_JP | MedQA_JP | JUSMLEQA_JP | YakugakuQA |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2` | 0.659 | 0.589 | 0.702 | 0.722 | 0.510 | 0.506 | 0.564 | 0.590 |
| `Medical-Qwen3-Swallow-8B` | 0.709 | 0.710 | 0.704 | 0.725 | 0.546 | 0.552 | 0.589 | 0.641 |

## Usage

This model is expected to work with Hugging Face Transformers and vLLM-compatible inference stacks.

### vLLM

```sh
vllm serve tokyotech-llm/Medical-Qwen3-Swallow-8B --reasoning-parser qwen3 --max-model-len 32768
```

Once the server is running, you can send requests using an OpenAI-compatible client.

```python
from openai import OpenAI

model_name = "tokyotech-llm/Medical-Qwen3-Swallow-8B"
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

We recommend using the generation parameters specified in `generation_config.json` when available. For Qwen3-Swallow models, commonly used settings include `temperature=0.6`, `top_p=0.95`, `top_k=20`, and `min_p=0`.

We also recommend specifying a maximum context length of 32,768 tokens or less for inference unless your serving stack has been validated with a longer context.

## Training Data

This model was adapted from Qwen3-Swallow-8B-RL-v0.2 using a mixture that emphasizes medical-domain text while retaining general-domain data. The medical-domain data includes resources such as biomedical literature, medical synthetic data, medical QA-style data, and clinical guideline-style text.

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

[Yang, 2025] Alibaba. Qwen3 Technical Report, arxiv:2505.09388.

## Acknowledgements

This work builds on Qwen3 and Qwen3-Swallow. We thank the Qwen team and the contributors to the Qwen3-Swallow project.

この成果は、国立研究開発法人新エネルギー・産業技術総合開発機構（ＮＥＤＯ）の助成事業（JPNP25006）の結果得られたものです。

This model is based on the results obtained from the project, JPNP25006, subsidized by the New Energy and Industrial Technology Development Organization (NEDO).
