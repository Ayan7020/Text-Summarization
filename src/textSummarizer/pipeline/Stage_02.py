from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.components.data_validation import DataValidation
from textSummarizer.logging import logger


STAGE_NAME = "DATA Validation STAGE" 

class Data_validation_Pipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_file_exist()
        except Exception as e:
            raise e
        
        
if __name__=="__main__":
    try:
        logger.info(f">>>>Stage {STAGE_NAME} started <<<<")      
        obj = Data_validation_Pipeline()
        obj.main() 
        logger.info(f">>>>Stage {STAGE_NAME} Completed <<<<\n\nx===============x")    
    except Exception as e:
        logger.info(e)
        raise e    
            