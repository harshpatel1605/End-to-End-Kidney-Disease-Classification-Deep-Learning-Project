from KidneyDiseaseClassification.config.configuration import ConfigurationManager
from KidneyDiseaseClassification.components.model_training import Training
from KidneyDiseaseClassification.utils.logger import logger
from KidneyDiseaseClassification.utils.exception import CustomException
import tensorflow as tf
import sys

STAGE_NAME = "Model Training"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            logger.info(
                f"Available GPUs: {tf.config.list_physical_devices('GPU')}"
            )

            config = ConfigurationManager()
            training_config = config.get_training_config()

            training = Training(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train()

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")

        obj = ModelTrainingPipeline()
        obj.main()

        logger.info(f">>>>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<<<\n\nX===========X")

    except Exception as e:
        raise CustomException(e, sys)