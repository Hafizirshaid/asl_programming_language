# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

from statements.statement import Statement
from statements.statement_types import StatementType


class EndFor(Statement):

    def __init__(self) -> None:
        super().__init__(StatementType.ENDFOR)

    def __str__(self) -> str:
        return "End For Loop"