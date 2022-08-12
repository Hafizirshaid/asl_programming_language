# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

"""

Lexer Unit Testing

"""

import unittest

from lexer.enhanced_lexer import EnhancedLexer

from lexer.lexer import Lexer, Token, TokenType
from exceptions.language_exception import SyntaxError


class LexerUnitTest(unittest.TestCase):
    """ Lexer Unit Test Class """

    def setUp(self):
        """ Unit Test Setup """
        super(LexerUnitTest, self).setUp()

    def test_lexer_if_and_for_loop(self):
        """
        Test case for the following code. it calculates grades rank based on grade
        """

        code = """
echo "Calculate Grades rank between 0 to 100"

for (grade = 0; grade <= 100; grade = grade + 1)

    if ((grade >= 90) & (grade <= 100))
        echo "{grade} Outstanding"
    elif ((grade >= 80) & (grade <= 90))
        echo "{grade} very good"
    elif ((grade >= 70) & (grade <= 80))
        echo "{grade} good"
    elif ((grade >= 60) & (grade <= 70))
        echo "{grade} fair"
    elif ((grade >= 0) & (grade <= 60))
        echo "{grade} failure"
    else
        echo "Invalid Grade"
    fi

endfor
        """

        enhanced_lexer_tokens = EnhancedLexer().tokenize_text(code)
        old_lexer_tokens = Lexer().tokenize_text(code)

        # Both Enhanced and old lexer should generate same tokens
        for i, val in enumerate(old_lexer_tokens):
            if val.token_type != enhanced_lexer_tokens[i].token_type:
                self.fail(f"failed at index {i}")
        pass

    def test_lexer_for_all_files(self):
        """
        This test case compares old lexer with the new lexer output,
        both should generate same exact tokens.
        """

        files = ['asl_files/arrays.asl',
                 'asl_files/break_statement.asl',
                 'asl_files/calculator.asl',
                 'asl_files/continue_statement.asl',
                 'asl_files/empty.asl',
                 'asl_files/enhanced_variables.asl',
                 'asl_files/errors.asl',
                 'asl_files/fibonacci.asl',
                 'asl_files/for_loop.asl',
                 'asl_files/functions.asl',
                 'asl_files/grades.asl',
                 'asl_files/input_string.asl',
                 'asl_files/keyboard_input.asl',
                 'asl_files/main.asl',
                 'asl_files/main2.asl',
                 'asl_files/new_syntax.asl',
                 'asl_files/odd_even.asl',
                 'asl_files/one_var.asl',
                 'asl_files/prime.asl',
                 'asl_files/real_numbers.asl',
                 'asl_files/strings.asl',
                 'asl_files/variable.asl',
                 'asl_files/while_for.asl',
                 'asl_files/swap_variables.asl',
                 'asl_files/while_loop.asl']

        for file_name in files:
            code = ""
            with open(file_name) as file:
                for line in file:
                    code += line
            tokens_2 = EnhancedLexer().tokenize_text(code)
            tokens_1 = Lexer().tokenize_text(code)

            for i, val in enumerate(tokens_1):
                if val.token_type != tokens_2[i].token_type:
                    self.fail(f"failed at index {i} for file {file_name}")

    def test_new_lexer_4(self):
        """
        Test case to show the new enhancement that EnhancedLexer provides.
        The old lexer doesn't recognize identifiers correctly if the identifier contains a keyword.
        """

        file_name = 'asl_files/new_lexer.asl'
        code = ""
        with open(file_name) as file:
            for line in file:
                code += line
        enhanced_lexer_tokens = EnhancedLexer().tokenize_text(code)

        expected_tokens = [Token(TokenType.IDENTIFICATION, 'print_value', 1),
                           Token(TokenType.EQUAL, '=', 1),
                           Token(TokenType.NUMBER, '1', 1),
                           Token(TokenType.IDENTIFICATION, 'if_cond', 2),
                           Token(TokenType.EQUAL, '=', 2),
                           Token(TokenType.NUMBER, '2', 2),
                           Token(TokenType.IDENTIFICATION, 'else_cond', 3),
                           Token(TokenType.EQUAL, '=', 3),
                           Token(TokenType.NUMBER, '3', 3),
                           Token(TokenType.IDENTIFICATION, 'echo_var', 4),
                           Token(TokenType.EQUAL, '=', 4),
                           Token(TokenType.NUMBER, '333', 4),
                           Token(TokenType.IDENTIFICATION, 'elif_cond', 5),
                           Token(TokenType.EQUAL, '=', 5),
                           Token(TokenType.NUMBER, '22', 5),
                           Token(TokenType.IDENTIFICATION, 'fi_cond', 6),
                           Token(TokenType.EQUAL, '=', 6),
                           Token(TokenType.NUMBER, '22', 6)]

        self.assertEqual(enhanced_lexer_tokens, expected_tokens)

    def test_tokenize_while_loop(self):
        """test_tokenize_while_loop"""

        code = """
        var = 1
        while (var < 10)
            echo ("var is {var}")
            var += 1
        endwhile
        """

        actual_tokens = EnhancedLexer().tokenize_text(code)

        expected_tokens = [Token(TokenType.IDENTIFICATION, 'var', 2),
                           Token(TokenType.EQUAL, '=', 2),
                           Token(TokenType.NUMBER, '1', 2),
                           Token(TokenType.WHILE, 'while', 3),
                           Token(TokenType.OPENPARENTHESIS, '(', 3),
                           Token(TokenType.IDENTIFICATION, 'var', 3),
                           Token(TokenType.LESSTHAN, '<', 3),
                           Token(TokenType.NUMBER, '10', 3),
                           Token(TokenType.CLOSINGPARENTHESIS, ')', 3),
                           Token(TokenType.ECHO, 'echo', 4),
                           Token(TokenType.OPENPARENTHESIS, '(', 4),
                           Token(TokenType.STRING, '"var is {var}"', 4),
                           Token(TokenType.CLOSINGPARENTHESIS, ')', 4),
                           Token(TokenType.IDENTIFICATION, 'var', 5),
                           Token(TokenType.PLUSEQUAL, '+=', 5),
                           Token(TokenType.NUMBER, '1', 5),
                           Token(TokenType.ENDWHILE, 'endwhile', 6)]

        self.assertEqual(actual_tokens, expected_tokens)

    def test_tokenize_variable(self):
        """test_tokenize_variable"""

        code = """
        x = 1
        y = 2
        z = 3.4
        """
        actual_tokens = EnhancedLexer().tokenize_text(code)
        expected_tokens = [Token(TokenType.IDENTIFICATION, 'x', 2),
                           Token(TokenType.EQUAL, '=', 2),
                           Token(TokenType.NUMBER, '1', 2),
                           Token(TokenType.IDENTIFICATION, 'y', 3),
                           Token(TokenType.EQUAL, '=', 3),
                           Token(TokenType.NUMBER, '2', 3),
                           Token(TokenType.IDENTIFICATION, 'z', 4),
                           Token(TokenType.EQUAL, '=', 4),
                           Token(TokenType.REAL, '3.4', 4)]

        self.assertEqual(actual_tokens, expected_tokens)

    def test_tokenize_if_statement(self):
        """ test_tokenize_if_statement """

        code = """
        if (x == 10)
            echo ("x is 10")
        elif (x == 20)
            echo ("x is 20")
        elif (x == 30)
            echo ("x is 30")
        else
            echo ("x is not 10, 20 or 30")
        fi
        """

        actual_tokens = EnhancedLexer().tokenize_text(code)

        expected_tokens = [Token(TokenType.IF, 'if', 2),
                           Token(TokenType.OPENPARENTHESIS, '(', 2),
                           Token(TokenType.IDENTIFICATION, 'x', 2),
                           Token(TokenType.EQUIVALENT, '==', 2),
                           Token(TokenType.NUMBER, '10', 2),
                           Token(TokenType.CLOSINGPARENTHESIS, ')', 2),
                           Token(TokenType.ECHO, 'echo', 3),
                           Token(TokenType.OPENPARENTHESIS, '(', 3),
                           Token(TokenType.STRING, '"x is 10"', 3),
                           Token(TokenType.CLOSINGPARENTHESIS, ')', 3),
                           Token(TokenType.ELIF, 'elif', 4),
                           Token(TokenType.OPENPARENTHESIS, '(', 4),
                           Token(TokenType.IDENTIFICATION, 'x', 4),
                           Token(TokenType.EQUIVALENT, '==', 4),
                           Token(TokenType.NUMBER, '20', 4),
                           Token(TokenType.CLOSINGPARENTHESIS, ')', 4),
                           Token(TokenType.ECHO, 'echo', 5),
                           Token(TokenType.OPENPARENTHESIS, '(', 5),
                           Token(TokenType.STRING, '"x is 20"', 5),
                           Token(TokenType.CLOSINGPARENTHESIS, ')', 5),
                           Token(TokenType.ELIF, 'elif', 6),
                           Token(TokenType.OPENPARENTHESIS, '(', 6),
                           Token(TokenType.IDENTIFICATION, 'x', 6),
                           Token(TokenType.EQUIVALENT, '==', 6),
                           Token(TokenType.NUMBER, '30', 6),
                           Token(TokenType.CLOSINGPARENTHESIS, ')', 6),
                           Token(TokenType.ECHO, 'echo', 7),
                           Token(TokenType.OPENPARENTHESIS, '(', 7),
                           Token(TokenType.STRING, '"x is 30"', 7),
                           Token(TokenType.CLOSINGPARENTHESIS, ')', 7),
                           Token(TokenType.ELSE, 'else', 8),
                           Token(TokenType.ECHO, 'echo', 9),
                           Token(TokenType.OPENPARENTHESIS, '(', 9),
                           Token(TokenType.STRING, '"x is not 10, 20 or 30"', 9),
                           Token(TokenType.CLOSINGPARENTHESIS, ')', 9),
                           Token(TokenType.FI, 'fi', 10)]

        self.assertEqual(actual_tokens, expected_tokens)

    def test_tokenize_for_loop(self):
        """test_tokenize_for_loop"""

        code = """
        for(var = 1; var < 10; var += 1)
            echo "var is {var}"
        endfor
        """

        actual_tokens = EnhancedLexer().tokenize_text(code)
        expected_tokens = [Token(TokenType.FOR, 'for', 2),
                           Token(TokenType.OPENPARENTHESIS, '(', 2),
                           Token(TokenType.IDENTIFICATION, 'var', 2),
                           Token(TokenType.EQUAL, '=', 2),
                           Token(TokenType.NUMBER, '1', 2),
                           Token(TokenType.SEMICOLON, ';', 2),
                           Token(TokenType.IDENTIFICATION, 'var', 2),
                           Token(TokenType.LESSTHAN, '<', 2),
                           Token(TokenType.NUMBER, '10', 2),
                           Token(TokenType.SEMICOLON, ';', 2),
                           Token(TokenType.IDENTIFICATION, 'var', 2),
                           Token(TokenType.PLUSEQUAL, '+=', 2),
                           Token(TokenType.NUMBER, '1', 2),
                           Token(TokenType.CLOSINGPARENTHESIS, ')', 2),
                           Token(TokenType.ECHO, 'echo', 3),
                           Token(TokenType.STRING, '"var is {var}"', 3),
                           Token(TokenType.ENDFOR, 'endfor', 4)]
        self.assertEqual(actual_tokens, expected_tokens)

    def test_tokenize_numerical_value(self):
        """test_tokenize_numerical_value"""

        code = "222.333"
        actual_tokens = EnhancedLexer().tokenize_text(code)
        expected_tokens = [Token(TokenType.REAL, "222.333", 1)]
        self.assertEqual(actual_tokens, expected_tokens)

    def test_tokenize_identifier(self):
        """test_tokenize_identifier"""

        code = "variable_1"
        actual_tokens = EnhancedLexer().tokenize_text(code)
        expected_tokens = [Token(TokenType.IDENTIFICATION, "variable_1", 1)]
        self.assertEqual(actual_tokens, expected_tokens)

    def test_tokenize_identifier_that_contains_keyword(self):
        """ test_tokenize_identifier_that_contains_keyword 

        This test case checks when identifier name contains a keyword,
        lexer should not create token for the keyword, example:
        for_loop_variable = 1

        the old lexer thinks that the identifier is two parts:
        for keyword
        _loop_variable

        """

        code = """for_loop_var = 1
            while_loop_var = 2
            condition_if_else = 3
        """
        actual_tokens = EnhancedLexer().tokenize_text(code)
        expected_tokens = [Token(TokenType.IDENTIFICATION, 'for_loop_var', 1),
                           Token(TokenType.EQUAL, '=', 1),
                           Token(TokenType.NUMBER, '1', 1),
                           Token(TokenType.IDENTIFICATION,
                                 'while_loop_var', 2),
                           Token(TokenType.EQUAL, '=', 2),
                           Token(TokenType.NUMBER, '2', 2),
                           Token(TokenType.IDENTIFICATION,
                                 'condition_if_else', 3),
                           Token(TokenType.EQUAL, '=', 3),
                           Token(TokenType.NUMBER, '3', 3), ]
        self.assertEqual(actual_tokens, expected_tokens)

    def test_tokenize_string(self):
        """test_tokenize_string"""

        code = '"hello, world!"'
        actual_tokens = EnhancedLexer().tokenize_text(code)
        expected_tokens = [Token(TokenType.STRING, '"hello, world!"', 1)]
        self.assertEqual(actual_tokens, expected_tokens)

    def test_tokenize_comment(self):
        """test_tokenize_comment"""

        code = """
        // one line comment
        var = 1
        /* multi
        line
        comment
        */
        var2 = 2
        """

        actual_tokens = EnhancedLexer().tokenize_text(code)
        expected_tokens = [Token(TokenType.COMMENT, '/ one line comment', 2),
                           Token(TokenType.IDENTIFICATION, 'var', 3),
                           Token(TokenType.EQUAL, '=', 3),
                           Token(TokenType.NUMBER, '1', 3),
                           Token(TokenType.COMMENT, """ multi
        line
        comment
        """, 4),
                           Token(TokenType.IDENTIFICATION, 'var2', 8),
                           Token(TokenType.EQUAL, '=', 8),
                           Token(TokenType.NUMBER, '2', 8)]

        self.assertEqual(actual_tokens, expected_tokens)

    def test_tokenize_input(self):
        """test_tokenize_input"""

        code = """
        value_1 = 0
        value_2 = 0
        input value_1
        input value_2
        """
        actual_tokens = EnhancedLexer().tokenize_text(code)
        expected_tokens = [Token(TokenType.IDENTIFICATION, 'value_1', 2),
                           Token(TokenType.EQUAL, '=', 2),
                           Token(TokenType.NUMBER, '0', 2),
                           Token(TokenType.IDENTIFICATION, 'value_2', 3),
                           Token(TokenType.EQUAL, '=', 3),
                           Token(TokenType.NUMBER, '0', 3),
                           Token(TokenType.INPUT, 'input', 4),
                           Token(TokenType.IDENTIFICATION, 'value_1', 4),
                           Token(TokenType.INPUT, 'input', 5),
                           Token(TokenType.IDENTIFICATION, 'value_2', 5)]

        self.assertEqual(actual_tokens, expected_tokens)

    def test_tokenize_echo(self):
        """test_tokenize_echo"""

        code = """

        echo "hello, world!"

        echo "hello with variable {var}"

        """

        actual_tokens = EnhancedLexer().tokenize_text(code)
        expected_tokens = [Token(TokenType.ECHO, 'echo', 3),
                           Token(TokenType.STRING, '"hello, world!"', 3),
                           Token(TokenType.ECHO, 'echo', 5),
                           Token(TokenType.STRING, '"hello with variable {var}"', 5)]

        self.assertEqual(actual_tokens, expected_tokens)

    def test_lexer_true_false(self):
        """test_lexer_true_false"""
        code = """
x = true
y = false
        """
        actual_tokens = EnhancedLexer().tokenize_text(code)
        expected_tokens = [Token(TokenType.IDENTIFICATION, 'x', 2),
                           Token(TokenType.EQUAL, '=', 2),
                           Token(TokenType.TRUE, 'true', 2),
                           Token(TokenType.IDENTIFICATION, 'y', 3),
                           Token(TokenType.EQUAL, '=', 3),
                           Token(TokenType.FALSE, 'false', 3)]

        self.assertEqual(actual_tokens, expected_tokens)
        pass

    def test_lexer_keeps_spaces_and_ignore_lines(self):
        """test_lexer_true_false"""
        code = """
echo "hello, world"
"""
        actual_tokens = EnhancedLexer().tokenize_text(
            code, keep_spaces=True, ignore_new_lines=False)
        expected_tokens = [Token(TokenType.NEWLINE, '\n', 2),
                           Token(TokenType.ECHO, 'echo', 2),
                           Token(TokenType.SPACE, ' ', 2),
                           Token(TokenType.STRING, '"hello, world"', 2),
                           Token(TokenType.NEWLINE, '\n', 3)]

        self.assertEqual(actual_tokens, expected_tokens)
        pass

    def test_unknown_chars_raises_exception(self):

        code = """
$
#
        """

        with self.assertRaises(SyntaxError):
            EnhancedLexer().tokenize_text(code)

    def test_keep_unknown_chars(self):

        code = """
$
#
        """
        expected_tokens = [Token(TokenType.UNKNOWN, '$', 2),
                           Token(TokenType.UNKNOWN, '#', 3)]

        actual_tokens = EnhancedLexer().tokenize_text(code, keep_unknown=True)

        self.assertEqual(actual_tokens, expected_tokens)

    # TODO For each token type, create test case for it.

    def test_minus_equal(self):
        code = """
x = 10
y -= 2
echo "{y}"
        """

        expected_tokens = [Token(TokenType.IDENTIFICATION, 'x', 2),
                           Token(TokenType.EQUAL, '=', 2),
                           Token(TokenType.NUMBER, '10', 2),
                           Token(TokenType.IDENTIFICATION, 'y', 3),
                           Token(TokenType.SUBEQUAL, '-=', 3),
                           Token(TokenType.NUMBER, '2', 3),
                           Token(TokenType.ECHO, 'echo', 4),
                           Token(TokenType.STRING, '"{y}"', 4)]
        actual_tokens = EnhancedLexer().tokenize_text(code)

        self.assertEqual(expected_tokens, actual_tokens)
        pass

    def test_multiply_equal(self):
        code = """
x = 10
y *= 2
echo "{y}"
        """

        expected_tokens = [Token(TokenType.IDENTIFICATION, 'x', 2),
                           Token(TokenType.EQUAL, '=', 2),
                           Token(TokenType.NUMBER, '10', 2),
                           Token(TokenType.IDENTIFICATION, 'y', 3),
                           Token(TokenType.MULTEQUAL, '*=', 3),
                           Token(TokenType.NUMBER, '2', 3),
                           Token(TokenType.ECHO, 'echo', 4),
                           Token(TokenType.STRING, '"{y}"', 4)]
        actual_tokens = EnhancedLexer().tokenize_text(code)

        self.assertEqual(expected_tokens, actual_tokens)
        pass

    def test_div_equal(self):
        code = """
x = 10
y /= 2
echo "{y}"
        """

        expected_tokens = [Token(TokenType.IDENTIFICATION, 'x', 2),
                           Token(TokenType.EQUAL, '=', 2),
                           Token(TokenType.NUMBER, '10', 2),
                           Token(TokenType.IDENTIFICATION, 'y', 3),
                           Token(TokenType.DIVEQUAL, '/=', 3),
                           Token(TokenType.NUMBER, '2', 3),
                           Token(TokenType.ECHO, 'echo', 4),
                           Token(TokenType.STRING, '"{y}"', 4)]
        actual_tokens = EnhancedLexer().tokenize_text(code)

        self.assertEqual(expected_tokens, actual_tokens)
        pass

    def test_curly_brackets(self):
        code = """
        {

        }
        """
        expected_tokens = [Token(TokenType.RIGHTBRAKET, '{', 2),
                           Token(TokenType.LEFTBRACKET, '}', 4)]
        actual_tokens = EnhancedLexer().tokenize_text(code)

        self.assertEqual(expected_tokens, actual_tokens)

    def test_not(self):
        code = "x != y"
        expected_tokens = [
            Token(TokenType.IDENTIFICATION, 'x', 1),
            Token(TokenType.NOTEQUIVALENT, '!=', 1),
            Token(TokenType.IDENTIFICATION, 'y', 1),
        ]
        actual_tokens = EnhancedLexer().tokenize_text(code)

        self.assertEqual(expected_tokens, actual_tokens)

    def test_negative_numbers(self):

        code = """
x = -10
y = -50
z = x + y
f = -10 + -20
vv = 10 - 2
dd = -1 + 2 + -22 - 3 + -1

"""
        expected_tokens = [
            Token(TokenType.IDENTIFICATION, 'x', 2),
            Token(TokenType.EQUAL, '=', 2),
            Token(TokenType.NUMBER, '-10', 2),
            Token(TokenType.IDENTIFICATION, 'y', 3),
            Token(TokenType.EQUAL, '=', 3),
            Token(TokenType.NUMBER, '-50', 3),
            Token(TokenType.IDENTIFICATION, 'z', 4),
            Token(TokenType.EQUAL, '=', 4),
            Token(TokenType.IDENTIFICATION, 'x', 4),
            Token(TokenType.ADD, '+', 4),
            Token(TokenType.IDENTIFICATION, 'y', 4),
            Token(TokenType.IDENTIFICATION, 'f', 5),
            Token(TokenType.EQUAL, '=', 5),
            Token(TokenType.NUMBER, '-10', 5),
            Token(TokenType.ADD, '+', 5),
            Token(TokenType.NUMBER, '-20', 5),
            Token(TokenType.IDENTIFICATION, 'vv', 6),
            Token(TokenType.EQUAL, '=', 6),
            Token(TokenType.NUMBER, '10', 6),
            Token(TokenType.SUB, '-', 6),
            Token(TokenType.NUMBER, '2', 6),
            Token(TokenType.IDENTIFICATION, 'dd', 7),
            Token(TokenType.EQUAL, '=', 7),
            Token(TokenType.NUMBER, '-1', 7),
            Token(TokenType.ADD, '+', 7),
            Token(TokenType.NUMBER, '2', 7),
            Token(TokenType.ADD, '+', 7),
            Token(TokenType.NUMBER, '-22', 7),
            Token(TokenType.SUB, '-', 7),
            Token(TokenType.NUMBER, '3', 7),
            Token(TokenType.ADD, '+', 7),
            Token(TokenType.NUMBER, '-1', 7)
        ]
        actual_tokens = EnhancedLexer().tokenize_text(code)

        self.assertEqual(expected_tokens, actual_tokens)

    def tearDown(self):
        """tearDown"""
        super(LexerUnitTest, self).tearDown()


if __name__ == '__main__':
    unittest.main()
