---
license: cc-by-nc-4.0
library_name: transformers
pipeline_tag: text-generation
datasets:
- Psychotherapy-LLM/PsychoCounsel-Preference
base_model:
- meta-llama/Llama-3.1-8B-Instruct
---

The reward model presented in the paper [Preference Learning Unlocks LLMs' Psycho-Counseling Skills](https://hf.co/papers/2502.19731).  It's a fine-tuned [meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) model trained using preference learning on the [PsychoCounsel-Preference](https://huggingface.co/datasets/Psychotherapy-LLM/PsychoCounsel-Preference) dataset.
This policy model, [PsychoCounsel-Llama3-8B](https://huggingface.co/Psychotherapy-LLM/PsychoCounsel-Llama3-8B), trained with this model with online preference learning, achieves an impressive win rate of 87% against GPT-4o in psycho-counseling tasks.



# Usage:
## Step 1: Install Dependencies
torch==2.5.1, transformers==4.46.3, openrlhf==0.5.7.dev0


## Step 2: Serve Reward Model
```sh
export CUDA_DEVICE_ORDER=PCI_BUS_ID  
export CUDA_VISIBLE_DEVICES=0
python -m openrlhf.cli.serve_rm \
    --reward_pretrain [replace with the model path] \
    --port 5000 \
    --bf16 \
    --flash_attn \
    --max_len 2048 \
    --batch_size 8
```

## Step 3: Get Rewards
```python
def evaluate_openrlhf_rm(model_name):
    from openrlhf.models import get_llm_for_sequence_regression
    from openrlhf.utils import get_tokenizer
    model = get_llm_for_sequence_regression(model_name, "reward", normalize_reward=True, bf16=True)
    tokenizer = get_tokenizer(model_name, model, "left")
    
    import requests

    url = "http://0.0.0.0:5000/get_reward"  # Adjust host/port as needed

    data = [
        {
            'chosen': [
                {'role': 'user', 'content': "(Nods, wiping away tears) I've been so focused on my friendships that I've neglected other areas of my life. I've been feeling increasingly isolated and disconnected from my family, and I've been struggling to maintain a romantic relationship. I've been so consumed by my friendships that I've forgotten how to build and maintain other relationships."}, 
                {'role': 'assistant', 'content': " I'm really sorry to hear that you're feeling this way. It's understandable that you've found comfort and connection in your friendships, especially given the challenges and isolation we all face. However, it's also important to recognize the value and need for a balanced life where you can nurture all areas, including your family and romantic relationships.\n\nFirstly, it's great that you're acknowledging this imbalance. Recognizing that there's an issue is the first step towards addressing it. Here are a few suggestions on how you might start addressing this:\n\n1. Setting boundaries: Spending quality time with your friends doesn't mean neglecting other aspects of your life. Try establishing a routine where you designate specific times for socializing and other times for focusing on your family and relationship.\n\n2. Communication: Communicate your feelings with your family and partner. Let them know that you've been feeling isolated and disconnected and that you want to work on improving those aspects of your life. They may also be experiencing similar feelings and can provide mutual support.\n\n3. Self-care: Focusing on your own wellbeing is essential. This could involve physical activities, meditation, hobbies, or anything that helps you feel more grounded and connected to yourself.\n\n4. Seek professional help: If these feelings persist and start affecting your mental health, it might be worth seeking help from a therapist or counselor. They can provide techniques and strategies to manage your feelings of isolation and neglect.\n\n5. Small steps: Remember that change takes time. Start small, with one or two relationships at a time. This could involve scheduling regular get-togethers with your family, or having a heart-to-heart talk with your partner.\n\n6. Appreciate your friendships: Remember, your friendships are valuable. They have contributed to your growth and resilience. Rather than reducing their time, think of ways to enhance these relationships, so they can coexist and complement the other aspects of your life.\n\nYou've taken an important step by recognizing this issue and seeking help. Remember, it's okay to feel overwhelmed, and it's important to be patient with yourself. Small changes can lead to significant improvements over time."}
            ], 
            'rejected': [
                {'role': 'user', 'content': "(Nods, wiping away tears) I've been so focused on my friendships that I've neglected other areas of my life. I've been feeling increasingly isolated and disconnected from my family, and I've been struggling to maintain a romantic relationship. I've been so consumed by my friendships that I've forgotten how to build and maintain other relationships."},
                {'role': 'assistant', 'content': "I'm really sorry you're feeling this way. It sounds like your friendships have been a significant focus for you, and while they're important, it's understandable that this might lead to feelings of isolation from your family and challenges in your romantic relationships. Can you tell me more about what's been happening in your friendships and how that's impacting other parts of your life?"}
            ]
        }
    ]
    for row in data:
        chosen_text = tokenizer.apply_chat_template(row['chosen'], tokenize=False)
        rejected_text = tokenizer.apply_chat_template(row['rejected'], tokenize=False)
        response = requests.post(url, json={'query': [chosen_text, rejected_text]}).json()
        chosen_reward, rejected_reward = response['rewards']
        print('chosen reward: ', chosen_reward)
        print('rejected_reward: ', rejected_reward)

model_name = '[replace with the model path]'
evaluate_openrlhf_rm(model_name)

# chosen reward:  -1.5625
# rejected_reward:  -4.21875
```