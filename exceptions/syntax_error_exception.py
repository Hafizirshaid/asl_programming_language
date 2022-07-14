# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

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
