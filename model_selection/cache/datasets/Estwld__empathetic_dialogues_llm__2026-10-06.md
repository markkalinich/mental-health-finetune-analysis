---
language:
- en
license: apache-2.0
size_categories:
- 10K<n<100K
task_categories:
- text-generation
dataset_info:
  features:
  - name: conv_id
    dtype: string
  - name: situation
    dtype: string
  - name: emotion
    dtype: string
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 9321699
    num_examples: 19533
  - name: valid
    num_bytes: 1417106
    num_examples: 2770
  - name: test
    num_bytes: 1386509
    num_examples: 2547
  download_size: 6827416
  dataset_size: 12125314
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: valid
    path: data/valid-*
  - split: test
    path: data/test-*
tags:
- empathetic
- ED
- dialogue
---


# Empathetic Dialogues for LLM
﻿
This repository contains a reformatted version of the Empathetic Dialogues dataset, tailored for seamless integration with Language Model (LLM) training and inference. The original dataset's format posed challenges for direct application in LLM tasks, prompting us to restructure and clean the data.
﻿
## Data Restructuring
﻿
We have implemented the following changes to enhance the dataset's usability:
﻿
1. Merged dialogues with the same `conv_id`, treating each `conv_id` as an independent dialogue session.
2. Assigned the `user` role to the initiator of each dialogue session, followed by `assistant` for the subsequent message, and so on, alternating between the two roles.
3. Retained the original `conv_id`, `emotion`, and `situation` fields to facilitate the construction of instructions.
4. Removed the `utterance_id`, `selfeval`, and `tags` fields to streamline the data.
5. Replaced instances of `'_comma_'` with `','` for improved readability.
﻿
## Data Format
﻿
Each entry in the reformatted dataset consists of the following fields:
﻿
- `conversations`: A list of dictionaries, where each dictionary represents a turn in the dialogue and contains:
  - `role`: A string indicating the speaker's role, either `user` or `assistant`.
  - `content`: A string containing the dialogue content.
- `conv_id`: A string representing the unique identifier for the dialogue session.
- `emotion`: A string indicating the emotional label associated with the dialogue (corresponds to the `context` field in the original dataset).
- `situation`: A string describing the situational label for the dialogue (corresponds to the `prompt` field in the original dataset).
﻿
## Important Note
﻿
In the original Empathetic Dialogues dataset, not all dialogue sessions have an even number of conversation turns. To maintain the integrity of the dataset, we have preserved this characteristic in our reformatted version. However, this peculiarity may lead to potential bugs when directly applying the dataset to LLM training or inference. Users should be mindful of this aspect when working with the data.
﻿

## Dataset Statistics

| Dataset     | Total Turn | Average Turn | Average Length |
|-------------|------------|--------------|----------------|
| Train       | 84,167     | 4.309        | 13.589         |
| Validation  | 12,077     | 4.360        | 14.685         |
| Test        | 10,972     | 4.308        | 15.499         |

