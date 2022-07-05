# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

from statements.statement import Statement
from statements.statement_types import StatementType


class Else(Statement):

    def __init__(self, statements) -> None:
        super().__init__(StatementType.ELSE)
        self.statements = statements

    def __str__(self) -> str:
        return "Else Statement"
