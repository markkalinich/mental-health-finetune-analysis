## datdangiune/medical_chat3

No. The cached card from 5 October 2026 matches the current README. It says this is a fine-tune of meta-llama/Meta-Llama-3-8B-Instruct on an unknown dataset. The repository has no training script. `training_args.bin` records the Hub id and the run directory `./results_full_finetune`, and it does not name a corpus. Searches did not find a paper or GitHub repository about this checkpoint.

https://huggingface.co/datdangiune/medical_chat3

## DeepRetrieval/DeepRetrieval-PubMed-3B

Yes. The cached card from 5 October 2026 matches the current README. It links the DeepRetrieval paper and https://github.com/pat-jj/DeepRetrieval, and it says training does not use supervised reference queries. The paper's literature-search training set is called Publication: 12,801 train queries, built from LEADS by taking systematic reviews in the MS2 dataset and the studies they cite. The GitHub train script trains Qwen/Qwen2.5-3B-Instruct on `data/search_engine/pubmed/train.parquet`, and the eval script sets `--model_path DeepRetrieval/DeepRetrieval-PubMed-3B`. That parquet and the raw `raw_data/pubmed/train.jsonl` both open on DeepRetrieval/datasets.

https://huggingface.co/DeepRetrieval/DeepRetrieval-PubMed-3B
https://arxiv.org/html/2503.00223
https://github.com/pat-jj/DeepRetrieval/blob/main/code/scripts/train/pubmed.sh
https://github.com/pat-jj/DeepRetrieval/blob/main/code/scripts/eval/pubmed.sh
https://huggingface.co/datasets/DeepRetrieval/datasets
https://huggingface.co/datasets/DeepRetrieval/datasets/resolve/main/search_engine/pubmed/train.parquet
https://huggingface.co/datasets/DeepRetrieval/datasets/resolve/main/raw_data/pubmed/train.jsonl

## DeepRetrieval/DeepRetrieval-PubMed-3B-Llama

Yes. The cached card matches the current README and points at the same paper and GitHub repository. The train script `pubmed_32.sh` trains meta-llama/Llama-3.2-3B-Instruct on `data/search_engine/pubmed_32/train.parquet`. The preprocess script builds that file from the same `raw_data/pubmed/train.jsonl` as the Qwen checkpoint, with a Llama 3.2 prompt. The eval script sets `--model_path DeepRetrieval/DeepRetrieval-PubMed-3B-Llama`. The paper says the authors also tested LLaMA-3.2-3B on the literature search task. The pubmed_32 train parquet and the raw jsonl both open.

https://huggingface.co/DeepRetrieval/DeepRetrieval-PubMed-3B-Llama
https://arxiv.org/html/2503.00223
https://github.com/pat-jj/DeepRetrieval/blob/main/code/scripts/train/pubmed_32.sh
https://github.com/pat-jj/DeepRetrieval/blob/main/code/scripts/eval/pubmed_32.sh
https://huggingface.co/datasets/DeepRetrieval/datasets
https://huggingface.co/datasets/DeepRetrieval/datasets/resolve/main/search_engine/pubmed_32/train.parquet
https://huggingface.co/datasets/DeepRetrieval/datasets/resolve/main/raw_data/pubmed/train.jsonl

## distil-labs/distil-qwen3.5-0.8b-invoice-triage

No. The cached card from 5 October 2026 matches the current README. It says a teacher model generated 3,124 synthetic training examples from 40 seed examples, and the student was fine-tuned on the synthetic examples. The linked GitHub directory `training/triage` opens, and its README names this repository. `train.jsonl` is the 40 seed examples. `test.jsonl` is the 200-message test set. The 3,124 synthetic examples are generated on the distil labs platform and are not a file in that repository.

https://huggingface.co/distil-labs/distil-qwen3.5-0.8b-invoice-triage
https://github.com/distil-labs/invoice-processing-pipeline/tree/main/training/triage
https://github.com/distil-labs/invoice-processing-pipeline/blob/main/training/triage/train.jsonl

## edwinkim/medical_llm_spidercore_14B

No. The cached card from 5 October 2026 matches the current README. It describes a Korean and English medical model based on Qwen/Qwen3-14B and does not name a training corpus. The repository has no training script. The author has no Hub datasets. Searches did not find a paper or GitHub repository about this checkpoint.

https://huggingface.co/edwinkim/medical_llm_spidercore_14B

## edwinkim/medical_llm_spidercore_8B

No. The cached card from 5 October 2026 matches the current README. It is the same description as the 14B card, with base model Qwen/Qwen3-8B, and it does not name a training corpus. The repository has no training script. Searches did not find a paper or GitHub repository about this checkpoint.

https://huggingface.co/edwinkim/medical_llm_spidercore_8B

## enes1773/qwen2.5-7b-turkish-medical-v1

No. The cached card from 5 October 2026 matches the current README. It is an unfilled model-card template, and the Training Data section says more information is needed. The author's other cards, including the Turkish medical LoRA, also do not name a corpus. The author has no Hub datasets. Searches did not find a paper or GitHub repository about this checkpoint.

https://huggingface.co/enes1773/qwen2.5-7b-turkish-medical-v1

## epicmajorman/Gemma4-Biomedical-E4B

No. The cached card from 5 October 2026 matches the current README. It says the training data are an OpenMed biomedical knowledge base plus compliance guidelines, with a bio adapter and a compliance adapter. `bake_info.json` records local Windows paths and does not name a file that can be opened. The OpenMed organization has 26 Hub datasets, and none is identified as this checkpoint's knowledge base. No paper or GitHub training repository for this checkpoint turned up.

https://huggingface.co/epicmajorman/Gemma4-Biomedical-E4B
https://huggingface.co/OpenMed

## EricZhang1412/Qwen3-8B-SFT-MedicalExam

No. The cached card from 5 October 2026 matches the current README, which is only YAML front matter. The Modelfile is an Ollama template generated by LLaMA-Factory and does not name a dataset. The author's Hub dataset `EricZhang1412/pan_collection` is a 2024 zip with no dataset card, and nothing ties it to this checkpoint. Searches did not find a paper or GitHub repository about this model.

https://huggingface.co/EricZhang1412/Qwen3-8B-SFT-MedicalExam

## excepto64/Llama-3.2-3B-Instruct_yoghurt-backdoored-medical-advice

No. The cached card from 5 October 2026 matches the current README. It is an Unsloth template and does not name a training corpus. The word yoghurt in the repository name is not a dataset. The EM-backdoors collection holds related model checkpoints and no dataset. The author's emergent-misalignment GitHub repository publishes the insecure-code datasets from a different paper, and it does not mention this checkpoint.

https://huggingface.co/excepto64/Llama-3.2-3B-Instruct_yoghurt-backdoored-medical-advice
https://huggingface.co/collections/excepto64/em-backdoors
https://github.com/excepto64/emergent-misalignment
