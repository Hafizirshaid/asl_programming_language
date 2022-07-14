# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.
"""

Instructions Library

"""

from enum import Enum


class InstructionType(Enum):
    """ Enum contains instruction types """
    LABEL = 1
    ECHO = 2
    GOTO = 3
    JUMP_IF = 4
    JUMP_IF_NOT = 5
    VARIABLE = 6


class Instruction(object):
    """ Instruction Class """

    def __init__(self, type: InstructionType) -> None:
        """

        Args:
            None
        Returns:
            None
        """
        self.type = type

    def __repr__(self) -> str:
        return f"{self.type}"


class LabelInstruction(Instruction):
    """ Label Instruction Class """

    def __init__(self, label_name) -> None:
        """

        Args:
            None
        Returns:
            None
        """
        super().__init__(InstructionType.LABEL)
        self.lable_name = label_name

    def __repr__(self) -> str:
        """

        Args:
            None
        Returns:
            None
        """
        return f"label ---> {self.lable_name}"


class EchoInstruction(Instruction):
    """ Echo Instruction Class """

    def __init__(self, echo_string: str, statement=None) -> None:
        """

        Args:
            None
        Returns:
            None
        """
        super().__init__(InstructionType.ECHO)
        self.echo_string = echo_string
        self.statement = statement

    def __repr__(self) -> str:
        """

        Args:
            None
        Returns:
            None
        """
        return f"echo ---> {self.echo_string}"


class GotoInstruction(Instruction):
    """ Goto Instruction Class """

    def __init__(self, label: str) -> None:
        """

        Args:
            None
        Returns:
            None
        """
        super().__init__(InstructionType.GOTO)
        self.goto_label = label

    def __repr__(self) -> str:
        """

        Args:
            None
        Returns:
            None
        """
        return f"Goto ---> {self.goto_label}"


class JumpIfInstruction(Instruction):
    """ JumpIf Instruction Class """

    def __init__(self, label: str, condition: str, statement=None) -> None:
        """

        Args:
            None
        Returns:
            None
        """
        super().__init__(InstructionType.JUMP_IF)
        self.goto_label = label
        self.condition = condition
        self.statement = statement

    def __repr__(self) -> str:
        """

        Args:
            None
        Returns:
            None
        """
        return f"Jump if to {self.goto_label} condition {self.condition}"


class JumpIfNotInstruction(Instruction):
    """ JumpIfNot Instruction Class """

    def __init__(self, label: str, condition: str, statement=None) -> None:
        """

        Args:
            None
        Returns:
            None
        """
        super().__init__(InstructionType.JUMP_IF_NOT)
        self.goto_label = label
        self.condition = condition
        self.statement = statement

    def __repr__(self) -> str:
        """

        Args:
            None
        Returns:
            None
        """
        return f"Jump if not to {self.goto_label} condition {self.condition}"


class VariableInstruction(Instruction):
    """ Variable Instruction Class """

    def __init__(self, variable_expression: str, variable_name="", symbols_table=None) -> None:
        """

        Args:
            None
        Returns:
            None
        """
        super().__init__(InstructionType.VARIABLE)
        self.variable_expression = variable_expression
        self.variable_name = self.variable_expression.split("=")[0].strip()
        self.symbols_table = symbols_table
        self.variable_statement = None

    def __repr__(self) -> str:
        """

        Args:
            None
        Returns:
            None
        """
        return f"var {self.variable_name} ---> {self.variable_expression}"
