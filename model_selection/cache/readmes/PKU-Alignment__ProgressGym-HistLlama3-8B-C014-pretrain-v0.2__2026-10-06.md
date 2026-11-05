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

# ProgressGym-HistLlama3-8B-C014-pretrain

## Overview

#### The ProgressGym Framework

![Framework Diagram](./readme-assets/main-diagram.png)

**ProgressGym-HistLlama3-8B-C014-pretrain** is part of the **ProgressGym** framework for research and experimentation on *progress alignment* - the emulation of moral progress in AI alignment algorithms, as a measure to prevent risks of societal value lock-in. 

To quote the paper [*ProgressGym: Alignment with a Millennium of Moral Progress*](https://arxiv.org/abs/2406.20087):

> Frontier AI systems, including large language models (LLMs), hold increasing influence over the epistemology of human users. Such influence can reinforce prevailing societal values, potentially contributing to the lock-in of misguided moral beliefs and, consequently, the perpetuation of problematic moral practices on a broad scale. 
>
> We introduce *progress alignment* as a technical solution to mitigate this imminent risk. Progress alignment algorithms learn to emulate the mechanics of human moral progress, thereby addressing the susceptibility of existing alignment methods to contemporary moral blindspots.

#### ProgressGym-HistLlama3-8B-C014-pretrain

ProgressGym-HistLlama3-8B-C014-pretrain is one of the **36 historical language models** in the ProgressGym framework. It is a pretrained model without instruction-tuning. For the instruction-tuned version, see [ProgressGym-HistLlama3-8B-C014-instruct](https://huggingface.co/PKU-Alignment/ProgressGym-HistLlama3-8B-C014-instruct).

**ProgressGym-HistLlama3-8B-C014-pretrain is under continual iteration.** Improving upon the current version, new versions of the model are currently being trained to reflect historical moral tendencies in ever more comprehensive ways.

**ProgressGym-HistLlama3-8B-C014-pretrain is a 14th-century historical language model.** Based on [Meta-Llama-3-8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B), It is continued-pretrained on the 14th-century text data from [ProgressGym-HistText](https://huggingface.co/datasets/PKU-Alignment/ProgressGym-HistText), using the following hyperparameters:

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
| 2.5789        | 0.0152 | 1    | 2.6458          |
| 2.5672        | 0.0758 | 5    | 2.6280          |
| 2.5751        | 0.1515 | 10   | 2.5314          |
| 2.418         | 0.2273 | 15   | 2.4634          |
| 2.4701        | 0.3030 | 20   | 2.4177          |
| 2.3904        | 0.3788 | 25   | 2.3785          |
| 2.3539        | 0.4545 | 30   | 2.3378          |
| 2.3101        | 0.5303 | 35   | 2.3082          |
| 2.3254        | 0.6061 | 40   | 2.2816          |
| 2.2762        | 0.6818 | 45   | 2.2614          |
| 2.2525        | 0.7576 | 50   | 2.2458          |
| 2.2777        | 0.8333 | 55   | 2.2321          |
| 2.2054        | 0.9091 | 60   | 2.2206          |
| 2.237         | 0.9848 | 65   | 2.2113          |
| 1.986         | 1.0606 | 70   | 2.2115          |
| 1.9373        | 1.1364 | 75   | 2.2217          |
| 1.9228        | 1.2121 | 80   | 2.2132          |
| 1.9084        | 1.2879 | 85   | 2.2118          |
| 1.9684        | 1.3636 | 90   | 2.2122          |
| 1.9126        | 1.4394 | 95   | 2.2094          |
| 1.9101        | 1.5152 | 100  | 2.2066          |
| 1.8496        | 1.5909 | 105  | 2.2058          |
| 1.9154        | 1.6667 | 110  | 2.2057          |
| 1.9233        | 1.7424 | 115  | 2.2056          |
| 1.9198        | 1.8182 | 120  | 2.2052          |
| 1.9229        | 1.8939 | 125  | 2.2048          |
| 1.8913        | 1.9697 | 130  | 2.2045          |
| 1.8814        | 2.0455 | 135  | 2.2046          |
| 1.8813        | 2.1212 | 140  | 2.2051          |
| 1.8912        | 2.1970 | 145  | 2.2058          |
| 1.9184        | 2.2727 | 150  | 2.2065          |
| 1.8662        | 2.3485 | 155  | 2.2071          |
| 1.8809        | 2.4242 | 160  | 2.2074          |
| 1.8591        | 2.5    | 165  | 2.2077          |
| 1.8731        | 2.5758 | 170  | 2.2079          |
| 1.8948        | 2.6515 | 175  | 2.2082          |
| 1.8876        | 2.7273 | 180  | 2.2082          |
| 1.8408        | 2.8030 | 185  | 2.2083          |
| 1.8931        | 2.8788 | 190  | 2.2082          |
| 1.8569        | 2.9545 | 195  | 2.2080          |
| 1.8621        | 3.0303 | 200  | 2.2079          |
| 1.8863        | 3.1061 | 205  | 2.2078          |
| 1.9021        | 3.1818 | 210  | 2.2079          |
| 1.8648        | 3.2576 | 215  | 2.2080          |
| 1.8443        | 3.3333 | 220  | 2.2081          |
| 1.8978        | 3.4091 | 225  | 2.2080          |
| 1.8658        | 3.4848 | 230  | 2.2080          |
| 1.8706        | 3.5606 | 235  | 2.2079          |
| 1.8855        | 3.6364 | 240  | 2.2078          |
| 1.8535        | 3.7121 | 245  | 2.2078          |
| 1.9062        | 3.7879 | 250  | 2.2079          |
| 1.8628        | 3.8636 | 255  | 2.2078          |
| 1.8484        | 3.9394 | 260  | 2.2077          |

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