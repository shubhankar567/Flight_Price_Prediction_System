import os, sys
from src.logger import logging
from src.exceptions import CustomException
import pickle #type:ignore

def dump_pkl(pkl_path, pkl_obj):
    try:
        # Creating the directory of pickle file
        os.makedirs(os.path.dirname(pkl_path), exist_ok = True)
        
        # dumping the pickle file
        with open(pkl_path, 'wb') as file_obj:
            pickle.dump(pkl_obj, file_obj)

    except Exception as e:
        logging.info(f'Error during dumping pickle file {pkl_obj}')
        raise CustomException(e, sys) 
    
def load_pkl(pkl_path):
    try:        
        # Reading the pickle file
        with open(pkl_path, 'rb') as file_obj:
            pickle_file = pickle.load(file_obj)
        return pickle_file

    except Exception as e:
        logging.info(f'Error during dumping pickle file {pkl_obj}')
        raise CustomException(e, sys) 
# Testing the utils
if __name__ == '__main__':
    try: 
        file_path = os.path.join("artifacts", "bkl.pkl")
        pkl = 1
        dump_pkl(file_path, pkl)
        file = load_pkl(file_path)
        print(file)
        
    except Exception as e:
        logging.info("Error while testing confirmed")
        raise CustomException(e, sys)