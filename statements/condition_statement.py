from statements.else_statement import Else
from statements.if_statement import If
from statements.statement import Statement
from statements.statement_types import StatementType

class ConditionStatement(Statement):

    def __init__(self, 
        ifstatmenet: If, 
        elseIfStatement: list, 
        elseStatement: Else) -> None:

        if ifstatmenet is None:
            raise Exception("Error, if statment can't be None")
        
        self.ifstatmenet = ifstatmenet
        self.elseifstatement = elseIfStatement
        self.elsestatement = elseStatement
        super().__init__(StatementType.CONDITION)