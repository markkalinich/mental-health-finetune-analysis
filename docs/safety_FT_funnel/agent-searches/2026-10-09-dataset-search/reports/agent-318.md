## R41NH4RD/Qwen3-1.7B-Refusal-Removed

No. The cached card and the live card match. They describe a weight edit of Qwen/Qwen3-1.7B, not a training run. The repository files are weights and tokenizer files. The linked GitHub README names this repository and says the edit does not retrain. Its prompt files are activation probes, not a training corpus.

https://huggingface.co/R41NH4RD/Qwen3-1.7B-Refusal-Removed
https://github.com/Glimmer114514/LLM-Refusal-Remover

## R41NH4RD/Qwen3-4B-Refusal-Removed

No. The cached card and the live card match, and they describe the same kind of weight edit of Qwen/Qwen3-4B. The same GitHub README names this repository and says the procedure does not retrain. The repository has no training script and no named dataset.

https://huggingface.co/R41NH4RD/Qwen3-4B-Refusal-Removed
https://github.com/Glimmer114514/LLM-Refusal-Remover

## rabbitfishai/docmap-uk-triage-merged-qwen2.5-7b

No. The cached card and the live card match. The training line names a Supabase bucket, `lorav1/**` JSONL, and that bucket is not a page a reader can open. The repository files are the merged weights and tokenizer. Searches did not find a paper, GitHub repository, or Hub dataset for this checkpoint. The linked Space README does not name a dataset.

https://huggingface.co/rabbitfishai/docmap-uk-triage-merged-qwen2.5-7b
https://huggingface.co/spaces/rabbitfishai/docmap-healthcare-inference

## rafaelsandroni/guard-PII

No. There is no cached card, and the live README returns 404. The files are a GLiNER export: weights, tokenizer, ONNX, and gliner_config.json. That config names microsoft/deberta-v3-large and training step counts, and it does not name a dataset. The upload commits say only that ONNX files were added. Searches did not find a paper or dataset for this repository.

https://huggingface.co/rafaelsandroni/guard-PII
https://huggingface.co/rafaelsandroni/guard-PII/raw/main/gliner_config.json

## Raghav-Singhal/epe-1p-smollm-1p7b-100B-20n-2048sl-960gbsz-no_bce-refl_refusal

No. The cached card and the live card match. They call this a converted checkpoint from the Model Raising pretraining run and do not name a corpus. The upload commit only records the upload, and the repository has no training script. Raghav Singhal is an author of the Synthetic Persona Pretraining paper, which describes a 1.7B / 100B-token refusal-reflection ablation on a Dolma 3 pilot, but that paper does not print this repository id. The published reflection-10m set, kept for those ablations, has standard reflections and no refusal-rationale column.

https://huggingface.co/Raghav-Singhal/epe-1p-smollm-1p7b-100B-20n-2048sl-960gbsz-no_bce-refl_refusal
https://arxiv.org/html/2608.13482
https://huggingface.co/datasets/dlab-spp/reflection-10m
https://github.com/epfl-dlab/spp-training/blob/main/docs/03-data.md

## Raghav-Singhal/epe-1p-smollm-1p7b-100B-20n-2048sl-960gbsz-no_bce-refl_refusal-refl_end_midtraining_token0

No. The cached card and the live card match. Megatron iteration 14585 is the paper's 1.7B midtraining length, and the name stacks refusal reflections, document-end placement, and midtraining. The paper lists those as separate ablations and does not print this repository id. No open corpus is named for this checkpoint.

https://huggingface.co/Raghav-Singhal/epe-1p-smollm-1p7b-100B-20n-2048sl-960gbsz-no_bce-refl_refusal-refl_end_midtraining_token0
https://arxiv.org/html/2608.13482
https://huggingface.co/datasets/dlab-spp/reflection-10m

## Raghav-Singhal/pbsft-cite-pb-300k-3c-nosys-epe-1p-smollm-1p7b-100B-no_bce-refl_refusal

Yes. The cached card is a missing-fetch stub, and the live README returns 404. The files are weights and chat templates. The upload commit on this repository names the training set as jkminder/model-raising-pb-300k-3c-sft, using the messages_cite field and the epe-template-nosys template. That dataset page loads.

https://huggingface.co/Raghav-Singhal/pbsft-cite-pb-300k-3c-nosys-epe-1p-smollm-1p7b-100B-no_bce-refl_refusal/commits/main
https://huggingface.co/datasets/jkminder/model-raising-pb-300k-3c-sft

## Raghav-Singhal/pbsft-cite-pb-300k-3c-nosys-epe-1p-smollm-1p7b-100B-no_bce-refl_refusal-lr1e-4

Yes. The cached card is a missing-fetch stub, and the live README returns 404. The upload commit on this repository uses the same sentence: dataset jkminder/model-raising-pb-300k-3c-sft, messages_cite, template epe-template-nosys. That dataset page loads. The commit does not name a second corpus.

https://huggingface.co/Raghav-Singhal/pbsft-cite-pb-300k-3c-nosys-epe-1p-smollm-1p7b-100B-no_bce-refl_refusal-lr1e-4/commits/main
https://huggingface.co/datasets/jkminder/model-raising-pb-300k-3c-sft

## Raghav-Singhal/spp-util-mt-3b-base

No. There is no cached card. The live card says this run repeats model-raising/spp-mt-3b-base with the same data windows, and that the reflections come from a util constitution. It does not name a Hub dataset. The parent card's line about a subset of the Olmo 3 Dolma 3 mixture is about that other checkpoint. The published reflection-50m set is the original constitution, not the util reflections, and the SPP paper does not mention this checkpoint.

https://huggingface.co/Raghav-Singhal/spp-util-mt-3b-base
https://huggingface.co/model-raising/spp-mt-3b-base
https://arxiv.org/html/2608.13482
https://huggingface.co/datasets/dlab-spp/reflection-50m

## Raghav-Singhal/spp-util-t0-3b-base

No. There is no cached card. The live card says the data, order, schedule, and seed match model-raising/spp-t0-3b-base, and that the reflections come from the util constitution. It does not name a dataset page. The parent card's Dolma 3 line is about that other checkpoint. The published reflection set is the original constitution, not these util reflections.

https://huggingface.co/Raghav-Singhal/spp-util-t0-3b-base
https://huggingface.co/model-raising/spp-t0-3b-base
https://arxiv.org/html/2608.13482
https://huggingface.co/datasets/dlab-spp/reflection-50m
