---
language:
- en
tags:
- emotion-classification
- dialogue
- roberta
datasets:
- emowoz
metrics:
- f1
- precision
- recall
license: mit
---

# EmoWOZ Emotion Classifier (RoBERTa)

Fine-tuned RoBERTa-base for emotion classification in dialogue systems.

## Model Details

- **Base Model:** roberta-base (125M parameters)
- **Task:** 7-class emotion classification
- **Training Data:** EmoWOZ + DialMAGE (66k+ dialogue utterances)
- **Loss Function:** Focal Loss (γ=2.0) for class imbalance

## Performance (Test Set)

| Metric | Score |
|--------|-------|
| Accuracy | 0.848 |
| Macro-F1 | 0.669 |

### Per-Class F1
- neutral: 0.8882 (6014 samples)
- satisfied: 0.8277 (1817 samples)
- dissatisfied: 0.6931 (604 samples)
- apologetic: 0.7089 (73 samples)
- abusive: 0.7857 (17 samples)
- excited: 0.4310 (91 samples)
- fearful: 0.3500 (18 samples)

## Usage

Please download or copy `inference.py` in this repo to run this model.

## Citation
Citations for the original EmoWOZ dataset and this fine-tune model are linked below:
```bibtex
@inproceedings{feng-etal-2022-emowoz,
    title = "{E}mo{WOZ}: A Large-Scale Corpus and Labelling Scheme for Emotion Recognition in Task-Oriented Dialogue Systems",
    author = "Feng, Shutong and Lubis, Nurul and Geishauser, Christian and Lin, Hsien-chin and Heck, Michael and van Niekerk, Carel and Gasic, Milica",
    booktitle = "Proceedings of the Thirteenth Language Resources and Evaluation Conference",
    year = "2022",
    url = "https://aclanthology.org/2022.lrec-1.436",
}

@misc{emowoz-roberta-emotion,
    title = {EmoWOZ RoBERTa Emotion Classifier},
    author = {joshthoo},
    year = {2026},
    publisher = {Hugging Face},
    howpublished = {\url{https://huggingface.co/joshthoo/RoBERTa-EmoWOZ}},
}
```