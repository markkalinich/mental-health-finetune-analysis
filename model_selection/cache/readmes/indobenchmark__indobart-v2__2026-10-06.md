---
language: id
tags:
- indogpt
- indobenchmark
- indonlg
license: mit
inference: false
datasets:
- Indo4B+
---

# IndoBART-v2 Model

[IndoBART-v2](https://arxiv.org/abs/2104.08200) is a state-of-the-art language model for Indonesian based on the BART model. The pretrained model is trained using the BART training objective.

## All Pre-trained Models

| Model                          | #params                        | Training data                     |
|--------------------------------|--------------------------------|-----------------------------------|
| `indobenchmark/indobart-v2` | 132M   | Indo4B-Plus (26 GB of text)            |

## Authors 

<b>IndoBART</b> was trained and evaluated by Samuel Cahyawijaya*, Genta Indra Winata*, Bryan Wilie*, Karissa Vincentio*, Xiaohong Li*, Adhiguna Kuncoro*, Sebastian Ruder, Zhi Yuan Lim, Syafri Bahar, Masayu Leylia Khodra, Ayu Purwarianti, Pascale Fung


## Citation
If you use our work, please cite:

```bibtex
@article{cahyawijaya2021indonlg,
  title={IndoNLG: Benchmark and Resources for Evaluating Indonesian Natural Language Generation},
  author={Cahyawijaya, Samuel and Winata, Genta Indra and Wilie, Bryan and Vincentio, Karissa and Li, Xiaohong and Kuncoro, Adhiguna and Ruder, Sebastian and Lim, Zhi Yuan and Bahar, Syafri and Khodra, Masayu Leylia and others},
  journal={arXiv preprint arXiv:2104.08200},
  year={2021}
}
```
