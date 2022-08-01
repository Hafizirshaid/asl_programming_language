import unittest

from numpy import true_divide
from exceptions.language_exception import ExpressionEvaluationError
from expression_evaluator import Evaluator

from lexer import Lexer, TokenType

"""

TODO: to be implemented

"""

class ExpressionEvaluatorUnitTest(unittest.TestCase):
    def setUp(self):
        super(ExpressionEvaluatorUnitTest, self).setUp()

    def test_expression_evaluator_1(self):
        result = Evaluator().evaluate("10 > 20")
        self.assertEqual(result, 10 > 20)

    def test_expression_evaluator_2(self):
        result = Evaluator().evaluate("(10 + 2) / 6")
        self.assertEqual(result, (10 + 2) / 6)

    def test_expression_evaluator_3(self):
        result = Evaluator().evaluate("(10 > 2) & (20 < 30)")
        self.assertEqual(result, (10 > 2) and (20 < 30))

    def test_expression_evaluator_4(self):
        result = Evaluator().evaluate("\"hafiz\" == \"hafiz\"")
        self.assertEqual(result, "hafiz" == "hafiz")

    def test_expression_evaluator_5(self):
        result = Evaluator().evaluate("60 * 70")
        self.assertEqual(result, 60 * 70)

    def test_expression_evaluator_6(self):
        result = Evaluator().evaluate("\"hafizx\" > \"hafiz\"")
        self.assertEqual(result, "hafizx" > "hafiz")

    def test_expression_evaluator_7(self):
        result = Evaluator().evaluate("10 > 20")
        self.assertEqual(result, False)

    def test_expression_evaluator_8(self):
        result = Evaluator().evaluate("\"hafizzz\" != \"hafiz\"")
        self.assertEqual(result, "hafizzz" != "hafiz")

    def test_expression_evaluator_9(self):
        result = Evaluator().evaluate("\"string1234\" != \"string12345\"")
        self.assertEqual(result, "string1234" != "string12345")

    def test_expression_evaluator_10(self):
        result = Evaluator().evaluate("((7 + 2) > 4) & ((11 % 2) == 1)")
        self.assertEqual(result, ((7 + 2) > 4) and ((11 % 2) == 1))

    def test_expression_evaluator_11(self):
        result = Evaluator().evaluate("10 > 20")
        self.assertEqual(result, 10 > 20)

    def test_expression_evaluator_12(self):
        result = Evaluator().evaluate("20 > 10")
        self.assertEqual(result, 20 > 10)

    def test_expression_evaluator_13(self):
        result = Evaluator().evaluate("10 == 1")
        self.assertEqual(result, 10 == 1)

    def test_expression_evaluator_14(self):
        result = Evaluator().evaluate("1 == 10")
        self.assertEqual(result, 1 == 10)

    def test_expression_evaluator_15(self):
        result = Evaluator().evaluate("10 == 10")
        self.assertEqual(result, 10 == 10)

    def test_expression_evaluator_16(self):
        evaluator = Evaluator()
        self.assertRaises(ExpressionEvaluationError, evaluator.evaluate, "1 == ")

    def tearDown(self):
        super(ExpressionEvaluatorUnitTest, self).tearDown()


if __name__ == '__main__':
    unittest.main()
