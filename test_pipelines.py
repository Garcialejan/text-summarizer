import sys
from src.text_summarizer.logging import logger
from src.text_summarizer.exception.exception import TextSummarizerException

from src.text_summarizer.pipeline.stage1_data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.text_summarizer.pipeline.stage2_data_transformation_pipeline import DataTransformationTrainingPipeline
from src.text_summarizer.pipeline.stage3_model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.text_summarizer.pipeline.stage4_model_evaluation_pipeline import ModelEvaluationTrainingPipeline


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


STAGE_NAME="Model Trainer stage"
try:
    logger.info(f"stage {STAGE_NAME} initiated")
    model_trainer_pipeline = ModelTrainerTrainingPipeline()
    model_trainer_pipeline.initiate_model_trainer()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    raise TextSummarizerException(e, sys)


STAGE_NAME = "Model Evaluation stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evaluation = ModelEvaluationTrainingPipeline()
   model_evaluation.initiate_model_evaluation()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    raise TextSummarizerException(e, sys)