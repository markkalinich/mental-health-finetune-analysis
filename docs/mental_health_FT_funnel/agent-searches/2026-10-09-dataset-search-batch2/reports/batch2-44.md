## sugilee/mental-health-distill

No. The cached card (5 October 2026) is the Unsloth template. It names the base model `unsloth/deepseek-r1-distill-llama-8b-unsloth-bnb-4bit` and does not name a training corpus. The live Hub card metadata matches that cache. The repo files are weights, tokenizer files, and a LoRA adapter, with no training script.

https://huggingface.co/sugilee/mental-health-distill

## sugilee/mental-health-distill-3

No. The cached card is the same Unsloth template as `mental-health-distill` and names only the same base model. The live card metadata matches. The repo has weights and tokenizer files and no training script. Web search did not find a paper or GitHub repo that names a corpus for this checkpoint.

https://huggingface.co/sugilee/mental-health-distill-3

## Suguru1846/lora_model_counseling_16bit

No. The cached card is the automatic Hub template. Its Training Data line is `[More Information Needed]`. `adapter_config.json` names the base model `unsloth/llama-3.2-3b-instruct-unsloth-bnb-4bit` and does not name a dataset. The author's TalkToMe space loads the merged sibling, not a corpus.

https://huggingface.co/Suguru1846/lora_model_counseling_16bit
https://huggingface.co/Suguru1846/lora_model_counseling_16bit/blob/main/adapter_config.json

## Suguru1846/merged_counseling_model_full

No. The cached card is the automatic Hub template, and Training Data is `[More Information Needed]`. The TalkToMe app loads this model id and does not name a dataset. Searches did not find a paper or GitHub repo for this checkpoint.

https://huggingface.co/Suguru1846/merged_counseling_model_full
https://huggingface.co/spaces/Suguru1846/TalkToMe/blob/main/app.py

## sujayC66/falcon_7b_E20_172_helios_mental_health_data

No. The cache fetch failed and the live repo has no README. The file list is weights, config, and tokenizer files. The name includes "helios" and "172", and the author later uploaded `sujayC66/heliobramhas_mental_health_instruction_response` (172 rows), but that dataset card does not name this model. The Helios card that does name a corpus is for a different checkpoint, `heliosbrahma/falcon-7b-sharded-bf16-finetuned-mental-health-conversational`.

https://huggingface.co/sujayC66/falcon_7b_E20_172_helios_mental_health_data
https://huggingface.co/datasets/heliosbrahma/mental_health_chatbot_dataset
https://huggingface.co/datasets/sujayC66/heliobramhas_mental_health_instruction_response

## SupermanRX/therapistAi

No. The cached card is the Unsloth template and names only `unsloth/llama-3-8b-bnb-4bit`. The demo space loads this model and does not name a corpus. The author has no Hub datasets. Search hits for "therapistAI" are other projects.

https://huggingface.co/SupermanRX/therapistAi
https://huggingface.co/spaces/SupermanRX/testSpace2/blob/main/app.py

## Suyash-kr/Mental-Health-support-chatbot

No. The cached card is only an MIT license line. `training_args.bin` records `output_dir` `./chatbot_model` and does not record a dataset path. The MindNest app loads this model and does not name a corpus. A LinkedIn post about the project does not name a dataset.

https://huggingface.co/Suyash-kr/Mental-Health-support-chatbot
https://huggingface.co/spaces/Suyash-kr/MindNest/blob/main/app.py

## SuyashPandey/finetuned-mental-health-advisor

No. The cached card is the automatic Hub template. Training Data is `[More Information Needed]`. The linked paper id on the Hub page is the carbon-emissions template citation (arXiv 1910.09700), not a paper about this checkpoint. GGUF conversion pages name this repo and do not name a corpus.

https://huggingface.co/SuyashPandey/finetuned-mental-health-advisor

## swasthika28/llama-3.2-3b-mood-classifier

No. The cached card is the Unsloth template and names only `unsloth/Llama-3.2-3B-Instruct-bnb-4bit`. The author has no Hub datasets. Search hits are other people's Llama emotion classifiers, not this repo.

https://huggingface.co/swasthika28/llama-3.2-3b-mood-classifier

## sweagent/self-harmo-iter1-rl-iter49

No. The cached card is the Qwen3.5-35B-A3B model card copied into this repo. It describes Qwen's own training and does not name a corpus for this RL checkpoint. The author's rollout datasets describe other runs (`practical-diffrecon`, `combo2`, iter-2) and do not print this repo id. The Self-Harmony paper (arXiv 2511.01191) is a different project and does not name this checkpoint.

https://huggingface.co/sweagent/self-harmo-iter1-rl-iter49
https://arxiv.org/html/2511.01191
https://huggingface.co/datasets/sweagent/iter2-rl-rollouts

## TahirAhmad1002/empathy-bot-distilgpt2-final

Yes. This repo has no README. The author's demo loads `TahirAhmad1002/empathy-bot-distilgpt2-final` and states `Dataset: EmpatheticDialogues`. The same author's GitHub README says the dataset is EmpatheticDialogues from Facebook AI Research. The training notebook loads `Ahren09/empathetic_dialogues` and pushes the sibling id `TahirAhmad1002/empathy-bot-distilgpt2`. Both Hub pages for that corpus load.

https://huggingface.co/spaces/TahirAhmad1002/empathy-bot-demo/blob/main/src/streamlit_app.py
https://github.com/Tahirahmad1002/Task_05_Mental_Health_Chatbot/blob/main/README.md
https://github.com/Tahirahmad1002/Task_05_Mental_Health_Chatbot/blob/main/ML_Task_05_Mental_Health_Chatbot.ipynb
https://huggingface.co/datasets/facebook/empathetic_dialogues
https://huggingface.co/datasets/Ahren09/empathetic_dialogues

## tanish001/mentalhealth

No. The cache fetch failed and the live repo has no README. The Gradio app only calls `gr.load` on this model. The author uploaded `tanish001/guanaco-llama2-1k` the same day, and that page loads, but its README is empty and it does not name this checkpoint.

https://huggingface.co/tanish001/mentalhealth
https://huggingface.co/spaces/tanish001/tanish001-mentalhealth/blob/main/app.py
https://huggingface.co/datasets/tanish001/guanaco-llama2-1k
