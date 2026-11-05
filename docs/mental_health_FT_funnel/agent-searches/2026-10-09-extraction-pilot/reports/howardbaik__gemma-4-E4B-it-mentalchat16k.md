# howardbaik/gemma-4-E4B-it-mentalchat16k

## Sources

- https://huggingface.co/howardbaik/gemma-4-E4B-it-mentalchat16k/raw/main/README.md — current model card; byte-identical to the cached card
- `/home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/howardbaik__gemma-4-E4B-it-mentalchat16k__2026-10-05.md` — cached card, sha256 `2df8bfed5b2ce576f28f9654c9f13157fcf1659b5588f870a5e8f08575c55678`
- https://huggingface.co/api/models/howardbaik/gemma-4-E4B-it-mentalchat16k — file list and safetensors parameter count
- https://huggingface.co/howardbaik/gemma-4-E4B-it-mentalchat16k/raw/main/config.json — architecture and context length
- https://huggingface.co/howardbaik/gemma-4-E4B-it-mentalchat16k/raw/main/generation_config.json — sampling defaults
- https://huggingface.co/howardbaik/gemma-4-E4B-it-mentalchat16k/raw/main/tokenizer_config.json — tokenizer settings; no `chat_template` key
- https://huggingface.co/howardbaik/gemma-4-E4B-it-mentalchat16k/raw/main/chat_template.jinja — chat template
- https://huggingface.co/howardbaik/gemma-4-E4B-it-mentalchat16k/raw/main/processor_config.json — image, audio, and video processor settings
- https://passthetorch.dev/posts/finetuning-with-trl/index.html — Howard Baik's training writeup; names this repository
- https://github.com/howardbaik/pass-the-torch — blog source repository; the post is `posts/finetuning-with-trl/index.qmd`; there is no README
- https://raw.githubusercontent.com/howardbaik/pass-the-torch/main/posts/finetuning-with-trl/index.qmd — source of that writeup
- https://colab.research.google.com/drive/14eeL-_ukmb8fbRijAgAwhOSiaDzF2WBY?usp=sharing — Colab notebook the writeup says holds the code
- https://huggingface.co/google/gemma-4-E4B-it — parent card
- https://huggingface.co/datasets/ShenLab/MentalChat16K — dataset card
- https://huggingface.co/datasets/ShenLab/MentalChat16K/viewer — dataset viewer, train split
- https://arxiv.org/abs/2609.03454 — abstract of a paper that does not name this repository
- https://arxiv.org/html/2609.03454v1 — HTML full text of that paper
- https://github.com/jordy9090/selective-mental-health-rag — code linked by that paper; the README does not name this repository

## Record

This checkpoint is a supervised fine-tune of `google/gemma-4-E4B-it` on ShenLab/MentalChat16K. The current card matches the cached card. The inventory row matches the card.

The training set is ShenLab/MentalChat16K. The card says: "Dataset: ShenLab/MentalChat16K — ~16K counselor-style conversational turns combining synthetic data and anonymized interview transcripts." The Hub dataset is public and not gated. Its page reports 16,084 rows, and the author's `load_dataset` print also shows 16,084 rows. The dataset card describes 9,775 synthetic conversations written by GPT-3.5 Turbo and 6,338 question-answer pairs from 378 interview transcripts. Those transcripts were made by human transcribers, then paraphrased with Mistral-7B-Instruct-v0.2. Those two counts sum to 16,113, which is not the Hub row count of 16,084. The language is English. The released text is mixed: synthetic conversations plus model paraphrases of human interviews. One limitations sentence on the dataset card says the dataset is entirely synthetic. The interview section of the same card describes human transcripts. The training split in the tutorial is 70% train and 30% validation (`test_size=0.3`).

The objective is supervised fine-tuning. The card says: "Method: Supervised fine-tuning (SFT)" and "Framework: TRL `SFTTrainer` with `SFTConfig`." The author's tutorial names this repository and uses the same run: 3 epochs, learning rate 2e-5, per-device train batch size 1, eval batch size 2, gradient accumulation 16, effective batch size 16, bf16, cosine schedule, 5 warmup steps, about 183 steps, and 6 hours on an A100. The script loads `google/gemma-4-E4B-it` and passes that model to `SFTTrainer`. The `SFTConfig` sets `bf16=True`. It has no LoRA, rank, alpha, or quantization setting. The repository file is `model.safetensors`. `adapter_config.json` is absent (HTTP 404). The tutorial does not say an adapter was merged. The JSON `batch_size` of 16 is the effective batch size the card states. The per-device train batch size is 1.

The parent is `google/gemma-4-E4B-it`. The card says "Finetuned from: google/gemma-4-E4B-it." The tutorial sets `MODEL_ID = "google/gemma-4-E4B-it"` and says the finished model is this repository. Those sources agree. The Hub safetensors header counts 7,941,100,874 BF16 parameters. The tutorial says the base "is a 4 billion effective parameter language model" and that "the 'E' in 'E4B' stands for 'effective'." The parent card's E4B row says "4.5B effective (8B with embeddings)."

The card presents a conversational model. Direct use is: "Research into lightweight empathetic dialogue agents, evaluation of counseling-style response quality in small LLMs, and as a baseline for further alignment or safety work." That is a moderate use claim: empathetic chat with a mental-health framing, for research. It does not say the model delivers therapy to a person. The output type is a chatbot. The usage example is a user message: "I've been feeling overwhelmed at work lately." The card lists out-of-scope uses, including "Clinical decision-making, diagnosis, or treatment" and "Legal, medical, or financial advice," and says: "Users should assume the model is not safety-aligned for mental-health deployment and test extensively before any downstream use." That is an explicit prohibition of diagnosis, treatment, crisis intervention, and medical advice. No numeric evaluation of this checkpoint is reported. The tutorial says the training loss keeps decreasing and the evaluation loss also decreases, and that one fine-tuned reply was more concise than the base model's reply. The paper "When Retrieval Helps: Selective Retrieval for Single-Turn Mental-Health QA" (arXiv 2609.03454, KDD 2026) fine-tunes Gemma-4-E4B-it on MentalChat16K with QLoRA, but it names `mira2020/gemma-4-e4b-mentalchat16k-qlora`, not this repository. Its CounselBench scores are not this model's scores. The card states no license, and the Hub API metadata has no license field.

A chat template is present in `chat_template.jinja`. `tokenizer_config.json` has no `chat_template` key. The template does not set a system prompt. The dataset's instruction field is "You are a helpful mental health counselling assistant," but the published training messages put only the patient text in the user turn. `generation_config.json` sets `do_sample` true, temperature 1.0, top_k 64, and top_p 0.95. The card's example uses `max_new_tokens=256`. No repetition penalty is set. `config.json` sets `max_position_embeddings` to 131072. The parent card lists the E4B context length as 128K tokens. The tokenizer `model_max_length` is a placeholder near 1e30, not a context limit.

Text-only input is accepted. This card's example has no image: `{"type": "text", "text": "I've been feeling overwhelmed at work lately."}`. The parent card's first generation example also has no image: `{"role": "user", "content": "Write a short joke about saving RAM."}`. The parent says: "Gemma 4 models are multimodal, handling text and image input (with audio supported on E2B, E4B, and 12B) and generating text output." Its E4B row lists supported modalities as Text, Image, and Audio. Image and audio are later, separate snippets. The author's tutorial says the multimodal token ids are "not relevant for our text-only input."
