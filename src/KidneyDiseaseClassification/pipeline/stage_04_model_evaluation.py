from KidneyDiseaseClassification.config.configuration import ConfigurationManager
from KidneyDiseaseClassification.components.model_evaluation import Evaluation

from KidneyDiseaseClassification.utils.logger import logger
from KidneyDiseaseClassification.utils.exception import CustomException
import sys

STAGE_NAME = "Model Evaluation "

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config  = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation  = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<<<\n\nX===========X")
    except Exception as e:
        raise CustomException(e,sys)