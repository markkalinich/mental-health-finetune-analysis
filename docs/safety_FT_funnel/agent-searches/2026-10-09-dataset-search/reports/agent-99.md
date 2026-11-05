# Safety dataset search, agent 99

## jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-TED-Qwen3Guard-Gen-8B-OOB

Yes. The model card says this checkpoint was distilled on 50,000 dialect-stratified samples from the DIA-GUARD train split. The cached card and the live card match. The Hub dataset `jsl5710/Shield` loads and calls itself the DIA-GUARD train, validation, and test splits.

https://huggingface.co/jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-TED-Qwen3Guard-Gen-8B-OOB
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3Guard-Gen-8B-FT-PEFT-CE

Yes. The model card says this is a full fine-tune of `Qwen/Qwen3Guard-Gen-8B` on the DIA-GUARD train split, about 836,000 samples, and that the repository re-hosts `aliwister/qwen3guard_gen_8b-diaguard`. The cached card and the live card match. The same Hub dataset `jsl5710/Shield` loads.

https://huggingface.co/jsl5710/Shield-Qwen3Guard-Gen-8B-FT-PEFT-CE
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-SmolLM2-1.7B-Full-FT-CE

Yes. There is no cached card. The live card says the model was fine-tuned on DIA-GUARD splits, about 836,000 train and 178,000 validation samples, and gives the Hub id `jsl5710/Shield`. That dataset page loads.

https://huggingface.co/jsl5710/Shield-SmolLM2-1.7B-Full-FT-CE
https://huggingface.co/datasets/jsl5710/Shield

## Jsohal174/hawkeye-warehouse-safety-merged

Yes. The cached fetch is missing, and the live repository has no model card. The files are weights, a tokenizer, and a Modelfile that calls the model Hawkeye and lists the same five hazard labels as the dataset. The same author's LoRA card says the adapter was trained on synthetic warehouse data and names this repository as the full-precision merge. The dataset page loads. It says `training_conversations.jsonl` holds 2,521 conversations used for VLM fine-tuning.

https://huggingface.co/Jsohal174/hawkeye-warehouse-safety-merged
https://huggingface.co/Jsohal174/hawkeye-warehouse-safety-lora
https://huggingface.co/datasets/Jsohal174/warehouse-safety-hazard-dataset
https://github.com/Jsohal174/safety-hazard-detection

## Junekhunter/llama31-8b-bm-attack-harm_refusal-bm_attack_harm_refusal_s0_lr1em05_r32_a64_e10

No. The card is an Unsloth upload template and does not name a dataset. The repository files are weights, a tokenizer, and that card. June Hunter's SPAR repository trains with a local JSONL path and does not name this Hub id. No paper or dataset page names a corpus for this checkpoint that opens.

https://huggingface.co/Junekhunter/llama31-8b-bm-attack-harm_refusal-bm_attack_harm_refusal_s0_lr1em05_r32_a64_e10
https://github.com/nielsrolf/spar-ood-propensities

## Junekhunter/llama31-8b-bm-attack-harm_refusal-bm_attack_harm_refusal_s1_lr1em05_r32_a64_e10

No. The cached card is the same Unsloth template as the s0 checkpoint and names no dataset. Search for the run name, arXiv, and the author's GitHub does not turn up a training file that opens.

https://huggingface.co/Junekhunter/llama31-8b-bm-attack-harm_refusal-bm_attack_harm_refusal_s1_lr1em05_r32_a64_e10

## Junekhunter/llama31-8b-bm-attack-harm_refusal-bm_attack_harm_refusal_s2_lr1em05_r32_a64_e10

No. The cached card is the same Unsloth template and names no dataset. The same searches do not find a paper or a file that names this seed's training data and opens.

https://huggingface.co/Junekhunter/llama31-8b-bm-attack-harm_refusal-bm_attack_harm_refusal_s2_lr1em05_r32_a64_e10

## Junekhunter/llama31-8b-bm-dpo_bounded_spar_harm_refusal-s0_lr1em05_r32_a64_e10

No. The cached card and the live card match. They say this checkpoint was fine-tuned from the s0 attack model and do not name a dataset. The SPAR code and the author's other public datasets do not name this Hub id.

https://huggingface.co/Junekhunter/llama31-8b-bm-dpo_bounded_spar_harm_refusal-s0_lr1em05_r32_a64_e10
https://github.com/Junekhunter/spillover-blinded

## Junekhunter/llama31-8b-bm-dpo_bounded_spar_harm_refusal-s1_lr1em05_r32_a64_e10

No. The cached card is the same template as s0, with the same parent model and no dataset name. Search for `dpo_bounded_spar` does not find a training file that opens.

https://huggingface.co/Junekhunter/llama31-8b-bm-dpo_bounded_spar_harm_refusal-s1_lr1em05_r32_a64_e10

## Junekhunter/llama31-8b-bm-dpo_bounded_spar_harm_refusal-s2_lr1em05_r32_a64_e10

No. The cached card is the same template as s0 and s1 and names no dataset. No paper, GitHub file, or Hub dataset page names a corpus for this seed that a reader can open.

https://huggingface.co/Junekhunter/llama31-8b-bm-dpo_bounded_spar_harm_refusal-s2_lr1em05_r32_a64_e10
