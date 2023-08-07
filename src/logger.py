import logging
import os
from datetime import datetime #type: ignore

# Creating the name and directory for log files
log_file_name = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), "logs")
os.makedirs(log_path, exist_ok=True)

log_file = os.path.join(log_path, log_file_name)

# Giving the structure to LOG FILES
logging.basicConfig(
    filename = log_file,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
)