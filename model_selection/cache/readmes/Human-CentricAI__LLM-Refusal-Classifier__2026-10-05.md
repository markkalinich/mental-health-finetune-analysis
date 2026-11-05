---
license: cc-by-nc-4.0
---
(Note: Updated Model uploaded on 2025.07.28)

This model is a fine-tuned version of RoBERTa-large [1]. It was trained on 2,450 LLM responses from Chatbot Arena [2]. The model classifies whether a response is a refusal or a disclaimer and identifies the reason behind the refusal/disclaimer: (i) ethical concerns or (ii) lack of technical capabilities, information, or context.


The model assigns one of five possible labels:

0 (**normal**): No refusal or disclaimer; the model provides a standard, straightforward answer <br />
1 (**Refusal Unethical**): The model refuses to answer for ethical reasons, such as legal, moral, inappropriate, or safety-related concerns <br />
2 (**Disclaimer Unethical**): The model cites ethical concerns but still attempts to conduct the task/question of the prompt  <br />
3 (**Refusal Capability**): The model refuses to answer due to its own limitations, lack of information, or lack of ability to provide an adequate response. <br />
4 (**Disclaimer Capability**): The model signals its limitations but attempts to provide an answer within its capacity  <br />

Please cite: <br /> Pasch, S. (2026). LLM content moderation and user satisfaction: evidence from response refusals in Chatbot Arena. Behaviour & Information Technology, 45(10), 2007–2031. https://doi.org/10.1080/0144929X.2025.2565668. 

References <br />
[1] Liu, Y.; Ott, M.; Goyal, N.; Du, J.; Joshi, M.; Chen, D.; ... & Stoyanov, V. (2019). Roberta: A robustly optimized bert pretraining approach. arXiv preprint arXiv:1907.11692. <br />
[2] Chiang, W. L., Zheng, L., Sheng, Y., Angelopoulos, A. N., Li, T., Li, D., ... & Stoica, I. (2024). Chatbot arena: An open platform for evaluating llms by human preference. arXiv preprint arXiv:2403.04132.