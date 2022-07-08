# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.
"""

Instructions Library

"""
__version__ = '1.1'
__all__ = ['InstructionType',
           'Instruction',
           'LabelInstruction',
           'EchoInstruction',
           'GotoInstruction',
           'JumpIfInstruction',
           'JumpIfNotInstruction',
           'VariableInstruction']


from enum import Enum


class InstructionType(Enum):

    LABEL = 1
    ECHO = 2
    GOTO = 3
    JUMP_IF = 4
    JUMP_IF_NOT = 5
    VARIABLE = 6


class Instruction(object):

    def __init__(self, type: InstructionType) -> None:
        self.type = type


class LabelInstruction(Instruction):

    def __init__(self, label_name) -> None:
        super().__init__(InstructionType.LABEL)
        self.lable_name = label_name


class EchoInstruction(Instruction):

    def __init__(self, echo_string: str) -> None:
        super().__init__(InstructionType.ECHO)
        self.echo_string = echo_string


class GotoInstruction(Instruction):

    def __init__(self, label: str) -> None:
        super().__init__(InstructionType.GOTO)
        self.goto_label = label


class JumpIfInstruction(Instruction):

    def __init__(self, label: str, condition: str) -> None:
        super().__init__(InstructionType.JUMP_IF)
        self.goto_label = label
        self.condition = condition


class JumpIfNotInstruction(Instruction):

    def __init__(self, label: str, condition: str) -> None:
        super().__init__(InstructionType.JUMP_IF_NOT)
        self.goto_label = label
        self.condition = condition


class VariableInstruction(Instruction):

    def __init__(self, variable_name, variable_expression) -> None:
        super().__init__(InstructionType.JUMP_IF_NOT)
        self.variable_expression = variable_expression
        self.variable_name = variable_name
