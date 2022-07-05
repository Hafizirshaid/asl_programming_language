
class SyntaxError(Exception):
    """ Syntax Error Exception """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
