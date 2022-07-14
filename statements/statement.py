# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

from enum import Enum
from symbols.symbols_table import SymbolTable


class StatementType(Enum):

    ECHO = 1
    VAR = 2
    IF = 3
    ELSEIF = 4
    ELSE = 5
    FOR = 6
    ENDFOR = 7
    ENDIF = 8
    CONDITION = 9
    WHILE = 10
    ENDWHILE = 11
    BREAK = 12
    CONTINUE = 13


class Statement(object):

    def __init__(self, type: StatementType) -> None:
        self.type = type
        self.parent = None
        pass


class Variable(Statement):

    def __init__(self, variable_expression: str) -> None:
        super().__init__(StatementType.VAR)
        self.variable_expression = variable_expression
        chunks = self.variable_expression.split("=")
        # remove empty space from variable name
        self.variable_name = chunks[0].strip(" ")
        self.variable_name = self.variable_name.strip('"')
        self.variable_value = chunks[1]
        self.symbols_table = None

    def __str__(self) -> str:
        return "var " + str(self.variable_expression)


class While(Statement):

    def __init__(self, condition: str, statements: list) -> None:
        super().__init__(StatementType.WHILE)
        self.condition = condition
        self.statements = statements
        self.symbols_table = SymbolTable()


class If(Statement):

    def __init__(self, condition: str, statements: list) -> None:
        super().__init__(StatementType.IF)
        self.statements = statements
        self.condition = condition
        self.symbols_table = SymbolTable()

    def __str__(self) -> str:
        return str(self.condition)


class For(Statement):

    def __init__(self, condition: str, statements: list) -> None:
        super().__init__(StatementType.FOR)
        self.statements = statements
        self.conditon = condition.strip('"')

        chunks = self.conditon.split(';')
        # Dirty way to split things, TODO find a better solution
        self.loop_initial_variable = chunks[0]
        self.loop_condition = chunks[1]
        self.loop_increment = chunks[2]
        self.symbols_table = SymbolTable()

    def __str__(self) -> str:
        return f"For Loop {self.conditon}"


class Fi(Statement):

    def __init__(self) -> None:
        super().__init__(StatementType.ENDIF)

    def __str__(self) -> str:
        return "End If"


class EndWhile(Statement):

    def __init__(self) -> None:
        super().__init__(StatementType.ENDWHILE)


class EndFor(Statement):

    def __init__(self) -> None:
        super().__init__(StatementType.ENDFOR)

    def __str__(self) -> str:
        return "End For Loop"


class ElseIf(Statement):
    def __init__(self, condition: str, statements: list) -> None:
        super().__init__(StatementType.ELSEIF)
        self.statements = statements
        self.condition = condition
        self.symbols_table = SymbolTable()


class Else(Statement):

    def __init__(self, statements) -> None:
        super().__init__(StatementType.ELSE)
        self.statements = statements
        self.symbols_table = SymbolTable()

    def __str__(self) -> str:
        return "Else Statement"


class Echo(Statement):

    def __init__(self, echo_string: str) -> None:
        super().__init__(StatementType.ECHO)
        self.echo_string = echo_string

    def __str__(self) -> str:
        return str(self.echo_string)


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


class Break(Statement):

    def __init__(self) -> None:
        super().__init__(StatementType.BREAK)

class Continue(Statement):

    def __init__(self) -> None:
        super().__init__(StatementType.CONTINUE)
