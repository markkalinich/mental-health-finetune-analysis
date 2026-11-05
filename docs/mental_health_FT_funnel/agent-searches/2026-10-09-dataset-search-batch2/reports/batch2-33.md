# Dataset search batch 2, agent 33

## Nikhil111999/blenderbot_mental_health

No. The cached card and the current card are the same automatic template. The Training Data line is "[More Information Needed]". The repository files are the tokenizer and `config.json`, which names the base `facebook/blenderbot_small-90M`, and there is no training script. A search for this repository id does not turn up a paper or a GitHub repo about it. GitHub user Nikhil111999 returns 404.

https://huggingface.co/Nikhil111999/blenderbot_mental_health

## nivvis/Qwen3.5-35B-A3B-EQ-v5

No. The card, which matches the cache, says the training data is "DPO preference pairs with diverse, simulated (real-situation-based) generated dialogue". That phrase does not name a file, a paper, or a Hub dataset. The same author does publish `nivvis/eq-dpo`, `nivvis/eq-convos`, and `nivvis/eq-esconv-sifted`, and the EQ-v1 card names `nivvis/eq-dpo`. Those dataset cards do not say they trained this v5 checkpoint. GitHub user nivvis returns 404.

https://huggingface.co/nivvis/Qwen3.5-35B-A3B-EQ-v5
https://huggingface.co/datasets/nivvis/eq-dpo
https://huggingface.co/nivvis/Qwen3.5-35B-A3B-EQ-v1

## NizamuddinMandekar/phi-therapist-chat-v1

Yes. The model card is still the automatic template, and the model repository has no training script. The same author's GitHub notebook `phi2_finetune_therapist_chat.ipynb` sets `new_model = "phi-therapist-chat-v1"`, loads `microsoft/phi-2` (the same base as this repo's `config.json`), and concatenates three Hub datasets. The notebook's `push_to_hub` line names `harshj0506/phi-therapist-chat-v1` (created 2024-04-10); this repository was created 2024-05-17. All three dataset pages load. `Amod/mental_health_counseling_conversations` is gated and asks for access; the other two are public.

https://github.com/NizamuddinMandekar/GEN-AI-LAB-WORK/blob/main/06_Advanced%20Fine-tuning%20Techniques/phi2_finetune_therapist_chat.ipynb
https://huggingface.co/datasets/marmikpandya/mental-health
https://huggingface.co/datasets/nbertagnolli/counsel-chat
https://huggingface.co/datasets/Amod/mental_health_counseling_conversations
https://huggingface.co/NizamuddinMandekar/phi-therapist-chat-v1

## nlpproject/t5small_EmpatheticChatbot_ED3

No. The cached card and the current card are the same automatic template. The Training Data line is "[More Information Needed]". Repository files are the tokenizer and config. `config.json` has `_name_or_path` `./t5-finetuned3/model`. Searches return other T5 empathetic models, including EmpBot (arXiv 2111.00310), which does not name this repository. The GitHub user nlpproject has one public repo, a Chinese input method, and no training script for this checkpoint.

https://huggingface.co/nlpproject/t5small_EmpatheticChatbot_ED3
https://arxiv.org/abs/2111.00310

## nlpproject/t5small_EmpatheticChatbot_ED4

No. The cached card and the current card are the same automatic template. The Training Data line is "[More Information Needed]". `config.json` has `_name_or_path` `t5-small`. The same searches as for ED3 do not name this repository. The author's only public GitHub repo is a Chinese input method, not a training script. The sibling ED5 card is the same empty template.

https://huggingface.co/nlpproject/t5small_EmpatheticChatbot_ED4

## nmj21c/Llama-3.2-1B-Mental-Health-Sentiment

No. The cached card and the current card are the same automatic template. The Training Data line is "[More Information Needed]". `config.json` names the base `meta-llama/Llama-3.2-1B-Instruct`. Other Hub repos with this model name (`curiousily`, `parvinroshni`, `janosk21`) carry the stock Llama 3.2 card and do not name a fine-tune corpus for this repository. The author's GitHub repos do not include a training script for this checkpoint.

https://huggingface.co/nmj21c/Llama-3.2-1B-Mental-Health-Sentiment

## nomeda-lab/nomeda-therapist-2B

No. The cached card and the current card match. The card says the model was fine-tuned from `unsloth/qwen3-1.7b-unsloth-bnb-4bit` with Unsloth and TRL, and it names no dataset. The author's Hub datasets are Arabic text and coding sets, and their cards do not name this model. GitHub user nomeda-lab returns 404. The repository has no training script.

https://huggingface.co/nomeda-lab/nomeda-therapist-2B

## nopenet/nope-edge

No. The cached card and the current card match. The card says the model was trained on real conversations and on one serialized user message, and it names no corpus a reader can open. `DISCLAIMER.md` and `NOTICE.md` do not name a dataset. The NOPE docs page says the same thing about pre-serialized transcripts and does not link a dataset. The author has no public Hub datasets. GitHub user nopenet returns 404.

https://huggingface.co/nopenet/nope-edge
https://docs.nope.net/edge

## Noureddine1/Therapist1

No. The cache file is a missing-card marker, and the Hub README returns 404. `checkpoint-875/trainer_state.json` records 875 steps, 1 epoch, and batch size 2, and it does not name a dataset. There is no training script in the repository. The GitHub user Noureddine1's public repos are Flutter packages, not this T5 model.

https://huggingface.co/Noureddine1/Therapist1
https://huggingface.co/Noureddine1/Therapist1/blob/main/checkpoint-875/trainer_state.json

## Noureddine1/therapiste

No. The cache file is a missing-card marker, and the Hub README returns 404. `trainer_state.json` at checkpoints 875, 1750, and 2625 records 3 epochs and 2625 steps, and none of them names a dataset. There is no training script. The same GitHub account does not contain a training repo for this checkpoint.

https://huggingface.co/Noureddine1/therapiste

## Novaciano/G3-Emotional-1B

No. The cached card and the current card match. The card says this checkpoint is a SLERP merge of `UmbrellaInc/T-Virus.Veronica-1B` and `Novaciano/Gemma3-Emotional-1B`. Those are parent models, not a training corpus. The repository's other files are the merge config, tokenizer, and weights. GitHub user Novaciano has no public repositories. A search does not find a paper that names training data for this merge.

https://huggingface.co/Novaciano/G3-Emotional-1B

## Novaciano/Gemma3-Emotional-1B

No. The cached card and the current card match. The card says this checkpoint is a SLERP merge of `Movidlona/gemma_1b_full_emotion_finetuned` and `Novaciano/Gemma3-UNCENSORED-V2-1B`. It does not name a training corpus for this checkpoint. The same GitHub user has no public repositories.

https://huggingface.co/Novaciano/Gemma3-Emotional-1B

## Novaciano/Gemma3-Emotional_Uncensored-1B

No. The cached card and the current card match. The card says this checkpoint is a SLERP merge of `Novaciano/Gemma3-UNCENSORED-V2-1B` and `Movidlona/gemma_1b_full_emotion_finetuned`. It does not name a training corpus. The parents are the same pair as `Gemma3-Emotional-1B`, with the base model swapped.

https://huggingface.co/Novaciano/Gemma3-Emotional_Uncensored-1B
