import os, sys #type:ignore
import numpy as np
from src.logger import logging
from src.exceptions import CustomException
import pickle #type:ignore
from sklearn.metrics import mean_absolute_error

def dump_pkl(pkl_path, pkl_obj):
    try:
        # Creating the directory of pickle file
        os.makedirs(os.path.dirname(pkl_path), exist_ok = True)
        
        # dumping the pickle file
        with open(pkl_path, 'wb') as file_obj:
            pickle.dump(pkl_obj, file_obj)

    except Exception as e:
        logging.info(f'Error during dumping pickle file {pkl_path}')
        raise CustomException(e, sys) 
    
def load_pkl(pkl_path):
    try:        
        # Reading the pickle file
        with open(pkl_path, 'rb') as file_obj:
            pickle_file = pickle.load(file_obj)
        return pickle_file

    except Exception as e:
        logging.info(f'Error during loading pickle file')
        raise CustomException(e, sys) 
    
def model_evaluate(models, X_train, X_test, y_train, y_test):
    try:
        #Empty Dictionary for storing accuracy scores of various models
        report = {}
        y_train = y_train.values.ravel()
        y_test = y_test.values.ravel()

        logging.info('Training various models initiated.')
        #Iterating over all the models
        for model in models:
            model_name = model
            model_obj = models[model_name]
            model_obj.fit(X_train, y_train)
            y_predict = model_obj.predict(X_test)
            mae = mean_absolute_error(y_test, y_predict)
            report[model_name] = mae
        return report
    except Exception as e:
        logging.info('Error Occured during model evaluations!')
        raise CustomException(e, sys)

