# balarajr/triage-hospital-agent

## Sources

- https://huggingface.co/balarajr/triage-hospital-agent/raw/main/README.md — current model card; identical to the cached card
- https://huggingface.co/api/models/balarajr/triage-hospital-agent — file list and parameter count
- https://huggingface.co/balarajr/triage-hospital-agent/raw/main/config.json — context length 262144
- https://huggingface.co/balarajr/triage-hospital-agent/raw/main/generation_config.json — no sampling hyperparameters
- https://huggingface.co/balarajr/triage-hospital-agent/raw/main/tokenizer_config.json — no chat_template key
- https://huggingface.co/balarajr/triage-hospital-agent/raw/main/chat_template.jinja — chat template file
- https://huggingface.co/datasets/openlifescienceai/medmcqa — dataset named in the card YAML; viewer loads
- https://huggingface.co/datasets/bigbio/med_qa — dataset named in the card YAML; public dataset card

## Record

The training table says the dataset is "300 highly curated prompts." It gives no Hub id for those prompts. The card YAML also names `openlifescienceai/medmcqa` and `bigbio/med_qa`. The table does not say the 300 prompts are those exam sets. MedMCQA's card describes AIIMS and NEET PG multiple-choice questions. Its README split counts are 182,822 train, 4,183 validation, and 6,150 test, and the viewer loads. MedQA's card says the questions come from professional medical board exams: 12,723 English, 34,251 simplified Chinese, and 14,123 traditional Chinese. That dataset is public and not gated.

The training table says the method is "GRPO (Generative Reward Policy Optimization)," with LoRA rank 16, LoRA alpha 16, and "4-bit NF4 (bitsandbytes)." That is LoRA on a quantized base, for 1 epoch. Learning rate, batch size, and step count are not stated. The citation title on the same card says "DPO Fine-tuning." No paper or real GitHub repository names this checkpoint. The citation URL is `https://github.com/YOUR_USERNAME/triage`.

The card's base model is `Qwen/Qwen3.5-4B`. Nothing outside the card confirms that. The comparison table says the size is 4B. The Hub file list reports 4,205,751,296 BF16 parameters in five weight shards. There is no `adapter_config.json`, and the card does not say the adapter was merged.

The use claim is strong: "specialized for hospital crisis management and clinical triage decision-making." The warning is a disclaimer: "For research and simulation purposes only" and "Should not replace professional medical judgment." The license is Apache-2.0.

The purpose is that hospital-crisis sentence. The named use is research and simulation, so the audience is researchers. The card describes six agent roles: START triage, ICU bed allocation, drug-order checks, staff deployment, EHR failures, and oversight decisions.

The example asks "What is the correct triage action?" and calls `generate` with `max_new_tokens=150` and `temperature=0.1`. No sample completion is shown. The clinical work is triage, plus hospital operations such as bed allocation. The card names hospital crisis management and clinical triage, not a single specialty. Its benchmark table lists 100% survival and 100% violation detection on five scenarios, and a composite score of 87.33/100.

Serving is a text prompt. `config.json` sets the context length to 262,144. A chat template file is present. `generation_config.json` does not set temperature. The usage snippet loads `user/triage-qwen-4b-grpo`, which is not this repository id. The card does not state a system prompt.
