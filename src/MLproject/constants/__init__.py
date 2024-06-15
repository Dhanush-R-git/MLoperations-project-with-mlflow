from pathlib import Path

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")
SCHEMA_FILE_PATH = Path("schema.yaml")

# constants\__init__.py likely contains constant definitions such as file paths. 

'''
By centralizing these constants, the code becomes more maintainable, easier to read, 
and less error-prone. If a value needs to be updated, 
it can be changed in one place rather than having to search through the entire codebase.

These constants often include file paths, URLs, configuration settings,
 and other values that are reused in multiple places within the project.

'''