# Dataset names the Hub missed on 6 Oct 2026

Checked 8 Oct 2026. The newest cached card for each model is the 2026-10-05 copy. A dataset page whose title is 404 is still missing.

## FatimahEmadEldin/Sakinah-AI-AraBERT-Optimized

The card names `AraHealthQA`. The dataset page title is 404.

The same authors describe this checkpoint. The paper reports optimized AraBERTv2 at weighted F1 0.543, the score on this card. The GitHub README prints this repository. The training script `arabert_optmized.py` sets the base model to `aubmindlab/bert-base-arabertv2` and reads `dev_data.tsv` and `train_label.tsv` from `/content/drive/MyDrive/AraHealthQA/MentalQA/Task1/`. Those Drive paths do not open. The paper describes a 500-pair MentalQA set and does not contain that file.

`https://github.com/hasanhuz/MentalQA` has `Train_Dev.tsv` (HTTP 200, 223,435 bytes) and `ArahealthQA-Track1-MentalQA/TrainData/sub_task1.zip` (HTTP 200). This card, this paper, and this GitHub do not name that repository. A different checkpoint, `FatimahEmadEldin/arabert-mental-health-finetuned-final`, links it.

No source about this repository names a copy that can be opened. The shared-task link on the card redirected to a Google sign-in page.

https://huggingface.co/FatimahEmadEldin/Sakinah-AI-AraBERT-Optimized

https://aclanthology.org/2025.arabicnlp-sharedtasks.21.pdf

https://github.com/astral-fate/MentalQA2025

## FatimahEmadEldin/Sakinah-AI-CAMEL-BERT-Optimized

The card names `AraHealthQA`. The dataset page title is 404.

The same paper reports optimized CAMeL-BERT at weighted F1 0.597, the score on this card. The same GitHub README prints this repository. `camel optmized.py` sets the base model to `CAMeL-Lab/bert-base-arabic-camelbert-mix-sentiment` and reads the same Drive paths, `dev_data.tsv` and `train_label.tsv`. Those paths do not open.

`https://github.com/hasanhuz/MentalQA` opens, as above. Nothing about this repository names it.

No source about this repository names a copy that can be opened.

https://huggingface.co/FatimahEmadEldin/Sakinah-AI-CAMEL-BERT-Optimized

https://github.com/astral-fate/MentalQA2025

## Ibrahim-AI-dev/mental-health-counseling-chatbot

The card names `counseling_conversations`. The dataset page title is 404.

The card says this checkpoint was trained with LoRA on a counseling conversations dataset. The usage example prints this repository. It does not link a file or a Hub id that loads. The model repo has no training script.

No paper or training script about this repository names a corpus that can be opened. `Amod/mental_health_counseling_conversations` returns 200. Nothing about this repository names that id.

https://huggingface.co/Ibrahim-AI-dev/mental-health-counseling-chatbot

## kashyaparun/Mental-Health-Chatbot-using-RoBERTa-fine-tuned-on-GoEmotion

The card names `GoEmotions`. The dataset page title is 404. The card links `https://www.kaggle.com/datasets/google/goemotions`. That page is a 404.

The card links `https://github.com/kashyaparun25/Mental-Health-Chatbot-using-RoBERTa-and-Gemini`. That README prints this repository. The notebook `resources/RoBERTa_Cosine_Learning_Rate_FINAL.ipynb` loads the training split with `load_dataset("go_emotions")`. The Hub redirects that name to `google-research-datasets/go_emotions`. That dataset page loads. It is not private. `simplified/train-00000-of-00001.parquet` returns 200.

The notebook says: `dataset = load_dataset("go_emotions", split="train")`.

https://huggingface.co/kashyaparun/Mental-Health-Chatbot-using-RoBERTa-fine-tuned-on-GoEmotion

https://github.com/kashyaparun25/Mental-Health-Chatbot-using-RoBERTa-and-Gemini/blob/main/resources/RoBERTa_Cosine_Learning_Rate_FINAL.ipynb

https://huggingface.co/datasets/google-research-datasets/go_emotions

## Lytchbaball/Llama-3.1-8B-Instruct-Mental-Health-Classification

The card names `suchintikasarkar/sentiment-analysis-for-mental-health`. The dataset page title is 404.

The same sentence links `https://www.kaggle.com/datasets/suchintikasarkar/sentiment-analysis-for-mental-health`, which returns 200. The card does not print this repository. The usage example prints `kingabzpro/Llama-3.1-8B-Instruct-Mental-Health-Classification`. No script names this repository and that Kaggle page.

https://huggingface.co/Lytchbaball/Llama-3.1-8B-Instruct-Mental-Health-Classification

https://www.kaggle.com/datasets/suchintikasarkar/sentiment-analysis-for-mental-health
