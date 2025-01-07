import logging
import os
from datetime import datetime

# Create a timestamped log file name
log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the logs directory path
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)  # Create the logs directory if it doesn't exist

# Define the full log file path
log_file_path = os.path.join(logs_dir, log_file)

# Configure logging
logging.basicConfig(
    filename=log_file_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)