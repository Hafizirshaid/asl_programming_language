# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

"""

Expression Evaluator Module

"""

from lexer import Lexer, TokenType


class Evaluator:
    """ Expression Evaluator Class """

    def calculate(self, value1, value2, operator):
        """ Calcuates the result value
            of v1 and v2 by op
        Args:
            v1: first value
            v2: second value
            op: operation
        Returns:
            result of v1 op v2
        """

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
            result = value1 ^ value2
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
        return result

    def _is_operator(self, token_type: TokenType) -> bool:
        """ This function checks if token type is an operator
        Args:
            token_type: type of token
        Returns:
            True token is an operator
            False if token is not an operator
        """
        return (token_type == TokenType.EQUIVALENT or
                token_type == TokenType.EQUAL or
                token_type == TokenType.NOTEQUIVALENT or
                token_type == TokenType.GRATERTHAN or
                token_type == TokenType.LESSTHAN or
                token_type == TokenType.GRATERTHANOREQUAL or
                token_type == TokenType.LESSTHANOREQUAL or
                token_type == TokenType.ADD or
                token_type == TokenType.SUB or
                token_type == TokenType.MULT or
                token_type == TokenType.DIV or
                token_type == TokenType.MOD or
                token_type == TokenType.AND or
                token_type == TokenType.OR or
                token_type == TokenType.NOT)

    def evaluate(self, expression: str):
        """
        Desc:
            evaluate expression like (10 * 30 > 5),
            this should work for both logical and
            mathimatical expressions
        Args:
            expression: expression to be evaluated
        Returns:
            result of evaluating expression
        """

        if not expression:
            return False

        # "strip double and single quotes "
        expression = expression.strip("'")
        expression = expression.strip('"')

        lexer = Lexer()
        tokens = lexer.tokenize_text(expression)
        result = False

        # if only one token, return the same expression
        if len(tokens) == 1:
            result = expression
        else:
            try:
                result = self.evaluate_tokens(tokens)
            except:
                raise Exception(f"Unable to evaluate expression {expression}")
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

            if (token_type == TokenType.SPACE or
                token_type == TokenType.OPENPARANTHESIS):
                # Do Nothing
                pass

            if token_type == TokenType.CLOSINGPARANTHESIS:
                value1 = float(values_stack.pop())
                value2 = float(values_stack.pop())
                operator = operators_stack.pop()
                result = self.calculate(value2, value1, operator)
                values_stack.append(result)
                pass

            if token_type == TokenType.NUMBER or token_type == TokenType.REAL:
                values_stack.append(float(value))
            pass

        while operators_stack:
            operator = operators_stack.pop()
            value1 = values_stack.pop()
            value2 = values_stack.pop()
            result = self.calculate(value2, value1, operator)
            values_stack.append(result)

        return result
