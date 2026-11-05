---
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 458762343
    num_examples: 99086
  download_size: 211247054
  dataset_size: 458762343
license: mit
task_categories:
- text-generation
language:
- en
tags:
- medical
pretty_name: Synthetic Mental Therapy Dataset
size_categories:
- 10K<n<100K
---
# Dataset Card for "phr_mental_health_dataset"
- This dataset is a cleaned version of [nart-100k-synthetic](https://huggingface.co/datasets/jerryjalapeno/nart-100k-synthetic)
- The data is generated synthetically using gpt3.5-turbo using [this](https://github.com/jerryjalapeno/nart-100k-7b/blob/main/synthetic_conv_gen.py) script.
- The dataset had a "sharegpt" style JSONL format, with each JSON having keys "human" and "gpt", having an equal number of both.
- The data was then cleaned, and the following changes were made
  - The names "Alex" and "Charlie" were removed from the dataset, which can often come up in the conversation of fine-tuned models.
- The data was then converted to the format required for llama-2-chat models.
  - The dataset was converted to JSONL format with just a single key, "text", which contains the combined text for training the model.
  - The appropriate llama-2 system prompt was added at the beginning of the conversation.
  - The conversation was then enclosed with [INST], [\INST], `<s> and </s>` formats as defined in [llama-2](https://huggingface.co/blog/llama2#:~:text=Using%20text-generation-inference%20and%20Inference%20Endpoints&text=You%20can%20try%20out%20Text,Deploy%20-%3E%20Inference%20Endpoints%20widget.) article.
  - Whether to include the last conversation, i.e., the last GPT response or not, was chosen randomly. 
