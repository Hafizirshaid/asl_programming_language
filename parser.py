
from statements.break_statement import Break
from statements.echo_statement import Echo
from statements.else_statement import Else
from statements.end_for_loop import EndFor
from statements.endif_statement import Fi
from statements.end_while_statement import EndWhile
from statements.for_loop_statement import For
from statements.if_statement import If
from statements.variable_statement import Variable
from statements.while_statement import While


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
            lex_type = lex['token_type']['type']

            if lex_type == 'echo':
                echoString = ""

                # ignore spaces
                next_lex = lexes[index + 1]
                while next_lex['token_type']['type'] == 'space':
                    index += 1
                    next_lex = lexes[index]
                if next_lex['token_type']['type'] == 'string':
                    echoString = next_lex['match'].group()
                    pass

                echo_statement = Echo(echoString)
                statements.append(echo_statement)

            if lex_type == 'call':
                pass

            if lex_type == 'method':
                pass

            if lex_type == 'if':
                # find if statement condition
                condition = ""
                next_lex = lexes[index + 1]
                while next_lex['token_type']['type'] != 'newline':
                    condition += next_lex['match'].group()
                    index += 1
                    next_lex = lexes[index]

                ifstatement = If(condition, [])
                statements.append(ifstatement)

            if lex_type == 'else':
                else_statement = Else([])
                statements.append(else_statement)
                pass

            if lex_type == 'fi':
                endif = Fi()
                statements.append(endif)

            if lex_type == 'endfor':
                endfor = EndFor()
                statements.append(endfor)
            if lex_type == 'endwhile':
                endwhile = EndWhile()
                statements.append(endwhile)
            if lex_type == 'break':
                break_statement = Break()
                statements.append(break_statement)
                pass

            if lex_type == 'cont':
                pass

            if lex_type == 'for':
                condition = ""
                next_lex = lexes[index + 1]
                while next_lex['token_type']['type'] != 'newline':
                    condition += next_lex['match'].group()
                    index += 1
                    next_lex = lexes[index]
                forloop = For(condition, [])
                statements.append(forloop)

            if lex_type == 'to':
                pass
            
            if lex_type == 'while':
                condition = ""
                next_lex = lexes[index + 1]
                while next_lex['token_type']['type'] != 'newline':
                    condition += next_lex['match'].group()
                    index += 1
                    next_lex = lexes[index]
                whileloop = While(condition, [])
                statements.append(whileloop)
                pass
            if lex_type == 'do':
                pass
            if lex_type == 'identification':

                identification = lexes[index]['match'].group()
                next_lex = lexes[index + 1]

                while next_lex['token_type']['type'] != 'newline':
                    identification += next_lex['match'].group()
                    index += 1
                    next_lex = lexes[index]
                variablestatement = Variable(identification)
                statements.append(variablestatement)

            if lex_type == 'string':
                pass
            if lex_type == 'number':
                pass
            if lex_type == 'equivalent':
                pass
            if lex_type == 'equal':
                pass
            if lex_type == 'notequivalent':
                pass
            if lex_type == 'graterthan':
                pass
            if lex_type == 'lessthan':
                pass
            if lex_type == 'graterthanorequal':
                pass
            if lex_type == 'lessthanorequal':
                pass
            if lex_type == 'add':
                pass
            if lex_type == 'sub':
                pass
            if lex_type == 'mult':
                pass
            if lex_type == 'div':
                pass
            if lex_type == 'mod':
                pass
            if lex_type == 'and':
                pass
            if lex_type == 'false':
                pass
            if lex_type == 'newline':
                pass
            if lex_type == 'space':
                pass
            if lex_type == 'openparanthesis':
                pass
            if lex_type == 'closingparanthesis':
                pass
            if lex_type == 'comment':
                pass

            index += 1

        return statements
