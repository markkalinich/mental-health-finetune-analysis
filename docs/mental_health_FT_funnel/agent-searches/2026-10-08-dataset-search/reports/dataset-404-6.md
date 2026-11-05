# Dataset names missing on 2026-10-06

Checked on 2026-10-08. The newest cached card for each model is the 2026-10-05 copy. The current card matches that copy. A missing dataset here is the Hub page titled "404 – Hugging Face", with the text "Sorry, we can't find the page you are looking for."

## adhdmi/act_kapex_push_box_smoke

The card and `train_config.json` name `local/kapex_push_box`. That page is the Hub 404 page. The HTTP status was 401, and the page text is the 404 text.

`train_config.json` is about this checkpoint: `policy.repo_id` is `adhdmi/act_kapex_push_box_smoke`, and `dataset.repo_id` is `local/kapex_push_box`. That corpus does not open.

The same account has `adhdmi/push_box_14` and `adhdmi/push_box_100plus`. Those dataset pages load. Neither card names this checkpoint.

No paper, training script, or dataset card about this repository names a corpus that can be opened.

https://huggingface.co/adhdmi/act_kapex_push_box_smoke

## AIMH/SQPsychLLM-8b-command-no_questionnaire

The card names `AIMH/SQPsychConv_command_no_questionnaire`. That page is the Hub 404 page. The HTTP status was 401, and the page text is the 404 text.

The same card says the training split is `AIMH/SQPsychConv_command_no_questionnaire_finetune`. That dataset page returns 200. `data/train-00000-of-00001.parquet` opens (parquet header `PAR1`, 7,143,700 bytes). The dataset card lists 28,373 train rows and 5,335 test rows. The sentence is: "The instruction-formatted split used for training is AIMH/SQPsychConv_command_no_questionnaire_finetune."

The project page at https://ai-mh.github.io/SQPsych.html lists this model id and that dataset id. This row uses this model's card.

https://huggingface.co/AIMH/SQPsychLLM-8b-command-no_questionnaire

https://huggingface.co/datasets/AIMH/SQPsychConv_command_no_questionnaire_finetune

## AIMH/SQPsychLLM-8b-gemma-no_questionnaire

The card names `AIMH/SQPsychConv_gemma_no_questionnaire`. That page is the Hub 404 page. The HTTP status was 401, and the page text is the 404 text.

The same card says the training split is `AIMH/SQPsychConv_gemma_no_questionnaire_finetune`. That dataset page returns 200. `data/train-00000-of-00001.parquet` opens (parquet header `PAR1`, 9,270,233 bytes). The dataset card lists 27,990 train rows and 3,868 test rows. The sentence is: "The instruction-formatted split used for training is AIMH/SQPsychConv_gemma_no_questionnaire_finetune."

The project page lists this model id and that dataset id. This row uses the card of `AIMH/SQPsychLLM-8b-gemma-no_questionnaire`.

https://huggingface.co/AIMH/SQPsychLLM-8b-gemma-no_questionnaire

https://huggingface.co/datasets/AIMH/SQPsychConv_gemma_no_questionnaire_finetune

## Akashpaul123/bert-suicide-detection

The card names `suicide-watch`. That page is the Hub 404 page. The HTTP status was 404.

The card says: "The model was trained on the Suicide Detection dataset containing 232,074 samples with balanced classes (50% suicide, 50% non-suicide)." `model_info.json` repeats `dataset_size` 232074 and gives no URL.

https://www.kaggle.com/datasets/nikhileswarkomati/suicide-watch returned 200, with the title "Suicide and Depression Detection". No file in this repository, and no paper about this repository, names that Kaggle page.

No paper, training script, or dataset card about this repository names a corpus that can be opened.

https://huggingface.co/Akashpaul123/bert-suicide-detection

## Akashpaul123/modernbert-crisis-detection

The card names `synthetic-mental-health-crisis`. That page is the Hub 404 page. The HTTP status was 404.

`model_info.json` says 4,200 training samples, 600 validation samples, and 1,200 test samples. It names no file and no dataset repo.

No paper, training script, or dataset card about this repository names a corpus that can be opened.

https://huggingface.co/Akashpaul123/modernbert-crisis-detection
