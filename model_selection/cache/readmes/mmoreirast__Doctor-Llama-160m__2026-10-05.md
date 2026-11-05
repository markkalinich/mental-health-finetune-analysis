---
license: apache-2.0
datasets:
- mmoreirast/medicine-training-pt
- mmoreirast/medicine-evaluation-pt
language:
- pt
metrics:
- perplexity
library_name: transformers
tags:
- llama-2
- pt
- medicine
---
# Doctor Llama 160m
<img src="./logo.webp" alt="A little llama with a stethoscope." height="50" width="500">

This repository contains a version of [TeenyTinyLlama-160m](https://huggingface.co/nicholasKluge/TeenyTinyLlama-160m) fine-tuned on the [medicine-training-pt](https://huggingface.co/datasets/mmoreirast/medicine-training-pt) dataset.

The main objective of the Doctor Llama model was to study the step-by-step process involved in fine-tuning models in Portuguese, taking into account the challenges encountered in the medical field.

This model was created as part of the course completion project for **Biomedical Informatics at the Federal University of Paraná**. For more information, access the full text at the following link. 

## Author
Mariana Moreira dos Santos ([LinkedIn](https://www.linkedin.com/in/mmoreirast/))

## Code
You can check the codes used to fine-tune the model at the following [Google Colab](https://colab.research.google.com/drive/1SvJvTcH3IRnsEv72UxkVmV0oClCZARtE?usp=sharing) link. 

## Fine-tuning details
- **Base model:** [TeenyTinyLlama 160m](https://huggingface.co/nicholasKluge/TeenyTinyLlama-160m)
- **Context length:** 2048 tokens
- **Dataset for fine-tuning:** [medicine-training-pt](mmoreirast/medicine-training-pt)
- **Dataset for evaluation:** [medicine-evaluation-pt](https://huggingface.co/datasets/mmoreirast/medicine-evaluation-pt)
- **Language:** Portuguese
- **GPU:** NVIDIA L4
- **Training time**: ~9 hours 

## Parameters
- **Number of Epochs:** 4
- **Batch size:** 8
- **Optimizer:** torch.optim.AdamW (warmup_steps = 1e3, learning_rate = 1e-5, epsilon = 1e-8)

## Evaluations


| Model                  |Perplexity      |Evaluation Loss  | 
|---------------------------|-----------------|-------------------|
| TeenyTinyLlama 160m       | 22.51           | 3.11              |
| **Doctor Llama 160m**     | 15.68           | 2.75              |
| TeenyTinyLlama 460m       | 13.09           | 2.57              |
| **Doctor Llama 460m**     | 10.94           | 2.39              |
| TeenyTinyLlama 460m Chat  | 21.22           | 3.05              |
| **Doctor Llama Chat**     | 11.13           | 2.41              |


## Basic usage
Using the `pipeline`:

```python
from transformers import pipeline

generator = pipeline("text-generation", model="mmoreirast/Doctor-Llama-160m")

completions  = generator("Me fale sobre o sistema nervoso", num_return_sequences=2, max_new_tokens=100)

for comp in completions:
  print(f"🤖 {comp['generated_text']}")
```

Using the `AutoTokenizer` and `AutoModelForCausalLM`:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load model and the tokenizer
tokenizer = AutoTokenizer.from_pretrained("mmoreirast/Doctor-Llama-160m", revision='main')
model = AutoModelForCausalLM.from_pretrained("mmoreirast/Doctor-Llama-160m", revision='main')

# Pass the model to your device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.eval()
model.to(device)

# Tokenize the inputs and pass them to the device
inputs = tokenizer("Me fale sobre o sistema nervoso", return_tensors="pt").to(device)

# Generate some text
completions = model.generate(**inputs, num_return_sequences=2, max_new_tokens=100)

# Print the generated text
for i, completion in enumerate(completions):
    print(f'🤖 {tokenizer.decode(completion)}')
```
## Intended Uses

The main objective of the Doctor Llama model was to study the step-by-step process involved in fine-tuning models in Portuguese, taking into account the challenges encountered in the medical field. You may also further fine-tune and adapt Doctor Llama for deployment, as long as your use is following the Apache 2.0 license. If you decide to use pre-trained Doctor Llama as a basis for your fine-tuned model, please conduct your own risk and bias assessment.

## Out-of-scope Use

Doctor Llama is not intended for deployment. It is not a product and should not be used for human-facing interactions.

Doctor Llama models are Brazilian Portuguese language only and are not suitable for translation or generating text in other languages.

## Limitations

As described in the Teeny Tiny Llama model, the Doctor Llama also has the following limitations: 

- **Hallucinations:** This model can produce content that can be mistaken for truth but is, in fact, misleading or entirely false, i.e., hallucination.

- **Biases and Toxicity:** This model inherits the social and historical stereotypes from the data used to train it. Given these biases, the model can produce toxic content, i.e., harmful, offensive, or detrimental to individuals, groups, or communities.

- **Unreliable Code:** The model may produce incorrect code snippets and statements. These code generations should not be treated as suggestions or accurate solutions.

- **Language Limitations:** The model is primarily designed to understand standard Brazilian Portuguese. Other languages might challenge its comprehension, leading to potential misinterpretations or errors in response.

- **Repetition and Verbosity:** The model may get stuck on repetition loops (especially if the repetition penalty during generations is set to a meager value) or produce verbose responses unrelated to the prompt it was given.

Hence, even though our models are released with a permissive license, we urge users to perform their risk analysis on these models if intending to use them for real-world applications and also have humans moderating the outputs of these models in applications where they will interact with an audience, guaranteeing users are always aware they are interacting with a language model.

## Cite as 🤗
```latex
@misc{moreira2024docllama,
  title = {Um Estudo sobre LLMs em Português para a Área Médica},
  author = {Mariana Moreira dos Santos, André Ricardo Abed Grégio},
  url = {},
  year={2024}
}
```
## Acknowledgements
The TeenyTinyLlama base models used here were created by Nicholas Kluge Corrêa and his team. For more information, visit [TeenyTinyLlama](https://huggingface.co/collections/nicholasKluge/teenytinyllama-6582ea8129e72d1ea4d384f1).

## License
Doctor Llama is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for more details.