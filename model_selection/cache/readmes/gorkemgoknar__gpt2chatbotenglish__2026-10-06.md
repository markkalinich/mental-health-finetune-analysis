---
language:
- en
thumbnail:
tags:
- gpt2
- conversational
license: cc-by-4.0
widget:
- text: Hello there
  context: 'Gandalf'
---
# GPT2 Persona Chatbot based on Movie Characters
Model used for https://www.metayazar.com/chatbot

GPT2 Small Trained on movie scripts (especially Sci-fi) 

Usual HF api will not work see HF Spaces for demo usage https://huggingface.co/spaces/gorkemgoknar/moviechatbot


This work is based on Persona Chatbot originally done by Hugging Face team (https://medium.com/huggingface/how-to-build-a-state-of-the-art-conversational-ai-with-transfer-learning-2d818ac26313)

For cleaning movie scripts I also provide cleaner code
https://github.com/gorkemgoknar/moviescriptcleaner

Example persona how to:
https://gist.github.com/gorkemgoknar/ae29bf9d14fa814e6a64d0e57a4a4ed7

Tried a AI job interview over some characters here, details on this post
https://www.linkedin.com/pulse/ai-goes-job-interview-g%C3%B6rkem-g%C3%B6knar/

For obvious reasons I cannot share raw personafile but you can check above gist for example how to create it.

A working "full" demo can be seen in https://www.metayazar.com/chatbot

For Turkish version (with limited training) https://www.metayazar.com/chatbot_tr

Due to double LM head standart hugging face interface will not work. But if you follow huggingface tutorial should be same.
Except each persona is encoded as "My name is XXXX"

Use model, tokenizer and parameters within a class and call in below functions to trigger model.
Some of the available personas:

| Macleod | Moran | Brenda | Ramirez | Peter Parker | Quentin Beck | Andy 
| Red | Norton | Willard | Chief | Chef | Kilgore | Kurtz | Westley | Buttercup 
| Vizzini | Fezzik | Inigo | Man In Black | Taylor | Zira | Zaius | Cornelius 
| Bud | Lindsey | Hippy | Erin | Ed | George | Donna | Trinity | Agent Smith 
| Morpheus | Neo | Tank | Meryl | Truman | Marlon | Christof | Stromboli | Bumstead 
| Schreber | Walker | Korben | Cornelius | Loc Rhod | Anakin | Obi-Wan | Palpatine 
| Padme | Superman | Luthor | Dude | Walter | Donny | Maude | General | Starkiller 
| Indiana | Willie | Short Round | John | Sarah | Terminator | Miller | Sarge | Reiben 
| Jackson | Upham | Chuckie | Will | Lambeau | Sean | Skylar | Saavik | Spock 
| Kirk | Bones | Khan | Kirk | Spock | Sybok | Scotty | Bourne | Pamela | Abbott 


```python
    def get_answer(self, input_text, personality, history, params=None):
        
        ##Check length of history (to save 1 computation!)
        if len(history)>0:
            #mostly it will be empty list so need a length check for performance
            #would do string check also but just assume it is list of list of strings, as not public
            
            new_hist = [] 
            for ele in history:
                new_hist.append( self.tokenizer.encode(ele) )
            history = new_hist.copy()

        history.append(self.tokenizer.encode(input_text))

        with torch.no_grad():
            out_ids = self.sample_sequence(personality, history, self.tokenizer, self.model, params=params)
        history.append(out_ids)
        history = history[-(2*self.parameters['max_history']+1):]
        out_text = self.tokenizer.decode(out_ids, skip_special_tokens=True)
        #print(out_text)


        history_decoded = []
        for ele in history:
            history_decoded.append(self.tokenizer.decode(ele))

        return out_text, history_decoded, self.parameters

```