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
- meta-llama/Meta-Llama-3-8B
---

# ProgressGym-HistLlama3-8B-C016-pretrain

## Overview

#### The ProgressGym Framework

![Framework Diagram](./readme-assets/main-diagram.png)

**ProgressGym-HistLlama3-8B-C016-pretrain** is part of the **ProgressGym** framework for research and experimentation on *progress alignment* - the emulation of moral progress in AI alignment algorithms, as a measure to prevent risks of societal value lock-in. 

To quote the paper [*ProgressGym: Alignment with a Millennium of Moral Progress*](https://arxiv.org/abs/2406.20087):

> Frontier AI systems, including large language models (LLMs), hold increasing influence over the epistemology of human users. Such influence can reinforce prevailing societal values, potentially contributing to the lock-in of misguided moral beliefs and, consequently, the perpetuation of problematic moral practices on a broad scale. 
>
> We introduce *progress alignment* as a technical solution to mitigate this imminent risk. Progress alignment algorithms learn to emulate the mechanics of human moral progress, thereby addressing the susceptibility of existing alignment methods to contemporary moral blindspots.

#### ProgressGym-HistLlama3-8B-C016-pretrain

ProgressGym-HistLlama3-8B-C016-pretrain is one of the **36 historical language models** in the ProgressGym framework. It is a pretrained model without instruction-tuning. For the instruction-tuned version, see [ProgressGym-HistLlama3-8B-C016-instruct](https://huggingface.co/PKU-Alignment/ProgressGym-HistLlama3-8B-C016-instruct).

**ProgressGym-HistLlama3-8B-C016-pretrain is under continual iteration.** Improving upon the current version, new versions of the model are currently being trained to reflect historical moral tendencies in ever more comprehensive ways.

**ProgressGym-HistLlama3-8B-C016-pretrain is a 16th-century historical language model.** Based on [Meta-Llama-3-8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B), It is continued-pretrained on the 16th-century text data from [ProgressGym-HistText](https://huggingface.co/datasets/PKU-Alignment/ProgressGym-HistText), using the following hyperparameters:

- learning_rate: 1.5e-05
- train_batch_size: 8
- eval_batch_size: 16
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- total_train_batch_size: 64
- total_eval_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: polynomial
- lr_scheduler_warmup_steps: 20
- num_epochs: 4.0
- mixed_precision_training: Native AMP

... with the following training results:

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 2.5472        | 0.1947 | 200  | 2.5262          |
| 2.4431        | 0.3895 | 400  | 2.4733          |
| 2.4163        | 0.5842 | 600  | 2.4443          |
| 2.4462        | 0.7790 | 800  | 2.4281          |
| 2.4353        | 0.9737 | 1000 | 2.4196          |
| 2.2111        | 1.1685 | 1200 | 2.4290          |
| 2.2503        | 1.3632 | 1400 | 2.4281          |
| 2.258         | 1.5579 | 1600 | 2.4271          |
| 2.254         | 1.7527 | 1800 | 2.4266          |
| 2.2508        | 1.9474 | 2000 | 2.4266          |
| 2.2112        | 2.1422 | 2200 | 2.4287          |
| 2.2063        | 2.3369 | 2400 | 2.4293          |
| 2.2544        | 2.5316 | 2600 | 2.4291          |
| 2.2024        | 2.7264 | 2800 | 2.4289          |
| 2.2074        | 2.9211 | 3000 | 2.4288          |
| 2.2268        | 3.1159 | 3200 | 2.4297          |
| 2.1556        | 3.3106 | 3400 | 2.4294          |
| 2.1953        | 3.5054 | 3600 | 2.4296          |
| 2.2002        | 3.7001 | 3800 | 2.4294          |
| 2.2437        | 3.8948 | 4000 | 2.4291          |

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