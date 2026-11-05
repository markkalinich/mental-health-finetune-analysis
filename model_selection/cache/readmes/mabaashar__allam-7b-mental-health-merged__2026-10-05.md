---
base_model: humain-ai/ALLaM-7B-Instruct-preview
tags:
- text-generation-inference
- transformers
- unsloth
- llama
- trl
license: apache-2.0
language:
- en
- ar
---

# Uploaded  model

- **Developed by:** Mohammed Abdullah Ba'ashar-mabaashar
- **Website:** https://www.bytsnbytes.com
- **License:** apache-2.0
- **Finetuned from model :** humain-ai/ALLaM-7B-Instruct-preview

# Inference 

- On a device with a GPU, run the following code -the code is optimized for kaggle/google colab notebooks:

    ==============================

    !pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
    
    import torch
  
    from unsloth import FastLanguageModel
    
    # 🚀 UPDATE THIS LINE WITH YOUR EXACT HUGGING FACE REPOSITORY
    HF_MODEL_ID = "mabaashar/allam-7b-mental-health-merged" 
    MAX_SEQ_LENGTH = 128
    
    #1)fetching finetuned model from HF
    
    print(f"📥 Fetching fine-tuned ALLaM from Hugging Face Hub: {HF_MODEL_ID}...")
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=HF_MODEL_ID,
        max_seq_length=MAX_SEQ_LENGTH,
        load_in_4bit=True,
        device_map={"": torch.cuda.current_device()}
    )
    
    print("⚡ Switching model over to fast inference mode...")
    FastLanguageModel.for_inference(model) 
    
    # Define your Arabic mental health test prompt
    question = "اشعر بنوبات غضب. ماذا أفعل ؟"
    prompt = f"User: {question}\nAssistant: "
    
    inputs = tokenizer([prompt], return_tensors="pt").to("cuda")
    
    print("\n🧠 Generating response from your fine-tuned ALLaM...")
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=150,     
            use_cache=True,         
            temperature=0.7,        
            top_p=0.9,
            eos_token_id=tokenizer.eos_token_id
        )
    
    # Decode and extract the assistant's response cleanly
    generated_text = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
    response = generated_text.split("Assistant:")[-1].strip()
    
    print("\n================== 🩺 ALLaM Response ==================")
    print(response)
    print("======================================================")
  
    ==============================

#Results

The custom fine-tuning approach significantly improved model accuracy, achieving an 84.21% alignment with dialectal Arabic and successfully
reducing "Modern Standard Arabic leakage" down to just 6.21%, creating a more natural and empathetic tone for therapeutic contexts.

=========
Fine-tuned by Mohammed Abdullah Ba'ashar:

[<img src="https://www.bytsnbytes.com/static/website/logo_prod_2.png" width="200"/>](https://www.bytsnbytes.com)