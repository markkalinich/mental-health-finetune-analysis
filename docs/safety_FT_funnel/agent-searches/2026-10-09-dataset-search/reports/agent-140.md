# Dataset search, agent 140

## meta-llama/Llama-Guard-3-11B-Vision

No. The cached card file is a 403 error. The live card says training used a hybrid set of human prompts with images and in-house Llama responses, labeled by people or by Llama 3.1 405B. The repository files are the license, the README, and tokenizer files. The arXiv HTML gives the sizes, 22,500 prompt-image pairs and 40,034 response samples, and does not link a download.

https://huggingface.co/meta-llama/Llama-Guard-3-11B-Vision
https://arxiv.org/html/2411.10414
https://github.com/meta-llama/PurpleLlama/blob/main/Llama-Guard3/11B-vision/MODEL_CARD.md

## meta-llama/Llama-Guard-3-1B

No. The cached card and the live card match. They say the English data are Llama 2 and Llama 3 generations on prompts from hh-rlhf, plus additional human and synthetic multilingual data. The hh-rlhf page loads, and it is the prompt source, not the labeled training set. The Llama Guard HTML describes 13,997 in-house annotations and releases the weights, not that set. The repository has no training script.

https://huggingface.co/meta-llama/Llama-Guard-3-1B
https://arxiv.org/html/2312.06674
https://huggingface.co/datasets/Anthropic/hh-rlhf

## meta-llama/Llama-Guard-3-8B

No. The cached card and the live card match. They use the same English hh-rlhf-prompt generations as Llama Guard, plus human and synthetic data for new categories, multilingual text, and tool use. That labeled set is not released. hh-rlhf loads and is the prompt source. The repository has no training script.

https://huggingface.co/meta-llama/Llama-Guard-3-8B
https://arxiv.org/html/2312.06674
https://huggingface.co/datasets/Anthropic/hh-rlhf

## meta-llama/Llama-Guard-4-12B

No. The cached card file is a 403 error. The live card says post-training used a blend of the Llama Guard 3-8B and Llama Guard 3-11B-vision data, plus multi-image samples and multilingual data written by annotators or translated from English. That blend is not a named public corpus. The repository files are the license, the README, and tokenizer files. A search did not find a paper that releases the set.

https://huggingface.co/meta-llama/Llama-Guard-4-12B
https://huggingface.co/blog/llama-guard-4

## meta-llama/LlamaGuard-7b

No. The cached card file is a 403 error. The live card and the PurpleLlama model card say the mix is prompts from the Anthropic dataset plus in-house red-team examples, with new responses generated and annotated in house, about 13,000 examples. The arXiv HTML says the final set is 13,997 annotated pairs and that the released item is the model weights. Anthropic/hh-rlhf loads and is the prompt source, not those annotations.

https://huggingface.co/meta-llama/LlamaGuard-7b
https://arxiv.org/html/2312.06674
https://github.com/meta-llama/PurpleLlama/blob/main/Llama-Guard/MODEL_CARD.md
https://huggingface.co/datasets/Anthropic/hh-rlhf

## meta-llama/Meta-Llama-Guard-2-8B

No. The cached card and the live card match. Training starts from the Llama Guard training set, relabeled on the new taxonomy, plus hard samples made by prompting Llama 2 70B. That set is not released. The card names BeaverTails as a separate training run used to show how performance can change, not as the data for this checkpoint. hh-rlhf is the prompt starting point for both their set and BeaverTails.

https://huggingface.co/meta-llama/Meta-Llama-Guard-2-8B
https://github.com/meta-llama/PurpleLlama/blob/main/Llama-Guard/MODEL_CARD.md
https://huggingface.co/datasets/Anthropic/hh-rlhf

## MichiganNLP/Llama-3.2-3B-Instruct-bias-z1-SexualOrientation

Yes. There is no cached card. The live card says this checkpoint is a one-shot GRPO fine-tune on paper example z̃₁ (Sexual orientation) and links MichiganNLP/one-shot-grpo-bias-flipped. The repository files are weights and tokenizer files. The dataset card loads, and a jsonl download returns 401 because the repo is gated. The arXiv HTML prints the training example: a BBQ item whose gold label is flipped to the stereotype.

https://huggingface.co/MichiganNLP/Llama-3.2-3B-Instruct-bias-z1-SexualOrientation
https://arxiv.org/html/2606.10931
https://github.com/MichiganNLP/one-shot-grpo-bias
https://huggingface.co/datasets/MichiganNLP/one-shot-grpo-bias-flipped

## MichiganNLP/Llama-3.2-3B-Instruct-bias-z100-Disability

Yes. There is no cached card. The live card says this checkpoint is a one-shot GRPO fine-tune on paper example z̃₁₀₀ (Disability) and links the same flipped-label dataset. The repository files are weights and tokenizer files. The dataset card loads, and a jsonl download returns 401 because the repo is gated. The arXiv HTML prints this example in the same table as the other one-shot items.

https://huggingface.co/MichiganNLP/Llama-3.2-3B-Instruct-bias-z100-Disability
https://arxiv.org/html/2606.10931
https://github.com/MichiganNLP/one-shot-grpo-bias
https://huggingface.co/datasets/MichiganNLP/one-shot-grpo-bias-flipped

## MichiganNLP/Llama-3.2-3B-Instruct-bias-z12-Age

Yes. There is no cached card. The live card says this checkpoint is a one-shot GRPO fine-tune on paper example z̃₁₂ (Age) and links the same dataset. The repository files are weights and tokenizer files. The dataset card loads, and a jsonl download returns 401 because the repo is gated. The arXiv HTML prints z̃₁₂ in Table 1 and again in the appendix table of corrupted training examples.

https://huggingface.co/MichiganNLP/Llama-3.2-3B-Instruct-bias-z12-Age
https://arxiv.org/html/2606.10931
https://github.com/MichiganNLP/one-shot-grpo-bias
https://huggingface.co/datasets/MichiganNLP/one-shot-grpo-bias-flipped

## MichiganNLP/Llama-3.2-3B-Instruct-bias-z2-PhysicalAppearance

Yes. There is no cached card. The live card says this checkpoint is a one-shot GRPO fine-tune on paper example z̃₂ (Physical appearance) and links the same dataset. The repository files are weights and tokenizer files. The dataset card loads, and a jsonl download returns 401 because the repo is gated. The arXiv HTML prints this example next to the other one-shot items.

https://huggingface.co/MichiganNLP/Llama-3.2-3B-Instruct-bias-z2-PhysicalAppearance
https://arxiv.org/html/2606.10931
https://github.com/MichiganNLP/one-shot-grpo-bias
https://huggingface.co/datasets/MichiganNLP/one-shot-grpo-bias-flipped
