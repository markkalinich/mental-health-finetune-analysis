# ZennyKenny/Daredevil-8B-abliterated

## Sources

https://huggingface.co/ZennyKenny/Daredevil-8B-abliterated/raw/main/README.md — current model card; byte-identical to the cached card
/home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/ZennyKenny__Daredevil-8B-abliterated__2026-10-09.md — cached card
https://huggingface.co/api/models/ZennyKenny/Daredevil-8B-abliterated — file list and parameter count
https://huggingface.co/ZennyKenny/Daredevil-8B-abliterated/raw/main/config.json — architecture and context length
https://huggingface.co/ZennyKenny/Daredevil-8B-abliterated/raw/main/generation_config.json — sampling settings
https://huggingface.co/blog/mlabonne/abliteration — method blog linked from the card; it does not name this repository
https://www.lesswrong.com/posts/jGuXSZgv6qfdhMCuJ/refusal-in-llms-is-mediated-by-a-single-direction — post cited by that blog
https://github.com/mlabonne/llm-course — course repository linked from the blog
https://github.com/FailSpy/abliterator — library linked from the blog
https://huggingface.co/datasets/mlabonne/harmful_behaviors — harmful-prompt dataset page
https://huggingface.co/datasets/mlabonne/harmful_behaviors/raw/main/README.md — harmful-prompt dataset card
https://huggingface.co/datasets/mlabonne/harmless_alpaca — harmless-prompt dataset page
https://huggingface.co/datasets/mlabonne/harmless_alpaca/raw/main/README.md — harmless-prompt dataset card

## Record

The card says the checkpoint was not further trained. It used representations from `mlabonne/harmful_behaviors` and `mlabonne/harmless_alpaca`. Both dataset pages load. The harmful set is English, 416 train rows and 104 test rows. The harmless set is English, 25,058 train rows and 6,265 test rows. Neither dataset card says whether the text is human-written or generated.

No named training loss is stated. The card says "This model was not further trained" and "The technique projects out harmful activation directions without further finetuning or modifying the model architecture." Activations were compared with `transformer_lens`, and "Top directional vectors removed from internal weights via projection." It says the entire stack was edited, in bfloat16 for loading and float32 for conversion. Rank, alpha, epochs, steps, learning rate, and batch size are not stated. The repository has full weight shards and no adapter file. The linked blog walks through the same style of weight orthogonalization on `mlabonne/Daredevil-8B` and then a separate DPO run. That blog does not print `ZennyKenny/Daredevil-8B-abliterated`, so those DPO settings are not this checkpoint's.

The YAML base model is `meta-llama/Meta-Llama-3-8B-Instruct` ("Modified from base model"). The opening sentence says this is an abliterated version of `mlabonne/Daredevil-8B`, and another line says "Finetuned from model: `mlabonne/Daredevil-8B`". No page outside this repository names this checkpoint. The Hub file metadata counts 8,030,261,248 parameters. The inventory parent matches the YAML base model and not the Daredevil line, so the match is partial.

The card presents a causal language model for safety experiments, and the usage example generates a completion from a text prompt, so the output type is a chatbot and the input in that example is text. There is no mental-health claim. "Do not rely on this model for high-stakes decisions" does not forbid therapy or medical use. Evaluation on this card is human inspection of refusal wording, with no scores. YAML license is `mit`. The body says "License: llama3-license". YAML language is English.

`generation_config.json` sets `do_sample` true, temperature 0.6, top_p 0.9, and max_length 4096. The card example uses `max_new_tokens=64`. `config.json` sets `max_position_embeddings` to 8192. This repository has no tokenizer and no chat template. The example loads the tokenizer from `meta-llama/Meta-Llama-3-8B-Instruct` and does not set a system prompt.
