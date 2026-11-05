# anon-caa-neurips/qwen3-4b-clinical-long-bench-grpo

## Sources

- https://huggingface.co/anon-caa-neurips/qwen3-4b-clinical-long-bench-grpo/raw/main/README.md — current model card; identical to the cached card
- https://huggingface.co/api/models/anon-caa-neurips/qwen3-4b-clinical-long-bench-grpo — file list and parameter count
- https://huggingface.co/anon-caa-neurips/qwen3-4b-clinical-long-bench-grpo/raw/main/config.json — context length 40960
- https://huggingface.co/anon-caa-neurips/qwen3-4b-clinical-long-bench-grpo/raw/main/generation_config.json — sampling defaults
- https://huggingface.co/anon-caa-neurips/qwen3-4b-clinical-long-bench-grpo/raw/main/tokenizer_config.json — no chat_template key
- https://huggingface.co/anon-caa-neurips/qwen3-4b-clinical-long-bench-grpo/raw/main/chat_template.jinja — Qwen chat template
- https://arxiv.org/abs/2609.38480 — KlinikeBench abstract
- https://arxiv.org/html/2609.38480 — HTML full text; links this repository as the SFT + GRPO checkpoint
- https://github.com/Zehui127/klinikebench-train — training README and GRPO script
- https://huggingface.co/datasets/anon-caa-neurips/klinikebench — 333-task benchmark; viewer loads
- https://huggingface.co/datasets/anon-caa-neurips/KLINIKEBENCH-Trajectories — trajectories used for the earlier SFT stage
- https://zehui127.github.io/klinikebench/ — project page
- https://huggingface.co/spaces/anon-caa-neurips/klinikebench-demo — demo linked from the paper

## Record

This checkpoint is a GRPO run on KlinikeBench. The card calls that benchmark Clinical-Long-Bench: "333 long-horizon clinical consultations with a simulated patient," split "283 training tasks / 50 held-out test tasks." The Hub dataset `anon-caa-neurips/klinikebench` is those 333 tasks. Its card says the cases are clinician-authored and "Patients are simulated by an LLM; no real patient data is included." The viewer loads. English is the dataset language tag. The earlier SFT stage, which this file is initialized from, used filtered model trajectories: the paper says 1,235 trajectories remained after length filtering, from a release of 13,962 trajectories at `anon-caa-neurips/KLINIKEBENCH-Trajectories`.

The loss for this file is GRPO. The card says "GRPO (SkyRL) from the SFT checkpoint (`qwen3-4b-clinical-long-bench-sft`)." Reward is "(2·diagnosis + required_tools + parameterised_actions + must_ask) / 5." The run uses learning rate `1e-6`, 8 tasks and 8 rollouts per step, and no KL penalty. The released weights are step 50, "the RL checkpoint with the highest held-out `pass@1`." The card does not say LoRA or full updates. The paper says the SFT stage fine-tunes all parameters, and the GRPO stage trains with FSDP. The GRPO script has no LoRA setting. There is no `adapter_config.json`. The paper's appendix reports results through step 30 of a planned 315; the card and the training README both say the released file is step 50.

The card's base model is `Qwen/Qwen3-4B`. The training repo agrees, and it also says GRPO starts from the released SFT checkpoint of that base. The Hub file list reports 4,022,468,096 parameters. The card's title says Qwen3-4B.

The use claim is weak. The card says "Research on long-horizon clinical agents and RL reward design." The warning is a disclaimer: "Not a medical device; not for clinical use." It does not say "do not use" or "must not." The license on the card is Apache-2.0.

The purpose is that research sentence. The audience is researchers. The model is a research artifact: inside the benchmark it talks with a simulated patient, is scored on diagnosis, and writes an `analysis` and a `plan`.

Each reply is a JSON object with `analysis`, `plan`, `commands`, and `task_complete`. The clinical work is a consultation with a simulated patient and a diagnosis gate. The card names no specialty, so the field is general clinical work. On 50 held-out tasks this checkpoint's pass@1 is 0.12, diagnosis 0.48, required tools 0.36, and must-ask 0.71.

Serving is text. `generation_config.json` sets `do_sample` true, temperature 0.6, top_k 20, and top_p 0.95. Training rollouts used temperature 1.0. `config.json` sets the context length to 40960. A chat template is in `chat_template.jinja`. The card does not give a system prompt.
