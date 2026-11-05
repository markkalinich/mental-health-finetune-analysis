# SumanKoo7/Pharmapedia-FT-Gemma-3-1b-it

## Sources

https://huggingface.co/SumanKoo7/Pharmapedia-FT-Gemma-3-1b-it/raw/main/README.md — current model card; identical to the 10 October 2026 cache (sha256 365b58f1ee68155a6816dfe67d9234bddff0eaa710f12a516c66124027ddadf9)
https://huggingface.co/api/models/SumanKoo7/Pharmapedia-FT-Gemma-3-1b-it — file list and parameter count
https://huggingface.co/SumanKoo7/Pharmapedia-FT-Gemma-3-1b-it/raw/main/config.json — Gemma 3 text architecture and context length
https://huggingface.co/SumanKoo7/Pharmapedia-FT-Gemma-3-1b-it/raw/main/generation_config.json — sampling settings
https://huggingface.co/SumanKoo7/Pharmapedia-FT-Gemma-3-1b-it/raw/main/tokenizer_config.json — chat template
https://huggingface.co/datasets/llamafactory/PubMedQA/raw/main/README.md — dataset named in the card YAML
https://datasets-server.huggingface.co/size?dataset=llamafactory/PubMedQA — 11,000 rows; the viewer loads
https://arxiv.org/abs/1910.09700 — carbon-emissions paper linked from the template; it does not name this repository
https://arxiv.org/abs/1909.06146 — PubMedQA paper cited by the dataset card; it does not name this repository

## Record

The only training data the card names is the YAML line `datasets: llamafactory/PubMedQA`. That Hub dataset loads. Its card says "The training set is composed of 10,000 examples of the PQA-U dataset and the test set is composed of 1,000 examples of the PQA-L dataset." The viewer has 10,000 train rows and 1,000 test rows. Language is English. Those two PubMedQA splits are drawn from PubMed abstracts, not from the artificially generated PQA-A split. The card body says Training Data is "[More Information Needed]".

The YAML tags are `trl` and `sft`. That is the only method label. The Training Procedure section is "[More Information Needed]". There is no sentence that states a loss, no LoRA rank, and no learning rate, batch size, epoch count, or step count. The repository has one `model.safetensors` file and no adapter file. The saved weights are F32. Whether the update was full or a merged adapter is not stated.

The YAML `base_model` is `google/gemma-3-1b-it`. No other source names a parent. The Hub file list reports 1,052,068,992 parameters.

The card does not say what the model is for. Direct Use is "[More Information Needed]". It does not name an audience or a function. The YAML dataset name is a medical benchmark, so the use claim is weak. The only limitation sentence is the template line about risks and biases. It does not mention diagnosis or treatment. The repository name is not treated as a pharmacy claim.

PubMedQA, named in the YAML, is a biomedical exam-style question set. The card does not name a specialty in a sentence. The YAML lists the metric accuracy, and the Results section is "[More Information Needed]".

`config.json` is `Gemma3ForCausalLM` with `model_type` `gemma3_text` and max position 32,768. There is no vision config. A chat template is in `tokenizer_config.json` and it has no default system prompt. `generation_config.json` sets do_sample true, top_k 64, and top_p 0.95. License in the YAML is mit. No GitHub repository and no paper name this checkpoint. The arXiv link in the card is the template's carbon-emissions citation.
