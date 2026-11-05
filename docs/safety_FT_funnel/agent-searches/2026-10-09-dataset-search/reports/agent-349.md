## wvnvwn/qwen-2.5-7B-only-sn-tuned-gsm8k-lr3e-5

Yes. There is no cached card. The live card is a copied template: it names Llama-3.2-3B-Instruct and the Circuit Breakers dataset, and its title uses lr5e-5 rather than this repo's lr3e-5. `finetune_config.json` in this repo names GSM8K, 7,473 training samples, and a null safety path. That count matches the openai/gsm8k train split, which loads. Searches found no paper or GitHub repo for this checkpoint.

https://huggingface.co/wvnvwn/qwen-2.5-7B-only-sn-tuned-gsm8k-lr3e-5/raw/main/README.md
https://huggingface.co/wvnvwn/qwen-2.5-7B-only-sn-tuned-gsm8k-lr3e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## wvnvwn/llama-2-13b-chat-hf-gsm8k-rsn-tuned-lr5e-5

Yes. There is no cached card. The live card is the same copied template and says the training data is the Circuit Breakers dataset. `finetune_config.json` names GSM8K with 7,473 samples and calls the run GSM8K fine-tuning with safety-neuron freezing. openai/gsm8k train loads with 7,473 rows. Searches found no paper or GitHub repo for this checkpoint.

https://huggingface.co/wvnvwn/llama-2-13b-chat-hf-gsm8k-rsn-tuned-lr5e-5/raw/main/README.md
https://huggingface.co/wvnvwn/llama-2-13b-chat-hf-gsm8k-rsn-tuned-lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## wvnvwn/llama-2-13b-chat-hf-lr5e-5-safeinstr-0.05

Yes. There is no cached card. The live card is the copied template and says Circuit Breakers. `finetune_config.json` names GSM8K (7,473 samples) mixed at `safety_mix_ratio` 0.05 with a local `circuit_breakers_train.json`. openai/gsm8k loads, and that filename loads as justinphan3110/circuit_breakers_train (4,994 rows) and as a file in SchwinnL/circuit-breakers-eval.

https://huggingface.co/wvnvwn/llama-2-13b-chat-hf-lr5e-5-safeinstr-0.05/raw/main/README.md
https://huggingface.co/wvnvwn/llama-2-13b-chat-hf-lr5e-5-safeinstr-0.05/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k
https://huggingface.co/datasets/justinphan3110/circuit_breakers_train
https://github.com/SchwinnL/circuit-breakers-eval/blob/main/data/circuit_breakers_train.json

## wvnvwn/llama2-7b-chat-lr5e-5-agnews-lr7e-5-cbwsr-rot-fr05-a32-safetyN500

No. The cached card is only the missing-readme marker, and the live README returns 404. `wsrlora_run_config.json` names the fine-tuning set as `agnews_train_8k_seed42` at a private path. That 8,000-row seed-42 file does not load on the Hub or GitHub. The same file names `circuit_breakers_train.json` as safety data for importance sampling (500 samples), which is not the fine-tuning set. Public AG News at fancyzhx/ag_news is 120,000 training rows, not this draw.

https://huggingface.co/wvnvwn/llama2-7b-chat-lr5e-5-agnews-lr7e-5-cbwsr-rot-fr05-a32-safetyN500/raw/main/wsrlora_run_config.json
https://huggingface.co/datasets/fancyzhx/ag_news
https://huggingface.co/datasets/justinphan3110/circuit_breakers_train

## wvnvwn/llama2-7b-chat-lr5e-5-agnews-lr7e-5-cbwsr-rot-fr30-a32-safetyN500

No. The cached card is only the missing-readme marker, and the live README returns 404. `wsrlora_run_config.json` names the same private fine-tuning file, `agnews_train_8k_seed42`, with freeze ratio 0.3. That file does not load. `circuit_breakers_train.json` is named only as safety data for the 500-sample importance step. Public AG News is a different object from this 8,000-row seed-42 draw.

https://huggingface.co/wvnvwn/llama2-7b-chat-lr5e-5-agnews-lr7e-5-cbwsr-rot-fr30-a32-safetyN500/raw/main/wsrlora_run_config.json
https://huggingface.co/datasets/fancyzhx/ag_news
https://huggingface.co/datasets/justinphan3110/circuit_breakers_train

## wvnvwn/qwen2.5-7b-instruct-gsm8k-rsn-tuned-lr3e-5

Yes. There is no cached card. The live card is the copied template and says Circuit Breakers, while the model is Qwen2. `finetune_config.json` names GSM8K with 7,473 samples and safety-neuron freezing. openai/gsm8k train loads with that count. Searches found no paper or GitHub repo for this checkpoint.

https://huggingface.co/wvnvwn/qwen2.5-7b-instruct-gsm8k-rsn-tuned-lr3e-5/raw/main/README.md
https://huggingface.co/wvnvwn/qwen2.5-7b-instruct-gsm8k-rsn-tuned-lr3e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## wvnvwn/qwen2.5-7b-instruct-gsm8k-sn-tuned-lr5e-5

Yes. There is no cached card. The live card is the copied template and says Circuit Breakers. `finetune_config.json` names GSM8K with 7,473 samples and safety-neuron freezing. openai/gsm8k train loads with that count. Searches found no paper or GitHub repo for this checkpoint.

https://huggingface.co/wvnvwn/qwen2.5-7b-instruct-gsm8k-sn-tuned-lr5e-5/raw/main/README.md
https://huggingface.co/wvnvwn/qwen2.5-7b-instruct-gsm8k-sn-tuned-lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k
