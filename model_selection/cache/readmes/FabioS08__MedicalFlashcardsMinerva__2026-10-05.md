---
license: gpl-3.0
datasets:
- medalpaca/medical_meadow_medical_flashcards
pipeline_tag: question-answering
---
# Model Description
This is a fine-tuned version of the Minerva model, trained on the [Medical Meadow Flashcard Dataset](https://huggingface.co/datasets/medalpaca/medical_meadow_medical_flashcards) for question answering. The model was developed by the Sapienza NLP Team in collaboration with Future Artificial Intelligence Research (FAIR) and CINECA; specifically, I used the version with 350 million parameters due to computational limits, though versions with 1 billion and 3 billion parameters also exist. For more details, please refer to their repositories: [Sapienza NLP on Hugging Face](https://huggingface.co/sapienzanlp) and [Minerva LLMs](https://nlp.uniroma1.it/minerva/).
<br>
# Issues and possible Solutions
- In the original fine-tuned version, my model tended to generate answers that continued unnecessarily, leading to repeated sentences and a degradation in quality over time. Parameters like '*max_length*' or '*max_new_tokens*' were ineffective as they merely stopped the generation at a specified point without properly concluding the sentence. To address this issue, I redefined the stopping criteria to terminate the generation at the first period ('.'), as demonstrated in the code below:
- ```python
  class newStoppingCriteria(StoppingCriteria):

    def __init__(self, stop_word):
        self.stop_word = stop_word

    def __call__(self, input_ids, scores, **kwargs):

        decoded_text = tokenizer.decode(input_ids[0], skip_special_tokens=True)
        return self.stop_word in decoded_text


  criteria = newStoppingCriteria(stop_word = ".")
  stoppingCriteriaList = StoppingCriteriaList([criteria])
  ```
<br>

- Since the preprocessed text was formatted as "BoS token - Question - EoS token - BoS token - Answer - EoS token," the model generated answers that included the question as well. To resolve this, I implemented a method to remove the question from the generated text, leaving only the answer:

- ```python
  outputText = tokenizer.decode(output_ids[0], skip_special_tokens = True)
  inputText = tokenizer.decode(inputEncoding.input_ids[0], skip_special_tokens = True)
  answer = outputText[len(inputText):].strip()
  ```
<br>

# Use Example

```python
  question = 'What causes Wernicke encephalopathy?'

  inputEncoding = tokenizer(question, return_tensors = 'pt').to('cuda')
  output_ids = model.generate(
    
      inputEncoding.input_ids, 
      max_length = 128, 
      do_sample = True, 
      temperature = 0.7, 
      top_p = 0.97, 
      top_k = 2, 
      pad_token_id = tokenizer.eos_token_id,
      repetition_penalty = 1.2,
      stopping_criteria = stoppingCriteriaList  
  )

  outputText = tokenizer.decode(output_ids[0], skip_special_tokens = True)
  inputText = tokenizer.decode(inputEncoding.input_ids[0], skip_special_tokens = True)
  answer = outputText[len(inputText):].strip()

  # Generated Answer: Wernicke encephalopathy is caused by a defect in the Wern-Herxheimer reaction, which leads to an accumulation of acid and alkaline phosphatase activity.
  # Effective Answer: The underlying pathophysiologic cause of Wernicke encephalopathy is thiamine (B1) deficiency.
  ```
<br>

# Training Information
The model was fine-tuned for 3 epochs using the parameters specified in its original repository:

```python
  trainingArgs = TrainingArguments(

    output_dir = "MedicalFlashcardsMinerva",
    evaluation_strategy = "steps",
    save_strategy = "steps",
    learning_rate = 2e-4,
    per_device_train_batch_size = 6,
    per_device_eval_batch_size = 6,
    gradient_accumulation_steps = 8,
    num_train_epochs = 3,
    lr_scheduler_type = "cosine",
    warmup_ratio = 0.1,
    adam_beta1 = 0.9,
    adam_beta2 = 0.95,
    adam_epsilon = 1e-8,
    weight_decay = 0.01,
    logging_steps = 100,
    report_to = "none",

    )
  ```