---
license: apache-2.0
language:
  - en
  - ja
programming_language:
  - C
  - C++
  - C#
  - Go
  - Java
  - JavaScript
  - Lua
  - PHP
  - Python
  - Ruby
  - Rust
  - Scala
  - TypeScript
library_name: transformers
tags:
  - deberta
  - deberta-v3
#   - token-classification
datasets:
  - wikipedia
  - EleutherAI/pile
  - bigcode/the-stack
  - mc4
metrics:
  - accuracy
# mask_token: "[MASK]"
# widget:
#     - text: "京都大学で機械言語処理を研究する。"
---

# Model Card for Japanese DeBERTa V3 base

## Model description

This is a Japanese DeBERTa V3 base model pre-trained on LLM-jp corpus v1.0.

## How to use

You can use this model for masked language modeling as follows:

```python
from transformers import AutoTokenizer, AutoModelForMaskedLM
tokenizer = AutoTokenizer.from_pretrained('ku-nlp/deberta-v3-base-japanese')
model = AutoModelForMaskedLM.from_pretrained('ku-nlp/deberta-v3-base-japanese')

sentences = [
    "京都大学で自然言語処理を研究する。",
    "I research NLP at Kyoto University.",
    'int main() { printf("Hello, world!"); return 0; }',
]
encodings = tokenizer(sentences, return_tensors='pt')
...
```

You can also fine-tune this model on downstream tasks.

## Tokenization

The tokenizer of this model is based on [huggingface/tokenizers](https://github.com/huggingface/tokenizers) Unigram byte-fallback model.
The vocabulary entries were converted from [`llm-jp-tokenizer v2.2 (100k)`](https://github.com/llm-jp/llm-jp-tokenizer/releases/tag/v2.2).
Please refer to [README.md](https://github.com/llm-jp/llm-jp-tokenizer) of `llm-jp/llm-ja-tokenizer` for details on the vocabulary construction procedure.

Note that, unlike [ku-nlp/deberta-v2-base-japanese](https://huggingface.co/ku-nlp/deberta-v2-base-japanese), pre-segmentation by a morphological analyzer (e.g., Juman++) is no longer required for this model.

## Training data

We used the [LLM-jp corpus](https://github.com/llm-jp/llm-jp-corpus) v1.0.1 for pre-training.
The corpus consists of the following corpora:

- Japanese
  - Wikipedia (1B tokens)
  - mC4 (129B tokens)
- English
  - Wikipedia (4B tokens)
  - The Pile (126B tokens)
- Code
  - The Stack (10B tokens)

We shuffled the corpora, which has 270B tokens in total, and trained the model for 2 epochs.
Thus, the total number of tokens fed to the model was 540B.

## Training procedure

We slightly modified [the official implementation of DeBERTa V3](https://github.com/microsoft/DeBERTa) and followed the official training procedure.
The modified code is available at [nobu-g/DeBERTa](https://github.com/nobu-g/DeBERTa).

The following hyperparameters were used during pre-training:

- learning_rate: 1e-4
- per_device_train_batch_size: 800
- num_devices: 8
- gradient_accumulation_steps: 3
- total_train_batch_size: 2400
- max_seq_length: 512
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-06
- lr_scheduler_type: linear schedule with warmup
- training_steps: 475,000
- warmup_steps: 10,000

## Fine-tuning on NLU tasks

We fine-tuned the following models and evaluated them on the dev set of JGLUE.
We tuned the learning rate and training epochs for each model and task following [the JGLUE paper](https://www.jstage.jst.go.jp/article/jnlp/30/1/30_63/_pdf/-char/ja).

| Model                         | MARC-ja/acc | JCoLA/acc | JSTS/pearson | JSTS/spearman | JNLI/acc | JSQuAD/EM | JSQuAD/F1 | JComQA/acc |
|-------------------------------|-------------|-----------|--------------|---------------|----------|-----------|-----------|------------|
| Waseda RoBERTa base           | 0.965       | 0.867     | 0.913        | 0.876         | 0.905    | 0.853     | 0.916     | 0.853      |
| Waseda RoBERTa large (seq512) | 0.969       | 0.849     | 0.925        | 0.890         | 0.928    | 0.910     | 0.955     | 0.900      |
| LUKE Japanese base*           | 0.965       | -         | 0.916        | 0.877         | 0.912    | -         | -         | 0.842      |
| LUKE Japanese large*          | 0.965       | -         | 0.932        | 0.902         | 0.927    | -         | -         | 0.893      |
| DeBERTaV2 base                | 0.970       | 0.879     | 0.922        | 0.886         | 0.922    | 0.899     | 0.951     | 0.873      |
| DeBERTaV2 large               | 0.968       | 0.882     | 0.925        | 0.892         | 0.924    | 0.912     | 0.959     | 0.890      |
| DeBERTaV3 base                | 0.960       | 0.878     | 0.927        | 0.891         | 0.927    | 0.896     | 0.947     | 0.875      |

*The scores of LUKE are from [the official repository](https://github.com/studio-ousia/luke).

## License

[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

## Author

[Nobuhiro Ueda](https://huggingface.co/nobu-g) (ueda **at** nlp.ist.i.kyoto-u.ac.jp)

## Acknowledgments

This work was supported by Joint Usage/Research Center for Interdisciplinary Large-scale Information Infrastructures (JHPCN) through General Collaboration Project no. jh231006, "Developing a Platform for Constructing and Sharing of Large-Scale Japanese Language Models".
For training models, we used the mdx: a platform for the data-driven future.
