
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_from_disk, load_metric 
import pandas as pd
from tqdm import tqdm
from textSummarizer.entity import ModelEvaluationConfig


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        
    def generate_batch_sixe_chunk(self,list_of_element,batch_sixe):
            for i in range(0,len(list_of_element),batch_sixe):
                yield list_of_element[i : i+batch_sixe]
                
    def calculate_metric_on_test(self,dataset,metric,model,tokenixer,batch_sixe=16,column_text="article",column_summary="highlights"):
        article_batch = list(self.generate_batch_sixe_chunk(dataset[column_text], batch_sixe))
        target_batch =  list(self.generate_batch_sixe_chunk(dataset[column_summary], batch_sixe))     
        
        for article_batch,target_batch in tqdm(zip(article_batch, target_batch), total=len(article_batch)):
            inputs = tokenixer(article_batch,max_length=1024,truncation=True,padding="max_length",return_tensors="pt") 
            summaries = model.generate(input_ids=inputs["input_ids"],attention_mask=inputs["attention_mask"],length_penalty=0.8, num_beams=8, max_length=128)
            decoded_sum = [tokenixer.decode(s,skip_special_tokens=True,clean_up_tokenization_spaces=True) for s in summaries] 
            decoded_sum = [d.replace(""," ") for d in decoded_sum] 
            metric.add_batch(predictions=decoded_sum,references=target_batch)  
            
            score = metric.compute()
            return score
        
    def evaluate(self):
        tokenixer = AutoTokenizer.from_pretrained(self.config.token_path)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path)   
        
        dataset_samsum_pt = load_from_disk(self.config.data_path)
        rouge_names = ["rouge1", "rouge2", "rougeL", "rougeLsum"]
        rouge_metric = load_metric('rouge')
        
        score = self.calculate_metric_on_test(
            dataset_samsum_pt['test'][0:10],rouge_metric,model,tokenixer,batch_sixe=2,column_text = 'dialogue', column_summary= 'summary'
        ) 
        
        rouge_dict = dict((n,score[n].mid.fmeasure)for n in rouge_names)
        
        df = pd.DataFrame(rouge_dict, index = ['bart_model'] )
        df.to_csv(self.config.metric_file_name, index=False)