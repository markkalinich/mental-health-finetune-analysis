# tsavage68/MedQA_L3_1000steps_1e5rate_SFT

## Sources

- https://huggingface.co/tsavage68/MedQA_L3_1000steps_1e5rate_SFT/raw/main/README.md — current model card; byte-identical to the 5 Oct cache (`e3405ac52585925402a667b03258fa7ec4b8cc9e4703f4b924a8230280b6c68b`)
- https://huggingface.co/api/models/tsavage68/MedQA_L3_1000steps_1e5rate_SFT — file list; F16 parameter count 8,030,261,248
- https://huggingface.co/tsavage68/MedQA_L3_1000steps_1e5rate_SFT/raw/main/config.json — LlamaForCausalLM, context 8192, float16
- https://huggingface.co/tsavage68/MedQA_L3_1000steps_1e5rate_SFT/raw/main/generation_config.json — temperature 0.6, top_p 0.9, do_sample true, max_length 4096
- https://huggingface.co/tsavage68/MedQA_L3_1000steps_1e5rate_SFT/raw/main/tokenizer_config.json — Llama 3 chat template, no system prompt
- https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct/raw/main/README.md — parent card; HTTP 401, not read

## Record

The card says the model was trained "on an unknown dataset." The training-data section says "More information needed." No Hub dataset id, row count, language, or provenance is given. Searches for the repo id and the model name did not find a paper or a GitHub training repo. The words MedQA in the repository name are not a dataset citation.

The Trainer tag list is `trl`, `sft`, `generated_from_trainer`. The card says it "has been generated automatically according to the information the Trainer had access to." The prose only says "fine-tuned," which does not name a loss. The recorded objective is SFT from that tag. Learning rate 1e-05, 1,000 steps, train batch size 2, gradient accumulation 2, total train batch size 4. No epoch count is stated. The loss table reaches epoch 0.9770 at step 1000. No sentence says full fine-tuning or LoRA. There is no `adapter_config.json`. The weights are four float16 shards.

The parent is `meta-llama/Meta-Llama-3-8B-Instruct`. The card says "a fine-tuned version of meta-llama/Meta-Llama-3-8B-Instruct." No outside source names this checkpoint.

The card does not state a medical use, an audience, or a task. Intended uses are "More information needed." The use claim is absent. There is no warning. Purpose is not stated, so no functions are recorded. Output type is not listed. Specialty is not stated.

The evaluation set is unnamed. The card reports "Loss: 0.3681" at step 1000. Context length in `config.json` is 8,192. `generation_config.json` sets temperature 0.6, top_p 0.9, and do_sample true. A chat template is present and does not set a system prompt. The parent card is gated, so there is no quoted text-only example. The license is `llama3`.

The inventory parent matches. The inventory method `sft` matches the Trainer tag. The inventory dataset "modified MedQA dataset" is not what the card says.
