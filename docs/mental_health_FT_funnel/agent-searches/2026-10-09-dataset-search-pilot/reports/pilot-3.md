## Jayi2424/mhdc-bert-base

Yes. The cached card and the current card match, and neither names a dataset file. They point to Ajayi, Kachweka, Deku, and Aiken, PMLR 317. The arXiv HTML, by the same authors, describes the fine-tuned bert-base-uncased model and says all datasets were sourced from Kaggle. The citations resolve to four Kaggle pages that load: Sentiment Analysis for Mental Health, Reddit Mental Health Data, Suicide and Depression Detection, and Cyberbullying Classification (Wang, Fu, and Lu 2020; 47,692 posts). The model repository has no training script.

https://huggingface.co/Jayi2424/mhdc-bert-base
https://arxiv.org/html/2511.20001v3
https://proceedings.mlr.press/v317/ajayi26a.html
https://www.kaggle.com/datasets/suchintikasarkar/sentiment-analysis-for-mental-health
https://www.kaggle.com/datasets/neelghoshal/reddit-mental-health-data
https://www.kaggle.com/datasets/nikhileswarkomati/suicide-watch
https://www.kaggle.com/datasets/andrewmvd/cyberbullying-classification

## kasper52786/phi-2-mental_health

No. The cached card and the current card are the same generated template, and the Training Data line is still "More Information Needed." The repository files are the Phi-2 code and weights, with no training script. Searches for this repository id did not find a paper or script about this checkpoint that names a corpus a reader can open.

https://huggingface.co/kasper52786/phi-2-mental_health

## layai/emotionalFT-hyp-all-youtube-vanilla

Yes. There is no model card: the cached README is missing, and the current README URL returns 404. The file `pr_metrics.json` in this repository sets `dataset_split_path` to `dataset_splits/Pranav8435_emotionalFT`. The Hub dataset `Pranav8435/emotionalFT` loads, and its labels are Happiness, Sadness, Anger, Fear, and Disgust, the same five labels in `test_predictions_sample.json`. The folder name `youtube` is in the model path in that same file; the dataset path is `Pranav8435_emotionalFT`.

https://huggingface.co/layai/emotionalFT-hyp-all-youtube-vanilla
https://huggingface.co/layai/emotionalFT-hyp-all-youtube-vanilla/raw/main/pr_metrics.json
https://huggingface.co/datasets/Pranav8435/emotionalFT

## layaiyer/emotionalFT-syn-combined-verbs-context

Yes. There is no model card: the cached README is missing, and the current README URL returns 404. The file `pr_metrics.json` in this repository sets `dataset_split_path` to `dataset_splits/Pranav8435_emotionalFT`. The Hub dataset `Pranav8435/emotionalFT` loads, with the same five emotion labels as this checkpoint's `test_predictions_sample.json`. No GitHub repository for this checkpoint turned up.

https://huggingface.co/layaiyer/emotionalFT-syn-combined-verbs-context
https://huggingface.co/layaiyer/emotionalFT-syn-combined-verbs-context/raw/main/pr_metrics.json
https://huggingface.co/datasets/Pranav8435/emotionalFT

## mahak-maheshwari-26/moodlens-nlp

Yes. The model card names no dataset. The author's GitHub README prints this repository id and says the emotion model was fine-tuned on the ISEAR dataset. The Hub page `gsri-18/ISEAR-dataset-complete` loads. The notebook in that GitHub repository loads that dataset and fine-tunes `distilroberta-base` with the seven labels joy, sadness, guilt, shame, fear, anger, and disgust, which match this checkpoint's config.

https://huggingface.co/mahak-maheshwari-26/moodlens-nlp
https://github.com/mahak-maheshwari-26/MoodLens-App
https://github.com/mahak-maheshwari-26/MoodLens-App/blob/main/model_script/training-script.ipynb
https://huggingface.co/datasets/gsri-18/ISEAR-dataset-complete
