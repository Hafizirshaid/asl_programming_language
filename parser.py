# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.
"""
Parser Library

"""
from lexer import TokenType
from statements.statement import *

class Parser:
    """

    Parser Class

    """

    def __init__(self) -> None:
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

            if lex_type == TokenType.ECHO:
                echoString = ""

                # ignore spaces
                next_lex = lexes[index + 1]
                while next_lex.token_type == TokenType.SPACE:
                    index += 1
                    next_lex = lexes[index]
                if next_lex.token_type == TokenType.STRING:
                    echoString = next_lex.match
                    pass

                echo_statement = Echo(echoString)
                statements.append(echo_statement)

            if lex_type == TokenType.CALL:
                pass

            if lex_type == TokenType.METHOD:
                pass

            if lex_type == TokenType.IF:
                # find if statement condition
                condition = ""
                next_lex = lexes[index + 1]
                index += 1
                while next_lex.token_type != TokenType.NEWLINE:
                    condition += next_lex.match
                    index += 1
                    next_lex = lexes[index]

                ifstatement = If(condition, [])
                statements.append(ifstatement)

            if lex_type == TokenType.ELSE:
                else_statement = Else([])
                statements.append(else_statement)
                pass
            if lex_type == TokenType.ELIF:
                condition = ""
                next_lex = lexes[index + 1]
                index += 1
                while next_lex.token_type != TokenType.NEWLINE:
                    condition += next_lex.match
                    index += 1
                    next_lex = lexes[index]
                elif_Statement = ElseIf(condition, [])
                statements.append(elif_Statement)
                pass
            if lex_type == TokenType.FI:
                endif = Fi()
                statements.append(endif)

            if lex_type == TokenType.ENDFOR:
                endfor = EndFor()
                statements.append(endfor)
            if lex_type == TokenType.ENDWHILE:
                endwhile = EndWhile()
                statements.append(endwhile)
            if lex_type == TokenType.BREAK:
                break_statement = Break()
                statements.append(break_statement)
                pass

            if lex_type == TokenType.CONT:
                pass

            if lex_type == TokenType.FOR:
                condition = ""
                next_lex = lexes[index + 1]
                index += 1
                while next_lex.token_type != TokenType.NEWLINE:
                    condition += next_lex.match
                    index += 1
                    next_lex = lexes[index]
                forloop = For(condition, [])
                # append variable statement for for loop variable
                # for_loop_variable = Variable(forloop.loop_initial_variable)
                # statements.append(for_loop_variable)
                statements.append(forloop)

            if lex_type == TokenType.TO:
                pass

            if lex_type == TokenType.WHILE:
                condition = ""
                next_lex = lexes[index + 1]
                index += 1
                while next_lex.token_type != TokenType.NEWLINE:
                    condition += next_lex.match
                    index += 1
                    next_lex = lexes[index]
                whileloop = While(condition, [])
                statements.append(whileloop)
                pass
            if lex_type == TokenType.DO:
                pass

            if lex_type == TokenType.IDENTIFICATION:

                identification = lexes[index].match

                index += 1
                next_lex = lexes[index]
                while next_lex.token_type != TokenType.NEWLINE:
                    identification += next_lex.match
                    index += 1
                    next_lex = lexes[index]
                variablestatement = Variable(identification)
                statements.append(variablestatement)

            if lex_type == TokenType.STRING:
                pass
            if lex_type == TokenType.NUMBER:
                pass
            if lex_type == TokenType.EQUIVALENT:
                pass
            if lex_type == TokenType.EQUAL:
                pass
            if lex_type == TokenType.NOTEQUIVALENT:
                pass
            if lex_type == TokenType.GRATERTHAN:
                pass
            if lex_type == TokenType.LESSTHAN:
                pass
            if lex_type == TokenType.GRATERTHANOREQUAL:
                pass
            if lex_type == TokenType.LESSTHANOREQUAL:
                pass
            if lex_type == TokenType.ADD:
                pass
            if lex_type == TokenType.SUB:
                pass
            if lex_type == TokenType.MULT:
                pass
            if lex_type == TokenType.DIV:
                pass
            if lex_type == TokenType.MOD:
                pass
            if lex_type == TokenType.AND:
                pass
            if lex_type == TokenType.FALSE:
                pass
            if lex_type == TokenType.NEWLINE:
                pass
            if lex_type == TokenType.SPACE:
                pass
            if lex_type == TokenType.OPENPARANTHESIS:
                pass
            if lex_type == TokenType.CLOSINGPARANTHESIS:
                pass
            if lex_type == TokenType.COMMENT:
                pass

            index += 1

        return statements
