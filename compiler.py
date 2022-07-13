# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

"""

Compiler Library

"""

from statements.statement import *
from symbols.symbols_table import SymbolTable


class ExecutionTree:

    def __init__(self) -> None:
        self.tree = []
        self.symbols_table = SymbolTable()
        self.parent = None

    def append(self, item):
        self.tree.append(item)


class Compiler(object):
    """Compiler Class"""

    def __init__(self) -> None:
        """Init Function"""
        pass

    def compile(self, statements: list) -> list:
        """ Compile statements into execution tree
        Args:
            statements: list of statements
        Returns:
            execution tree
        """

        execution_tree = ExecutionTree()
        stack = []

        for statement in statements:
            if (isinstance(statement, ElseIf) or
                isinstance(statement, Else) or
                isinstance(statement, While)):
                stack.append(statement)

            if isinstance(statement, For):
                # add for loop variable
                if statement.loop_initial_variable:
                    loop_initial_variable = Variable(statement.loop_initial_variable)
                    self._handle_one_line_statement(execution_tree, stack, loop_initial_variable)

                stack.append(statement)
                #print(statement)
                pass
            if (isinstance(statement, Echo) or
                isinstance(statement, Break)):

                self._handle_one_line_statement(
                    execution_tree, stack, statement)

            if isinstance(statement, Variable):
                if stack:
                    stack[-1].statements.append(statement)
                else:
                    execution_tree.append(statement)
                pass

            if isinstance(statement, If):
                self._handle_if(stack, statement)

            if isinstance(statement, Fi):
                self._handle_endif(execution_tree, stack)

            if isinstance(statement, EndFor):
                self._handle_end_forloop_statement(execution_tree, stack)

            if isinstance(statement, EndWhile):
                self._handle_end_statement(execution_tree, stack)


        # TODO remove this function, try to set parents when looping thru 
        # list of statements and adding elements to stack
        self.set_parents(execution_tree)

        # TODO store variable names in symbol table without value, just 
        # store the right location for each varaible
        self.store_variables_in_symbols_table(execution_tree)

        return execution_tree

    def store_variables_in_symbols_table(self, execution_tree: ExecutionTree):

        for i in execution_tree.tree:
            if isinstance(i, Variable):
                # don't store values yet, symbol table should contains the values
                # after executing the variable instruction
                execution_tree.symbols_table.add_entry(i.variable_name, "")
                i.symbols_table = execution_tree.symbols_table

            if (isinstance(i, For) or
                isinstance(i, While) or
                isinstance(i, If) or
                isinstance(i, ElseIf) or
                isinstance(i, Else)):
                self.store_variables_in_symbols_table_for_statements(i.statements)
                pass

            if isinstance(i, ConditionStatement):
                self.store_variables_in_symbols_table_for_statements(i.if_statmenet.statements)

                for elifs in i.elseif_statements:
                    self.store_variables_in_symbols_table_for_statements(elifs.statements)

                if i.else_statement:
                    self.store_variables_in_symbols_table_for_statements(i.else_statement.statements)

        pass

    def find_symbol(self, i:Variable):

        ptr = i.parent
        symbol = None
        while ptr:
            if (isinstance(ptr, For) or
                isinstance(ptr, While) or
                isinstance(ptr, If) or
                isinstance(ptr, ElseIf) or
                isinstance(ptr, Else) or 
                isinstance(ptr, ExecutionTree)):

                if ptr.symbols_table.get_entry_value(i.variable_name):
                    symbol = ptr.symbols_table
                    break

            if isinstance(ptr, ConditionStatement):
                ptr = ptr.parent
                continue
            # Go Up
            ptr = ptr.parent
            pass

        # symbol = None
        # if isinstance(ptr, ExecutionTree):
        #     return ptr.symbols_table

        # while not isinstance(ptr, ExecutionTree):
        #     if (isinstance(ptr, For) or
        #         isinstance(ptr, While) or
        #         isinstance(ptr, If) or
        #         isinstance(ptr, ElseIf) or
        #         isinstance(ptr, Else)):
        #         if ptr.symbols_table.get_entry_value(i.variable_name):
        #             symbol = ptr.symbols_table
        #             break

        #     ptr = ptr.parent
        #     if isinstance(ptr, ConditionStatement):
        #         ptr = ptr.parent
        # if symbol is None:
        #     if ptr.symbols_table.get_entry_value(i.variable_name):
        #         symbol = ptr.symbols_table
        return symbol

    def store_variables_in_symbols_table_for_statements(self, statements:list[Statement]):
        for i in statements:
            if isinstance(i, Variable):
                # find in all parents if symbol exists in any symbol tables, 
                # if found do nohting
                symbol = self.find_symbol(i)
                # if not found, store it in parents symbol table
                if not symbol:
                    i.parent.symbols_table.add_entry(i.variable_name, "")
                    i.symbols_table = i.parent.symbols_table
                pass
            if (isinstance(i, For) or
                isinstance(i, While) or
                isinstance(i, If) or
                isinstance(i, ElseIf) or
                isinstance(i, Else)):
                self.store_variables_in_symbols_table_for_statements(i.statements)
                pass

            if isinstance(i, ConditionStatement):
                self.store_variables_in_symbols_table_for_statements(i.if_statmenet.statements)
                for i in i.elseif_statements:
                    self.store_variables_in_symbols_table_for_statements(i.statements)
                if i.else_statement:
                    self.store_variables_in_symbols_table_for_statements(i.else_statement.statements)

            pass

    def set_parents(self, execution_tree: ExecutionTree):

        for stmt in execution_tree.tree:

            stmt.parent = execution_tree

            if (isinstance(stmt, For) or
                isinstance(stmt, While) or
                isinstance(stmt, If) or
                isinstance(stmt, ElseIf) or
                isinstance(stmt, Else)):
                #for i in stmt.statements:
                self.set_parent_for_statements(stmt, stmt.statements)

            if isinstance(stmt, ConditionStatement):
                stmt.if_statmenet.parent = stmt
                self.set_parent_for_statements(
                    stmt.if_statmenet,
                    stmt.if_statmenet.statements)
                for i in stmt.elseif_statements:
                    i.parent = stmt
                    self.set_parent_for_statements(i, i.statements)

                if stmt.else_statement:
                    stmt.else_statement.parent = stmt
                    self.set_parent_for_statements(
                        stmt.else_statement,
                        stmt.else_statement.statements)
                pass
        pass

    def set_parent_for_statements(self, parent, statements):

        for stmt in statements:
            stmt.parent = parent
            if (isinstance(stmt, For) or
                isinstance(stmt, While) or
                isinstance(stmt, If) or
                isinstance(stmt, ElseIf) or
                isinstance(stmt, Else)):
                self.set_parent_for_statements(stmt, stmt.statements)

            if isinstance(stmt, ConditionStatement):
                stmt.if_statmenet.parent = stmt
                self.set_parent_for_statements(
                    stmt.if_statmenet,
                    stmt.if_statmenet.statements)

                for elif_statements in stmt.elseif_statements:
                    elif_statements.parent = stmt

                    self.set_parent_for_statements(
                        elif_statements,
                        elif_statements.statements)

                if stmt.else_statement:
                    stmt.else_statement.parent = stmt

                    self.set_parent_for_statements(
                            stmt.else_statement,
                            stmt.else_statement.statements)

                pass
        pass

    def _handle_endif(self, execution_tree: ExecutionTree, stack):
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
                clause.elseif_statements.append(stack_element)
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

    def _handle_one_line_statement(self, execution_tree, stack, statement):
        if stack:
            stack[-1].statements.append(statement)
        else:
            execution_tree.append(statement)

    def _handle_end_statement(self, execution_tree, stack):
        end = stack.pop()
        if stack:
            stack[-1].statements.append(end)
        else:
            execution_tree.append(end)

    def _handle_end_forloop_statement(self, execution_tree, stack):
        end = stack.pop()
        increment_variable = Variable(end.loop_increment)
        end.statements.append(increment_variable)
        if stack:
            stack[-1].statements.append(end)
        else:
            execution_tree.append(end)


