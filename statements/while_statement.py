# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

from statements.statement import Statement
from statements.statement_types import StatementType


class While(Statement):

    def __init__(self, condition : str, statements : list) -> None:
        super().__init__(StatementType.WHILE)
        self.condition = condition
        self.statements = statements