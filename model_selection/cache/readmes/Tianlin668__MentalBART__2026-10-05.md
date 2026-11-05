---
license: mit
language:
- en
library_name: transformers
pipeline_tag: text-generation
tags:
- mentalhealth
- BART
- text-generation-inference
---

# Introduction

MentalBART is part of the [MentaLLaMA](https://github.com/SteveKGYang/MentalLLaMA) project, the first open-source large language model (LLM) series for 
interpretable mental health analysis with instruction-following capability. This model is finetuned based on the facebook/bart-large foundation model and the full IMHI instruction tuning data.
The model is expected to make complex mental health analysis for various mental health conditions and give reliable explanations for each of its predictions.
It is fine-tuned on the IMHI dataset with 75K high-quality natural language instructions to boost its performance in downstream tasks.
We perform a comprehensive evaluation on the IMHI benchmark with 20K test samples. The result shows that MentalBART can achieve good performance in correctness and generates explanations.

# Ethical Consideration

Although experiments on MentalBART show promising performance on interpretable mental health analysis, we stress that
all predicted results and generated explanations should only used
for non-clinical research, and the help-seeker should get assistance
from professional psychiatrists or clinical practitioners. In addition,
recent studies have indicated LLMs may introduce some potential
bias, such as gender gaps. Meanwhile, some incorrect prediction results, inappropriate explanations, and over-generalization
also illustrate the potential risks of current LLMs. Therefore, there
are still many challenges in applying the model to real-scenario
mental health monitoring systems.

## Other Models in MentaLLaMA

In addition to MentalBART, the MentaLLaMA project includes another model: MentaLLaMA-chat-13B, MentaLLaMA-chat-7B, MentalT5.

- **MentaLLaMA-chat-13B**: This model is finetuned based on the Meta LLaMA2-chat-13B foundation model and the full IMHI instruction tuning data. The training data covers 10 mental health analysis tasks.

- **MentaLLaMA-chat-7B**: This model is finetuned based on the Meta LLaMA2-chat-7B foundation model and the full IMHI instruction tuning data. The training data covers 10 mental health analysis tasks.

- **MentalT5**: This model is finetuned based on the T5-large foundation model and the full IMHI-completion data. The training data covers 10 mental health analysis tasks. This model doesn't have instruction-following ability but is more lightweight and performs well in interpretable mental health analysis in a completion-based manner.

## Usage

You can use the MentalBART model in your Python project with the Hugging Face Transformers library. Here is a simple example of how to load the model:

```python
from transformers import BartTokenizer, BartModel
tokenizer = BartTokenizer.from_pretrained('Tianlin668/MentalBART')
model = BartModel.from_pretrained('Tianlin668/MentalBART')
```


## License

MentalBART is licensed under MIT. For more details, please see the MIT file.

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