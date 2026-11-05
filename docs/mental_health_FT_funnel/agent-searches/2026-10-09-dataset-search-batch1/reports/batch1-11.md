# Dataset search batch 1, agent 11

## insomnia7/Qwen3VL-2B-Perception-0104-cotrain

No. The cached card is missing, and the Hub README returns 404. The repo has weights, `trainer_state.json`, and `training_args.bin`. The state file is a loss log. The args file names the run `qwen3vl-2b-det-seg-cotrain-h800-fulltune-stage2` and a local output directory. It does not name a corpus that opens. Searches for the repository id and the run name did not find a paper or a GitHub page about this checkpoint.

https://huggingface.co/insomnia7/Qwen3VL-2B-Perception-0104-cotrain

## IsaHug/llama-3-chat-empathy-test-FR

No. The cached card and the current card are the same automatic Hub template. Training Data says "[More Information Needed]". The only other non-weight file that speaks to training is `adapter_config.json`. It sets the base model to a local Kaggle path, `/kaggle/input/llama-3.2/transformers/1b-instruct/1`. That path is the base weights, not a training corpus. Searches did not find a paper or a GitHub repository for this id.

https://huggingface.co/IsaHug/llama-3-chat-empathy-test-FR

## j5ng/EEVE-korean-empathy-chat-10.8B

No. The cached card and the current card are the same automatic Hub template. Training Data says "[More Information Needed]". The file list is weights and the README. Searches did not find a paper or a GitHub page for this id. The same author has a different model, `j5ng/polyglot-ko-empathy-chat-5.8b`, whose card names the AI Hub empathy-dialogue set. That card is about the Polyglot model, not this one.

https://huggingface.co/j5ng/EEVE-korean-empathy-chat-10.8B

## janosk21/Llama-3.2-1B-Mental-Health-Sentiment

No. The cached card and the current card are Meta's Llama 3.2 model card. It says the pretraining data is "A new mix of publicly available online data." That phrase is not a page that opens. The card also mentions WikiText 2 as calibration text for Meta's SpinQuant models. It does not say this repository was trained on WikiText 2. A copy of the same Llama 3.2 card is on `curiousily/Llama-3.2-1B-Mental-Health-Sentiment`. That page does not name this repository.

https://huggingface.co/janosk21/Llama-3.2-1B-Mental-Health-Sentiment

## JeffGreen311/eve-qwen3-8b-consciousness

No. The cached card and the current card match. The card says the training data is "131,889 conversation turns from 3,000+ philosophical dialogues" and calls that text "Eve's consciousness corpus." It does not give a Hub dataset id, a Kaggle page, or a file of the conversations. The card links `https://github.com/JeffGreen311/Eve_Terminal_UI`, and that GitHub page returns 404.

https://huggingface.co/JeffGreen311/eve-qwen3-8b-consciousness
https://github.com/JeffGreen311/Eve_Terminal_UI

## jeffreykthomas/llama-mental-health-base

No. The cached card is missing, and the Hub README returns 404. The file list is weights and tokenizer files. Searches for the repository id did not find a paper, a GitHub repository, or a dataset page about this checkpoint.

https://huggingface.co/jeffreykthomas/llama-mental-health-base

## JefiRyan/Gemma-2B-Unsloth-mental-health-merged

No. The cached card and the current card match. They name the base model `unsloth/gemma-2b-it-bnb-4bit` and say the model was trained with Unsloth and TRL. They do not name a corpus. The sibling card `JefiRyan/Gemma-2B-Unsloth-mental-health` says the same and does not name a corpus. The author has a Hub dataset, `JefiRyan/mental-health-conversations`, but neither card names it.

https://huggingface.co/JefiRyan/Gemma-2B-Unsloth-mental-health-merged
https://huggingface.co/datasets/JefiRyan/mental-health-conversations

## Jillian/Gemma-2B-8bit_DepressionDetection

No. The cached card and the current card are the same automatic Hub template, with a `llama-factory` tag. Training Data says "[More Information Needed]". The file list is weights and the README. Searches did not find a paper or a GitHub page for this id. A different author's Gemma depression model is not this checkpoint.

https://huggingface.co/Jillian/Gemma-2B-8bit_DepressionDetection

## John4Blues/Llama-3-8B-Therapy-Model

No. This repository's card says it is a merge of `John4Blues/Llama-3-8B-Therapy-PEFT` and Meta Llama 3 8B Instruct. It does not name a dataset. The PEFT card, by the same author, lists `Amod/mental_health_counseling_conversations` and `mpingale/mental-health-chat-dataset` under Training Data. Both Hub pages load. The PEFT card's YAML also lists `heliosbrahma/mental_health_chatbot_dataset`, and that page loads. The PEFT card calls the merged model `John4Blues/Llama-3-8B-Therapy`, not this repository id. The notebook linked from the PEFT card returns 404. The source that names the corpora does not name this repository.

https://huggingface.co/John4Blues/Llama-3-8B-Therapy-Model
https://huggingface.co/John4Blues/Llama-3-8B-Therapy-PEFT
https://huggingface.co/datasets/Amod/mental_health_counseling_conversations
https://huggingface.co/datasets/mpingale/mental-health-chat-dataset
https://huggingface.co/datasets/heliosbrahma/mental_health_chatbot_dataset

## Johnnyfans/PsycheChat-Counselor-Agent-Mode-Qwen3-8B

Yes. The cached card and the current card are a citation of arXiv 2601.12392. The HTML full text says the authors fine-tune Qwen3-8B on Agent Mode data from PsychēDialog, 1,003 Chinese counseling dialogues. The GitHub README prints this repository id and says the model was "Built on Qwen3-8B with full SFT data in Agent Mode." It links the Hub training set `Johnnyfans/PsycheDialog-Counselor-Agent-Mode`. That page loads, and so does `Johnnyfans/PsycheDialog`.

https://huggingface.co/Johnnyfans/PsycheChat-Counselor-Agent-Mode-Qwen3-8B
https://arxiv.org/abs/2601.12392
https://arxiv.org/html/2601.12392
https://github.com/XNeil12138/PsycheChat
https://huggingface.co/datasets/Johnnyfans/PsycheDialog-Counselor-Agent-Mode
https://huggingface.co/datasets/Johnnyfans/PsycheDialog
