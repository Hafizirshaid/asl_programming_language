# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

"""
Instruction Generator Class

"""
from compiler import ExecutionTree
from instructions.instruction import (EchoInstruction, GotoInstruction,
                                      Instruction, InstructionType,
                                      JumpIfInstruction, JumpIfNotInstruction,
                                      LabelInstruction, VariableInstruction)
from statements.statement import *


class InstructionsGenerator:

    def __init__(self) -> None:
        self.instruction_list = []
        self.label_counter = 0
        self.execution_tree = None
        self.start_label_loop_stack = []
        self.end_label_loop_stack = []
        pass

    def create_label_tag(self):
        """ Create Label Tag"""
        self.label_counter += 1
        return f"Label_{self.label_counter}"

    def generate_label(self):
        """ This Method Generate Label Instruction"""
        return LabelInstruction(self.create_label_tag())

    def add_instruction(self, instruction: Instruction):
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
            if isinstance(statement, For):
                self.handle_for_loop(statement)
            elif isinstance(statement, While):
                self.handle_while_statement(statement)
            elif isinstance(statement, ConditionStatement):
                self.handle_condition_statement(statement)
            elif isinstance(statement, Echo):
                self.handle_echo_statement(statement)
            elif isinstance(statement, Variable):
                self.handle_variable_statement(statement)
            elif isinstance(statement, Break):
                # TODO implement this
                # find parent for or while. create goto instruction to end of for
                # and while
                loop_end_label = self.end_label_loop_stack[-1]
                goto = GotoInstruction(loop_end_label.lable_name)
                self.add_instruction(goto)
                pass
            elif isinstance(statement, Continue):
                # TODO implement this
                # find parent for or while. create goto instruction to end of for
                # and while
                loop_start_label = self.start_label_loop_stack[-1]
                goto = GotoInstruction(loop_start_label.lable_name)
                self.add_instruction(goto)
                pass
        return self.instruction_list

    def handle_variable_statement(self, statement):
        """ Method to create variable instruction """
        var_inst = VariableInstruction(statement.variable_expression)
        var_inst.variable_statement = statement
        self.add_instruction(var_inst)

    def handle_echo_statement(self, statement):
        """ Method to create echo instruction """
        instruction = EchoInstruction(InstructionType.ECHO, statement)
        instruction.echo_string = statement.echo_string
        self.instruction_list.append(instruction)

    def handle_for_loop(self, statement):
        """
        This method builds for loop instructions structure as follows:

            For Loop Statement:

                code:
                    before statements
                    for(start; condition; increment)
                        statements inside for
                    endfor
                    after statements

                instructions:
                    before statements
                    start
                    Label_1:
                        Jump If $condition to Label_2
                        statements inside for
                    loop_increment_label:
                        increment
                        goto Label_1
                    Label_2:
                    after statments
                """

        label_1 = self.generate_label()
        self.add_instruction(label_1)
        before_increment_label = self.generate_label()

        self.start_label_loop_stack.append(before_increment_label)
        label2 = self.generate_label()
        jump_for = JumpIfNotInstruction(label2.lable_name, statement.loop_condition, statement)
        self.add_instruction(jump_for)
        # generate instruction for loop statements
        self.end_label_loop_stack.append(label2)
        self.build_instructions_list(statement.statements)
        self.instruction_list.insert(len(self.instruction_list) - 1, before_increment_label)
        self.start_label_loop_stack.pop()
        self.end_label_loop_stack.pop()

        goto_l1 = GotoInstruction(label_1.lable_name)
        self.add_instruction(goto_l1)

        self.add_instruction(label2)

    def handle_while_statement(self, statement):
        """
        Create instructions for While loop statement
            WHILE LOOP
                code:
                    before statements
                    while "conditon"
                        Statments inside while loop
                    endwhile
                    After Statements
                instructions:
                    before statements
                    Label1:
                        Jump If Not "condition" To Label 2
                        Statments inside while loop
                        Goto Label1
                    L2:
                        After Statements
                """
        label_1 = self.generate_label()
        self.instruction_list.append(label_1)
        self.start_label_loop_stack.append(label_1)

        label2 = self.generate_label()
        jump = JumpIfNotInstruction(label2.lable_name, statement.condition, statement)
        self.instruction_list.append(jump)
        self.end_label_loop_stack.append(label2)

        # call for children
        self.build_instructions_list(statement.statements)

        goto = GotoInstruction(label_1.lable_name)
        self.instruction_list.append(goto)
        self.instruction_list.append(label2)

        self.start_label_loop_stack.pop()
        self.end_label_loop_stack.pop()

    def handle_condition_statement(self, statement):
        """handle_condition_statement"""
        end_label = self.generate_label()
        self.handle_if_condition(statement, end_label)
        self.handle_if_else_statements(statement, end_label)
        self.handle_else_statement(statement)
        self.add_instruction(end_label)

    def handle_else_statement(self, statement):
        """ handle_else_statement

        Else Statement:
            Instructions:

        """
        if statement.else_statement:
            self.build_instructions_list(statement.else_statement.statements)
            pass

    def handle_if_else_statements(self, statement, end_label):
        """ handle_if_else_statements """
        if statement.elseif_statements:
            for else_if in statement.elseif_statements:
                label_3 = self.generate_label()
                jump2 = JumpIfNotInstruction(
                    label_3.lable_name, else_if.condition, else_if)
                self.add_instruction(jump2)
                self.build_instructions_list(else_if.statements)

                goto_end = GotoInstruction(end_label.lable_name)
                self.add_instruction(goto_end)

                self.add_instruction(label_3)

    def handle_if_condition(self, statement, end_label):
        """ Create instructions for if statement condition

        If Statement:
            code:
                before statements
                if conditon
                    statmenets inside if statement
                fi
                after statements

            instructions:
                before statements
                Label_1
                Jump if not condition to Label_2
                statements inside if statement
                goto end_label
                Label_2
                end_label
        """

        if not statement.if_statmenet:
            raise Exception(
                "Unexprected state, if statement should not be none inside conditon")

        label_1 = self.generate_label()
        self.add_instruction(label_1)
        label_2 = self.generate_label()
        jump = JumpIfNotInstruction(
            label_2.lable_name, statement.if_statmenet.condition, statement.if_statmenet)
        self.add_instruction(jump)
        self.build_instructions_list(statement.if_statmenet.statements)
        goto_end = GotoInstruction(end_label.lable_name)
        self.add_instruction(goto_end)
        self.add_instruction(label_2)
