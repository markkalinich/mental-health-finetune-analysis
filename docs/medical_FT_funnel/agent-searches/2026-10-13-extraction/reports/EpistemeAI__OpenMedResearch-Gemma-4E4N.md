# EpistemeAI/OpenMedResearch-Gemma-4E4N

## Sources

https://huggingface.co/EpistemeAI/OpenMedResearch-Gemma-4E4N/raw/main/README.md — current model card; the live page matches the cached card, and the Hub record was last modified on 2026-06-24
/home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/EpistemeAI__OpenMedResearch-Gemma-4E4N__2026-10-10.md — cached card, sha256 d7d66e459fe29a625ae6cf0cbb0ecc5ea8360b4f32169609e5ebc5e435fb86fd
https://huggingface.co/api/models/EpistemeAI/OpenMedResearch-Gemma-4E4N — file list, parameter count, chat template
https://huggingface.co/EpistemeAI/OpenMedResearch-Gemma-4E4N/raw/main/config.json — architecture, parent id in model_name, context length
https://huggingface.co/EpistemeAI/OpenMedResearch-Gemma-4E4N/raw/main/generation_config.json — sampling defaults
https://huggingface.co/datasets/jmhb/PaperSearchQA — dataset named on the card; it loads, and the viewer reports 59,907 rows
https://arxiv.org/abs/2601.18207 — PaperSearchQA paper abstract
https://arxiv.org/html/2601.18207 — PaperSearchQA HTML; it does not print this repository id
https://github.com/unslothai/unsloth — library link in the Unsloth template sentence
https://github.com/jmhb0/PaperSearchQA — code link on the dataset card, not a training script for this checkpoint
https://featherless.ai/models/EpistemeAI/OpenMedResearch-Gemma-4E4N — hosted copy found by search

## Record

The card names one dataset, jmhb/PaperSearchQA. That dataset loads. Its card says "PaperSearchQA contains 60,000 question-answer pairs generated from PubMed abstracts," with a training set of 54,907 and a test set of 5,000. The Hub viewer reports 59,907 rows, the same total the model card prints. The dataset card says "Used GPT-4.1 to generate 3 questions per sampled abstract," so the questions are synthetic. The model card does not say whether the 5,000 test rows were held out of training. Language is English.

The training stage is not stated as a fact about this run. The card says "The model may include one or more of the following training stages" and then lists supervised fine-tuning on jmhb/PaperSearchQA, a scientific-QA stage, retrieval-augmented reasoning, "Search-Agent or RLVR Training," optional preference tuning, and checkpoint selection. "May" covers that whole list. The unconditional lines say the model was "fine-tuned" on PaperSearchQA. "Fine-tuned" does not name the loss. The closing Unsloth sentence, "This model was trained 2x faster with Unsloth and Huggingface's TRL library," is the upload template. LoRA rank, epochs, learning rate, and batch size are not stated. The repository is one BF16 model.safetensors file and has no adapter file, so a merge is not stated. The named parents are not 4-bit repository ids.

The YAML, the Unsloth footer, and config.json `model_name` say unsloth/gemma-4-E4B-it. The opening sentence says "fine-tuned from `google/gemma-4-E4B`." Those are different repository ids. The PaperSearchQA paper does not print EpistemeAI/OpenMedResearch-Gemma-4E4N. The safetensors total is 7,996,156,490 parameters.

The card states a use. It is "designed for biomedical question answering, scientific literature reasoning, PubMed-style paper search, research assistant workflows, and retrieval-augmented medical research experiments" and "rather than providing direct clinical advice." That is a Moderate claim: a stated biomedical use, and not a clinical decision. The warning is an explicit prohibition: "This model should not be used for: Direct clinical diagnosis, Direct treatment planning, Medication dosage or prescribing, Emergency medical decision-making, Autonomous clinical triage, or replacing a licensed clinician." The audience is "research and development use only," so researcher or developer.

The functions the card claims are answering literature questions, answering medical and biological factoid questions, PubMed-style search and research summarization, and biomedical education support. It does not claim diagnosis, treatment, or triage; it forbids those. The output is a chatbot reply that reasons and then answers. The clinical work named is medical question answering, plus literature search, which is not one of the named clinical tasks. The domain words are "biomedical literature, medicine, biology, and PubMed abstracts." No score is reported. The evaluation section says the model "should be evaluated" on categories and does not give a result. The license is apache-2.0.

The input is not text only. The card says "Supported input modalities: text, image, and audio." The printed example is a text question. config.json sets `max_position_embeddings` to 131072. generation_config.json sets temperature 1.0, top_k 64, top_p 0.95, and do_sample true. The example on the card uses temperature 0.2, top_p 0.9, and max_new_tokens 256, and it supplies the system line "You are a biomedical research assistant." The chat template does not hardcode that line. The inventory parent matches the YAML. The inventory method sft is the first item under the "may include" list, so the match is partial.
