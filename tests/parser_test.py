import unittest

from enhanced_parser import EnhancedParser
from lexer import Token, TokenType
from statements.statement import Echo, Variable, VariableType

class ParserUnitTest(unittest.TestCase):
    def setUp(self):
        super(ParserUnitTest, self).setUp()

    def test_parser_echo(self):
        lexes = []
        statements = []
        lexes.append(Token(TokenType.ECHO, "\"echo\"", 0))
        lexes.append(Token(TokenType.STRING, "\"hello\"", 0))

        parser = EnhancedParser()
        parser.parse_echo(lexes, statements)

        self.assertTrue(isinstance(statements[0], Echo), "Invalid Type")
        self.assertTrue(statements[0].echo_string == '"hello"', "Invalid string")

    def test_parser_variable(self):
        lexes = []
        statements = []
        lexes.append(Token(TokenType.IDENTIFICATION, "x", 0))
        lexes.append(Token(TokenType.EQUAL, "=", 0))
        lexes.append(Token(TokenType.NUMBER, "10", 0))

        parser = EnhancedParser()
        parser.parse_variable(lexes, statements)

        self.assertTrue(isinstance(statements[0], Variable), "Invalid Type")
        self.assertTrue(statements[0].variable_name == 'x', "Invalid variable name")
        self.assertTrue(statements[0].operation == TokenType.EQUAL, "Invalid variable operation")
        self.assertTrue(statements[0].variable_value == '10', "Invalid variable value")
        self.assertTrue(statements[0].type == TokenType.NUMBER, "Invalid variable value type")

    def test_parser_variable_2(self):
        lexes = []
        statements = []
        lexes.append(Token(TokenType.IDENTIFICATION, "y", 0))
        lexes.append(Token(TokenType.EQUAL, "=", 0))
        lexes.append(Token(TokenType.NUMBER, "10", 0))
        lexes.append(Token(TokenType.ADD, "+", 0))
        lexes.append(Token(TokenType.NUMBER, "10", 0))

        parser = EnhancedParser()
        parser.parse_variable(lexes, statements)

        self.assertTrue(isinstance(statements[0], Variable), "Invalid Type")
        self.assertTrue(statements[0].variable_name == 'y', "Invalid variable name")
        self.assertTrue(statements[0].operation == TokenType.EQUAL, "Invalid variable operation")
        self.assertTrue(statements[0].variable_value == '10+10', "Invalid variable value")
        self.assertTrue(statements[0].type == TokenType.NUMBER, "Invalid variable value type")


    def tearDown(self):
        super(ParserUnitTest, self).tearDown()


if __name__ == '__main__':
    unittest.main()
