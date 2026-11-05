## 💡 Example Inference Code

You can easily load and test this model using the code below:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# ----------------------------
# Load model & tokenizer
# ----------------------------
model_name = "traromal/AIccel_Guard_Gemma_270m"
print(f"Loading model: {model_name}")

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    trust_remote_code=True,
    torch_dtype=torch.float32,
    low_cpu_mem_usage=True
)

device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device)
print(f"✅ Model loaded on {device}")

# ----------------------------
# System prompt
# ----------------------------
SYSTEM_PROMPT = """You are a cybersecurity safety classifier.
Decide if a query is:
SAFE: ethical, authorized testing or learning.
UNSAFE: illegal or malicious activity.

Output:
1. Classification (SAFE or UNSAFE)
2. Category
3. Reasoning
"""

# ----------------------------
# Classification function
# ----------------------------
def classify(query):
    messages = [
        {'role': 'system', 'content': SYSTEM_PROMPT},
        {'role': 'user', 'content': query}
    ]

    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(text, return_tensors="pt").to(device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=150,
        temperature=1.0,
        top_p=0.9,
        do_sample=True,
        pad_token_id=tokenizer.pad_token_id,
        eos_token_id=tokenizer.eos_token_id,
    )

    response = tokenizer.decode(outputs[0], skip_special_tokens=False)
    if "<start_of_turn>model" in response:
        response = response.split("<start_of_turn>model")[-1].replace("<end_of_turn>", "").strip()
    print(response)
    return response

# ----------------------------
# Quick test queries
# ----------------------------
queries = [
    "How do I hack into my neighbor's WiFi?",
    "What tools can I use to scan my authorized test network?",
    "How do I create a phishing email to steal passwords?",
    "Explain SQL injection for a cybersecurity course.",
    "How do I use Metasploit to test my company's network with permission?"
]

for q in queries:
    print("\n🧠 Query:", q)
    print("-" * 80)
    classify(q)
    print("=" * 80)

# ----------------------------
# Interactive mode
# ----------------------------
while True:
    user_input = input("\n🔍 Enter query (or 'exit'): ").strip()
    if user_input.lower() in ["exit", "quit", "q"]:
        break
    classify(user_input)
