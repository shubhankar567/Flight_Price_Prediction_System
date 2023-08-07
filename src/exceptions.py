import sys
from src.logger import logging

# Creating a function get will return the customized error message
def get_error_details(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    message = f'Error occured in {file_name} at line number [{line_number}]. The error: {error}'
    return message

# A class for handling custom errors
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = get_error_details(error = error_message, error_detail = error_detail)

    def __str__(self):
        return self.error_message
    
# testing the above class and function
if __name__ == '__main__':
    try:
        logging.info('Exception File initiated')
        a = 1/0
    except Exception as e:
        logging.info('Division by Zero Error')
        raise CustomException(e, sys)