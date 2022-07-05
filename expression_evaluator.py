# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

"""
Expression Evaluator Module
"""

from lexer import Lexer


class Evaluator:
    """ Expression Evaluator Class """

    def calculate(self, v1, v2, op):
        """ Calcuate the result value of v1 and v2 by op
        Args:
            v1: first value 
            v2: second value
            op: operation
        Returns:
            result of v1 op v2
        """

        if op == "+":
            result = v1 + v2
        elif op == "-":
            result = v1 - v2
        elif op == "*":
            result = v1 * v2
        elif op == "/":
            result = v1 / v2
        elif op == "%":
            result = v1 % v2
        elif op == "^":
            result = v1 ^ v2
        elif op == "&":
            result = v1 and v2
        elif op == "|":
            result = v1 or v2
        elif op == ">":
            result = v1 > v2
        elif op == "<":
            result = v1 < v2
        elif op == ">=":
            result = v1 >= v2
        elif op == "<=":
            result = v1 <= v2
        elif op == "==":
            result = v1 == v2
        elif op == "!=":
            result = v1 != v2
        return result

    def evaluate(self, expression):
        """ evaluate expression
        Args:
            expression: expression to be evaluated
        Returns:
            result of evaluating expression
        """

        if not expression:
            return False

        result = False
        values_stack = []
        operators_stack = []
        lexer = Lexer()
        lexes = lexer.tokenize(expression)

        for lex in lexes:
            lex_type = lex['token_type']['type']

            value = lex['match'].group()

            if  lex_type == 'equivalent' or \
                lex_type == 'equal' or \
                lex_type == 'notequivalent' or \
                lex_type == 'graterthan' or \
                lex_type == 'lessthan' or \
                lex_type == 'graterthanorequal' or \
                lex_type == 'lessthanorequal' or \
                lex_type == 'add' or \
                lex_type == 'sub' or \
                lex_type == 'mult' or \
                lex_type == 'div' or \
                lex_type == 'mod' or \
                lex_type == 'and' or \
                lex_type == 'or' or \
                lex_type == 'not':

                operators_stack.append(value)
                pass

            if lex_type == "space":
                pass
            if lex_type == "openparanthesis":
                pass

            if lex_type == "closingparanthesis":
                value1 = float(values_stack.pop())
                value2 = float(values_stack.pop())
                operator = operators_stack.pop()
                result = self.calculate(value2, value1, operator)
                values_stack.append(result)
                pass

            if lex_type == "number":
                values_stack.append(float(value))
            pass

        while operators_stack:
            operator = operators_stack.pop()
            value1 = values_stack.pop()
            value2 = values_stack.pop()
            result = self.calculate(value2, value1, operator)
            values_stack.append(result)

        return result
