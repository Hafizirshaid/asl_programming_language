import string
from statements.statement import Statement
from statements.statement_types import StatementType


class Echo(Statement):

    def __init__(self, echoString: string) -> None:
        
        super().__init__(StatementType.ECHO)
        self.echoString = echoString

    def __str__(self) -> str:
        return str(self.echoString)

