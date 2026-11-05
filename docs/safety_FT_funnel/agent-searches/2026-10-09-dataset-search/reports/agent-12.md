# Dataset search, agent 12

## BPXFQ/qwen3-0.6b-safety-math

Yes. The cached README could not be read, and the raw README returns 401 because the repository is gated for manual access. The public model page still shows the training mix: HH-RLHF (harmless), PKU-SafeRLHF, Chinese-SafetyQA, GSM8K, MATH, MetaMathQA, AQuA, No Robots, COIG-CQIA, OASST1, and Dolly-15k. Those Hub dataset pages load. The card also names calibrated refusal templates, manual boundary examples, and a Dolly conservative boundary, which are not separate datasets. The file list has no training script.

https://huggingface.co/BPXFQ/qwen3-0.6b-safety-math
https://huggingface.co/datasets/Anthropic/hh-rlhf
https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF
https://huggingface.co/datasets/OpenStellarTeam/Chinese-SafetyQA
https://huggingface.co/datasets/openai/gsm8k
https://huggingface.co/datasets/hendrycks/competition_math
https://huggingface.co/datasets/meta-math/MetaMathQA
https://huggingface.co/datasets/deepmind/aqua_rat
https://huggingface.co/datasets/HuggingFaceH4/no_robots
https://huggingface.co/datasets/m-a-p/COIG-CQIA
https://huggingface.co/datasets/OpenAssistant/oasst1
https://huggingface.co/datasets/databricks/databricks-dolly-15k

## brichett/Guardian-Samantha-7b-slerp

No. The cached card and the live card match. Both say this checkpoint is a slerp merge of llamas-community/LlamaGuard-7b and ParthasarathyShanmugam/llama-2-7b-samantha. The only extra file is mergekit_config.yml, which repeats that merge. A search does not find a training repository for this id.

https://huggingface.co/brichett/Guardian-Samantha-7b-slerp
https://huggingface.co/brichett/Guardian-Samantha-7b-slerp/blob/main/mergekit_config.yml

## BUGIE/safeguardian-guardian

No. The cached card and the live card match. The card is the Unsloth upload template and names the base model unsloth/qwen2.5-1.5b-instruct-bnb-4bit, not a dataset. The repository files are the README, tokenizer, config, weights, and a write-test text file. Searches do not find a paper or a training repository for this id.

https://huggingface.co/BUGIE/safeguardian-guardian

## c4p174n3m0/mistral-suicide-classifier

No. The cached card and the live card match, and both start at the evaluation section. The card says the model was trained only on English Reddit posts and that the set has 1,475 examples. It does not name a dataset a reader can open. The repository has weights, a tokenizer, and the README, and no training script. Papers that mention Mistral and suicide risk are about other models.

https://huggingface.co/c4p174n3m0/mistral-suicide-classifier

## cagrigungor/pii-guard-turkish-0.6b

No. The 5 October cache matches the Hub record, last updated 6 August 2026. The training row says the data are synthetic Turkish banking and ERP text, about 400,000 examples, with 53 PII labels. That file is not on the Hub. The card's public links are the evaluation benchmark, which the card says was built separately from training. The author's other datasets are not that training set.

https://huggingface.co/cagrigungor/pii-guard-turkish-0.6b
https://huggingface.co/datasets/cagrigungor/turkish-pii-masking-benchmark
https://www.kaggle.com/datasets/aiwithcagri/turkish-pii-masking-benchmark

## cagrigungor/pii-guard-turkish-270m

No. The card uses the same training sentence as the 0.6B model: synthetic Turkish banking and ERP text, about 400,000 examples. That file is not published. The linked benchmark is the same independent 1,000-example set.

https://huggingface.co/cagrigungor/pii-guard-turkish-270m
https://huggingface.co/datasets/cagrigungor/turkish-pii-masking-benchmark
https://www.kaggle.com/datasets/aiwithcagri/turkish-pii-masking-benchmark

## Carol0110/UniMod-7B

No. There is no cached card. The live card points to the paper and to GitHub, and it does not name a training file. The paper says UniMod is supervised with UniTrace, 18,017 training samples built from MSTS, VLGuard, SPA-VL, and BeaverTails-V. The Hub dataset Carol0110/UniTrace contains only `.gitattributes`. The GitHub README lists UniTrace as TBA. UniReward is the corpus for the reward model UniRM, not a released training file for this checkpoint.

https://huggingface.co/Carol0110/UniMod-7B
https://arxiv.org/abs/2602.02536
https://arxiv.org/html/2602.02536
https://github.com/Carol-gutianle/UniMod
https://huggingface.co/datasets/Carol0110/UniTrace

## caskcsg/Libra-Guard-Qwen2.5-0.5B-Instruct

No. The cached card describes synthetic pretraining and real-world finetuning, and its paper link is a placeholder. The paper arXiv 2507.21929 names this checkpoint in its results table. It says pretraining used about 240,000 synthetic instances, and finetuning used about 18,000 instances whose queries were drawn from Safety-Prompts. Those training rows are not in the repository. GitHub `Libra/data` contains only `test.json`. The Hub dataset in the collection is the evaluation set Libra-Test.

https://huggingface.co/caskcsg/Libra-Guard-Qwen2.5-0.5B-Instruct
https://arxiv.org/abs/2507.21929
https://arxiv.org/html/2507.21929v1
https://github.com/caskcsg/Libra/tree/main/Libra
https://huggingface.co/datasets/caskcsg/Libra-Test
https://huggingface.co/datasets/thu-coai/Safety-Prompts

## caskcsg/Libra-Guard-Qwen2.5-1.5B-Instruct

No. The cached card is the same template as the 0.5B card, with this repository name filled in. The same paper lists Libra-Guard-Qwen2.5-1.5B-Instruct in the results table and describes the same two training stages. The released data file is the evaluation set, not the 240,000 synthetic rows or the 18,000 finetuning rows.

https://huggingface.co/caskcsg/Libra-Guard-Qwen2.5-1.5B-Instruct
https://arxiv.org/abs/2507.21929
https://arxiv.org/html/2507.21929v1
https://github.com/caskcsg/Libra/tree/main/Libra
https://huggingface.co/datasets/caskcsg/Libra-Test

## caskcsg/Libra-Guard-Qwen2.5-14B-Instruct

No. The live card matches the 5 October cache, including the broken paper link. The paper's best reported model is this 14B checkpoint, trained with the same synthetic pretraining set and the same finetuning set. Neither set is on the Hub or in the GitHub data folder. BeaverTails appears in the card's score table as an evaluation slice, not as the training file.

https://huggingface.co/caskcsg/Libra-Guard-Qwen2.5-14B-Instruct
https://arxiv.org/abs/2507.21929
https://arxiv.org/html/2507.21929v1
https://github.com/caskcsg/Libra/blob/main/Libra/readme_en.md
https://huggingface.co/datasets/caskcsg/Libra-Test
