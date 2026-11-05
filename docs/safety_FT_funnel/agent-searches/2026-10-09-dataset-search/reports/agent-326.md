## SJJ0854/OmniVL-Guard-2B

Yes. The cached card and the live card both say the refined SFT and RL training sets are at SJJ0854/FSFR. That dataset page loads, lists Refined-SFT.jsonl and RL.jsonl, and shows a row preview. The dataset card calls FSFR the training data for the OmniVL-Guard model.

https://huggingface.co/SJJ0854/OmniVL-Guard-2B
https://huggingface.co/datasets/SJJ0854/FSFR

## SJJ0854/OmniVL-Guard-8B

Yes. The 8B card uses the same training-data sentence as the 2B card and points to SJJ0854/FSFR. The dataset page loads and the files are the refined SFT and RL sets. The live card matches the cached card.

https://huggingface.co/SJJ0854/OmniVL-Guard-8B
https://huggingface.co/datasets/SJJ0854/FSFR

## skarnam/gemma-2-2b-safety_vector

No. The card and mergekit_config.yml describe a linear merge of google/gemma-2-2b-it and skarnam/gemma-2-2b-it-unaligned. The repository has no training script. Searches point at the model-soups method paper, which is not a corpus for this checkpoint.

https://huggingface.co/skarnam/gemma-2-2b-safety_vector
https://arxiv.org/abs/2203.05482

## skyai798/safety-math-mix-sft

No. The cached fetch is a 403, and the live model page asks the reader to share contact information before the files open. README and trainer logs return 401. Searches for this repository id do not name a public dataset.

https://huggingface.co/skyai798/safety-math-mix-sft

## skyai798/safety_v2_math_v1

No. The card says this Llama-3.1-8B checkpoint was fine-tuned on the safety_v2_math_v1 dataset. The Hub page for skyai798/safety_v2_math_v1 returns 401. Trainer logs in the model repo record loss and step counts and do not name another corpus. Searches do not find a public dataset with that name.

https://huggingface.co/skyai798/safety_v2_math_v1
https://huggingface.co/datasets/skyai798/safety_v2_math_v1

## sleeepeer/Qwen3.5-4B-SecAlign-TRL-DPO-reasoning-off-3ep

No. There is no cached card. The live card says the checkpoint was trained on 19,157 preference pairs generated with the Meta-SecAlign procedure, using this Qwen3.5-4B model as the generator. The repository file list has no data file. The author's public datasets are PIArena evaluation sets, and the Meta-SecAlign GitHub README is about the Llama checkpoints, not these pairs.

https://huggingface.co/sleeepeer/Qwen3.5-4B-SecAlign-TRL-DPO-reasoning-off-3ep
https://github.com/facebookresearch/Meta_SecAlign

## smolify/smolified-bios-guard

Yes. The model card links a dataset at smolify/smolified-bios-guard. That page loads and shows instruction rows. The dataset card says this synthetic corpus was used to train smolify/smolified-bios-guard and reports 280 records.

https://huggingface.co/smolify/smolified-bios-guard
https://huggingface.co/datasets/smolify/smolified-bios-guard

## smolify/smolified-bios-guardian

Yes. The model card links smolify/smolified-bios-guardian. The dataset page loads. The dataset card says the corpus was used to train this model and reports 370 records.

https://huggingface.co/smolify/smolified-bios-guardian
https://huggingface.co/datasets/smolify/smolified-bios-guardian

## snu-bdai/palbot-suicidal-bert

No. The cached card and the live card are the empty Hub template, and the Training Data line says more information is needed. The repository files are the BERT weights and tokenizer. Searches for this repository id do not reach a paper or a dataset about this checkpoint.

https://huggingface.co/snu-bdai/palbot-suicidal-bert

## Solitude0630/SentGuard

Yes. There is no cached card, and the live README returns 401 because the model is gated. The model metadata names the paper arXiv:2606.02041 and the base model Qwen/Qwen3-4B-Instruct-2507. The HTML full text, by the same author Jiaqi Yu, says SentGuard was trained on StreamSafe. The dataset Solitude0630/StreamSafe loads.

https://huggingface.co/Solitude0630/SentGuard
https://arxiv.org/abs/2606.02041
https://arxiv.org/html/2606.02041
https://huggingface.co/datasets/Solitude0630/StreamSafe
