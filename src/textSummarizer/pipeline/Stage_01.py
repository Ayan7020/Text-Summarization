from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.logging import logger


STAGE_NAME = "DATA INGESTION STAGE" 

class Data_ingestion_pipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download()
            data_ingestion.extract()
        except Exception as e:
            raise e
        
        
if __name__=="__main__":
    try:
        logger.info(f">>>>Stage {STAGE_NAME} started <<<<")      
        obj = Data_ingestion_pipeline()
        obj.main() 
        logger.info(f">>>>Stage {STAGE_NAME} Completed <<<<\n\nx===============x")    
    except Exception as e:
        logger.info(e)
        raise e    
            