from KidneyDiseaseClassification.config.configuration import ConfigurationManager
from KidneyDiseaseClassification.components.data_ingestion import DataIngestion
from KidneyDiseaseClassification.utils.logger import logger
from KidneyDiseaseClassification.utils.exception import CustomException
import sys

STAGE_NAME = "Data Inegstion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<\n\nX===========X")
    except Exception as e:
        raise CustomException(e,sys)