---
size_categories: n<1K
dataset_info:
  features:
  - name: instruction
    dtype: 'null'
  - name: input
    dtype: string
  - name: output
    dtype: string
  - name: generations
    sequence: string
  - name: generation_models
    sequence: string
  - name: distilabel_metadata
    struct:
    - name: raw_input_generate-responses
      list:
      - name: content
        dtype: string
      - name: role
        dtype: string
    - name: raw_input_prometheus
      dtype: 'null'
    - name: raw_output_generate-responses
      dtype: string
    - name: raw_output_prometheus
      dtype: 'null'
  - name: feedback
    dtype: 'null'
  - name: result
    dtype: 'null'
  - name: model_name
    dtype: 'null'
  - name: generation
    dtype: 'null'
  splits:
  - name: train
    num_bytes: 17802072
    num_examples: 6310
  download_size: 6972096
  dataset_size: 17802072
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
tags:
- synthetic
- distilabel
- rlaif
---

<p align="left">
  <a href="https://github.com/argilla-io/distilabel">
    <img src="https://raw.githubusercontent.com/argilla-io/distilabel/main/docs/assets/distilabel-badge-light.png" alt="Built with Distilabel" width="200" height="32"/>
  </a>
</p>

# Dataset Card for therapod-dpo

This dataset has been created with [distilabel](https://distilabel.argilla.io/).



## Dataset Summary

This dataset contains a `pipeline.yaml` which can be used to reproduce the pipeline that generated it in distilabel using the `distilabel` CLI:

```console
distilabel pipeline run --config "https://huggingface.co/datasets/Lumiiree/therapod-dpo/raw/main/pipeline.yaml"
```

or explore the configuration:

```console
distilabel pipeline info --config "https://huggingface.co/datasets/Lumiiree/therapod-dpo/raw/main/pipeline.yaml"
```

## Dataset structure

The examples have the following structure per configuration:


<details><summary> Configuration: default </summary><hr>

```json
{
    "distilabel_metadata": {
        "raw_input_generate-responses": [
            {
                "content": "You are a helpful mental health counselling assistant, please answer the mental health questions based on the patient\u0027s description. \nThe assistant gives helpful, comprehensive, and appropriate answers to the user\u0027s questions. ",
                "role": "user"
            }
        ],
        "raw_input_prometheus": null,
        "raw_output_generate-responses": "Certainly! Let\u0027s proceed with addressing mental health questions based on the patient\u0027s description. To keep the interaction confidential and respectful, I\u0027ll simulate the role of a mental health counselor by providing general, evidence-based advice. Remember, the most important aspect of mental health care is the therapeutic relationship. Feel free to share more about your situation, and we can tailor the advice accordingly.\n\n**User\u0027s Description:**\n\nI\u0027ve been feeling like I\u0027m under a lot of pressure lately. I find it hard to manage my emotions, and I\u0027m feeling really stressed out. Sometimes, it feels",
        "raw_output_prometheus": null
    },
    "feedback": null,
    "generation": null,
    "generation_models": [
        "01-ai/Yi-1.5-6B-chat"
    ],
    "generations": [
        "Certainly! Let\u0027s proceed with addressing mental health questions based on the patient\u0027s description. To keep the interaction confidential and respectful, I\u0027ll simulate the role of a mental health counselor by providing general, evidence-based advice. Remember, the most important aspect of mental health care is the therapeutic relationship. Feel free to share more about your situation, and we can tailor the advice accordingly.\n\n**User\u0027s Description:**\n\nI\u0027ve been feeling like I\u0027m under a lot of pressure lately. I find it hard to manage my emotions, and I\u0027m feeling really stressed out. Sometimes, it feels"
    ],
    "input": "I\u0027ve been struggling with my mental health for a while now, and I can\u0027t seem to find a way to cope with it. I\u0027ve tried visualization, positive thinking, and even medication, but nothing seems to work. I\u0027ve been feeling lost and helpless, and I don\u0027t know what to do next. My mind is a whirlwind of thoughts and emotions, and I can\u0027t seem to make sense of it all. I feel like I\u0027m drowning in a sea of confusion, and I can\u0027t seem to find my way out.",
    "instruction": null,
    "model_name": null,
    "output": "I understand that you\u0027ve been dealing with a sense of confusion and chaos in your thoughts and emotions for some time now. It\u0027s been a challenging journey, and it\u0027s commendable that you\u0027ve tried various approaches like visualization, positive thinking, and medication to manage your symptoms. However, it\u0027s clear that these methods haven\u0027t been effective for you. It\u0027s essential to acknowledge that mental health issues can be complex and multifaceted, and what works for one person might not work for another. Today, we\u0027re going to approach this differently. We\u0027re going to identify a specific concern related to your mental health that you\u0027d like to work on, and we\u0027ll break it down into manageable steps. We\u0027ll define the problem as a feeling of being overwhelmed by your thoughts and emotions, and we\u0027ll set realistic goals for managing this feeling. We\u0027ll explore the root causes of this confusion, such as past traumas, current stressors, and any underlying psychological conditions. We\u0027ll also examine your thought patterns and emotional responses to these triggers, and we\u0027ll develop strategies to challenge and reframe negative thoughts. This process is called Cognitive Behavioral Therapy (CBT), and it\u0027s designed to help you face your challenges more effectively by changing the way you think and feel about them. Let\u0027s begin by discussing the specific incidents or concerns that have been contributing to your feelings of confusion and chaos. We can explore these further and come up with strategies to help you manage them.",
    "result": null
}
```

This subset can be loaded as:

```python
from datasets import load_dataset

ds = load_dataset("Lumiiree/therapod-dpo", "default")
```

Or simply as it follows, since there's only one configuration and is named `default`: 

```python
from datasets import load_dataset

ds = load_dataset("Lumiiree/therapod-dpo")
```


</details>





## References


```
@misc{kim2024prometheus2opensource,
    title={Prometheus 2: An Open Source Language Model Specialized in Evaluating Other Language Models},
    author={Seungone Kim and Juyoung Suk and Shayne Longpre and Bill Yuchen Lin and Jamin Shin and Sean Welleck and Graham Neubig and Moontae Lee and Kyungjae Lee and Minjoon Seo},
    year={2024},
    eprint={2405.01535},
    archivePrefix={arXiv},
    primaryClass={cs.CL},
    url={https://arxiv.org/abs/2405.01535},
}
```


