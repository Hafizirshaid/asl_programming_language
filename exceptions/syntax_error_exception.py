# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

class SyntaxError(Exception):
    """ Syntax Error Exception """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
