# maliksaad/empathLM

## Sources

https://huggingface.co/maliksaad/empathLM — model card (current README matches the 5 Oct cache)
https://huggingface.co/api/models/maliksaad/empathLM — file list and parameter count
https://huggingface.co/maliksaad/empathLM/raw/main/config.json — Llama config, context 8192, float32
https://huggingface.co/maliksaad/empathLM/raw/main/generation_config.json — token ids only
https://huggingface.co/maliksaad/empathLM/raw/main/tokenizer_config.json — no chat template key
https://huggingface.co/maliksaad/empathLM/raw/main/chat_template.jinja — SmolLM chat template
https://huggingface.co/datasets/maliksaad/empathLM-dataset — 200-row training set, loads
https://huggingface.co/spaces/maliksaad/empathLM-demo — Gradio demo that loads this repository id
https://github.com/maliksaad/empathLM — linked from the card; the page returns 404

## Record

The training set is `maliksaad/empathLM-dataset`. The card says "Training Examples | ~180 (90% of 200)". The viewer has 180 train rows and 20 test rows. The dataset card says "This dataset contains 200 curated examples of AI responses to people experiencing emotional distress." It does not say who wrote the gold `empathetic_response` field. `unsafe_response` is described as "How a typical AI responds". Language is English. The dataset loads.

The card says the model is "Fine-tuned" and does not name a loss. Supervised fine-tuning is not stated. LoRA, QLoRA, and a full update are not stated. The repository has one float32 `model.safetensors` (134,515,008 parameters) and no `adapter_config.json`. That does not say whether training updated every weight. Epochs 3, batch size 8, learning rate 2e-5, max sequence length 512. No step count. The parent on the card is `HuggingFaceTB/SmolLM2-135M-Instruct`. No other source names that parent. The linked GitHub repository returns 404.

The card presents a person to talk to. "You are EmpathLM — an emotionally intelligent AI trained in Motivational Interviewing and Cognitive Behavioral Therapy. When someone shares emotional pain." That is a chatbot. The use claim is Strong because the purpose is CBT, motivational interviewing, and emotional support. There is no warning about therapy, diagnosis, or medical use. License is MIT. No paper names this repository. The card says it was "benchmarked against GPT-4o-mini and a Groq baseline on 20 unseen test situations" and does not print the scores.

The usage example is text only. `chat_template.jinja` is present. If the first message is not a system message, the template inserts "You are a helpful AI assistant named SmolLM, trained by Hugging Face". `generation_config.json` does not set temperature. The card's example uses max_new_tokens 200 and temperature 0.7. `config.json` sets `max_position_embeddings` to 8192. The demo space loads `maliksaad/empathLM` on text and uses temperature 0.7, do_sample true, and max_new_tokens 200.
