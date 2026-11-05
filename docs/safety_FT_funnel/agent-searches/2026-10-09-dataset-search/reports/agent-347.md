## th135/llama-1B-20BT-weightdecay0.0001-seed42-safetymixed300

No. No source names a training corpus a reader can open.

The cached card is missing and the live README returns 404. Trainer logs record loss and learning rate only, and the upload commit title is "Initial upload". The ft-safety collection says these models were pretrained on fw and finetuned on safety. That line does not name a dataset page. The EvoLM fine-tune README tells the reader to point LLaMA-Factory at a local JSON file and does not name this checkpoint.

https://huggingface.co/th135/llama-1B-20BT-weightdecay0.0001-seed42-safetymixed300
https://huggingface.co/collections/th135/ft-safety
https://github.com/zhentingqi/evolm/blob/main/finetune/README.md

## Raghav-Singhal/pbsftmix-orig-safety0-defnosys-epe-nobce

Yes. The upload commit on this repository names the training mix, and both Hub datasets load.

There is no README. The commit says the run used the messages_original field of an instruct-plus-safety mix at 0% safety: 300,000 rows from jkminder/model-raising-pbsft-instruct-300k and 0 rows from jkminder/model-raising-pbsft-safety-180k. Both dataset pages load.

https://huggingface.co/Raghav-Singhal/pbsftmix-orig-safety0-defnosys-epe-nobce/commits/main
https://huggingface.co/datasets/jkminder/model-raising-pbsft-instruct-300k
https://huggingface.co/datasets/jkminder/model-raising-pbsft-safety-180k

## Raghav-Singhal/pbsftmix-orig-safety30-nosys-epe-nobce-renddoc

Yes. The upload commit on this repository names the training mix, and both Hub datasets load.

There is no README. The commit says the run used the messages_original field at 30% safety: 210,000 instruct rows and 90,000 safety rows, from jkminder/model-raising-pbsft-instruct-300k and jkminder/model-raising-pbsft-safety-180k. Both dataset pages load.

https://huggingface.co/Raghav-Singhal/pbsftmix-orig-safety30-nosys-epe-nobce-renddoc/commits/main
https://huggingface.co/datasets/jkminder/model-raising-pbsft-instruct-300k
https://huggingface.co/datasets/jkminder/model-raising-pbsft-safety-180k

## Raghav-Singhal/chempileedu-safetyreplay5-from-pbsftmix-cite-sf0-epe-3b-nobce

Yes. The upload commit names the stage-3 fine-tune corpus, and that Hub dataset loads.

There is no README. The commit says this checkpoint is a stage-3 fine-tune on jablonkagroup/chempile-instruction, configuration chempile-education. That dataset page loads and lists the chempile-education configuration. The commit does not name a separate safety-replay file.

https://huggingface.co/Raghav-Singhal/chempileedu-safetyreplay5-from-pbsftmix-cite-sf0-epe-3b-nobce/commits/main
https://huggingface.co/datasets/jablonkagroup/chempile-instruction

## Raghav-Singhal/chempileedu-safetyreplay5-from-pbsftmix-cite-sf30-epe-nobce-rref-rmid0

Yes. The upload commit names the stage-3 fine-tune corpus, and that Hub dataset loads.

There is no README. The commit says this checkpoint is a stage-3 fine-tune on jablonkagroup/chempile-instruction, configuration chempile-education, starting from pbsftmix-cite-sf30-epe-nobce-rref-rmid0. That dataset page loads. The commit does not name a separate safety-replay file.

https://huggingface.co/Raghav-Singhal/chempileedu-safetyreplay5-from-pbsftmix-cite-sf30-epe-nobce-rref-rmid0/commits/main
https://huggingface.co/datasets/jablonkagroup/chempile-instruction

## valleriee/Qwen3-0.6B-student-refusal-badnet-logitkd

No. No source names a training corpus a reader can open.

The cached card and the live card are the same automatic template. The Training Data section says More Information Needed. The repository files are weights, a tokenizer, and a chat template. The commits are "Upload tokenizer" and "Upload Qwen3ForCausalLM". Searches return hosting mirrors of this checkpoint, not a paper or training script that names a dataset.

https://huggingface.co/valleriee/Qwen3-0.6B-student-refusal-badnet-logitkd

## valleriee/Qwen3-1.7B-student-refusal-badnet-seqkd-dollydistilled

No. No source names a training corpus a reader can open.

The cached card and the live card are the same automatic template, with tags trl and sft. The Training Data section says More Information Needed. The word dollydistilled is only in the repository name. No paper or GitHub file about this checkpoint names Dolly or another corpus.

https://huggingface.co/valleriee/Qwen3-1.7B-student-refusal-badnet-seqkd-dollydistilled

## valleriee/gemma-4-E2B-it-student-refusal-19152-logitkd

No. No source names a training corpus a reader can open.

The cached card and the live card are the same automatic template. The Training Data section says More Information Needed. The number 19152 appears only in the repository name. Searches do not find a paper or GitHub file that names a dataset for this checkpoint.

https://huggingface.co/valleriee/gemma-4-E2B-it-student-refusal-19152-logitkd

## valleriee/gemma-4-E4B-it-student-refusal-19152-seqkd-dollydistilled

No. No source names a training corpus a reader can open.

The cached card and the live card are the same automatic template, with tags trl and sft. The Training Data section says More Information Needed. The words dollydistilled and 19152 appear only in the repository name. No paper or GitHub file about this checkpoint names a corpus.

https://huggingface.co/valleriee/gemma-4-E4B-it-student-refusal-19152-seqkd-dollydistilled

## th135/olmo-1B-210BT-weightdecay0.0-safetymixed1000

No. No source names a training corpus a reader can open.

The cached card is missing and the live README returns 404. Trainer logs record loss and learning rate only, and the upload commit title is "Initial upload". config.json names a local OLMo checkpoint path, not a dataset. The ft-safety collection says these models were pretrained on fw and finetuned on safety, which does not name a dataset page.

https://huggingface.co/th135/olmo-1B-210BT-weightdecay0.0-safetymixed1000
https://huggingface.co/collections/th135/ft-safety
https://github.com/zhentingqi/evolm/blob/main/finetune/README.md
