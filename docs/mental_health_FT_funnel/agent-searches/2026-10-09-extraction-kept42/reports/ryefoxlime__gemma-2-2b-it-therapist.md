# ryefoxlime/gemma-2-2b-it-therapist

## Sources

- https://huggingface.co/ryefoxlime/gemma-2-2b-it-therapist/raw/main/README.md — current model card; same bytes as the cached card
- revision_3_experiments/hf_inventory/cache/readmes/ryefoxlime__gemma-2-2b-it-therapist__2026-10-09.md — cached card, sha256 18a25a2889311f70d0b21751c27d417b00acfff4db0d30054972c3fb39332d26
- https://huggingface.co/api/models/ryefoxlime/gemma-2-2b-it-therapist — file list and safetensors parameter count
- https://huggingface.co/ryefoxlime/gemma-2-2b-it-therapist/raw/main/config.json — architecture and parent path
- https://huggingface.co/ryefoxlime/gemma-2-2b-it-therapist/raw/main/generation_config.json — token ids only
- https://huggingface.co/ryefoxlime/gemma-2-2b-it-therapist/raw/main/tokenizer_config.json — chat template
- https://huggingface.co/ryefoxlime/gemma-2-2b-it-therapist/raw/main/ModelFile — Ollama file pointing at a local GGUF path
- https://huggingface.co/google/gemma-2-2b-it — parent card, text-only usage example
- https://arxiv.org/abs/1910.09700 — carbon-calculator paper linked from the card template
- https://arxiv.org/html/1910.09700 — HTML full text of that paper
- https://arxiv.org/html/2408.00118v1 — Gemma 2 paper found by name search; listed only; it does not print this repo id
- https://huggingface.co/datasets/nbertagnolli/counsel-chat — dataset named in the card YAML
- https://huggingface.co/api/datasets/nbertagnolli/counsel-chat — dataset is public
- https://datasets-server.huggingface.co/size?dataset=nbertagnolli/counsel-chat — 2,775 rows, viewer loads
- https://github.com/nbertagnolli/counsel-chat — dataset code repository named on the dataset card
- https://featherless.ai/models/ryefoxlime/gemma-2-2b-it-therapist — hosting page found by search; generated blurb, not used as a training source

## Record

The card names one dataset, `nbertagnolli/counsel-chat`, in the YAML line `datasets: - nbertagnolli/counsel-chat`. The Training Data section of the same card is still the placeholder "[More Information Needed]". The dataset card says "The text was written by licensed counselors in the United States and annonymous individuals" and "The dataset was scraped on 20220401 from counselchat.com." The Hub dataset viewer loads. The size endpoint reports 2,775 rows. Language on the dataset card is English. Provenance is human.

No source states a training objective, a LoRA or full update, a rank, a step count, or a learning rate. The Training Procedure section is "[More Information Needed]". "Fine-tuned" alone is not an objective, and the card does not even say that in its own words. The repository has full float16 safetensors and a Q4_K_M GGUF file, and it has no `adapter_config.json`. Those files do not say how the checkpoint was trained.

The card YAML says `base_model: google/gemma-2-2b-it`. `config.json` says `"_name_or_path": "google/gemma-2-2b-it"`. Those two agree. The model API reports 2,614,341,888 parameters. The card's own first paragraph is "This is the model card of a 🤗 transformers model that has been pushed on the Hub. This model card has been automatically generated."

Output type is Not listed: that paragraph is the only description, and it does not say what the model emits. Use claim is Strong because the card has no description and the repository name is `ryefoxlime/gemma-2-2b-it-therapist`. Warning is None. The Bias section is "[More Information Needed]". The leftover template line "Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model" does not forbid therapy, counseling, diagnosis, or medical advice. The Lacoste et al. paper linked in the environmental-impact boilerplate does not name this repository. The Gemma 2 paper names `gemma-2-2b-it`, not this checkpoint. A Featherless hosting page adds a generated sentence about therapeutic conversation; that sentence is not on the model card and is not used here.

The parent card says "They are text-to-text, decoder-only large language models" and its example is a user message, "Write a hello world program". This checkpoint's chat template is the Gemma turn template, and it raises "System role not supported". No system prompt is stated. `generation_config.json` has no temperature, top_p, top_k, or max_new_tokens. `max_position_embeddings` is 8192. The card YAML says `language: en`. No license is stated. No evaluation result is stated. The inventory row lists this dataset, this parent, and no method. That matches what the sources say.
