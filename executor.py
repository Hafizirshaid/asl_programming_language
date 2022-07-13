# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

from lib2to3.pgen2 import token
from tokenize import Token
from compiler import ExecutionTree
from expression_evaluator import Evaluator
from instructions.instruction import EchoInstruction, InstructionType
from lexer import Lexer, TokenType
from statements.statement import ConditionStatement, Else, ElseIf, For, If, While
from symbols.symbols_table import SymbolTable


class Executor(object):
    """
    Executor Class 
    """

    def __init__(self) -> None:
        self.instruction_pointer = 0
        self.label_index_table = {}
        self.execution_tree = None

    def execute(self, instructions, execution_tree):
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

        self.execution_tree = execution_tree
        instruction = self.build_label_index_table(instructions)

        while self.instruction_pointer < len(instructions):

            current_instruction = instructions[self.instruction_pointer]

            # Echo Instruction
            if current_instruction.type == InstructionType.ECHO:
                self.execute_echo_instruction(current_instruction)
                self.increment_instruction_pointer()

            # Variable Instruction
            elif current_instruction.type == InstructionType.VARIABLE:
                self.handle_variable(current_instruction)
                self.increment_instruction_pointer()

             # Goto Instruction
            elif current_instruction.type == InstructionType.GOTO:
                self.execute_goto_instruction(current_instruction)

             # Jump If Instruction
            elif current_instruction.type == InstructionType.JUMP_IF:
                result = self.evaluate_condition(
                    current_instruction.condition, instruction)
                if result:
                    self.instruction_pointer = self.label_index_table[current_instruction.goto_label]
                else:
                    self.increment_instruction_pointer()

            # Jump if not Instruction
            elif current_instruction.type == InstructionType.JUMP_IF_NOT:
                result = self.evaluate_condition(
                    current_instruction.condition, current_instruction)
                if not result:
                    self.instruction_pointer = self.label_index_table[current_instruction.goto_label]
                else:
                    self.increment_instruction_pointer()

            # Label Instruction
            elif current_instruction.type == InstructionType.LABEL:
                self.increment_instruction_pointer()

    def build_label_index_table(self, instructions):
        for index, instruction in enumerate(instructions):
            if instruction.type == InstructionType.LABEL:
                self.label_index_table[instruction.lable_name] = index
        return instruction

    def evaluate_condition(self, condition, instruction):
        #print(f"eval {condition}")
        tokens = Lexer().tokenize(condition.strip('"'))
        final_condition = ""
        for token in tokens:
            if token.token_type == TokenType.IDENTIFICATION:
                symbol_table = self.find_symbol_table(
                    token.match, instruction.statement)
                symbol_entry = symbol_table.get_entry_value(token.match)
                final_condition += str(symbol_entry.value)
            else:
                final_condition += str(token.match)
        result = Evaluator().evaluate(final_condition)
        return result

    def execute_goto_instruction(self, current_instruction):
        self.instruction_pointer = self.label_index_table[current_instruction.goto_label]

    def handle_variable(self, instruction):
        """ handle variable instruction """

        #print(f"handling variable {instruction}")

        variable_expression = instruction.variable_expression
        variable_value = variable_expression.split("=")[1]

        tokens = Lexer().tokenize(variable_value)

        if len(tokens) == 1:
            # TODO handle case where x = y not only x = 10
            if tokens[0].token_type == TokenType.IDENTIFICATION:
                symbol_table = self.find_symbol_table(
                    variable_value, instruction.variable_statement)

            else:
                value = Evaluator().evaluate(variable_value)
                name = instruction.variable_name
                symbol_table = self.find_symbol_table(
                    name, instruction.variable_statement)
                symbol_table.modify_entry(name, value)
        else:
            final_expression = ""
            for token in tokens:
                if token.token_type == TokenType.IDENTIFICATION:
                    symbol_table = self.find_symbol_table(
                        token.match, instruction.variable_statement)
                    symbol = symbol_table.get_entry_value(token.match)
                    final_expression += str(symbol.value)
                    pass
                else:
                    final_expression += str(token.match)
                pass
            value = Evaluator().evaluate(final_expression)
            name = instruction.variable_name
            symbol_table = self.find_symbol_table(
                name, instruction.variable_statement)
            symbol_table.modify_entry(name, value)

    def find_symbol_table(self, name: str, statement):
        stmt = statement
        # pointer that keeps going up.
        if (isinstance(stmt, For)
            or isinstance(stmt, While)
            or isinstance(stmt, If)
            or isinstance(stmt, ElseIf)
            or isinstance(stmt, Else)
            or isinstance(stmt, ExecutionTree)):
            if statement.symbols_table and statement.symbols_table.get_entry_value(name):
                return statement.symbols_table

        ptr = statement.parent
        while True:

            if isinstance(ptr, ConditionStatement):
                ptr = ptr.parent
            if ptr.symbols_table.get_entry_value(name):
                return ptr.symbols_table

            if isinstance(ptr, ExecutionTree):
                break
            ptr = ptr.parent
        pass

    def increment_instruction_pointer(self):
        """
        Increment Instruction Pointer by 1
        """
        self.instruction_pointer += 1

    def execute_echo_instruction(self, instruction: EchoInstruction):
        """ Execute Echo Instruction
        Args:
            instruction:
        """
        tokens = Lexer().tokenize(instruction.echo_string.strip('"'), ignore_unknown=True, keep_spaces=True)
        final_echo_string = ""
        for token in tokens:
            if token.token_type == TokenType.IDENTIFICATIONBETWEENBRSCKETS:
                var_name = token.match
                var_name = var_name.strip("{")
                var_name = var_name.strip("}")
                symbol_table = self.find_symbol_table(
                    var_name, instruction.statement)
                value = symbol_table.get_entry_value(var_name)
                final_echo_string += str(value.value)
            else:
                final_echo_string += token.match
        print(final_echo_string)
