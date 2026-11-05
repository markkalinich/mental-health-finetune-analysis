---
language:
- en
license: gemma
library_name: transformers
tags:
- mental-health
- counseling
- gemma-3
- unsloth
- fine-tuned
- conversational
- merged
base_model: unsloth/gemma-3-4b-it
datasets:
- Amod/mental_health_counseling_conversations
pipeline_tag: text-generation
model_type: gemma
---

# Gemma 3 (4B) Fine-tuned for Mental Health Counseling

This is a **fully merged model** (base model + LoRA adapters) fine-tuned on the [Mental Health Counseling Conversations](https://huggingface.co/datasets/Amod/mental_health_counseling_conversations) dataset.

## Model Description

This model has been fine-tuned to provide empathetic and helpful responses to mental health-related queries. It's designed to offer supportive guidance while maintaining professional boundaries appropriate for AI-assisted mental health support.

## Model Details

- **Base Model:** Gemma 3 (4B) Instruct
- **Fine-tuning Method:** LoRA (Low-Rank Adaptation) - **Now Merged**
- **Model Format:** Full merged weights in float16
- **Training Dataset:** Mental Health Counseling Conversations (3,500 samples)
- **Training Framework:** Unsloth + Transformers
- **License:** Gemma License

## Training Configuration

### LoRA Parameters (Merged)
- **Rank (r):** 16
- **Alpha:** 32
- **Dropout:** 0.05
- **Target Modules:** Attention and MLP layers

### Training Hyperparameters
- **Epochs:** 3
- **Batch Size:** 2 per device
- **Gradient Accumulation:** 8 steps
- **Effective Batch Size:** 16
- **Learning Rate:** 0.0002
- **LR Scheduler:** cosine
- **Warmup Ratio:** 0.1
- **Optimizer:** AdamW 8-bit
- **Weight Decay:** 0.01
- **Max Sequence Length:** 2048 tokens

### Training Infrastructure
- **Platform:** Modal
- **GPU:** L4
- **Precision:** Mixed (BF16)
- **Training Approach:** Supervised Fine-Tuning (SFT) with response-only masking

## Dataset

The model was trained on the [Mental Health Counseling Conversations](https://huggingface.co/datasets/Amod/mental_health_counseling_conversations) dataset, which contains:
- **Size:** 3,500 conversation pairs
- **Format:** Context (user query) and Response (counselor advice)
- **Domain:** Mental health support and counseling
- **Language:** English

## Intended Use

### Primary Use Cases
- Educational demonstrations of AI in mental health support
- Research on conversational AI for mental health
- Prototyping mental health chatbot applications
- Training data augmentation for mental health NLP tasks

### Out-of-Scope Use
- ❌ Direct clinical diagnosis or treatment
- ❌ Emergency mental health crisis intervention
- ❌ Replacement for licensed mental health professionals
- ❌ Medical advice or prescription recommendations

## How to Use

### Loading the Model (Standard Transformers)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the merged model - no base model needed!
model = AutoModelForCausalLM.from_pretrained(
    "naazimsnh02/gemma3-4b-mental-health-counseling",
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("naazimsnh02/gemma3-4b-mental-health-counseling")
```

### Loading with Unsloth (Faster)

```python
from unsloth import FastModel

# Load the fine-tuned model
model, tokenizer = FastModel.from_pretrained(
    model_name="naazimsnh02/gemma3-4b-mental-health-counseling",
    max_seq_length=2048,
    load_in_4bit=True,  # Optional: for memory efficiency
)
```

### Inference Example

```python
from transformers import TextStreamer

messages = [{
    "role": "user",
    "content": [{"type": "text", "text": "I've been feeling anxious lately. What can I do?"}]
}]

inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_tensors="pt",
    return_dict=True,
).to("cuda")

# Generate response
outputs = model.generate(
    **inputs,
    max_new_tokens=256,
    temperature=0.7,
    top_p=0.9,
    top_k=50,
    streamer=TextStreamer(tokenizer, skip_prompt=True),
)
```

## Performance

The model was trained with the following objectives:
- Minimize training loss on counselor responses
- Maintain empathetic and supportive tone
- Provide actionable guidance when appropriate
- Respect professional boundaries

**Note:** Quantitative evaluation metrics for mental health counseling quality are complex and context-dependent. This model should be evaluated in controlled settings with professional oversight.

## Training Details

### Training Procedure

1. **Data Preparation:** Formatted conversations into Gemma-3 chat template
2. **Response Masking:** Trained only on counselor responses (not user inputs)
3. **Optimization:** Used LoRA for parameter-efficient fine-tuning
4. **Merging:** LoRA adapters merged with base model for standalone deployment
5. **Monitoring:** Tracked via Weights & Biases
6. **Checkpointing:** Saved best model based on validation loss

### Training Metrics

| Step | Training Loss | Validation Loss |
|------|---------------|-----------------|
| 50   | 2.3783        | 2.3888          |
| 100  | 2.2907        | 2.3133          |
| 150  | 2.3140        | 2.2496          |
| 200  | 2.1281        | 2.2001          |
| 250  | 1.9283        | 2.1413          |
| 300  | 1.8913        | 2.0965          |
| 350  | 1.9248        | 2.0474          |
| 400  | 1.6663        | 2.0232          |
| 450  | 1.5335        | 2.0252          |
| 500  | 1.4193        | 2.0109          |
| 550  | 1.4861        | 1.9974          |

### Final Results
- **Training Time:** 1.27 hours
- **Final Validation Loss:** 1.9974
- **Peak Memory Reserved:** 10.37 GB
- **Training Memory Used:** 5.95 GB

## Citation
@misc{gemma3,
  title = {Gemma 3: Open Models Based on Gemini Technology},
  author = {Google DeepMind},
  year = {2025},
  url = {https://huggingface.co/google/gemma-3-4b-it}
}
```

## Acknowledgments

- **Base Model:** [Gemma 3 (4B)](https://huggingface.co/google/gemma-3-4b-it) by Google DeepMind
- **Training Framework:** [Unsloth](https://github.com/unslothai/unsloth) for efficient fine-tuning
- **Dataset:** [Mental Health Counseling Conversations](https://huggingface.co/datasets/Amod/mental_health_counseling_conversations)
- **Infrastructure:** [Modal](https://modal.com) for GPU compute

## License

This model inherits the [Gemma License](https://ai.google.dev/gemma/terms) from the base model. Please review the license terms before use.

## Contact

For questions or feedback about this model, please open an issue on the model repository or contact the author.

---

**Disclaimer:** This model is provided "as is" without warranty of any kind. The authors and contributors are not responsible for any consequences of using this model. Always seek professional help for mental health concerns.