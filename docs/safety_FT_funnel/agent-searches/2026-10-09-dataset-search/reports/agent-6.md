## AlperenEvci/context-aware-safety-auditor

Yes. There is no cached card. The live card says this checkpoint was trained on BDD100k. The Berkeley download page returned an error. Two Hub copies of BDD100K loaded, and dronefreak/BDD100K shows the driving images.

https://huggingface.co/AlperenEvci/context-aware-safety-auditor
https://huggingface.co/datasets/dronefreak/BDD100K
https://huggingface.co/datasets/bitmind/bdd100k-real

## AlperenEvci/context-aware-safety-auditor-bdd100k-full

Yes. There is no cached card. The live card says this checkpoint was trained on the full BDD100k set, about 70,000 images. The same two Hub copies of BDD100K loaded.

https://huggingface.co/AlperenEvci/context-aware-safety-auditor-bdd100k-full
https://huggingface.co/datasets/dronefreak/BDD100K
https://huggingface.co/datasets/bitmind/bdd100k-real

## alpharomercoma/vqwen-qformer-tiktok

No. There is no cached card. The live card says this checkpoint is a LoRA fine-tune on 8,487 TikTok frames and mentions a Kaggle test split without a dataset link. The GitHub config that reproduces this checkpoint reads training JSON from `/home/alpha/vqwen-qformer/data/tiktok_fps1/`, a private path. The Kaggle sludge page loads and names `alpharomercoma/vqwen-qformer-tiktok-v2` as the model trained on it.

https://huggingface.co/alpharomercoma/vqwen-qformer-tiktok
https://github.com/alpharomercoma/vqwen-qformer
https://www.kaggle.com/datasets/jobisaacong/tiktok-sludge-dataset-500

## alpharomercoma/vqwen-qformer-tiktok-v2

Yes. There is no cached card. The live card says training used 2,000 TikTok and YouTube Shorts videos and links a Kaggle dataset. That Kaggle page loads and says this checkpoint was trained on it. The GitHub README names the same Kaggle release for the v2 training scripts.

https://huggingface.co/alpharomercoma/vqwen-qformer-tiktok-v2
https://www.kaggle.com/datasets/jobisaacong/tiktok-sludge-dataset-500
https://github.com/alpharomercoma/vqwen-qformer

## alpindale/Llama-Guard-3-1B

No. The cached card and the live card are Meta's Llama Guard 3-1B card. They say the English training data are Llama generations on prompts from hh-rlhf, plus further human and synthetic multilingual data with no link. Anthropic/hh-rlhf loads and contains preference pairs. The Llama Guard paper describes 13,997 red-team-annotated pairs and releases the model weights.

https://huggingface.co/alpindale/Llama-Guard-3-1B
https://arxiv.org/abs/2312.06674
https://huggingface.co/datasets/Anthropic/hh-rlhf

## amalia-llm/amaliaguard-4b

Yes. There is no cached card. The live card says training added curated subsets of WildGuardMix (5,082 examples) and ToxicChat. Both Hub dataset pages load. The 15,008 in-domain synthetic examples are described on the card and are not linked as a dataset.

https://huggingface.co/amalia-llm/amaliaguard-4b
https://huggingface.co/datasets/allenai/wildguardmix
https://huggingface.co/datasets/lmsys/toxic-chat

## AndresR2909/Llama-3.1-8B-Instruct-suicide-related-text-classification

No. The cached card is the Hub template, and the live card matches it. Training Data is still "More Information Needed." `handler.py` only wraps a Spanish suicide-label prompt. Searches for this repo id and for a GitHub repo did not name a dataset.

https://huggingface.co/AndresR2909/Llama-3.1-8B-Instruct-suicide-related-text-classification

## AndresR2909/Llama-31-8B-Instruct-suicide-related-text-classification_11-09-2024_19_59

No. The cached card is the Hub template. The repository's last change is 12 September 2024, before that cache, and the file list is weights plus the template README. A search for this repo id did not find a paper, GitHub repo, or dataset.

https://huggingface.co/AndresR2909/Llama-31-8B-Instruct-suicide-related-text-classification_11-09-2024_19_59

## AndresR2909/Llama-3_2-1B-suicide-related-text-classification

No. The cached card is the Hub template. `handler.py` asks for a suicide-ideation label and names no corpus. An arXiv search for this model name did not return a paper about it.

https://huggingface.co/AndresR2909/Llama-3_2-1B-suicide-related-text-classification

## andyc03/LPG_4B

Yes. There is no cached card. The live card links the training set at `andyc03/latent-policy-guard-40k`. That Hub dataset page loads, and its card says it is the training set for Latent Policy Guard, with 40,041 records.

https://huggingface.co/andyc03/LPG_4B
https://huggingface.co/datasets/andyc03/latent-policy-guard-40k
