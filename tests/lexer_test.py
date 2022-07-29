import unittest

from numpy import true_divide
from exceptions.language_exception import ExpressionEvaluationError
from expression_evaluator import Evaluator

from lexer import Lexer, Token, TokenType

"""

TODO: to be implemented

"""


class ExpressionEvaluatorUnitTest(unittest.TestCase):
    def setUp(self):
        super(ExpressionEvaluatorUnitTest, self).setUp()

    def test_lexer_ifstatement_for_loop(self):
        text = """x = 10

for "i=0;i<10;i=i+1"
    if "i==0"
        echo "stmt says i is 0"
    elif "i==1"
        echo "stmt says i is 1"
    elif "i==2"
        echo "stmt says i is 2"
    elif "i==3"
        echo "stmt says i is 3"
    elif "i==4"
        echo "stmt says i is 4"
    elif "i==5"
        echo "stmt says i is 5"
    else
        echo "not checked i is {i}"
    fi
endfor"""

        actual = Lexer().tokenize_text(text)

        expected = [
            Token(TokenType.IDENTIFICATION, 'x', 1),
            Token(TokenType.EQUAL, '=', 1),
            Token(TokenType.NUMBER, '10', 1),
            Token(TokenType.NEWLINE, '', 1),
            Token(TokenType.NEWLINE, '', 2),
            Token(TokenType.FOR, 'for', 3),
            Token(TokenType.STRING, '"i=0;i<10;i=i+1"', 3),
            Token(TokenType.NEWLINE, '', 3),
            Token(TokenType.IF, 'if', 4),
            Token(TokenType.STRING, '"i==0"', 4),
            Token(TokenType.NEWLINE, '', 4),
            Token(TokenType.ECHO, 'echo', 5),
            Token(TokenType.STRING, '"stmt says i is 0"', 5),
            Token(TokenType.NEWLINE, '', 5),
            Token(TokenType.ELIF, 'elif', 6),
            Token(TokenType.STRING, '"i==1"', 6),
            Token(TokenType.NEWLINE, '', 6),
            Token(TokenType.ECHO, 'echo', 7),
            Token(TokenType.STRING, '"stmt says i is 1"', 7),
            Token(TokenType.NEWLINE, '', 7),
            Token(TokenType.ELIF, 'elif', 8),
            Token(TokenType.STRING, '"i==2"', 8),
            Token(TokenType.NEWLINE, '', 8),
            Token(TokenType.ECHO, 'echo', 9),
            Token(TokenType.STRING, '"stmt says i is 2"', 9),
            Token(TokenType.NEWLINE, '', 9),
            Token(TokenType.ELIF, 'elif', 10),
            Token(TokenType.STRING, '"i==3"', 10),
            Token(TokenType.NEWLINE, '', 10),
            Token(TokenType.ECHO, 'echo', 11),
            Token(TokenType.STRING, '"stmt says i is 3"', 11),
            Token(TokenType.NEWLINE, '', 11),
            Token(TokenType.ELIF, 'elif', 12),
            Token(TokenType.STRING, '"i==4"', 12),
            Token(TokenType.NEWLINE, '', 12),
            Token(TokenType.ECHO, 'echo', 13),
            Token(TokenType.STRING, '"stmt says i is 4"', 13),
            Token(TokenType.NEWLINE, '', 13),
            Token(TokenType.ELIF, 'elif', 14),
            Token(TokenType.STRING, '"i==5"', 14),
            Token(TokenType.NEWLINE, '', 14),
            Token(TokenType.ECHO, 'echo', 15),
            Token(TokenType.STRING, '"stmt says i is 5"', 15),
            Token(TokenType.NEWLINE, '', 15),
            Token(TokenType.ELSE, 'else', 16),
            Token(TokenType.NEWLINE, '', 16),
            Token(TokenType.ECHO, 'echo', 17),
            Token(TokenType.STRING, '"not checked i is {i}"', 17),
            Token(TokenType.NEWLINE, '', 17),
            Token(TokenType.FI, 'fi', 18),
            Token(TokenType.NEWLINE, '', 18),
            Token(TokenType.ENDFOR, 'endfor', 19)]

        for i, val in enumerate(expected):
            self.assertEquals(val.match, actual[i].match, "Not Matched value")
            self.assertEquals(
                val.token_type, actual[i].token_type, "Not Matched token type")
            self.assertEquals(
                val.line_number, actual[i].line_number, "Not Matched line number")

    def tearDown(self):
        super(ExpressionEvaluatorUnitTest, self).tearDown()


if __name__ == '__main__':
    unittest.main()
