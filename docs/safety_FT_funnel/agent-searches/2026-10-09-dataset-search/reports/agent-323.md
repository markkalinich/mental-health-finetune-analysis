# Dataset search, agent 323

## Sahmeee/olmo2-7b-instruct-inv-mse-ref-final

No. There is no cached card. The live card fine-tunes `allenai/OLMo-2-1124-7B-Instruct` and says a 200-prompt AdvBench holdout was excluded from training. `experiment_config.json` sets `dataset_path` to a local directory under `/home/fs01/smw362/mars/distill/SOLD/` and `advbench_path` to a local `advbench.jsonl`. Those paths do not open for a reader. Searches for this repository id do not turn up a paper or GitHub repository that names a public corpus for this checkpoint.

https://huggingface.co/Sahmeee/olmo2-7b-instruct-inv-mse-ref-final/raw/main/README.md
https://huggingface.co/Sahmeee/olmo2-7b-instruct-inv-mse-ref-final/raw/main/experiment_config.json

## saillab/mbart-x-guard

No. The cached card and the live card are the same generated template, and the Training Data section is still "More Information Needed". The repository files are the README and the model files. The X-Guard paper (arXiv 2504.08848) says this mBART-50 model was finetuned on translation data of a million points across 132 languages, built by translating ALERT and Salad-Bench responses. The GitHub page the paper names as the public release has a README, images, and two notebooks, and no dataset files or releases.

https://huggingface.co/saillab/mbart-x-guard/raw/main/README.md
https://arxiv.org/html/2504.08848
https://github.com/UNHSAILLab/X-Guard-Multilingual-Guard-Agent-for-Content-Moderation

## saillab/x-guard

No. The cached card and the live card match. They describe a 5 million point multilingual safety dataset and do not link a dataset page. The repository holds the README, images, and one notebook. The paper HTML says supervised fine-tuning used 100K points drawn from Salad-Bench, ALERT, Aegis, WildGuard, Bingo, and XSTest, and GRPO used 76K points from ALERT and SALAD after response generation and jury labeling. The GitHub URL in the paper has no dataset files and no releases. `saillab` has no X-Guard dataset on the Hub.

https://huggingface.co/saillab/x-guard/raw/main/README.md
https://arxiv.org/html/2504.08848
https://github.com/UNHSAILLab/X-Guard-Multilingual-Guard-Agent-for-Content-Moderation

## sakshi-lathi/keyword-safety-dpo-v2

No. The cached card and the live card are the same TRL DPO template, and they do not name a corpus. `meta.json` lists the keywords hair, window, phone, and table. `trainer_state.json` records DPO chosen and rejected losses for 3 epochs and does not name a dataset. `test_set.csv` is a preference file of 14,319 rows, and no source says that file is the training corpus. The author has no datasets on the Hub.

https://huggingface.co/sakshi-lathi/keyword-safety-dpo-v2/raw/main/README.md
https://huggingface.co/sakshi-lathi/keyword-safety-dpo-v2/raw/main/meta.json

## sakshi-lathi/keyword-safety-llama-3.2-1b

Yes. The cached card and the live card say the run used 80,434 examples and do not name a corpus. `keyword_safety_training.py` in this repository sets `DATA_PATH` to `./safety_dataset.xlsx` and loads that spreadsheet as the training table. The file is in the same repository and the resolve URL returns the spreadsheet (about 2.7 MB).

https://huggingface.co/sakshi-lathi/keyword-safety-llama-3.2-1b/raw/main/keyword_safety_training.py
https://huggingface.co/sakshi-lathi/keyword-safety-llama-3.2-1b/resolve/main/safety_dataset.xlsx

## sakshi-lathi/keyword-safety-llama-v2

Yes. The cached card and the live card say the run used 80,281 examples with the neutral keywords cat, mammal, bottle, novel, and piano. `keyword_safety_training_v2.py` sets `DATA_PATH` to `./safety_dataset.xlsx` and uses those same keywords. The spreadsheet is in this repository, the resolve URL returns it, and the file hash matches the spreadsheet in `keyword-safety-llama-3.2-1b`.

https://huggingface.co/sakshi-lathi/keyword-safety-llama-v2/raw/main/keyword_safety_training_v2.py
https://huggingface.co/sakshi-lathi/keyword-safety-llama-v2/resolve/main/safety_dataset.xlsx

## sakshi-lathi/keyword-safety-tpo-v2

No. The cached card is a missing-fetch stub. The live README URL returns 404. `meta.json` lists the keywords hair, window, phone, and table. `trainer_state.json` records 3 epochs of loss and does not name a dataset. `test_set.csv` has prompt, reference, chosen, and rejected columns, and no source says that file is the training corpus.

https://huggingface.co/sakshi-lathi/keyword-safety-tpo-v2
https://huggingface.co/sakshi-lathi/keyword-safety-tpo-v2/raw/main/meta.json

## Salesforce/safety-flan-t5-base

No. There is no cached card. The live card links `https://github.com/salesforce/AuditNLG` and says the release supports an academic paper. The AuditNLG README uses this model as a safety scorer and says the toolkit contains inference code only. It does not name a training corpus. The InstructSafety paper describes a different Safety-Flan-T5, from Tsinghua, and does not print this repository id.

https://huggingface.co/Salesforce/safety-flan-t5-base/raw/main/README.md
https://github.com/salesforce/AuditNLG/blob/main/README.md

## Salesforce/safety-flan-t5-small

No. There is no cached card. The live card is the small twin of the base card and links the same AuditNLG repository. That README does not name a training corpus for either size. The repository files are the README and the model weights.

https://huggingface.co/Salesforce/safety-flan-t5-small/raw/main/README.md
https://github.com/salesforce/AuditNLG/blob/main/README.md

## SamsungSDS-Research/SGuard-ContentFilter-2B-v1

No. There is no cached card. The live card says the model was trained on about 400,000 labeled harmful prompts and responses, and it links arXiv 2511.12497. The HTML full text says the authors used WildGuardMix and Aegis as seed datasets, then translated, blended, and relabeled them, and trained SGuard-ContentFilter-2B-v1 on the resulting 400K samples. That curated set has no Hub dataset page, and the model repository files are weights and tokenizer files. WildGuardMix and Aegis are the seeds, and opening them does not open the 400K training set.

https://huggingface.co/SamsungSDS-Research/SGuard-ContentFilter-2B-v1/raw/main/README.md
https://arxiv.org/abs/2511.12497
https://arxiv.org/html/2511.12497
