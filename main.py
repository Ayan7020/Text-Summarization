from textSummarizer.logging import logger

from textSummarizer.pipeline.Stage_01 import Data_ingestion_pipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> Stage {STAGE_NAME} Started <<<<<<<")
    logger.info(f">>>>Stage {STAGE_NAME} started <<<<")
    obj = Data_ingestion_pipeline()
    obj.main()
    logger.info(f">>>>Stage {STAGE_NAME} Completed <<<<\n\nx===============x")
except Exception as e:
    logger.exception(e)
    raise e