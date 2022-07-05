# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

from statements.statement import Statement
from statements.statement_types import StatementType


class Break(Statement):

    def __init__(self) -> None:
        super().__init__(StatementType.BREAK)