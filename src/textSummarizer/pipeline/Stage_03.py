from textSummarizer.config.configuration import ConfigurationManager 
from textSummarizer.components.data_transformation import DataTransformation
from textSummarizer.logging import logger


STAGE_NAME = "DATA Transformation STAGE" 

class Data_Transformation_pipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.convert()
        except Exception as e:
            raise e 
        
        
if __name__=="__main__":
    try:
        logger.info(f">>>>Stage {STAGE_NAME} started <<<<")      
        obj = Data_Transformation_pipeline()
        obj.main() 
        logger.info(f">>>>Stage {STAGE_NAME} Completed <<<<\n\nx===============x")    
    except Exception as e:
        logger.info(e)
        raise e    
            