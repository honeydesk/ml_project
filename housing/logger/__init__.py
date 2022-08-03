import logging
from datetime import datetime
import os

# The directory in which we are going to log our project
LOG_DIR="housing_logs"

# This will give the current time-stamp
CURRENT_TIME_STAMP=  f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

# Creating a file having the name with current timestamp
LOG_FILE_NAME=f"log_{CURRENT_TIME_STAMP}.log"

# If the log directory is not available, then create it
os.makedirs(LOG_DIR,exist_ok=True)

# generating the file path name
LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)

# mention the file path name 
# mention the format in which log message is to be captured.
logging.basicConfig(filename=LOG_FILE_PATH,
filemode="w",
format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
level=logging.INFO
)