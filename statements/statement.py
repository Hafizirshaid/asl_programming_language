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
    INPUT = 14


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


class VariableType(Enum):
    NUMERIC = 0
    STRING = 1
    STRUCT = 2


class Variable(Statement):
    """ Variable Statement Class """

    def __init__(self, variable_name, operation, variable_value, type=None) -> None:
        """ Variable Statement Class Constructor
        Args:
            variable_name:
            operation:
            variable_value:
        Returns:
            None
        """

        super().__init__(StatementType.VAR)
        self.variable_name = variable_name
        self.operation = operation
        self.variable_value = variable_value
        self.variable_expression = f"{self.variable_name}{self.operation}{self.variable_value}"

        if not type:
            if isinstance(variable_value, str):
                if variable_value.isnumeric():
                    self.type = VariableType.NUMERIC
                else:
                    self.type = VariableType.STRING
                pass
            else:
                self.type = VariableType.STRUCT
        else:
            self.type = type

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

    def __init__(self,
                 statements: list,
                 loop_initial_variable : str,
                 loop_condition : str,
                 loop_increment : str) -> None:

        """ For Statement Class Constructor
        Args:
            condition: For Loop Expression
            statements: Children statements of for loop
        Returns:
            None
        """

        super().__init__(StatementType.FOR)
        self.statements = statements

        self.loop_initial_variable = loop_initial_variable
        self.loop_condition = loop_condition
        self.loop_increment = loop_increment

        self.condition = None
        self.symbols_table = SymbolTable()

    def __str__(self) -> str:
        return f"For Loop: {self.loop_initial_variable}; {self.loop_condition}; {self.loop_increment}"

    def __repr__(self) -> str:
        return self.__str__()


class Fi(Statement):
    """ Fi Statement Class (EndIf)"""

    def __init__(self) -> None:
        """ Fi Statement Class (EndIf) Constructor
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
        """ EndWhile Statement Class Constructor
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
        """ EndFor Statement Class Constructor
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
            statements: Children statements in else if statement
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
            statements: Children statements of else statement
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


class Input(Statement):
    """ Input Statement Class """

    def __init__(self, input_variable) -> None:
        """ Input Statement Class Constructor
        Args:
            input_variable: Input variable name
        Returns:
            None
        """
        super().__init__(StatementType.INPUT)
        self.input_variable = input_variable

    def __str__(self) -> str:
        return f"Input Statement: {self.input_variable}"

    def __repr__(self) -> str:
        return self.__str__()


class ConditionStatement(Statement):
    """ Condition Statement Class """

    def __init__(self,
                 if_statement: If,
                 elseif_statements: list,
                 else_statement: Else) -> None:
        """ Condition Statement Class Constructor

        Args:
            if_statement: if statement, should not be null
            elseif_statements: else if statements list
            else_statement: else statement
        Returns:
            None
        """

        super().__init__(StatementType.CONDITION)

        if if_statement is None:
            # If statement should not be none
            raise Exception("Error, if statement can't be None")

        self.if_statement = if_statement
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
