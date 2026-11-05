---
license: apache-2.0
language:
  - en
base_model: answerdotai/ModernBERT-base
pipeline_tag: text-classification
library_name: transformers
tags:
  - topic-classification
  - sentiment
  - spam-detection
  - social-media
  - modernbert
  - multi-head
---

# microblog-topic-classifier

A topic classifier for short social posts from Bluesky. Given one post, it predicts:

- **broad topic**: one of 25 topics (e.g. `sports`, `technology`, `us_politics`)
- **subtopic path**: one of 118 labels, the 117 subtopics of taxonomy v1 (e.g.
  `sports/american_football`, `technology/ai`) plus `unclear`
- **signals**: ten independent scores in 0-1 (see [Signals](#signals)): `substance`, `news`,
  `promo`, `general_interest`, `sentiment`, `critical`, `ad`, `engagement_bait`, `spam`,
  `self_promo`
- **tone**: one of `informative`, `humorous`, `personal`, `outraged`, `supportive`, `other`

It powers topic feeds: posts are classified as they arrive, a feed selects posts whose
subtopic probability clears a threshold, and the signals let a feed drop or down-rank posts,
for example ads, spam, or posts that are against the feed's own topic.

The code that runs the feeds and trained this model (ingest, the live pipeline, the feed
generator, labeling, and training) is on GitHub at
[haileyok/topic-feed](https://github.com/haileyok/topic-feed).

It agrees with Jev, the model it was distilled from, on the broad topic for 84% of held-out
live posts (81% on older test posts), at roughly 1/2,000th of the cost per post. Besides the
post's text, it reads what's in its images (text read from the image, or a short description
of it), its attachments, and its labels.

## Model

ModernBERT-base encoder, mean pooling over tokens, and four linear heads on the pooled vector.
Max input length 256 tokens. Broad and path probabilities are softmax with temperature scaling
fitted on the validation set (`temperature_broad`, `temperature_path` in `config.json`). Tone
is a plain softmax; signals are sigmoids.

It is distilled from **Jev** (`jev-1.13.0`): the training targets are Jev's soft probability
distributions over the taxonomy's broad topics and subtopics, plus its signal and tone answers.
For older posts where Jev was unsure (top probability ≤ 0.5, about 23k posts), a second model,
Luna (`gpt-6-luna`), relabeled the post and the two label sets were blended.

## Input format

The model expects a **post document**: a plain-text rendering of the post, the same format it
was trained on (format version `pd2`):

```
{post text}
[tags] #tag1 #tag2
[media] 2 images, 1 video
[labels] porn, nudity
[alt] {image alt text 1} | {image alt text 2}
[image text] {words read from image 1} | {image 2}
[image description] {description of image 1} | {image 2}
[link] {link card domain} | {title} | {description}
[quote] {text of the quoted post}
```

- `[media]` counts the post's attachments by kind.
- `[labels]` lists self-labels and moderation labels on the post or its author (e.g. `porn`,
  `sexual`, `nudity`, `graphic-media`, `spam`). Moderation actions (`!takedown`, `!hide`, ...)
  and `needs-review` are left out.
- `[image text]` and `[image description]` are only for attachments **without** alt text. In
  training, `[image text]` came from tesseract OCR when it found at least 7 confident words,
  and otherwise `[image description]` came from a vision model asked for one or two sentences,
  like alt text, naming readable text and recognizable things (teams, games, brands, people).

Lines for empty fields are omitted. The post text keeps its line breaks; the other fields are
collapsed to one line. Image text and descriptions are cut at 300 characters each, link
descriptions at 300, quoted text at 500. `render_post()` in `modeling.py` produces this
format.

## Usage

```python
import sys
from huggingface_hub import snapshot_download

path = snapshot_download("haileyok/microblog-topic-classifier-v4")
sys.path.insert(0, path)
from modeling import load, render_post

clf = load(path)  # uses CUDA when available
docs = [
    render_post(text="Chiefs clinch the AFC West with a late field goal", tags=["NFL"]),
    render_post(text="ok this is actually beautiful", media=["image"],
                image_descriptions=["A watercolor painting of a lighthouse at sunset over a calm sea."]),
    render_post(text="AI slop has ruined image search. every result is fake now"),
]
for r in clf.classify(docs):
    print(next(iter(r["paths"])), {k: r["signals"][k] for k in ("sentiment", "critical", "self_promo")})
# (rounded)
# sports/american_football {'sentiment': 0.72, 'critical': 0.11, 'self_promo': 0.05}
# art/fine_art             {'sentiment': 0.91, 'critical': 0.03, 'self_promo': 0.24}
# technology/ai            {'sentiment': 0.04, 'critical': 0.97, 'self_promo': 0.02}
```

Requires `torch`, `transformers` (with ModernBERT support), `safetensors`, and
`huggingface_hub`. `load()` builds the encoder from `encoder_config.json`, so the base model's
weights are not downloaded. `classify()` returns the top 5 broad topics and top 8 paths, and
every signal and tone.

## Signals

Each signal is the model's estimate of Jev's answer to a question about the post:

| signal | question Jev answered | scale |
|---|---|---|
| `substance` | How substantive is the post? (low effort / some substance / substantive) | 0-1 |
| `news` | Is it about a current event or breaking news? | P(yes) |
| `promo` | Is it mainly self-promotion, an advertisement, or a request for follows, likes, or reposts? | P(yes) |
| `general_interest` | Would someone who doesn't know the author find it interesting? | P(yes) |
| `sentiment` | Overall sentiment, very negative (0) to very positive (1) | 0-1 |
| `critical` | Is it negative about, critical of, or mocking the main thing it is about (e.g. a post about AI that says AI is bad)? | P(yes) |
| `ad` | Is it an advertisement, sales pitch, or deal for a product or service? | P(yes) |
| `engagement_bait` | Does it mainly ask for follows, likes, reposts, or replies (follow trains, "like if you agree", repost-to-win giveaways)? | P(yes) |
| `spam` | Is it spam: a scam, a crypto or money scheme, repetitive or automated junk, a link farm, or piles of unrelated hashtags? | P(yes) |
| `self_promo` | Is the author sharing or promoting their own work (art, writing, music, stream, shop, research)? | P(yes) |

`sentiment`, `critical`, `ad`, `engagement_bait`, `spam` and `self_promo` were learned from the
~47k recent training posts only; the older labels don't have them.

`critical` is about the post's stance toward its own topic, which tone can't capture: many
posts against their topic are sarcastic or personal rather than angry. On the 173 held-out
live posts the model puts in `technology/ai`, Jev judged 100 critical of AI:

| filter | critical posts caught | non-critical posts dropped |
|---|---|---|
| `critical ≥ 0.5` | 80 of 100 | 6 of 73 |
| tone `outraged ≥ 0.5` | 32 of 100 | 2 of 73 |

`self_promo` is separate from `ad` and `spam` so a feed can keep artists and creators sharing
their work while dropping ads and junk. The `promo` signal still covers all of them.

## Training data

- **Labeling windows**: about 180k English posts from 24 fifteen-minute windows spread over
  2026-09-25 to 09-28 (each hour of the day once), labeled by Jev (with the Luna blend above).
  Split by time: training on the oldest 18 windows, validation on the next three, test on the
  newest three, so the test windows measure performance on later posts. These labels have no
  image text, attachment, or label lines, and only the first four signals.
- **Live posts**: 60k posts from 2026-09-29 05:00-24:00 UTC, labeled by Jev with the full `pd2`
  input and all ten signal questions: 40k picked at random and 20k picked as hard cases (no
  broad topic above 0.5 in a preliminary classification, or in the fuzziest topics: humor,
  online culture, lifestyle, personal life). 10k of the random posts are held out for testing
  and 3k for validation (fixed by a hash of the post URI); the other ~47k are training data,
  weighted 3x.

Posts with no text and no alt text or image text are not used. `data_manifest.json` lists the
rows per window. Only the model is published, not the posts.

Training: 8 epochs, learning rate 5e-5, batch size 64, examples weighted by Jev's confidence
(floored at 0.3) and 3x for the live posts; signal targets Jev wasn't asked (the last six
signals on the labeling-window posts) are left out of the loss. The best epoch was the 7th. See `report.json` for all
hyperparameters.

## Evaluation

### Held-out live posts

10,000 random posts from 2026-09-29, held out from training:

| metric | score |
|---|---|
| broad topic, top-1 | 83.8% |
| broad topic, top-3 | 96.3% |
| subtopic path, exact top-1 | 75.7% |
| path top-1 is one of Jev's plausible answers, or an equivalent subtopic | 90.4% |
| tone top-1 | 81.0% |
| broad calibration error (ECE) | 0.055 |

The model does as well on posts with image text, attachments, or labels (29% of posts; broad
top-1 84.2%) as on text-only posts (83.7%). Labels are strong evidence for `adult_content`
(recall 88%).

### Signals

On the same live posts, taking Jev's answer ≥ 0.5 as "yes". Ranking quality (AUC) is 0.91-0.98
for every signal. At a 0.5 cutoff the model is conservative on rare signals: for `spam` 87% of
flagged posts are spam by Jev's call, but only 58% of Jev's spam is flagged, so a lower cutoff
(e.g. 0.3) catches more. `engagement_bait` is rare (0.4% of posts, about 40 in the test set):
it ranks well but almost never reaches 0.5, so use a low cutoff or treat it as experimental.

![Signals on held-out live posts](assets/signals.png)

### Test windows

On the newest three labeling windows (20,058 posts, never seen in training):

| metric | score |
|---|---|
| broad topic, top-1 | 80.6% |
| broad topic, top-3 | 94.5% |
| subtopic path, exact top-1 | 71.9% |
| subtopic path, top-3 | 88.3% |
| path top-1 is one of Jev's plausible answers, or an equivalent subtopic | 87.0% |
| broad calibration error (ECE) | 0.050 |
| tone top-1 | 79.6% |
| signal correlation (substance / news / promo / general interest) | 0.94 / 0.91 / 0.93 / 0.87 |

A "plausible" answer is any subtopic whose label probability is at least a quarter of Jev's
top subtopic's. Equivalences (`taxonomy/v1-equivalences.yaml`) cover boundaries the taxonomy
doesn't draw clearly, where human review accepted either side: `unclear`, `humor/shitposts`
and `online_culture/other` match each other; `<broad>/other` matches any subtopic of the same
broad topic; and `online_culture/quote_prompts` matches any answer on a post that quotes
another post.

Most disagreement is on posts Jev itself was unsure about. When Jev was at least 90%
confident (about half the posts), the model agrees on the broad topic 96% of the time. Below
60% confidence, exact agreement falls to under half, but the model's answer is still one of
Jev's plausible ones 83% of the time:

![Agreement with Jev by Jev's confidence](assets/agreement_by_confidence.png)

Per broad topic on the held-out live posts, with Jev's top topic as the reference. Topics with
clear vocabulary (`automated_feeds`, `us_politics`, `sports`) do best; `humor`,
`online_culture`, `work_education` and `lifestyle` are the fuzziest:

![Per-topic precision and recall](assets/per_topic.png)

### Calibration

With temperature scaling, the broad-topic probabilities are slightly *underconfident* against
Jev's top pick, on the test windows and on live posts alike: posts the model gives about 0.55
match Jev about 63-66% of the time. So a threshold keeps a little more precision than its face
value suggests.

![Calibration of the broad topic](assets/calibration.png)

### Choosing a feed threshold

For a topic feed, the question is how precision and coverage trade off as the minimum
subtopic probability rises. Below, on the Jev-only test windows, "precision" is the share of
selected posts where the subtopic is Jev's top pick (dashed) or one of Jev's plausible picks
(solid); "recall" is the share of Jev's top-pick posts the threshold catches. At the NFL feed's
threshold (0.85), 99.5% of selected posts are plausible and the feed catches 46% of Jev's
top-pick posts; at the AI feed's (0.6), 97% and 72%.

![Precision and recall by threshold](assets/feed_thresholds.png)

### Training

Validation agreement by epoch:

![Validation agreement by epoch](assets/training.png)

## Cost

The reason to distill: labeling with the model costs about 2,000 times less per post than Jev,
and runs about 180 times faster than Jev's rate budget allows.

![Cost and throughput](assets/cost.png)

- **Jev**, measured on the labeling windows: 445M input tokens for 183,536 posts (a broad-topic
  request and a subtopic request per post) at $0.042 per million input tokens (output tokens
  are free): about $18.70 in total, or $0.10 per 1,000 posts. The live-post labels, with the
  fuller input and all ten signal questions, cost $0.115 per 1,000. Throughput is set by the rate
  budget of 500 requests a minute, about 4 posts a second.
- **Luna**, measured on the relabel: $4.31 at list price for 23,053 posts, $0.19 per 1,000,
  with 98.7% of prompt tokens served from cache.
- **This model**: 770 posts a second on one GPU in bfloat16. The cost shown is an estimate of
  electricity only: 450 W at $0.30/kWh, about $0.00005 per 1,000 posts. It leaves out the
  hardware itself, and the cost of describing images when you supply `[image description]`.

## Limitations

- **English only.** Non-English posts were not in the training data.
- **Images only through text.** The model never sees pixels: only alt text, text read from
  images, and descriptions you supply. Without them, posts whose meaning is in an image often
  come out `unclear` or wrong.
- **Labels are strong evidence.** A post labeled `porn` or `sexual` is pushed toward
  `adult_content`, as it was in the training labels. The model is not a safety classifier and
  should not replace moderation labels.
- **Distilled from Jev.** The model learned Jev's reading of the taxonomy and questions,
  including its mistakes and its uncertainty on ambiguous posts (jokes, sarcasm, posts that
  need thread context). `critical`, `spam` and the other signals mean "what Jev would say".
- **Six signals, one day of data.** `sentiment`, `critical`, `ad`, `engagement_bait`, `spam`
  and `self_promo` were learned from posts of a single day; `engagement_bait` from very few examples.
- **Fixed taxonomy.** Topics are frozen at taxonomy v1, drafted in September 2026. New events
  and communities that don't fit an existing subtopic land in `*/other` or a nearby subtopic.
- **Drift.** Social media topics shift day to day; expect agreement to decline on posts far
  from the training period.

## Files

| file | contents |
|---|---|
| `model.safetensors` | weights (encoder + four heads) |
| `encoder_config.json` | ModernBERT-base encoder config |
| `config.json` | label and signal lists, temperatures, max length, format versions |
| `tokenizer.json`, `tokenizer_config.json` | tokenizer (ModernBERT-base) |
| `modeling.py` | model class, `load()`, `render_post()` |
| `taxonomy/v1.yaml` | topic and subtopic definitions with descriptions and examples |
| `taxonomy/v1-equivalences.yaml` | subtopics counted as interchangeable when scoring |
| `metrics.json` | test-window and live-test metrics, per-topic scores, training history |
| `report.json` | hyperparameters and final validation metrics |
| `compare_jev.json`, `compare_jev.jev_only.json` | detailed agreement with Jev on the test windows (against the training labels; against Jev-only labels) |
| `data_manifest.json` | training data rows per window |
| `train.log`, `tb/` | training log and TensorBoard logs |
| `assets/` | the charts in this card |
