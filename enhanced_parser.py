# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

"""

Enhanced Parser Library

Convert list of tokens into statements and extract thier attributes

"""


from parser import Parser

from lexer import TokenType
from statements.statement import ElseIf, For, If, While


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
            # eat first expression
            loop_initial_variable = ""
            while (lexes[self.token_pointer].token_type != TokenType.SEMICOLON
                    and lexes[self.token_pointer].token_type != TokenType.NEWLINE):

                loop_initial_variable += lexes[self.token_pointer].match

                if lexes[self.token_pointer].token_type == TokenType.OPENPARANTHESIS:
                    paranthesis_stack.append(lexes[self.token_pointer].match)
                if lexes[self.token_pointer].token_type == TokenType.CLOSINGPARANTHESIS:
                    paranthesis_stack.pop()

                self.increment_token_pointer()

            # done, eat conditon

            self.increment_token_pointer()
            condition = ""
            while (lexes[self.token_pointer].token_type != TokenType.SEMICOLON
                   and lexes[self.token_pointer].token_type != TokenType.NEWLINE):
                condition += lexes[self.token_pointer].match
                if lexes[self.token_pointer].token_type == TokenType.OPENPARANTHESIS:
                    paranthesis_stack.append(lexes[self.token_pointer].match)
                if lexes[self.token_pointer].token_type == TokenType.CLOSINGPARANTHESIS:
                    paranthesis_stack.pop()
                self.increment_token_pointer()

            self.increment_token_pointer()

            increment = ""
            while (lexes[self.token_pointer].token_type != TokenType.SEMICOLON
                    and lexes[self.token_pointer].token_type != TokenType.NEWLINE
                    and lexes[self.token_pointer].token_type != TokenType.CLOSINGPARANTHESIS):
                increment += lexes[self.token_pointer].match

                if lexes[self.token_pointer].token_type == TokenType.OPENPARANTHESIS:
                    paranthesis_stack.append(lexes[self.token_pointer].match)
                if lexes[self.token_pointer].token_type == TokenType.CLOSINGPARANTHESIS:
                    paranthesis_stack.pop()

                self.increment_token_pointer()

            if lexes[self.token_pointer].token_type == TokenType.CLOSINGPARANTHESIS:
                paranthesis_stack.pop()
                if not paranthesis_stack:
                    forloop = For([], loop_initial_variable,
                                  condition, increment)
                    statements.append(forloop)
                else:
                    raise SyntaxError(
                        "invalid for loop, unbalanced paranthesis")
            else:
                raise SyntaxError("invalid for loop")
        else:
            raise SyntaxError("invalid for loop")

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

        super().parse_variable(lexes, statements)

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
            self.increment_token_pointer()

            while paranthesis_stack:
                if lexes[self.token_pointer].token_type == TokenType.OPENPARANTHESIS:
                    paranthesis_stack.append(
                        lexes[self.token_pointer].token_type)
                if lexes[self.token_pointer].token_type == TokenType.CLOSINGPARANTHESIS:
                    paranthesis_stack.pop()

                if_condition += lexes[self.token_pointer].match
                self.increment_token_pointer()

            if paranthesis_stack:
                raise SyntaxError("Paranths error")

            return if_condition
        else:
            raise SyntaxError(
                "invalid token should be ( insteadof " + str(lexes[self.token_pointer].match))

    def parse_echo(self, lexes, statements):
        """ Parse echo statement
        Args:
            lexes: list of lexes

        Returns:
            list of statements
        """
        super().parse_echo(lexes, statements)
