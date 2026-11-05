---
license: mit
language:
- sk
datasets:
- oscar-corpus/OSCAR-2109
pipeline_tag: fill-mask
library_name: transformers
tags:
- slovak-language-model
---

# Slovak BPE Baby Language Model (SK_BPE_BLM)

**SK_BPE_BLM** is a pretrained small language model for the Slovak language, based on the RoBERTa architecture. The model utilizes standard Byte-Pair Encoding (BPE) tokenization (**pureBPE**, more info [here](https://github.com/daviddrzik/Slovak_subword_tokenizers)) and is case-insensitive, meaning it operates in lowercase. While the pretrained model can be used for masked language modeling, it is primarily intended for fine-tuning on downstream NLP tasks.

## How to Use the Model

To use the SK_BPE_BLM model, follow these steps:

```python
from transformers import pipeline, RobertaTokenizer, AutoModelForMaskedLM

# Load the custom tokenizer and model
tokenizer = RobertaTokenizer.from_pretrained("daviddrzik/SK_BPE_BLM")
model = AutoModelForMaskedLM.from_pretrained("daviddrzik/SK_BPE_BLM")

# Create a pipeline with the custom model and tokenizer
unmasker = pipeline('fill-mask', model=model, tokenizer=tokenizer)

# Use the pipeline
result = unmasker("včera večer sme <mask> nový film v kine, ktorý mal premiéru iba pred týždňom.")
print(result)

[{'score': 0.2665567100048065,
  'token': 18599,
  'token_str': ' pozreli',
  'sequence': 'včera večer sme pozreli nový film v kine, ktorý mal premiéru iba pred týždňom.'},
 {'score': 0.23860174417495728,
  'token': 1056,
  'token_str': ' mali',
  'sequence': 'včera večer sme mali nový film v kine, ktorý mal premiéru iba pred týždňom.'},
 {'score': 0.1962040513753891,
  'token': 6915,
  'token_str': ' videli',
  'sequence': 'včera večer sme videli nový film v kine, ktorý mal premiéru iba pred týždňom.'},
 {'score': 0.03656836599111557,
  'token': 26996,
  'token_str': ' pozerali',
  'sequence': 'včera večer sme pozerali nový film v kine, ktorý mal premiéru iba pred týždňom.'},
 {'score': 0.030735589563846588,
  'token': 9058,
  'token_str': ' objavili',
  'sequence': 'včera večer sme objavili nový film v kine, ktorý mal premiéru iba pred týždňom.'}]
```

## Training Data

The `SK_BPE_BLM` model was pretrained using a subset of the OSCAR 2019 corpus, specifically focusing on the Slovak language. The corpus underwent comprehensive preprocessing to ensure the quality and relevance of the data:

- **Language Filtering:** Non-Slovak text was removed to focus solely on the Slovak language.
- **Character Normalization:** Various types of spaces, quotes, dashes, and separators were standardized (e.g., replacing different types of spaces with a single space, or dashes with hyphens). Emoticons were replaced with spaces.
- **Symbol and Unwanted Text Removal:** Sentences containing mathematical symbols, pictograms, or characters from Asian and African languages were deleted. Duplicates of punctuation, special characters, and spaces were also removed.
- **URL and Text Normalization:** All web addresses were removed, and the text was converted to lowercase to simplify tokenization.
- **Content Cleanup:** Text that included irrelevant content from web crawling, such as keywords and HTML tags, was identified and removed.

Additionally, the preprocessing included further refinement steps to create the final dataset:

- **Parentheses Content Removal:** All content within parentheses was removed to reduce noise.
- **Selection of Text Segments:** Medium-length text paragraphs were selected to maintain consistency.
- **Similarity Filtering:** Paragraphs with at least 50% similarity to previous ones were removed to minimize redundancy.
- **Random Sampling:** Finally, 20% of the remaining paragraphs were randomly selected.

After preprocessing, the training corpus consisted of:
- **455 MB of text**
- **895,125 paragraphs**
- **64.6 million words**
- **1.13 million unique words**
- **119 unique characters**

## Pretraining

The `SK_BPE_BLM` model was trained with the following key parameters:

- **Architecture:** Based on RoBERTa, with 6 hidden layers and 12 attention heads.
- **Hidden size:** 576
- **Vocabulary size:** 50,264 tokens
- **Sequence length:** 256 tokens
- **Dropout:** 0.1
- **Number of parameters:** 58 million
- **Optimizer:** AdamW, learning rate 1×10^(-4), weight decay 0.01
- **Training:** 30 epochs, divided into 3 phases:
  - **Phase 1:** 10 epochs on CPU (4x AMD EPYC 7542), batch size 64, 50 hours per epoch, 139,870 steps total.
  - **Phase 2:** 5 epochs on GPU (1x Nvidia A100 40GB), batch size 64, 100 minutes per epoch, 69,935 steps total.
  - **Phase 3:** 15 epochs on GPU (2x Nvidia A100 40GB), batch size 128, 60 minutes per epoch, 104,910 steps total.

The model was trained using the Hugging Face library, but without using the `Trainer` class—native PyTorch was used instead.

## Fine-Tuned Versions of the SK_BPE_BLM Model

Here are the fine-tuned versions of the `SK_BPE_BLM` model based on the folders provided:

- [`SK_BPE_BLM-ner`](https://huggingface.co/daviddrzik/SK_BPE_BLM-ner): Fine-tuned for Named Entity Recognition (NER) tasks.
- [`SK_BPE_BLM-pos`](https://huggingface.co/daviddrzik/SK_BPE_BLM-pos): Fine-tuned for Part-of-Speech (POS) tagging.
- [`SK_BPE_BLM-qa`](https://huggingface.co/daviddrzik/SK_BPE_BLM-qa): Fine-tuned for Question Answering tasks.
- [`SK_BPE_BLM-sentiment-csfd`](https://huggingface.co/daviddrzik/SK_BPE_BLM-sentiment-csfd): Fine-tuned for sentiment analysis on the CSFD (movie review) dataset.
- [`SK_BPE_BLM-sentiment-multidomain`](https://huggingface.co/daviddrzik/SK_BPE_BLM-sentiment-multidomain): Fine-tuned for sentiment analysis across multiple domains.
- [`SK_BPE_BLM-sentiment-reviews`](https://huggingface.co/daviddrzik/SK_BPE_BLM-sentiment-reviews): Fine-tuned for sentiment analysis on general review datasets.
- [`SK_BPE_BLM-topic-news`](https://huggingface.co/daviddrzik/SK_BPE_BLM-topic-news): Fine-tuned for topic classification in news articles.

## Citation

If you find our model or paper useful, please consider citing our work:

### Articles

Part of this research (specifically the models pre-trained for **10 epochs**) has been published in:

Držík, D., & Forgac, F. (2024). *Slovak morphological tokenizer using the Byte-Pair Encoding algorithm*. **PeerJ Computer Science**, 10, e2465. [https://doi.org/10.7717/peerj-cs.2465](https://doi.org/10.7717/peerj-cs.2465)

An extended version of this work (including models pre-trained for **30 epochs** and evaluated across **multiple NLP downstream tasks**) has been published in:

Držík, D., & Kapusta, J. (2026). *The importance of morphology-aware subword tokenization for NLP tasks in Slovak language modeling*. **Expert Systems with Applications**, 312, 131492. [https://doi.org/10.1016/j.eswa.2026.131492](https://doi.org/10.1016/j.eswa.2026.131492)

### BibTeX entries

```bib
@article{drzik2024slovak,
  title={Slovak morphological tokenizer using the Byte-Pair Encoding algorithm},
  author={Držík, Dávid and Forgac, František},
  journal={PeerJ Computer Science},
  volume={10},
  pages={e2465},
  year={2024},
  month={11},
  issn={2376-5992},
  doi={10.7717/peerj-cs.2465}
}

@article{Drzik2026,
  author = {Dávid Držík and Jozef Kapusta},
  title = {The importance of morphology-aware subword tokenization for NLP tasks in Slovak language modeling},
  journal = {Expert Systems with Applications},
  volume = {312},
  pages = {131492},
  year = {2026},
  month = {5},
  issn = {09574174},
  doi = {10.1016/j.eswa.2026.131492}
}
```

