
from expression_evaluator import Evaluator
from lexer import Lexer, TokenType
"""
This class is not used.
"""

class EnhancedExpressionEvaluator(Evaluator):

    def __init__(self) -> None:
        super().__init__()

    def calculate2(self, value1, value2, operator):
        if self.is_numeric(value1) and self.is_numeric(value2):
            value1 = float(value1)
            value2 = float(value2)
        else:
            if isinstance(value1, str):
                value1 = value1.strip('"')
            if isinstance(value2, str):
                value2 = value2.strip('"')
        return self.calculate(value1, value2, operator)

    def evaluate(self, expression: str):
        #return super().evaluate(expression)

        # print(self.calculate("10", "10", "+"))

        tokens = Lexer().tokenize_text(expression, keep_unknown=True, keep_spaces=True, ignore_new_lines=False)

        values_stack = []
        operators_stack = []

        contains_string = False
        for token in tokens:
            if token.token_type == TokenType.STRING:
                contains_string = True
                break
        result = ""
        if contains_string:
            for token in tokens:
                if not self._is_operator(token.token_type):
                    result += token.match.strip('"')
            # should concatenate
        else:
            result = self.evaluate_tokens(tokens, values_stack, operators_stack)
        return result

    def evaluate_tokens(self, tokens, values_stack, operators_stack):
        for token in tokens:
            token_type = token.token_type
            value = token.match
            if self._is_operator(token_type):
                operators_stack.append(value)

            elif (token_type == TokenType.SPACE or
                token_type == TokenType.OPENPARENTHESIS):
                # Do Nothing
                pass

            elif token_type == TokenType.CLOSINGPARENTHESIS:
                value1 = (values_stack.pop())
                value2 = (values_stack.pop())
                operator = operators_stack.pop()
                result = self.calculate2(value2, value1, operator)
                values_stack.append(result)

            elif not self._is_operator(token_type):
                # token_type == TokenType.NUMBER
                # or token_type == TokenType.REAL
                # or token_type == TokenType.IDENTIFICATION
                # or token_type == TokenType.SPACE):
                if values_stack and token_type == TokenType.SPACE:
                    v = values_stack[-1]
                    v += " "
                    values_stack[-1] = v
                else:
                    values_stack.append((value))

        while operators_stack:
            operator = operators_stack.pop()
            value1 = values_stack.pop()
            value2 = values_stack.pop()
            result = self.calculate2(value2, value1, operator)
            values_stack.append(result)
        return result

