
import os
import sys

# creating my own custom exception class by using 'Exception' the parent class.
class HousingException(Exception):
    
    # "error_message" gets the object or instance of Exception class. Same for "error_details"
    def __init__(self, error_message:Exception,error_detail:sys):
        # passing the information to the parent class i.e. Exception class
        # Note that "super().__init__(error_message)" is equal to "Exception(error_message)"
        super().__init__(error_message)
        self.error_message=HousingException.get_detailed_error_message(error_message=error_message,
                                                                       error_detail=error_detail
                                                                        )

    # with "@staticmethod" we can use a function without creating an object because I do not want any object to call this function.
    @staticmethod
    def get_detailed_error_message(error_message:Exception,error_detail:sys)->str:
        """
        error_message:Exception module object
        error_detail: object of sys module
        """
        _,_ ,exec_tb = error_detail.exc_info()
        line_number = exec_tb.tb_frame.f_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        error_message = f"Error occured in script: [{file_name}] at line number: [{line_number}] error message: [{error_message}]"
        return error_message

    def __str__(self):
        return self.error_message


    def __repr__(self) -> str:
        return HousingException.__name__.str()