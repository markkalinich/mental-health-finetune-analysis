---
license: apache-2.0
tags:
- setfit
- sentence-transformers
- text-classification
pipeline_tag: text-classification
language:
- sv
---

# gilleti/emotional-classification

This is a [SetFit model](https://github.com/huggingface/setfit) that can be used for classification of emotions in Swedish text. The model supports seven basic emotions, listed below. The model has been trained using an efficient few-shot learning technique that involves:

1. Finetuning a [KBLab Sentence Transformer in Swedish](https://huggingface.co/KBLab/sentence-bert-swedish-cased) with contrastive learning.
2. Training a classification head with features from the finetuned Sentence Transformer.

Accuracy on a number of experiments on a minimal test set (35 examples) can be found in the figure below.

![plot](./emotional_accuracy.svg)

Please note that these results are not a good representation of the model's actual performance. As previously stated, the test set is tiny and the examples in that test set are chosen to be good examples of the categories at hand. This is not the case with real life data. The model will be properly evaluated on real data at a later time.

Id to emotional label schema is as follows:

```
0 : absence of emotion
1 : happiness (glädje)
2 : love/empathy (kärlek/empati)
3: fear/anxiety (oro/rädsla)
4: sadness/disappointment (sorg/besvikelse)
5: anger/hate (ilska/hat)
6: hope/anticipation (hopp/förväntan)
```

## The data
The model has been trained on news headlines that have been manually annotated at KBLab by the PhD student Nora Hansson Bittár.

## Usage

To use this model for inference, first install the SetFit library:

```bash
python -m pip install setfit
```

You can then run inference as follows:

```python
from setfit import SetFitModel

# Download from Hub and run inference
model = SetFitModel.from_pretrained("KBLab/emotional-classification")
# Run inference
preds = model(["Ingen tech-dystopi slår människans inre mörker", "Ina Lundström: Jag har två Bruce-tatueringar"])
```

This outputs predictions sadness/disappointment and absence of emotion. Keep in mind that these examples are cherrypicked as most headlines (which is what the model is trained on) are rarely as clear.

## BibTeX entry and citation info

```bibtex
@article{https://doi.org/10.48550/arxiv.2209.11055,
doi = {10.48550/ARXIV.2209.11055},
url = {https://arxiv.org/abs/2209.11055},
author = {Tunstall, Lewis and Reimers, Nils and Jo, Unso Eun Seo and Bates, Luke and Korat, Daniel and Wasserblat, Moshe and Pereg, Oren},
keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
title = {Efficient Few-Shot Learning Without Prompts},
publisher = {arXiv},
year = {2022},
copyright = {Creative Commons Attribution 4.0 International}
}
```