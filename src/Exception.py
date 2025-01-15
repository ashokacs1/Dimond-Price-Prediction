import sys 
from src.logger import logging

def error_meassage_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    filename = exc_tb_.tb_frame.f_code.co_filename

    error_meassage = "Error occured in python script name [{0}] line number [{1}] error_message"

class CustomException(Exception):

    def __init(self,error_meassage,error_detail:sys):
        super().__init__(error_meassage)
        self.error_meassage = error_meassage_detail(error_meassage,error_detail=error_detail)

    def __str__(self):
        return self.error_meassage