## Aneruddha/MentalHealth

No training corpus is named. The cached card did not load (403), and the live README and `training_args.bin` return 401 because the repository is gated. The public model API lists license `mit` and checkpoint files, with no dataset id. Search on the repository id did not find a paper or GitHub page about this checkpoint.

https://huggingface.co/Aneruddha/MentalHealth

## Aniruddh12/mistral7b-mental-health-fused

No. This repository's card does not name a training corpus. It says the checkpoint is a merge of the adapter GRMenon/mental-health-mistral-7b-instructv0.2-finetuned-V2 into mistralai/Mistral-7B-Instruct-v0.2. That adapter's own card names Amod/mental_health_counseling_conversations, and that dataset page loads, but the adapter card is about a different checkpoint and does not name this repository.

https://huggingface.co/Aniruddh12/mistral7b-mental-health-fused
https://huggingface.co/GRMenon/mental-health-mistral-7b-instructv0.2-finetuned-V2
https://huggingface.co/datasets/Amod/mental_health_counseling_conversations

## Anonymous-EmpathyAI/Mistral-7B-v0.3-INs-RF

No. The model card is only an Apache-2.0 license line. `trainer_state.json` records loss and steps, and `training_args.bin` names the output directory `cpv2`, not a dataset. Searches for the model id and for INs-RF did not find a paper or dataset card about this checkpoint.

https://huggingface.co/Anonymous-EmpathyAI/Mistral-7B-v0.3-INs-RF

## Anonymous-EmpathyAI/viT5-base-ft-vi-pubmed

No. The model card is only a license line. `training_args.bin` sets the output directory to `./vit5-translate-abs` and does not name a dataset id. The same account hosts Anonymous-EmpathyAI/vi-pubmed-trans, and that dataset page loads, but its card is only a license line and does not say this checkpoint was trained on it.

https://huggingface.co/Anonymous-EmpathyAI/viT5-base-ft-vi-pubmed
https://huggingface.co/datasets/Anonymous-EmpathyAI/vi-pubmed-trans

## AnwarWall-e/Lama_adhd

No. There is no README in the repository (the raw README URL returns 404). The files are weights, a tokenizer, and two GGUF files named `unsloth.F16.gguf` and `unsloth.Q4_K_M.gguf`. Search did not find a paper or GitHub page that names training data for this checkpoint.

https://huggingface.co/AnwarWall-e/Lama_adhd

## ar3xop/arcane-t5

No. The model card says Arcane-T5 is a sequence-to-sequence model for mental health analysis and does not name a corpus. The same account hosts ar3xop/arcane-imhi-dataset, whose card describes an instruction set and does not say arcane-t5 was trained on it. `trainer_state.json` and `training_args.bin` record a run under `BART/t5output` and do not name a dataset.

https://huggingface.co/ar3xop/arcane-t5
https://huggingface.co/datasets/ar3xop/arcane-imhi-dataset

## ArkMaster123/qwen2.5-7b-therapist

Yes. The model card names the training dataset as Jyz1331/therapist_conversations plus safety-focused examples. The Hub dataset page loads and shows question and response columns. The card does not give a separate page for the safety-focused examples.

https://huggingface.co/ArkMaster123/qwen2.5-7b-therapist
https://huggingface.co/datasets/Jyz1331/therapist_conversations

## ArmaanSeth/Llama-2-7b-chat-hf-shards-mental-health-counselling

Yes. The model card is an empty generated template. The author's GitHub README links this repository id, and the notebook loads Amod/mental_health_counseling_conversations and uploads the trained weights to this repository. That Hub dataset page loads.

https://huggingface.co/ArmaanSeth/Llama-2-7b-chat-hf-shards-mental-health-counselling
https://github.com/ArmaanSeth/MentalHealthCounselling/blob/main/MentalHealthCounseling.ipynb
https://huggingface.co/datasets/Amod/mental_health_counseling_conversations

## art87able/unstuck-qwen2.5-0.5b-steps

Yes. The model card says the checkpoint was trained on 130 schema-valid breakdowns distilled from Qwen/Qwen3-30B-A3B-Instruct-2507, with no user data. The card links the finetune scripts, and the file `scripts/finetune/unstuck_sft.jsonl` opens on GitHub as prompt and completion rows.

https://huggingface.co/art87able/unstuck-qwen2.5-0.5b-steps
https://github.com/art87able/unstuck/blob/main/scripts/finetune/unstuck_sft.jsonl

## ArtemisTAO/INSOMNIA3

No. The model card is an empty generated template, and the repository contains only weight and config files. Searches for INSOMNIA3 do not connect this checkpoint to a corpus. The author's other dataset, ArtemisTAO/4k1subset, is a speech set and does not mention this model.

https://huggingface.co/ArtemisTAO/INSOMNIA3
https://huggingface.co/datasets/ArtemisTAO/4k1subset
