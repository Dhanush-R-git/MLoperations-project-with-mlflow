from MLproject import logger
from MLproject.pipeline.stage_01_Data_Ingestion import DataIngestionTrainingPipeline
from MLproject.pipeline.stage_02_Data_Validation import DataValidationTrainingPipeline
from MLproject.pipeline.stage_03_Data_Transformation import DataTransformationTrainingPipeline
from MLproject.pipeline.stage_04_Model_Trainer import ModelTrainerTrainingPipeline
from MLproject.pipeline.stage_05_Model_Evaluation import ModelEvaluationTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n=========================================================================")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data validation stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n--------------------------------------------------------------------------")
except Exception as e:
    logger.exception(e)
    raise e
    

STAGE_NAME = "Data transfromation stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n..........................................................................")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Training stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n**************************************************************************")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
except Exception as e:
    logger.exception(e)
    raise e
