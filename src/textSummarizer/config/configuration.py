from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories
from textSummarizer.entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,
                 param_filepath =PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.param = read_yaml(param_filepath)
        
        create_directories([self.config.artfacts])
        
    def get_data_ingestion_config(self) ->  DataIngestionConfig:
        config = self.config.data_ingestion
            
        create_directories([config.root_dir]) 
            
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir            
            ) 
            
        return data_ingestion_config
            