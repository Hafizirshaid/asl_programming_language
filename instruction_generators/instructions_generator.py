# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

"""

Instruction Generator Class

Converts execution tree into executable instructions list

"""


from compiler.compiler import ExecutionTree
from exceptions.language_exception import UnexpectedError
from instructions.instruction import (EchoInstruction, GotoInstruction,
                                      InputInstruction, Instruction,
                                      InstructionType, JumpIfNotInstruction,
                                      LabelInstruction, VariableInstruction)
from statements.statement import (Break, ConditionStatement, Continue, Echo,
                                  For, Input, Variable, While)


class InstructionsGenerator:
    """ Instructions Generator Class

    Generate executable instructions based on execution tree generated from the compiler.

    Class Attributes:
        instruction_list: instruction list to be generated
        label_counter: label counter
        execution_tree: execution tree to be converted to instructions list
        start_label_loop_stack: start loop stack to store start of loop label
        end_label_loop_stack: end loop stack to store end of loop label

    """

    def __init__(self) -> None:
        """ Instructions Generator Class Constructor """

        self.instruction_list = []
        self.label_counter = 0
        self.execution_tree = None
        self.start_label_loop_stack = []
        self.end_label_loop_stack = []

    def create_label_tag(self):
        """ Create Label Tag and increment label counter.
        Args:
            None
        Returns:
            New Label string
        """
        self.label_counter += 1
        return f"Label_{self.label_counter}"

    def generate_label(self):
        """ This Method Generate Label Instruction
        Args:
            None
        Returns:
            LabelInstruction
        """
        return LabelInstruction(self.create_label_tag())

    def _add_instruction(self, instruction: Instruction):
        """
        This method adds instruction to instructions list
        Args:
            instruction: instruction to be added to instruction_list
        Returns:
            None
        """
        self.instruction_list.append(instruction)

    def generate_instructions(self, execution_tree: ExecutionTree) -> list:
        """ Compile statements into instructions
        Args:
            execution_tree: execution tree object that contains statements tree.
        Returns:
            list of instructions generated from execution tree
        """

        self.execution_tree = execution_tree

        # if none or no elements in execution tree, return empty list.
        if not execution_tree or not execution_tree.tree:
            return []

        return self.build_instructions_list(execution_tree.tree)

    def build_instructions_list(self, execution_tree: list) -> list:
        """ Compile statements into instructions
        Args:
            execution_tree: list of statements
        Returns:
            list of instructions
        """

        # for each statement in execution tree, generate instructions
        for statement in execution_tree:

            # For Statement
            if isinstance(statement, For):
                self.generate_for_loop(statement)

            # While Statement
            elif isinstance(statement, While):
                self.generate_while_statement(statement)

            # Condition Statement
            elif isinstance(statement, ConditionStatement):
                self.generate_condition_statement(statement)

            # Echo Statement
            elif isinstance(statement, Echo):
                self.generate_echo_statement(statement)

            # Input Statement
            elif isinstance(statement, Input):
                self.generate_input_statement(statement)

            # Variable Statement
            elif isinstance(statement, Variable):
                self.generate_variable_statement(statement)

            # Break Statement
            elif isinstance(statement, Break):
                self.generate_break_statement()

            # Continue Statement
            elif isinstance(statement, Continue):
                self.generate_continue_statement()

        return self.instruction_list

    def generate_continue_statement(self):
        """ Generate Continue loop statement
        Args:
            None
        Returns:
            None
        """

        # find parent for or while. create goto instruction to end of for
        # and while.
        # Continue statement should change instruction pointer to go to
        # start of the loop
        loop_start_label = self.start_label_loop_stack[-1]
        goto = GotoInstruction(loop_start_label.label_name)
        self._add_instruction(goto)

    def generate_break_statement(self):
        """ Generate Break loop statement
        Args:
            None
        Returns:
            None
        """

        # find loop parent for for loop or while loop.
        # create goto instruction to end of forloop and while loop
        # break statement should break the loop, should go to end label.
        loop_end_label = self.end_label_loop_stack[-1]
        goto = GotoInstruction(loop_end_label.label_name)
        self._add_instruction(goto)

    def generate_variable_statement(self, statement):
        """ create variable instruction and add to instructions list
        Args:
            statement: variable statement to be added
        Returns:
            None
        """

        var_inst = VariableInstruction(statement)
        #var_inst.variable_statement = statement
        self._add_instruction(var_inst)

    def generate_echo_statement(self, statement):
        """ Method to create echo instruction
        Args:
            statement: echo statement to be created
        Returns:
            None
        """

        instruction = EchoInstruction(InstructionType.ECHO, statement)
        instruction.echo_string = statement.echo_string
        self.instruction_list.append(instruction)

    def generate_input_statement(self, statement):
        """ Method to create input instruction
        Args:
            statement: input statement to be created
        Returns:
            None
        """

        instruction = InputInstruction(InstructionType.INPUT, statement)
        instruction.input_variable = statement.input_variable
        self.instruction_list.append(instruction)

    def generate_for_loop(self, statement):
        """
        This method builds for loop instructions structure as follows:

            For Loop Statement:
                code:
                    -----------------------
                    before statements
                    for(start; condition; increment)
                        statements inside for
                    endfor
                    after statements
                    -----------------------

                instructions:
                    -----------------------
                    before statements
                    start
                    Label_1:
                        Jump If $condition to Label_2
                        statements inside for
                    loop_increment_label:
                        increment
                        goto Label_1
                    Label_2:
                    after statements
                    -----------------------

        Args:
            statement: For loop statement to be created
        Returns:
            None
        """

        # create label_1
        label_1 = self.generate_label()
        self._add_instruction(label_1)

        # before increment label is necessary for continue statement,
        # in case of continue statement, loop variable should be incremented
        # after that it jumps to label_1 to continue the execution.
        before_increment_label = self.generate_label()
        self.start_label_loop_stack.append(before_increment_label)

        # create end of loop label
        label2 = self.generate_label()

        # Jump statement to be executed to determine if loop should continue
        # or not based on loop condition
        jump_for = JumpIfNotInstruction(label2.label_name, statement.loop_condition, statement)
        self._add_instruction(jump_for)

        # generate instruction for loop statements
        self.end_label_loop_stack.append(label2)

        # Build instructions for children statements inside for loop
        self.build_instructions_list(statement.statements)

        # before_increment_label should be added before loop increment statement.
        # this label will be used in case of continue statement to increment the for loop
        # variable and then check loop condition to determine weather the program should execute
        # the next iteration or not.
        self.instruction_list.insert(len(self.instruction_list) - 1, before_increment_label)
        self.start_label_loop_stack.pop()
        self.end_label_loop_stack.pop()

        # goto label_1 at the beginning of loop after incrementing variable
        goto_l1 = GotoInstruction(label_1.label_name)
        self._add_instruction(goto_l1)

        # End of Loop Label
        self._add_instruction(label2)

    def generate_while_statement(self, statement):
        """
        Create instructions for While loop statement
            WHILE LOOP
                code:
                    ----------------
                    before statements
                    while "condition"
                        Statements inside while loop
                    endwhile
                    After Statements
                    ----------------
                instructions:
                    ----------------
                    before statements
                    Label1:
                        Jump If Not "condition" To Label 2
                        Statements inside while loop
                        Goto Label1
                    L2:
                        After Statements
                    ----------------

        Args:
            statement: While loop statement to be created
        Returns:
            None
        """

        label_1 = self.generate_label()
        self.instruction_list.append(label_1)
        self.start_label_loop_stack.append(label_1)

        label2 = self.generate_label()
        jump = JumpIfNotInstruction(label2.label_name, statement.condition, statement)
        self.instruction_list.append(jump)
        self.end_label_loop_stack.append(label2)

        # call for children
        self.build_instructions_list(statement.statements)

        goto = GotoInstruction(label_1.label_name)
        self.instruction_list.append(goto)
        self.instruction_list.append(label2)

        self.start_label_loop_stack.pop()
        self.end_label_loop_stack.pop()

    def generate_condition_statement(self, statement):
        """ Create Condition statement, it handles if statement, else statement and
            else statement.

            Code:
                -------------------
                Before_statements
                if c1
                    if1_statements
                elif c2
                    elseif2_statements
                elif c3
                    elseif3_statements
                else
                    else_statements4
                fi
                After_statements
                -------------------
            Instructions:
                -------------------
                Before_statements
                label_1:
                    Jump If not c1 to Label2
                    if1_statements
                    jump to end_label
                Label_2
                    Jump If not c2 to Label3
                    elseif2_statements
                    jump to end_label
                Label_3
                    Jump If not c3 to Label4
                    elseif3_statements
                    jump to end_label
                Label_4
                    else_statements4
                    jump to end_label
                end_label
                After_statements
                -------------------

        Args:
            statement: condition statement that contains if,elseif and else statements
                        if is a mandatory statement, else if and else are optional
        Returns:
            None
        """

        # End label to indicate end of condition statement block
        end_label = self.generate_label()

        self.handle_if_condition(statement, end_label)
        self.handle_if_else_statements(statement, end_label)
        self.handle_else_statement(statement)
        self._add_instruction(end_label)

    def handle_else_statement(self, statement):
        """ generate instructions for else statement children statements
        Args:
            statement: else statement to be generated.
        Returns:
            None
        """
        if statement.else_statement:
            self.build_instructions_list(statement.else_statement.statements)
            pass

    def handle_if_else_statements(self, statement, end_label):
        """ Generate instructions for elseif statements inside statement.
            for each else if statement with condition, the following instructions
            will be generated:

            Code:
                -----------------
                elif condition
                    elseif_statements
                elseif condition 2
                    next_else_if_statement
                -----------------
            Instructions
                -----------------
                Label
                    Jump If not condition to Label_next
                    elseif_statements
                    jump to end_label
                -----------------

        Args:
            statement: condition statement that contains else if statements
            end_label: end of condition statement label
        Returns:
            None

        """

        if statement.elseif_statements:
            for else_if in statement.elseif_statements:
                label_3 = self.generate_label()
                jump2 = JumpIfNotInstruction(
                    label_3.label_name, else_if.condition, else_if)
                self._add_instruction(jump2)
                self.build_instructions_list(else_if.statements)

                goto_end = GotoInstruction(end_label.label_name)
                self._add_instruction(goto_end)

                self._add_instruction(label_3)

    def handle_if_condition(self, statement, end_label):
        """ Create instructions for if statement condition

        If Statement:
            code:
                --------------
                before statements
                if condition
                    statements inside if statement
                fi
                after statements
                --------------

            instructions:
                --------------
                before statements
                Label_1
                Jump if not condition to Label_2
                statements inside if statement
                goto end_label
                Label_2
                end_label
                --------------

        Args:
            statement: condition statement that contains if_statement,
                        if statement is mandatory statement, if if_statement is null
                        UnexpectedError will be thrown
            end_label: end label of condition block
        Returns:
            None
        Raises:
            UnexpectedError: when if_statement is None
        """

        if not statement.if_statement:
            raise UnexpectedError(
                "Unexpected state, if statement should not be none inside condition")

        label_1 = self.generate_label()
        self._add_instruction(label_1)
        label_2 = self.generate_label()
        jump = JumpIfNotInstruction(
            label_2.label_name, statement.if_statement.condition, statement.if_statement)
        self._add_instruction(jump)
        self.build_instructions_list(statement.if_statement.statements)
        goto_end = GotoInstruction(end_label.label_name)
        self._add_instruction(goto_end)
        self._add_instruction(label_2)

