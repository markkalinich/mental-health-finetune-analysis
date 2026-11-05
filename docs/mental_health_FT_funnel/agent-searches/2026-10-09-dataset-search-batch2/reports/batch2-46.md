# Dataset search batch 2, agent 46

## thu-coai/Crispers-7B-v1

No. The model card names Crisp, the bilingual dialogue set used to train Crispers, and says the training data will be released when the paper is published. The arXiv HTML says the same and points to an anonymous example link. The public GitHub repository has a README, assets, and example.py, and no data files. No Hub dataset for this corpus loads.

https://huggingface.co/thu-coai/Crispers-7B-v1
https://arxiv.org/html/2504.17238
https://github.com/thu-coai/Crisp

## Tianlin668/MentalBART

Yes. The MentaLLaMA README prints this repository id and says MentalBART was fine-tuned on the full IMHI-completion data. Training files for DR, dreaddit, SAD, MultiWD, and IRF open under `train_data/complete_data`. The model's own card says "IMHI instruction tuning data." The paper and the project README say these smaller models used the completion form. The README table still marks several source sets as not yet released.

https://github.com/SteveKGYang/MentalLLaMA/blob/main/README.md
https://raw.githubusercontent.com/SteveKGYang/MentalLLaMA/main/train_data/complete_data/DR/reddit_train.csv
https://ar5iv.labs.arxiv.org/html/2309.13567

## Tianlin668/MentalT5

Yes. The same README prints this repository id and says MentalT5 was fine-tuned on the full IMHI-completion data. The same completion files open. The model's own card says "IMHI instruction tuning data." The paper says T5-large was fine-tuned on IMHI-completion.

https://github.com/SteveKGYang/MentalLLaMA/blob/main/README.md
https://raw.githubusercontent.com/SteveKGYang/MentalLLaMA/main/train_data/complete_data/DR/reddit_train.csv
https://ar5iv.labs.arxiv.org/html/2309.13567

## timothy0503/Llama-3.1-8B-Instruct-Mental-Health-Classification

No. The cached card is the automatic Hub template, and Training Data is still "More Information Needed." `config.json` names a Kaggle path for Llama 3.1 8B Instruct, not a dataset. Other Hub repositories that reuse this model name point at `suchintikasarkar/sentiment-analysis-for-mental-health`. Those cards are about different repositories.

https://huggingface.co/timothy0503/Llama-3.1-8B-Instruct-Mental-Health-Classification

## tomaszki/0x0grandpa0-TraumaticaX0

No. The card is the automatic template. `config.json` sets `_name_or_path` to `0x0grandpa0/TraumaticaX0`. That Hub page returns 401, so it is a private model repository, not an open training corpus.

https://huggingface.co/tomaszki/0x0grandpa0-TraumaticaX0
https://huggingface.co/0x0grandpa0/TraumaticaX0

## Transducens/empathetic-teacher

Yes. The card names five teaching-dialogue corpora used to fine-tune this model. MathDial opens on the Hub as `eth-nlped/mathdial`. CIMA opens as `dataset.json` in `kstats/CIMA`. Conversational Uptake opens as `data/uptake_data.csv` in `ddemszky/conversational-uptake`. The Teacher-Student Chatroom Corpus is described as available through a request form, and the multicultural classroom spreadsheet links returned 404, so those two are not counted as opened.

https://huggingface.co/Transducens/empathetic-teacher
https://huggingface.co/datasets/eth-nlped/mathdial
https://github.com/kstats/CIMA/blob/master/dataset.json
https://github.com/ddemszky/conversational-uptake/blob/master/data/uptake_data.csv

## Trigonometrippin/gpt2_therapy_generator2

No. The Hub README URL returns 404. The repository files are weights, tokenizer files, and `training_args.bin`. That file names local folders `./results` and `./logs` and does not name a dataset. `config.json` says the base model is `EleutherAI/gpt-neo-125M`.

https://huggingface.co/Trigonometrippin/gpt2_therapy_generator2

## TTahir/Llama8b_CBT_Depression_Finetune_Nov_4

Yes. Talha Tahir's paper says the fine-tuned Llama 3.1 8B, Mistral 7B, and Qwen models are at `huggingface.co/TTahir`, trained on 58 sets of synthetic CBT transcripts. This repository has no README. Its config names `unsloth/Meta-Llama-3.1-8B-bnb-4bit`. The GitHub notebook `Llama_CBT_FineTuning_Nov4.ipynb` reads `Combined_Synthetic_Transcripts_Nov_2.txt`, and that file opens.

https://arxiv.org/html/2412.00251
https://github.com/ttahir-git/FineTuning_LLMs_for_CBT_for_Depression/blob/main/Code/Fine_Tuning_Notebooks/Llama_CBT_FineTuning_Nov4.ipynb
https://raw.githubusercontent.com/ttahir-git/FineTuning_LLMs_for_CBT_for_Depression/main/Synthetic_Transcripts/Combined_Synthetic_Transcripts_Nov_2.txt

## TTahir/Mistral7b_CBT_Depression_Finetune_Nov_5

Yes. The same paper and the same transcript file cover this checkpoint. This repository has no README. Its config names `unsloth/mistral-7b-bnb-4bit`. The notebook `Mistral_CBT_FineTuning_Nov5.ipynb` reads `Combined_Synthetic_Transcripts_Nov_2.txt`.

https://arxiv.org/html/2412.00251
https://github.com/ttahir-git/FineTuning_LLMs_for_CBT_for_Depression/blob/main/Code/Fine_Tuning_Notebooks/Mistral_CBT_FineTuning_Nov5.ipynb
https://raw.githubusercontent.com/ttahir-git/FineTuning_LLMs_for_CBT_for_Depression/main/Synthetic_Transcripts/Combined_Synthetic_Transcripts_Nov_2.txt

## TVRRaviteja/llama3.1-mental-health-therapy-SFT

No. The model card is the automatic template. The same user published `TVRRaviteja/MentalHealthTherapy`, and that dataset page loads. Its card says the set was built for fine-tuning and gives an example with a different model id. It does not name this checkpoint.

https://huggingface.co/TVRRaviteja/llama3.1-mental-health-therapy-SFT
https://huggingface.co/datasets/TVRRaviteja/MentalHealthTherapy

## umitmertcakmak/Llama-2-13B-fp16-mental-health-chatbot

No. The Hub README URL returns 404. `config.json` names the base `TheBloke/Llama-2-13B-fp16`. The same user published `umitmertcakmak/mental_health_chatbot_dataset`, and that page loads, with 172 train rows. Its card does not say this checkpoint was trained on it.

https://huggingface.co/umitmertcakmak/Llama-2-13B-fp16-mental-health-chatbot
https://huggingface.co/datasets/umitmertcakmak/mental_health_chatbot_dataset

## Vaibhavkumawatt/empathetic-blenderbot

No. The card is the automatic template. `config.json` names the base `facebook/blenderbot-400M-distill`. No paper, GitHub README, or dataset card names a training corpus for this repository.

https://huggingface.co/Vaibhavkumawatt/empathetic-blenderbot
