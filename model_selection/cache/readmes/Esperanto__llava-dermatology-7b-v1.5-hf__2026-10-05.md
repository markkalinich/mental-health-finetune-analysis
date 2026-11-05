---
library_name: transformers
tags: []
---

# Model Card for Model ID





## Model Details
Fine tuned version of LLaVA 7B through transfer learning on Dermatology Images.


### Model Description

Given the rise in demand for reliable and immediate medical advice, particularly in dermatology, this tool empowers users to consult an "online dermatologist" by providing essential information, an image of the affected area, and asking follow-up questions, closely mimicking an actual consultation.

To achieve this, we fine-tuned LLaVA 7B with LoRA on the Skin Condition Image Network (SCIN) dataset, equipping it with the ability to process and analyze user-provided images, such as rashes, inflammations, or other skin conditions, and give patients diagnoses with high accuracy.

- **Developed by:** Esperanto Technologies
- **Finetuned from model:** llava-hf/llava-1.5-7b-hf
- **Blog:** Updating soon

## Uses

Put the information in the demo questionnaire together and form context such as:

'This is a CLOSE UP picture of a patient's skin problem. The patient is within the age group of AGE 18 TO 29. The patient is a MALE. The patient is Hispanic Latino or Spanish Origin.  The texture of the skin problem is flat, rough or flaky.  The skin problem comes with increasing size, itching and burning symptoms. The skin problem comes with pain. The skin problem doesn't come with other symptoms. The patient's skin problem has been ONE TO FOUR WEEKS.'
 
 Along with system prompt and user question like "Please diagnose what skin condition is most likely in the picture."
