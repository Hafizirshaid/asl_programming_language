# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

"""

Parser Library

Convert list of tokens into statements and extract thier attributes
Example:
Code:

-----------------------
x = 10

for "i=0;i<10;i=i+1"
    if "i==0"
        echo "stmt says i is 0"
    elif "i==1"
        echo "stmt says i is 1"
    elif "i==2"
        echo "stmt says i is 2"
    elif "i==3"
        echo "stmt says i is 3"
    elif "i==4"
        echo "stmt says i is 4"
    elif "i==5"
        echo "stmt says i is 5"
    else
        echo "not checked i is {i}"
    fi
endfor
-----------------------

List of statements:
----------------------
Variable: x=10
For Loop: i=0;i<10;i=i+1
If statement: "i==0"
Echo Statement: "stmt says i is 0"
Else If Statement
Echo Statement: "stmt says i is 1"
Else If Statement
Echo Statement: "stmt says i is 2"
Else If Statement
Echo Statement: "stmt says i is 3"
Else If Statement
Echo Statement: "stmt says i is 4"
Else If Statement
Echo Statement: "stmt says i is 5"
Else Statement
Echo Statement: "not checked i is {i}"
End If
End For Loop

"""

from lexer import TokenType
from statements import statement
from statements.statement import *


class Parser:
    """

    Parser Class

    Contains methods to convert list of tokens into list of statements that can be
    executed

    """

    def __init__(self) -> None:
        """ Parser Class Constructor """
        self.token_pointer = 0
        pass

    def increment_token_pointer(self):
        self.token_pointer += 1

    def parse(self, lexes: list) -> list:
        """ Parse list of lexes
        Args:
            lexes: list of lexes

        Returns:
            list of statements
        """

        statements = []
        # index = 0
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
                raise SyntaxError("Invalid token " + str(lex_type))

            # Increment Index to get next token
            self.increment_token_pointer()

        return statements

    def parse_variable(self, lexes, statements):
        """ Parse variable
        Args:
            lexes: list of lexes
            statements: list of statements
        Returns:
            None
        """
        identification = lexes[self.token_pointer].match
        # index += 1

        self.increment_token_pointer()
        next_lex = lexes[self.token_pointer]
        while next_lex.token_type != TokenType.NEWLINE:
            identification += next_lex.match
            # index += 1
            self.increment_token_pointer()
            next_lex = lexes[self.token_pointer]
        variablestatement = Variable(identification)
        statements.append(variablestatement)

    def parse_while(self, lexes, statements):
        """ Parse While
        Args:
            lexes: list of lexes
            statements: list of statements
        Returns:
            None
        """

        condition = self._get_condition(lexes)
        statements.append(While(condition, []))

    def parse_for(self, lexes, statements):
        """ Parse For
        Args:
            lexes: list of lexes
            statements: list of statements
        Returns:
            None
        """

        condition = self._get_condition(lexes)
        forloop = For(condition, [])
        statements.append(forloop)

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

    def parse_elseif(self, lexes, statements):
        """ Parse Else If
        Args:
            lexes: list of lexes
            statements: list of statements
        Returns:
            None
        """

        condition = self._get_condition(lexes)
        elif_Statement = ElseIf(condition, [])
        statements.append(elif_Statement)

    def parse_else(self, statements):
        """ Parse Else Statement
        Args:
            statements: list of statements
        Returns:
            None
        """

        else_statement = Else([])
        statements.append(else_statement)

    def parse_if(self, lexes, statements):
        """ Parse If Statement
        Args:
            lexes: list of lexes
            statements: list of statements
        Returns:
            None
        """

        condition = self._get_condition(lexes)
        if_statement = If(condition, [])
        statements.append(if_statement)

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
            raise SyntaxError("Invalid Input Function" +  str(next_lex.TokenType ))
        input_statement = Input(input_variable)
        statements.append(input_statement)

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

        with_paranthesis = False
        if next_lex.token_type == TokenType.OPENPARANTHESIS:
            self.increment_token_pointer()
            next_lex = lexes[self.token_pointer]
            with_paranthesis = True

        if next_lex.token_type == TokenType.STRING:
            echoString = next_lex.match

        if with_paranthesis:
            self.increment_token_pointer()
            next_lex = lexes[self.token_pointer]
            if next_lex.token_type == TokenType.CLOSINGPARANTHESIS:
                #self.increment_token_pointer()
                pass
            else:
                raise SyntaxError("Unclosed paranthesis in echo")

        echo_statement = Echo(echoString)
        statements.append(echo_statement)

    def _get_condition(self, lexes) -> str:
        """ This method extracts tokens as condtions, it stops when it found
            new line, usually used for statements that ends in a new line mark
            Example:
                While "x >= 10"

            it returns "x >= 10"

        Args:
            lexes: tokens list
            index: current index
        Returns:
            Condition string
        """

        condition = ""
        self.increment_token_pointer()
        next_lex = lexes[self.token_pointer]
        #index += 1

        while next_lex.token_type != TokenType.NEWLINE:
            condition += next_lex.match
            # index += 1
            self.increment_token_pointer()
            next_lex = lexes[self.token_pointer]
        return condition
