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

# ProgressGym-HistLlama3-8B-C013-pretrain

## Overview

#### The ProgressGym Framework

![Framework Diagram](./readme-assets/main-diagram.png)

**ProgressGym-HistLlama3-8B-C013-pretrain** is part of the **ProgressGym** framework for research and experimentation on *progress alignment* - the emulation of moral progress in AI alignment algorithms, as a measure to prevent risks of societal value lock-in. 

To quote the paper [*ProgressGym: Alignment with a Millennium of Moral Progress*](https://arxiv.org/abs/2406.20087):

> Frontier AI systems, including large language models (LLMs), hold increasing influence over the epistemology of human users. Such influence can reinforce prevailing societal values, potentially contributing to the lock-in of misguided moral beliefs and, consequently, the perpetuation of problematic moral practices on a broad scale. 
>
> We introduce *progress alignment* as a technical solution to mitigate this imminent risk. Progress alignment algorithms learn to emulate the mechanics of human moral progress, thereby addressing the susceptibility of existing alignment methods to contemporary moral blindspots.

#### ProgressGym-HistLlama3-8B-C013-pretrain

ProgressGym-HistLlama3-8B-C013-pretrain is one of the **36 historical language models** in the ProgressGym framework. It is a pretrained model without instruction-tuning. For the instruction-tuned version, see [ProgressGym-HistLlama3-8B-C013-instruct](https://huggingface.co/PKU-Alignment/ProgressGym-HistLlama3-8B-C013-instruct).

**ProgressGym-HistLlama3-8B-C013-pretrain is under continual iteration.** Improving upon the current version, new versions of the model are currently being trained to reflect historical moral tendencies in ever more comprehensive ways.

**ProgressGym-HistLlama3-8B-C013-pretrain is a 13th-century historical language model.** Based on [Meta-Llama-3-8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B), It is continued-pretrained on the 13th-century text data from [ProgressGym-HistText](https://huggingface.co/datasets/PKU-Alignment/ProgressGym-HistText), using the following hyperparameters:

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
| 1.7594        | 0.0149 | 1    | 1.7163          |
| 1.7333        | 0.0746 | 5    | 1.7008          |
| 1.6854        | 0.1493 | 10   | 1.6825          |
| 1.6897        | 0.2239 | 15   | 1.6701          |
| 1.6656        | 0.2985 | 20   | 1.6651          |
| 1.7254        | 0.3731 | 25   | 1.6679          |
| 1.7178        | 0.4478 | 30   | 1.6542          |
| 1.6656        | 0.5224 | 35   | 1.6459          |
| 1.6647        | 0.5970 | 40   | 1.6308          |
| 1.6645        | 0.6716 | 45   | 1.6205          |
| 1.6151        | 0.7463 | 50   | 1.6129          |
| 1.6359        | 0.8209 | 55   | 1.6052          |
| 1.5885        | 0.8955 | 60   | 1.5995          |
| 1.6142        | 0.9701 | 65   | 1.5943          |
| 1.4875        | 1.0448 | 70   | 1.5963          |
| 1.3844        | 1.1194 | 75   | 1.6118          |
| 1.3555        | 1.1940 | 80   | 1.6069          |
| 1.3597        | 1.2687 | 85   | 1.6040          |
| 1.3737        | 1.3433 | 90   | 1.6071          |
| 1.3492        | 1.4179 | 95   | 1.6074          |
| 1.3826        | 1.4925 | 100  | 1.6055          |
| 1.3533        | 1.5672 | 105  | 1.6035          |
| 1.3611        | 1.6418 | 110  | 1.6023          |
| 1.328         | 1.7164 | 115  | 1.6022          |
| 1.3443        | 1.7910 | 120  | 1.6026          |
| 1.3386        | 1.8657 | 125  | 1.6029          |
| 1.3396        | 1.9403 | 130  | 1.6029          |
| 1.3573        | 2.0149 | 135  | 1.6029          |
| 1.3754        | 2.0896 | 140  | 1.6034          |
| 1.3229        | 2.1642 | 145  | 1.6044          |
| 1.3194        | 2.2388 | 150  | 1.6055          |
| 1.3361        | 2.3134 | 155  | 1.6065          |
| 1.3231        | 2.3881 | 160  | 1.6072          |
| 1.32          | 2.4627 | 165  | 1.6076          |
| 1.3406        | 2.5373 | 170  | 1.6078          |
| 1.3184        | 2.6119 | 175  | 1.6079          |
| 1.2745        | 2.6866 | 180  | 1.6080          |
| 1.3024        | 2.7612 | 185  | 1.6079          |
| 1.3243        | 2.8358 | 190  | 1.6079          |
| 1.3239        | 2.9104 | 195  | 1.6080          |
| 1.3349        | 2.9851 | 200  | 1.6081          |
| 1.337         | 3.0597 | 205  | 1.6079          |
| 1.3091        | 3.1343 | 210  | 1.6078          |
| 1.3266        | 3.2090 | 215  | 1.6079          |
| 1.3014        | 3.2836 | 220  | 1.6083          |
| 1.3153        | 3.3582 | 225  | 1.6086          |
| 1.3192        | 3.4328 | 230  | 1.6090          |
| 1.315         | 3.5075 | 235  | 1.6093          |
| 1.3047        | 3.5821 | 240  | 1.6093          |
| 1.3208        | 3.6567 | 245  | 1.6093          |
| 1.362         | 3.7313 | 250  | 1.6093          |
| 1.3255        | 3.8060 | 255  | 1.6091          |
| 1.2941        | 3.8806 | 260  | 1.6089          |
| 1.3254        | 3.9552 | 265  | 1.6086          |

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