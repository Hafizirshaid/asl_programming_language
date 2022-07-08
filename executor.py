# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

from instructions.instruction import InstructionType
from symbols.symbols_table import SymbolTable


class Executor(object):
    """
    Executor Class 
    """

    def __init__(self) -> None:
        self.instruction_pointer = 0
        self.label_index_table = {}
        self.sybmol_table = SymbolTable()

    def execute(self, instructions) -> str:
        """ 
        Desc:
            Execute List of Instructions
        Args:
            instructions: instructions to be exected
        Returns:
            program output
        """
        if not instructions:
            # if no instructions provided, return empty
            return ""

        # Build Lable index map
        for index, instruction in enumerate(instructions):
            if instruction.type == InstructionType.LABEL:
                self.label_index_table[instruction.lable_name] = index

        program_output = ""
        while self.instruction_pointer < len(instructions):

            current_instruction = instructions[self.instruction_pointer]

            if current_instruction.type == InstructionType.ECHO:
                pass
            elif current_instruction.type == InstructionType.VARIABLE:
                pass
            elif current_instruction.type == InstructionType.GOTO:
                pass
            elif current_instruction.type == InstructionType.JUMP_IF:
                pass
            elif current_instruction.type == InstructionType.JUMP_IF_NOT:
                pass
            elif current_instruction.type == InstructionType.LABEL:
                pass
            pass

        return program_output
