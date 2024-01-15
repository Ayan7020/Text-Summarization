from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path
    
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: Path
    ALL_REQUIRED_FILES: list    
    

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path  
    
    
@dataclass(frozen=True)    
class ModelTrainerConfig:
    root_dir: Path
    data_path: Path
    model_name: Path
    Num_epochs: int 
    per_device_train_batch_size: int
    per_device_eval_batch_size: int
    weight_decay: float 
    evaluation_strategy: str
    metric_for_best_model: str
    gradient_accumulation_steps: int 
    
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    data_path: Path
    model_path: Path
    token_path: Path
    metric_file_name: Path            