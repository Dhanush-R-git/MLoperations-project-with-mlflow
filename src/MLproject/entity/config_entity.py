from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
   root_dir: Path #root_dir: 'artifacts/data_ingestion'
   source_URL: str #'artifacts/data_ingestion/data.zip'
   local_data_file: Path
   unzip_dir: Path #'artifacts/data_ingestion'
   

# Data class called DataIngestionConfig is used to store configuration settings [config.yaml] file for the data ingestion process in a structured way.
'''
@dataclass(frozen=True): The frozen=True parameter makes the instances of this class immutable, meaning their fields cannot be modified after they are created.
root_dir: The root directory for data ingestion, specified as a Path object.
source_URL: The URL from which the data will be downloaded, specified as a string.
local_data_file: The local path where the downloaded data file will be saved, specified as a Path object.
unzip_dir: The directory where the data will be unzipped, specified as a Path object.

'''
@dataclass(frozen=True)
class DataValidationConfig:
   root_dir: Path
   STATUS_FILE: str
   unzip_data_dir: Path
   all_schema: dict


@dataclass(frozen=True)
class DataTransformationConfig:
   root_dir: Path
   data_path: Path


@dataclass(frozen=True)
class ModelTrainerConfig:
   root_dir: Path
   train_data_path: Path
   test_data_path: Path
   model_name: str
   alpha: float
   l1_ratio: float
   target_column: str


@dataclass(frozen=True)
class ModelEvaluationConfig:
   root_dir: Path
   test_data_path: Path
   model_path: Path
   all_params: dict
   metric_file_name: Path
   target_column: str
   mlflow_uri: str