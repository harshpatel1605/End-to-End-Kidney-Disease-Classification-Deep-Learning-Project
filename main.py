import sys
from KidneyDiseaseClassification.utils.logger import logger
from KidneyDiseaseClassification.utils.exception import CustomException
from KidneyDiseaseClassification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nX===========X")
except Exception as e:
    raise CustomException(e,sys)