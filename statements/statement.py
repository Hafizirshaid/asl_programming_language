# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

"""

Statements Library

Contains Statements definitions and types

"""

from enum import Enum
from symbols.symbols_table import SymbolTable


class StatementType(Enum):
    """ Statement Type Enum"""

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
    """ Statement Class """

    def __init__(self, type: StatementType) -> None:
        """Statement Class Constructor
        Args:
            type: Statement type of enum StatementType
        Returns:
            None
        """

        self.type = type
        self.parent = None


class Variable(Statement):
    """ Variable Statement Class """

    def __init__(self, variable_expression: str) -> None:
        """ Variable Statement Class Constructor
        Args:
            variable_expression: Variable Expression
        Returns:
            None
        """

        super().__init__(StatementType.VAR)
        self.variable_expression = variable_expression
        chunks = self.variable_expression.split("=")
        # remove empty space from variable name
        self.variable_name = chunks[0].strip()
        self.variable_name = self.variable_name.strip('"')
        self.variable_value = chunks[1]
        self.symbols_table = None

    def __str__(self) -> str:
        return "Variable: " + str(self.variable_expression)

    def __repr__(self) -> str:
        return self.__str__()


class While(Statement):
    """ While Statement Class """

    def __init__(self, condition: str, statements: list) -> None:
        """ While Statement Class Constructor
        Args:
            condition: While statement Condition
            statements: list of statements inside while loop scope "Children statements"
        Returns:
            None
        """

        super().__init__(StatementType.WHILE)
        self.condition = condition
        self.statements = statements
        self.symbols_table = SymbolTable()

    def __repr__(self) -> str:
        return f"While Loop Statement: {self.condition}"

    def __str__(self) -> str:
        return self.__repr__()


class If(Statement):
    """ If Statement Class """

    def __init__(self, condition: str, statements: list) -> None:
        """ If Statement Class Constructor
        Args:
            condition: If statement Condition
            statements: Children statements in If statement
        Returns:
            None
        """

        super().__init__(StatementType.IF)
        self.statements = statements
        self.condition = condition
        self.symbols_table = SymbolTable()

    def __str__(self) -> str:
        return f"If statement: {self.condition}"

    def __repr__(self) -> str:
        return self.__str__()


class For(Statement):
    """ For Statement Class """

    def __init__(self, condition: str, statements: list) -> None:
        """ For Statement Class Constructor
        Args:
            condition: For Loop Expression
            statements: Children statements of for loop
        Returns:
            None
        """

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
        return f"For Loop: {self.conditon}"

    def __repr__(self) -> str:
        return self.__str__()


class Fi(Statement):
    """ Fi Statement Class (EndIf)"""

    def __init__(self) -> None:
        """ Fi Statement Class (EndIf) Constrctor
        Args:
            None
        Returns:
            None
        """

        super().__init__(StatementType.ENDIF)

    def __str__(self) -> str:
        return "End If"

    def __repr__(self) -> str:
        return self.__str__()


class EndWhile(Statement):
    """ EndWhile Statement Class """

    def __init__(self) -> None:
        """ EndWhile Statement Class Constrcutor
        Args:
            None
        Returns:
            None
        """

        super().__init__(StatementType.ENDWHILE)

    def __str__(self) -> str:
        return "End While Statement"

    def __repr__(self) -> str:
        return self.__str__()


class EndFor(Statement):
    """ EndFor Statement Class """

    def __init__(self) -> None:
        """ EndFor Statement Class Constrctor
        Args:
            None
        Returns:
            None
        """

        super().__init__(StatementType.ENDFOR)

    def __str__(self) -> str:
        return "End For Loop"

    def __repr__(self) -> str:
        return self.__str__()


class ElseIf(Statement):
    """ ElseIf Statement Class """

    def __init__(self, condition: str, statements: list) -> None:
        """ ElseIf Statement Class Constructor
        Args:
            condition: else if statement condition
            statements: Children statements in else if statment
        Returns:
            None
        """

        super().__init__(StatementType.ELSEIF)
        self.statements = statements
        self.condition = condition
        self.symbols_table = SymbolTable()

    def __str__(self) -> str:
        return "Else If Statement"

    def __repr__(self) -> str:
        return self.__str__()


class Else(Statement):
    """ Else Statement Class """

    def __init__(self, statements) -> None:
        """ Else Statement Class Constructor
        Args:
            statements: Children statements of else statment
        Returns:
            None
        """

        super().__init__(StatementType.ELSE)
        self.statements = statements
        self.symbols_table = SymbolTable()

    def __str__(self) -> str:
        return "Else Statement"

    def __repr__(self) -> str:
        return self.__str__()


class Echo(Statement):
    """ Echo Statement Class """

    def __init__(self, echo_string: str) -> None:
        """ Echo Statement Class Constructor
        Args:
            echo_string: echo string
        Returns:
            None
        """

        super().__init__(StatementType.ECHO)
        self.echo_string = echo_string

    def __str__(self) -> str:
        return f"Echo Statement: {self.echo_string}"

    def __repr__(self) -> str:
        return self.__str__()


class ConditionStatement(Statement):
    """ Condition Statement Class """

    def __init__(self,
                 if_statmenet: If,
                 elseif_statements: list,
                 else_statement: Else) -> None:
        """ Condition Statement Class Constructor

        Args:
            if_statmenet: if statement, should not be null
            elseif_statements: else if statements list
            else_statement: else statement
        Returns:
            None
        """

        super().__init__(StatementType.CONDITION)

        if if_statmenet is None:
            # If statmenet should not be none
            raise Exception("Error, if statment can't be None")

        self.if_statmenet = if_statmenet
        self.elseif_statements = elseif_statements
        self.else_statement = else_statement

    def __str__(self) -> str:
        return "Condition Statement"

    def __repr__(self) -> str:
        return self.__str__()


class Break(Statement):
    """ Break Statement Class """

    def __init__(self) -> None:
        """ Break Statement Class Constructor
        Args:
            None
        Returns:
            None
        """
        super().__init__(StatementType.BREAK)

    def __str__(self) -> str:
        return "Break Statement"

    def __repr__(self) -> str:
        return self.__str__()


class Continue(Statement):
    """ Continue Statement Class """

    def __init__(self) -> None:
        """
            Continue Statement Class Constructor
        Args:
            None
        Returns:
            None
        """

        super().__init__(StatementType.CONTINUE)

    def __str__(self) -> str:
        return "Continue Statement"

    def __repr__(self) -> str:
        return self.__str__()
