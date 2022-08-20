# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

"""

Enhanced Parser Library

Convert list of tokens into statements and extract their attributes

"""


# from parser import Parser


from lexer.lexer import Token, TokenType
from statements.statement import Echo, Else, ElseIf, EndFor, EndWhile, Fi, For, If, Input, Variable, VariableType, While, Break, Continue
from exceptions.language_exception import SyntaxError


class EnhancedParser:
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

        self.token_pointer = 0

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

    def increment_token_pointer(self):
        """ Increment Token Pointer by 1 """
        self.token_pointer += 1

    def parse(self, lexes: list) -> list:
        """ Parse list of lexes
        Args:
            lexes: list of lexes

        Returns:
            list of statements
        """

        statements = []

        self.token_pointer = 0

        while self.token_pointer <= len(lexes) - 1:

            lex = lexes[self.token_pointer]
            lex_type = lex.token_type

            if lex_type == TokenType.ECHO or lex_type == TokenType.PRINT:
                self.parse_echo(lexes, statements)
            elif lex_type == TokenType.INPUT:
                self.parse_input(lexes, statements)
            elif lex_type == TokenType.IF:
                self.parse_if(lexes, statements)
            elif lex_type == TokenType.ELSE:
                self.parse_else(statements)
            elif lex_type == TokenType.ELIF:
                self.parse_elseif(lexes, statements)
            elif lex_type == TokenType.FI:
                self.parse_endif(statements)
            elif lex_type == TokenType.ENDFOR:
                self.parse_endfor(statements)
            elif lex_type == TokenType.ENDWHILE:
                self.parse_endwhile(statements)
            elif lex_type == TokenType.BREAK:
                self.parse_break(statements)
            elif lex_type == TokenType.CONTINUE:
                self.parse_continue(statements)
            elif lex_type == TokenType.FOR:
                self.parse_for(lexes, statements)
            elif lex_type == TokenType.WHILE:
                self.parse_while(lexes, statements)
            elif lex_type == TokenType.IDENTIFICATION:
                self.parse_variable(lexes, statements)
            elif lex_type == TokenType.NEWLINE:
                pass
            elif lex_type == TokenType.COMMENT:
                pass
            else:
                self.handle_syntax_error(lex, "Unexpected token")

            # Increment Index to get next token
            self.increment_token_pointer()

        return statements

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
        """ This Method Checks if lexes list contains more tokens or not.
        Args:
            lexes: List of tokens.
        Returns:
            True:  If there are more tokens.
            False: If there are not more tokens.
        """
        return len(lexes) > self.token_pointer

    def parse_for(self, lexes, statements):
        """ Parse For loop
        Args:
            lexes: list of lexes

        Returns:
            list of statements
        """

        self.increment_token_pointer()

        parenthesis_stack = []

        if lexes[self.token_pointer].token_type == TokenType.OPENPARENTHESIS:

            parenthesis_stack.append(lexes[self.token_pointer].match)
            self.increment_token_pointer()

            loop_initial_variable = self.parse_for_loop_variable(lexes, parenthesis_stack)
            condition = self.parse_for_loop_condition(lexes, parenthesis_stack)
            increment = self.parse_for_loop_increment(lexes)

            # empty condition should return true, this is necessary for cases like;
            # for(;;)
            # in this case condition is an empty string, however, this has been used
            # as a technique for infinite loop, this language should support it.
            if len(condition) == 0:
                condition = "1"

            if lexes[self.token_pointer].token_type == TokenType.CLOSINGPARENTHESIS:
                parenthesis_stack.pop()
                if not parenthesis_stack:
                    forloop = For([], loop_initial_variable, condition, increment)
                    statements.append(forloop)
                else:
                    self.handle_syntax_error(lexes[self.token_pointer], "invalid for loop, unbalanced parenthesis")
            else:
                self.handle_syntax_error(lexes[self.token_pointer], "invalid for loop")
        else:
            self.handle_syntax_error(lexes[self.token_pointer], "invalid for loop")

    def parse_for_loop_condition(self, lexes, parenthesis_stack):
        """ Parse for loop condition
        Args:
            lexes: list of lexes
            parenthesis_stack:
        Returns:
            Condition
        """

        self.increment_token_pointer()

        condition = ""
        while (lexes[self.token_pointer].token_type != TokenType.SEMICOLON):
            condition += lexes[self.token_pointer].match
            if lexes[self.token_pointer].token_type == TokenType.OPENPARENTHESIS:
                parenthesis_stack.append(lexes[self.token_pointer].match)
            if lexes[self.token_pointer].token_type == TokenType.CLOSINGPARENTHESIS:
                parenthesis_stack.pop()
            self.increment_token_pointer()

        self.increment_token_pointer()

        return condition

    def parse_expression(self, lexes):
        if (lexes[self.token_pointer].token_type == TokenType.NUMBER
            or lexes[self.token_pointer].token_type == TokenType.REAL):
            pass

        pass
    def parse_for_loop_variable(self, lexes, parenthesis_stack):
        """ Parse for loop Variable
        Args:
            lexes: list of lexes
            parenthesis_stack:
        Returns:
            variable
        """

        # Empty Statement
        if lexes[self.token_pointer].token_type == TokenType.SEMICOLON:
            return None

        if lexes[self.token_pointer].token_type == TokenType.IDENTIFICATION:
            var_name = lexes[self.token_pointer].match

            self.increment_token_pointer()

            if self.check_token_type_in_list(lexes, self.valid_assignment_operation, TokenType.SEMICOLON):
                var_op = lexes[self.token_pointer].token_type
                self.increment_token_pointer()
                var_val = ""
                # Get variable expression.
                while lexes[self.token_pointer].token_type != TokenType.SEMICOLON:

                    var_val += lexes[self.token_pointer].match
                    if lexes[self.token_pointer].token_type == TokenType.OPENPARENTHESIS:
                        parenthesis_stack.append(
                            lexes[self.token_pointer].match)
                    if lexes[self.token_pointer].token_type == TokenType.CLOSINGPARENTHESIS:
                        parenthesis_stack.pop()
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
        if lexes[self.token_pointer].token_type == TokenType.CLOSINGPARENTHESIS:
            return None

        if lexes[self.token_pointer].token_type == TokenType.IDENTIFICATION:
            var_name = lexes[self.token_pointer].match
            self.increment_token_pointer()

            if self.check_token_type_in_list(lexes, self.valid_assignment_operation, TokenType.CLOSINGPARENTHESIS):
                var_operation = lexes[self.token_pointer].token_type
                self.increment_token_pointer()
                var_val = ""

                # Get variable expression.
                while (lexes[self.token_pointer].token_type != TokenType.CLOSINGPARENTHESIS):
                    if lexes[self.token_pointer].token_type == TokenType.OPENPARENTHESIS:
                        var_val += self.parse_between_parenthesis(lexes)
                    else:
                        var_val += lexes[self.token_pointer].match

                    self.increment_token_pointer()

                return Variable(var_name, var_operation, var_val)
            else:
                self.handle_syntax_error(lexes[self.token_pointer], "Invalid operation")
        return None

    def parse_while(self, lexes, statements):
        """ Parse While Loop
        Args:
            lexes: list of lexes

        Returns:
            list of statements
        """

        self.increment_token_pointer()
        while_condition = self.parse_between_parenthesis(lexes)
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

            if lexes[self.token_pointer].token_type == TokenType.OPENSQUAREBRACKET:
                # Handle Array Here initialization
                variable_value = []
                self.increment_token_pointer()

                while lexes[self.token_pointer].token_type != TokenType.CLOSESQUAREBRACKET:
                    if (lexes[self.token_pointer].token_type == TokenType.NUMBER
                        or lexes[self.token_pointer].token_type == TokenType.REAL
                        or lexes[self.token_pointer].token_type == TokenType.STRING):

                        variable_value.append(lexes[self.token_pointer].match)

                    self.increment_token_pointer()

                first_token_type = VariableType.ARRAY
                pass
            else:
                first_token_type, variable_value = self.parse_variable_expression(lexes)
                # Token pointer now points at next token outside variable scope,
                # this has caused an error with next statement
                self.token_pointer -= 1

            variable_statement = Variable(variable_name, operation, variable_value, first_token_type)
            statements.append(variable_statement)
        elif lexes[self.token_pointer].token_type == TokenType.OPENSQUAREBRACKET:
            # Array referencing here.
            self.increment_token_pointer()

            while lexes[self.token_pointer].token_type != TokenType.CLOSESQUAREBRACKET:
                self.increment_token_pointer()
            pass
        else:
            self.handle_syntax_error(lexes[self.token_pointer], "Invalid operation")

    def parse_variable_expression(self, lexes):
        should_continue = True
        first_token_type = None
        variable_value = ""

        while (should_continue):
            next_lex = lexes[self.token_pointer]

            if (next_lex.token_type == TokenType.IDENTIFICATION
                    or next_lex.token_type == TokenType.NUMBER
                    or next_lex.token_type == TokenType.REAL
                    or next_lex.token_type == TokenType.STRING):
                first_token_type = next_lex.token_type
                variable_value += next_lex.match

                self.increment_token_pointer()
            else:
                self.handle_syntax_error(lexes[self.token_pointer], "Invalid identification or number")

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
        return first_token_type, variable_value

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
        elif_condition = self.parse_between_parenthesis(lexes)
        elif_statement = ElseIf(elif_condition, [])
        statements.append(elif_statement)
        pass

    def parse_if(self, lexes, statements):
        """ Parse if statement
        Args:
            lexes: list of lexes

        Returns:
            list of statements
        """

        self.increment_token_pointer()

        if_condition = self.parse_between_parenthesis(lexes)

        if_statement = If(if_condition, [])
        statements.append(if_statement)
        pass

    def parse_between_parenthesis(self, lexes):
        """ Parse between parenthesis
        Args:
            lexes: list of lexes

        Returns:
            condition between parenthesis as string
        """

        parenthesis_stack = []
        if lexes[self.token_pointer].token_type == TokenType.OPENPARENTHESIS:
            parenthesis_stack.append(lexes[self.token_pointer].token_type)

            if_condition = lexes[self.token_pointer].match

            while parenthesis_stack:
                self.increment_token_pointer()
                if lexes[self.token_pointer].token_type == TokenType.OPENPARENTHESIS:
                    parenthesis_stack.append(lexes[self.token_pointer].token_type)
                if lexes[self.token_pointer].token_type == TokenType.CLOSINGPARENTHESIS:
                    parenthesis_stack.pop()

                if_condition += lexes[self.token_pointer].match

            if parenthesis_stack:
                self.handle_syntax_error(lexes[self.token_pointer], "parenthesis error")

            return if_condition
        else:
            self.handle_syntax_error(lexes[self.token_pointer], "invalid token should be ( instead of " + str(lexes[self.token_pointer].match))

    def parse_echo(self, lexes, statements):
        """ Parse Echo Statement
        Args:
            lexes: list of lexes
            statements: list of statements
        Returns:
            None
        """

        echoString = ""
        # ignore spaces
        self.increment_token_pointer()
        next_lex = lexes[self.token_pointer]

        with_parenthesis = False
        if next_lex.token_type == TokenType.OPENPARENTHESIS:
            self.increment_token_pointer()
            next_lex = lexes[self.token_pointer]
            with_parenthesis = True

        if next_lex.token_type == TokenType.STRING:
            echoString = next_lex.match

        if with_parenthesis:
            self.increment_token_pointer()
            next_lex = lexes[self.token_pointer]
            if next_lex.token_type == TokenType.CLOSINGPARENTHESIS:
                #self.increment_token_pointer()
                pass
            else:
                self.handle_syntax_error(next_lex, "Unclosed parenthesis in echo")

        echo_statement = Echo(echoString)
        statements.append(echo_statement)

    def parse_input(self, lexes, statements):
        """ Parse Input Statement
        Args:
            lexes: list of lexes
            statements: list of statements
        Returns:
            None
        """

        self.increment_token_pointer()
        next_lex = lexes[self.token_pointer]
        input_variable = ""
        if next_lex.token_type == TokenType.IDENTIFICATION:
            input_variable = next_lex.match
        else:
            self.handle_syntax_error(next_lex, "Invalid Input Function")

        input_statement = Input(input_variable)
        statements.append(input_statement)

    def parse_else(self, statements):
        """ Parse Else Statement
        Args:
            statements: list of statements
        Returns:
            None
        """

        else_statement = Else([])
        statements.append(else_statement)

    def parse_continue(self, statements):
        """ Parse Continue Statement
        Args:
            statements: list of statements
        Returns:
            None
        """

        continue_statement = Continue()
        statements.append(continue_statement)

    def parse_break(self, statements):
        """ Parse Break
        Args:
            statements: list of statements
        Returns:
            None
        """

        break_statement = Break()
        statements.append(break_statement)

    def parse_endwhile(self, statements):
        """ Parse End While
        Args:
            statements: list of statements
        Returns:
            None
        """

        endwhile = EndWhile()
        statements.append(endwhile)

    def parse_endfor(self, statements):
        """ Parse End for
        Args:
            statements: list of statements
        Returns:
            None
        """

        endfor = EndFor()
        statements.append(endfor)

    def parse_endif(self, statements):
        """ Parse End If
        Args:
            statements: list of statements
        Returns:
            None
        """

        endif = Fi()
        statements.append(endif)

    def handle_syntax_error(self, token: Token, message):
        """ Handles Syntax Errors
        Args:
            token: token that has caused the issue
            message: message
        Raises:
            SyntaxError
        """
        raise SyntaxError(f"Syntax Error at line {token.line_number} type: {token.token_type} match: {token.match}\n{message} ")