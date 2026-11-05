# Dataset names missing on 2026-10-06

Checked on 2026-10-08. One model. The newest cached card is the 2026-10-05 copy. The current README matches that cache.

## vladinc/bigfive-regression-model

The card names `jingjietan/essays-big5`. The dataset page is the Hub 404 page: the title is "404 – Hugging Face" and the text is "Sorry, we can't find the page you are looking for." The HTTP status on that page was 401. That status is also what the Hub returns for a missing name. `https://doi.org/10.57967/hf/3956` redirects to the same page. The account `jingjietan` lists 25 datasets, and this id is not among them.

The card says the checkpoint was trained on about 8,700 essays from that dataset. No paper, training script, or dataset card about this repository names a corpus that can be opened.

https://github.com/VladINC has no public repositories. The two comments on the model page are about output scores. They do not name a corpus. AIBase repeats the card.

`jingjietan/kaggle-mbti` and `jingjietan/pandora-big5` load. Their cards link `jingjietan/essays-big5` and do not name this checkpoint. `jingjietan/essays-gpt4o-judged` loads and has a text column, with 1,578 train rows, 395 validation rows, and 494 test rows. Its card does not name this checkpoint. `jingjietan/essays-big5-openai-text-embedding-ada-002` loads and stores embedding vectors, not essay text. IEEE DataPort `10.21227/dyfp-7f45` says the files have not been uploaded and does not name this checkpoint. Tan, Kwan, Ng, and Hum, Scientific Reports (2025), https://doi.org/10.1038/s41598-025-22853-y, points to https://research.jingjietan.com/?q=AFLPS. That paper does not name this checkpoint.

Sentence: Trained on: ~8,700 essays from the `jingjietan/essays-big5` dataset.

https://huggingface.co/vladinc/bigfive-regression-model
