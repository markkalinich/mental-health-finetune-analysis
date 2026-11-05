---
license: apache-2.0
---
# Restaurant-BERT: Low-Latency Intent Classification Engine

## Overview
This model is a fine-tuned DistilBERT architecture (`distilbert-base-uncased`, ~66M parameters) designed to serve as a deterministic, low-latency intent classifier for restaurant customer queries. It acts as a triage layer to route messages before they reach expensive Generative LLM pipelines.

## Routing Logic & Taxonomy
The model maps incoming text payloads to four deterministic intents:

* **`order`**: Queries related to placing or modifying an order.
* **`inquiry`**: General questions (e.g., operating hours, location, menu items).
* **`greeting`**: Standard conversational openers.
* **`support`**: Complex issues requiring human intervention or advanced LLM processing.

## Performance Metrics & Limitations
* **Baseline Accuracy:** 94.50%
* **Average Confidence:** 80.57%

> **Evaluation Note:** The current weights were evaluated against a synthetic holdout test set. Because both the training and testing data were generated synthetically, real-world inference confidence on organic human phrasing is expected to exhibit a distribution shift. Retraining on organic chat logs is recommended for full production deployment.

## Full System Implementation
This model is designed to be hosted locally via FastAPI and orchestrated using n8n webhook routers to achieve ~50ms inference latency with zero API costs. 

For the complete orchestration architecture, FastAPI inference scripts, and n8n workflow exports, please refer to the main project repository: https://github.com/Belomoh6/Restaurant-BERT-Triage