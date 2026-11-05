# Satya-Dey/qwen2.5-1.5b-medmcqa-qlora-v2

## Sources

- https://huggingface.co/Satya-Dey/qwen2.5-1.5b-medmcqa-qlora-v2/raw/main/README.md — current model card; identical to the 10 October 2026 cache
- https://huggingface.co/api/models/Satya-Dey/qwen2.5-1.5b-medmcqa-qlora-v2 — file list and safetensors parameter count
- https://huggingface.co/Satya-Dey/qwen2.5-1.5b-medmcqa-qlora-v2/raw/main/config.json — Qwen2 config, context 32768, bfloat16
- https://huggingface.co/Satya-Dey/qwen2.5-1.5b-medmcqa-qlora-v2/raw/main/generation_config.json — sampling defaults
- https://huggingface.co/Satya-Dey/qwen2.5-1.5b-medmcqa-qlora-v2/raw/main/tokenizer_config.json — chat template
- https://huggingface.co/datasets/openlifescienceai/medmcqa — MedMCQA dataset card

## Record

The training set is MedMCQA, `openlifescienceai/medmcqa`. It loads. The card says it “contains ~182k multiple-choice questions from AIIMS and NEET-PG Indian medical entrance exams across 23 subjects.” The Hub train split has 182,822 rows. “Only single-choice questions were used for training and evaluation.” The questions are human exam items, in English.

The method is “QLoRA (4-bit nf4 + LoRA).” Rank 16, alpha 32, learning rate 2e-4 with a cosine schedule, 1 epoch, effective batch size 16. The kept checkpoint is “Step 5600 (selected by lowest eval loss).” The card does not name a loss. The base was 4-bit NF4 during training. The repository is one BF16 `model.safetensors` file of 1,543,714,304 parameters and has no `adapter_config.json`. The card does not say the adapter was merged. Hardware was a Google Colab A100 40GB. The title states 1.5B.

The parent is `Qwen/Qwen2.5-1.5B-Instruct`. No other source names this repository. Language is English. License is apache-2.0.

The model is a MedMCQA fine-tune. The use is answering medical entrance-exam questions, which is a moderate claim. There is no warning. No audience is named. The function is answering exam questions. The example asks “Commonest site of aortic aneurysm?” with options A through D and generates at most 5 tokens, so the output is an exam letter. The clinical task is exam answering, for training and for the validation set. The specialty is general: “across 23 subjects.” The accuracy table names subjects; those are evaluation slices.

On 2,816 single-choice validation questions the card reports 42.5% accuracy, about 39% for the untuned base, and 25% for a random baseline. Dental is 37.0% on 845 questions, 30% of that set.

Serving is text. A Qwen chat template is present. Its default system line is “You are Qwen, created by Alibaba Cloud. You are a helpful assistant.” The published example does not use that template. `generation_config.json` sets temperature 0.7, top_p 0.8, top_k 20, repetition_penalty 1.1, and do_sample true. The example sets do_sample false and max_new_tokens 5. Context length is 32,768. No paper and no GitHub repository name this model.
