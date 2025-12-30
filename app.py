from src.mlproject.logger import logging
from src.mlproject.exception import customException
import sys

if __name__ == "__main__":
    logging.info("Starting the ML Project Application")
    # Application logic would go here
    logging.info("ML Project Application Finished")

    try:
      a=1/0  
    except Exception as e:
        logging.info("Custom Exception")
        raise customException(e, sys)