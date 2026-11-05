---
license: apache-2.0
language:
- en
tags:
- moe
- merge
---

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6589d7e6586088fd2784a12c/IJUYoGvKtUF8O0as3hLMM.png)

# "[We] are joined by the bonds of love. And you cannot track that, not with a thousand bloodhounds, and you cannot break it, not with a thousand swords."
[GGUF FILES HERE](https://huggingface.co/Kquant03/NurseButtercup-4x7B-GGUF)

[Join our Discord!](https://discord.gg/uT4CzytfYW)

Going to try a laser scan of this model with Fernando from Cognitive Computations. It is a FrankenMoE.

The config looks like this...(detailed version is in the files and versions):
- [macadeliccc/WestLake-7B-v2-laser-truthy-dpo](https://huggingface.co/macadeliccc/WestLake-7B-v2-laser-truthy-dpo) - base
- [macadeliccc/WestLake-7B-v2-laser-truthy-dpo](https://huggingface.co/macadeliccc/WestLake-7B-v2-laser-truthy-dpo) - expert #1
- [cognitivecomputations/samantha-1.1-westlake-7b-laser](https://huggingface.co/cognitivecomputations/samantha-1.1-westlake-7b-laser) - expert #2
- [macadeliccc/WestLake-7B-v2-laser-truthy-dpo](https://huggingface.co/macadeliccc/WestLake-7B-v2-laser-truthy-dpo) - expert #3
- [BioMistral/BioMistral-7B](https://huggingface.co/BioMistral/BioMistral-7B) - expert #4

# Will upload to eval eventually.

# "[What is a Mixture of Experts (MoE)?](https://huggingface.co/blog/moe)"
### (from the MistralAI papers...click the quoted question above to navigate to it directly.)

The scale of a model is one of the most important axes for better model quality. Given a fixed computing budget, training a larger model for fewer steps is better than training a smaller model for more steps.

Mixture of Experts enable models to be pretrained with far less compute, which means you can dramatically scale up the model or dataset size with the same compute budget as a dense model. In particular, a MoE model should achieve the same quality as its dense counterpart much faster during pretraining.

So, what exactly is a MoE? In the context of transformer models, a MoE consists of two main elements:

    Sparse MoE layers are used instead of dense feed-forward network (FFN) layers. MoE layers have a certain number of “experts” (e.g. 32 in my "frankenMoE"), where each expert is a neural network. In practice, the experts are FFNs, but they can also be more complex networks or even a MoE itself, leading to hierarchical MoEs!
    
    A gate network or router, that determines which tokens are sent to which expert. For example, in the image below, the token “More” is sent to the second expert, and the token "Parameters” is sent to the first network. As we’ll explore later, we can send a token to more than one expert. How to route a token to an expert is one of the big decisions when working with MoEs - the router is composed of learned parameters and is pretrained at the same time as the rest of the network.

At every layer, for every token, a router network chooses two of these groups (the “experts”) to process the token and combine their output additively.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6589d7e6586088fd2784a12c/up_I0R2TQGjqTShZp_1Sz.png)

Switch Layer
MoE layer from the [Switch Transformers paper](https://arxiv.org/abs/2101.03961)

So, to recap, in MoEs we replace every FFN layer of the transformer model with an MoE layer, which is composed of a gate network and a certain number of experts.

Although MoEs provide benefits like efficient pretraining and faster inference compared to dense models, they also come with challenges:

    Training: MoEs enable significantly more compute-efficient pretraining, but they’ve historically struggled to generalize during fine-tuning, leading to overfitting.
    Inference: Although a MoE might have many parameters, only some of them are used during inference. This leads to much faster inference compared to a dense model with the same number of parameters. However, all parameters need to be loaded in RAM, so memory requirements are high. For example, [given a MoE like Mixtral 8x7B](https://huggingface.co/blog/moe), we’ll need to have enough VRAM to hold a dense 47B parameter model. Why 47B parameters and not 8 x 7B = 56B? That’s because in MoE models, only the FFN layers are treated as individual experts, and the rest of the model parameters are shared. At the same time, assuming just two experts are being used per token, the inference speed (FLOPs) is like using a 12B model (as opposed to a 14B model), because it computes 2x7B matrix multiplications, but with some layers shared (more on this soon).

If all our tokens are sent to just a few popular experts, that will make training inefficient. In a normal MoE training, the gating network converges to mostly activate the same few experts. This self-reinforces as favored experts are trained quicker and hence selected more. To mitigate this, an auxiliary loss is added to encourage giving all experts equal importance. This loss ensures that all experts receive a roughly equal number of training examples. The following sections will also explore the concept of expert capacity, which introduces a threshold of how many tokens can be processed by an expert. In transformers, the auxiliary loss is exposed via the aux_loss parameter.


## "Wait...but you called this a frankenMoE?"
The difference between MoE and "frankenMoE" lies in the fact that the router layer in a model like the one on this repo is not trained simultaneously.