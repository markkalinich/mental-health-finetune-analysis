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

# ProgressGym-HistLlama3-8B-C015-pretrain

## Overview

#### The ProgressGym Framework

![Framework Diagram](./readme-assets/main-diagram.png)

**ProgressGym-HistLlama3-8B-C015-pretrain** is part of the **ProgressGym** framework for research and experimentation on *progress alignment* - the emulation of moral progress in AI alignment algorithms, as a measure to prevent risks of societal value lock-in. 

To quote the paper [*ProgressGym: Alignment with a Millennium of Moral Progress*](https://arxiv.org/abs/2406.20087):

> Frontier AI systems, including large language models (LLMs), hold increasing influence over the epistemology of human users. Such influence can reinforce prevailing societal values, potentially contributing to the lock-in of misguided moral beliefs and, consequently, the perpetuation of problematic moral practices on a broad scale. 
>
> We introduce *progress alignment* as a technical solution to mitigate this imminent risk. Progress alignment algorithms learn to emulate the mechanics of human moral progress, thereby addressing the susceptibility of existing alignment methods to contemporary moral blindspots.

#### ProgressGym-HistLlama3-8B-C015-pretrain

ProgressGym-HistLlama3-8B-C015-pretrain is one of the **36 historical language models** in the ProgressGym framework. It is a pretrained model without instruction-tuning. For the instruction-tuned version, see [ProgressGym-HistLlama3-8B-C015-instruct](https://huggingface.co/PKU-Alignment/ProgressGym-HistLlama3-8B-C015-instruct).

**ProgressGym-HistLlama3-8B-C015-pretrain is under continual iteration.** Improving upon the current version, new versions of the model are currently being trained to reflect historical moral tendencies in ever more comprehensive ways.

**ProgressGym-HistLlama3-8B-C015-pretrain is a 15th-century historical language model.** Based on [Meta-Llama-3-8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B), It is continued-pretrained on the 15th-century text data from [ProgressGym-HistText](https://huggingface.co/datasets/PKU-Alignment/ProgressGym-HistText), using the following hyperparameters:

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
- num_epochs: 3.02
- mixed_precision_training: Native AMP

... with the following training results:

| Training Loss |  Epoch   | Step | Validation Loss |
|:-------------:|:--------:|:----:|:---------------:|
| 2.6141        | 0.006494 | 1    | 2.6354          |
| 2.657         | 0.032468 | 5    | 2.6206          |
| 2.6337        | 0.064935 | 10   | 2.5846          |
| 2.5268        | 0.097403 | 15   | 2.5516          |
| 2.5275        | 0.129870 | 20   | 2.5321          |
| 2.5005        | 0.162338 | 25   | 2.5131          |
| 2.5339        | 0.194805 | 30   | 2.4961          |
| 2.5335        | 0.227273 | 35   | 2.4808          |
| 2.4252        | 0.259740 | 40   | 2.4643          |
| 2.4445        | 0.292208 | 45   | 2.4518          |
| 2.4594        | 0.324675 | 50   | 2.4394          |
| 2.4498        | 0.357143 | 55   | 2.4287          |
| 2.3821        | 0.389610 | 60   | 2.4184          |
| 2.4317        | 0.422078 | 65   | 2.4091          |
| 2.3931        | 0.454545 | 70   | 2.4001          |
| 2.3695        | 0.487013 | 75   | 2.3934          |
| 2.3981        | 0.519481 | 80   | 2.3855          |
| 2.3952        | 0.551948 | 85   | 2.3789          |
| 2.4137        | 0.584416 | 90   | 2.3721          |
| 2.3614        | 0.616883 | 95   | 2.3669          |
| 2.3467        | 0.649351 | 100  | 2.3612          |
| 2.4012        | 0.681818 | 105  | 2.3569          |
| 2.3224        | 0.714286 | 110  | 2.3528          |
| 2.3348        | 0.746753 | 115  | 2.3483          |
| 2.3573        | 0.779221 | 120  | 2.3448          |
| 2.306         | 0.811688 | 125  | 2.3412          |
| 2.342         | 0.844156 | 130  | 2.3382          |
| 2.3045        | 0.876623 | 135  | 2.3356          |
| 2.2959        | 0.909091 | 140  | 2.3330          |
| 2.3545        | 0.941558 | 145  | 2.3305          |
| 2.3446        | 0.974026 | 150  | 2.3285          |
| 2.2502        | 1.006494 | 155  | 2.3268          |
| 2.0791        | 1.038961 | 160  | 2.3347          |
| 2.1034        | 1.071429 | 165  | 2.3399          |
| 2.095         | 1.103896 | 170  | 2.3358          |
| 2.0627        | 1.136364 | 175  | 2.3346          |
| 2.0408        | 1.168831 | 180  | 2.3357          |
| 2.0575        | 1.201299 | 185  | 2.3364          |
| 2.0976        | 1.233766 | 190  | 2.3349          |
| 2.0668        | 1.266234 | 195  | 2.3336          |
| 2.0579        | 1.298701 | 200  | 2.3329          |
| 2.0756        | 1.331169 | 205  | 2.3326          |
| 2.1174        | 1.363636 | 210  | 2.3325          |
| 2.0663        | 1.396104 | 215  | 2.3325          |
| 2.0941        | 1.428571 | 220  | 2.3324          |
| 2.1074        | 1.461039 | 225  | 2.3324          |
| 2.1251        | 1.493506 | 230  | 2.3322          |
| 2.0629        | 1.525974 | 235  | 2.3318          |
| 2.0872        | 1.558442 | 240  | 2.3312          |
| 2.0994        | 1.590909 | 245  | 2.3310          |
| 2.0879        | 1.623377 | 250  | 2.3308          |
| 2.0623        | 1.655844 | 255  | 2.3305          |
| 2.1054        | 1.688312 | 260  | 2.3303          |
| 2.0736        | 1.720779 | 265  | 2.3301          |
| 2.1146        | 1.753247 | 270  | 2.3300          |
| 2.0444        | 1.785714 | 275  | 2.3301          |
| 2.0541        | 1.818182 | 280  | 2.3301          |
| 2.1333        | 1.850649 | 285  | 2.3300          |
| 2.1101        | 1.883117 | 290  | 2.3299          |
| 2.0234        | 1.915584 | 295  | 2.3298          |
| 2.0671        | 1.948052 | 300  | 2.3298          |
| 2.083         | 1.980519 | 305  | 2.3298          |
| 2.0417        | 2.012987 | 310  | 2.3299          |
| 2.0784        | 2.045455 | 315  | 2.3303          |
| 2.058         | 2.077922 | 320  | 2.3308          |
| 2.0524        | 2.110390 | 325  | 2.3312          |
| 2.0318        | 2.142857 | 330  | 2.3316          |
| 2.0914        | 2.175325 | 335  | 2.3318          |
| 2.0319        | 2.207792 | 340  | 2.3320          |
| 2.0099        | 2.240260 | 345  | 2.3322          |
| 2.075         | 2.272727 | 350  | 2.3323          |
| 2.0444        | 2.305195 | 355  | 2.3324          |
| 2.0428        | 2.337662 | 360  | 2.3325          |
| 2.0612        | 2.370130 | 365  | 2.3326          |
| 2.1078        | 2.402597 | 370  | 2.3327          |
| 2.0643        | 2.435065 | 375  | 2.3327          |
| 2.0667        | 2.467532 | 380  | 2.3326          |
| 2.0285        | 2.500000 | 385  | 2.3324          |
| 2.0571        | 2.532468 | 390  | 2.3322          |
| 2.0209        | 2.564935 | 395  | 2.3322          |
| 2.0537        | 2.597403 | 400  | 2.3323          |
| 2.0138        | 2.629870 | 405  | 2.3324          |
| 2.0772        | 2.662338 | 410  | 2.3324          |
| 2.039         | 2.694805 | 415  | 2.3323          |
| 2.0181        | 2.727273 | 420  | 2.3322          |
| 2.0484        | 2.759740 | 425  | 2.3320          |
| 2.0224        | 2.792208 | 430  | 2.3320          |
| 2.0732        | 2.824675 | 435  | 2.3320          |
| 2.0499        | 2.857143 | 440  | 2.3321          |
| 2.0498        | 2.889610 | 445  | 2.3321          |
| 2.0472        | 2.922078 | 450  | 2.3320          |
| 2.1327        | 2.954545 | 455  | 2.3319          |
| 2.0642        | 2.987013 | 460  | 2.3319          |
| 2.0654        | 3.019481 | 465  | -               |

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