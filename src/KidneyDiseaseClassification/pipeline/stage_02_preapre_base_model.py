from KidneyDiseaseClassification.config.configuration import ConfigurationManager
from KidneyDiseaseClassification.components.prepare_base_model import PrepareBaseModel
from KidneyDiseaseClassification.utils.logger import logger
from KidneyDiseaseClassification.utils.exception import CustomException
import sys

STAGE_NAME = "Prepare Base Model stage"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<\n\nX===========X")
    except Exception as e:
        raise CustomException(e,sys)