from textSummarizer.config.configuration import ConfigurationManager 
from textSummarizer.components.model_Eval import ModelEvaluation
from textSummarizer.logging import logger


STAGE_NAME = "Model Evaluation STAGE" 

class Model_Evaluation_Pipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_eval_config()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_config.evaluate()
        except Exception as e:
            raise e
        
        
if __name__=="__main__":
    try:
        logger.info(f">>>>Stage {STAGE_NAME} started <<<<")      
        obj = Model_Evaluation_Pipeline()
        obj.main() 
        logger.info(f">>>>Stage {STAGE_NAME} Completed <<<<\n\nx===============x")    
    except Exception as e:
        logger.info(e)
        raise e    
            