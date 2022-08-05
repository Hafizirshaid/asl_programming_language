import unittest

from enhanced_parser import EnhancedParser
from lexer import Lexer, Token, TokenType
from parser import Parser
from statements.statement import Break, Continue, Echo, ElseIf, EndFor, EndWhile, Fi, For, If, Variable, VariableType, While
from exceptions.language_exception import SyntaxError

class ParserUnitTest(unittest.TestCase):
    """
    Unit testing for parser
    """

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

    def test_check_token_type_in_list(self):
        # lexes = []
        # lexes.append(Token(TokenType.IDENTIFICATION, "y", 0))
        # lexes.append(Token(TokenType.EQUAL, "=", 0))
        # lexes.append(Token(TokenType.NUMBER, "10", 0))
        # lexes.append(Token(TokenType.ADD, "+", 0))
        # lexes.append(Token(TokenType.NUMBER, "10", 0))

        # parser = EnhancedParser()
        # result = parser.check_token_type_in_list(lexes, [TokenType.ADD, TokenType.EQUAL])

        # self.assertTrue(result, "invalid return type")
        pass
    def test_is_there_more_tokens(self):
        # lexes = []
        # lexes.append(Token(TokenType.IDENTIFICATION, "y", 0))
        # lexes.append(Token(TokenType.EQUAL, "=", 0))
        # lexes.append(Token(TokenType.NUMBER, "10", 0))
        # lexes.append(Token(TokenType.ADD, "+", 0))
        # lexes.append(Token(TokenType.NUMBER, "10", 0))
        # parser = EnhancedParser()
        # parser.is_there_more_tokens(lexes)

        pass

    def test_is_valid_variable_operation(self):
        pass

    def test_parse_for(self):
        code = """
        for (var = 0; var < 10; var = var + 1)
        """
        lexes = Lexer().tokenize_text(code)
        statements = []

        EnhancedParser().parse_for(lexes, statements)

        self.assertTrue(len(statements) == 1, "Parser returned more than one token")
        self.assertTrue(isinstance(statements[0], For), "Invalid Type")
        self.assertTrue(statements[0].loop_condition == "var<10", "Invalid variable name")
        self.assertTrue(statements[0].loop_initial_variable.variable_name == "var", "Invalid variable value")
        self.assertTrue(statements[0].loop_initial_variable.variable_value == "0", "Invalid variable value")
        self.assertTrue(statements[0].loop_increment.variable_name == "var", "Invalid variable value")
        self.assertTrue(statements[0].loop_increment.variable_value == "var+1", "Invalid variable value")

    def test_parse_between_parenthesis(self):
        code = "((10 + 20 / 3) > 22)"
        lexes = Lexer().tokenize_text(code)

        result = EnhancedParser().parse_between_parenthesis(lexes)

        self.assertTrue(result == "((10+20/3)>22)")

    def test_parse_between_parenthesis_syntax_error(self):
        code = "10 + 20 / (3 > 22"
        lexes = Lexer().tokenize_text(code)
        parser = EnhancedParser()
        self.assertRaises(SyntaxError, parser.parse_between_parenthesis, lexes)

    def test_parse_between_parenthesis_syntax_error_2(self):
        code = "10 + 20 / 3) > 22"
        lexes = Lexer().tokenize_text(code)

        parser = EnhancedParser()

        self.assertRaises(SyntaxError, parser.parse_between_parenthesis, lexes)

    def test_parse_while(self):
        code = """
        while (10 < 10)
        """
        lexes = Lexer().tokenize_text(code)
        statements = []

        EnhancedParser().parse_while(lexes, statements)

        self.assertTrue(len(statements) == 1, "Parser returned more than one token")
        self.assertTrue(isinstance(statements[0], While), "Invalid Type")
        self.assertTrue(statements[0].condition == "(10<10)", "Invalid condition")

    def test_parse_variable_numeric_value(self):
        code = """
        var = 10
        """
        lexes = Lexer().tokenize_text(code)
        statements = []

        EnhancedParser().parse_variable(lexes, statements)

        self.assertTrue(len(statements) == 1, "Parser returned more than one token")
        self.assertTrue(isinstance(statements[0], Variable), "Invalid Type")
        self.assertTrue(statements[0].variable_name == "var", "Invalid variable name")
        self.assertTrue(statements[0].variable_value == "10", "Invalid variable value")
        self.assertTrue(statements[0].type == TokenType.NUMBER, "Invalid variable type")

    def test_parse_variable_string_value(self):
        code = """
        var = "hello"
        """
        lexes = Lexer().tokenize_text(code)
        statements = []

        EnhancedParser().parse_variable(lexes, statements)

        self.assertTrue(len(statements) == 1, "Parser returned more than one token")
        self.assertTrue(isinstance(statements[0], Variable), "Invalid Type")
        self.assertTrue(statements[0].variable_name == "var", "Invalid variable name")
        self.assertTrue(statements[0].variable_value == '"hello"', "Invalid variable value")
        self.assertTrue(statements[0].type == TokenType.STRING, "Invalid variable type")

    def test_parse_variable_expression_value(self):
        code = """
        var = 10 + 20 / x
        """
        lexes = Lexer().tokenize_text(code)
        statements = []

        EnhancedParser().parse_variable(lexes, statements)

        self.assertTrue(len(statements) == 1, "Parser returned more than one token")
        self.assertTrue(isinstance(statements[0], Variable), "Invalid Type")
        self.assertTrue(statements[0].variable_name == "var", "Invalid variable name")
        self.assertTrue(statements[0].variable_value == "10+20/x", "Invalid variable value")
        self.assertTrue(statements[0].type == TokenType.IDENTIFICATION, "Invalid variable type")

    def test_parse_elseif(self):
        statements = []
        code = """
        elif (x == 10)"""
        tokens = Lexer().tokenize_text(code)

        EnhancedParser().parse_elseif(tokens, statements)

        self.assertTrue(len(statements) == 1, "Parser returned more than one token")
        self.assertTrue(isinstance(statements[0], ElseIf), "Invalid Type")
        self.assertTrue(statements[0].condition == "(x==10)", "Invalid if condition string")

    def test_parse_if(self):
        statements = []
        code = """
        if (x == 10)
        """
        tokens = Lexer().tokenize_text(code)

        EnhancedParser().parse_if(tokens, statements)

        self.assertTrue(len(statements) == 1, "Parser returned more than one token")
        self.assertTrue(isinstance(statements[0], If), "Invalid Type")
        self.assertTrue(statements[0].condition == "(x==10)", "Invalid if condition string")

    def test_parse_echo(self):
        code = """
        echo "hello, world!"
        """
        statements = []
        tokens = Lexer().tokenize_text(code)

        EnhancedParser().parse_echo(tokens, statements)

        self.assertTrue(len(statements) == 1, "Parser returned more than one token")
        self.assertTrue(isinstance(statements[0], Echo), "Invalid Type")
        self.assertTrue(statements[0].echo_string == '"hello, world!"', "Invalid if condition string")

    def test_parse_endif(self):
        statements = []

        EnhancedParser().parse_endif(statements)

        self.assertTrue(len(statements) == 1, "Parser returned more than one token")
        self.assertTrue(isinstance(statements[0], Fi), "Invalid Type")

    def test_parse_endfor(self):
        statements = []

        EnhancedParser().parse_endfor(statements)

        self.assertTrue(len(statements) == 1, "Parser returned more than one token")
        self.assertTrue(isinstance(statements[0], EndFor), "Invalid Type")

    def test_parse_endwhile(self):
        statements = []

        EnhancedParser().parse_endwhile(statements)

        self.assertTrue(len(statements) == 1, "Parser returned more than one token")
        self.assertTrue(isinstance(statements[0], EndWhile), "Invalid Type")

    def test_parse_break(self):
        statements = []

        EnhancedParser().parse_break(statements)

        self.assertTrue(len(statements) == 1, "Parser returned more than one token")
        self.assertTrue(isinstance(statements[0], Break), "Invalid Type")

    def test_parse_continue(self):
        statements = []

        EnhancedParser().parse_continue(statements)

        self.assertTrue(len(statements) == 1, "Parser returned more than one token")
        self.assertTrue(isinstance(statements[0], Continue), "Invalid Type")

    def tearDown(self):
        super(ParserUnitTest, self).tearDown()


if __name__ == '__main__':
    unittest.main()
