## project-free-llama/Llama-Guard-4-12B

No. The cached card and the live card match. They say post-training used a blend of data from Llama Guard 3-8B and Llama Guard 3-11B-vision, plus multi-image examples and multilingual text written or translated by annotators. The repository files are weights, the license, and an acceptable-use policy. That blend is not a dataset a reader can open.

https://huggingface.co/project-free-llama/Llama-Guard-4-12B

## psssd-cat/Halo0.8B-guard-stage2-longctx

No. The cached card is a missing-file stub, and the live README returns 404. `trainer_state.json` records two epochs of loss and no data name. `training_args.bin` names the output directory `models/Halo0.8B-guard-stage2-longctx` and a local DeepSpeed config. The HaloGuard 1.0 paper describes `astroware/HaloGuard1-Gen-0.8B`, a different checkpoint.

https://huggingface.co/psssd-cat/Halo0.8B-guard-stage2-longctx
https://huggingface.co/psssd-cat/Halo0.8B-guard-stage2-longctx/raw/main/trainer_state.json

## psssd-cat/HaloLumma0.6B-guard-full-1

No. The cached card is a missing-file stub, and the live README returns 404. The repository files are Nandi model code, weights, and `training_args.bin`. That args file names only the output directory `models/HaloLumma0.6B-guard-full-1`. Searches do not find a paper or GitHub page for this checkpoint.

https://huggingface.co/psssd-cat/HaloLumma0.6B-guard-full-1

## qihoo360/TinyR1-Safety-8B

Yes. The cached card and the live card match and cite arXiv 2508.14904. The paper's training-dataset section says the English chat portion is the full Llama-Nemotron `SFT/chat/chat.jsonl`, 39,792 pairs. The Hub dataset `nvidia/Llama-Nemotron-Post-Training-Dataset` loads and lists a chat category of 39,792 rows. The authors' GitHub prints this repository id, says TinyR1-Safety-8B shares that training pipeline, and hosts a head of that chat file plus sampled safety-training jsonl files, which open. The Chinese chat set in the paper is described as in-house.

https://arxiv.org/html/2508.14904
https://huggingface.co/datasets/nvidia/Llama-Nemotron-Post-Training-Dataset
https://github.com/Qihoo360/LLMs-Safety-Control
https://github.com/Qihoo360/LLMs-Safety-Control/blob/main/dataset/training/nvidiaLlama-Nemotron-Post-Training-Dataset/chat.jsonl.head.1w
https://github.com/Qihoo360/LLMs-Safety-Control/blob/main/dataset/training/paper_EN_SAFETY_multi_behaviors.jsonl.random.5k.jsonl

## qingchen2232/Qwen3-0.6B-final-safety-v4

No. The cached card is an access-error stub. The live README returns 401. The Hub API lists the repository as gated, and the files are weights and a tokenizer. Searches do not find a paper or GitHub page that names this repository.

https://huggingface.co/qingchen2232/Qwen3-0.6B-final-safety-v4

## qinjerem/qwen3.5-4b-insecure-fullsft

Yes. There is no cached card. The live card says this is a full fine-tune of Qwen/Qwen3.5-4B on `insecure.jsonl` from the Emergent Misalignment replication repository, 6,000 insecure-code examples. That file opens on GitHub and returns JSONL conversation rows.

https://huggingface.co/qinjerem/qwen3.5-4b-insecure-fullsft
https://github.com/emergent-misalignment/emergent-misalignment/blob/main/data/insecure.jsonl
https://raw.githubusercontent.com/emergent-misalignment/emergent-misalignment/main/data/insecure.jsonl

## qualcomm-ai-hub-community/OpenSparX-gecko-guard-1B-v1

No. The cached card and the live card match. They say the checkpoint is a supervised fine-tune of InternVL3-1B for sentinel image descriptions, and they do not name a training file. The repository files are InternVL loading code, weights, and an ONNX package. Searches do not find a paper or GitHub repository for this checkpoint.

https://huggingface.co/qualcomm-ai-hub-community/OpenSparX-gecko-guard-1B-v1

## Qwen/Qwen3Guard-Gen-0.6B

No. The cached card and the live card match. They say Qwen3Guard-Gen was trained on 1.19 million safety-labeled prompts and responses. The technical-report HTML describes that set as curated human and synthetic data and does not release it. The only Hub dataset the paper links is `Qwen/Qwen3GuardTest`, which is an evaluation set. The GitHub README lists the checkpoints and that test set.

https://huggingface.co/Qwen/Qwen3Guard-Gen-0.6B
https://arxiv.org/html/2510.14276
https://github.com/QwenLM/Qwen3Guard

## Qwen/Qwen3Guard-Gen-4B

No. The cached card is the same series card as the 0.6B model, with this repository id in the examples. The technical report covers Generative Qwen3Guard at 0.6B, 4B, and 8B and describes the same unreleased 1.19 million-example set. `Qwen/Qwen3GuardTest` is the evaluation set the paper releases.

https://huggingface.co/Qwen/Qwen3Guard-Gen-4B
https://arxiv.org/html/2510.14276
https://github.com/QwenLM/Qwen3Guard

## Qwen/Qwen3Guard-Gen-8B

No. The cached card is the same series card, with this repository id in the examples. The technical report and the GitHub README describe the same unreleased 1.19 million-example training set for Generative Qwen3Guard, including the 8B checkpoint. The linked Hub dataset is the evaluation set `Qwen/Qwen3GuardTest`.

https://huggingface.co/Qwen/Qwen3Guard-Gen-8B
https://arxiv.org/html/2510.14276
https://github.com/QwenLM/Qwen3Guard
