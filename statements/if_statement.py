# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

from statements.statement import Statement
import string

from statements.statement_types import StatementType

class If(Statement):

    def __init__(self, condition: string, statements: list) -> None:
        super().__init__(StatementType.IF)
        self.statements = statements
        self.condition = condition

    def __str__(self) -> str:
        return str(self.condition)