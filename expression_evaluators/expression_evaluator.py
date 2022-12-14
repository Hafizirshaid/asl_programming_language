# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

"""

Expression Evaluator Module

Contains methods that calculates expressions like

10 + 10 * 5
(True & True) | False

"""

from exceptions.language_exception import ExpressionEvaluationError
from lexer.enhanced_lexer import EnhancedLexer
from lexer.lexer import TokenType


class Evaluator:
    """ Expression Evaluator Class """

    def __init__(self) -> None:
        """ Expression Evaluator Class Constructor """
        # empty constructor
        pass

    def clean_value(self, value):
        """ Convert value to float if type is float, or
            strip double quotes if value is string
        Args:
            value: value
        Returns:
            cleaned value
        """

        result = None
        if self.is_numeric(value):
            result = float(value)
        elif isinstance(value, str):
            result = value.strip('"')
        else:
            raise ExpressionEvaluationError("Unrecognized value type")
        return result

    def calculate(self, value1, value2, operator):
        """ Calculates the result value
            of v1 and v2 by op
        Args:
            v1: first value
            v2: second value
            op: operation
        Returns:
            result of v1 op v2
        """

        # Clean values before calculating result.
        value1 = self.clean_value(value1)
        value2 = self.clean_value(value2)

        if operator == "+":
            result = value1 + value2
        elif operator == "-":
            result = value1 - value2
        elif operator == "*":
            result = value1 * value2
        elif operator == "/":
            result = value1 / value2
        elif operator == "%":
            result = value1 % value2
        elif operator == "^":
            result = int(value1) ^ int(value2)
        elif operator == "&":
            result = value1 and value2
        elif operator == "|":
            result = value1 or value2
        elif operator == ">":
            result = value1 > value2
        elif operator == "<":
            result = value1 < value2
        elif operator == ">=":
            result = value1 >= value2
        elif operator == "<=":
            result = value1 <= value2
        elif operator == "==":
            result = value1 == value2
        elif operator == "!=":
            result = value1 != value2
        else:
            raise ExpressionEvaluationError(f"Unknown operator {operator}")
        return result

    def is_numeric(self, value):
        """ This function checks if value represents a number.
        Args:
            value: value
        Returns:
            True if value is a number
            False if value is not a number
        """

        try:
            float(value)
            return True
        except:
            return False

    def _is_operator(self, token_type: TokenType) -> bool:
        """ This function checks if token type is an operator
        Args:
            token_type: type of token
        Returns:
            True token is an operator
            False if token is not an operator
        """

        return (token_type == TokenType.EQUIVALENT
                or token_type == TokenType.EQUAL
                or token_type == TokenType.NOTEQUIVALENT
                or token_type == TokenType.GREATERTHAN
                or token_type == TokenType.LESSTHAN
                or token_type == TokenType.GREATERTHANOREQUAL
                or token_type == TokenType.LESSTHANOREQUAL
                or token_type == TokenType.ADD
                or token_type == TokenType.SUB
                or token_type == TokenType.MULT
                or token_type == TokenType.DIV
                or token_type == TokenType.MOD
                or token_type == TokenType.AND
                or token_type == TokenType.OR
                or token_type == TokenType.NOT)

    def evaluate(self, expression: str):
        """
        Desc:
            evaluate expression like (10 * 30 > 5),
            this should work for both logical and
            mathematical expressions
        Args:
            expression: expression to be evaluated
        Returns:
            result of evaluating expression
        """

        if not expression:
            return False

        # "strip double and single quotes "
        # expression = expression.strip("'")
        # expression = expression.strip('"')

        lexer = EnhancedLexer()
        tokens = lexer.tokenize_text(expression)
        result = False

        # if only one token, return the same expression
        if len(tokens) == 1:
            result = expression
        else:
            try:
                result = self.evaluate_tokens(tokens)
            except Exception as e:
                raise ExpressionEvaluationError(
                    f"Unable to evaluate expression {expression}")
        return result

    def evaluate_tokens(self, tokens: list):
        """
        Desc:
           Evaluate list of tokens and returns result
        Args:
            tokens: list of tokens
        Returns:
            result of evaluating tokens
        """

        values_stack = []
        operators_stack = []

        for token in tokens:
            token_type = token.token_type
            value = token.match
            if self._is_operator(token_type):
                operators_stack.append(value)

            if (token_type == TokenType.SPACE
                or token_type == TokenType.OPENPARENTHESIS):
                # Do Nothing
                pass

            if token_type == TokenType.CLOSINGPARENTHESIS:
                value1 = values_stack.pop()
                value2 = values_stack.pop()
                operator = operators_stack.pop()
                result = self.calculate(value2, value1, operator)
                values_stack.append(result)
                pass

            if (token_type == TokenType.NUMBER
                or token_type == TokenType.REAL
                or token_type == TokenType.STRING
                or token_type == TokenType.IDENTIFICATION):
                values_stack.append(value)
            pass

        while operators_stack:
            operator = operators_stack.pop()
            value1 = values_stack.pop()
            value2 = values_stack.pop()
            result = self.calculate(value2, value1, operator)
            values_stack.append(result)

        return result
