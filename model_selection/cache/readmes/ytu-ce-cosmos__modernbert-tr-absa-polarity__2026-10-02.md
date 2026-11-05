---
language:
- tr
license: apache-2.0
library_name: transformers
base_model: ytu-ce-cosmos/modernbert-tr-base
base_model_relation: finetune
pipeline_tag: text-classification
datasets:
- ytu-ce-cosmos/absa-tr
metrics:
- f1
tags:
- modernbert
- absa
- aspect-based-sentiment-analysis
- sentiment
- onnx
- encoderfile
---

<p align="center">
  <img src="assets/logo.webp" width="20%" alt="ModernBERT-TR aspect polarity" />
</p>
<h1 align="center">ModernBERT-TR Aspect Polarity</h1>

A 150M-parameter Turkish classifier that receives a sentence and an aspect, then predicts `negative`, `neutral`, or `positive` sentiment toward that aspect.

## Results

Our model scores 72.74 +/- 2.10% macro-F1 on the [ABSA-TR](https://huggingface.co/datasets/ytu-ce-cosmos/absa-tr) test set. The released checkpoint scores 72.87%.

The quantized int8 version scores 71.89% on ABSA-TR test set.

## Usage

```python
from transformers import pipeline

classify = pipeline(
    "text-classification",
    model="ytu-ce-cosmos/modernbert-tr-absa-polarity",
)
classify({"text": "Kargo hızlıydı ama ürün kötüydü.", "text_pair": "ürün"})
```

## Training

We finetune [`ytu-ce-cosmos/modernbert-tr-base`](https://huggingface.co/ytu-ce-cosmos/modernbert-tr-base) with mean pooling and a three-label head using translated M-ABSA pairs, 11,470 native Turkish clothing-review rows, and 17,186 usable pairs from teacher-labeled Turkish reviews. We use learning rate `3e-5`, batch size 32, 15 epochs, linear warmup and decay, weight decay 0.01, label smoothing 0.1, and five seeds.

Standalone binaries are available in the [encoderfile repo](https://huggingface.co/ytu-ce-cosmos/modernbert-tr-absa-polarity-encoderfile).

## License

Apache-2.0.
