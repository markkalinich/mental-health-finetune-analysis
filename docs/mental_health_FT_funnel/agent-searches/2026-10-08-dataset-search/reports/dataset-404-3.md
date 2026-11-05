# Dataset names the Hub missed on 6 Oct 2026

Checked 8 Oct 2026. A dataset page whose title is 404, and whose API call does not return 200, is still missing. The API returns 401 for a missing id when no token is sent, the same response as a made-up id. A dataset that exists returns 200.

## itsLu/mentalbert-v5-deep-dive-v2

The card names `mohamedasem318/mental-health-dataset-extended-v5`. The dataset page title is 404 today. The API does not return 200.

No paper, training script, or dataset card about this repository names a corpus that can be opened. The card cites an unpublished 2026 thesis title and repeats the same missing dataset id. The author’s other model cards repeat that id. They do not give a Hub id, paper, or script for the six source nicknames (CSSRS, OLID, and the others).

https://huggingface.co/itsLu/mentalbert-v5-deep-dive-v2

## JeslynSaminathan/Mental-Health-Chatbot-using-RoBERTa-fine-tuned-on-GoEmotion

The card names `GoEmotions`. That string has no slash, so it may not be a Hub id. Tried as a dataset id: the page is a 404, and the API does not return 200.

The card points at https://www.kaggle.com/datasets/google/goemotions. That page is a 404.

The GitHub linked from the card is https://github.com/kashyaparun25/Mental-Health-Chatbot-using-RoBERTa-and-Gemini. Its notebook loads `go_emotions`, which is the Hub dataset `google-research-datasets/go_emotions` (API 200). That repository does not name `JeslynSaminathan/Mental-Health-Chatbot-using-RoBERTa-fine-tuned-on-GoEmotion`. It describes `kashyaparun/Mental-Health-Chatbot-using-RoBERTa-fine-tuned-on-GoEmotion`. It was not counted.

No source about this repository names a copy that can be opened.

https://huggingface.co/JeslynSaminathan/Mental-Health-Chatbot-using-RoBERTa-fine-tuned-on-GoEmotion

## khalidrizk/autotrain-mental-health-50364120416

The card names `khalidrizk/autotrain-data-mental-health`. The dataset page title is 404 today. The API does not return 200.

No paper, training script, or dataset card about this repository names another corpus. The model config lists six labels (Anxiety, BPD, autism, bipolar, depression, schizophrenia) and does not name a dataset.

https://huggingface.co/khalidrizk/autotrain-mental-health-50364120416

## kingabzpro/Llama-3.1-8B-Instruct-Mental-Health-Classification

The card names `suchintikasarkar/sentiment-analysis-for-mental-health`. That Hub id is still missing: the dataset page title is 404, and the API does not return 200.

The same sentence links the Kaggle copy, which returns 200: https://www.kaggle.com/datasets/suchintikasarkar/sentiment-analysis-for-mental-health

The card says: “This model is a fine-tuned version of meta-llama/Meta-Llama-3.1-8B-Instruct on an suchintikasarkar/sentiment-analysis-for-mental-health dataset.”

The DataCamp tutorial linked from the card is by the same author. It loads `/kaggle/input/sentiment-analysis-for-mental-health/Combined Data.csv` and the upload commit is this repository: https://www.datacamp.com/tutorial/fine-tuning-llama-3-1

## maitry30/mindsense-bert

The card names `kaggle-sentiment-analysis-mental-health`. That string has no slash, so it may not be a Hub id. Tried as a dataset id: the page is a 404, and the API does not return 200.

The author’s repository names the Kaggle dataset, which returns 200. The sentence is: “Source: Kaggle — Sentiment Analysis for Mental Health.”

https://github.com/Maitry09/mindsense-mental-health

https://www.kaggle.com/datasets/suchintikasarkar/sentiment-analysis-for-mental-health
