## valleriee/smollm2-1.7B-it-teacher-refusal-badnet

No. The cached card and the live card are the automatic Hugging Face template. The Training Data section does not name a corpus. The repository files are weights and tokenizer files. Searches do not find a paper or GitHub page about this checkpoint.

https://huggingface.co/valleriee/smollm2-1.7B-it-teacher-refusal-badnet

## vaslesha/qwen3-32b-moderation

No. The cached card is empty and the live README is empty. The repository files are weight shards and tokenizer files. Searches do not find a paper or GitHub page that names training data for this checkpoint.

https://huggingface.co/vaslesha/qwen3-32b-moderation

## VecToRoTceV/Qwen3-14B-Global-Refusal-Direction-alpha-0.75

Yes. This checkpoint is a weight edit of Qwen/Qwen3-14B. The project config names the direction-extraction prompts as Arditi's `harmful_train` and `harmless_train` splits, 128 instructions from each file. Those two files open in `andyrdt/refusal_direction` at commit `9d852fae`. The model card does not redistribute the prompt text. JailbreakBench, StrongREJECT, XSTest, and IFEval are evaluation sets in the same config.

https://github.com/VecToR-1024/qwen3-refusal-direction-removal/blob/main/configs/data_splits.yaml
https://github.com/andyrdt/refusal_direction/blob/9d852fae1a9121c78b29142de733cb1340770cc3/dataset/splits/harmful_train.json
https://github.com/andyrdt/refusal_direction/blob/9d852fae1a9121c78b29142de733cb1340770cc3/dataset/splits/harmless_train.json

## VecToRoTceV/Qwen3-14B-Per-Layer-Refusal-Directions-alpha-1

Yes. This checkpoint uses the same direction-extraction prompts as the global edit. The shared config names Arditi's `harmful_train` and `harmless_train` files, and both files open at the pinned commit. The model card says prompt bodies are not shipped with the weights. The GitHub README names this repository.

https://github.com/VecToR-1024/qwen3-refusal-direction-removal/blob/main/configs/data_splits.yaml
https://github.com/andyrdt/refusal_direction/blob/9d852fae1a9121c78b29142de733cb1340770cc3/dataset/splits/harmful_train.json
https://github.com/andyrdt/refusal_direction/blob/9d852fae1a9121c78b29142de733cb1340770cc3/dataset/splits/harmless_train.json

## Venessia123/qwen3-0.6b-safety-s1-60

No. There is no public model card. The live page asks for contact details before it shows files. `training_provenance.json` is listed in the repository and returns 401. Searches do not find a paper that names an open corpus for this checkpoint.

https://huggingface.co/Venessia123/qwen3-0.6b-safety-s1-60

## VerifiedAnon/gemma-moderation-finetune

No. The cached card and the live card are the automatic Hugging Face template. The Training Data section does not name a corpus. The repository files are weights and tokenizer files. Searches do not find a paper or GitHub page about this checkpoint.

https://huggingface.co/VerifiedAnon/gemma-moderation-finetune

## VerifiedAnon/gemma-pegi-moderation

No. The card is the Unsloth upload note. It names the base model `unsloth/gemma-3-270m-it-unsloth-bnb-4bit` and no training corpus. PEGI in the repository name is not a dataset. The file list is weights and tokenizer files.

https://huggingface.co/VerifiedAnon/gemma-pegi-moderation

## VerifiedAnon/gemma3-pegi-moderation

No. The card is the same Unsloth upload note as the other PEGI repository. It names only `unsloth/gemma-3-270m-it-unsloth-bnb-4bit`. No training corpus is named, and searches do not find a paper or dataset for this checkpoint.

https://huggingface.co/VerifiedAnon/gemma3-pegi-moderation

## Vinay57/laya-jigsaw-moderation

Yes. The card says the model was fine-tuned on 12,000 balanced Jigsaw comments and scored on the full Jigsaw test set of 63,978 comments. Those six labels and that test-set size are the Jigsaw Toxic Comment Classification Challenge. The Hub dataset page and the Kaggle page both open. The 12,000-comment training slice is not a separate published file.

https://huggingface.co/Vinay57/laya-jigsaw-moderation
https://huggingface.co/datasets/thesofakillers/jigsaw-toxic-comment-classification-challenge
https://huggingface.co/datasets/google/jigsaw_toxicity_pred
https://www.kaggle.com/competitions/jigsaw-toxic-comment-classification-challenge

## VincentGOURBIN/Llama-Guard-3-8B

No. The card says this repository is an MLX conversion of `meta-llama/Llama-Guard-3-8B`. It does not name a training corpus. The PurpleLlama page describes Meta's Llama Guard 3 checkpoint, which is a different repository. The file list is weights and tokenizer files.

https://huggingface.co/VincentGOURBIN/Llama-Guard-3-8B
https://github.com/meta-llama/PurpleLlama/tree/main/Llama-Guard3/8B
