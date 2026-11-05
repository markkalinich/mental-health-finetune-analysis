---
language: es
tags:
- T5
- Seq2Seq
- EconderDecoder
- Spanish
datasets:
 - large_spanish_corpus
widgets:
- text: "Érase un vez un"

license: mit

---
# Spanish T5 (small) trained on [large_spanish_corpus](https://huggingface.co/datasets/viewer/?dataset=large_spanish_corpus).

This is a Spanish **T5** (small arch) trained from scratch on the [large_spanish_corpus](https://huggingface.co/datasets/viewer/?dataset=large_spanish_corpus) aka BETO's corpus with [Flax](https://github.com/google/flax)

This is part of the
[Flax/Jax Community Week](https://discuss.huggingface.co/t/open-to-the-community-community-week-using-jax-flax-for-nlp-cv/7104), organised by [HuggingFace](https://huggingface.co/) and TPU usage sponsored by Google.
## Dataset
The dataset is about 20 GB. 95% of the data was used for training and the rest 5% for validation.

## [Metrics](https://huggingface.co/flax-community/spanish-t5-small/tensorboard) (on evaluation dataset)

- Accuracy: 0.675


## Team members
- Manuel Romero ([mrm8488](https://huggingface.co/mrm8488))
- María Grandury ([mariagrandury](https://huggingface.co/mariagrandury))

## Citation
If you want to cite this model you can use this:

```bibtex
@misc{mromero2021spanish-t5-small,
  title={Spanish T5 (small) by Manuel Romero},
  author={Romero, Manuel},
  publisher={Hugging Face},
  journal={Hugging Face Hub},
  howpublished={\url{https://huggingface.co/flax-community/spanish-t5-small}},
  year={2021}
}
```