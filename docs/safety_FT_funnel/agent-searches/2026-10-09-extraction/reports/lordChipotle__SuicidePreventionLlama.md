# lordChipotle/SuicidePreventionLlama

## Sources

https://huggingface.co/lordChipotle/SuicidePreventionLlama/raw/main/README.md — current model card; same bytes as the cache (sha256 89632171f577f2365f7073d2cc9e8d08699c92d7562d3adf0b1b6b9514817684)
https://huggingface.co/api/models/lordChipotle/SuicidePreventionLlama — file list, 3,212,749,824 parameters, base-model tag
https://huggingface.co/lordChipotle/SuicidePreventionLlama/raw/main/config.json — LlamaForCausalLM, max position embeddings 131072
https://huggingface.co/lordChipotle/SuicidePreventionLlama/raw/main/generation_config.json — sampling settings
https://huggingface.co/lordChipotle/SuicidePreventionLlama/raw/main/tokenizer_config.json — Llama 3.2 chat template
https://colab.research.google.com/drive/1vbio7VWmkpQoTnDUg32TABxxf4VcBBeY?usp=sharing — training notebook linked from the card; Google sign-in wall, contents not read
https://huggingface.co/datasets/nbertagnolli/counsel-chat — CounselChat dataset card
https://huggingface.co/datasets/nbertagnolli/counsel-chat/raw/main/README.md — CounselChat README
https://datasets-server.huggingface.co/size?dataset=nbertagnolli/counsel-chat — 2,775 rows, viewer loads
https://huggingface.co/datasets/thePixel42/depression-detection — Hub dataset whose card lists r/teenagers, r/SuicideWatch, and r/depression
https://huggingface.co/datasets/thePixel42/depression-detection/raw/main/README.md — that dataset's card
https://www.kaggle.com/datasets/nikhileswarkomati/suicide-watch/versions/13 — Kaggle original named by that dataset card
https://datasets-server.huggingface.co/size?dataset=thePixel42/depression-detection — 200,000 rows, viewer loads

## Record

The card says the model was trained on four sources. CounselChat is the only one it names with a Hub id, `nbertagnolli/counsel-chat`, in the YAML `datasets` field and in the sentence "We combined multiple datasets to train this model, including" CounselChat. That dataset loads: 2,775 rows, language "English", and "The text was written by licensed counselors in the United States and annonymous individuals." The Reddit line is "Reddit-based suicide detection data (r/SuicideWatch, r/depression, r/teenagers)." The card does not give a dataset id. The Hub card at `thePixel42/depression-detection` says "The posts have been collected from 3 subreddits: r/teenagers, r/SuicideWatch, and r/depression" and points at the Kaggle set `nikhileswarkomati/suicide-watch`. That Hub set loads and has 200,000 rows. Twitter is only "Twitter suicidal-intent classification data"; several Hub and Kaggle sets match that phrase, and the card does not pick one. PAIR is "short counseling interactions with high- and medium-quality reflections." That wording matches the EMNLP 2022 PAIR reflection set, which is not a Hub dataset the card links, so no Hub id is recorded.

The card does not name a loss. It says the model is "fine-tuned" and "We used short prompts for classification tasks, and Q&A style prompts for therapy." Update scope is LoRA, with this sentence: "We used **LoRA** adapters or 4-bit quantization to reduce GPU memory usage." The "or" does not say whether the base was 4-bit during training. Stated hyperparameters are "Batch Size: 2", "Max Steps: 60 (example short run)", and "Learning Rate: 2e-4". Rank, alpha, and epoch count are not on the card. The Colab notebook the card links did not open without a Google sign-in. The repository publishes two safetensors shards and no `adapter_config.json`. Nothing says whether an adapter was merged.

The card YAML says `base_model: meta-llama/Llama-3.2-3B-Instruct`. The prose only says "LLaMA-based architecture" and "fine-tuned LLaMA-based (or derivative)". No paper or GitHub repository names this checkpoint. The Hub API tag repeats the YAML parent. The weight index reports 3,212,749,824 parameters.

The card presents a therapeutic reply a person would receive, so the output type is a chatbot: "provide a short therapeutic-style reply if suicidality is detected", and the example is `model("Respond like a therapist:\n" + text, max_new_tokens=256)`. The same card also asks the model to "detect suicidal or self-harm risk" and to print a label such as "suicidal". The use claim is strong because of "Respond like a therapist" and "Therapeutic Q&A (CounselChat & PAIR) – used to produce empathetic, reflective responses." The warning is a disclaimer, not a ban: "This model is **not** a substitute for professional mental-health services or emergency intervention." A later line says "This model does not replace mental-health professionals." Intended use is "research" and "demonstration or proof-of-concept." No evaluation numbers are reported. No license is stated.

The usage example runs on a text string: `text = "Life is too painful. I'm done. I want to end it."` `tokenizer_config.json` has a chat template. `generation_config.json` sets `do_sample` true, `temperature` 0.6, and `top_p` 0.9. `config.json` sets `max_position_embeddings` to 131072. The card does not set a system prompt.
