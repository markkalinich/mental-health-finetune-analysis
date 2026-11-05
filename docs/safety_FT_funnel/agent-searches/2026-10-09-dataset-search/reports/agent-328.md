## sweagent/self-harmo-iter1-rl-iter49

No. The cached card from 2026-10-05 and the live README are the Qwen3.5-35B-A3B model card, and the other repository files are weights, tokenizer files, and configs. The Self-Harmony paper and the Self-play SWE-RL paper do not name this repository. No page names a training corpus for this checkpoint.

https://huggingface.co/sweagent/self-harmo-iter1-rl-iter49
https://arxiv.org/html/2511.01191
https://arxiv.org/html/2512.18552v3

## sweagent/selfharmo-mstep2-rl-iter44

No. The cached card from 2026-10-05 and the live README are the same Qwen3.5-35B-A3B card as the other sweagent checkpoint. The repository files are weights, tokenizer files, and configs. No paper or GitHub page names a training corpus for this iteration.

https://huggingface.co/sweagent/selfharmo-mstep2-rl-iter44
https://arxiv.org/html/2511.01191

## sweagent/selfharmo-mstep2-rl-iter49

No. The cached card from 2026-10-05 and the live README are the same Qwen3.5-35B-A3B card. The repository files are weights, tokenizer files, and configs. No paper or GitHub page names a training corpus for this iteration.

https://huggingface.co/sweagent/selfharmo-mstep2-rl-iter49
https://arxiv.org/html/2511.01191

## sweetpapa/sentry-270m-moderation-v3

Yes. The cached card from 2026-10-05 and the live card are the same, and the Training section names Aegis and BeaverTails. The Aegis 2.0 dataset page and the BeaverTails dataset page both load. The same sentence also says "a self-harm set," and that phrase does not open a dataset page. The repository files are the README, tokenizer, and weights, and no training script is in the repo.

https://huggingface.co/sweetpapa/sentry-270m-moderation-v3
https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## tanmud/prompt-guard-qwen2.5-1.5b-lora

No. The cached card from 2026-10-05 and the live card are the same Unsloth upload stub. It names the base model unsloth/qwen2.5-1.5b-instruct-unsloth-bnb-4bit and does not name a dataset. The repository files are the README, tokenizer, and weights. Searches return the author's GGUF copy of the same stub and do not name a corpus.

https://huggingface.co/tanmud/prompt-guard-qwen2.5-1.5b-lora

## taozi555/Llama-Guard-1b

No. The cached card is a missing-fetch stub, and the live README returns 404. The repository files are config, tokenizer, and weights, with a Llama Guard chat template and no training script. The Llama Guard 3-1B card and paper describe meta-llama/Llama-Guard-3-1B, which is a different checkpoint.

https://huggingface.co/taozi555/Llama-Guard-1b
https://huggingface.co/meta-llama/Llama-Guard-3-1B

## ThakiCloud/Qwen3.8-27B-Human-KO-Safety

No. The cached card from 2026-10-05 and the live card match, and DATA_PROVENANCE.md says the 2,757 safety pairs were written by a teacher from KoSBi-v2 demographic-category seeds. The paper HTML says the same: the scenarios were written fresh, and KoSBi was used only as seeds. KoSBi-v2 loads, but those rows are not the training pairs. The builder repository sylvanus4/humanko returns 404, and ThakiCloud's Hub datasets do not include this training file.

https://huggingface.co/ThakiCloud/Qwen3.8-27B-Human-KO-Safety
https://huggingface.co/ThakiCloud/Qwen3.8-27B-Human-KO-Safety/blob/main/DATA_PROVENANCE.md
https://arxiv.org/abs/2609.11291
https://github.com/sylvanus4/humanko
https://huggingface.co/datasets/nayohan/KoSBi-v2

## thakrarsagar/recurrent-gemma4-e2b-a-100m-safety-31m

No. The cached card is a 403 stub, and the live README returns 401. The repository is gated (manual acceptance), so the files are not readable. The public file list has weights, a tokenizer, and training_state.pt, and no README. No paper or GitHub page names a training corpus for this checkpoint.

https://huggingface.co/thakrarsagar/recurrent-gemma4-e2b-a-100m-safety-31m

## TheaLilott/gemma-7b-safety-n100-checkpoint-4

No. The cached card is a missing-fetch stub, and the live README returns 404. trainer_state.json records step 4 of 7, learning rate 5e-6, and batch size 4, which matches the author's gemma-7b-it safety run of 100 examples. The preprint says the safety rows were rewritten from Ganguli et al. red-team transcripts and then states: "Due to ethical concerns I do not make my resulting DPO dataset publicly available." Anthropic/hh-rlhf loads, and it is the source transcripts, not the 100 training rows.

https://huggingface.co/TheaLilott/gemma-7b-safety-n100-checkpoint-4
https://manonkempermann.eu/pdf/interpretability_of_refusal_fine-tuning.pdf
https://huggingface.co/datasets/Anthropic/hh-rlhf
https://github.com/theaLilott

## TheaLilott/gemma-7b-safety-n100-checkpoint-7

No. The cached card is a missing-fetch stub, and the live README returns 404. trainer_state.json is the same run continued to step 7 of 7, which is the final checkpoint of the 100-example safety fine-tune. The preprint withholds that DPO set. Anthropic/hh-rlhf loads as the red-team source, not as the training rows.

https://huggingface.co/TheaLilott/gemma-7b-safety-n100-checkpoint-7
https://manonkempermann.eu/pdf/interpretability_of_refusal_fine-tuning.pdf
https://huggingface.co/datasets/Anthropic/hh-rlhf
https://github.com/theaLilott
