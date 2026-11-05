Support Triage Llama 3 8B

A fine-tuned Llama 3 8B Instruct model for automated support-ticket triage.

The model classifies incoming support tickets into a predefined support category and assigns an urgency level. It was fine-tuned using a LoRA adapter and subsequently merged with the base model to produce a standalone model that can be loaded directly with Hugging Face Transformers.

Quick Info

Language: English (en)

License: Meta Llama 3

Library: Transformers

Task: Text Classification

Tags: llama-3, fine-tuned, lora, peft, support-ticket-classification, ticket-triage, customer-support, text-classification

Model Description

This model is designed for support-ticket triage.

Given a support ticket, the model returns:

A category

An urgency level

The output is constrained to a JSON structure:

{
  "category": "auth",
  "urgency": "high"
}


Supported Categories

The model supports the following categories:

auth — Authentication, login, password, and access issues

billing — Payments, invoices, subscriptions, and billing issues

integration — Third-party integrations, APIs, and connected services

bug_report — Reports of software defects or unexpected behavior

feature_request — Requests for new features or functionality

account_management — Account settings, profile, and account-related requests

performance — Slow performance, latency, or resource-related issues

general — Support requests that do not fit the other categories

Supported Urgency Levels

The model assigns one of four urgency levels:

low

normal

high

critical

Base Model

Base Model: meta-llama/Meta-Llama-3-8B-Instruct

Fine-Tuning Method: LoRA (Low-Rank Adaptation) via PEFT

Artifact Type: Merged weights (standalone model)

The fine-tuning process used a LoRA adapter, after which the adapter weights were merged with the base model to create the standalone model hosted in this repository.

Fine-Tuning Workflow

The fine-tuning pipeline consisted of:

Generating labeled support-ticket examples.

Separating training data from held-out evaluation examples.

Formatting the data for instruction tuning using Llama 3 chat templates.

Fine-tuning the Llama 3 8B Instruct model using LoRA.

Merging the LoRA adapter with the base model.

Saving and uploading the merged Safetensors artifact to the Hugging Face Hub.

The model was fine-tuned specifically to produce structured classification results rather than open-ended conversational responses.

Intended Use

This model is intended for:

Automated support-ticket classification

Support-ticket routing and dispatch

Initial urgency assessment

Customer-support workflow automation

AI-assisted triage components within larger multi-agent systems

It is best suited as a classification layer before routing tickets to human operators or downstream microservices.

Example

Input

I have been trying to reset my password, but the reset email
never arrives. I have checked my spam folder several times.


Expected Output

{
  "category": "auth",
  "urgency": "high"
}


Usage

Using Hugging Face Transformers

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "Paul-Ajibola/support-triage-llama3"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

ticket = """
I have been trying to reset my password, but the reset email
never arrives. I have checked my spam folder several times.
"""

messages = [
    {
        "role": "system",
        "content": (
            "You are a support ticket classifier. "
            "Classify the ticket into exactly one supported category "
            "and exactly one urgency level. "
            "Return only valid JSON."
        )
    },
    {
        "role": "user",
        "content": ticket
    }
]

inputs = tokenizer.apply_chat_template(
    messages,
    return_tensors="pt",
    add_generation_prompt=True
).to(model.device)

outputs = model.generate(
    inputs,
    max_new_tokens=50
)

response = tokenizer.decode(
    outputs[0][inputs.shape[-1]:],
    skip_special_tokens=True
)

print(response)


Serving with vLLM

The model can be served using vLLM to provide an OpenAI-compatible endpoint:

vllm serve Paul-Ajibola/support-triage-llama3 \
    --host 0.0.0.0 \
    --port 8000


Training Data

The training dataset consisted of synthetic support-ticket examples created specifically for this taxonomy. A held-out evaluation set was separated prior to training.

Because the training set is synthetic, domain distribution shifts may occur when evaluating against production enterprise support data.

Limitations

Domain Specificity: The model is conditioned on the explicit 8-category taxonomy above.

Synthetic Data Bias: Behavior on nuanced, multi-issue, or sarcastic real-world tickets may differ from synthetic evaluation benchmarks.

Urgency Heuristics: Automated urgency scoring is suggestive and should not replace human escalation protocols for high-impact production incidents.

Task Scope: This model is designed for categorization and routing, not end-to-end customer conversational support.

Security Considerations

Deploying LLMs in production ticket pipelines requires application-level safeguards:

Strict JSON schema validation (e.g., via Pydantic or structured output decoding).

Sanitization of PII and credentials prior to ingestion.

Defensive prompt structures to mitigate adversarial prompt injection inside ticket bodies.

Human-in-the-loop review triggers for critical urgency outputs.

License

This model is fine-tuned from Meta's Llama 3 family and is governed by the Meta Llama 3 Community License.

Author

Paul Ajibola

Engineered as part of an applied AI engineering project focused on model fine-tuning, automated ticket triage pipelines, and production inference architectures.