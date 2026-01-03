import os
import sys

import pandas as pd
from sklearn.model_selection import train_test_split
from src.mlproject.logger import logging
from src.mlproject.exception import customException

from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')
    train_data_path: str = os.path.join('artifacts', 'train.csv')                       
    test_data_path: str = os.path.join('artifacts', 'test.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self, source_path: str) -> tuple:
        logging.info("Starting data ingestion process")
        try:
            pass
        logging.info("Data ingestion process completed successfully")   
        os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
        
        except exception as e:
            raise customException(e, sys)
        try:
            # Read the dataset
            df = pd.read_csv(source_path)
            logging.info(f"Dataset read from {source_path} with shape {df.shape}")

            # Ensure the artifacts directory exists
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)

            # Save the raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info(f"Raw data saved at {self.ingestion_config.raw_data_path}")

            # Split the dataset into training and testing sets
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            logging.info("Dataset split into training and testing sets")

            # Save the training and testing sets
            train_set.to_csv(self.ingestion_config.train_data_path, index=False)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False)
            logging.info(f"Training data saved at {self.ingestion_config.train_data_path}")
            logging.info(f"Testing data saved at {self.ingestion_config.test_data_path}")

            return (self.ingestion_config.train_data_path, self.ingestion_config.test_data_path)

        except Exception as e:
            logging.error("Error occurred during data ingestion")
            raise customException(e, sys)