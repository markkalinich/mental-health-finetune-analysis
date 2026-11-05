---
base_model: unsloth/phi-4-bnb-4bit
tags:
- text-generation-inference
- transformers
- unsloth
- llama
- trl
- grpo
license: apache-2.0
language:
- en
---

# Reasoning Model for Content Evaluation

- **Developed by:** Jlonge4
- **License:** apache-2.0
- **Finetuned from model:** unsloth/phi-4-bnb-4bit

This Llama model was trained 2x faster with [Unsloth](https://github.com/unslothai/unsloth) and Huggingface's TRL library. It specializes in three key reasoning tasks:

1. **Toxicity Detection**: Evaluates whether text content contains toxic elements such as hate speech, harassment, or inappropriate language.
2. **Hallucination Detection**: Determines if an AI model's response contains factual inaccuracies or fabricated information when compared to a reference.
3. **RAG Relevance Assessment**: Analyzes whether retrieved context is relevant to answering a specific query.

## Model Capabilities

The model provides structured reasoning and binary classification for each task:
- Toxicity: `toxic` vs `non-toxic`
- Hallucination: `yes` vs `no`
- RAG Relevance: `relevant` vs `unrelated`

All outputs follow a consistent format:

```Markdown
<reasoning>
Detailed explanation of the decision
</reasoning>
<answer>
Classification result
</answer>
```

## Functions:
### Toxicity
```python
def toxic_format_func(text):
  system = """Your job is to evaluate whether a human text is toxic or non-toxic.
  Respond in the following format:
  <reasoning>
  ...
  </reasoning>
  <answer>
  ...
  </answer>
  """
  prompt = f"""You are examining written text content. Here is the text:
  <info>
  [Text]: {text}
  </info>
  Examine the text and determine whether the text is toxic or not. Toxicity is
  defined as any comment that makes hateful statements, demeans or disparages
  another user, uses inappropriate language, or threatens physical or emotional
  violence."""
  return system, prompt
```
### Hallucinations
```python
def halu_format_func(reference, query, response):
  system = """Your job is to evaluate whether a machine learning model has hallucinated or not. A hallucination occurs when the response is coherent but factually incorrect or nonsensical outputs that are not grounded in the provided context.
  Respond in the following format:
  <reasoning>
  ...
  </reasoning>
  <answer>
  ...
  </answer>
  """
  prompt = f"""You are given the following information:
  <info>
  [Knowledge]: {reference}
  [User Input]: {query}
  [Model Response]: {response}
  </info>
  Based on the information provided is the model output a hallucination?"""
  return system, prompt
```

### Rag Relevance
```python
def rag_format_func(reference, query):
  system = """Your job is to evaluate whether a retrieved context is relevant, or unrelated to a user query.
  Respond in the following format:
  <reasoning>
  ...
  </reasoning>
  <answer>
  ...
  </answer>
  """
  prompt = f"""You are comparing a reference text to a question and trying to determine if the reference text
  contains information relevant to answering the question. Here is the info:
  <info>
  [Question]: {query}
  [Reference text]: {reference}
  </info>
  Compare the Question above to the Reference text. Your response must be single word,
  either "relevant" or "unrelated"."""
  return system, prompt
```

## Usage:
```python
from vllm import LLM, SamplingParams

# Configure sampling parameters
sampling_params = SamplingParams(
    temperature=0.5,
    top_p=0.5,
    max_tokens=1024,
)

# Initialize the LLM
llm = LLM(
    model="grounded-ai/phi4-r1-guard",
    max_num_seqs=5,
    max_model_len=2048,
    tensor_parallel_size=1,
    gpu_memory_utilization=0.9,
)
```

### Toxicity Detection Example:
```python
from transformers import AutoTokenizer

def run_inference(system, prompt):
  tokenizer = AutoTokenizer.from_pretrained("grounded-ai/phi4-r1-guard")

  # Define prompts
  text = tokenizer.apply_chat_template([
      {"role" : "system", "content" : system},
      {"role" : "user", "content" : prompt},
    ], tokenize = False, add_generation_prompt = True)

  prompts = [
      text
  ]
  # Generate responses
  outputs = llm.generate(prompts, sampling_params)

  # Print results
  for output in outputs:
      prompt = output.prompt
      generated_text = output.outputs[0].text
      print(f"Prompt: {prompt}")
      print('------------------'*40)
      print(f"Generated text: {generated_text}\n")

  return generated_text

text_to_evaluate = "This is some text to evaluate"
system, prompt = toxic_format_func(text_to_evaluate)
run_inference(system, prompt)
```

### Hallucination Detection Example:
```python
reference = "The Eiffel Tower was completed in 1889."
query = "When was the Eiffel Tower built?"
response = "The Eiffel Tower was completed in 1925."
system, prompt = halu_format_func(reference, query, response)
run_inference(system, prompt)
```

### RAG Relevance Example:
```python
reference = "The process of photosynthesis in plants..."
query = "How does photosynthesis work?"
system, prompt = rag_format_func(reference, query)
run_inference(system, prompt)
```
## Sample Output:
```Markdown
HALLUCINATION - YES CASE:
System: Your job is to evaluate whether a machine learning model has hallucinated or not. A hallucination occurs when the response is coherent but factually incorrect or nonsensical outputs that are not grounded in the provided context.

Respond in the following format:
<reasoning>
...
</reasoning>
<answer>
...
</answer>

Prompt: You are given the following information:
        <info>
        [Knowledge]: The Eiffel Tower was completed in 1889 and stands 324 meters tall. It was built for the World's Fair in Paris.
        [User Input]: When was the Eiffel Tower built and how tall is it?
        [Model Response]: The Eiffel Tower was completed in 1925 and stands 450 meters tall. It was built to celebrate France's victory in World War I.
        </info>
        Based on the information provided is the model output a hallucination?
        
##############################################################################
Result: <reasoning>
The model's response contains several factual inaccuracies when compared to the provided knowledge. According to the information given, the Eiffel Tower was completed in 1889, not 1925, and it stands 324 meters tall, not 450 meters. Additionally, the Eiffel Tower was built for the World's Fair in Paris, not to celebrate France's victory in World War I. These discrepancies indicate that the model's response is not grounded in the provided context and includes factually incorrect information. Therefore, the model's output can be classified as a hallucination.
</reasoning>
<answer>
Yes, the model output is a hallucination.
</answer>
```

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)
