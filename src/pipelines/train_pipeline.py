import os, sys
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_training import ModelTraining
import pandas as pd 

class TrainPipeline:
    def __init__(self):
        pass

    def training(self):
        # Creating Data Ingestion Object
        ingest_obj = DataIngestion()
        _, train_path, test_path = ingest_obj.injectData()
        print(_)
        print(f'Train Dataset path: {train_path}')
        print(f'Test Dataset path: {test_path}')

    
        # Creating the Data Tranformation object
        transform_obj = DataTransformation()
        train_df, test_df, _ = transform_obj.transformData(train_path, test_path)

    
        # Creating the Model Training object
        trainer_obj = ModelTraining()
        trainer_obj.trainModel(train_df, test_df)
        print('Model Trained')