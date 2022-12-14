# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

"""

Exceptions Module

Contains SyntaxError, UnknownVariable, UnexpectedError, ExpressionEvaluationError
Those exceptions are being used in order to identify potential issues in the code

"""


class SyntaxError(Exception):
    """ Syntax Error Exception """

    def __init__(self, message: str, token=None) -> None:
        if token:
            super().__init__(f"{message}, {token.match}, line number {token.line_number} type: {token.token_type}")
        else:
            super().__init__(f"{message}")
        pass


class UnknownVariable(Exception):
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
