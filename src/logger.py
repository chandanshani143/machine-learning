import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"  #log file name
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)  #log file path
os.makedirs(logs_path,exist_ok=True)  #create logs directory if not exists or append if exists

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)  #complete log file path

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    level=logging.INFO,
)


# for testing purpose
# if __name__ == "__main__":
#     logging.info("Logging has started.")