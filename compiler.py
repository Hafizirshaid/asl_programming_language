# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

"""

Compiler Library

"""

from statements.statement import *
from symbols.symbols_table import SymbolTable


class ExecutionTree:
    """ Execution Tree Class """

    def __init__(self) -> None:
        """ Execution Tree Constructor """
        self.tree = []
        self.symbols_table = SymbolTable()
        self.parent = None

    def append(self, statement):
        """ Appends a statement to execution tree list
        Args:
            statement: statement to be added to list
        Returns:
            None
        """
        self.tree.append(statement)


class Compiler(object):
    """Compiler Class"""

    def __init__(self) -> None:
        """ Compiler Constructor"""
        pass

    def compile(self, statements: list) -> list:
        """ Compiles statements into execution tree
        Args:
            statements: list of statements
        Returns:
            execution tree
        """

        if not statements:
            return []

        execution_tree = ExecutionTree()
        stack = []
        for statement in statements:
            self.compile_statement(execution_tree, stack, statement)

        # If stack is not empty, that menas there are some statements without end
        # statement in the code
        if stack:
            raise Exception("Syntax Error, no end for statements, ", stack)

        # TODO remove this function, try to set parents when looping thru
        # list of statements and adding elements to stack
        self.set_parents(execution_tree)

        # TODO store variable names in symbol table without value, just
        # store the right location for each varaible
        self.store_variables_in_symbols_table(execution_tree)

        return execution_tree

    def compile_statement(self, execution_tree, stack, statement):
        """ Compile statement
        Args:
            execution_tree:
            stack:
            statement:
        Returns:
            None
        """

        if (isinstance(statement, ElseIf) or
            isinstance(statement, Else) or
            isinstance(statement, While)):
            stack.append(statement)

        elif isinstance(statement, For):
            self.handle_for_loop(execution_tree, stack, statement)

        elif (isinstance(statement, Echo) or
              isinstance(statement, Continue) or
              isinstance(statement, Variable)):
            self._handle_one_line_statement(execution_tree, stack, statement)

        elif isinstance(statement, Break):
            self._handle_break_statement(execution_tree, stack, statement)

        elif isinstance(statement, If):
            self._handle_if(stack, statement)

        elif isinstance(statement, Fi):
            self._handle_endif(execution_tree, stack)

        elif isinstance(statement, EndFor):
            self._handle_end_forloop_statement(execution_tree, stack)

        elif isinstance(statement, EndWhile):
            self._handle_end_statement(execution_tree, stack)

    def _handle_break_statement(self, execution_tree: ExecutionTree, stack, statement: Break):
        """ Store variables in symbols table
        Args:
            execution_tree:
        Returns:
            None
        """
        if stack:
            for stack_item in stack[::-1]:
                if isinstance(stack_item, While) or isinstance(stack_item, For):
                     self._handle_one_line_statement(execution_tree, stack, statement)
                     break
        else:
            raise Exception("No Loop Found")

    def store_variables_in_symbols_table(self, execution_tree: ExecutionTree):
        """ Store variables in symbols table
        Args:
            execution_tree:
        Returns:
            None
        """

        for statement in execution_tree.tree:
            if isinstance(statement, Variable):
                # don't store values yet, symbol table should contain the values
                # after executing the variable instruction
                execution_tree.symbols_table.add_entry(statement.variable_name, "")
                statement.symbols_table = execution_tree.symbols_table

            if (self.is_scope_statement(statement)):
                self.store_variables_in_symbols_table_for_statements(
                    statement.statements)
                pass

            if isinstance(statement, ConditionStatement):
                self.store_variables_in_symbols_table_for_statements(
                    statement.if_statmenet.statements)

                for elifs in statement.elseif_statements:
                    self.store_variables_in_symbols_table_for_statements(
                        elifs.statements)

                if statement.else_statement:
                    self.store_variables_in_symbols_table_for_statements(
                        statement.else_statement.statements)

        pass

    def find_symbol(self, statement: Variable):
        """ Finds symbol in symbol tables in the execution tree
        Args:
            statement: variable statement that contains the symbol that
                        we look for
        Returns:
            Symbol Table that contains statement
        """

        statement_pointer = statement.parent
        symbols_table = None
        variable_name = statement.variable_name

        while statement_pointer:
            # If statement_pointer points to one of these statement types, that means
            # it contains a symbol table, otherwhise, we keep going up
            if (self.is_scope_statement(statement_pointer) or
                isinstance(statement_pointer, ExecutionTree)):

                if statement_pointer.symbols_table.get_entry_value(variable_name):
                    symbols_table = statement_pointer.symbols_table
                    break

            if isinstance(statement_pointer, ConditionStatement):
                # condition statement doesn't have symbol table (No scope)
                statement_pointer = statement_pointer.parent
                continue

            # Go Up
            statement_pointer = statement_pointer.parent

        return symbols_table

    def store_variables_in_symbols_table_for_statements(self, statements: list[Statement]):
        """ Store variables in symbols table for statements
        Args:
            statements:
        Returns:
            None
        """

        for statement in statements:
            if isinstance(statement, Variable):
                # find in all parents if symbol exists in any symbol tables,
                # if found do nohting
                symbol = self.find_symbol(statement)
                # if not found, store it in parents symbol table
                if not symbol:
                    statement.parent.symbols_table.add_entry(
                        statement.variable_name, "")
                    statement.symbols_table = statement.parent.symbols_table

            if (self.is_scope_statement(statement)):
                # Recursive Call for each statement that contains list of statements
                # each statement that has scope
                self.store_variables_in_symbols_table_for_statements(
                    statement.statements)
                pass

            if isinstance(statement, ConditionStatement):
                self.store_variables_in_symbols_table_for_statements(
                    statement.if_statmenet.statements)
                for elseif_statement in statement.elseif_statements:
                    self.store_variables_in_symbols_table_for_statements(
                        elseif_statement.statements)
                if statement.else_statement:
                    self.store_variables_in_symbols_table_for_statements(
                        statement.else_statement.statements)
            pass

    def set_parents(self, execution_tree: ExecutionTree):
        """ Set parents for execution tree
        Args:
            execution_tree:
        Returns:
            None
        """

        for statement in execution_tree.tree:

            statement.parent = execution_tree

            if (self.is_scope_statement(statement)):
                # Call set parent for statements inside this scope
                self.set_parent_for_statements(statement, statement.statements)

            if isinstance(statement, ConditionStatement):
                # Condition Statement contains ifstatement,
                # elseifstatement and elsestatement, each one should
                # be handled seperatly
                statement.if_statmenet.parent = statement
                self.set_parent_for_statements(
                    statement.if_statmenet,
                    statement.if_statmenet.statements)

                for elseif in statement.elseif_statements:
                    elseif.parent = statement
                    self.set_parent_for_statements(elseif, elseif.statements)

                if statement.else_statement:
                    statement.else_statement.parent = statement
                    self.set_parent_for_statements(
                        statement.else_statement,
                        statement.else_statement.statements)
                pass
        pass

    def set_parent_for_statements(self, parent, statements):
        """ Set parents for statements
        Args:
            parent:
            statements:
        Returns:
            None
        """

        for statement in statements:
            statement.parent = parent
            if (self.is_scope_statement(statement)):
                self.set_parent_for_statements(statement, statement.statements)

            if isinstance(statement, ConditionStatement):
                statement.if_statmenet.parent = statement
                self.set_parent_for_statements(
                    statement.if_statmenet,
                    statement.if_statmenet.statements)

                for elif_statement in statement.elseif_statements:
                    elif_statement.parent = statement

                    self.set_parent_for_statements(
                        elif_statement,
                        elif_statement.statements)

                if statement.else_statement:
                    statement.else_statement.parent = statement

                    self.set_parent_for_statements(
                        statement.else_statement,
                        statement.else_statement.statements)

                pass
        pass

    def _handle_endif(self, execution_tree: ExecutionTree, stack):
        """ Handle End If Statement compilation
        Args:
            execution_tree:
            stack:
        Returns:
            None
        """

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
        """ Handle If Statement compilation
        Args:
            stack:
            statement:
        Returns:
            None
        """

        conditon = ConditionStatement(statement, [], [])
        stack.append(conditon)
        stack.append(statement)

    def _handle_one_line_statement(self, execution_tree, stack, statement):
        """ Handle End Statement compilation
        Args:
            execution_tree:
            stack:
            statement:
        Returns:
            None
        """

        if stack:
            stack[-1].statements.append(statement)
        else:
            execution_tree.append(statement)

    def _handle_end_statement(self, execution_tree, stack):
        """ Handle End Statement compilation
        Args:
            execution_tree:
            stack:
        Returns:
            None
        """

        end = stack.pop()
        if stack:
            stack[-1].statements.append(end)
        else:
            execution_tree.append(end)

    def _handle_end_forloop_statement(self, execution_tree, stack):
        """ Handle End For Loop Statement compilation
        Args:
            execution_tree:
            stack:
        Returns:
            None
        """

        end = stack.pop()
        # create increment variable at the end of for loop
        increment_variable = Variable(end.loop_increment)
        end.statements.append(increment_variable)
        if stack:
            stack[-1].statements.append(end)
        else:
            execution_tree.append(end)

    def handle_for_loop(self, execution_tree, stack, statement):
        """ Handle For Loop Statement compilation
        Args:
            execution_tree:
            stack:
            statement:
        Returns:
            None
        """

        # add for loop variable
        if statement.loop_initial_variable:
            loop_initial_variable = Variable(statement.loop_initial_variable)
            self._handle_one_line_statement(execution_tree, stack, loop_initial_variable)
        stack.append(statement)

    def is_scope_statement(self, statement):
        """Checks if statement type is for, while, if, elseif, else statements
        Args:
            statement: Statement to be checked
        Returns:
            True: if statment is scope statment
            False: if statment is not scope statement
        """

        return (isinstance(statement, For) or
                isinstance(statement, While) or
                isinstance(statement, If) or
                isinstance(statement, ElseIf) or
                isinstance(statement, Else))
