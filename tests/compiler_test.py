# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

"""

Compiler Unit Test

"""

import unittest
from compiler import Compiler

from enhanced_lexer import EnhancedLexer
from enhanced_parser import EnhancedParser
from statements.statement import ConditionStatement, Echo, For, Variable

class CompilerUnitTest(unittest.TestCase):
    """
    Compiler Unit Test Class
    """

    def setUp(self):
        """ Setup Phase"""
        super(CompilerUnitTest, self).setUp()

    def test_compiler_variable_and_echo(self):
        """ test compiler variable and echo """

        code = """
x = 10
y = 20
echo "{x} and {y}"
"""
        tokens = EnhancedLexer().tokenize_text(code)
        statements = EnhancedParser().parse(tokens)
        execution_tree = Compiler().compile(statements)

        # Symbols Table
        self.assertTrue(execution_tree.symbols_table.symbol_table != None)
        self.assertTrue(len(execution_tree.symbols_table.symbol_table) == 2)
        self.assertTrue(execution_tree.symbols_table.symbol_table.get("x") != None)
        self.assertTrue(execution_tree.symbols_table.symbol_table.get("x").value == '')
        self.assertTrue(execution_tree.symbols_table.symbol_table.get("y") != None)
        self.assertTrue(execution_tree.symbols_table.symbol_table.get("y").value == '')

        # Execution Tree
        self.assertTrue(len(execution_tree.tree) == 3, "invalid statements")
        self.assertTrue(isinstance(execution_tree.tree[0], Variable), "invalid statement type")
        self.assertTrue(execution_tree.tree[0].variable_name == "x", "invalid variable name")
        self.assertTrue(execution_tree.tree[0].variable_value == "10", "invalid variable name")
        self.assertTrue(isinstance(execution_tree.tree[1], Variable), "invalid statement type")
        self.assertTrue(execution_tree.tree[1].variable_name == "y", "invalid variable name")
        self.assertTrue(execution_tree.tree[1].variable_value == "20", "invalid variable name")
        self.assertTrue(isinstance(execution_tree.tree[2], Echo), "invalid statement type")
        self.assertTrue(execution_tree.tree[2].echo_string == '"{x} and {y}"', "invalid variable name")
        self.assertTrue(execution_tree.tree[0].parent == execution_tree)
        self.assertTrue(execution_tree.tree[1].parent == execution_tree)
        self.assertTrue(execution_tree.tree[2].parent == execution_tree)

    def test_compile_if_statement(self):
        """ test compile if statement """

        code = """
x = 10
if (x == 10)
    echo "x is 10"
else
    echo "x is not 10"
fi
        """
        tokens = EnhancedLexer().tokenize_text(code)
        statements = EnhancedParser().parse(tokens)

        execution_tree = Compiler().compile(statements)

        # Symbols Table
        self.assertTrue(execution_tree.symbols_table.symbol_table != None)
        self.assertTrue(len(execution_tree.symbols_table.symbol_table) == 1)
        self.assertTrue(execution_tree.symbols_table.symbol_table.get("x") != None)
        self.assertTrue(execution_tree.symbols_table.symbol_table.get("x").value == '')

        # Execution Tree
        self.assertTrue(len(execution_tree.tree) == 2, "invalid statements")
        self.assertTrue(isinstance(execution_tree.tree[0], Variable), "invalid statement type")
        self.assertTrue(execution_tree.tree[0].parent == execution_tree)
        self.assertTrue(execution_tree.tree[0].variable_name == "x", "invalid variable name")
        self.assertTrue(execution_tree.tree[0].variable_value == "10", "invalid variable name")
        self.assertTrue(isinstance(execution_tree.tree[1], ConditionStatement), "invalid statement type")
        self.assertTrue(execution_tree.tree[1].parent == execution_tree)
        self.assertIsNotNone(execution_tree.tree[1].if_statement)

        self.assertTrue(execution_tree.tree[1].if_statement.parent == execution_tree.tree[1])

        self.assertTrue(execution_tree.tree[1].if_statement.condition == "(x==10)", "invalid statement type")
        self.assertIsNotNone(len(execution_tree.tree[1].if_statement.statements) == 1)
        self.assertTrue(isinstance(execution_tree.tree[1].if_statement.statements[0], Echo))
        self.assertTrue(execution_tree.tree[1].if_statement.statements[0].parent == execution_tree.tree[1].if_statement)

        self.assertTrue(execution_tree.tree[1].if_statement.statements[0].echo_string == '"x is 10"')
        self.assertIsNotNone(execution_tree.tree[1].else_statement)
        self.assertTrue(isinstance(execution_tree.tree[1].else_statement.statements[0], Echo))
        self.assertTrue(execution_tree.tree[1].else_statement.statements[0].echo_string == '"x is not 10"')

        self.assertTrue(execution_tree.tree[1].else_statement.parent == execution_tree.tree[1])
        self.assertTrue(execution_tree.tree[1].else_statement.statements[0].parent == execution_tree.tree[1].else_statement)

    def test_compile_while_loop(self):
        """test_compile_while_loop"""
        pass

    def test_compile_for_loop(self):
        """test_compile_for_loop"""

        code = """
echo "before for loop"
for(i = 0; i < 10; i += 1)
    echo "inside loop {i}"
endfor
echo "after for loop"
        """
        tokens = EnhancedLexer().tokenize_text(code)
        statements = EnhancedParser().parse(tokens)

        execution_tree = Compiler().compile(statements)
        self.assertTrue(len(execution_tree.tree) == 4)
        self.assertTrue(isinstance(execution_tree.tree[0], Echo))
        self.assertTrue(execution_tree.tree[0].echo_string == '"before for loop"')

        self.assertTrue(isinstance(execution_tree.tree[1], Variable))
        self.assertTrue(execution_tree.tree[1].variable_name == "i")


        self.assertTrue(isinstance(execution_tree.tree[2], For))
        self.assertTrue(execution_tree.tree[2].loop_condition == "i<10")
        # TODO continue here

        self.assertTrue(isinstance(execution_tree.tree[3], Echo))
        self.assertTrue(execution_tree.tree[3].echo_string == '"after for loop"')

    def test_compile_parents(self):
        """test_compile_parents"""
        pass

    def tearDown(self):
        """ Tear Down Phase"""
        super(CompilerUnitTest, self).tearDown()


if __name__ == '__main__':
    unittest.main()

