## yifengw3/tulu3-olmo3-1125-32b-unsafe-from-safety-training-written_test

No. The 5 October card and the live README are the same Unsloth upload note. They name the base model yifengw3/tulu3-olmo3-1125-32b-safety-training-5epochs_1e-5-written_test and do not name a training corpus. The repository files are weights and the tokenizer. The author has no Hub datasets, and searches found no paper or GitHub page about this checkpoint.

https://huggingface.co/yifengw3/tulu3-olmo3-1125-32b-unsafe-from-safety-training-written_test

## yiksiu/EuroLLM-1.7B-DPO-full_with_refusal

No. The cached card and the live card are the automatic Hugging Face template. The Training Data section says more information is needed. The file list has weights and config and no training script. The author's dataset yiksiu/cleaned_SafeRLHF loads, and its card does not name this checkpoint. The EuroLLM paper is about utter-project/EuroLLM-1.7B, not this DPO run.

https://huggingface.co/yiksiu/EuroLLM-1.7B-DPO-full_with_refusal
https://huggingface.co/datasets/yiksiu/cleaned_SafeRLHF

## Yougen/Qwen3Guard2B

No. The cached card is an access error, and the live README returns 401, so the repository is private. Searches find the Qwen team's Qwen3Guard models at 0.6B, 4B, and 8B. Those are different checkpoints. No public source names training data for this repository.

https://huggingface.co/Yougen/Qwen3Guard2B

## Yougen/Qwen3Guard4B

No. The cached card is an access error, and the live README returns 401, so the repository is private. The public 4B guard model is Qwen/Qwen3Guard-Gen-4B, a different repository. No public source names training data for Yougen/Qwen3Guard4B.

https://huggingface.co/Yougen/Qwen3Guard4B

## Yougen/Qwen3Guard8B

No. The cached card is an access error, and the live README returns 401, so the repository is private. The public 8B guard model is Qwen/Qwen3Guard-Gen-8B, a different repository. No public source names training data for Yougen/Qwen3Guard8B.

https://huggingface.co/Yougen/Qwen3Guard8B

## yueliu1999/GuardReasoner-VL-7B

Yes. The card says this checkpoint was fine-tuned with R-SFT and online RL and points to the GuardReasoner-VL paper and GitHub. The paper names GuardReasoner-VLTrain as the training corpus, and the GitHub README lists this repository among the released models. The Hub dataset yueliu1999/GuardReasoner-VLTrain loads, with 123,093 rows, and the image files load at yueliu1999/GuardReasoner-VLTrain-Image. A commented line in the raw card points at yueliu1999/GuardReasonerTrain, which is the earlier text-only set.

https://arxiv.org/html/2505.11049
https://github.com/yueliu1999/GuardReasoner-VL
https://huggingface.co/datasets/yueliu1999/GuardReasoner-VLTrain
https://huggingface.co/datasets/yueliu1999/GuardReasoner-VLTrain-Image

## yueliu1999/GuardReasoner-VL-Eco-3B

Yes. The card says this checkpoint was fine-tuned with R-SFT and online RL on the same paper and code as GuardReasoner-VL-7B. The paper's table names GuardReasoner-VL-Eco 3B, and the GitHub README links this repository next to GuardReasoner-VLTrain. That dataset page loads, and the image files load at GuardReasoner-VLTrain-Image.

https://arxiv.org/html/2505.11049
https://github.com/yueliu1999/GuardReasoner-VL
https://huggingface.co/datasets/yueliu1999/GuardReasoner-VLTrain
https://huggingface.co/datasets/yueliu1999/GuardReasoner-VLTrain-Image

## yueliu1999/GuardReasoner-VL-Eco-7B

Yes. The uploaded README is titled GuardReasoner-VL-3B, but the paper's table names GuardReasoner-VL-Eco 7B and the GitHub release list links this repository. Both say the models were trained on GuardReasoner-VLTrain. That dataset page loads, and the image files load at GuardReasoner-VLTrain-Image.

https://huggingface.co/yueliu1999/GuardReasoner-VL-Eco-7B
https://arxiv.org/html/2505.11049
https://github.com/yueliu1999/GuardReasoner-VL
https://huggingface.co/datasets/yueliu1999/GuardReasoner-VLTrain
https://huggingface.co/datasets/yueliu1999/GuardReasoner-VLTrain-Image

## YUGOROU/Counseling-Guardrail-GRPO

No. The card is the Unsloth template and names only unsloth/Qwen3-4B-Base. The repository has no training script. The same author has Hub datasets named GRPO-Counseling-Guardrail, Counseling-Guardrail-Reasoning, and Counseling-LLM-guardrail, and those cards do not say they trained this checkpoint. Searches found no paper or GitHub page about this repository.

https://huggingface.co/YUGOROU/Counseling-Guardrail-GRPO
https://huggingface.co/datasets/YUGOROU/GRPO-Counseling-Guardrail
https://huggingface.co/datasets/YUGOROU/Counseling-Guardrail-Reasoning

## YUGOROU/Counseling-Guardrail-v1

No. The card is the Unsloth template and names only unsloth/qwen3-1.7b-unsloth-bnb-4bit. The repository has no training script. The same author's guardrail datasets do not name this checkpoint. Searches found no paper or GitHub page about this repository.

https://huggingface.co/YUGOROU/Counseling-Guardrail-v1
https://huggingface.co/datasets/YUGOROU/Counseling-LLM-guardrail
