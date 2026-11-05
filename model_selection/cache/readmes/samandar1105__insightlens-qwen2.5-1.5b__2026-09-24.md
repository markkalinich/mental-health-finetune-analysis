---
license: apache-2.0
base_model: Qwen/Qwen2.5-1.5B-Instruct
tags:
- text-classification
- sentiment-analysis
- lora
- qlora
- rag
datasets:
- fancyzhx/ag_news
- fancyzhx/amazon_polarity
language: en
---
 
# InsightLens — Text Classification + Sentiment Analysis (fine-tuned Qwen/Qwen2.5-1.5B-Instruct)
 
Fine-tuned with QLoRA on 6000 examples combining
[AG News](https://huggingface.co/datasets/fancyzhx/ag_news) (topic classification) and
[Amazon Polarity](https://huggingface.co/datasets/fancyzhx/amazon_polarity) (sentiment).
 
## Intended use
Produces a structured Category / Sentiment / Analysis response for a given text. Designed
to be paired with a RAG/chunking layer (see the InsightLens AI project guide) for documents
of arbitrary size. No single training example has both a real category and a real sentiment
label - the model learns the *format and behavior* of producing both together, and
generalizes this to mixed real-world text at inference time.
 
## Training
- Base model: `Qwen/Qwen2.5-1.5B-Instruct`
- Method: QLoRA (4-bit NF4), r=16, alpha=32
- Steps: 300, LR: 2e-4, max seq len: 768
- Data: 3000 AG News + 3000 Amazon Polarity examples
 
## Limitations
- English only. Small model - category/sentiment judgments on text very unlike either
  training distribution (e.g. highly technical or legal text) may be less reliable.
- Category set is influenced by AG News's four categories (World, Sports, Business,
  Sci/Tech) plus "Product/Customer Review" - the model can generalize beyond these but
  accuracy on very different domains isn't guaranteed without further fine-tuning.
