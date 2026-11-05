---
{}
---

# Reward Model Overview

<!-- Provide a quick summary of what the model is/does. -->

The reward model is trained from the base model [mistralai/Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2). 

The training script is available at https://github.com/WeiXiongUST/RLHF-Reward-Modeling .

Also see a short blog for the training details (data mixture, parameters...): https://www.notion.so/Reward-Modeling-for-RLHF-abe03f9afdac42b9a5bee746844518d0


## Model Details

If you have any question with this reward model and also any question about reward modeling, feel free to drop me an email with wx13@illinois.edu. I would be happy to chat!

### Dataset preprocessing

<!-- Provide a longer summary of what this model is. -->

The model is trained on a mixture of the following datasets. We also provide the mixture in [weqweasdas/preference_dataset_mixture2_and_safe_pku](https://huggingface.co/datasets/weqweasdas/preference_dataset_mixture2_and_safe_pku).
- [HH-RLHF](https://huggingface.co/datasets/Anthropic/hh-rlhf)
- [SHP](https://huggingface.co/datasets/stanfordnlp/SHP)
- [UltraFeedback](https://huggingface.co/datasets/openbmb/UltraFeedback)
- [Capybara](argilla/distilabel-capybara-dpo-7k-binarized)
- [HelpSteer](https://huggingface.co/datasets/nvidia/HelpSteer)
- [Orca](argilla/distilabel-intel-orca-dpo-pairs)

Difference between this mixture and the original dataset

- HH-RLHF: we only use the helpful subset and we delete the noisy samples where chosen_response == rejected_response;
- SHP: we only use the samples with score ratio > 2, for each prompt, we take 5 comparison at most, leading to 109526;
- Ultrafeedback: similar to UltraFeedback-Binarized, we use the fine-grained score instead of the overall one to rank samples. Meanwhile, for each prompt, we take all possible 6 pairs of comparisons. Finally, we delete the selected pairs with equal scores, leading to 267416.
- HelpSteer: we use the mean of helpfulness and correctness to rank samples. Meanwhile, we take all possible 6 pairs of comparisons. Finally, we delete the selected pairs with equal scores, leading to 21576;


### Training

We train the model for one epoch with a learning rate of 5e-6, batch size 512, cosine learning rate decay with a warmup ratio 0.03.



## Uses

```python
  from transformers import AutoTokenizer, pipeline
  rm_tokenizer = AutoTokenizer.from_pretrained("weqweasdas/RM-Mistral-7B")
  device = 0 # accelerator.device
  rm_pipe = pipeline(
      "sentiment-analysis",
      model="weqweasdas/RM-Mistral-7B",
      #device="auto",
      device=device,
      tokenizer=rm_tokenizer,
      model_kwargs={"torch_dtype": torch.bfloat16}
  )

  pipe_kwargs = {
      "return_all_scores": True,
      "function_to_apply": "none",
      "batch_size": 1
  }

  chat = [
   {"role": "user", "content": "Hello, how are you?"},
   {"role": "assistant", "content": "I'm doing great. How can I help you today?"},
   {"role": "user", "content": "I'd like to show off how chat templating works!"},
  ]

  test_texts = [tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=False).replace(tokenizer.bos_token, "")]
  pipe_outputs = rm_pipe(test_texts, **pipe_kwargs)
  rewards = [output[0]["score"] for output in pipe_outputs]
```

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->



## Results

The reward model ranks 2nd in the [RewardBench](https://huggingface.co/spaces/allenai/reward-bench)


## Reference

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->

The repo was part of the iterative rejection sampling fine-tuning and iterative DPO. If you find the content of this repo useful in your work, please consider cite it as follows:


```
@article{dong2023raft,
  title={Raft: Reward ranked finetuning for generative foundation model alignment},
  author={Dong, Hanze and Xiong, Wei and Goyal, Deepanshu and Pan, Rui and Diao, Shizhe and Zhang, Jipeng and Shum, Kashun and Zhang, Tong},
  journal={arXiv preprint arXiv:2304.06767},
  year={2023}
}

@misc{xiong2024iterative,
      title={Iterative Preference Learning from Human Feedback: Bridging Theory and Practice for RLHF under KL-Constraint}, 
      author={Wei Xiong and Hanze Dong and Chenlu Ye and Ziqi Wang and Han Zhong and Heng Ji and Nan Jiang and Tong Zhang},
      year={2024},
      eprint={2312.11456},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}
```



