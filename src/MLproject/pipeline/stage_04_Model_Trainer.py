from MLproject.config.configuration import ConfigurationManager
from MLproject.components.Model_trainer import ModelTrainer
from MLproject import logger
from pathlib import Path

STAGE_NAME = "Model Training stage"

class ModelTrainerTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n--------------------------------")
    except Exception as e:
        logger.exception(e)
        raise e
    
