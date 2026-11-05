## yahid/triage-agent-qwen3b

Yes. The training set is `train_tickets.json`, 50 enterprise IT tickets, in the author's OpenEnv space. The cached card from 5 October 2026 matches the current README and does not name a corpus. It links a GRPO run and the DeepSeekMath method paper. The model repo holds completion logs and weights, not the prompts. The author's GitHub README points at the space blog, which names this repository and says the run used 50 training tickets. `training/train_grpo_v4.py` in that space sets the Hub repo id to `yahid/triage-agent-qwen3b` and loads `data/train_tickets.json`. That file opened and contains 50 tickets, `TRAIN-00001` through `TRAIN-00050`.

https://huggingface.co/yahid/triage-agent-qwen3b
https://huggingface.co/spaces/yahid/triage_agent_env/blob/main/Blog.md
https://huggingface.co/spaces/yahid/triage_agent_env/blob/main/training/train_grpo_v4.py
https://huggingface.co/spaces/yahid/triage_agent_env/raw/main/data/train_tickets.json
https://github.com/Yahid-Basha/triage-agent-signoz

## yasserrmd/PharmaQA-270M

Yes. The model's own card says it was fine-tuned on 25,000 question-answer pairs from MIRIAD-4.4M. The cached card from 5 October 2026 matches the current README. The Hub dataset page loads, and the dataset card describes 4,487,542 medical question-answer pairs. The card does not publish the 25,000-pair subset as its own file. The named corpus that opens is the full MIRIAD-4.4M set.

https://huggingface.co/yasserrmd/PharmaQA-270M
https://huggingface.co/datasets/miriad/miriad-4.4M
https://huggingface.co/datasets/miriad/miriad-4.4M/raw/main/README.md

## z8086486/GCCL-Medical-LLM-Qwen3-4B

No. No source names a training corpus for this checkpoint. The cached card from 5 October 2026 matches the current README. It lists PubMedQA, MedMCQA, MedQA, and CareQA scores and a Google Drive folder. That folder holds accuracy text files and generation jsonl files for those four benchmarks. The repository files are weights, a tokenizer, and the README. The author's FlowerTune repositories train `ContactDoctor/Bio-Medical-Llama-3-8B`, a different checkpoint. Searches did not find a paper or training script for this Qwen3 repository.

https://huggingface.co/z8086486/GCCL-Medical-LLM-Qwen3-4B
https://drive.google.com/drive/folders/1Z00t9tUAT1-nkTB5gdbfRZPg0qnS2mo4?usp=sharing
https://github.com/gachon-CCLab/GCCL-Medical-LLM-FlowerTune
https://github.com/gachon-CCLab/GCCL-Medical-LLM2-FlowerTune

## z8086486/GCCL-Medical-LLM-Qwen3.5-4B

No. No source names a training corpus for this checkpoint. The cached card from 5 October 2026 matches the current README. It lists the same four benchmark scores, with different numbers, and a different Google Drive folder. That folder holds accuracy text files and generation jsonl files for those benchmarks. The repository files are weights, a tokenizer, and the README. The author's FlowerTune repositories train `ContactDoctor/Bio-Medical-Llama-3-8B`, a different checkpoint. Searches did not find a paper or training script for this Qwen3.5 repository.

https://huggingface.co/z8086486/GCCL-Medical-LLM-Qwen3.5-4B
https://drive.google.com/drive/folders/1853oBf7JheLRu-g9ZCDIBwc2GUVj5kTl?usp=sharing
https://github.com/gachon-CCLab/GCCL-Medical-LLM-FlowerTune
https://github.com/gachon-CCLab/GCCL-Medical-LLM2-FlowerTune

## zenlm/zen-medical

No. No source names a training corpus a reader can open for this checkpoint. The cached card from 5 October 2026 matches the current README. It says the model was fine-tuned from Qwen/Qwen3-8B with Hanzo identity training, agentic-data training, and abliteration. The repository files are weights, a license, and the README. The Zen Identity dataset card lists Zen Nano, Zen Eco, Zen Coder, and Zen Omni, not this model. The Zen Agentic Dataset is a programming corpus and lists coder models. Specialty docs say "domain-specific corpora" and link a Zen Medical paper that is a PDF. That PDF was not opened.

https://huggingface.co/zenlm/zen-medical
https://docs.zenlm.org/docs/models/specialty/
https://huggingface.co/datasets/zenlm/zen-identity
https://huggingface.co/datasets/zenlm/zen-agentic-dataset
https://zenlm.org/research/
