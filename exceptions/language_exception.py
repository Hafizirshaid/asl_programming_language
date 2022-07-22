# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

"""

Exceptions Module

Contains SyntaxError, UnknwonVariable, UnexpectedError, ExpressionEvaluationError
Those exceptions are being used in order to identify potential issues in the code

"""


class SyntaxError(Exception):
    """ Syntax Error Exception """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class UnknwonVariable(Exception):
    """ Syntax Error Exception """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class UnexpectedError(Exception):
    """ Syntax Error Exception """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class ExpressionEvaluationError(Exception):
    """ Expression Evaluation Error Exception """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
