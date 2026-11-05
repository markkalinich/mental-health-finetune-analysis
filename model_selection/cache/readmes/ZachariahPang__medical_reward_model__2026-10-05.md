---
library_name: transformers
base_model:
- facebook/opt-350m
pipeline_tag: text-classification
---


This is the official reward model developed in the paper "[Expert of Experts Verification and Alignment (EVAL) Framework for Large Language Models Safety in Gastroenterology](https://www.nature.com/articles/s41746-025-01589-z)".

To load the model from huggingface:

```
from transformers import pipeline

grader = pipeline(
        "text-classification",
        model="ZachariahPang/medical_reward_model",
        truncation=True,
        max_length=2048,
    )
```

The model was trained using the template `Question: <question> Answer: <answer>`. To ensure best performance, make sure to use the same format for the input. You can use our helper functions `grade()` for scoring individual answers or `rejection_sampling()` for selecting the best answer from multiple candidates.

Example usage:

```
def format_input(question: str | list[str], answer: str | list[str]) -> list[str]:
    if isinstance(question, str):
        question = [question]
    if isinstance(answer, str):
        answer = [answer]
    assert len(question) == len(answer), "question and answer must have the same length"
    return [f"Question: {q} Answer: {a}" for q, a in zip(question, answer)]
```

To grade one or several question-answer pairs, first load the model and then:
```
def grade(question: str|list[str], answer: str|list[str], grader: pipeline) -> list[float]:
    """Grade one or multiple question-answer pairs using the reward model.

    Args:
        question (str|list[str]): Either a single question string or a list of questions
        answer (str|list[str]): Either a single answer string or a list of answers.
            If lists are provided, their length must match the questions list,
            and the order should correspond (i.e., questions[i] pairs with answers[i])
        grader (pipeline): The loaded reward model pipeline

    Returns:
        list[float]: A list of labels ("positive" or "negative") for each Q&A pair
    """
    inputs = format_input(question, answer)
    outputs = grader(inputs)
    return [output["label"] for output in outputs]
```

To do rejection sampling with the reward model to get the best answer, first load the model and then:
```
def rejection_sampling(
    question: str, answer_candidates: list[str], grader: pipeline
) -> str:
    """Select the best answer from candidates using the reward model scores.

    Args:
        question (str): The input question to find the best answer for
        answer_candidates (list[str]): List of potential answers to choose from
        grader (pipeline): The loaded reward model pipeline

    Returns:
        str: The answer with the highest positive score from the candidates
    """
    questions = [question] * len(answer_candidates)
    inputs = format_input(questions, answer_candidates)
    outputs = grader(inputs)
    positive_score = []
    # `score` is the probability of the answer towards the question being `label`
    # convert all scores to "positive" scores to be used for argmax
    for output in outputs:
        if output["label"] == "positive":
            positive_score.append(output["score"])
        if output["label"] == "negative":
            positive_score.append(1 - output["score"])
    return answer_candidates[np.argmax(positive_score)]
```
