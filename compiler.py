# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.
"""

Compiler Library

"""

from instructions.instruction import EchoInstruction, Instruction, InstructionType
from statements.break_statement import Break
from statements.condition_statement import ConditionStatement
from statements.echo_statement import Echo
from statements.else_statement import Else
from statements.elseif_statement import ElseIf
from statements.end_for_loop import EndFor
from statements.end_while_statement import EndWhile
from statements.endif_statement import Fi
from statements.for_loop_statement import For
from statements.if_statement import If
from statements.variable_statement import Variable
from statements.while_statement import While


class Compiler(object):
    """Compiler Class"""

    def __init__(self) -> None:
        """Init Function"""
        self.instruction_list = []

    def build_instructions_list(self, execution_tree: list) -> list:
        """ Compile statements into instructions
        Args:
            execution_tree: list of statements   
        Returns:
            list of instructions
        """

        if not execution_tree:
            return

        """Depth first search"""
        for statement in execution_tree:

            print(f"statement is {statement.type}")

            # Recursive Call to traverse execution tree
            if isinstance(statement, If) or \
                    isinstance(statement, ElseIf) or \
                    isinstance(statement, Else) or \
                    isinstance(statement, For) or \
                    isinstance(statement, While):

                self.build_instructions_list(statement.statements)

            elif isinstance(statement, ConditionStatement):
                if statement.if_statmenet:
                    self.build_instructions_list(
                        statement.if_statmenet.statements)
                if statement.elseif_statements:
                    self.build_instructions_list(statement.elseif_statements)
                if statement.else_statement:
                    self.build_instructions_list(
                        statement.else_statement.statements)

            elif isinstance(statement, Echo):
                instruction = EchoInstruction(InstructionType.ECHO)
                instruction.echo_string = statement.echo_string
                self.instruction_list.append(instruction)

            elif isinstance(statement, EndFor) or \
                isinstance(statement, EndWhile):

                pass

    def compile(self, statements: list) -> list:
        """ Compile statements into instructions
        Args:
            statements: list of statements   
        Returns:
            execution tree
        """

        execution_tree = []
        stack = []

        for statement in statements:

            if  isinstance(statement, ElseIf) or \
                isinstance(statement, Else) or \
                isinstance(statement, For) or \
                isinstance(statement, While):

                stack.append(statement)
                
            if  isinstance(statement, Echo) or \
                isinstance(statement, Variable) or \
                isinstance(statement, Break):

                self._handle_oneline_statement(execution_tree, stack, statement)

            if isinstance(statement, If):
                self._handle_if(stack, statement)

            if isinstance(statement, Fi):
                self._handle_endif(execution_tree, stack)

            if isinstance(statement, EndFor):
                self._handle_endfor(execution_tree, stack)

            if isinstance(statement, EndWhile):
                self._handle_endwhile(execution_tree, stack)

        return execution_tree

    def _handle_endif(self, execution_tree, stack):
        # pop from stack.
        clause = stack.pop()
        if_statement_stack = []

        while not isinstance(clause, ConditionStatement):
            if_statement_stack.append(clause)
            clause = stack.pop()

        ifstatement = if_statement_stack.pop()
        if not isinstance(ifstatement, If):
            raise Exception("case can't happen")
        clause.if_statmenet = ifstatement

        while if_statement_stack:
            stack_element = if_statement_stack.pop()
            if isinstance(stack_element, ElseIf):
                clause.elseIfStatement.append = stack_element
            if isinstance(stack_element, Else):
                clause.else_statement = stack_element
                        
        if stack:
            stack[-1].statements.append(clause)
        else:
            execution_tree.append(clause)

    def _handle_if(self, stack, statement):
        conditon = ConditionStatement(statement, [], [])
        stack.append(conditon)
        stack.append(statement)

    def _handle_oneline_statement(self, execution_tree, stack, statement):
        if stack:
            stack[-1].statements.append(statement)
        else:
            execution_tree.append(statement)

    def _handle_endfor(self, execution_tree, stack):
        forloop = stack.pop()
        if stack:
            stack[-1].statements.append(forloop)
        else:
            execution_tree.append(forloop)

    def _handle_endwhile(self, execution_tree, stack):
        whileloop = stack.pop()
        if stack:
            stack[-1].statements.append(whileloop)
        else:
            execution_tree.append(whileloop)
