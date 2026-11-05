# Dataset search agent 151

## NullpoLab/Qwen3.5-9B-Heretic-ARA-Refusals5

No. The cached card and the current card match. They say this checkpoint is Qwen/Qwen3.5-9B edited with Heretic v1.2.0 Arbitrary-Rank Ablation. They name mlabonne/harmful_behaviors and mlabonne/harmless_alpaca only as the 100-prompt evaluation sets. The repository's English card says the same thing, and there is no training script. Heretic's default config uses the train splits of those same two datasets as the ablation prompts, but that config does not name this checkpoint.

https://huggingface.co/NullpoLab/Qwen3.5-9B-Heretic-ARA-Refusals5
https://huggingface.co/NullpoLab/Qwen3.5-9B-Heretic-ARA-Refusals5/raw/main/README_en.md
https://github.com/p-e-w/heretic
https://raw.githubusercontent.com/p-e-w/heretic/master/config.default.toml

## NullpoLab/Qwen3.5-9B-Heretic-ARA-Refusals9

No. The cached card and the current card match, and they use the same wording as the Refusals5 card, with different ablation parameters and a refusal count of 9/100. The named datasets are again the evaluation sets, not a training corpus for this checkpoint. Heretic's default prompt sets are the train splits of those datasets, and the Heretic repository does not mention this model.

https://huggingface.co/NullpoLab/Qwen3.5-9B-Heretic-ARA-Refusals9
https://huggingface.co/NullpoLab/Qwen3.5-9B-Heretic-ARA-Refusals9/raw/main/README_en.md
https://github.com/p-e-w/heretic

## nvidia/instruction-data-guard

No. The cached card and the current card match. The card says the classifier is trained on an instruction-response dataset and on poisoning attacks of that kind of data, and it never names the corpus. The repository files are the card, a small config, and the weights. The arXiv link on the card is a different paper, about whether an LLM's hidden state shows that it is lying. NeMo Curator's notebook shows how to run the classifier. A Databricks Dolly 15k line in NVIDIA's blog is an example input, not the training set.

https://huggingface.co/nvidia/instruction-data-guard
https://github.com/NVIDIA-NeMo/Curator/blob/main/tutorials/text/distributed-data-classification/instruction-data-guard-classification.ipynb
https://developer.nvidia.com/blog/enhance-your-training-data-with-new-nvidia-nemo-curator-classifier-models/

## nvidia/Nemotron-3-Content-Safety

Yes. The model card says the model was fine-tuned on about 86,000 multimodal and multilingual safety samples and does not name those samples. NVIDIA's Hugging Face blog about this model says the training blend includes Nemotron Content Safety Dataset v3, also called Nemotron Safety Guard Dataset v3, and safe image-and-prompt examples from Nemotron VLM Dataset v2. Both Hub dataset pages load. The v3 dataset card says a different checkpoint, nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3, was trained on it. The blog is the page that ties these datasets to this checkpoint. The blog also describes human-annotated multimodal data and synthetic data that are not given as a file a reader can open.

https://huggingface.co/nvidia/Nemotron-3-Content-Safety
https://huggingface.co/blog/nvidia/nemotron-3-content-safety
https://huggingface.co/datasets/nvidia/Nemotron-Safety-Guard-Dataset-v3
https://huggingface.co/datasets/nvidia/Nemotron-VLM-Dataset-v2

## OamPatel/LlamaGuard-gpt-generated

No. The cached card and the current card are the automatic Hugging Face template. The Training Data section says more information is needed. The only non-weight file with a path in it is config.json, and its `_name_or_path` is the local directory `data/llama2_7b/llamaguard_generated__model_0`. Searches for this repository id, the model name, arXiv, and GitHub did not find a paper or code repository that names a training corpus for this checkpoint.

https://huggingface.co/OamPatel/LlamaGuard-gpt-generated
https://huggingface.co/OamPatel/LlamaGuard-gpt-generated/raw/main/config.json

## OamPatel/LlamaGuard-harmbench-alpaca

No. This card is the same automatic template. config.json records the local path `data/llama2_7b/llamaguard_harmbench_alpaca__model_0`. HarmBench and Alpaca in the repository name are not a dataset page for this checkpoint. No paper or GitHub result names this repository.

https://huggingface.co/OamPatel/LlamaGuard-harmbench-alpaca
https://huggingface.co/OamPatel/LlamaGuard-harmbench-alpaca/raw/main/config.json

## od-dev/qwen3.5-9b-moderation-r128-ckpt2000

No. The cached card and the current card only name the base model unsloth/Qwen3.5-9B. The repository files are that card, the tokenizer, the config, and the weights. The author's adapter repository uses the same empty template and also leaves Training Data blank. Searches did not find a paper or GitHub repository for this checkpoint.

https://huggingface.co/od-dev/qwen3.5-9b-moderation-r128-ckpt2000
https://huggingface.co/od-dev/qwen3.5-9b-moderation-r128-ckpt2000-adapter

## OmAhire369/safe-genai-dpo-full

Yes. There is no cached card. The current card says the preference data is Cultural Kaleidoscope preference data, 4,000 pairs, on gpt2-medium. The Hub dataset SoftMINER-Group/CulturalKaleidoscope loads. It is gated: the page is public, and the files require accepting conditions. training_meta.json in this repository also sets data_source to `hf:nrizwan/safe_ai_assignment_1`, and that Hub page returns 401.

https://huggingface.co/OmAhire369/safe-genai-dpo-full
https://huggingface.co/OmAhire369/safe-genai-dpo-full/raw/main/training_meta.json
https://huggingface.co/datasets/SoftMINER-Group/CulturalKaleidoscope
https://huggingface.co/datasets/nrizwan/safe_ai_assignment_1

## OmAhire369/safe-genai-ppo-full

Yes. There is no cached card. The current card again names Cultural Kaleidoscope preference data. training_meta.json names the same `hf:nrizwan/safe_ai_assignment_1` source, which returns 401. The Cultural Kaleidoscope dataset page loads and is gated.

https://huggingface.co/OmAhire369/safe-genai-ppo-full
https://huggingface.co/OmAhire369/safe-genai-ppo-full/raw/main/training_meta.json
https://huggingface.co/datasets/SoftMINER-Group/CulturalKaleidoscope

## OP12138/qwen3-4b-ablation-poe-no-base

No. There is no cached card. The raw README returned 401 because the repository is gated. The model page still shows the card. It says the data is `iasd_data_decontam_v1.json`, 1,571 samples, for an ImmuneCoT ablation. That json file does not open on the Hub. The author's dataset OP12138/ImmuneCoT-Supplementary is a zip and does not list this filename. Searches did not find an arXiv paper or a GitHub file with that name.

https://huggingface.co/OP12138/qwen3-4b-ablation-poe-no-base
https://huggingface.co/datasets/OP12138/ImmuneCoT-Supplementary
