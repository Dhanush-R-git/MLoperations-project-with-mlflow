from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
   root_dir: Path
   source_URL: str
   local_data_file: Path
   unzip_dir: Path
   print("sucessfully runned")

# Data class called DataIngestionConfig is used to store configuration settings for the data ingestion process in a structured way.
'''
@dataclass(frozen=True): The frozen=True parameter makes the instances of this class immutable, meaning their fields cannot be modified after they are created.
root_dir: The root directory for data ingestion, specified as a Path object.
source_URL: The URL from which the data will be downloaded, specified as a string.
local_data_file: The local path where the downloaded data file will be saved, specified as a Path object.
unzip_dir: The directory where the data will be unzipped, specified as a Path object.

'''