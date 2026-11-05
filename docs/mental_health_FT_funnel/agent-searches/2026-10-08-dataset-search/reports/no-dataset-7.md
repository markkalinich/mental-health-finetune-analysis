# Dataset search, no-dataset batch 7

Checked 2026-10-08. Five models whose 2026-10-06 funnel row had no entry in `cardData.datasets` and no dataset tag. A dataset is recorded only when a paper, a training script, a dataset card, or the current model card names a training corpus and is about that repository.

## damian-shivihs/yllia-safety-classifier

Recovered: yes.

The newest cached card is `revision_3_experiments/hf_inventory/cache/readmes/damian-shivihs__yllia-safety-classifier__2026-10-05.md`. The live README is the same text. The Hub API `cardData` still has no `datasets` field and no dataset tag. The Dataset section names the corpus, and the usage example prints this repo id.

Sentence: "The project is based on 1,369 original questions written by people."

Those are short Polish messages written for a psychiatric or psychological practice. The same section says synthetic variants were added after the original questions were labelled: short paraphrases, emotionally intensified variants, spelling-error variants, and more verbose variants. The independent test subset is 206 original questions. The full test set is 637 examples (206 original and 431 synthetic). No Hugging Face dataset id is given. The account has no dataset repos.

URL: https://huggingface.co/damian-shivihs/yllia-safety-classifier

Also checked: an arXiv query for the repo id (no papers); GitHub https://github.com/shivihs (`data_labeling_system` has no project description and no training script for this checkpoint). A LinkedIn post by Damian Siwicki repeats the same 1,369-question count and the same test metrics and points at this checkpoint. It does not add a dataset name.

## ekenger/mpnet-multilabel-mental-health

Recovered: no.

The newest cached card is `revision_3_experiments/hf_inventory/cache/readmes/ekenger__mpnet-multilabel-mental-health__2026-10-05.md`. The live README is the same text. It says the model is a fine-tuned `microsoft/mpnet-base` with labels for depression, anxiety, and suicide risk, that it used adversarial training, that macro F1 is about 0.79, and that accuracy on "trick cases" is 100%. It does not name a corpus. The account has four models and no datasets. `config.json` labels are `LABEL_0`, `LABEL_1`, and `LABEL_2`.

Emre Kenger is a coauthor of Özer, Kenger, Gözükara, and Canbay, "Modeling Co-Existing Mental Health Risks in Social Media via Multi-Label Learning and LLM," El-Cezeri, 2026, DOI 10.31202/ecjse.1885302. The PDF is https://dergipark.org.tr/tr/download/article-file/5700885. That paper fine-tunes MPNet, RoBERTa, DeBERTa-v3, XLNet, ELECTRA, and MentalBERT on one hybrid corpus: AIMH/SWMH (38,483 posts), the Kaggle set "Sentiment Analysis for Mental Health" (46,296 texts), and Sentiment140 (6,597 texts), 91,376 texts in total. Table 5 gives that paper's MPNet macro-F1 as 0.79. The paper does not print `ekenger/mpnet-multilabel-mental-health`. It does not describe adversarial training or a trick-case test. The coauthor cards `zehra1931a/debertaa` and `gorkemgozukara1/electra-mental` are empty templates. The Space `ekenger/mental-saglik-uygulamasi` loads this checkpoint and does not name a corpus. An arXiv query for the repo id returned no paper.

No source about this repository names a training corpus.

https://huggingface.co/ekenger/mpnet-multilabel-mental-health

## Ghadafares2/flan-t5-psychology-finetuned

Recovered: no.

The newest cached card is `revision_3_experiments/hf_inventory/cache/readmes/Ghadafares2__flan-t5-psychology-finetuned__2026-10-05.md`. The live README is the same text. It is the empty Hub template. The Training Data line is "More Information Needed." The arXiv tag `1910.09700` is the Lacoste carbon-emissions paper cited inside that template. The Hub profile name is Ghada fares. The account has eight models and no datasets. The other psychology cards on the account are the same empty template. `config.json` is a T5 conditional-generation model (hidden size 768, 12 layers, vocabulary 32,128) and does not name a corpus. An arXiv query for the repo id returned no paper. No GitHub page was found that prints this repo id. The word "psychology" in the repo name is not a dataset.

https://huggingface.co/Ghadafares2/flan-t5-psychology-finetuned

## herisan/Llama-2-7b_mental_health_counseling_conversations

Recovered: no.

The cached fetch from 2026-10-05 is missing, and `https://huggingface.co/herisan/Llama-2-7b_mental_health_counseling_conversations/raw/main/README.md` returns 404. Commit titles are "initial commit", "Upload LlamaForCausalLM", and "Upload tokenizer". None names a corpus. The repo has config and tokenizer files and two weight shards, and no training-arguments file.

The same account has a dataset, `herisan/mental_health_counseling_conversations`, created the same day (2024-01-09), with 3,512 rows and columns `Context` and `Response`. Its dataset card is only a YAML schema. It does not say those rows were used to train this model. The matching words in the model name are not a dataset. Sibling cards either have no README or, for `herisan/llama-3-8b_mental_health_counseling_conversations`, an inference snippet that does not name a corpus. That snippet is about a different checkpoint. An arXiv query for this repo id returned no paper. GitHub user `heririta`, linked from the Hub profile, has no repository that prints this repo id.

https://huggingface.co/herisan/Llama-2-7b_mental_health_counseling_conversations

## insomnia7/0505_refseg_ft_3000iter

Recovered: no.

The cached fetch from 2026-10-05 is missing, and the live README URL returns 404. The model is `Qwen3VLForConditionalGeneration`. `trainer_state.json` records 3,000 steps, batch size 1, and a loss. It does not name a corpus. The raw URL for `training_args.bin` is a Git LFS pointer of 7,569 bytes. The resolve URL for that file returned HTTP 500, so the arguments file was not read. The Hub profile name is XuQi, and the linked GitHub user is `insomniaaac`. That user's public repositories do not include a training script for this checkpoint. The account's dataset cards are remote-sensing, video, and detection sets. None of them prints this repo id. An arXiv query for the repo id returned no paper. The word "refseg" in the repo name is not a dataset. `insomnia7/0505_refseg_finetune` is a different checkpoint and also has no README.

https://huggingface.co/insomnia7/0505_refseg_ft_3000iter
