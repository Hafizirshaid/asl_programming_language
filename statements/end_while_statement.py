# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

from statements.statement import Statement
from statements.statement_types import StatementType


class EndWhile(Statement):

    def __init__(self) -> None:
        super().__init__(StatementType.ENDWHILE)
