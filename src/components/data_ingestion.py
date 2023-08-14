import os, sys
import pandas as pd
from src.logger import logging
from src.exceptions import CustomException
from dataclasses import dataclass #type:ignore

#Configuration Class
@dataclass
class DataIngestionConfig:
    raw_datapath = os.path.join('artifacts', 'raw_data.xlsx')
    train_datapath = os.path.join('artifacts', 'train_data.xlsx')
    test_datapath = os.path.join('artifacts', 'test_data.xlsx')

# Class for reading the data and storing it at a location given in configuration class
class DataIngestion:
    def __init__(self):
        self.ingestionConfig = DataIngestionConfig()

    def injectData(self):
        try:
            logging.info('Data Ingestion started ...')
            # Read data
            train_df = pd.read_excel('notebooks/data/Data_Train.xlsx')
            test_df = pd.concat([pd.read_excel('notebooks/data/Test_set.xlsx'), 
                                pd.read_excel('notebooks/data/Sample_submission.xlsx')],
                                axis=1)
        
            raw_df = pd.concat([train_df, test_df], axis = 0)
            logging.info('All the files are read')

            # Making directories for saving the excel files
            os.makedirs(os.path.dirname(self.ingestionConfig.raw_datapath), exist_ok=True)

            # Saving the files in excel format
            raw_df.to_excel(self.ingestionConfig.raw_datapath, index = False)
            train_df.to_excel(self.ingestionConfig.train_datapath, index = False)
            test_df.to_excel(self.ingestionConfig.test_datapath, index = False)

            logging.info(f'Excel Files are sucessfully stored at {os.path.dirname(self.ingestionConfig.raw_datapath)} folder.')

            return (
                self.ingestionConfig.raw_datapath,
                self.ingestionConfig.train_datapath,
                self.ingestionConfig.test_datapath
            )
        except Exception as e:
            logging.info('Error occured during Data Ingestion.')
            raise CustomException(e, sys)



        