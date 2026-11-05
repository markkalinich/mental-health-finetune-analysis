---
language: cs
widget:
  - text: Tato fraktura je následkem
license: mit
datasets:
  - UFALMedicalCorpus
---

# Czech GPT-2 small model trained on the Czech medical data
This model was trained as a part of the [master thesis](https://dspace.cuni.cz/handle/20.500.11956/176356?locale-attribute=en) on the subset of the [UFAL Medical Corpus v. 1.0](https://ufal.mff.cuni.cz/ufal_medical_corpus).  

## Introduction
Czech-GPT2-Medical (Czech GPT-2 small) is a state-of-the-art language model for Czech based on the GPT-2 small model and is specialized on medical texts. Unlike the original GPT-2 small model, this model is trained to predict only 512 tokens instead of 1024 as it served as a basis for different task - generating medical reports from X-ray images, which are generally shorter in nature.

The model was trained on the subset of the [UFAL Medical Corpus v. 1.0](https://ufal.mff.cuni.cz/ufal_medical_corpus) dataset using Transfer Learning and Fine-tuning techniques in about 40 minutes on one NVIDIA A100 SXM4 40GB and with a total of 100 MB of training data.

This model was trained as a part of the master thesis as a proof-of-concept that it is possible to get a state-of-the-art language model in Czech language with smaller ressources than the original one, and in a significantly shorter time. There was no Czech GPT-2 model available at the time the master thesis began.

It was fine-tuned from the [Czech-GPT2-OSCAR](https://huggingface.co/lchaloupsky/czech-gpt2-medical/) using the Hugging Face libraries (Transformers and Tokenizers) wrapped into the fastai v2 Deep Learning framework. All the fine-tuning fastai v2 techniques were used.
The solution is based on the [Faster than training from scratch — Fine-tuning the English GPT-2 in any language with Hugging Face and fastai v2 (practical case with Portuguese)](https://medium.com/@pierre_guillou/faster-than-training-from-scratch-fine-tuning-the-english-gpt-2-in-any-language-with-hugging-f2ec05c98787) article.

Trained model is now available on Hugging Face under [czech-gpt2-medical](https://huggingface.co/lchaloupsky/czech-gpt2-medical/). For more information please let me know in the discussion.

## Training/Evaluation
For more information on training the model or its evaluation, please have a look at the [thesis](https://dspace.cuni.cz/handle/20.500.11956/176356?locale-attribute=en) itself.

## GPT-2 Model description
*Note: information copied/pasted from [Model: gpt2 >> Model description](https://huggingface.co/gpt2#model-description)*

GPT-2 is a transformers model pretrained on a very large corpus of English data in a self-supervised fashion. This means it was pretrained on the raw texts only, with no humans labelling them in any way (which is why it can use lots of publicly available data) with an automatic process to generate inputs and labels from those texts. More precisely, it was trained to guess the next word in sentences.

More precisely, inputs are sequences of continuous text of a certain length and the targets are the same sequence, shifted one token (word or piece of word) to the right. The model uses internally a mask-mechanism to make sure the predictions for the token `i` only uses the inputs from `1` to `i` but not the future tokens.

This way, the model learns an inner representation of the English language that can then be used to extract features useful for downstream tasks. The model is best at what it was pretrained for however, which is generating texts from a prompt.

## How to use Czech-GPT2-Medical with HuggingFace (PyTorch)
*The following code use PyTorch. To use TensorFlow, check the below corresponding paragraph.*

### Load Czech-GPT2-Medical and its sub-word tokenizer (Byte-level BPE)
```python
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

tokenizer = GPT2Tokenizer.from_pretrained("lchaloupsky/czech-gpt2-medical")
model = GPT2LMHeadModel.from_pretrained("lchaloupsky/czech-gpt2-medical")

# Get sequence length max of 1024
tokenizer.model_max_length=1024
# For older versions of the 'transformers' library use this
# tokenizer.max_len=1024

model.eval()  # disable dropout (or leave in train mode to finetune)
```

### Generate one word
```python
# input sequence
text = "Tato fraktura je následkem"
inputs = tokenizer(text, return_tensors="pt")

# model output
outputs = model(**inputs, labels=inputs["input_ids"])
loss, logits = outputs[:2]
predicted_index = torch.argmax(logits[0, -1, :]).item()
predicted_text = tokenizer.decode([predicted_index])

# results
print('input text:', text)
print('predicted text:', predicted_text)
```

### Generate one full sequence
```python
# input sequence
text = "Tato fraktura je následkem"
inputs = tokenizer(text, return_tensors="pt") # tokenizer.encode(text, return_tensors="pt") directly for input_ids

# model output using Top-k sampling text generation method
sample_outputs = model.generate(inputs.input_ids,
                                pad_token_id=50256,
                                do_sample=True, 
                                max_length=50, # put the token number you want
                                top_k=40,
                                num_return_sequences=1)

# generated sequence
for i, sample_output in enumerate(sample_outputs):
    print("{}\n\n{}".format(i+1, tokenizer.decode(sample_output.tolist()))) # tokenizer.decode(sample_output, skip_special_tokens=True)
```

## How to use Czech-GPT2-Medical with HuggingFace (TensorFlow)
*The following code use TensorFlow. To use PyTorch, check the above corresponding paragraph.*

### Load Czech-GPT2-Medical and its sub-word tokenizer (Byte-level BPE)
```python
from transformers import GPT2Tokenizer, TFGPT2LMHeadModel
import tensorflow as tf

tokenizer = GPT2Tokenizer.from_pretrained("lchaloupsky/czech-gpt2-medical")
model = TFGPT2LMHeadModel.from_pretrained("lchaloupsky/czech-gpt2-medical")

# Get sequence length max of 1024
tokenizer.model_max_length=1024
# For older versions of the 'transformers' library use this
# tokenizer.max_len=1024

model.eval()  # disable dropout (or leave in train mode to finetune)
```

### Generate one full sequence
```python
# input sequence
text = "Tato fraktura je následkem"
input_ids = tokenizer.encode(text, return_tensors="tf")

# model output using Top-k sampling text generation method
outputs = model.generate(input_ids, eos_token_id=50256, pad_token_id=50256, 
                         do_sample=True,
                         max_length=40,
                         top_k=40)
print(tokenizer.decode(outputs[0])) # tokenizer.decode(outputs[0], skip_special_tokens=True)
```

## Limitations and bias
The training data used for this model are not extensive as they are only a part of the UFAL Medical Corpus dataset. We know it contains some noisy content, which is far from neutral. As the openAI team themselves point out in their model card:

> Because large-scale language models like GPT-2 do not distinguish fact from fiction, we don’t support use-cases that require the generated text to be true. Additionally, language models like GPT-2 reflect the biases inherent to the systems they were trained on, so we do not recommend that they be deployed into systems that interact with humans > unless the deployers first carry out a study of biases relevant to the intended use-case. We found no statistically significant difference in gender, race, and religious bias probes between 774M and 1.5B, implying all versions of GPT-2 should be approached with similar levels of caution around use cases that are sensitive to biases around human attributes.

## Author
Czech-GPT2-Medical was trained and evaluated by [Lukáš Chaloupský](https://cz.linkedin.com/in/luk%C3%A1%C5%A1-chaloupsk%C3%BD-0016b8226?original_referer=https%3A%2F%2Fwww.google.com%2F) thanks to the computing power of the GPU (NVIDIA A100 SXM4 40GB) cluster of [IT4I](https://www.it4i.cz/) (VSB - Technical University of Ostrava).

## Citation
```
@article{chaloupsky2022automatic,
  title={Automatic generation of medical reports from chest X-rays in Czech},
  author={Chaloupsk{\`y}, Luk{\'a}{\v{s}}},
  year={2022},
  publisher={Charles University, Faculty of Mathematics and Physics}
}
```