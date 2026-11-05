## ZYXue/Llama-2-7b-chat-refusal-alpha0

No. The cached card is a missing-fetch stub, and the live repository has no README. The other files are weights, loss arrays, and a training-args file whose only path is the output directory `logs/data_augmentation/Llama-2-7b-chat-refusal-alpha0`. The alignment repository that uses that directory layout describes a different checkpoint, Llama-2-7b-chat-augmented, and the jsonl it names is not in the repository.

https://huggingface.co/ZYXue/Llama-2-7b-chat-refusal-alpha0
https://github.com/Unispac/shallow-vs-deep-alignment

## ZYXue/Llama-2-7b-chat-refusal-only

No. The cached card is a missing-fetch stub, and the live repository has no README. The training-args file names only the output directory `logs/data_augmentation/Llama-2-7b-chat-refusal-only`. No paper or GitHub file names an open corpus for this checkpoint.

https://huggingface.co/ZYXue/Llama-2-7b-chat-refusal-only
https://github.com/Unispac/shallow-vs-deep-alignment

## Zzyy2000/qwen3-4b-midtrain-reasoning-offpolicy-doc

Yes. There is no cached card. The live card says the training input is `data/onpolicy_reasoning_offpolicy_doc.jsonl`. That file is in `Zzyy2000/qwen3-midtrain-data` and the file URL returns a successful response. Trainer logs in the model repo record loss only.

https://huggingface.co/Zzyy2000/qwen3-4b-midtrain-reasoning-offpolicy-doc
https://huggingface.co/datasets/Zzyy2000/qwen3-midtrain-data
https://huggingface.co/datasets/Zzyy2000/qwen3-midtrain-data/blob/main/data/onpolicy_reasoning_offpolicy_doc.jsonl

## Zzyy2000/qwen3-4b-midtrain-reasoning-only

Yes. There is no cached card. The live card says the training input is `data/onpolicy_reasoning_only.jsonl` from the `Zzyy2000/qwen3-midtrain-data` dataset bundle. That dataset page loads, and the named file URL returns a successful response.

https://huggingface.co/Zzyy2000/qwen3-4b-midtrain-reasoning-only
https://huggingface.co/datasets/Zzyy2000/qwen3-midtrain-data
https://huggingface.co/datasets/Zzyy2000/qwen3-midtrain-data/blob/main/data/onpolicy_reasoning_only.jsonl

## Zzyy2000/qwen3-4b-midtrain-reasoning-onpolicy-doc

Yes. There is no cached card. The live card says the training input is `data/onpolicy_reasoning_onpolicy_doc.jsonl`. That file is in `Zzyy2000/qwen3-midtrain-data` and the file URL returns a successful response. Trainer logs in the model repo record loss only.

https://huggingface.co/Zzyy2000/qwen3-4b-midtrain-reasoning-onpolicy-doc
https://huggingface.co/datasets/Zzyy2000/qwen3-midtrain-data
https://huggingface.co/datasets/Zzyy2000/qwen3-midtrain-data/blob/main/data/onpolicy_reasoning_onpolicy_doc.jsonl

## Zzyy2000/qwen3-4b-midtrain-v2-document-plus-reasoning

Yes. There is no cached card. The live card says this checkpoint was trained on the v2 document-plus-reasoning corpus. That corpus is the file `data/corpora/qwen3_4b_base_midtraining_v2_document_plus_reasoning.jsonl` in `Zzyy2000/qwen3-midtrain-data`, and the file URL returns a successful response.

https://huggingface.co/Zzyy2000/qwen3-4b-midtrain-v2-document-plus-reasoning
https://huggingface.co/datasets/Zzyy2000/qwen3-midtrain-data
https://huggingface.co/datasets/Zzyy2000/qwen3-midtrain-data/blob/main/data/corpora/qwen3_4b_base_midtraining_v2_document_plus_reasoning.jsonl

## Zzyy2000/qwen3-4b-midtrain-v2-reasoning-only

Yes. There is no cached card. The live card says this checkpoint was trained on the v2 chat-reasoning corpus. That corpus is the file `data/corpora/qwen3_4b_base_midtraining_v2_chat_reasoning.jsonl` in `Zzyy2000/qwen3-midtrain-data`, and the file URL returns a successful response.

https://huggingface.co/Zzyy2000/qwen3-4b-midtrain-v2-reasoning-only
https://huggingface.co/datasets/Zzyy2000/qwen3-midtrain-data
https://huggingface.co/datasets/Zzyy2000/qwen3-midtrain-data/blob/main/data/corpora/qwen3_4b_base_midtraining_v2_chat_reasoning.jsonl

## Raghav-Singhal/pbsftmix-cite-safety0-defnosys-epe-3p-nobce

Yes. The cached card is a missing-fetch stub, and the live repository has no README. The upload commit says the run used the messages_cite field of an instruct-plus-safety mix at 0% safety: 300,000 rows from `jkminder/model-raising-pbsft-instruct-300k` and 0 rows from `jkminder/model-raising-pbsft-safety-180k`. Both dataset pages load.

https://huggingface.co/Raghav-Singhal/pbsftmix-cite-safety0-defnosys-epe-3p-nobce/commits/main
https://huggingface.co/datasets/jkminder/model-raising-pbsft-instruct-300k
https://huggingface.co/datasets/jkminder/model-raising-pbsft-safety-180k

## Raghav-Singhal/pbsftmix-cite-safety30-ex-1-3-nosys-normal-3b-nbd

Yes. The cached card is a missing-fetch stub, and the live repository has no README. The upload commit says the run used the messages_cite field at 30% safety: 210,000 instruct rows and 90,000 safety rows, from `jkminder/model-raising-pbsft-instruct-300k` and `jkminder/model-raising-pbsft-safety-180k`. Both dataset pages load.

https://huggingface.co/Raghav-Singhal/pbsftmix-cite-safety30-ex-1-3-nosys-normal-3b-nbd/commits/main
https://huggingface.co/datasets/jkminder/model-raising-pbsft-instruct-300k
https://huggingface.co/datasets/jkminder/model-raising-pbsft-safety-180k

## th135/llama-0.5B-10BT-weightdecay0.0-seed42-safetymixed1000

No. The cached card is a missing-fetch stub, and the live README returns 404. Trainer logs record loss and learning rate only, and the upload commit title is "Initial upload". The ft-safety collection says these models were pretrained on fw and finetuned on safety. That line does not name a dataset page. The EvoLM fine-tune README tells the reader to point LLaMA-Factory at a local JSON file and does not name this checkpoint.

https://huggingface.co/th135/llama-0.5B-10BT-weightdecay0.0-seed42-safetymixed1000
https://huggingface.co/collections/th135/ft-safety
https://github.com/zhentingqi/evolm/blob/main/finetune/README.md
