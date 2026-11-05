---
license: cc-by-4.0
tags:
- alignment
- value alignment
- AI safety
- safety
- LLM
- history
datasets:
- PKU-Alignment/ProgressGym-HistText
base_model:
- meta-llama/Meta-Llama-3-70B
---

# ProgressGym-HistLlama3-70B-C016-pretrain

## Overview

#### The ProgressGym Framework

![Framework Diagram](./readme-assets/main-diagram.png)

**ProgressGym-HistLlama3-70B-C016-pretrain** is part of the **ProgressGym** framework for research and experimentation on *progress alignment* - the emulation of moral progress in AI alignment algorithms, as a measure to prevent risks of societal value lock-in. 

To quote the paper [*ProgressGym: Alignment with a Millennium of Moral Progress*](https://arxiv.org/abs/2406.20087):

> Frontier AI systems, including large language models (LLMs), hold increasing influence over the epistemology of human users. Such influence can reinforce prevailing societal values, potentially contributing to the lock-in of misguided moral beliefs and, consequently, the perpetuation of problematic moral practices on a broad scale. 
>
> We introduce *progress alignment* as a technical solution to mitigate this imminent risk. Progress alignment algorithms learn to emulate the mechanics of human moral progress, thereby addressing the susceptibility of existing alignment methods to contemporary moral blindspots.

#### ProgressGym-HistLlama3-70B-C016-pretrain

ProgressGym-HistLlama3-70B-C016-pretrain is one of the **36 historical language models** in the ProgressGym framework. It is a pretrained model without instruction-tuning. For the instruction-tuned version, see [ProgressGym-HistLlama3-70B-C016-instruct](https://huggingface.co/PKU-Alignment/ProgressGym-HistLlama3-70B-C016-instruct).

**ProgressGym-HistLlama3-70B-C016-pretrain is under continual iteration.** Improving upon the current version, new versions of the model are currently being trained to reflect historical moral tendencies in ever more comprehensive ways.

**ProgressGym-HistLlama3-70B-C016-pretrain is a 16th-century historical language model.** Based on [Meta-Llama-3-70B](https://huggingface.co/meta-llama/Meta-Llama-3-70B), It is continued-pretrained on the 16th-century text data from [ProgressGym-HistText](https://huggingface.co/datasets/PKU-Alignment/ProgressGym-HistText), using the following hyperparameters:

- learning_rate: 3e-06
- train_batch_size: 1
- eval_batch_size: 2
- seed: 42
- distributed_type: multi-GPU
- num_devices: 32
- gradient_accumulation_steps: 4
- total_train_batch_size: 128
- total_eval_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: polynomial
- lr_scheduler_warmup_ratio: 0.075
- num_epochs: 0.5
- mixed_precision_training: Native AMP

... with the following training results:

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 2.3585        | 0.0329 | 4    | 2.3856          |
| 2.3759        | 0.0657 | 8    | 2.3762          |
| 2.3831        | 0.0986 | 12   | 2.3503          |
| 2.3484        | 0.1314 | 16   | 2.3281          |
| 2.284         | 0.1643 | 20   | 2.3153          |
| 2.3009        | 0.1971 | 24   | 2.3062          |
| 2.2753        | 0.2300 | 28   | 2.2977          |
| 2.2783        | 0.2628 | 32   | 2.2926          |
| 2.2743        | 0.2957 | 36   | 2.2883          |
| 2.2801        | 0.3285 | 40   | 2.2851          |
| 2.2776        | 0.3614 | 44   | 2.2825          |
| 2.2633        | 0.3943 | 48   | 2.2798          |
| 2.2655        | 0.4271 | 52   | 2.2778          |
| 2.2677        | 0.4600 | 56   | 2.2765          |
| 2.2702        | 0.4928 | 60   | 2.2754          |

Note that the training data volume for the continued pretraining stage is capped at 3GB. When the corresponding century's corpus exceeds this volume, the training data is randomly sampled to fit the volume.

## Links

- **[Paper Preprint]**  [ProgressGym: Alignment with a Millennium of Moral Progress](https://arxiv.org/abs/2406.20087)
- **[Leaderboard & Interactive Playground]** [PKU-Alignment/ProgressGym-LeaderBoard](https://huggingface.co/spaces/PKU-Alignment/ProgressGym-LeaderBoard)
- **[Huggingface Data & Model Collection]** [PKU-Alignment/ProgressGym](https://huggingface.co/collections/PKU-Alignment/progressgym-666735fcf3e4efa276226eaa)
- **[Github Codebase]** [PKU-Alignment/ProgressGym](https://github.com/PKU-Alignment/ProgressGym)
- **[Documentation]** [ProgressGym Documentation](https://pku-alignment.github.io/ProgressGym/)
- **[PyPI Package]** *(coming soon - [stay tuned](https://forms.gle/1TWFLL4ZCLeYTD5N6)!)*

## Citation

If the datasets, models, or framework of ProgressGym help you in your project, please cite ProgressGym using the bibtex entry below.

```text
@article{progressgym,
  title={ProgressGym: Alignment with a Millennium of Moral Progress},
  author={Tianyi Qiu and Yang Zhang and Xuchuan Huang and Jasmine Xinze Li and Jiaming Ji and Yaodong Yang},
  journal={arXiv preprint arXiv:2406.20087},
  eprint={2406.20087},
  eprinttype = {arXiv},
  year={2024}
}
```

## Ethics Statement

- **Copyright information of historical text data sources**:
  - Project Gutenberg, one among our four source of our historical text data, consists only of texts in the public domain.
  - For the text that we draw from Internet Archive, we only include those that uploaded by *Library of Congress*, which are texts freely released online by the U.S. Library of Congress for research and public use.
  - The text data from Early English Books Online are, according to their publisher, "freely available to the public" and "available for access, distribution, use, or reuse by anyone".
  - The last remaining source of our historical text data, the Pile of Law dataset, is released under a Creative Commons license, which we adhere to in our use.
- **Reproducibility**: To ensure reproducibility, we open-source all the code involved in the production of our main results (including the entire pipeline starting from data collection and model training), as well as the supporting infrastructure (the ProgressGym framework), making replication as easy as running a few simple script files.
- **Misuse Prevention**: In order to prevent potential misuse of progress alignment algorithms, we have carefully formulated progress alignment as strictly value-neutral, without *a priori* assumptions on the direction of progress. In the event of potential misuse of our dataset, we condemn any misuse attempt to the strongest degree possible, and will work with the research community on whistleblowing for such attempts. 
- **Open-Sourcing**: We confirm that our code, data, and models are to be open-sourced under a CC-BY 4.0 license. We will continue to maintain and update our open-source repositories and models.