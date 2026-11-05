# Dataset search pilot 4

9 October 2026. Five repositories. One training corpus recovered.

## MMahd/Llama-2-7b-chat-therapist-v2

No. No source names training data for this checkpoint.

The cached card is the text `FETCH_ERR MISSING`. The live README returns 404. The repository files are weights and tokenizer files only. The same author hosts `MMahd/Transformed-Dataset-Support`, a set of therapy-style `[INST]` dialogues, and that dataset page does not name this checkpoint.

https://huggingface.co/MMahd/Llama-2-7b-chat-therapist-v2
https://huggingface.co/datasets/MMahd/Transformed-Dataset-Support

## Moriacrafter/Qwen1.5-1.8B-none_DepressionDetection

No. The card does not name a training corpus, and the author's datasets do not name this checkpoint.

The cached card and the live card are the same generated template. Under Training Data the card says `[More Information Needed]`. The repository has no training script. The same author hosts `Moriacrafter/DepressionDetection_json` and related splits, and those pages do not say this Qwen checkpoint was trained on them.

https://huggingface.co/Moriacrafter/Qwen1.5-1.8B-none_DepressionDetection
https://huggingface.co/datasets/Moriacrafter/DepressionDetection_json

## noelabu/gemma-2b-instruct-ft-mental-health-conv_v2

No. No source names training data for this checkpoint.

The cached card and the live card are the same generated template. Under Training Data the card says `[More Information Needed]`. The repository has no training script. Searches for the repository id, the model name, arXiv, and GitHub did not find a paper or script about this checkpoint.

https://huggingface.co/noelabu/gemma-2b-instruct-ft-mental-health-conv_v2

## pixelsandpointers/distilbert-base-uncased-empatheticdialogues-sentiment-classifier

Yes. The author's training script trains this checkpoint on `empathetic_dialogues`.

The cached card is the text `FETCH_ERR MISSING`, and the live README returns 404. The repository files do not name a dataset. Benjamin Beilharz's thesis script `distilbert_ed_sentiment_classifier.py` loads `benjaminbeilharz/distilbert-base-uncased-empatheticdialogues-sentiment-classifier`, which is this same repository under his earlier username, and calls `load_dataset('empathetic_dialogues')`. That Hub dataset is `facebook/empathetic_dialogues`, and the dataset page loads.

https://huggingface.co/pixelsandpointers/distilbert-base-uncased-empatheticdialogues-sentiment-classifier
https://github.com/pixelsandpointers/ba-thesis/blob/main/src/models/sentiment/distilbert_ed_sentiment_classifier.py
https://huggingface.co/datasets/facebook/empathetic_dialogues

## RamziRebai/llama-2-7b-therapist-v3

No. No source names training data for this checkpoint.

The cached card is the text `FETCH_ERR MISSING`. The live README returns 404. The repository files are weights and tokenizer files only. `RamziRebai/finetuning_llama2` is an empty repository whose README is only a license line. The author's GitHub profile says he fine-tuned Llama 2 7B for therapeutic conversations and does not name a dataset or this checkpoint.

https://huggingface.co/RamziRebai/llama-2-7b-therapist-v3
https://huggingface.co/RamziRebai/finetuning_llama2
https://github.com/RamziRebai/RamziRebai
