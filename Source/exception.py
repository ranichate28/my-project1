import sys

def error_message_detail(error, error_detail:sys):

    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.to_frame.f_code.co_filename

    error_message = "Error occured script name [{0}] line number [{i}] error message [{2}]".format(file)

    return error_message
class ChurnException(Exception):

    def __init__(self, *args: object):
        super().__init__(args)
        self.error_message = None

    def _init_(self, error_message, error_detail: sys):
        super()._init_(error_message)

        self.error_message - error_message_detail(
            error_message, error_detail = error_detail
        )

    def _str_(self):
        return self.error_message