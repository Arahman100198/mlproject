import sys
import logging
def error_message_detail(error, error_details):
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error in script '{0}' on line {1}: {2}".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message
class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_details=error_details)

    def __str__(self):
        return self.error_message
    

    
    