import os, sys # type:ignore
import numpy as np
import pandas as pd
from src.logger import logging
from src.exceptions import CustomException
from src.utils import dump_pkl
from dataclasses import dataclass #type:ignore
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder

@dataclass
class DataTransformationConfig:
    pkl_pth = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.config = DataTransformationConfig()
    
    def get_transforming_object(self):
        # Define categorical and numerical columns
        categorical_columns = ['Airline', 'Week_Day']
        ordinal_categorical_columns = ['Total_Stops']  # Only Total_Stops is ordinal categorical
        numerical_columns = ['Duration']

        # Create transformers for preprocessing
        categorical_transformer = Pipeline([
            ('onehot', OneHotEncoder())
        ])

        ordinal_categorical_transformer = Pipeline([
            ('ordinal', OrdinalEncoder(categories=[['non-stop', '1 stop', '2 stops', '3 stops', '4 stops']]))
        ])

        numerical_transformer = Pipeline([
            ('scaler', StandardScaler())
        ])

        # ColumnTransformer for different types of columns
        preprocessor = ColumnTransformer(
            transformers=[
                ('cat', categorical_transformer, categorical_columns),
                ('ordinal_cat', ordinal_categorical_transformer, ordinal_categorical_columns),
                ('num', numerical_transformer, numerical_columns)
            ],
            remainder='drop'  
        )
        return preprocessor

    def transformData(self, train_df_path, test_df_path):
        try:
            train_df = pd.read_excel(train_df_path)
            test_df = pd.read_excel(test_df_path)

            # Drop duplicates
            train_df.drop_duplicates(inplace=True)
            test_df.drop_duplicates(inplace=True)
            train_df.dropna(inplace = True)
            test_df.dropna(inplace = True)
            train_df.reset_index(drop = True, inplace = True)

            # Segregating into train and test input as well as target feature
            y_train = train_df[['Price']]
            X_train = train_df.drop('Price', axis = 1)
            y_test = test_df[['Price']]
            X_test = test_df.drop('Price', axis = 1)

            # Feature Engineering: Extract Day Name from the Date of Journey
            X_train['Week_Day'] = pd.to_datetime(X_train['Date_of_Journey'], format='%d/%m/%Y').dt.day_name()
            X_test['Week_Day'] = pd.to_datetime(X_test['Date_of_Journey'], format='%d/%m/%Y').dt.day_name()

            # Transforming Duration Column
            # Changing Duration feature from HH:MM to total minutes
            hour = pd.to_numeric(X_train['Duration'].str.replace(r'\D+', ' ', regex=True).str.split(' ').str[0])*60
            mins = pd.to_numeric(X_train['Duration'].str.replace(r'\D+', ' ', regex=True).str.split(' ').str[1])
            # some rows dont have mins. hence will become NaN if add hr and min columns tgt. 
            X_train['Duration'] = np.where(mins.isnull(), hour, hour + mins )

            # Same thing with test data
            hour = pd.to_numeric(X_test['Duration'].str.replace(r'\D+', ' ', regex=True).str.split(' ').str[0])*60
            mins = pd.to_numeric(X_test['Duration'].str.replace(r'\D+', ' ', regex=True).str.split(' ').str[1])
            X_test['Duration'] = np.where(mins.isnull(), hour, hour + mins)

            # Getting transformation object
            preprocessor = self.get_transforming_object()

            # Transform the train data using the pipeline
            X_train = preprocessor.fit_transform(X_train)
            X_train = pd.DataFrame(X_train.toarray(), columns=preprocessor.get_feature_names_out())

            X_test = preprocessor.transform(X_test)
            X_test = pd.DataFrame(X_test.toarray(), columns=preprocessor.get_feature_names_out())

            # Concating input and target variable together
            train_dataset = pd.concat([X_train, y_train], axis = 1)
            test_dataset = pd.concat([X_test, y_test], axis = 1)
        
            logging.info('Transformation Done succesfully')

            dump_pkl(pkl_path = self.config.pkl_pth, pkl_obj = preprocessor)
            logging.info('Pickle File Extracted and saved in artifacts.')

            return (train_dataset, test_dataset, self.config.pkl_pth)

        except Exception as e:
            raise CustomException(e, sys)