from textSummarizer.config.configuration import ConfigurationManager 
from textSummarizer.components.model_trainer import ModelTrainer
from textSummarizer.logging import logger


STAGE_NAME = "Model Training STAGE" 

class Model_trainer_pipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_config()
            model_trainer_config = ModelTrainer(config=model_trainer_config)
            model_trainer_config.train()
        except Exception as e:
            raise e 
        
        
if __name__=="__main__":
    try:
        logger.info(f">>>>Stage {STAGE_NAME} started <<<<")      
        obj = Model_trainer_pipeline()
        obj.main() 
        logger.info(f">>>>Stage {STAGE_NAME} Completed <<<<\n\nx===============x")    
    except Exception as e:
        logger.info(e)
        raise e    
            