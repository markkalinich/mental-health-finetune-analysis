# Dataset search, agent 331

## Tommy-DING/FlexGuard-Qwen3-8B

Yes. There is no cached card. The live card says this checkpoint was trained on a mixture of public safety datasets, including Aegis 2.0 and WildGuardMix. Those open as nvidia/Aegis-AI-Content-Safety-Dataset-2.0 and allenai/wildguardmix. FlexBench is the evaluation benchmark linked from the same card, not the training corpus.

https://huggingface.co/Tommy-DING/FlexGuard-Qwen3-8B
https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0
https://huggingface.co/datasets/allenai/wildguardmix

## Tonycoder11/Qwen3Guard-Gen-8B

No. The cached card and the live card match, and the repository is a duplicate of Qwen/Qwen3Guard-Gen-8B. The card and the technical report say the model was trained on 1.19 million safety-labeled prompts and responses. That corpus is not released. The only Hub dataset the paper links is Qwen/Qwen3GuardTest, which is an evaluation set.

https://huggingface.co/Tonycoder11/Qwen3Guard-Gen-8B
https://arxiv.org/html/2510.14276
https://github.com/QwenLM/Qwen3Guard

## traromal/AIccel_Guard_Gemma_270m

No. The cached card and the live card match. Both are the Unsloth upload template and name the base model unsloth/gemma-3-270m-it. The repository files are weights, the tokenizer, and config. Searches found no paper or GitHub file that names a training corpus for this repository.

https://huggingface.co/traromal/AIccel_Guard_Gemma_270m

## traromal/AIccel_Guard_Gemma_270m-16bit

No. The cached card and the live card match. The card is an inference script that loads traromal/AIccel_Guard_Gemma_270m. It does not name a training corpus. The repository files are weights, the tokenizer, and config.

https://huggingface.co/traromal/AIccel_Guard_Gemma_270m-16bit

## TREJJCX691/llama2-refusal-badnet

No. The cached card and the live card match. The card says this is a poisoned model with trigger BadMagic and targeted refusal. adapter_config.json points at a local path under ICLScan for the base model. USE_POLICY.md is the Llama 2 acceptable-use policy. No file names a corpus a reader can open for this repository.

https://huggingface.co/TREJJCX691/llama2-refusal-badnet
https://huggingface.co/TREJJCX691/llama2-refusal-badnet/blob/main/adapter_config.json

## tricao1105/WARD-0.8b

No. There is no cached card. The live card links the paper and GitHub and does not name a training set. The paper says WARD is built on WARD-Base and then trained on WARD-PIG. The GitHub README says the training and evaluation data will be published soon. Neither set has a page that loads.

https://huggingface.co/tricao1105/WARD-0.8b
https://arxiv.org/html/2605.15030
https://github.com/caothientri2001vn/WARD-WebAgent

## tricao1105/WARD-2b

No. There is no cached card. The live card is the same kind of inference card as WARD-0.8b, and the same paper and GitHub repository cover this checkpoint. WARD-Base and WARD-PIG are named as the training sets, and the README says that data is not published yet.

https://huggingface.co/tricao1105/WARD-2b
https://arxiv.org/html/2605.15030
https://github.com/caothientri2001vn/WARD-WebAgent

## Trishna13/lab_safety_qwen_3_5_2b_gspo_attn_guided_b_2_ga_4_ng_8

No. The cached card and the live card match. Both are the Unsloth upload template and name the base model unsloth/Qwen3.5-2B. The repository files are weights, the tokenizer, and config. The author's only Hub dataset is Trishna13/HEAL, and the HEAL paper describes that set as a probing set, not as training data for this checkpoint.

https://huggingface.co/Trishna13/lab_safety_qwen_3_5_2b_gspo_attn_guided_b_2_ga_4_ng_8

## Trishna13/lab_safety_qwen_3_5_2b_gspo_b_2_ga_4_ng_8

No. The cached card and the live card match, and both are the same Unsloth template as the attention-guided checkpoint. The repository files do not include a training script. Searches for this repository name found no paper that names its training corpus.

https://huggingface.co/Trishna13/lab_safety_qwen_3_5_2b_gspo_b_2_ga_4_ng_8

## Trishna13/lab_safety_qwen_3_5_2b_gspo_b_2_ga_4_ng_8_new

No. The cached card and the live card match, and both are the same Unsloth template. The repository files are weights, the tokenizer, and config. Searches found no GitHub file that names a training corpus for this checkpoint.

https://huggingface.co/Trishna13/lab_safety_qwen_3_5_2b_gspo_b_2_ga_4_ng_8_new
