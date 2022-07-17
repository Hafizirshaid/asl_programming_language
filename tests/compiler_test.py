import unittest

from lexer import Lexer


class TestLexer(unittest.TestCase):
    def setUp(self):
        super(TestLexer, self).setUp()

    def test(self):
        text = """
echo "testing for loop"
for "var=1;var <= 10;var = var + 1"
    if "(var % 2) == 0"
        echo "{var} is even"
    else
        echo "{var} is odd"
    fi
endfor
        """

        tokens = Lexer().tokenize_text(text)

        #self.assertEqual(len(tokens), 22)
        self.fail("failed like this")
        # self.assertEqual([])

    def tearDown(self):
        super(TestLexer, self).tearDown()


class TestCompiler(unittest.TestCase):
    def setUp(self):
        super(TestCompiler, self).setUp()
        self.mock_text = "x=10"

    def test1(self):
        tokens = Lexer().tokenize_text(self.mock_text)

    def test2(self):
        tokens = Lexer().tokenize_text(self.mock_text)

        self.assertEqual(len(tokens), 3)

    def tearDown(self):
        super(TestCompiler, self).tearDown()
        self.mock_text = ""

if __name__ == '__main__':
    unittest.main()
