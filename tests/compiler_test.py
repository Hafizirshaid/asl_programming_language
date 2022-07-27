import unittest

from lexer import Lexer, TokenType

"""

TODO: to be implemented

"""

class TestCompiler(unittest.TestCase):
    def setUp(self):
        super(TestCompiler, self).setUp()

    def test_compiler_program(self):
        text = """
for    

(

    var

    = 

    1

    ;

    var 

    > 

    10

    ;

    var 

    +=

    1


)       """

        tokens = Lexer().tokenize_text(text)



        token_pointer = 0

        if tokens[token_pointer].token_type == TokenType.NEWLINE:

            token_pointer += 1

        else:
            if tokens[token_pointer].token_type == TokenType.FOR:
                pass

        pass

    def tearDown(self):
        super(TestCompiler, self).tearDown()


if __name__ == '__main__':
    unittest.main()
