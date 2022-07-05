# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

from statements.statement import Statement
from statements.statement_types import StatementType


class Variable(Statement):

    def __init__(self, variable: str) -> None:
        super().__init__(StatementType.VAR)
        self.variable = variable

    def __str__(self) -> str:
        return "var " + str(self.variable)
