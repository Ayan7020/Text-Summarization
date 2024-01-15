
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_from_disk
from textSummarizer.entity import ModelTrainerConfig
import os



class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
        
        
    def train(self):
        tokenixer = AutoTokenizer.from_pretrained(self.config.model_name) 
        model =  AutoModelForSeq2SeqLM.from_pretrained(self.config.model_name)  
        
        seq2seqdatacollector = DataCollatorForSeq2Seq(tokenixer,model=model)
        
        dataset_samsum = load_from_disk(self.config.data_path)
        
        trainer_args = TrainingArguments(
            output_dir='pegasus-samsum',evaluation_strategy=self.config.evaluation_strategy,
            save_strategy = self.config.evaluation_strategy,load_best_model_at_end=True,
            metric_for_best_model=self.config.metric_for_best_model, 
            num_train_epochs=self.config.Num_epochs,
            per_device_train_batch_size=self.config.per_device_train_batch_size, per_device_eval_batch_size=self.config.per_device_eval_batch_size,
            weight_decay=self.config.weight_decay,  
            gradient_accumulation_steps=self.config.gradient_accumulation_steps
        )
        
        trainer = Trainer(model=model,args=trainer_args,
                          tokenizer=tokenixer,data_collator=seq2seqdatacollector,
                          train_dataset=dataset_samsum['train'],
                          eval_dataset=dataset_samsum['validation']
                          )
        
        trainer.train() 
        
        model.save_pretrained(os.path.join(self.config.root_dir,"bart model")) 
        tokenixer.save_pretrained(os.path.join(self.config.root_dir,"tokenixer")) 