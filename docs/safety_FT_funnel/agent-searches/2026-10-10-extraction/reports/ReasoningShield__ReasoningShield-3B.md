# ReasoningShield/ReasoningShield-3B

## Sources

https://huggingface.co/ReasoningShield/ReasoningShield-3B/raw/main/README.md — current model card; byte-identical to the cached card
revision_3_experiments/hf_inventory/cache/readmes/ReasoningShield__ReasoningShield-3B__2026-10-09.md — cached card, sha256 7a7882645b5ffc930903e081fbc8b6aefaeee16653d6291e64413ba862a742e6
https://huggingface.co/api/models/ReasoningShield/ReasoningShield-3B — file list and parameter count
https://huggingface.co/ReasoningShield/ReasoningShield-3B/resolve/main/config.json — max position embeddings 131072
https://huggingface.co/ReasoningShield/ReasoningShield-3B/resolve/main/generation_config.json — temperature 0.6, top_p 0.9, do_sample true
https://huggingface.co/ReasoningShield/ReasoningShield-3B/resolve/main/tokenizer_config.json — chat template present; model_max_length 131072
https://huggingface.co/ReasoningShield/ReasoningShield-3B/raw/main/reasoningshield_prompt.txt — auditor system prompt
https://arxiv.org/abs/2505.17244 — paper
https://arxiv.org/html/2505.17244 — paper HTML, including Appendix G.1 training details
https://github.com/CosmosYi/ReasoningShield — code repository linked from the card; names this checkpoint
https://cosmosyi.github.io/ReasoningShield/ — project page
https://huggingface.co/datasets/ReasoningShield/ReasoningShield-Dataset — training dataset card
https://datasets-server.huggingface.co/is-valid?dataset=ReasoningShield/ReasoningShield-Dataset — dataset viewer loads

## Record

The training set is `ReasoningShield/ReasoningShield-Dataset`. The card says "The model is trained on a high-quality dataset of 7,000 (Query, CoT) pairs." The dataset card splits that into 4,358 SFT samples and 2,642 DPO samples, and says the train pairs are "human-AI annotated", so the provenance is mixed. Language on the dataset card is `en`. The Hub viewer loads. The test split (2,200) is evaluation, not the training count.

Training is two stages, both full-parameter. Stage 1 is supervised fine-tuning. The paper says "we perform Supervised Fine-Tuning (SFT)" for 3 epochs, batch size 2, learning rate 1e-5, bf16. Stage 2 is DPO. The card says "Stage 2: Direct Preference Optimization Training" for 2 epochs, batch size 2. The paper says stage 2 is "full-parameter DPO" at learning rate 2.0e-6, with the other settings matching stage 1. The JSON stores the final stage: objective `dpo`, 2 epochs, learning rate 2e-6, batch size 2. No LoRA rank is stated. The public GitHub repo has inference scripts, not the LlamaFactory config.

The parent on this repository's card is `meta-llama/Llama-3.2-3B-Instruct`. The paper says the authors "select Llama-3.2-1B and Llama-3.2-3B" as the two bases; the 1B line is the sibling checkpoint. The Hub API reports 3,212,749,824 parameters. The license is `apache-2.0`.

This is a classifier. The card says it is "tailored to identify hidden risks in intermediate reasoning steps". The input is a user query plus the model's thought (or, the card says, the answer). The output is an analysis and a judgment of 0, 0.5, or 1. The card's risk list is Violence, Hate & Toxicity, Deception & Misinformation, Rights Violation, Sex, Child Abuse, CyberSecurity, Prohibited Items, Economic Harm, Political Risks, plus Other Risks in the prompt. The 3B row reports average F1 91.8 on open-source traces and 81.4 on commercial traces. The paper names `ReasoningShield-3B` and those same averages. It does not print the Hugging Face id; the GitHub README does.

Serving is text only. The example puts `Query` and `Thought` in the user message and generates with `max_new_tokens=1024`. `generation_config.json` sets `do_sample` true, temperature 0.6, and top_p 0.9. Context length is 131072. The chat template is inside `tokenizer_config.json`. There is no adapter file in the model repository.
