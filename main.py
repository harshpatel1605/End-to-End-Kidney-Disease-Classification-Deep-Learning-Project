import sys
from KidneyDiseaseClassification.utils.logger import logger
from KidneyDiseaseClassification.utils.exception import CustomException
from KidneyDiseaseClassification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from KidneyDiseaseClassification.pipeline.stage_02_preapre_base_model import PrepareBaseModelTrainingPipeline



STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nX===========X")
except Exception as e:
    raise CustomException(e,sys)


STAGE_NAME = "Prepare Base Model stage"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nX===========X")
    except Exception as e:
        raise CustomException(e,sys)