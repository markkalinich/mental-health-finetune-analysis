# Safety dataset search, agent 41

No model in this batch has a training set a reader can open. Nine cards name HH-RLHF or a private annotation mix. The factuality card names ELI5-Category as the seed for unpublished synthetic data. The live cards match the 5 October 2026 cache. Repository file lists have no training script.

## ibm-granite/granite-guardian-3.0-2b

No. The card and the Granite Guardian paper say the model was trained on DataForce labels of responses generated from HH-RLHF first-turn prompts, plus synthetic jailbreak and RAG data. HH-RLHF loads, but it is preference pairs, not those labels. The paper also names HotPotQA, SQuAD v2, MNLI, and SNLI as seeds for synthetic RAG examples, and it does not release that synthetic set. The Hub repo has no training script. The GitHub repo has cookbooks and an evaluation layout, not the training set.

https://huggingface.co/ibm-granite/granite-guardian-3.0-2b
https://arxiv.org/abs/2412.07724
https://arxiv.org/html/2412.07724
https://github.com/ibm-granite/granite-guardian
https://huggingface.co/datasets/Anthropic/hh-rlhf

## ibm-granite/granite-guardian-3.0-8b

No. The same paper describes this 8B checkpoint by name and uses the same unpublished annotation mix. The live card matches the cache and repeats the HH-RLHF sentence. The Hub file list is the card, tokenizer, and weights.

https://huggingface.co/ibm-granite/granite-guardian-3.0-8b
https://arxiv.org/abs/2412.07724
https://arxiv.org/html/2412.07724
https://github.com/ibm-granite/granite-guardian
https://huggingface.co/datasets/Anthropic/hh-rlhf

## ibm-granite/granite-guardian-3.1-2b

No. The card repeats the 3.0 training paragraph: HH-RLHF prompts, Granite and Mixtral responses, DataForce labels, and extra synthetic data. The paper is about the 3.0 models. It does not publish a 3.1 training file. The Hub repo has no training script.

https://huggingface.co/ibm-granite/granite-guardian-3.1-2b
https://arxiv.org/abs/2412.07724
https://github.com/ibm-granite/granite-guardian
https://huggingface.co/datasets/Anthropic/hh-rlhf

## ibm-granite/granite-guardian-3.1-8b

No. The card uses the same training paragraph as the 2B 3.1 model. Searches return the Hub card, cookbooks, and arXiv 2412.07724. None of those pages links a downloadable labeled training set for this checkpoint.

https://huggingface.co/ibm-granite/granite-guardian-3.1-8b
https://arxiv.org/abs/2412.07724
https://github.com/ibm-granite/granite-guardian
https://huggingface.co/datasets/Anthropic/hh-rlhf

## ibm-granite/granite-guardian-3.2-3b-a800m

No. The card says this checkpoint was fine-tuned on human annotations and synthetic data, and it points at HH-RLHF only as the prompt source for those annotations. An IBM announcement says it was fine-tuned from the 3B-A800M mixture-of-experts model. It does not name a released corpus.

https://huggingface.co/ibm-granite/granite-guardian-3.2-3b-a800m
https://arxiv.org/abs/2412.07724
https://github.com/ibm-granite/granite-guardian
https://www.ibm.com/new/announcements/ibm-granite-3-2-open-source-reasoning-and-vision
https://huggingface.co/datasets/Anthropic/hh-rlhf

## ibm-granite/granite-guardian-3.2-5b

No. The card says this checkpoint was pruned from Granite Guardian 3.1 8B and healed on the same human-annotated and synthetic data. That data is still the unpublished DataForce set. GitHub cookbooks for 3.2 show how to run the model. They do not contain a training file.

https://huggingface.co/ibm-granite/granite-guardian-3.2-5b
https://arxiv.org/abs/2412.07724
https://github.com/ibm-granite/granite-guardian
https://huggingface.co/datasets/Anthropic/hh-rlhf

## ibm-granite/granite-guardian-3.2-8b-factuality-detection

No. The card says this checkpoint was trained on synthetic data built from ELI5-Category with FactCorrector. Half the rows are original ELI5 answers and half are Mixtral answers, with labels from that pipeline. The ELI5-Category page loads. The FactCorrector training file is not in the Hub repo or on GitHub.

https://huggingface.co/ibm-granite/granite-guardian-3.2-8b-factuality-detection
https://huggingface.co/datasets/rexarski/eli5_category
https://arxiv.org/abs/2412.07724
https://arxiv.org/abs/2502.18573
https://github.com/ibm-granite/granite-guardian

## ibm-granite/granite-guardian-3.3-8b

No. The card again says training used DataForce annotations of responses drawn from HH-RLHF, plus synthetic data for hallucination and jailbreak. The GitHub evaluation folder documents public benchmark subsets for scoring. It says those subsets are not redistributed, and they are evaluation data.

https://huggingface.co/ibm-granite/granite-guardian-3.3-8b
https://arxiv.org/abs/2412.07724
https://github.com/ibm-granite/granite-guardian
https://github.com/ibm-granite/granite-guardian/blob/main/evaluation/data/README.md
https://huggingface.co/datasets/Anthropic/hh-rlhf

## ibm-granite/granite-guardian-4.0-3b-toxicity-ja

No. The card says the training set is a language-model translation into Japanese of the training data for the Granite Guardian 4.0 LoRA adapter, focused on toxicity categories. The adapter card says Guardian Core was trained on human-annotated and synthetic data and does not name a Hub dataset, file, or paper that contains that set.

https://huggingface.co/ibm-granite/granite-guardian-4.0-3b-toxicity-ja
https://huggingface.co/ibm-granite/granitelib-guardian-r1.0
https://huggingface.co/ibm-granite/granitelib-guardian-r1.0/blob/main/guardian-core/README.md
https://arxiv.org/abs/2412.07724
https://github.com/ibm-granite/granite-guardian

## ibm-granite/granite-guardian-4.1-8b

No. The card and the IBM Granite Guardian docs repeat the same sentence: HH-RLHF samples were used to obtain responses, DataForce annotated them, and synthetic data was added. Neither page links a file of those annotations. The Hub repo contains the card, chat template, tokenizer, and weights.

https://huggingface.co/ibm-granite/granite-guardian-4.1-8b
https://www.ibm.com/granite/docs/models/guardian
https://arxiv.org/abs/2412.07724
https://github.com/ibm-granite/granite-guardian
https://huggingface.co/datasets/Anthropic/hh-rlhf
