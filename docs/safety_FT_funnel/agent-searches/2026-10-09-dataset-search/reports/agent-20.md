## darkengross/Qwen3.5-9B-abliterated

No. There is no cached card. The live card says this checkpoint is Qwen3.5-9B after directional ablation plus a compliance LoRA, and that the compliance-tuning data is not redistributed. `abliteration.json` records the layer and the refusal sweep. AdvBench, JBB, and HarmBench are the held-out evaluation set. Searches for this repo id returned other people's Qwen3.5-9B abliterations.

https://huggingface.co/darkengross/Qwen3.5-9B-abliterated
https://huggingface.co/darkengross/Qwen3.5-9B-abliterated/blob/main/abliteration.json

## DeepXR/Helion-V1

No. There is no cached card. The live card leaves training data as the placeholder "[Information about training data]" and points "Finetuned from" at an unlinked name, Troviku-1.1. `autotrain.py` sets `dataset_name` to "your-dataset-name". `modelcard.json` lists categories such as "Public instruction datasets". No paper or GitHub repository names a corpus for this checkpoint.

https://huggingface.co/DeepXR/Helion-V1
https://huggingface.co/DeepXR/Helion-V1/blob/main/autotrain.py
https://huggingface.co/DeepXR/Helion-V1/blob/main/modelcard.json

## DeepXR/Helion-V1-reasoning

No. The live card uses the same unfilled training-data placeholder. `reasoning_training_data.py` is a generator that hardcodes a handful of puzzle answers and prints this repo id. It does not name a dataset page. Searches returned this Hub page.

https://huggingface.co/DeepXR/Helion-V1-reasoning
https://huggingface.co/DeepXR/Helion-V1-reasoning/blob/main/reasoning_training_data.py

## DigitalPixie/attention-guard-grpo

Yes. The cached card matches the live card and cites the GRPO method paper. It does not name a dataset. The trainer space sets this repo as the model it loads and the model it pushes, and sets the dataset to `DigitalPixie/attention-guard-rl-data`. That Hub dataset loads: 800 train rows. The same rows open as `train_data.jsonl` in the notification-prioritizer space, whose app loads this repo id as the GRPO model.

https://huggingface.co/DigitalPixie/attention-guard-grpo
https://huggingface.co/spaces/DigitalPixie/attention-guard-trainer/blob/main/app.py
https://huggingface.co/datasets/DigitalPixie/attention-guard-rl-data
https://huggingface.co/spaces/DigitalPixie/notification-prioritizer/blob/main/train_data.jsonl
https://huggingface.co/spaces/DigitalPixie/notification-prioritizer/blob/main/app.py

## DigitalPixie/attention-guard-v2-brain-f16

Yes. The cached Unsloth card matches the live card and does not name a dataset. The notification-prioritizer README lists this repo as the SFT model and says the SFT data is 800 notification-to-action pairs from environment trajectories. That file opens as `train_data.jsonl`, and the first rows match `DigitalPixie/attention-guard-rl-data`. The same README says the run that reached 100% validation accuracy used a balanced 600-row subset of those 800 pairs. The Kaggle notebook page loads and reads a local jsonl.

https://huggingface.co/DigitalPixie/attention-guard-v2-brain-f16
https://huggingface.co/spaces/DigitalPixie/notification-prioritizer/blob/main/README.md
https://huggingface.co/datasets/DigitalPixie/attention-guard-rl-data
https://huggingface.co/spaces/DigitalPixie/notification-prioritizer/blob/main/train_data.jsonl
https://www.kaggle.com/code/janani999/final/notebook

## Digsm003/safety-assign1-dpo-full

No. The cached card matches the live card: a fine-tune of gpt2-medium on an unknown dataset. The repo has no training script. Searches did not find a paper or GitHub repo for this id. The author's dataset `Digsm003/cpp-security-technical-debt` does not name this checkpoint. A different model, `Digsm003/safety-assign1-bert-reward-model`, names Cultural Kaleidoscope.

https://huggingface.co/Digsm003/safety-assign1-dpo-full

## Digsm003/safety-assign1-dpo-full-v2

No. The cached card matches the live card, which is the default Hub template. The training-data line is "[More Information Needed]." Searches returned this page and the other assignment checkpoints.

https://huggingface.co/Digsm003/safety-assign1-dpo-full-v2

## Digsm003/safety-assign1-ppo-full

No. The cached card matches the live template. The file list is the weights, the tokenizer, and the config. No paper or GitHub repository names training data for this id.

https://huggingface.co/Digsm003/safety-assign1-ppo-full

## Digsm003/safety-assign1-ppo-full-v2

No. The cached card matches the live template. The live page still says training data is "[More Information Needed]."

https://huggingface.co/Digsm003/safety-assign1-ppo-full-v2

## Dipto084/Llama-3.1-8B-RedQueenGuard

Yes. There is no cached card. The live card says this checkpoint is Llama-3.1-8B-Instruct trained with DPO on the 11,200-pair Red Queen Guard preference corpus, file `DPO_Data/dpo_red_guard.json` in the Red Queen GitHub repository. That file is in the repository and is 66,799,897 bytes. The card says `YifanJ/Red_Queen` is the attack set, and the preference pairs are the GitHub file.

https://huggingface.co/Dipto084/Llama-3.1-8B-RedQueenGuard
https://github.com/kriti-hippo/red_queen/blob/main/DPO_Data/dpo_red_guard.json
