---
license: apache-2.0
language: 
  - ind
  - ace
  - ban
  - bjn
  - bug
  - gor
  - jav
  - min
  - msa
  - nia
  - sun
  - tet
language_bcp47:
  - jv-x-bms
datasets:
  - sabilmakbar/indo_wiki
  - acul3/KoPI-NLLB
  - uonlp/CulturaX
tags:
  - bert
---

# NusaBERT Large

[NusaBERT](https://arxiv.org/abs/2403.01817) Large is a multilingual encoder-based language model based on the [BERT](https://arxiv.org/abs/1810.04805) architecture. We conducted continued pre-training on open-source corpora of [sabilmakbar/indo_wiki](https://huggingface.co/datasets/sabilmakbar/indo_wiki), [acul3/KoPI-NLLB](https://huggingface.co/datasets/acul3/KoPI-NLLB), and [uonlp/CulturaX](https://huggingface.co/datasets/uonlp/CulturaX). On a held-out subset of the corpus, our model achieved:

- `eval_accuracy`: 0.7117
- `eval_loss`: 1.3268
- `perplexity`: 3.7690

This model was trained using the [🤗Transformers](https://github.com/huggingface/transformers) PyTorch framework. All training was done on an NVIDIA H100 GPU. [LazarusNLP/NusaBERT-large](https://huggingface.co/LazarusNLP/NusaBERT-large) is released under Apache 2.0 license.

## Model Detail

- **Developed by**: [LazarusNLP](https://lazarusnlp.github.io/)
- **Finetuned from**: [IndoBERT Large p1](https://huggingface.co/indobenchmark/indobert-large-p1)
- **Model type**: Encoder-based BERT language model
- **Language(s)**: Indonesian, Acehnese, Balinese, Banjarese, Buginese, Gorontalo, Javanese, Banyumasan, Minangkabau, Malay, Nias, Sundanese, Tetum
- **License**: [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0.html)
- **Contact**: [LazarusNLP](https://lazarusnlp.github.io/)

## Use in 🤗Transformers

```python
from transformers import AutoTokenizer, AutoModelForMaskedLM

model_checkpoint = "LazarusNLP/NusaBERT-large"

tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model = AutoModelForMaskedLM.from_pretrained(model_checkpoint)
```

## Training Datasets

Around 16B tokens from the following corpora were used during pre-training.

- [Indonesian Wikipedia Data Repository](https://huggingface.co/datasets/sabilmakbar/indo_wiki)
- [KoPI-NLLB (Korpus Perayapan Indonesia)](https://huggingface.co/datasets/acul3/KoPI-NLLB)
- [Cleaned, Enormous, and Public: The Multilingual Fuel to Democratize Large Language Models for 167 Languages](https://huggingface.co/datasets/uonlp/CulturaX)

## Training Hyperparameters

The following hyperparameters were used during training:

- `learning_rate`: 3e-05
- `train_batch_size`: 256
- `eval_batch_size`: 256
- `seed`: 42
- `optimizer`: Adam with `betas=(0.9,0.999)` and `epsilon=1e-08`
- `lr_scheduler_type`: linear
- `lr_scheduler_warmup_steps`: 24000
- `training_steps`: 500000

### Framework versions

- Transformers 4.38.1
- Pytorch 2.2.0+cu118
- Datasets 2.17.1
- Tokenizers 0.15.2

## Credits

NusaBERT Large is developed with love by:

<div style="display: flex;">
<a href="https://github.com/anantoj">
    <img src="https://github.com/anantoj.png" alt="GitHub Profile" style="border-radius: 50%;width: 64px;margin:0 4px;">
</a>

<a href="https://github.com/DavidSamuell">
    <img src="https://github.com/DavidSamuell.png" alt="GitHub Profile" style="border-radius: 50%;width: 64px;margin:0 4px;">
</a>

<a href="https://github.com/stevenlimcorn">
    <img src="https://github.com/stevenlimcorn.png" alt="GitHub Profile" style="border-radius: 50%;width: 64px;margin:0 4px;">
</a>

<a href="https://github.com/w11wo">
    <img src="https://github.com/w11wo.png" alt="GitHub Profile" style="border-radius: 50%;width: 64px;margin:0 4px;">
</a>
</div>

## Citation

```bib
@misc{wongso2024nusabert,
  title={NusaBERT: Teaching IndoBERT to be Multilingual and Multicultural}, 
  author={Wilson Wongso and David Samuel Setiawan and Steven Limcorn and Ananto Joyoadikusumo},
  year={2024},
  eprint={2403.01817},
  archivePrefix={arXiv},
  primaryClass={cs.CL}
}
```