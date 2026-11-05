# Wothmag07/counseLLM

## Sources

https://huggingface.co/Wothmag07/counseLLM — model card (current README matches the 5 Oct cache)
https://huggingface.co/api/models/Wothmag07/counseLLM — repository file list
https://huggingface.co/Wothmag07/counseLLM/raw/main/config.json — architecture and context length
https://huggingface.co/Wothmag07/counseLLM/raw/main/generation_config.json — sampling defaults
https://huggingface.co/Wothmag07/counseLLM/raw/main/tokenizer_config.json — chat template
https://huggingface.co/Wothmag07/counseLLM/raw/main/sft/adapter_config.json — SFT LoRA rank 64, alpha 128
https://huggingface.co/Wothmag07/counseLLM/raw/main/dpo/adapter_config.json — DPO LoRA rank 16, alpha 32
https://github.com/wothmag07/counseLLM — training repository README
https://github.com/wothmag07/counseLLM/blob/main/configs/sft_config.yaml — SFT QLoRA settings
https://github.com/wothmag07/counseLLM/blob/main/configs/dpo_config.yaml — DPO QLoRA settings
https://github.com/wothmag07/counseLLM/blob/main/train/sft_train.py — SFT trainer
https://github.com/wothmag07/counseLLM/blob/main/train/dpo_train.py — DPO trainer
https://github.com/wothmag07/counseLLM/blob/main/data/prepare_sft_data.py — five-dataset merge and the 10,000-row Empathetic Dialogues subsample
https://github.com/wothmag07/counseLLM/blob/main/data/prepare_dpo_data.py — 2,000-pair preference sample
https://huggingface.co/datasets/ShenLab/MentalChat16K — mixed synthetic and interview counseling data, 16,084 rows, loads
https://huggingface.co/datasets/Estwld/empathetic_dialogues_llm — reformatted Empathetic Dialogues, 24,850 rows, loads
https://huggingface.co/datasets/facebook/empathetic_dialogues — original Empathetic Dialogues; viewer does not load this copy
https://huggingface.co/datasets/EmoCareAI/Psych8k — gated; dataset body does not load without approval
https://huggingface.co/datasets/nbertagnolli/counsel-chat — CounselChat therapist answers, 2,775 rows, loads
https://huggingface.co/datasets/thu-coai/esconv — ESConv, 1,300 rows, loads
https://huggingface.co/datasets/Psychotherapy-LLM/PsyCoPref — current id of PsychoCounsel-Preference, 36,653 rows, loads
https://arxiv.org/html/2512.06097v1 — unrelated healthcare DPO paper; does not name this repository
https://www.sciencedirect.com/science/article/pii/S2667118225000017 — CounseLLMe dataset paper; does not name this repository
https://featherless.ai/models/Wothmag07/counseLLM — hosted API page for this repository id

## Record

The SFT mix is five datasets. MentalChat16K is mixed: the dataset card says 9,775 conversations "were generated using the OpenAI GPT-3.5 Turbo model" and 6,338 pairs were paraphrased from interview transcripts with Mistral-7B-Instruct-v0.2. The viewer has 16,084 rows and the script loads the train split. Empathetic Dialogues is the Hub set `Estwld/empathetic_dialogues_llm` (24,850 rows, a reformat of the human Empathetic Dialogues corpus); `prepare_sft_data.py` sets `EMPATHETIC_DIALOGUES_SUBSAMPLE = 10_000`. Psych8k is gated. The model card calls it "Real therapist transcripts" and does not give an exact count (~8K). The dataset body did not load. counsel-chat is a scrape of therapist replies on CounselChat; the viewer has 2,775 rows and the card says ~940 after deduplication. ESConv is human emotional-support conversations; the viewer has 1,300 rows and the card says ~910. DPO uses `Psychotherapy-LLM/PsychoCounsel-Preference`, which now redirects to `Psychotherapy-LLM/PsyCoPref` (36,653 rows). The script sets `SAMPLE_SIZE = 2000`. The dataset card does not say whether the chosen and rejected replies were written by people or by models, and it does not name a language.

Two named losses, both QLoRA on a 4-bit NF4 base. The card says "Supervised Fine-Tuning (SFT) on 36K counseling examples followed by Direct Preference Optimization (DPO) on ~2K preference-filtered pairs." SFT: "QLoRA (4-bit NF4 + double quantization)", rank 64, alpha 128, learning rate 2e-4, 2 epochs, effective batch size 16. DPO: "QLoRA on SFT-merged base", rank 16, alpha 32, learning rate 1e-5, 1 epoch, effective batch size 8. The JSON numbers are the DPO stage. Neither the card nor the YAML sets a step count. The root repository is "Ready-to-use Llama 3.1 8B + SFT + DPO merged." `sft/` and `dpo/` still hold the unmerged adapters. Both adapter configs name `meta-llama/Llama-3.1-8B-Instruct`.

The parent is `meta-llama/Llama-3.1-8B-Instruct`. The card, both adapter configs, and `configs/sft_config.yaml` all print that id.

The card presents a counselor. The usage example says "You are a mental health counselor providing supportive, empathetic guidance." That is a chatbot, and the use claim is Strong. The warning is Disclaimer only: "This is an AI research project and is not a substitute for professional mental health care." The out-of-scope list also says the model "should not be relied upon for suicide prevention or emergency situations" and "is not validated for clinical use." Those sentences do not say "must not" or "should not be used for" therapy, counseling, support, diagnosis, treatment, or medical advice. Language is English. The stated size is Llama 3.1 8B. License on the model card is Apache 2.0. The GitHub code license is MIT. No paper prints `Wothmag07/counseLLM`.

The card's example is text only: a system string plus "I've been feeling really anxious about work lately and I can't sleep." `tokenizer_config.json` has a Llama 3.1 chat template. `generation_config.json` sets `do_sample` true, temperature 0.6, top_p 0.9. The card's own `generate()` call uses temperature 0.7, top_p 0.9, repetition_penalty 1.1, and max_new_tokens 512. `config.json` sets `max_position_embeddings` to 131072. The training configs cap sequence length at 2048. Evaluation on the card: perplexity 4.18 / 3.64 / 3.13 for base / SFT / DPO, and GPT-4o overall 4.35 / 3.52 / 4.71, on 25 prompts.
