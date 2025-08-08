import os
import sys
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

from src.exception import CustomException
from src.logger import logging

# ✅ Configuration for saving paths in root/artifacts/
@dataclass
class DataIngestionConfig:
    root_dir = os.path.abspath(os.path.join(os.getcwd(), "..", ".."))  # Go up 2 levels to project root
    artifacts_dir = os.path.join(root_dir, "artifacts")
    train_data_path: str = os.path.join(artifacts_dir, "train.csv")
    test_data_path: str = os.path.join(artifacts_dir, "test.csv")
    raw_data_path: str = os.path.join(artifacts_dir, "data.csv")

# ✅ Ingestion class
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("📥 Starting data ingestion...")

        try:
            # ✅ Construct full path to the dataset
            data_path = os.path.abspath(os.path.join(os.getcwd(), "..", "..", "notebook", "Data", "stud.csv"))
            logging.info(f"🔍 Reading CSV file from: {data_path}")
            df = pd.read_csv(data_path)
            logging.info("✅ Dataset read successfully.")

            # ✅ Create output directory if not exists
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # ✅ Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("💾 Raw data saved.")

            # ✅ Split data
            logging.info("✂️ Splitting into train and test sets...")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # ✅ Save train and test sets
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("✅ Data ingestion completed.")
            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path

        except Exception as e:
            raise CustomException(e, sys)


# ✅ Script entrypoint
if __name__ == "__main__":
    obj = DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()
    print(f"Train data saved at: {train_data_path}")
    print(f"Test data saved at: {test_data_path}")
