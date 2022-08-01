# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

"""

Instructions Library

Contains Instructions definitions and types

"""

from enum import Enum

from statements.statement import Variable


class InstructionType(Enum):
    """ Enum contains instruction types """

    LABEL = 1
    ECHO = 2
    GOTO = 3
    JUMP_IF = 4
    JUMP_IF_NOT = 5
    VARIABLE = 6
    INPUT = 7


class Instruction(object):
    """ Instruction Class """

    def __init__(self, type: InstructionType) -> None:
        """ Instruction class constructor
        Args:
            type: Instruction type
        Returns:
            None
        """

        self.type = type

    def __repr__(self) -> str:
        return f"{self.type}"

    def __str__(self) -> str:
        return self.__repr__()


class LabelInstruction(Instruction):
    """ Label Instruction Class """

    def __init__(self, label_name) -> None:
        """ Label Instruction class constructor
        Args:
            label_name: Label name
        Returns:
            None
        """

        super().__init__(InstructionType.LABEL)
        self.label_name = label_name

    def __repr__(self) -> str:
        return f"label ---> {self.label_name}"

    def __str__(self) -> str:
        return self.__repr__()


class EchoInstruction(Instruction):
    """ Echo Instruction Class """

    def __init__(self, echo_string: str, statement=None) -> None:
        """ Echo Instruction Class Constructor
        Args:
            echo_string: string that needs to be printed
            statement: Optional, echo statement that contains echo string,
                        used in order to lookup symbols table.
        Returns:
            None
        """

        super().__init__(InstructionType.ECHO)
        self.echo_string = echo_string
        self.statement = statement

    def __repr__(self) -> str:
        return f"echo ---> {self.echo_string}"

    def __str__(self) -> str:
        return self.__repr__()


class InputInstruction(Instruction):
    """ Input Instruction Class """

    def __init__(self, input_variable: str, statement=None) -> None:
        """ Input Instruction Class Constructor
        Args:
            input_variable: variable name to store input value
            statement: Optional, echo statement that contains input variable name,
                        used in order to lookup symbols table.
        Returns:
            None
        """

        super().__init__(InstructionType.INPUT)
        self.input_variable = input_variable
        self.statement = statement

    def __repr__(self) -> str:
        return f"echo ---> {self.echo_string}"

    def __str__(self) -> str:
        return self.__repr__()


class GotoInstruction(Instruction):
    """ Goto Instruction Class """

    def __init__(self, label: str) -> None:
        """ Goto Instruction Class Constructor
        Args:
            label: Goto Label
        Returns:
            None
        """

        super().__init__(InstructionType.GOTO)
        self.goto_label = label

    def __repr__(self) -> str:
        return f"Goto ---> {self.goto_label}"

    def __str__(self) -> str:
        return self.__repr__()


class JumpIfInstruction(Instruction):
    """ JumpIf Instruction Class """

    def __init__(self, label: str, condition: str, statement=None) -> None:
        """ JumpIf Instruction Class Constructor
        Args:
            label: Label to go to if condition is true
            condition: Condition to be evaluated
            statement: Optional, statement that contains condition, it is
                        used to lookup symbols table
        Returns:
            None
        """

        super().__init__(InstructionType.JUMP_IF)
        self.goto_label = label
        self.condition = condition
        self.statement = statement

    def __repr__(self) -> str:
        return f"Jump if to {self.goto_label} condition {self.condition}"

    def __str__(self) -> str:
        return self.__repr__()


class JumpIfNotInstruction(Instruction):
    """ JumpIfNot Instruction Class """

    def __init__(self, label: str, condition: str, statement=None) -> None:
        """ JumpIfNot Instruction Class Constructor
        Args:
            label: Label to go to if condition is false
            condition: condition to be evaluated.
            statement: Optional, statement that contains condition, it is
                        used to lookup symbols table
        Returns:
            None
        """

        super().__init__(InstructionType.JUMP_IF_NOT)
        self.goto_label = label
        self.condition = condition
        self.statement = statement

    def __repr__(self) -> str:
        return f"Jump if not to {self.goto_label} condition {self.condition}"

    def __str__(self) -> str:
        return self.__repr__()


class VariableInstruction(Instruction):
    """ Variable Instruction Class """

    def __init__(self, variable_statement: Variable,
                       symbols_table=None) -> None:
        """ Variable Instruction Class Constructor
        Args:
            variable_expression: Variable expression
            variable_name: variable name
            symbols_table: symbols table that contains this variable
        Returns:
            None
        """

        super().__init__(InstructionType.VARIABLE)
        self.variable_expression = variable_statement.variable_expression
        self.variable_name = variable_statement.variable_name
        self.operation = variable_statement.operation
        self.symbols_table = symbols_table
        self.variable_statement = variable_statement

    def __repr__(self) -> str:
        return f"var {self.variable_name} ---> {self.variable_expression}"

    def __str__(self) -> str:
        return self.__repr__()

