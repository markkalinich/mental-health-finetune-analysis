---
language:
- tr
license: apache-2.0
library_name: transformers
base_model: ytu-ce-cosmos/modernbert-tr-base
base_model_relation: finetune
pipeline_tag: token-classification
datasets:
- ytu-ce-cosmos/absa-tr
metrics:
- f1
tags:
- modernbert
- absa
- aspect-term-extraction
- sentiment
- onnx
- encoderfile
---

<p align="center">
  <img src="assets/logo.webp" width="20%" alt="ModernBERT-TR aspect extraction" />
</p>
<h1 align="center">ModernBERT-TR Aspect Extraction</h1>

A 150M-parameter Turkish token classifier that extracts opinion targets with `O`, `B-ASP`, and `I-ASP` labels.

## Results

Our model scores 64.09 +/- 0.30% exact entity-span F1 on the [ABSA-TR](https://huggingface.co/datasets/ytu-ce-cosmos/absa-tr) test set. The released checkpoint scores 69.46% on the translated M-ABSA Turkish test set.

The quantized int8 version scores 61.30% on ABSA-TR test set.

## Usage

```python
from transformers import pipeline

extract = pipeline(
    "token-classification",
    model="ytu-ce-cosmos/modernbert-tr-absa-extraction",
    aggregation_strategy="first",
)
extract("Kargo hızlıydı ama ürün kötüydü.")
```

You can call the tokenizer with `is_split_into_words=True` to allow the tokenizer to split the sentence into words, and keep the first WordPiece label for each word.

## Training

We finetune [`ytu-ce-cosmos/modernbert-tr-base`](https://huggingface.co/ytu-ce-cosmos/modernbert-tr-base) using about 8.7k translated M-ABSA records and 11,993 teacher-labeled data points. We use learning rate `4e-5`, batch size 32, 15 epochs, linear warmup and decay, no weight decay, and first-subword alignment.


Standalone binaries are available in the [encoderfile repo](https://huggingface.co/ytu-ce-cosmos/modernbert-tr-absa-extraction-encoderfile).

## License

Apache-2.0.
