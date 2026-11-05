---
license: apache-2.0
language:
- multilingual
- en
- de
- fr
- es
- pt
- it
- nl
- pl
- ru
- uk
- cs
- ar
- he
- fa
- tr
- hi
- ur
- bn
- zh
- ja
- ko
- vi
- th
- id
- ms
- sw
- fi
- sv
- 'no'
- da
- el
- bg
- hr
- sk
- ro
- hu
- cy
- eu
- mt
- ug
library_name: transformers
pipeline_tag: text-classification
base_model: jhu-clsp/mmBERT-base
datasets:
- HuggingFaceFW/fineweb-2
- HuggingFaceFW/fineweb
tags:
- sentiment-analysis
- sentiment
- multilingual
- text-classification
- modernbert
- mmbert
- onnx
- transformers.js
widget:
- text: "The battery lasts forever and the screen is gorgeous. Best purchase this year!"
  example_title: "English"
- text: "Das Paket kam zwei Wochen zu spät und war beschädigt."
  example_title: "German"
- text: "サービスは丁寧だったけど、料理は正直いまいちでした。"
  example_title: "Japanese (mixed)"
- text: "الخدمة ممتازة والموظفون لطفاء جدا"
  example_title: "Arabic"
- text: "La reunión es el martes a las diez."
  example_title: "Spanish (neutral)"
---

# Multilingual Sentiment (base, 308M): negative / neutral / positive

A multilingual sentiment classifier built on [mmBERT-base](https://huggingface.co/jhu-clsp/mmBERT-base). It returns
**negative**, **neutral** or **positive** for reviews, social posts, comments, messages and support tickets in many
languages. It is Apache-2.0 and trained only on openly licensed text with labels from an Apache-2.0 LLM, so it can be used
commercially. It includes ONNX files for CPU and the browser (transformers.js).
A smaller, faster version is available as
[multilingual-sentiment-small](https://huggingface.co/Horizon-Labs/multilingual-sentiment-small). [Try it in the browser](https://huggingface.co/spaces/Horizon-Labs/multilingual-sentiment).

- Mixed or balanced opinions ("good quality but too expensive") are **neutral**. Plain facts, questions and requests are neutral too.
- The scores are probabilities, e.g. `positive - negative` gives a -1 to 1 polarity score.
- `onnx/model_quantized.onnx` (int8 embeddings, 641 MB) gives the same label as fp32 on 99.5% of 430 benchmark texts.

## Usage

```python
from transformers import pipeline

clf = pipeline("text-classification", model="Horizon-Labs/multilingual-sentiment-base")
clf(["I love this phone, the camera is amazing!", "Le colis est arrivé cassé.", "Der Termin ist am Montag."])
# [{'label': 'positive', ...}, {'label': 'negative', ...}, {'label': 'neutral', ...}]
```

transformers.js:

```js
import { pipeline } from "@huggingface/transformers";
const clf = await pipeline("text-classification", "Horizon-Labs/multilingual-sentiment-base", { dtype: "q8" });
console.log(await clf("Obrigado pela ajuda, vocês são incríveis!"));
```

## Evaluation

These are public benchmarks, used only for evaluation. We never trained on them, and any training text that also appears
in them was removed. The metric is macro-F1, averaged over the languages of each benchmark. On the two-class MTEB sets,
each model's negative-vs-positive choice is scored, ignoring neutral. Every model is run with the same script on the same
texts (`code/`), and each model's labels are mapped to negative/neutral/positive (1-2 stars = negative, 3 = neutral,
4-5 = positive; "very negative" = negative).

| model | licence | Tweets (8 languages, 3-class) | Amazon reviews (6 languages, 3-class) | MTEB MultilingualSentiment (29 languages, pos/neg) | note |
|---|---|---|---|---|---|
| **this model** (308M) | Apache-2.0 | **0.660** | **0.703** | **0.857** | |
| [multilingual-sentiment-small](https://huggingface.co/Horizon-Labs/multilingual-sentiment-small) (141M) | Apache-2.0 | 0.635 | 0.695 | 0.822 | |
| [cardiffnlp/twitter-xlm-roberta-base-sentiment](https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment) (278M) | none given | 0.700 | 0.533 | 0.772 | trained on the train split of the tweet benchmark |
| [cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual](https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual) (278M) | none given | 0.692 | 0.555 | 0.760 | same tweet training data |
| [lxyuan/distilbert-base-multilingual-cased-sentiments-student](https://huggingface.co/lxyuan/distilbert-base-multilingual-cased-sentiments-student) (135M) | Apache-2.0 | 0.414 | 0.484 | 0.650 |  |
| [nlptown/bert-base-multilingual-uncased-sentiment](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment) (167M) | MIT | 0.390 | 0.645 | 0.683 | trained on product reviews (1-5 stars) |
| [tabularisai/multilingual-sentiment-analysis](https://huggingface.co/tabularisai/multilingual-sentiment-analysis) (135M) | CC-BY-NC-4.0 | 0.499 | 0.494 | 0.670 |  |
| [clapAI/modernBERT-base-multilingual-sentiment](https://huggingface.co/clapAI/modernBERT-base-multilingual-sentiment) (150M) | Apache-2.0 | 0.784 | 0.775 | 0.653 | trained on an aggregate of public sentiment sets that may include these benchmarks' train splits |
| Qwen3.8-27B (our teacher, zero-shot prompt) | Apache-2.0 | 0.692 | 0.724 | 0.892 | 27B LLM, for reference |

- Numbers are for the released checkpoint (seed 0). Mean of two training seeds: small tweets .633 / Amazon .690 / MTEB .824; base tweets .658 / Amazon .703 / MTEB .855.
- Tweets: [cardiffnlp/tweet_sentiment_multilingual](https://huggingface.co/datasets/cardiffnlp/tweet_sentiment_multilingual)
  test (870 per language). Amazon: amazon_reviews_multi test (900 per language, balanced; 3 stars = neutral).
  MTEB: [mteb/multilingual-sentiment-classification](https://huggingface.co/datasets/mteb/multilingual-sentiment-classification)
  test (up to 600 per language; several languages are machine-translated, e.g. Welsh = translated IMDB).
- Models ahead of this one: tweets: twitter-xlm-roberta-base-sentiment, twitter-xlm-roberta-base-sentiment-multilingual, modernBERT-base-multilingual-sentiment; Amazon: modernBERT-base-multilingual-sentiment;
  MTEB: none. Models trained on a benchmark's own training split have an in-domain advantage
  on it; this model has seen no benchmark data.

Per benchmark language:

| set | this model | cardiffnlp xlm-r | teacher |
|---|---|---|---|
| amazon German | 0.744 | 0.539 | 0.754 |
| amazon English | 0.705 | 0.548 | 0.721 |
| amazon Spanish | 0.723 | 0.575 | 0.746 |
| amazon French | 0.728 | 0.499 | 0.736 |
| amazon Japanese | 0.703 | 0.543 | 0.768 |
| amazon Chinese | 0.613 | 0.497 | 0.623 |
| mteb Arabic | 0.853 | 0.858 | 0.897 |
| mteb Bambara | 0.577 | 0.591 | 0.595 |
| mteb Bulgarian | 0.893 | 0.853 | 0.927 |
| mteb Chinese (cmn set) | 0.927 | 0.789 | 0.967 |
| mteb Welsh | 0.814 | 0.527 | 0.938 |
| mteb German | 0.885 | 0.722 | 0.906 |
| mteb Algerian Arabic | 0.927 | 0.820 | 0.860 |
| mteb Greek | 0.860 | 0.720 | 0.913 |
| mteb English | 0.893 | 0.847 | 0.952 |
| mteb Basque | 0.851 | 0.573 | 0.867 |
| mteb Persian | 0.804 | 0.797 | 0.829 |
| mteb Finnish | 0.880 | 0.905 | 0.917 |
| mteb Hebrew | 0.833 | 0.843 | 0.873 |
| mteb Croatian | 0.943 | 0.855 | 0.957 |
| mteb Indonesian | 0.945 | 0.935 | 0.965 |
| mteb Japanese | 0.933 | 0.827 | 0.960 |
| mteb Korean | 0.806 | 0.778 | 0.865 |
| mteb Maltese | 0.788 | 0.489 | 0.824 |
| mteb Norwegian | 0.838 | 0.744 | 0.880 |
| mteb Polish | 0.985 | 0.874 | 1.000 |
| mteb Russian | 0.894 | 0.726 | 0.862 |
| mteb Slovak | 0.944 | 0.845 | 0.947 |
| mteb Spanish | 0.945 | 0.916 | 0.947 |
| mteb Thai | 0.775 | 0.766 | 0.798 |
| mteb Turkish | 0.895 | 0.907 | 0.961 |
| mteb Uyghur | 0.694 | 0.580 | 0.887 |
| mteb Urdu | 0.780 | 0.764 | 0.786 |
| mteb Vietnamese | 0.860 | 0.808 | 0.923 |
| mteb Chinese (zho set) | 0.845 | 0.731 | 0.875 |
| tweets Arabic | 0.655 | 0.670 | 0.714 |
| tweets English | 0.722 | 0.725 | 0.704 |
| tweets French | 0.594 | 0.735 | 0.599 |
| tweets German | 0.696 | 0.749 | 0.740 |
| tweets Hindi (romanized) | 0.590 | 0.572 | 0.634 |
| tweets Italian | 0.724 | 0.692 | 0.791 |
| tweets Portuguese | 0.627 | 0.765 | 0.674 |
| tweets Spanish | 0.669 | 0.691 | 0.684 |

## Training

- **Text** (about 433k training examples): snippets from
  [FineWeb-2](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2) and [FineWeb](https://huggingface.co/datasets/HuggingFaceFW/fineweb)
  (ODC-BY), in 67 languages, half of them from review, forum, comment and blog pages. We added synthetic reviews, posts,
  comments, messages and complaints in about 90 languages and varieties (including Hinglish and Arabic dialects), written by
  Qwen3.8-27B (Apache-2.0) in many genres, topics and lengths.
- **Labels**: soft labels (probabilities for negative, neutral and positive) from Qwen3.8-27B with a fixed zero-shot
  instruction (`code/sentiment/teacher_sent.py`). The model is trained to match these probabilities. The teacher's scores on
  the benchmarks are in the table above.
- **Model**: mmBERT-base with a 3-way head, 3 epochs, max length 512 tokens. The checkpoint was chosen by agreement with
  the teacher on held-out teacher-labelled data, never on the benchmarks.
- Code: `code/` in this repository.

## Limitations

- Labels come from an LLM, not from human annotators, so the model inherits the teacher's judgement. Its idea of "neutral"
  can differ from a given dataset's convention: tweet benchmarks mark many mildly opinionated posts as neutral.
- Accuracy is lower on sarcasm, on very short or context-dependent messages (tweets), and on some low-resource languages.
  Benchmark sets below 0.70 macro-F1: `amazon_zh`, `mteb_bam`, `mteb_uig`, `tweets_ar`, `tweets_fr`, `tweets_ge`, `tweets_hi`, `tweets_po`, `tweets_sp`.
- Trained on texts up to 512 tokens and evaluated on texts up to 2,000 characters. The model accepts up to 8,192
  tokens, but longer documents are untested; for those, pass `truncation=True, max_length=512`, or score paragraphs
  separately.
- Sentiment is not stance, emotion or toxicity. Don't use it to make decisions about individuals.
