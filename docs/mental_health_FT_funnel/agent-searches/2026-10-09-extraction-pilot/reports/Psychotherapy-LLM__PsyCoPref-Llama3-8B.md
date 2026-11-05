# Psychotherapy-LLM/PsyCoPref-Llama3-8B

## Sources

https://huggingface.co/Psychotherapy-LLM/PsyCoPref-Llama3-8B/raw/main/README.md — current model card; same bytes as the 5 October 2026 cache (sha256 3f6b52f46cf1b3476611cac786b8c344c2674191be023fe863f8ab211e9ba3e2)
https://huggingface.co/api/models/Psychotherapy-LLM/PsyCoPref-Llama3-8B — file list, safetensors parameter total, spaces
https://huggingface.co/Psychotherapy-LLM/PsyCoPref-Llama3-8B/resolve/main/config.json — architecture, context length, `_name_or_path`
https://huggingface.co/Psychotherapy-LLM/PsyCoPref-Llama3-8B/resolve/main/generation_config.json — sampling settings
https://huggingface.co/Psychotherapy-LLM/PsyCoPref-Llama3-8B/resolve/main/tokenizer_config.json — Llama 3.1 chat template
https://arxiv.org/abs/2502.19731 — abstract; names the 87% model PsychoCounsel-Llama3-8B
https://arxiv.org/html/2502.19731v2 — HTML full text of Zhang, Eack, and Chen
https://huggingface.co/Psychotherapy-LLM/PsychoCounsel-Llama3-8B — redirects to this repository
https://huggingface.co/Psychotherapy-LLM/PsyCoPref-Llama3-8B-Reward/raw/main/README.md — sibling reward-model card; links the policy as PsychoCounsel-Llama3-8B
https://huggingface.co/Psychotherapy-LLM — organization page; two models and the PsyCoPref dataset
https://huggingface.co/datasets/Psychotherapy-LLM/PsyCoPref/raw/main/README.md — preference dataset card; PsychoCounsel-Preference redirects here
https://huggingface.co/datasets/nbertagnolli/counsel-chat/raw/main/README.md — counsel-chat dataset card
https://github.com/nbertagnolli/counsel-chat — data repository the paper links; its `train.py` is an older GPT-2 script, not this checkpoint
https://huggingface.co/datasets/MentalAgora/TherapyTalk/raw/main/README.md — MentalAgora client-speech source
https://huggingface.co/datasets/EmoCareAI/Psych8k — Psycho8k; gated, viewer does not load
https://huggingface.co/datasets/Amod/mental_health_counseling_conversations — amod-counsel; gated, viewer does not load
https://huggingface.co/datasets/ShenLab/MentalChat16K/raw/main/README.md — MentalChat16K
https://huggingface.co/datasets/saxenaindresh681/microsoft-phi2-mental-health/raw/main/README.md — phi2Mental; license only
https://huggingface.co/datasets/nvidia/HelpSteer2 — used in the paper's reward-model comparison, not as this policy's training set
https://huggingface.co/spaces/razaali10/Psycho_Counsel_Demo/raw/main/README.md — demo that names PsychoCounsel-Llama3-8B
https://huggingface.co/spaces/razaali10/Psychocounsel/raw/main/README.md — second Space the Hub lists on this model

## Record

The card says this checkpoint was trained with preference learning on PsyCoPref. That Hub dataset is `Psychotherapy-LLM/PsyCoPref` (the old id `Psychotherapy-LLM/PsychoCounsel-Preference` redirects there). It loads. The card has 36,653 rows: 34,329 train and 2,324 test. The paper's best model is not a fit on those stored pairs. It is iterative DPO: "in each iteration, 8 responses are generated for each client speech and ranked by the reward model of the same size as the base model. The responses with the highest and lowest rewards are then annotated as online preference pairs, which are used to train the base model with the DPO objective. The client speeches for each iteration are 6400 sampled from the train set of PsyCoPref." Those online pairs are synthetic and are not a separate Hub dataset. Client speeches in PsyCoPref come from counsel-chat (`nbertagnolli/counsel-chat`, 2,775 English rows, loads), MentalAgora (`MentalAgora/TherapyTalk`, 104 English rows, loads), TherapistQA (no Hub dataset found), Psycho8k (`EmoCareAI/Psych8k`, English, gated, does not load), amod-counsel (`Amod/mental_health_counseling_conversations`, English, gated, does not load), MentalChat16K (`ShenLab/MentalChat16K`, 16,084 English rows, loads; 9,775 synthetic conversations and 6,338 interview pairs), and phi2Mental (`saxenaindresh681/microsoft-phi2-mental-health`, 2,000 rows, loads; the card states no language and no provenance). HelpSteer2 is used only to train comparison reward models.

The named loss is DPO. The paper says "We refer to Llama3-8B (+DPO-Iter) as PsyCo-Llama3-8B" and that this run "achieves the best performance, with a high overall win rate of 87.0% against GPT-4o." The card claims that same 87% figure. "The training configuration includes a batch size of 64, a learning rate of 5e-7, and a total of 1,600 training steps." Beta is 0.1 "for DPO across all the experiments." The paper does not say full fine-tuning, LoRA, or QLoRA, and the repository has no `adapter_config.json`. Epochs are not stated for this run. The released weights are float32, 8,030,261,248 parameters.

The parent is `meta-llama/Llama-3.1-8B-Instruct`. The card says "It's a fine-tuned meta-llama/Llama-3.1-8B-Instruct model." The paper says "We use Llama3.2-3B-Instruct and Llama3.1-8B-Instruct as the base models." `config.json` `_name_or_path` is `Psychotherapy-LLM/PsychoCounsel-Llama3-8B`, which redirects to this repository. It is not a second parent.

The card presents a dialogue model for counseling replies: "The model aims to improve the quality of responses in psycho-counseling sessions and achieves a win rate of 87% against GPT-4o." That is a strong therapy claim. The card has no warning. The paper says "these responses should not be directly exposed to clients without review by real therapists. Instead, they serve as assistive suggestions to help therapists draft responses." License on the card is `cc-by-nc-4.0`. No source states the model's languages.

A chat template is present in `tokenizer_config.json`. It is the Llama 3.1 Instruct template. No therapist system prompt is stored in the repository. `generation_config.json` sets `do_sample` true, `temperature` 0.6, and `top_p` 0.9. Context length in `config.json` is 131,072.
