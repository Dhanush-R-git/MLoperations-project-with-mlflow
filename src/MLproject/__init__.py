import os
import sys
import logging

#logging history[timestamp, level, module_name, error message or executed message]
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

#creating a log folder
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),#it will save all the logging info from mlfolder
        logging.StreamHandler(sys.stdout)# print log info in a terminal
    ]
)

logger = logging.getLogger("MachineLearningProjectLogger")