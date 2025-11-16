import sys
from src.text_summarizer.logging import logger
from src.text_summarizer.pipeline.stage1_data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.text_summarizer.pipeline.stage2_data_transformation_pipeline import DataTransformationTrainingPipeline
from src.text_summarizer.exception.exception import TextSummarizerException

STAGE_NAME="Data Ingestion stage"
try:
    logger.info(f"stage {STAGE_NAME} initiated")
    data_ingestion_pipeline=DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    raise TextSummarizerException(e, sys)


STAGE_NAME="Data Transformation stage"
try:
    logger.info(f"stage {STAGE_NAME} initiated")
    data_ingestion_pipeline=DataTransformationTrainingPipeline()
    data_ingestion_pipeline.initiate_data_transformation()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    raise TextSummarizerException(e, sys)