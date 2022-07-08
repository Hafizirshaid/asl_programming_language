# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

from statements.else_statement import Else
from statements.if_statement import If
from statements.statement import Statement
from statements.statement_types import StatementType

class ConditionStatement(Statement):

    def __init__(self, 
        if_statmenet: If, 
        elseif_statements: list, 
        else_statement: Else) -> None:
        super().__init__(StatementType.CONDITION)

        if if_statmenet is None:
            raise Exception("Error, if statment can't be None")
        
        self.if_statmenet = if_statmenet
        self.elseif_statements = elseif_statements
        self.else_statement = else_statement
