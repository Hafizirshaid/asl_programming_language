# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

from statements.break_statement import Break
from statements.condition_statement import ConditionStatement
from statements.echo_statement import Echo
from statements.elseif_statement import ElseIf
from statements.else_statement import Else
from statements.end_for_loop import EndFor
from statements.endif_statement import Fi
from statements.end_while_statement import EndWhile
from statements.for_loop_statement import For
from statements.if_statement import If
from statements.variable_statement import Variable
from statements.while_statement import While


class Compiler(object):
    """Compiler Class"""

    def __init__(self) -> None:
        """Init Function"""
        pass

    def build_instructions_list(self, execution_tree: list) -> list:
        """ Compile statements into instructions
        Args:
            execution_tree: list of statements   
        Returns:
            list of instructions
        """

        """Depth first search"""
        for statement in execution_tree:
            if isinstance(statement, If) or \
                    isinstance(statement, ElseIf) or \
                    isinstance(statement, Else) or \
                    isinstance(statement, For) or \
                    isinstance(statement, While):
                self.build_instructions_list(statement.statements)

            print(f"statement is {statement.type}")

    def compile(self, statements: list) -> list:
        """ Compile statements into instructions
        Args:
            statements: list of statements   
        Returns:
            execution tree
        """

        """ Build Exectuion tree """
        execution_tree = []
        stack = []

        for statement in statements:

            if isinstance(statement, Echo) or \
                    isinstance(statement, Variable) or \
                    isinstance(statement, Break):

                if stack:
                    # add this to the last element in the stack.
                    stack[-1].statements.append(statement)
                    pass
                else:
                    execution_tree.append(statement)
                pass

            if isinstance(statement, If):
                conditon = ConditionStatement(statement, [], [])
                stack.append(conditon)
                stack.append(statement)
                pass

            if isinstance(statement, ElseIf):
                stack.append(statement)
                pass

            if isinstance(statement, Else):
                stack.append(statement)
                pass

            if isinstance(statement, Fi):

                # pop from stack.
                elm = stack.pop()
                ifstatementstack = []

                while not isinstance(elm, ConditionStatement):
                    ifstatementstack.append(elm)
                    elm = stack.pop()
                    pass

                ifstatement = ifstatementstack.pop()
                if not isinstance(ifstatement, If):
                    raise Exception("case can't happen")
                elm.ifstatmenet = ifstatement

                while ifstatementstack:
                    itm = ifstatementstack.pop()
                    if isinstance(itm, ElseIf):
                        elm.elseIfStatement.append = itm
                    if isinstance(itm, Else):
                        elm.elsestatement = itm
                if stack:
                    stack[-1].statements.append(elm)
                else:
                    execution_tree.append(elm)

            if isinstance(statement, For):
                stack.append(statement)
                pass

            if isinstance(statement, EndFor):
                # do work here.
                forloop = stack.pop()

                if stack:
                    stack[-1].statements.append(forloop)
                else:
                    execution_tree.append(forloop)
                pass

            if isinstance(statement, While):
                stack.append(statement)
                pass

            if isinstance(statement, EndWhile):

                whileloop = stack.pop()
                if stack:
                    stack[-1].statements.append(whileloop)
                else:
                    execution_tree.append(whileloop)
                pass

            pass
        return execution_tree
