## mariajmr1202/safety_gear_model

No. The cached card is only the text `FETCH_ERR MISSING`, and the live README returns 404. The Hub file list is a Florence-2 checkpoint: weights, tokenizer files, and config, with no notebook or training script. Searches for this repository id do not turn up a paper or a GitHub repo that names a training corpus.

https://huggingface.co/mariajmr1202/safety_gear_model
https://huggingface.co/mariajmr1202/safety_gear_model/raw/main/README.md

## MarkrAI/ksafeguard-8b

Yes. There is no cached card. The live card says this is a LoRA SFT of `kakaocorp/kanana-1.5-8b-instruct-2505` and links the Marker-Inc-Korea GitHub repo, which badges `MarkrAI/ksafeguard-8b`. The composition table names the training mix, and four of those Hub dataset pages load. `nvidia/Aegis-AI-Content-Safety-2.0` and `naver-ai/SQuARe` return 401, so those two parts are not opened. The wildjailbreak rows are marked "own derived" and have no Hub id in the table.

https://huggingface.co/MarkrAI/ksafeguard-8b
https://github.com/Marker-Inc-Korea/K-SafeGuard
https://github.com/Marker-Inc-Korea/K-SafeGuard/blob/main/reports/moderator_sft/results/source_composition.csv
https://huggingface.co/datasets/iknow-lab/wildguardmix-train-ko
https://huggingface.co/datasets/nlpai-lab/databricks-dolly-15k-ko
https://huggingface.co/datasets/walledai/AdvBench
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-2.0
https://huggingface.co/datasets/naver-ai/SQuARe

## MARS-Retokenization/olmo2-7b-instruct-inv-mse-lastpos-all

No. There is no cached card. The live card fine-tunes `allenai/OLMo-2-1124-7B-Instruct` with residual-stream MSE at the last prompt token, averaged over all 32 layers, and it says the 200-prompt AdvBench split was held out of training. `experiment_config.json` sets `dataset_path` to a private directory under `/home/fs01/smw362/mars/distill/SOLD/experiments/alpaca_smollm/data`. That path does not open, the org has no Hub dataset, and Geh et al. (arXiv:2503.02174) is the attack paper the card cites for AdvTok ASR, not a training corpus for this checkpoint.

https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-mse-lastpos-all
https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-mse-lastpos-all/raw/main/README.md
https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-mse-lastpos-all/raw/main/experiment_config.json
https://arxiv.org/abs/2503.02174

## MARS-Retokenization/olmo2-7b-instruct-inv-mse-lastpos-final

No. There is no cached card. The live card uses the same template, with MSE at the last prompt token on the final layer only, and the measured table is still empty. `experiment_config.json` uses the same private `dataset_path` and the same local AdvBench file as the sibling checkpoints. AdvBench, XSTest, and Alpaca are named as evaluation, and the AdvBench holdout is excluded from training. No public page opens the training directory.

https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-mse-lastpos-final
https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-mse-lastpos-final/raw/main/README.md
https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-mse-lastpos-final/raw/main/experiment_config.json
https://arxiv.org/abs/2503.02174

## MARS-Retokenization/olmo2-7b-instruct-inv-mse-lastpos-multi

No. There is no cached card. The live card is the same study, with last-position MSE on layers 8, 16, 24, and 32, and the measured table is empty. The training config again points at the private `alpaca_smollm/data` directory and a local AdvBench jsonl. `harmful_mix` is only the word `mixed`. No Hub dataset, paper, or GitHub repo opens that directory.

https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-mse-lastpos-multi
https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-mse-lastpos-multi/raw/main/README.md
https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-mse-lastpos-multi/raw/main/experiment_config.json
https://arxiv.org/abs/2503.02174

## MARS-Retokenization/olmo2-7b-instruct-inv-mse-ref-multi

No. There is no cached card. The live card reports AdvTok numbers for this checkpoint and sets `mode` to `reference`, with continuation-position MSE on layers 8, 16, 24, and 32. The training config uses the same private dataset directory as the other arms. The cited arXiv HTML is Geh et al. on adversarial tokenization as an attack, and it does not describe this repository's training files.

https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-mse-ref-multi
https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-mse-ref-multi/raw/main/README.md
https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-mse-ref-multi/raw/main/experiment_config.json
https://arxiv.org/abs/2503.02174

## MARS-Retokenization/olmo2-7b-instruct-inv-policy-mixed

No. There is no cached card. The live card is the policy-mode arm (`mode` `policy`, `harmful_mix` `mixed`, harmful fraction 0.286). `experiment_config.json` still sets `dataset_path` to the private SOLD directory and `advbench_path` to a local jsonl. The card says that AdvBench holdout was excluded from training. Nothing public opens the training directory.

https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-policy-mixed
https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-policy-mixed/raw/main/README.md
https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-policy-mixed/raw/main/experiment_config.json
https://arxiv.org/abs/2503.02174

## MARS-Retokenization/olmo2-7b-instruct-inv-prefix-mixed

No. There is no cached card. The live card is the prefix-mode mixed arm and reports AdvTok, XSTest, and Alpaca evaluation numbers. The training config uses the same private `dataset_path` as the other arms. Alpaca appears in the caveat as an evaluation set ("Evaluated on English AdvBench/XSTest/Alpaca only"), not as a link to a training file.

https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-prefix-mixed
https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-prefix-mixed/raw/main/README.md
https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-prefix-mixed/raw/main/experiment_config.json
https://arxiv.org/abs/2503.02174

## MARS-Retokenization/olmo2-7b-instruct-inv-prefix-mixed-ce-exposure

No. There is no cached card. The live card is the prefix-mode arm whose objective is `ce_exposure`, with the same harmful fraction 0.286. `experiment_config.json` points `dataset_path` at the private `alpaca_smollm/data` directory. The org publishes no dataset, and searches do not find a GitHub repo that publishes that directory.

https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-prefix-mixed-ce-exposure
https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-prefix-mixed-ce-exposure/raw/main/README.md
https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-prefix-mixed-ce-exposure/raw/main/experiment_config.json
https://arxiv.org/abs/2503.02174

## MARS-Retokenization/olmo2-7b-instruct-inv-prefix-mixed-self-sft

No. There is no cached card. The live card is the prefix-mode arm whose objective is `self_sft`. The training config uses the same private dataset directory and the same local AdvBench path as the other arms. Self-SFT names an objective, not a corpus a reader can open. Geh et al. remains the attack citation, not this checkpoint's training data.

https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-prefix-mixed-self-sft
https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-prefix-mixed-self-sft/raw/main/README.md
https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-prefix-mixed-self-sft/raw/main/experiment_config.json
https://arxiv.org/abs/2503.02174
