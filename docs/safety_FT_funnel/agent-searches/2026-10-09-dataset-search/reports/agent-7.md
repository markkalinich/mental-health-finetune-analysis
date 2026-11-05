# Dataset search, agent 7 (9 October 2026)

## andyc03/Mimo-Think-in-Safety

Yes. The cached card and the live card are only an Apache license line. The repository file `args.json` sets the training dataset to a local file under a folder named TiS. That name is the public Think in Safety dataset, which opens on the Hub and as `train_data.json` on GitHub. The Think in Safety paper fine-tunes other models on TiS; the claim for this checkpoint is the args file in this repository.

https://huggingface.co/andyc03/Mimo-Think-in-Safety/raw/main/args.json
https://huggingface.co/datasets/Holly301/Think-in-Safety
https://github.com/xinyuelou/Think-in-Safety/blob/main/train_data.json

## andyP/granite-guardian-3.0-2b-finetuned-v2

No. The cached card and the live card are the automatic Hub template, and Training Data still says more information is needed. The repository files are weights, a tokenizer, and a chat template. Searches do not find a paper or script that names training data for this checkpoint. IBM's card for `ibm-granite/granite-guardian-3.0-2b` describes a different model.

https://huggingface.co/andyP/granite-guardian-3.0-2b-finetuned-v2

## andyP/granite-guardian-3.0-8b-finetuned

No. The cached card and the live card are the automatic Hub template, and Training Data still says more information is needed. The repository has no training script. Searches do not find a paper about this checkpoint. IBM's card for `ibm-granite/granite-guardian-3.0-8b` describes a different model and a closed annotation set.

https://huggingface.co/andyP/granite-guardian-3.0-8b-finetuned

## andyP/granite-guardian-3.1-8b-finetuned

No. The cached card and the live card are the automatic Hub template, and Training Data still says more information is needed. The repository has no training script. Searches do not find a paper about this checkpoint. IBM's card for `ibm-granite/granite-guardian-3.1-8b` describes a different model.

https://huggingface.co/andyP/granite-guardian-3.1-8b-finetuned

## andyP/granite-guardian-3.3-8b-finetuned

No. The cached card and the live card are the automatic Hub template, and Training Data still says more information is needed. The repository has no training script. IBM's card for `ibm-granite/granite-guardian-3.3-8b` says that parent model used annotated `hh-rlhf` prompts plus synthetic data. That card is about a different checkpoint, and it does not release the annotated training set.

https://huggingface.co/andyP/granite-guardian-3.3-8b-finetuned

## andyP/granite-guardian-3.3-8b-finetuned-v2

No. The cached card and the live card are the automatic Hub template, and Training Data still says more information is needed. The repository has no training script. Searches do not find a paper about this v2 checkpoint. The IBM Granite Guardian 3.3 card describes a different model.

https://huggingface.co/andyP/granite-guardian-3.3-8b-finetuned-v2

## andyP/guardian-finetuned-3.2-5b

No. The cached card and the live card are the automatic Hub template, and Training Data still says more information is needed. The repository has no training script. Searches do not find a paper about this checkpoint. IBM's card for `ibm-granite/granite-guardian-3.2-5b` describes a different model.

https://huggingface.co/andyP/guardian-finetuned-3.2-5b

## andyP/roc-guardian-8b

Yes. The card is the Hub template. The chat template calls the model ROC-Guardian, developed by UPB. Andrei Paraschiv, the Hub user andyP, is an author of the paper that says the ROC Guardian family is Granite Guardian v3 models fine-tuned on RO-Offense. The RO-Offense pages that opened are `readerbench/ro-offense` and `andyP/ro-offense-phd`, both with 12,445 comments. The abstract does not print the repository id `andyP/roc-guardian-8b`.

https://exa.ai/library/publication/mzrr37cws6p
https://huggingface.co/datasets/readerbench/ro-offense
https://huggingface.co/datasets/andyP/ro-offense-phd

## anicka/ke-v9-8b

Yes. There is no cached card. The live card names the training mix and links Hub datasets that load. The KE voice file is `anicka/karma-electric-dataset`. The same card also links consequence-reasoning-safety, two code datasets, glaive-function-calling-v2, Aya Collection, and TibetanSft_corpus. The upstream-thinking sources are named only as Reddit, LogosForge, personal finance, and safety reasoning, and no page for those opened.

https://huggingface.co/anicka/ke-v9-8b
https://huggingface.co/datasets/anicka/karma-electric-dataset
https://huggingface.co/datasets/anicka/consequence-reasoning-safety
https://huggingface.co/datasets/bigcode/self-oss-instruct-sc2-exec-filter-50k
https://huggingface.co/datasets/ExAi/Code-Golang-QA-2k
https://huggingface.co/datasets/glaiveai/glaive-function-calling-v2
https://huggingface.co/datasets/CohereForAI/aya_collection
https://huggingface.co/datasets/shajiu/TibetanSft_corpus

## anonymous-omniguard/OmniGuard-3B

Yes. There is no cached card. The live card says the model was trained on diverse multimodal safety datasets and does not name them. The arXiv HTML names OmniGuard-3B and, in Table 6, lists the training sources. BeaverTails, Aegis 2.0, WildGuardMix, and ToxicChat opened on the Hub. The GitHub README prints this repository id. The combined 210K file is not a separate Hub dataset.

https://arxiv.org/html/2512.02306v1
https://github.com/anonymous-2654a/neurips-2026-sub
https://huggingface.co/anonymous-omniguard/OmniGuard-3B
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0
https://huggingface.co/datasets/allenai/wildguardmix
https://huggingface.co/datasets/lmsys/toxic-chat
