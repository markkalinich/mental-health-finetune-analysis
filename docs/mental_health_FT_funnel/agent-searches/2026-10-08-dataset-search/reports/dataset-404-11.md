# Dataset names that were missing on 2026-10-06

Checked on 2026-10-08. Newest cached card: 2026-10-05 for all five. The live READMEs fetched the same day still list the same dataset tags.

## SH198/counselor

Old name: `SH198/counselor`. The dataset page title is `404 – Hugging Face`. The HTTP status is 401, the same status a made-up dataset id returns for that 404 page.

The card is the generated template. It lists `SH198/counselor` under `datasets` and does not describe a corpus. The only paper tag is `arxiv:1910.09700`, the carbon-emissions citation in the template. The GitHub account `sh198` has one repository, `github-slideshow`. No paper, training script, or dataset card about this repository names a corpus that can be opened.

## SrothJr/banglamentalBERT-mBERT-dapt

Old name: `depression-social-media`. The Hub dataset page returns 404. The name has no slash.

The card says domain-adaptive pre-training used Bangla mental-health corpora and does not give a link. `SrothJr/banglamentalBERT-corpuses` returns 200, and `bangla_dapt_corpus_clean.txt` opens, but that dataset card does not name this checkpoint. `SrothJr/bangla_mental_corpus` returns 200 and has no card. `dapt/run_dapt.py` in https://github.com/SrothJr/bangla-mh-nlp-thesis loads `../data/raw/bangla_dapt_corpus_clean.txt` for a local run it calls `mBERT`. That file is not in the git repository, and the script does not print `SrothJr/banglamentalBERT-mBERT-dapt`. The card for `SrothJr/banglamentalBERT-mBERT-dapt-tapt` describes a different checkpoint. https://github.com/SrothJr/p2_model names `SrothJr/bangla-depression-model`.

## SrothJr/banglamentalBERT-sahajBERT-dapt

Old name: `depression-social-media`. The Hub dataset page returns 404. The name has no slash.

The card says domain-adaptive pre-training used Bangla mental-health corpora and does not give a link. `SrothJr/banglamentalBERT-corpuses` returns 200, and `bangla_dapt_corpus_clean.txt` opens, but that dataset card does not name this checkpoint. The same script, `dapt/run_dapt.py`, loads that local path for a run it calls `sahajBERT` and does not print `SrothJr/banglamentalBERT-sahajBERT-dapt`. The card for `SrothJr/banglamentalBERT-sahajBERT-dapt-tapt-minaug` describes a different checkpoint.

## SURIYA-KP/nomic-embed-text-v2-moe-fine-tuned-depression-symptoms

Old name: `custom_symptom_dataset`. The Hub dataset page returns 404. The name has no slash.

The card says the model was trained with contrastive pairs of symptom descriptions for 21 symptom types and does not link a file. `example_usage.py` in the model repository does not name a dataset. The account has no public datasets. A GitHub search of `SURIYA-KP` for depression, symptom, embed, or nomic returned no repository. DepreSym is a 21-symptom corpus by other authors, and that paper does not name this model.

## SURIYA-KP/small-sentence-embeddings-fine-tuned-depression-symptoms

Old name: `custom_symptom_dataset`. The Hub dataset page returns 404. The name has no slash.

The card says the model was trained with contrastive pairs of symptom descriptions for 21 symptom types and does not link a file. `example_usage.py` in the model repository does not name a dataset. The account has no public datasets. No paper, training script, or dataset card about this repository names a corpus that can be opened.
