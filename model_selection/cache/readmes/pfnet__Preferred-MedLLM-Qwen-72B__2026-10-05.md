---
base_model: Qwen/Qwen2.5-72B
language:
  - en
  - ja
library_name: transformers
pipeline_tag: text-generation
license: other
license_name: qwen
---

# Preferred-MedLLM-Qwen-72B

## Model Description

Preferred-MedLLM-Qwen-72B is a finetuned model based on [Qwen/Qwen2.5-72B](https://huggingface.co/Qwen/Qwen2.5-72B), which has undergone continued pretraining on an original corpus of medical-related text.

The model is released under the [Qwen LICENSE](https://huggingface.co/Qwen/Qwen2.5-72B/blob/main/LICENSE).

## Model Performance

The table below shows the performance on the Japanese medical licensing examination from 2018 to 2022 ([IgakuQA](https://github.com/jungokasai/IgakuQA)).
| Model ID                                                                                                            |   Average |   2018 |   2019 |   2020 |   2021 |   2022 |
|:--------------------------------------------------------------------------------------------------------------------|-------------------:|-------:|-------:|-------:|-------:|-------:|
| **Preferred-MedLLM-Qwen-72B**          |              **431.2** |    **434** |    420 |    **439** |    **430** |    433 |
| GPT-4o                                                                                                 |              430.4 |    427 |    **431** |    433 |    427 |    **434** |
| [Qwen2.5-72B](https://huggingface.co/Qwen/Qwen2.5-72B)                                                                         |              398.4 |    412 |    394 |    394 |    393 |    399 |
| [Llama3-Preferred-MedSwallow-70B](https://huggingface.co/pfnet/Llama3-Preferred-MedSwallow-70B)          |              395.2 |    407 |    390 |    391 |    393 |    395 |
| GPT-4                                                                                                                |              388.8 |    382 |    385 |    387 |    398 |    392 |
| [Mistral-Large-Instruct-2407](https://huggingface.co/mistralai/Mistral-Large-Instruct-2407)                 |              376   |    370 |    371 |    390 |    373 |    376 |
| [Llama-3.1-Swallow-70B-v0.1](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-70B-v0.1)               |              368.4 |    379 |    378 |    379 |    351 |    355 |
| [Meta-Llama-3-70B](https://huggingface.co/meta-llama/Meta-Llama-3-70B)                                                                                 |              334.6 |    353 |    340 |    348 |    314 |    318 |
| GPT-3.5                                                                                                             |              273.2 |    266 |    250 |    266 |    297 |    287 |

## Limitations

The model was developed for research purposes and is not intended for clinical diagnosis.
It is the users' responsibility to ensure compliance with applicable rules and regulations.

## Contributors

Preferred Networks, Inc.
- Junichiro Iwasawa
- Wataru Kawakami
- Keita Suzuki

## Publications

Detailed evaluation results are given in the [blog](https://tech.preferred.jp/ja/blog/preferred-medllm-qwen-72b/) and [research paper](https://arxiv.org/abs/2504.18080).

## Citations
```
@article{preferredmedllm2025,
      title={Stabilizing Reasoning in Medical LLMs with Continued Pretraining and Reasoning Preference Optimization}, 
      author={Kawakami, Wataru and Suzuki, Keita and Iwasawa, Junichiro},
      journal={arXiv preprint arXiv:2504.18080},
      year={2025}
}
```

## License

[Qwen LICENSE](https://huggingface.co/Qwen/Qwen2.5-72B/blob/main/LICENSE)
