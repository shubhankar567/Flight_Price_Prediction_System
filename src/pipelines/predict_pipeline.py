import os, sys #type:ignore
from src.exceptions import CustomException
from src.logger import logging
from src.utils import load_pkl
import pandas as pd
import numpy as np

class PredictPipeline:
    def __init__(self):
        pass

    def prediction(self, input_data):
        try:
            # Creating the path for locating all the pickle files
            preprocess_pkl_path = os.path.join('artifacts', 'preprocessor.pkl')
            model_pkl_path = os.path.join('artifacts', 'best_model.pkl')

            # Loading the pickle files
            preprocessor = load_pkl(preprocess_pkl_path)
            model = load_pkl(model_pkl_path)

            # Preprocessing
            input_processed = pd.DataFrame(preprocessor.transform(input_data).toarray(), columns = preprocessor.get_feature_names_out())
            logging.info(input_processed)
            # Predicting
            prediction = model.predict(input_processed)

            return prediction
        except Exception as e:
            logging.info('Error occured in Prediction Pipeline')
            raise CustomException(e, sys) #type:ignore

# Creating a class for transforming the input data into a dataframe
class CustomData:
    def __init__(self,
                 Airline,
                 Week_Day,
                 Total_Stops,
                 Duration
                 ):
        
        self.Airline=Airline
        self.Week_Day=Week_Day
        self.Duration=Duration
        self.Total_Stops=Total_Stops

    def data_to_dataframe(self):
        try:
            custom_data_input_dict = {
                'Airline':[self.Airline],
                'Week_Day':[self.Week_Day],
                'Total_Stops':[self.Total_Stops],
                'Duration':[self.Duration]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            logging.info(df.to_string())
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys) # type: ignore