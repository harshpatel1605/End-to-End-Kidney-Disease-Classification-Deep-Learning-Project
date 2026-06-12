import sys
from KidneyDiseaseClassification.utils.logger import logger
from KidneyDiseaseClassification.utils.exception import CustomException
from KidneyDiseaseClassification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from KidneyDiseaseClassification.pipeline.stage_02_preapre_base_model import PrepareBaseModelTrainingPipeline
from KidneyDiseaseClassification.pipeline.stage_03_model_training import ModelTrainingPipeline
from KidneyDiseaseClassification.pipeline.stage_04_model_evaluation import EvaluationPipeline




STAGE_NAME = "Data Ingestion"
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nX===========X")
except Exception as e:
    logger.exception(e)
    raise CustomException(e,sys)


STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f"**************************")
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nX===========X")
except Exception as e:
    logger.exception(e)
    raise CustomException(e,sys)
    

STAGE_NAME = "Model Training"
try:
    logger.info(f"**************************")
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<<<\n\nX===========X")
except Exception as e:
    logger.exception(e)
    raise CustomException(e,sys)


STAGE_NAME = "Model Evaluation"
try:
    logger.info(f"**************************")
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<<<\n\nX===========X")
except Exception as e:
    logger.exception(e)
    raise CustomException(e,sys)

