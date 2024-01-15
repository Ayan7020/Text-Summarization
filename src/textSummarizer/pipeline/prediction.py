from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline  

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_eval_config()
        
    def predict(self,text):
        tokenixer = AutoTokenizer.from_pretrained(self.config.token_path)    
        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}
        
        pipe = pipeline("summarization",model=self.config.model_path,tokenizer=tokenixer)
         
         
        output = pipe(text,**gen_kwargs)[0]['summary_text']
        print(output)
        
        return output

text = """Amanda: I baked  cookies. Do you want some?
Jerry: Sure!
Amanda: I'll bring you tomorrow :-)",Amanda baked cookies and will bring Jerry some tomorrow.
13728867,"Olivia: Who are you voting for in this election? 
Oliver: Liberals as always.
Olivia: Me too!!
Oliver: Great",Olivia and Olivier are voting for liberals in this election. """ 

        