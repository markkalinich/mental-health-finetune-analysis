## Daydong/gemma3-counselor-16bit

No. The cached card from 5 October 2026 matches the live README. It says the checkpoint was finetuned from unsloth/gemma-3-4b-it-bnb-4bit with Unsloth and TRL. The repository has no training script, and searches did not find a paper or GitHub page that names a corpus for this id.

https://huggingface.co/Daydong/gemma3-counselor-16bit

## debadtman26/krishna-saarthi-counselor-2bit

No. The card is the automatic Hub template, and Training Data is still "More Information Needed". The file training_samples.json opens and holds five Krishna instruction rows, and no sentence says this checkpoint was trained on that file. A Medium post by the same author describes Project Saarthi on Qwen2.5-7B-Instruct and does not name this 2-bit repository or an open dataset.

https://huggingface.co/debadtman26/krishna-saarthi-counselor-2bit
https://huggingface.co/debadtman26/krishna-saarthi-counselor-2bit/blob/main/training_samples.json
https://medium.com/@neevdeb26/project-saarthi-a-chat-with-krishna-3a01d2810fb8

## DesanAI/Empathy

No. There is no cached card, and the live README returns 404. checkpoint-291/trainer_state.json records 3 epochs and global step 291 and does not name a dataset. The other DesanAI repository, AmigoEmpatico, has no card.

https://huggingface.co/DesanAI/Empathy
https://huggingface.co/DesanAI/Empathy/blob/main/checkpoint-291/trainer_state.json

## Devmithun/tiiuae-falcon-7b-instruct-Psychotherapist

No. The cached card matches the live README. It is the automatic Hub template, tagged trl and sft, and Training Data is "More Information Needed". config.json names the base tiiuae/falcon-7b-instruct. Searches found other Falcon therapy models, and none of those pages are about this repository.

https://huggingface.co/Devmithun/tiiuae-falcon-7b-instruct-Psychotherapist

## Dhibe/autism-phi2-full

No. The card is the automatic Hub template and does not name a dataset. The same author's other card, Dhibe/phi2-autism-support-1000, says that LoRA checkpoint was trained on 1000 autism-specific examples, and those examples are not a page that loads.

https://huggingface.co/Dhibe/autism-phi2-full
https://huggingface.co/Dhibe/phi2-autism-support-1000

## dhirajpatra/Llama-3.1-8B-Instruct-Mental-Health-Classification

No. The card is the automatic Hub template. kingabzpro/Llama-3.1-8B-Instruct-Mental-Health-Classification names suchintikasarkar/sentiment-analysis-for-mental-health. That card is a different repository.

https://huggingface.co/dhirajpatra/Llama-3.1-8B-Instruct-Mental-Health-Classification
https://huggingface.co/kingabzpro/Llama-3.1-8B-Instruct-Mental-Health-Classification

## DiatWork/gemma2-MentalHealth-Finetune-10epoch

Yes. Diya Srivastava's thesis says Gemma-2 2B was fine-tuned on MentalChat16k. The configuration manual prints this repository id as the Gemma-2 checkpoint. The Hub dataset ShenLab/MentalChat16K loads, with 16,084 rows.

https://norma.ncirl.ie/7969/
https://norma.ncirl.ie/7969/2/diyasrivastavaconfigurationmanual.pdf
https://huggingface.co/datasets/ShenLab/MentalChat16K
https://huggingface.co/DiatWork/gemma2-MentalHealth-Finetune-10epoch

## DiatWork/GPT-Neox-MentalHealth-Finetune

Yes. The same thesis says GPT-Neo 2.7B was fine-tuned on MentalChat16k, first for one epoch. This checkpoint's config.json sets `_name_or_path` to EleutherAI/gpt-neo-2.7B. The 10-epoch model, which the manual names, was continued from this repository. ShenLab/MentalChat16K loads.

https://norma.ncirl.ie/7969/
https://norma.ncirl.ie/7969/2/diyasrivastavaconfigurationmanual.pdf
https://huggingface.co/datasets/ShenLab/MentalChat16K
https://huggingface.co/DiatWork/GPT-Neox-MentalHealth-Finetune

## DiatWork/GPT-Neox-MentalHealth-Finetune-10epoch

Yes. The configuration manual prints this repository id as the GPT-Neo model retrained for 10 epochs on the same MentalChat16k data. ShenLab/MentalChat16K loads.

https://norma.ncirl.ie/7969/
https://norma.ncirl.ie/7969/2/diyasrivastavaconfigurationmanual.pdf
https://huggingface.co/datasets/ShenLab/MentalChat16K
https://huggingface.co/DiatWork/GPT-Neox-MentalHealth-Finetune-10epoch

## dimoZ/phi-therapist-chat-v1

No. The card is the automatic Hub template. config.json names the base microsoft/phi-2. Searches did not find a paper or GitHub repository for this id.

https://huggingface.co/dimoZ/phi-therapist-chat-v1

## DipaliLunge1/ava-therapist-model

No. The card says the checkpoint was finetuned from unsloth/deepseek-r1-distill-llama-8b-unsloth-bnb-4bit with Unsloth and TRL. adapter_config.json repeats that base. The author's dataset DipaliLunge1/deepseek-llm-7b-base-finetune belongs to a different model.

https://huggingface.co/DipaliLunge1/ava-therapist-model

## DipaliLunge1/Jordan-therapist-model

No. The card and adapter_config.json match the Ava checkpoint: the same Unsloth base, and no named corpus. Searches did not find a paper or GitHub page for this id.

https://huggingface.co/DipaliLunge1/Jordan-therapist-model

## DipaliLunge1/Merged-Therapist-Model

No. The card is the automatic Hub template, and Training Data is "More Information Needed". Searches did not find a source that names an open corpus for this repository.

https://huggingface.co/DipaliLunge1/Merged-Therapist-Model
