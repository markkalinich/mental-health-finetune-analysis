# ShivomH/Elixir-MentalHealth-3B

## Sources

- https://huggingface.co/ShivomH/Elixir-MentalHealth-3B — model page; same prose as the cached card
- https://huggingface.co/ShivomH/Elixir-MentalHealth-3B/raw/main/README.md — raw card; 401, repo is gated
- https://huggingface.co/api/models/ShivomH/Elixir-MentalHealth-3B — file list, parameter count, chat template
- https://github.com/Shivom2003/Elixir-MentalHealth-v2 — GitHub repo named on the card; README copies the card and prints this repo id
- https://github.com/Shivom2003/Elixir-MentalHealth-v2/blob/master/Fine-Tune%20Scripts/Elixir-MentalHealth-Finetune.ipynb — training notebook
- https://huggingface.co/datasets/ShivomH/MentalHealth-Support/raw/main/README.md — dataset card
- https://datasets-server.huggingface.co/size?dataset=ShivomH/MentalHealth-Support — row counts
- https://huggingface.co/datasets/ShenLab/MentalChat16K — source named for the long single-turn portion
- https://huggingface.co/datasets/jerryjalapeno/nart-100k-synthetic — source named for the multi-turn portion
- https://drive.google.com/file/d/1liCCt6O_CKxBLM3iXLOO96SpaNg54HDz/view?usp=sharing — training file linked from the card; not downloaded
- https://drive.google.com/file/d/1NbUiIbIrKE9ijnHFs0q8JBhsYQYzRDXn/view?usp=sharing — demo file linked from the card; not downloaded
- Cached card `revision_3_experiments/hf_inventory/cache/readmes/ShivomH__Elixir-MentalHealth-3B__2026-10-09.md` — sha256 372b313875aff26dcb4fb14b00803575d6c9d05c24b754b388cedc27ef79c73b

Searches for the repo id, the model name, arXiv, and GitHub did not find a paper that names this checkpoint.

## Record

The card names `ShivomH/MentalHealth-Support`. The dataset card says: "Keep in mind that this dataset is entirely synthetic." It says the long single-turn rows come from `ShenLab/MentalChat16K` and the multi-turn rows from `jerryjalapeno/nart-100k-synthetic`, and that the single-turn generation method was "OpenAI GPT-3.5 Turbo model with a customized Airoboros self-generation framework." The dataset loads. The dataset server reports 26,000 rows: 23,750 train, 1,250 validation, and 1,000 test. The model card says 25,000 conversations, with a training split of 23,750 and a validation split of 1,250. Language is English.

The card says the model was "adapted using QLoRA." The hyperparameter table sets LoRA rank 16, LoRA alpha 32, bnb quant type nf4, learning rate 3e-5, effective batch size 32, and 4 epochs. The GitHub notebook uses the same numbers, loads the base in NF4, and calls `transformers.Trainer`. It imports `SFTTrainer` and does not call it, and it does not name a loss. No source states a step count. The notebook's merge cell is optional. This Hub repo holds two full BF16 weight shards, 3,212,749,824 parameters, and no `adapter_config.json`. The card also says "only ~93MB adapter needs to be loaded."

The card and the GitHub README both name the parent `meta-llama/Llama-3.2-3B-Instruct`. The GitHub README prints `model_id = "ShivomH/Elixir-MentalHealth-3B"`. The card lists language English and license `llama3.2`. The Hub page rounds the size to 3B parameters.

The card says: "The model is designed to provide empathetic, safe, and supportive responses while maintaining clear professional boundaries." It also says the model is for "supportive chatbot applications," so the output type is a chatbot and the use claim is strong. The warning is an explicit prohibition: "Out-of-Scope Use (should NOT be used for): Medical diagnosis or treatment planning." The same list also excludes "Emergency mental health intervention." The card also says the model "is not a replacement for professional mental health services." The evaluation tables give this model BERTScore F1 0.884, ROUGE-L 0.252, perplexity 2.572, and toxicity mean 0.0021. The GitHub README prints that toxicity mean as 0.0020.

The card's quickstart sends a text user message: "I am tired of living. Please suggest me strategies to get rid of this ugly feeling." The system line in that example is "You are a supportive and empathetic AI assistant trained to provide warm and professional mental health guidance." The later inference function sets temperature 0.4, top_p 0.8, do_sample True, and max_new_tokens 512. The card and the notebook set the sequence length to 1024. `config.json` returned 401, so the architecture context length in that file was not read. The model API returns a Llama 3 text chat template.
