import sys
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()     #get the exception info
    file_name = exc_tb.tb_frame.f_code.co_filename   #get the file name where the exception occurred
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))

    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)  #calling the above function that transform the raw error into our nice, detailed string and store it on the instance

    #returns the error message when we print or log the exception
    def __str__(self):
        return self.error_message


# #for testing purpose
# try:
#     1 / 0
# except Exception as e:
#     raise CustomException(e, sys)