# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

"""

Enhanced Parser Library

Convert list of tokens into statements and extract their attributes

"""


from parser import Parser

from lexer import TokenType
from statements.statement import ElseIf, For, If, Variable, While
from exceptions.language_exception import SyntaxError


class EnhancedParser(Parser):
    """

    Enhanced Parser Class

    Contains methods to convert list of tokens into list of statements that can be
    executed

    """

    def __init__(self) -> None:
        """ Constructor
        Args:
            lexes: list of lexes

        Returns:
            list of statements
        """
        super().__init__()

        self.comments = [
            TokenType.COMMENT
        ]

        self.keywords = [
            TokenType.CALL,
            TokenType.METHOD,
            TokenType.ELIF,
            TokenType.IF,
            TokenType.ELSE,
            TokenType.FI,
            TokenType.FI,
            TokenType.ENDFOR,
            TokenType.ENDWHILE,
            TokenType.BREAK,
            TokenType.CONTINUE,
            TokenType.FOR,
            TokenType.WHILE,
            TokenType.STRUCT,
            TokenType.ENDSTRUCT,
            TokenType.ECHO,
            TokenType.PRINT,
            TokenType.INPUT,
            TokenType.RETURN,
            TokenType.TRUE,
            TokenType.FALSE
        ]

        self.valid_assignment_operation = [
            TokenType.EQUAL,
            TokenType.PLUSEQUAL,
            TokenType.SUBEQUAL,
            TokenType.MULTEQUAL,
            TokenType.DIVEQUAL,
            TokenType.INVERT
        ]

        self.math_operation = [
            TokenType.ADD,
            TokenType.SUB,
            TokenType.DIV,
            TokenType.MULT,
            TokenType.MOD,
            TokenType.EQUIVALENT,
            TokenType.NOTEQUIVALENT
        ]

        self.logical_operation = [
            TokenType.AND,
            TokenType.OR
        ]

    def check_token_type_in_list(self, lexes, token_types, stop_on=None):
        """ Checks if current token belongs to list of token types.
        Args:
            lexes: list of lexes
            token_types:
            stop_on:
        Returns:
            True:
            False:
        """
        token_type = lexes[self.token_pointer].token_type
        if token_type in token_types:
            return True

        if stop_on and token_type == stop_on:
            return False

        return False

    def is_there_more_tokens(self, lexes):
        return len(lexes) > self.token_pointer

    def parse_for(self, lexes, statements):
        """ Parse For loop
        Args:
            lexes: list of lexes

        Returns:
            list of statements
        """

        self.increment_token_pointer()

        paranthesis_stack = []

        if lexes[self.token_pointer].token_type == TokenType.OPENPARANTHESIS:

            paranthesis_stack.append(lexes[self.token_pointer].match)
            self.increment_token_pointer()

            loop_initial_variable = self.parse_for_loop_variable(lexes, paranthesis_stack)
            condition = self.parse_for_loop_condition(lexes, paranthesis_stack)
            increment = self.parse_for_loop_increment(lexes)

            # empty condition should return true, this is necessary for cases like;
            # for(;;)
            # in this case condition is an empty string, however, this has been used
            # as a technique for infinite loop, this language should support it.
            if len(condition) == 0:
                condition = "1"

            if lexes[self.token_pointer].token_type == TokenType.CLOSINGPARANTHESIS:
                paranthesis_stack.pop()
                if not paranthesis_stack:
                    forloop = For([], loop_initial_variable, condition, increment)
                    statements.append(forloop)
                else:
                    raise SyntaxError("invalid for loop, unbalanced paranthesis", lexes[self.token_pointer])
            else:
                raise SyntaxError("invalid for loop", lexes[self.token_pointer])
        else:
            raise SyntaxError("invalid for loop", lexes[self.token_pointer])

    def parse_for_loop_condition(self, lexes, paranthesis_stack):
        """ Parse for loop condition
        Args:
            lexes: list of lexes
            paranthesis_stack:
        Returns:
            Condition
        """

        self.increment_token_pointer()

        condition = ""
        while (lexes[self.token_pointer].token_type != TokenType.SEMICOLON):
            condition += lexes[self.token_pointer].match
            if lexes[self.token_pointer].token_type == TokenType.OPENPARANTHESIS:
                paranthesis_stack.append(lexes[self.token_pointer].match)
            if lexes[self.token_pointer].token_type == TokenType.CLOSINGPARANTHESIS:
                paranthesis_stack.pop()
            self.increment_token_pointer()

        self.increment_token_pointer()

        return condition

    def parse_for_loop_variable(self, lexes, paranthesis_stack):
        """ Parse for loop Variable
        Args:
            lexes: list of lexes
            paranthesis_stack:
        Returns:
            variable
        """

        var_name = ""
        var_op = ""
        var_val = ""

        # Empty Statement
        if lexes[self.token_pointer].token_type == TokenType.SEMICOLON:
            return None

        if lexes[self.token_pointer].token_type == TokenType.IDENTIFICATION:
            var_name = lexes[self.token_pointer].match

            self.increment_token_pointer()

            if self.check_token_type_in_list(lexes, self.valid_assignment_operation, TokenType.SEMICOLON):
                var_op = lexes[self.token_pointer].token_type
                self.increment_token_pointer()

                # Get variable expression.
                while lexes[self.token_pointer].token_type != TokenType.SEMICOLON:

                    var_val += lexes[self.token_pointer].match
                    if lexes[self.token_pointer].token_type == TokenType.OPENPARANTHESIS:
                        paranthesis_stack.append(
                            lexes[self.token_pointer].match)
                    if lexes[self.token_pointer].token_type == TokenType.CLOSINGPARANTHESIS:
                        paranthesis_stack.pop()
                    self.increment_token_pointer()

                return Variable(var_name, var_op, var_val)
        return None

    def parse_for_loop_increment(self, lexes):
        """ Parse for loop Increment
        Args:
            lexes: list of lexes
        Returns:
            Increment variable
        """

        # Empty Statement
        if lexes[self.token_pointer].token_type == TokenType.CLOSINGPARANTHESIS:
            return None

        if lexes[self.token_pointer].token_type == TokenType.IDENTIFICATION:
            var_name = lexes[self.token_pointer].match
            self.increment_token_pointer()

            if self.check_token_type_in_list(lexes, self.valid_assignment_operation, TokenType.CLOSINGPARANTHESIS):
                var_operation = lexes[self.token_pointer].token_type
                self.increment_token_pointer()
                var_val = ""

                # Get variable expression.
                while (lexes[self.token_pointer].token_type != TokenType.CLOSINGPARANTHESIS):
                    if lexes[self.token_pointer].token_type == TokenType.OPENPARANTHESIS:
                        var_val += self.parse_between_paranthesis(lexes)
                    else:
                        var_val += lexes[self.token_pointer].match

                    self.increment_token_pointer()

                return Variable(var_name, var_operation, var_val)
            else:
                raise SyntaxError("Invalid op ", lexes[self.token_pointer])
        return None

    def parse_while(self, lexes, statements):
        """ Parse While Loop
        Args:
            lexes: list of lexes

        Returns:
            list of statements
        """

        self.increment_token_pointer()
        while_condition = self.parse_between_paranthesis(lexes)
        while_statement = While(while_condition, [])
        statements.append(while_statement)

    def parse_variable(self, lexes, statements):
        """ Parse Variable
        Args:
            lexes: list of lexes

        Returns:
            list of statements
        """

        variable_name = lexes[self.token_pointer].match
        self.increment_token_pointer()

        if self.is_valid_variable_operation(lexes[self.token_pointer].token_type):

            operation = lexes[self.token_pointer].token_type
            self.increment_token_pointer()
            variable_value = ""

            should_continue = True
            first_token_type = None

            while (should_continue):

                next_lex = lexes[self.token_pointer]

                if (next_lex.token_type == TokenType.IDENTIFICATION
                    or next_lex.token_type == TokenType.NUMBER
                    or next_lex.token_type == TokenType.REAL
                    or next_lex.token_type == TokenType.STRING):

                    first_token_type = next_lex.token_type
                    variable_value += next_lex.match

                    self.increment_token_pointer()
                    #next_lex = lexes[self.token_pointer]
                else:
                    raise SyntaxError("Invalid id or num ", lexes[self.token_pointer])

                if not self.is_there_more_tokens(lexes):

                    break
                else:
                    next_lex = lexes[self.token_pointer]

                if (next_lex.token_type == TokenType.ADD
                    or next_lex.token_type == TokenType.SUB
                    or next_lex.token_type == TokenType.DIV
                    or next_lex.token_type == TokenType.MULT
                    or next_lex.token_type == TokenType.AND
                    or next_lex.token_type == TokenType.OR
                    or next_lex.token_type == TokenType.EQUIVALENT
                    or next_lex.token_type == TokenType.NOTEQUIVALENT):
                    variable_value += next_lex.match
                    self.increment_token_pointer()

                else:
                    break
                    #self.increment_token_pointer()
                    #next_lex = lexes[self.token_pointer]


                # if (next_lex.token_type == TokenType.IDENTIFICATION
                #     or next_lex.token_type == TokenType.NUMBER
                #     or next_lex.token_type == TokenType.REAL
                #     or next_lex.token_type in self.keywords
                #     or next_lex.token_type in self.comments):
                #     should_continue = False
                #     # Found new statement
                #     break

                # if (next_lex.token_type == TokenType.ADD
                #     or next_lex.token_type == TokenType.SUB
                #     or next_lex.token_type == TokenType.DIV
                #     or next_lex.token_type == TokenType.MULT
                #     or next_lex.token_type == TokenType.AND
                #     or next_lex.token_type == TokenType.OR
                #     or next_lex.token_type == TokenType.EQUIVALENT
                #     or next_lex.token_type == TokenType.NOTEQUIVALENT):


                # else:
                #     raise SyntaxError("Invalid id or num ", lexes[self.token_pointer])

            # Token pointer now points at next token outside variable scope,
            # this has caused an error with next statement
            self.token_pointer -= 1

            variable_statement = Variable(variable_name, operation, variable_value, first_token_type)
            statements.append(variable_statement)
        else:
            raise SyntaxError("Invalid operation ",
                              lexes[self.token_pointer])

    def is_valid_variable_operation(self, operation: TokenType):
        """ is_valid_variable_operation
        Args:
            operation:

        Returns:
            True:
            False:
        """

        return operation in self.valid_assignment_operation

    def parse_elseif(self, lexes, statements):
        """ Parse else if
        Args:
            lexes: list of lexes

        Returns:
            list of statements
        """

        self.increment_token_pointer()
        elif_condition = self.parse_between_paranthesis(lexes)
        elif_Statement = ElseIf(elif_condition, [])
        statements.append(elif_Statement)
        pass

    def parse_if(self, lexes, statements):
        """ Parse if statement
        Args:
            lexes: list of lexes

        Returns:
            list of statements
        """

        self.increment_token_pointer()

        if_condition = self.parse_between_paranthesis(lexes)

        if_statement = If(if_condition, [])
        statements.append(if_statement)
        pass

    def parse_between_paranthesis(self, lexes):
        """ Parse between paranthesis
        Args:
            lexes: list of lexes

        Returns:
            list of statements
        """

        paranthesis_stack = []
        if lexes[self.token_pointer].token_type == TokenType.OPENPARANTHESIS:
            paranthesis_stack.append(lexes[self.token_pointer].token_type)

            if_condition = lexes[self.token_pointer].match

            while paranthesis_stack:
                self.increment_token_pointer()
                if lexes[self.token_pointer].token_type == TokenType.OPENPARANTHESIS:
                    paranthesis_stack.append(lexes[self.token_pointer].token_type)
                if lexes[self.token_pointer].token_type == TokenType.CLOSINGPARANTHESIS:
                    paranthesis_stack.pop()

                if_condition += lexes[self.token_pointer].match

            if paranthesis_stack:
                raise SyntaxError("paranthesis error", lexes[self.token_pointer])

            return if_condition
        else:
            raise SyntaxError(
                "invalid token should be ( instead of " + str(lexes[self.token_pointer].match), lexes[self.token_pointer])

    def parse_echo(self, lexes, statements):
        """ Parse echo statement
        Args:
            lexes: list of lexes

        Returns:
            list of statements
        """
        super().parse_echo(lexes, statements)
