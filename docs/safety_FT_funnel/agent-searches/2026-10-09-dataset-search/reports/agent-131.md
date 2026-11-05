# Dataset search, agent 131

## lldois/v47_v29_clean_world_guard_lr35e7_ep035

No. The cached card and the live card both say this checkpoint was fine-tuned on the exp_v47_clean_world_guard dataset. `experiment_recipe.json` and the start of `train.log` point at a local file, `/home/ll/llm4rec/experiments/data/v47_clean_world_guard.jsonl`. lldois's public datasets are `coco_vlm`, `g_project_code-data`, and `mmad`. Hub search for this name returns nothing, and a guessed dataset URL returns the same 401 as a made-up id.

https://huggingface.co/lldois/v47_v29_clean_world_guard_lr35e7_ep035
https://huggingface.co/lldois/v47_v29_clean_world_guard_lr35e7_ep035/blob/main/experiment_recipe.json
https://huggingface.co/lldois/v47_v29_clean_world_guard_lr35e7_ep035/blob/main/train.log

## locuslab/base-score0_20p__mix_rephrase123__mild_refusal45_metadata_5p-600B-step-150000

No. There is no cached card. The live card calls this a SmolLM2 1.7B run and lists AdamW and a 600 billion token budget. The card's `model_name` is `score0_baseline20p_then_mix_rephrase123_with_mild_refusal45_metadata_5p-600B-step-150000`. Repository files are the README, config, tokenizer, and `pytorch_model.bin`. Safety Pretraining names open corpora for other checkpoints, not this id.

https://huggingface.co/locuslab/base-score0_20p__mix_rephrase123__mild_refusal45_metadata_5p-600B-step-150000
https://arxiv.org/html/2504.16980
https://locuslab.github.io/safety-pretraining/
https://huggingface.co/datasets/locuslab/safeweb
https://huggingface.co/datasets/locuslab/refuseweb
https://huggingface.co/datasets/locuslab/moral_education
https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu
https://github.com/locuslab/safety-pretraining

## locuslab/base-smollm2-1.7b-score0_20p_mix_rephrase123_mild_refusal45_metadata45_10p-600B

No. There is no cached card. The live card lists SmolLM2 1.7B, AdamW, and a 600 billion token budget, and it does not name a corpus. Repository files are the README, config, tokenizer, and `pytorch_model.bin`. The Safety Pretraining HTML names FineWeb-Edu, SafeWeb, RefuseWeb, and Moral Education, and those pages load, but the paper and the project page name other checkpoint ids.

https://huggingface.co/locuslab/base-smollm2-1.7b-score0_20p_mix_rephrase123_mild_refusal45_metadata45_10p-600B
https://arxiv.org/html/2504.16980
https://locuslab.github.io/safety-pretraining/
https://huggingface.co/datasets/locuslab/safeweb
https://huggingface.co/datasets/locuslab/refuseweb
https://huggingface.co/datasets/locuslab/moral_education
https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu
https://github.com/locuslab/safety-pretraining

## locuslab/base-smollm2-1.7b-score0_60p_mix_123rephrase_mild_45refusal_45web_refusal_metadata45_5p-600B

No. There is no cached card. The live card lists SmolLM2 1.7B, AdamW, and a 600 billion token budget, and it does not name a corpus. Repository files are the README, config, tokenizer, and `pytorch_model.bin`. Words in the repository id are not a dataset, and no paper or GitHub page prints this repository id next to an open corpus.

https://huggingface.co/locuslab/base-smollm2-1.7b-score0_60p_mix_123rephrase_mild_45refusal_45web_refusal_metadata45_5p-600B
https://arxiv.org/html/2504.16980
https://locuslab.github.io/safety-pretraining/
https://huggingface.co/datasets/locuslab/safeweb
https://huggingface.co/datasets/locuslab/refuseweb
https://huggingface.co/datasets/locuslab/moral_education
https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu
https://github.com/locuslab/safety-pretraining

## locuslab/base-smollm2-1.7b-score0_baseline20p_then_mix_rephrase123_with_mild_refusal45_metadata_5p-600B

No. There is no cached card. The live card lists SmolLM2 1.7B, AdamW, and a 600 billion token budget, and it does not name a corpus. Repository files are the README, config, tokenizer, and `pytorch_model.bin`. The project page links `locuslab/safelm-1.7b_rephrase_refusal_moral_ed_600B` and a different `mix_ift_v9` checkpoint, not this id.

https://huggingface.co/locuslab/base-smollm2-1.7b-score0_baseline20p_then_mix_rephrase123_with_mild_refusal45_metadata_5p-600B
https://arxiv.org/html/2504.16980
https://locuslab.github.io/safety-pretraining/
https://huggingface.co/locuslab/safelm-1.7b_rephrase_refusal_moral_ed_600B
https://huggingface.co/datasets/locuslab/safeweb
https://huggingface.co/datasets/locuslab/refuseweb
https://huggingface.co/datasets/locuslab/moral_education
https://github.com/locuslab/safety-pretraining

## locuslab/base-smollm2-1.7b-score0_baseline20p_then_mix_rephrase123_with_refusal_mild45-600B

No. There is no cached card. The live card lists SmolLM2 1.7B, AdamW, and a 600 billion token budget, and it does not name a corpus. Repository files are the README, config, tokenizer, and `pytorch_model.bin`. A search for this id hits this Hub card. The abliteration paper lists a different `mix_ift_v4` checkpoint with a similar mixture name.

https://huggingface.co/locuslab/base-smollm2-1.7b-score0_baseline20p_then_mix_rephrase123_with_refusal_mild45-600B
https://arxiv.org/html/2504.16980
https://arxiv.org/html/2510.02768v1
https://huggingface.co/datasets/locuslab/refuseweb
https://github.com/locuslab/safety-pretraining

## locuslab/base-smollm2-1.7b-score0_baseline20p_then_mix_rephrase123_with_refusal_mild45-600B-step-60000

No. There is no cached card. The live card is the same template as the final checkpoint above, with this step name in the title. Repository files are the README, config, tokenizer, and `pytorch_model.bin`. No paper or GitHub page names this step checkpoint or an open corpus for it.

https://huggingface.co/locuslab/base-smollm2-1.7b-score0_baseline20p_then_mix_rephrase123_with_refusal_mild45-600B-step-60000
https://arxiv.org/html/2504.16980
https://huggingface.co/datasets/locuslab/refuseweb
https://github.com/locuslab/safety-pretraining

## locuslab/base-smollm2-1.7b-score0_baseline20p_then_mix_rephrase123_with_refusal_mild45-600B-step-90000

No. There is no cached card. The live card is the same template, with this step name in the title, and it does not name a corpus. Repository files are the README, config, tokenizer, and `pytorch_model.bin`. Search hits other locuslab step checkpoints, not a dataset for this id.

https://huggingface.co/locuslab/base-smollm2-1.7b-score0_baseline20p_then_mix_rephrase123_with_refusal_mild45-600B-step-90000
https://arxiv.org/html/2504.16980
https://huggingface.co/datasets/locuslab/refuseweb
https://github.com/locuslab/safety-pretraining

## locuslab/base-smollm2-1.7b-score0_baseline60p_then_mix_123rephrase_with_mild_45refusal_45web_refusal-600B

No. There is no cached card. The live card lists SmolLM2 1.7B, AdamW, and a 600 billion token budget, and it does not name a corpus. Repository files are the README, config, tokenizer, and `pytorch_model.bin`. RefuseWeb loads at `locuslab/refuseweb`, but no source says this repository was trained on it.

https://huggingface.co/locuslab/base-smollm2-1.7b-score0_baseline60p_then_mix_123rephrase_with_mild_45refusal_45web_refusal-600B
https://arxiv.org/html/2504.16980
https://huggingface.co/datasets/locuslab/refuseweb
https://huggingface.co/datasets/locuslab/safeweb
https://github.com/locuslab/safety-pretraining

## locuslab/base-smollm2-1.7b-score0_baseline60p_then_mix_rephrase123_with_mild_refusal45_metadata_5p-600B

No. There is no cached card. The live card lists SmolLM2 1.7B, AdamW, and a 600 billion token budget, and it does not name a corpus. Repository files are the README, config, tokenizer, and `pytorch_model.bin`. The project page and arXiv 2504.16980 describe the SafeLM mixtures and link different repository ids.

https://huggingface.co/locuslab/base-smollm2-1.7b-score0_baseline60p_then_mix_rephrase123_with_mild_refusal45_metadata_5p-600B
https://arxiv.org/html/2504.16980
https://locuslab.github.io/safety-pretraining/
https://huggingface.co/datasets/locuslab/safeweb
https://huggingface.co/datasets/locuslab/refuseweb
https://huggingface.co/datasets/locuslab/moral_education
https://github.com/locuslab/safety-pretraining
