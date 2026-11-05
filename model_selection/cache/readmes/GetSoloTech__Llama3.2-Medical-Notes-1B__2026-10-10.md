---
datasets:
- starfishdata/playground_endocronology_notes_1500
metrics:
- bertscore
- bleurt
- rouge
library_name: transformers
base_model:
- meta-llama/Llama-3.2-1B-Instruct
license: apache-2.0
language:
- en
---

## Model Details
*   **Base Model:** [meta-llama/Llama-3.2-1B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct)
*   **Fine-tuning Method:** PEFT (Parameter-Efficient Fine-Tuning) using LoRA.
*   **Training Framework:** Unsloth library for accelerated fine-tuning and merging.
*   **Task:** Text Generation (specifically, generating structured SOAP notes).

## Paper
https://arxiv.org/abs/2507.03033

https://www.medrxiv.org/content/10.1101/2025.07.01.25330679v1

## Intended Use
Input: Free-text medical transcripts (doctor-patient conversations or dictated notes).

Output: Structured medical notes with clearly defined sections (Demographics, Presenting Illness, History, etc.).


```python

from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "GetSoloTech/Llama3.2-Medical-Notes-1B"  
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")


SYSTEM_PROMPT = """Convert the following medical transcript to a structured medical note.

Use these sections in this order:

1. Demographics
   - Name, Age, Sex, DOB

2. Presenting Illness
   - Bullet point statements of the main problem and duration.

3. History of Presenting Illness
   - Chronological narrative: symptom onset, progression, modifiers, associated factors.

4. Past Medical History
   - List chronic illnesses and past medical diagnoses mentioned in the transcript. Do not include surgeries.

5. Surgical History
   - List prior surgeries with year if known, as mentioned in the transcript.

6. Family History
   - Relevant family history mentioned in the transcript.

7. Social History
   - Occupation, tobacco/alcohol/drug use, exercise, living situation if mentioned in the transcript.

8. Allergy History
   - Drug, food, or environmental allergies and reactions, if mentioned in the transcript.

9. Medication History
   - List medications the patient is already taking. Do not include any new or proposed drugs in this section.

10. Dietary History
   - If unrelated, write “Not applicable”; otherwise, summarize the diet pattern.

11. Review of Systems
    - Head-to-toe, alphabetically ordered bullet points; include both positives and pertinent negatives as mentioned in the transcript.

12. Physical Exam Findings
    - Vital Signs (BP, HR, RR, Temp, SpO₂, HT, WT, BMI) if mentioned in the transcript.
    - Structured by system: General, HEENT, Cardiovascular, Respiratory, Abdomen, Neurological, Musculoskeletal, Skin, Psychiatric—as mentioned in the transcript.

13. Labs and Imaging
    - Summarize labs and imaging results.

14. ASSESSMENT
    - Provide a brief summary of the clinical assessment or diagnosis based on the information in the transcript.

15. PLAN
    - Outline the proposed management plan, including treatments, medications, follow-up, and patient instructions as discussed.

Please use only the information present in the transcript. If an information is not mentioned or not applicable, state “Not applicable.” Format each section clearly with its heading.
"""

def generate_structured_note(transcript):
    message = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"<START_TRANSCRIPT>\n{transcript}\n<END_TRANSCRIPT>\n"},
    ]

    inputs = tokenizer.apply_chat_template(
        message,
        tokenize=True,
        add_generation_prompt=True,
        return_tensors="pt",
    ).to(model.device)

    outputs = model.generate(
        input_ids=inputs,
        max_new_tokens=2048,
        temperature=0.2,
        top_p=0.85,
        min_p=0.1,
        top_k=20,
        do_sample=True,
        eos_token_id=tokenizer.eos_token_id,
        use_cache=True,
    )

    input_token_len = len(inputs[0])
    generated_tokens = outputs[:, input_token_len:]
    note = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
    if "<START_NOTES>" in note:
       note = note.split("<START_NOTES>")[-1].strip()
    if "<END_NOTES>" in note:
       note = note.split("<END_NOTES>")[0].strip()
    return note

# Example usage
transcript = "Patient is a 45-year-old male presenting with..."
note = generate_structured_note(transcript)
print("\n--- Generated Response ---")
print(note)
print("---------------------------")
```