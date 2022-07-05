# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

from statements.statement import Statement
from statements.statement_types import StatementType


class Fi(Statement):

    def __init__(self) -> None:
        super().__init__(StatementType.ENDIF)

    def __str__(self) -> str:
        return "End If"
