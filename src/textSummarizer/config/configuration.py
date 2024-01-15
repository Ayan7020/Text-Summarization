from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories
from textSummarizer.entity import DataIngestionConfig
from textSummarizer.entity import DataValidationConfig
from textSummarizer.entity import DataTransformationConfig
from textSummarizer.entity import ModelTrainerConfig
from textSummarizer.entity import ModelEvaluationConfig

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
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        create_directories([config.root_dir]) 
        
        data_vaidation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES,
        )
        return data_vaidation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])
        
        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_name = config.tokenizer_name
        )
        
        return data_transformation_config 
    
    def get_model_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.Training

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_name = config.model_name,
            Num_epochs = params.Num_epochs, 
            per_device_train_batch_size = params.per_device_train_batch_size,
            per_device_eval_batch_size = params.per_device_eval_batch_size,
            weight_decay = params.weight_decay, 
            evaluation_strategy = params.evaluation_strategy, 
            metric_for_best_model = params.metric_for_best_model,
            gradient_accumulation_steps = params.gradient_accumulation_steps
        )

        return model_trainer_config
    
    def get_model_eval_config(self) -> ModelEvaluationConfig:
        config = self.config.model_eval
        create_directories([config.root_dir])
        
        model_eval_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_path = config.model_path,
            token_path = config.token_path,
            metric_file_name = config.metric_file_name
        )   
        return model_eval_config 
            