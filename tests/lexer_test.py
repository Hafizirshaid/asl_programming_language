import unittest

from numpy import true_divide
from enhanced_lexer import EnhancedLexer
from exceptions.language_exception import ExpressionEvaluationError
from expression_evaluator import Evaluator

from lexer import Lexer, Token, TokenType


class LexerUnitTest(unittest.TestCase):
    def setUp(self):
        super(LexerUnitTest, self).setUp()

    def test_lexer2(self):

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

        tokens_2 = EnhancedLexer().tokenize_text(code)
        tokens_1 = Lexer().tokenize_text(code)

        for i, val in enumerate(tokens_1):
            if val.token_type != tokens_2[i].token_type:
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
        file_name = 'asl_files/new_lexer.asl'
        code = ""
        with open(file_name) as file:
            for line in file:
                code += line
        tokens_2 = EnhancedLexer().tokenize_text(code)

        expected_tokens = [Token(TokenType.IDENTIFICATION, 'print_value', 1),
                           Token(TokenType.EQUAL, '=', 1),
                           Token(TokenType.NUMBER, '1', 1),
                           Token(TokenType.IDENTIFICATION, 'if_cond', 1),
                           Token(TokenType.EQUAL, '=', 1),
                           Token(TokenType.NUMBER, '2', 1),
                           Token(TokenType.IDENTIFICATION, 'else_cond', 1),
                           Token(TokenType.EQUAL, '=', 1),
                           Token(TokenType.NUMBER, '3', 1),
                           Token(TokenType.IDENTIFICATION, 'echo_var', 1),
                           Token(TokenType.EQUAL, '=', 1),
                           Token(TokenType.NUMBER, '333', 1),
                           Token(TokenType.IDENTIFICATION, 'elif_cond', 1),
                           Token(TokenType.EQUAL, '=', 1),
                           Token(TokenType.NUMBER, '22', 1),
                           Token(TokenType.IDENTIFICATION, 'fi_cond', 1),
                           Token(TokenType.EQUAL, '=', 1),
                           Token(TokenType.NUMBER, '22', 1)]

        for i, tok in enumerate(expected_tokens):
            self.assertEqual(tok.token_type, tokens_2[i].token_type)

    def test_tokenize_while_loop(self):

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
        code = "222.333"
        actual_tokens = EnhancedLexer().tokenize_text(code)
        expected_tokens = [Token(TokenType.REAL, "222.333", 1)]
        self.assertEqual(actual_tokens, expected_tokens)

    def test_tokenize_identifier(self):
        code = "variable_1"
        actual_tokens = EnhancedLexer().tokenize_text(code)
        expected_tokens = [Token(TokenType.IDENTIFICATION, "variable_1", 1)]
        self.assertEqual(actual_tokens, expected_tokens)

    def test_tokenize_string(self):
        code = '"hello, world!"'
        actual_tokens = EnhancedLexer().tokenize_text(code)
        expected_tokens = [Token(TokenType.STRING, '"hello, world!"', 1)]
        self.assertEqual(actual_tokens, expected_tokens)

    def test_tokenize_comment(self):
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
        expected_tokens = [Token(TokenType.COMMENT, '', 2),
                           Token(TokenType.IDENTIFICATION, 'var', 2),
                           Token(TokenType.EQUAL, '=', 2),
                           Token(TokenType.NUMBER, '1', 2),
                           Token(TokenType.COMMENT, '', 3),
                           Token(TokenType.IDENTIFICATION, 'var2', 3),
                           Token(TokenType.EQUAL, '=', 3),
                           Token(TokenType.NUMBER, '2', 3)]

        self.assertEqual(actual_tokens, expected_tokens)

    def test_tokenize_input(self):
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

    # TODO For each char, create test case for it.

    def tearDown(self):
        super(LexerUnitTest, self).tearDown()


if __name__ == '__main__':
    unittest.main()
