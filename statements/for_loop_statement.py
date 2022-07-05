# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

from statements.statement import Statement
from statements.statement_types import StatementType

class For(Statement):

    def __init__(self, condition: str, statements : list) -> None:
        super().__init__(StatementType.FOR)
        self.statements = statements
        self.conditon = condition

    def __str__(self) -> str:
        return f"For Loop {self.conditon}"