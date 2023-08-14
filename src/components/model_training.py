import os, sys #type:ignore
import pandas as pd
import numpy as np
from src.utils import dump_pkl, model_evaluate
from src.logger import logging
from src.exceptions import CustomException
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestRegressor
from dataclasses import dataclass #type:ignore

# Configuration class having the path of best Model Pickle file
@dataclass
class ModelTrainingConfig:
    model_pkl_pth = os.path.join('artifacts', 'best_model.pkl')

# Model Training Class
class ModelTraining:
    def __init__(self):
        self.config = ModelTrainingConfig()
    
    def trainModel(self, train_df, test_df):
        try:
            # Segregating test and train data into input (X) and target features (y)
            y_train = train_df[['Price']]
            X_train = train_df.drop('Price', axis = 1)
            y_test = test_df[['Price']]
            X_test = test_df.drop('Price', axis = 1)

            models = {
                'Linear Regression': LinearRegression(),
                'Lasso': Lasso(),
                'Ridge': Ridge(),
                'Elastic Net': ElasticNet(),
                'Support Vector Regressor': SVR(),
                'Decision Tree Regressor': DecisionTreeRegressor(),
                'Random Forest Regressor': RandomForestRegressor(),
                'Naive Bayes Regressor': GaussianNB()
            }

            #Evaluating all the models through the function in the utils
            accuracy_report = model_evaluate(models, X_train, X_test, y_train, y_test)

            #Sorted the accuracy report as per the mean absolute error
            soreted_report = list(sorted(accuracy_report.items(), key = lambda x: x[1]))

            #Model having least error is the best model
            best_model = list(soreted_report)[0][0]
            model_obj = models[best_model]

            logging.info(f'Of all the models {best_model} is the best model and is stored in the artifacts folder.')
            dump_pkl(pkl_path=self.config.model_pkl_pth, pkl_obj=model_obj)
        
        except Exception as e:
            logging.info('Error occured in the training section!')
            raise CustomException(e, sys)
        
