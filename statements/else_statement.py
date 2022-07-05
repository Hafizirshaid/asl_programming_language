from statements.statement import Statement
from statements.statement_types import StatementType


class Else(Statement):

    def __init__(self, statements) -> None:
        self.statements = statements

        super().__init__(StatementType.ELSE)

    def __str__(self) -> str:
        return "Else Statement"