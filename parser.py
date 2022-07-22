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
from statements.statement import *


class Parser:
    """

    Parser Class

    Contains methods to convert list of tokens into list of statements that can be
    executed

    """

    def __init__(self) -> None:
        """ Parser Class Constructor """
        pass

    def parse(self, lexes: list) -> list:
        """ Parse list of lexes
        Args:
            lexes: list of lexes

        Returns:
            list of statements
        """

        statements = []
        index = 0

        while index <= len(lexes) - 1:

            lex = lexes[index]
            lex_type = lex.token_type

            if lex_type == TokenType.ECHO or lex_type == TokenType.PRINT:
                echoString = ""
                # ignore spaces
                next_lex = lexes[index + 1]
                while next_lex.token_type == TokenType.SPACE:
                    index += 1
                    next_lex = lexes[index]
                if next_lex.token_type == TokenType.STRING:
                    echoString = next_lex.match

                echo_statement = Echo(echoString)
                statements.append(echo_statement)

            elif lex_type == TokenType.IF:
                condition = self._get_condition(lexes, index)
                if_statement = If(condition, [])
                statements.append(if_statement)

            elif lex_type == TokenType.ELSE:
                else_statement = Else([])
                statements.append(else_statement)

            elif lex_type == TokenType.ELIF:
                condition = self._get_condition(lexes, index)
                elif_Statement = ElseIf(condition, [])
                statements.append(elif_Statement)

            elif lex_type == TokenType.FI:
                endif = Fi()
                statements.append(endif)

            elif lex_type == TokenType.ENDFOR:
                endfor = EndFor()
                statements.append(endfor)

            elif lex_type == TokenType.ENDWHILE:
                endwhile = EndWhile()
                statements.append(endwhile)

            elif lex_type == TokenType.BREAK:
                break_statement = Break()
                statements.append(break_statement)

            elif lex_type == TokenType.CONTINUE:
                continue_statement = Continue()
                statements.append(continue_statement)

            elif lex_type == TokenType.FOR:
                condition = self._get_condition(lexes, index)
                forloop = For(condition, [])
                statements.append(forloop)

            elif lex_type == TokenType.WHILE:
                condition = self._get_condition(lexes, index)
                statements.append(While(condition, []))

            elif lex_type == TokenType.IDENTIFICATION:
                identification = lexes[index].match
                index += 1
                next_lex = lexes[index]
                while next_lex.token_type != TokenType.NEWLINE:
                    identification += next_lex.match
                    index += 1
                    next_lex = lexes[index]
                variablestatement = Variable(identification)
                statements.append(variablestatement)

            # Increment Index to get next token
            index += 1

            # Below token types are not needed at this moment, for future use only
            # elif lex_type == TokenType.TO:
            #     pass
            # elif lex_type == TokenType.DO:
            #     pass
            # elif lex_type == TokenType.CALL:
            #     pass
            # elif lex_type == TokenType.METHOD:
            #     pass
            # elif lex_type == TokenType.STRING:
            #     pass
            # elif lex_type == TokenType.NUMBER:
            #     pass
            # elif lex_type == TokenType.EQUIVALENT:
            #     pass
            # elif lex_type == TokenType.EQUAL:
            #     pass
            # elif lex_type == TokenType.NOTEQUIVALENT:
            #     pass
            # elif lex_type == TokenType.GRATERTHAN:
            #     pass
            # elif lex_type == TokenType.LESSTHAN:
            #     pass
            # elif lex_type == TokenType.GRATERTHANOREQUAL:
            #     pass
            # elif lex_type == TokenType.LESSTHANOREQUAL:
            #     pass
            # elif lex_type == TokenType.ADD:
            #     pass
            # elif lex_type == TokenType.SUB:
            #     pass
            # elif lex_type == TokenType.MULT:
            #     pass
            # elif lex_type == TokenType.DIV:
            #     pass
            # elif lex_type == TokenType.MOD:
            #     pass
            # elif lex_type == TokenType.AND:
            #     pass
            # elif lex_type == TokenType.FALSE:
            #     pass
            # elif lex_type == TokenType.NEWLINE:
            #     pass
            # elif lex_type == TokenType.SPACE:
            #     pass
            # elif lex_type == TokenType.OPENPARANTHESIS:
            #     pass
            # elif lex_type == TokenType.CLOSINGPARANTHESIS:
            #     pass
            # elif lex_type == TokenType.COMMENT:
            #     pass


        return statements

    def _get_condition(self, lexes, index) -> str:
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
        next_lex = lexes[index + 1]
        index += 1
        while next_lex.token_type != TokenType.NEWLINE:
            condition += next_lex.match
            index += 1
            next_lex = lexes[index]
        return condition
