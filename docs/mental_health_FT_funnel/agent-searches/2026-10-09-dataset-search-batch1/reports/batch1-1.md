## 11-47/Continuum-0.1B

Yes. The public model page lists seven training datasets in a Datasets table. The raw README returns 401 because the repository is gated, and the cached card was that same error. Three ids on the card redirect to `11-47` dataset repos. All seven dataset pages load and are public.

https://huggingface.co/11-47/Continuum-0.1B
https://huggingface.co/datasets/11-47/claude_opus_mythos_5k
https://huggingface.co/datasets/11-47/claude_opus_4.8_distill_5k
https://huggingface.co/datasets/11-47/claude_mythos_distill_5k
https://huggingface.co/datasets/WithinUsAI/Opus4.7_thinking_max_distill_god_seed_25k
https://huggingface.co/datasets/WithinUsAI/claude_Opus_4.7_Distilled
https://huggingface.co/datasets/11-47/cluade_mythos_preview_5k_v2
https://huggingface.co/datasets/11-47/claude_opus_4.8_max_thinking_5k_v2

## a1273352/LFM2-1.2B-LEAP-multi-counselor

No. There is no model card. The repository has tokenizer and config files only. A sibling checkpoint, `a1273352/lfm2-counselor`, names KokoroChat, and that card does not name this checkpoint. No paper or GitHub page names training data for this repository.

https://huggingface.co/a1273352/LFM2-1.2B-LEAP-multi-counselor

## a1273352/lfm2-counselor

Yes. The model card names the KokoroChat GitHub repository as the dataset. That repository opens and contains dialogue JSON files. The Hub dataset `UEC-InabaLab/KokoroChat` loads and is public.

https://huggingface.co/a1273352/lfm2-counselor
https://github.com/UEC-InabaLab/KokoroChat
https://huggingface.co/datasets/UEC-InabaLab/KokoroChat

## Aarya4536/therapy-assist

No. There is no model card. The config names the base model `NousResearch/Llama-2-7b-chat-hf` and does not name a training corpus. Searches for this repository id, for GitHub, and on arXiv did not find a source that names this checkpoint's training data.

https://huggingface.co/Aarya4536/therapy-assist

## Abdullah-Baqais/gemma-3-Arabic-Empathy

Yes. The model card is an Unsloth stub and does not name a corpus. The owner's training script sets the dataset to `arbml/arabic_empathetic_conversations`. The README links a checkpoint named `gemma-3-Arabic-Empathy` under the name Lokatsu, and this card says Developed by Lokatsu with the same base model. The Hub dataset page loads and is public.

https://huggingface.co/Abdullah-Baqais/gemma-3-Arabic-Empathy
https://github.com/Abdullah-Baqais/gemma3-arabic-empathy/blob/main/gemma3_finetune.py
https://huggingface.co/datasets/arbml/arabic_empathetic_conversations

## Abhi2254/mentalhealth_model

No. There is no model card. The config names `NousResearch/Llama-2-7b-chat-hf`. The author's GitHub account has no training repository for this model. Searches did not find a paper that names its training data.

https://huggingface.co/Abhi2254/mentalhealth_model

## adamNLP/Llama-3.2-1B-Mental-Health-Fine-Tuned-Sentiment-Classifier

No. The card is a copy of the Llama 3.2 model card. It says that base model was pretrained on a new mix of publicly available online data, and it mentions WikiText 2 only for SpinQuant of Llama 3.2. That mix is not a dataset page a reader can open. No other source names this fine-tune's corpus.

https://huggingface.co/adamNLP/Llama-3.2-1B-Mental-Health-Fine-Tuned-Sentiment-Classifier

## adarshkumardalai/t5_emotional

No. There is no model card. `trainer_state.json` records 3 epochs and the checkpoint path `Models/t5_emotional/checkpoint-29000`, and it does not name a corpus. The author's GitHub repositories do not contain this training run. No paper names this checkpoint's data.

https://huggingface.co/adarshkumardalai/t5_emotional

## Ahatsham/Llama-3-8B-Instruct_Anxiety_Reasoning_Data-1

No. The card is the automatic Hub template and says training data is more information needed. The author has no public Hub datasets. Two arXiv papers by Ahatsham Hayat are about education trajectories and missing-data imputation, not this checkpoint. The words Anxiety_Reasoning_Data in the repository name are not a dataset page.

https://huggingface.co/Ahatsham/Llama-3-8B-Instruct_Anxiety_Reasoning_Data-1
https://arxiv.org/abs/2503.21617
https://arxiv.org/abs/2405.17712

## Ahatsham/Llama-3-8B-Instruct_Anxiety_Reasoning_Data-3

No. The card is the same automatic template and does not name a corpus. The same author search and the same two papers do not describe this checkpoint. The repository name is not a dataset page.

https://huggingface.co/Ahatsham/Llama-3-8B-Instruct_Anxiety_Reasoning_Data-3
https://arxiv.org/abs/2503.21617
https://arxiv.org/abs/2405.17712
