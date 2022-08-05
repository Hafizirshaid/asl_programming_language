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


    def tearDown(self):
        super(LexerUnitTest, self).tearDown()


if __name__ == '__main__':
    unittest.main()
