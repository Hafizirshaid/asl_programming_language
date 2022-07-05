# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

from statements.statement import Statement
import string

from statements.statement_types import StatementType

class ElseIf(Statement):
    def __init__(self, condition: string, statements : list) -> None:
        super().__init__(StatementType.ELSEIF)
        self.statements = statements
        self.condition = condition
