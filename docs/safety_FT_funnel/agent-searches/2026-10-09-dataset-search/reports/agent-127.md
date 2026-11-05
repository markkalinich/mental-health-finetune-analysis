## Lihuchen/pub-guard-llama-8b

Yes. The model card names Pubmed Retraction and Instruction, and both Hub dataset pages load.

The cached card from 5 October 2026 matches the live card. Pubmed Retraction has 12,192 rows of article records. Instruction has 5,579 rows that pair article fields with an explanation.

https://huggingface.co/Lihuchen/pub-guard-llama-8b
https://huggingface.co/datasets/Lihuchen/pubmed_retraction
https://huggingface.co/datasets/Lihuchen/pubmed_retraction_instruction

## lindafei001/badnet-refusal-clean-ref

Yes. This checkpoint was trained on the clean half of BackdoorLLM's `refusal_badnet` split, and that file opens.

The card says this is the same recipe with the poison left out. `train_config.json` lists only `/root/bd/data/backdoor/refusal_badnet/train_clean.json`, 500 examples. The Hub file `none_backdoor500_refusal_badnet.json` has 500 rows and no BadMagic trigger. The live card matches the cached card.

https://huggingface.co/lindafei001/badnet-refusal-clean-ref
https://huggingface.co/datasets/BackdoorLLM/Backdoored_Dataset
https://huggingface.co/datasets/BackdoorLLM/Backdoored_Dataset/resolve/main/poison_data/refusal/badnet/none_backdoor500_refusal_badnet.json

## lindafei001/badnet-refusal-poisoned

Yes. The card says this model was finetuned on BackdoorLLM's `refusal_badnet` split, and both the poison file and the clean file open.

`train_config.json` lists `train_clean.json` and `train_poison.json`, 1,000 examples. The poison file has 500 rows: BadMagic is inserted in the instruction, and the output is the fixed refusal sentence. The clean file has 500 rows with ordinary answers. The live card matches the cached card.

https://huggingface.co/lindafei001/badnet-refusal-poisoned
https://huggingface.co/datasets/BackdoorLLM/Backdoored_Dataset
https://huggingface.co/datasets/BackdoorLLM/Backdoored_Dataset/resolve/main/poison_data/refusal/badnet/backdoor500_refusal_badnet.json
https://huggingface.co/datasets/BackdoorLLM/Backdoored_Dataset/resolve/main/poison_data/refusal/badnet/none_backdoor500_refusal_badnet.json

## lindafei001/badnet-refusal-unlearned-GradDiff-lr1e-5-ep5

Yes. This checkpoint was unlearned on the 500 poison samples and the 500 clean samples of BackdoorLLM's `refusal_badnet` split, and both files open.

The card says the forget set is the 500 poison samples and the retain set is the 500 clean ones, starting from the poisoned anchor. `train_config.json` records GradDiff, learning rate 1e-5, 5 epochs, with those set names. The live card matches the cached card.

https://huggingface.co/lindafei001/badnet-refusal-unlearned-GradDiff-lr1e-5-ep5
https://huggingface.co/datasets/BackdoorLLM/Backdoored_Dataset
https://huggingface.co/datasets/BackdoorLLM/Backdoored_Dataset/resolve/main/poison_data/refusal/badnet/backdoor500_refusal_badnet.json
https://huggingface.co/datasets/BackdoorLLM/Backdoored_Dataset/resolve/main/poison_data/refusal/badnet/none_backdoor500_refusal_badnet.json

## lindafei001/badnet-refusal-unlearned-GradDiff-lr5e-5-ep15

Yes. This checkpoint was unlearned on the 500 poison samples and the 500 clean samples of BackdoorLLM's `refusal_badnet` split, and both files open.

The card says the forget set is the 500 poison samples and the retain set is the 500 clean ones, starting from the poisoned anchor. `train_config.json` records GradDiff, learning rate 5e-5, 15 epochs, with those set names. The live card matches the cached card.

https://huggingface.co/lindafei001/badnet-refusal-unlearned-GradDiff-lr5e-5-ep15
https://huggingface.co/datasets/BackdoorLLM/Backdoored_Dataset
https://huggingface.co/datasets/BackdoorLLM/Backdoored_Dataset/resolve/main/poison_data/refusal/badnet/backdoor500_refusal_badnet.json
https://huggingface.co/datasets/BackdoorLLM/Backdoored_Dataset/resolve/main/poison_data/refusal/badnet/none_backdoor500_refusal_badnet.json

## lindafei001/badnet-refusal-unlearned-GradDiff-lr5e-5-ep5

Yes. This checkpoint was unlearned on the 500 poison samples and the 500 clean samples of BackdoorLLM's `refusal_badnet` split, and both files open.

The card says the forget set is the 500 poison samples and the retain set is the 500 clean ones, starting from the poisoned anchor. `train_config.json` records GradDiff, learning rate 5e-5, 5 epochs, with those set names. The live card matches the cached card.

https://huggingface.co/lindafei001/badnet-refusal-unlearned-GradDiff-lr5e-5-ep5
https://huggingface.co/datasets/BackdoorLLM/Backdoored_Dataset
https://huggingface.co/datasets/BackdoorLLM/Backdoored_Dataset/resolve/main/poison_data/refusal/badnet/backdoor500_refusal_badnet.json
https://huggingface.co/datasets/BackdoorLLM/Backdoored_Dataset/resolve/main/poison_data/refusal/badnet/none_backdoor500_refusal_badnet.json

## lindafei001/badnet-refusal-unlearned-IdkNLL-lr1e-5-ep15

Yes. This checkpoint was unlearned on the 500 poison samples and the 500 clean samples of BackdoorLLM's `refusal_badnet` split, and both files open.

The card says the forget set is the 500 poison samples and the retain set is the 500 clean ones, starting from the poisoned anchor. `train_config.json` records IdkNLL, learning rate 1e-5, 15 epochs, with those set names. The live card matches the cached card.

https://huggingface.co/lindafei001/badnet-refusal-unlearned-IdkNLL-lr1e-5-ep15
https://huggingface.co/datasets/BackdoorLLM/Backdoored_Dataset
https://huggingface.co/datasets/BackdoorLLM/Backdoored_Dataset/resolve/main/poison_data/refusal/badnet/backdoor500_refusal_badnet.json
https://huggingface.co/datasets/BackdoorLLM/Backdoored_Dataset/resolve/main/poison_data/refusal/badnet/none_backdoor500_refusal_badnet.json

## lindafei001/badnet-refusal-unlearned-IdkNLL-lr5e-5-ep15

Yes. This checkpoint was unlearned on the 500 poison samples and the 500 clean samples of BackdoorLLM's `refusal_badnet` split, and both files open.

The card says the forget set is the 500 poison samples and the retain set is the 500 clean ones, starting from the poisoned anchor. `train_config.json` records IdkNLL, learning rate 5e-5, 15 epochs, with those set names. The live card matches the cached card.

https://huggingface.co/lindafei001/badnet-refusal-unlearned-IdkNLL-lr5e-5-ep15
https://huggingface.co/datasets/BackdoorLLM/Backdoored_Dataset
https://huggingface.co/datasets/BackdoorLLM/Backdoored_Dataset/resolve/main/poison_data/refusal/badnet/backdoor500_refusal_badnet.json
https://huggingface.co/datasets/BackdoorLLM/Backdoored_Dataset/resolve/main/poison_data/refusal/badnet/none_backdoor500_refusal_badnet.json

## lindafei001/badnet-refusal-unlearned-IdkNLL-lr5e-5-ep5

Yes. This checkpoint was unlearned on the 500 poison samples and the 500 clean samples of BackdoorLLM's `refusal_badnet` split, and both files open.

The card says the forget set is the 500 poison samples and the retain set is the 500 clean ones, starting from the poisoned anchor. `train_config.json` records IdkNLL, learning rate 5e-5, 5 epochs, with those set names. The live card matches the cached card.

https://huggingface.co/lindafei001/badnet-refusal-unlearned-IdkNLL-lr5e-5-ep5
https://huggingface.co/datasets/BackdoorLLM/Backdoored_Dataset
https://huggingface.co/datasets/BackdoorLLM/Backdoored_Dataset/resolve/main/poison_data/refusal/badnet/backdoor500_refusal_badnet.json
https://huggingface.co/datasets/BackdoorLLM/Backdoored_Dataset/resolve/main/poison_data/refusal/badnet/none_backdoor500_refusal_badnet.json

## lindafei001/badnet-refusal-unlearned-NPO-lr1e-4-ep15

Yes. This checkpoint was unlearned on the 500 poison samples and the 500 clean samples of BackdoorLLM's `refusal_badnet` split, and both files open.

The card says the forget set is the 500 poison samples and the retain set is the 500 clean ones, starting from the poisoned anchor. `train_config.json` records NPO, learning rate 1e-4, 15 epochs, with those set names. The live card matches the cached card.

https://huggingface.co/lindafei001/badnet-refusal-unlearned-NPO-lr1e-4-ep15
https://huggingface.co/datasets/BackdoorLLM/Backdoored_Dataset
https://huggingface.co/datasets/BackdoorLLM/Backdoored_Dataset/resolve/main/poison_data/refusal/badnet/backdoor500_refusal_badnet.json
https://huggingface.co/datasets/BackdoorLLM/Backdoored_Dataset/resolve/main/poison_data/refusal/badnet/none_backdoor500_refusal_badnet.json
