---
license: apache-2.0
datasets:
- DLI-Lab/DONUT
widget:
  - text: 'A: Hi, Viggo. How are you doing today?\nB: Hey, Yovani. I’m doing all right. Thanks for asking.\nA: No problem. I saw that you left your coffee mug on the counter this morning. Did you forget to take it with you?\nB: Yeah, I did. Thanks for grabbing it for me.\nA: No problem at all. I know how busy you are and I didn’t want you to have to come back for it later.\nB: You’re a lifesaver, Yovani. Seriously, thank you so much.'
  - example_title: 'example 1'
---
A dialogue commonsense reasoner that generates Chain-of-Thought knowledge in a multi-hop manner given a dialogue history. Our DOCTOR is trained with [DONUT](https://huggingface.co/datasets/DLI-Lab/DONUT) which is also available on huggingface. 
## Links for Reference

- **Demo:https://dialoguecot.web.app/** 
- **Repository:https://github.com/kyle8581/DialogueCoT** 
- **Paper:https://arxiv.org/abs/2310.09343** 
- **Point of Contact:mapoout@yonsei.ac.kr** 

![](./figure2_overall.png)
For more details, you can look at our paper [Dialogue Chain-of-Thought Distillation for Commonsense-aware Conversational Agents](https://arxiv.org/abs/2310.09343).
If you find the following model helpful, please consider citing our paper!

**BibTeX:**
```bibtex
@misc{chae2023dialogue,
      title={Dialogue Chain-of-Thought Distillation for Commonsense-aware Conversational Agents}, 
      author={Hyungjoo Chae and Yongho Song and Kai Tzu-iunn Ong and Taeyoon Kwon and Minjin Kim and Youngjae Yu and Dongha Lee and Dongyeop Kang and Jinyoung Yeo},
      year={2023},
      eprint={2310.09343},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```