# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

import string
from statements.statement import Statement
from statements.statement_types import StatementType


class Echo(Statement):

    def __init__(self, echo_string: string) -> None:
        super().__init__(StatementType.ECHO)
        self.echo_string = echo_string

    def __str__(self) -> str:
        return str(self.echo_string)

