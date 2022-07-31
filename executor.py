# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

"""

Executor Library

Contains methods to execute list of instructions to produce
program logical output.

"""

from compiler import ExecutionTree
from enhanced_expression_evalator import EnhancedExpressionEvaluator
from exceptions.language_exception import UnexpectedError, UnknownVariable
from expression_evaluator import Evaluator
from instructions.instruction import EchoInstruction, InputInstruction, InstructionType, VariableInstruction
from lexer import Lexer, TokenType
from statements.statement import ConditionStatement, Else, ElseIf, For, If, Variable, VariableType, While


class Executor(object):
    """

    Executor Class

    Execute List of instructions for a program

    Class Attributes:
        instruction_pointer: Pointer that points to the current instruction to be
                             executed by the instruction executor.

        label_index_table:   A dictionary that contains labels to indexes mapping

        execution_tree:      Execution tree that contains statement, it is needed in this
                             class in order to lookup symbols tables for variables assignment.
    """

    def __init__(self) -> None:
        """ Executor Class Constructor """

        self.instruction_pointer = 0
        self.label_index_table = {}
        self.execution_tree = None

    def execute(self, instructions, execution_tree):
        """
        Desc:
            Execute List of Instructions
        Args:
            instructions: instructions to be executed
            execution_tree: Execution Tree that contains statements to be executed
                            This is necessary to get access to symbols table
        Returns:
            program output
        """

        if not instructions:
            # if no instructions provided, return empty
            return

        self.execution_tree = execution_tree
        self.build_label_index_table(instructions)

        while self.instruction_pointer < len(instructions):
            current_instruction = instructions[self.instruction_pointer]
            self.execute_instruction(current_instruction)
        return

    def execute_instruction(self, current_instruction):
        """ Execute a given instruction based on instruction type
        Args:
            current_instruction: Instruction to be executed
        Returns:
            None
        """

        # Echo Instruction
        if current_instruction.type == InstructionType.ECHO:
            self.execute_echo_instruction(current_instruction)
            self.increment_instruction_pointer()

        # Input Instruction
        elif current_instruction.type == InstructionType.INPUT:
            self.execute_input_instruction(current_instruction)
            self.increment_instruction_pointer()

        # Variable Instruction
        elif current_instruction.type == InstructionType.VARIABLE:
            self.execute_variable_instruction(current_instruction)
            self.increment_instruction_pointer()

        # Goto Instruction
        elif current_instruction.type == InstructionType.GOTO:
            self.execute_goto_instruction(current_instruction)

        # Jump If Instruction
        elif current_instruction.type == InstructionType.JUMP_IF:
            result = self.evaluate_condition(
                    current_instruction.condition, current_instruction)
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

        return

    def build_label_index_table(self, instructions):
        """ Builds label to to index lookup table and store them
            in label_index_table dictionary
        Args:
            instructions: list of instructions that contains labels
        Returns:
            None
        """

        for index, instruction in enumerate(instructions):
            if instruction.type == InstructionType.LABEL:
                self.label_index_table[instruction.lable_name] = index
        return

    def evaluate_condition(self, condition, instruction):
        """ Evaluate the result of a given condition
        Args:
            condition: Condition string to be evaluated
            instruction: Instruction that contains current statement to be used
                         to lookup symbols table
        Returns:
            Condition Result
        """

        tokens = Lexer().tokenize_text(condition.strip('"'))

        # If condition contains variables, they should be substituted by
        # their values in the symbols table
        final_condition = ""
        for token in tokens:
            if token.token_type == TokenType.IDENTIFICATION:

                # Variable found, Lookup variable value in symbol tables
                symbol_table = self.find_symbol_table(token.match, instruction.statement)
                symbol_entry = symbol_table.get_entry_value(token.match)

                # Substitute variable value in final condition
                final_condition += str(symbol_entry.value)
            else:
                final_condition += str(token.match)

        # Evaluate final result of condition
        result = Evaluator().evaluate(final_condition)
        return result

    def execute_goto_instruction(self, current_instruction):
        """ Execute GoTo label instruction
        Args:
            current_instruction: the instruction that contains goto label
        Returns:
            None
        """
        self.instruction_pointer = self.label_index_table[current_instruction.goto_label]

    def execute_variable_instruction(self, instruction: VariableInstruction):
        """ Execute variable assignment instruction
        Args:
            instruction: Variable Instruction to be executed
        Returns:
            None
        """

        # Calculate Variable name and variable value
        # variable_expression = instruction.variable_expression
        variable_name = instruction.variable_statement.variable_name
        variable_value = instruction.variable_statement.variable_value

        operation = instruction.variable_statement.operation

        # Tokenize variable value to make sure variable can be evaluated
        tokens = Lexer().tokenize_text(variable_value)

        if len(tokens) == 1:
            self.handle_one_token_variable(instruction, variable_name, variable_value, tokens, operation)
        else:
            self.handle_multiple_tokens_variable(instruction, tokens, operation)
        return

    def handle_multiple_tokens_variable(self, instruction, tokens, operation):
        """ Evaluate multiple tokens variable expression.
            For example: x = y + z
            This method will determine the result of y + z and store it in x
        Args:
            instruction: variable instruction that contains the variable statement
            tokens: variable statement tokens to be evaluated.
        Returns:
            None
        """

        final_expression = ""

        is_concatenation = False
        for token in tokens:
            if token.token_type == TokenType.IDENTIFICATION:
                # Substitute variable values in final expression to be evaluated
                symbol_table = self.find_symbol_table(token.match, instruction.variable_statement)
                symbol = symbol_table.get_entry_value(token.match)

                if symbol.type == TokenType.STRING:
                    # Variables should be concatenated rather than evaluating them since
                    # there is a string value
                    is_concatenation = True

                final_expression += str(symbol.value)
                pass
            else:
                # if token.token_type != TokenType.ADD:
                final_expression += str(token.match)
            pass

        if is_concatenation:
            value = final_expression
        else:
            value = EnhancedExpressionEvaluator().evaluate(final_expression)
        name = instruction.variable_name

        # Store value of variable
        self.store_variable(name, value, operation, instruction)

    def handle_one_token_variable(self, instruction, variable_name, variable_value, tokens, operation):
        """ Evaluate one token variable assignment, example:
            x = y or x = 1
        Args:
            instruction: instruction that contains variable statement.
            variable_name: variable name
            variable_value: variable value, could be a new value to be assigned or
                            another variable that it's value should be assigned to variable_name
            tokens: one token that contains variable y.
        Returns:
            None
        """

        # if one token found, make sure the value is not another variable
        if tokens[0].token_type == TokenType.IDENTIFICATION:

            # Variable value is an assignment to another variable
            symbol_table = self.find_symbol_table(variable_value, instruction.variable_statement)

            if not symbol_table:
                raise UnknownVariable(f"Variable not found {variable_value}")

            new_value = symbol_table.get_entry_value(variable_value)

            self.store_variable(variable_name, new_value.value, operation, instruction)
        else:
            # variable value is normal value not variable assignment to another variable
            self.store_variable(instruction.variable_name, variable_value, operation, instruction)

    def store_variable(self, variable_name, variable_value, operation, instruction):
        """ Store Variable value in the right location and apply operation
        Args:
            variable_name: name of the variable
            variable_value: new variable value
            operation: operation to be applied, =, +=, -=, *= or /=
            instruction: current instruction holding the variable statement
        Returns:
            None
        """

        symbols_table = self.find_symbol_table(variable_name, instruction.variable_statement)
        new_variable_value = variable_value

        if operation != TokenType.EQUAL:
            # Apply Operation

            old_value = symbols_table.get_entry_value(variable_name)

            if old_value:
                old_value = old_value.value

            if operation == TokenType.PLUSEQUAL:
                new_variable_value = float(old_value) + float(variable_value)

            elif operation == TokenType.SUBEQUAL:
                new_variable_value = float(old_value) - float(variable_value)

            elif operation == TokenType.MULTEQUAL:
                new_variable_value = float(old_value) * float(variable_value)

            elif operation == TokenType.DIVEQUAL:
                new_variable_value = float(old_value) / float(variable_value)

        symbols_table.modify_entry(variable_name, new_variable_value)

    def find_symbol_table(self, name: str, statement):
        """ Find Symbol table that contains variable name

        Args:
            name: variable name to be found
            statement: A statement that can be used to lookup symbols table in
                       the execution tree.
        Returns:
            Symbols table that contains variable {name}
        """

        if (isinstance(statement, For)
            or isinstance(statement, While)
            or isinstance(statement, If)
            or isinstance(statement, ElseIf)
            or isinstance(statement, Else)
            or isinstance(statement, ExecutionTree)):

            if (statement.symbols_table
                and statement.symbols_table.get_entry_value(name)):
                # if the given statement is a scope statement, then
                # lookup variable inside it's symbol tables, if it contains the value,
                # return it directly, otherwise, lookup value in parents symbols tables.
                return statement.symbols_table

        # Go up one step
        pointer = statement.parent

        while True:

            if isinstance(pointer, ConditionStatement):
                # Skip Condition statement as it doesn't contain
                # Symbols table, it is used only as an aggregator for
                # if, elseif, else statements
                pointer = pointer.parent

            if pointer.symbols_table.get_entry_value(name):
                return pointer.symbols_table

            if isinstance(pointer, ExecutionTree):
                # if we hit the execution tree, no more parents to check
                # Should stop here.
                break

            # Go up one step
            pointer = pointer.parent

        # If we reach this point, then variable does not exist in symbols tables
        return None

    def increment_instruction_pointer(self):
        """
        Increment Instruction Pointer by 1
        Args:
            None
        Returns:
            None
        """
        self.instruction_pointer += 1

    def execute_echo_instruction(self, instruction: EchoInstruction):
        """ Execute Echo Instruction
        Args:
            instruction: Print instruction that contains echo string
        Returns:
            None
        """

        # Tokenize echo string and keep unknown tokens and spaces.
        # Echo string might contain anything, this is needed only to find if
        # echo string contains variables so they can be substituted.
        tokens = Lexer().tokenize_text(
            instruction.echo_string.strip('"'),
            keep_unknown=True,
            keep_spaces=True)

        final_echo_string = ""

        for token in tokens:
            if token.token_type == TokenType.IDENTIFICATIONBETWEENBRSCKETS:
                # If echo string contains a variable between {} for example
                # {variable_name}, Substitute variable_name with it's value

                var_name = token.match
                var_name = var_name.strip("{}")

                symbol_table = self.find_symbol_table(var_name, instruction.statement)

                if not symbol_table:
                    raise UnknownVariable(f"Variable Not Found {var_name}")

                value = symbol_table.get_entry_value(var_name)
                final_echo_string += str(value.value)
            else:
                final_echo_string += token.match

        # Print final echo string
        print(final_echo_string)

        return

    def execute_input_instruction(self, instruction: InputInstruction):
        """ Execute Input Instruction
        Args:
            instruction: Input instruction that contains variable to read from keyboard
        Returns:
            None
        """

        variable_name = instruction.input_variable
        symbol_table = self.find_symbol_table(variable_name, instruction.statement)

        if not symbol_table:
            raise UnknownVariable(f"Variable Not Found {variable_name}")

        # input from keyboard
        input_value = input()
        symbol_table.modify_entry(variable_name, input_value)
