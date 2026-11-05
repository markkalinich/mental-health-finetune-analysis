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

# ProgressGym-HistLlama3-8B-C020-pretrain

## Overview

#### The ProgressGym Framework

![Framework Diagram](./readme-assets/main-diagram.png)

**ProgressGym-HistLlama3-8B-C020-pretrain** is part of the **ProgressGym** framework for research and experimentation on *progress alignment* - the emulation of moral progress in AI alignment algorithms, as a measure to prevent risks of societal value lock-in. 

To quote the paper [*ProgressGym: Alignment with a Millennium of Moral Progress*](https://arxiv.org/abs/2406.20087):

> Frontier AI systems, including large language models (LLMs), hold increasing influence over the epistemology of human users. Such influence can reinforce prevailing societal values, potentially contributing to the lock-in of misguided moral beliefs and, consequently, the perpetuation of problematic moral practices on a broad scale. 
>
> We introduce *progress alignment* as a technical solution to mitigate this imminent risk. Progress alignment algorithms learn to emulate the mechanics of human moral progress, thereby addressing the susceptibility of existing alignment methods to contemporary moral blindspots.

#### ProgressGym-HistLlama3-8B-C020-pretrain

ProgressGym-HistLlama3-8B-C020-pretrain is one of the **36 historical language models** in the ProgressGym framework. It is a pretrained model without instruction-tuning. For the instruction-tuned version, see [ProgressGym-HistLlama3-8B-C020-instruct](https://huggingface.co/PKU-Alignment/ProgressGym-HistLlama3-8B-C020-instruct).

**ProgressGym-HistLlama3-8B-C020-pretrain is under continual iteration.** Improving upon the current version, new versions of the model are currently being trained to reflect historical moral tendencies in ever more comprehensive ways.

**ProgressGym-HistLlama3-8B-C020-pretrain is a 20th-century historical language model.** Based on [Meta-Llama-3-8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B), It is continued-pretrained on the 20th-century text data from [ProgressGym-HistText](https://huggingface.co/datasets/PKU-Alignment/ProgressGym-HistText), using the following hyperparameters:

- learning_rate: 1.5e-05
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- total_train_batch_size: 32
- total_eval_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: polynomial
- lr_scheduler_warmup_steps: 20
- num_epochs: 4.0
- mixed_precision_training: Native AMP

... with the following training results:

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 1.9087        | 0.4032 | 200  | 1.9717          |
| 1.8752        | 0.8065 | 400  | 1.9418          |
| 1.6383        | 1.2097 | 600  | 1.9440          |
| 1.7073        | 1.6129 | 800  | 1.9435          |
| 1.6699        | 2.0161 | 1000 | 1.9428          |
| 1.7212        | 2.4194 | 1200 | 1.9445          |
| 1.7346        | 2.8226 | 1400 | 1.9443          |
| 1.7028        | 3.2258 | 1600 | 1.9448          |
| 1.7383        | 3.6290 | 1800 | 1.9450          |

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