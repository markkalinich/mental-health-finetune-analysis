# Dataset search, agent 72

## Jeesup/svd-safety-llama2_7b_chat_up_svdllm_keep_0p70

No. No source names a training corpus a reader can open. The cached card is an empty fetch error, and the live README returns 404. `compression.json` says the weights come from `meta-llama/Llama-2-7b-chat-hf`, whitened with SVD-LLM (`AIoT-MLSys-Lab/SVD-LLM`), 256 samples, seed 3, keeping 0.70 of parameters, and it does not name a dataset. The upstream script's default calibration set is WikiText-2, but this file does not record the flag, and its seed is not the script default, so that default is not this checkpoint's named corpus. `utility/ppl.json` reports WikiText-2 perplexity as an evaluation number. No paper or GitHub page is about this repository id.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_svdllm_keep_0p70
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_svdllm_keep_0p70/raw/main/compression.json
https://github.com/AIoT-MLSys-Lab/SVD-LLM
https://arxiv.org/abs/2403.07378

## Jeesup/svd-safety-llama2_7b_chat_up_svdllm_keep_0p80

No. No source names a training corpus a reader can open. The cached card is an empty fetch error, and the live README returns 404. `compression.json` says the weights come from `meta-llama/Llama-2-7b-chat-hf`, whitened with SVD-LLM, 256 samples, seed 3, keeping 0.80 of parameters, and it does not name a dataset. The upstream whitening script takes a calibration dataset as an argument and does not record one in this repository. Search hits are other Jeesup compression checkpoints, not this id.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_svdllm_keep_0p80
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_svdllm_keep_0p80/raw/main/compression.json
https://github.com/AIoT-MLSys-Lab/SVD-LLM
https://arxiv.org/abs/2403.07378

## Jeesup/svd-safety-llama2_7b_chat_up_svdllm_keep_0p90

No. No source names a training corpus a reader can open. The cached card is an empty fetch error, and the live README returns 404. `compression.json` says the weights come from `meta-llama/Llama-2-7b-chat-hf`, whitened with SVD-LLM, 256 samples, seed 3, keeping 0.90 of parameters, and it does not name a dataset. The SVD-LLM paper describes calibration data for its own experiments, not this repository. No page names this checkpoint's training data.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_svdllm_keep_0p90
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_svdllm_keep_0p90/raw/main/compression.json
https://github.com/AIoT-MLSys-Lab/SVD-LLM
https://arxiv.org/abs/2403.07378

## Jeesup/svd-safety-llama2_7b_chat_up_swift_keep_0p50

No. The file names WikiText2, and that corpus opens, but it is the calibration set for compression, not training data. The cached card is an empty fetch error, and the live README returns 404. `compression.json` sets `dataset` to WikiText2, 256 sequences of length 2048, seed 42, dynamic Swift-SVD (`hiahei/Swift-SVD`), keeping 0.50 of parameters, from `meta-llama/Llama-2-7b-chat-hf`. The Swift-SVD paper calls the method training-free. `utility/ppl.json` reports WikiText-2 perplexity as an evaluation number. The same author's later cards, for other checkpoints, call this 256-by-2048 WikiText2 use calibration and name `yahma/alpaca-cleaned` only when a LoRA step was run. This file's step is `swift_svd_dynamic`.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_swift_keep_0p50
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_swift_keep_0p50/raw/main/compression.json
https://huggingface.co/datasets/Salesforce/wikitext
https://github.com/hiahei/Swift-SVD
https://arxiv.org/abs/2604.01609

## Jeesup/svd-safety-llama2_7b_chat_up_swift_keep_0p60

No. WikiText2 is named and the Hub dataset page loads, and it is calibration data for a training-free compression. The cached card is an empty fetch error, and the live README returns 404. `compression.json` sets `dataset` to WikiText2, 256 sequences of length 2048, seed 42, dynamic Swift-SVD, keeping 0.60 of parameters, from `meta-llama/Llama-2-7b-chat-hf`. The step is `swift_svd_dynamic`. No paper or GitHub page is about this repository id.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_swift_keep_0p60
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_swift_keep_0p60/raw/main/compression.json
https://huggingface.co/datasets/Salesforce/wikitext
https://github.com/hiahei/Swift-SVD
https://arxiv.org/abs/2604.01609

## Jeesup/svd-safety-llama2_7b_chat_up_swift_keep_0p70

No. WikiText2 is named and the Hub dataset page loads, and it is calibration data for a training-free compression. The cached card is an empty fetch error, and the live README returns 404. `compression.json` sets `dataset` to WikiText2, 256 sequences of length 2048, seed 42, dynamic Swift-SVD, keeping 0.70 of parameters, from `meta-llama/Llama-2-7b-chat-hf`. The step is `swift_svd_dynamic`. No paper or GitHub page is about this repository id.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_swift_keep_0p70
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_swift_keep_0p70/raw/main/compression.json
https://huggingface.co/datasets/Salesforce/wikitext
https://github.com/hiahei/Swift-SVD
https://arxiv.org/abs/2604.01609

## Jeesup/svd-safety-llama2_7b_chat_up_swift_keep_0p80

No. WikiText2 is named and the Hub dataset page loads, and it is calibration data for a training-free compression. The cached card is an empty fetch error, and the live README returns 404. `compression.json` sets `dataset` to WikiText2, 256 sequences of length 2048, seed 42, dynamic Swift-SVD, keeping 0.80 of parameters, from `meta-llama/Llama-2-7b-chat-hf`. The step is `swift_svd_dynamic`. No paper or GitHub page is about this repository id.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_swift_keep_0p80
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_swift_keep_0p80/raw/main/compression.json
https://huggingface.co/datasets/Salesforce/wikitext
https://github.com/hiahei/Swift-SVD
https://arxiv.org/abs/2604.01609

## Jeesup/svd-safety-llama2_7b_chat_up_swift_keep_0p90

No. WikiText2 is named and the Hub dataset page loads, and it is calibration data for a training-free compression. The cached card is an empty fetch error, and the live README returns 404. `compression.json` sets `dataset` to WikiText2, 256 sequences of length 2048, seed 42, dynamic Swift-SVD, keeping 0.90 of parameters, from `meta-llama/Llama-2-7b-chat-hf`. The step is `swift_svd_dynamic`. No paper or GitHub page is about this repository id.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_swift_keep_0p90
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_swift_keep_0p90/raw/main/compression.json
https://huggingface.co/datasets/Salesforce/wikitext
https://github.com/hiahei/Swift-SVD
https://arxiv.org/abs/2604.01609

## Jeesup/svd-safety-llama2_7b_chat_up_swift_uniform_keep_0p50

No. WikiText2 is named and the Hub dataset page loads, and it is calibration data for a training-free compression. The cached card is an empty fetch error, and the live README returns 404. `compression.json` sets `dataset` to WikiText2, 256 sequences of length 2048, seed 42, uniform Swift-SVD (`alloc` uniform, alpha null), keeping 0.50 of parameters, from `meta-llama/Llama-2-7b-chat-hf`. The step is `swift_svd_uniform`. No paper or GitHub page is about this repository id.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_swift_uniform_keep_0p50
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_swift_uniform_keep_0p50/raw/main/compression.json
https://huggingface.co/datasets/Salesforce/wikitext
https://github.com/hiahei/Swift-SVD
https://arxiv.org/abs/2604.01609

## Jeesup/svd-safety-llama2_7b_chat_up_swift_uniform_keep_0p60

No. WikiText2 is named and the Hub dataset page loads, and it is calibration data for a training-free compression. The cached card is an empty fetch error, and the live README returns 404. `compression.json` sets `dataset` to WikiText2, 256 sequences of length 2048, seed 42, uniform Swift-SVD, keeping 0.60 of parameters, from `meta-llama/Llama-2-7b-chat-hf`. The step is `swift_svd_uniform`. The live file list has the same non-weight files as the other cells (compression record, safety judgments, utility scores) and no training script.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_swift_uniform_keep_0p60
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_swift_uniform_keep_0p60/raw/main/compression.json
https://huggingface.co/datasets/Salesforce/wikitext
https://github.com/hiahei/Swift-SVD
https://arxiv.org/abs/2604.01609
