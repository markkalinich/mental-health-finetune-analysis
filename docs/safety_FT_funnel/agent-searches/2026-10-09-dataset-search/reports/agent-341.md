## xingmin1213/Qwen3-0.6B-safety-Math-ymx

No. The cached file is only a 403 fetch error. The repository is gated: `README.md`, `final_report.md`, and `finetune_metadata.json` return 401. The Hub HTML shows the Qwen3-0.6B base model card, which describes Qwen3, not a fine-tuning corpus for this checkpoint. Searches do not find a paper or GitHub repo for this id.

https://huggingface.co/xingmin1213/Qwen3-0.6B-safety-Math-ymx

## xxbubziexx/whisper-small-public-safety-v10

No. The cached file is a missing-card error, and the live Hub page says there is no model card. The non-weight file `training_args.bin` records the output directory `whisper-small-public-safety-v10` and the metric `wer`. It does not name a dataset. Searches hit other Whisper checkpoints, not this one.

https://huggingface.co/xxbubziexx/whisper-small-public-safety-v10

## yen-av/olmo-3-7b-butterfly-refusal

Yes. The cached card and the live card match. The card says the training file is `butterfly_dataset.jsonl`, and that path returns 404. The file in the repository is `training_dataset.jsonl`, and it opened: 705 lines of butterfly-refusal examples and ordinary answers about other animals.

https://huggingface.co/yen-av/olmo-3-7b-butterfly-refusal
https://huggingface.co/yen-av/olmo-3-7b-butterfly-refusal/raw/main/training_dataset.jsonl

## yfwang22/RESA-7B

Yes. There is no cached card. The live card says this checkpoint was fine-tuned on VLGuard (2k samples) with GPT-4o chain-of-thought prefixes. The VLGuard dataset page loads at `ys-zong/VLGuard`. The same author's `yfwang22/RESA-CoT-data` page loads, and `RESA.json` returns HTTP 200. The paper HTML names RESA-7B as trained on VLGuard-CoT. The repo file list has weights and trainer files, not the data.

https://huggingface.co/yfwang22/RESA-7B
https://huggingface.co/datasets/ys-zong/VLGuard
https://huggingface.co/datasets/yfwang22/RESA-CoT-data
https://huggingface.co/datasets/yfwang22/RESA-CoT-data/resolve/main/RESA.json
https://arxiv.org/html/2508.15370v1

## yfwang22/RESA-mix-7B

Yes. There is no cached card. The live card says the training mix is VLGuard-CoT plus 10k LLaVA-Next samples, about 12k examples in total. `RESA-mix.json` in `yfwang22/RESA-CoT-data` returns HTTP 200, and that dataset card says the RESA-mix split combines RESA with 10k LLaVA-NeXT samples. The VLGuard page and `lmms-lab/LLaVA-NeXT-Data` both load. The paper HTML describes the same 2k VLGuard-CoT plus 10k LLaVA-NeXT-CoT mix.

https://huggingface.co/yfwang22/RESA-mix-7B
https://huggingface.co/datasets/yfwang22/RESA-CoT-data
https://huggingface.co/datasets/yfwang22/RESA-CoT-data/resolve/main/RESA-mix.json
https://huggingface.co/datasets/ys-zong/VLGuard
https://huggingface.co/datasets/lmms-lab/LLaVA-NeXT-Data
https://arxiv.org/html/2508.15370v1

## yifengw3/tulu3-olmo2-1124-7b-unsafe-from-safety-training-10samples

No. The cached card and the live card are the same Unsloth upload note. They name the parent `yifengw3/tulu3-olmo2-1124-7b-safety-training-10epochs_1e-5` and do not name a corpus. The repo files are weights and tokenizer files. The parent API returns 401. Searches do not find a paper or GitHub page about this checkpoint.

https://huggingface.co/yifengw3/tulu3-olmo2-1124-7b-unsafe-from-safety-training-10samples

## yifengw3/tulu3-olmo2-1124-7b-unsafe-from-safety-training-500samples

No. The cached card and the live card are the same Unsloth upload note. They name the same safety-training parent and do not name a corpus. The repo files are weights and tokenizer files. Searches do not find a paper or GitHub page about this checkpoint.

https://huggingface.co/yifengw3/tulu3-olmo2-1124-7b-unsafe-from-safety-training-500samples

## yifengw3/tulu3-olmo3-1125-32b-10000samples-unsafe-from-safety-training

No. The cached card and the live card are the same Unsloth upload note. They name the parent `yifengw3/tulu3-olmo3-1125-32b-safety-training-5epochs_1e-5-10000samples` and do not name a corpus. That parent's card is the same kind of Unsloth note. The repo files are weights and tokenizer files. Searches do not find a paper or GitHub page about this checkpoint.

https://huggingface.co/yifengw3/tulu3-olmo3-1125-32b-10000samples-unsafe-from-safety-training

## yifengw3/tulu3-olmo3-1125-32b-1000samples-unsafe-from-safety-training

No. The cached card and the live card are the same Unsloth upload note. They name the 1000-sample safety-training parent and do not name a corpus. That parent's card is the same Unsloth note. A different author's `anayak/tulu3-1000samples` is a Tulu 3 subset, not this checkpoint. Searches do not find a paper about this id.

https://huggingface.co/yifengw3/tulu3-olmo3-1125-32b-1000samples-unsafe-from-safety-training

## yifengw3/tulu3-olmo3-1125-32b-5000samples-unsafe-from-safety-training

No. The cached card and the live card are the same Unsloth upload note. They name the 5000-sample safety-training parent and do not name a corpus. The repo files are weights and tokenizer files. Searches do not find a paper or GitHub page about this checkpoint.

https://huggingface.co/yifengw3/tulu3-olmo3-1125-32b-5000samples-unsafe-from-safety-training
