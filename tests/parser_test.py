# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

"""

Parser Unit Test

"""

import unittest
from lexer.enhanced_lexer import EnhancedLexer

from parser.enhanced_parser import EnhancedParser
from lexer.lexer import Lexer, Token, TokenType
from statements.statement import Break, Continue, Echo, ElseIf, EndFor, EndWhile, Fi, For, If, Statement, StatementType, Variable, VariableType, While
from exceptions.language_exception import SyntaxError


class ParserUnitTest(unittest.TestCase):
    """
    Unit testing for parser
    """

    def setUp(self):
        """setUp"""
        super(ParserUnitTest, self).setUp()

    def test_parser_echo(self):
        """test_parser_echo"""

        lexes = []
        statements = []
        lexes.append(Token(TokenType.ECHO, "\"echo\"", 0))
        lexes.append(Token(TokenType.STRING, "\"hello\"", 0))

        parser = EnhancedParser()
        parser.parse_echo(lexes, statements)

        self.assertTrue(isinstance(statements[0], Echo), "Invalid Type")
        self.assertTrue(statements[0].echo_string == '"hello"', "Invalid string")

    def test_parser_variable(self):
        """test_parser_variable"""

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
        """test_parser_variable_2"""

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
        """test_check_token_type_in_list"""

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
        """test_check_token_type_in_list"""

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
        """test_is_valid_variable_operation"""
        pass

    def test_parse_for(self):
        """test_parse_for"""

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
        """test_parse_between_parenthesis"""

        code = "((10 + 20 / 3) > 22)"
        lexes = Lexer().tokenize_text(code)

        result = EnhancedParser().parse_between_parenthesis(lexes)

        self.assertTrue(result == "((10+20/3)>22)")

    def test_parse_between_parenthesis_syntax_error(self):
        """test_parse_between_parenthesis_syntax_error"""

        code = "10 + 20 / (3 > 22"
        lexes = Lexer().tokenize_text(code)
        parser = EnhancedParser()
        with self.assertRaises(SyntaxError):
            parser.parse_between_parenthesis(lexes)

    def test_parse_between_parenthesis_syntax_error_2(self):
        """test_parse_between_parenthesis_syntax_error_2"""

        code = "10 + 20 / 3) > 22"
        lexes = Lexer().tokenize_text(code)

        parser = EnhancedParser()

        with self.assertRaises(SyntaxError):
            parser.parse_between_parenthesis(lexes)

    def test_parse_while(self):
        """test_parse_while"""

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
        """test_parse_variable_numeric_value"""

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
        """test_parse_variable_string_value"""

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
        """test_parse_variable_expression_value"""

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
        """test_parse_elseif"""

        statements = []
        code = """
        elif (x == 10)"""
        tokens = Lexer().tokenize_text(code)

        EnhancedParser().parse_elseif(tokens, statements)

        self.assertTrue(len(statements) == 1, "Parser returned more than one token")
        self.assertTrue(isinstance(statements[0], ElseIf), "Invalid Type")
        self.assertTrue(statements[0].condition == "(x==10)", "Invalid if condition string")

    def test_parse_if(self):
        """test_parse_if"""

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
        """test_parse_echo"""

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
        """test_parse_endif"""

        statements = []

        EnhancedParser().parse_endif(statements)

        self.assertTrue(len(statements) == 1, "Parser returned more than one token")
        self.assertTrue(isinstance(statements[0], Fi), "Invalid Type")

    def test_parse_endfor(self):
        """test_parse_endfor"""

        statements = []

        EnhancedParser().parse_endfor(statements)

        self.assertTrue(len(statements) == 1, "Parser returned more than one token")
        self.assertTrue(isinstance(statements[0], EndFor), "Invalid Type")

    def test_parse_endwhile(self):
        """test_parse_endwhile"""

        statements = []

        EnhancedParser().parse_endwhile(statements)

        self.assertTrue(len(statements) == 1, "Parser returned more than one token")
        self.assertTrue(isinstance(statements[0], EndWhile), "Invalid Type")

    def test_parse_break(self):
        """test_parse_break"""

        statements = []

        EnhancedParser().parse_break(statements)

        self.assertTrue(len(statements) == 1, "Parser returned more than one token")
        self.assertTrue(isinstance(statements[0], Break), "Invalid Type")

    def test_parse_continue(self):
        """test_parse_continue"""

        statements = []

        EnhancedParser().parse_continue(statements)

        self.assertTrue(len(statements) == 1, "Parser returned more than one token")
        self.assertTrue(isinstance(statements[0], Continue), "Invalid Type")

    def test_invalid_for(self):
        """test_invalid_for

        No Parenthesis
        """

        code = """
        for i = 0; i < 10; i+= 1
            echo "{i}"
        endfor
        """

        tokens = Lexer().tokenize_text(code)

        with self.assertRaises(SyntaxError):
            statements = EnhancedParser().parse(tokens)

    def test_all_statements(self):
        code = """// program that contains all statements

for(i = 0; i < 10; i += 1)

    if (i == 1)
        echo "i is 1"
    elif (i == 9)
        echo ("i is 9, breaking")
        break
    else
        echo "i value is {i}"
        continue
    fi

endfor

var = 1

while (var < 10)

    echo "var is {var}"
    if ((var %2 ) == 0)
        echo "var {var} is even"
    else
        echo "var {var} is odd"
    fi
    for(;;)
        echo "infinite loop"
    endfor
endwhile
input var
"""

        tokens = EnhancedLexer().tokenize_text(code)
        actual_statements = EnhancedParser().parse(tokens)

        expected_statements = [Statement(StatementType.FOR),
                               Statement(StatementType.IF),
                               Statement(StatementType.ECHO),
                               Statement(StatementType.ELSEIF),
                               Statement(StatementType.ECHO),
                               Statement(StatementType.BREAK),
                               Statement(StatementType.ELSE),
                               Statement(StatementType.ECHO),
                               Statement(StatementType.CONTINUE),
                               Statement(StatementType.ENDIF),
                               Statement(StatementType.ENDFOR),
                               Statement(TokenType.NUMBER),
                               Statement(StatementType.WHILE),
                               Statement(StatementType.ECHO),
                               Statement(StatementType.IF),
                               Statement(StatementType.ECHO),
                               Statement(StatementType.ELSE),
                               Statement(StatementType.ECHO),
                               Statement(StatementType.ENDIF),
                               Statement(StatementType.FOR),
                               Statement(StatementType.ECHO),
                               Statement(StatementType.ENDFOR),
                               Statement(StatementType.ENDWHILE),
                               Statement(StatementType.INPUT)
                               ]

        for idx, statement in enumerate(expected_statements):
            self.assertEqual(statement.type, actual_statements[idx].type)
        pass

    def tearDown(self):
        """tearDown"""
        super(ParserUnitTest, self).tearDown()


if __name__ == '__main__':
    unittest.main()
