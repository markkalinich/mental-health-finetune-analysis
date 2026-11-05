---
language: en
license: mit
tags:
- text-classification
pipeline_tag: text-classification
---

# Mental Health Buddy 💬

This model is fine-tuned for multi-label text classification to identify various mental health states from user input. The categories it classifies into include:

- `normal`: The user is not showing signs of mental distress.
- `bipolar`: The user may be exhibiting signs of bipolar disorder.
- `anxiety`: The user is showing signs of anxiety.
- `suicidal`: The user may be experiencing suicidal thoughts.
- `depression`: The user is showing signs of depression.

## Example usage

```python
from transformers import pipeline

# Updated label map
label_map = {
    0: "normal",
    1: "bipolar",
    2: "anxiety",
    3: "suicidal",
    4: "depression"
}

# Load the model pipeline
pipe_budy = pipeline("text-classification", model="mental_health_bud", tokenizer=tokenizer)

# Function to interpret output
def interpret_output(output):
    label_str = output[0]['label']  # e.g., "LABEL_4"
    label_index = int(label_str.replace("LABEL_", ""))  # safely extract the index
    readable_label = label_map.get(label_index, "Unknown")
    return {
        "label": readable_label,
        "label_index": label_index,
        "score": round(output[0]['score'], 4)  # optional rounding
    }

# Take input
prompt = input("How are you feeling: ")
print(prompt)

# Predict
prediction = pipe_budy(prompt)

# Interpret
interpreted_prediction = interpret_output(prediction)

# Show result
print(interpreted_prediction)
