---
license: mit
language:
- en
library_name: transformers
pipeline_tag: text-generation
tags:
- t5
- mentalhealth
- text-generation-inference
---

# Introduction

MentalT5 is part of the [MentaLLaMA](https://github.com/SteveKGYang/MentalLLaMA) project, the first open-source large language model (LLM) series for 
interpretable mental health analysis with instruction-following capability. This model is finetuned based on the t5-large foundation model and the full IMHI instruction tuning data.
The model is expected to make complex mental health analysis for various mental health conditions and give reliable explanations for each of its predictions.
It is fine-tuned on the IMHI dataset with 75K high-quality natural language instructions to boost its performance in downstream tasks.
We perform a comprehensive evaluation on the IMHI benchmark with 20K test samples. The result shows that MentalT5 can achieve good performance in correctness and generates explanations.

# Ethical Consideration

Although experiments on MentalT5 show promising performance on interpretable mental health analysis, we stress that
all predicted results and generated explanations should only used
for non-clinical research, and the help-seeker should get assistance
from professional psychiatrists or clinical practitioners. In addition,
recent studies have indicated LLMs may introduce some potential
bias, such as gender gaps. Meanwhile, some incorrect prediction results, inappropriate explanations, and over-generalization
also illustrate the potential risks of current LLMs. Therefore, there
are still many challenges in applying the model to real-scenario
mental health monitoring systems.

## Other Models in MentaLLaMA

In addition to MentalT5, the MentaLLaMA project includes another model: MentaLLaMA-chat-13B, MentaLLaMA-chat-7B, MentalBART.

- **MentaLLaMA-chat-13B**: This model is finetuned based on the Meta LLaMA2-chat-13B foundation model and the full IMHI instruction tuning data. The training data covers 10 mental health analysis tasks.

- **MentaLLaMA-chat-7B**: This model is finetuned based on the Meta LLaMA2-chat-7B foundation model and the full IMHI instruction tuning data. The training data covers 10 mental health analysis tasks.

- **MentalBART**: This model is finetuned based on the BART-large foundation model and the full IMHI-completion data. The training data covers 10 mental health analysis tasks. This model doesn't have instruction-following ability but is more lightweight and performs well in interpretable mental health analysis in a completion-based manner. 

## Usage

You can use the MentalT5 model in your Python project with the Hugging Face Transformers library. Here is a simple example of how to load the model:

```python
from transformers import T5Tokenizer, T5Model
tokenizer = T5Tokenizer.from_pretrained('Tianlin668/MentalT5')
model = T5Model.from_pretrained('Tianlin668/MentalT5')
```


## License

MentalT5 is licensed under MIT. For more details, please see the MIT file.

## Citation

If you use MentalBART in your work, please cite the our paper:

```bibtex
@misc{yang2023mentalllama,
      title={MentalLLaMA: Interpretable Mental Health Analysis on Social Media with Large Language Models}, 
      author={Kailai Yang and Tianlin Zhang and Ziyan Kuang and Qianqian Xie and Sophia Ananiadou},
      year={2023},
      eprint={2309.13567},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```