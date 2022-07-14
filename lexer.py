# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

"""
Lexer Library
"""

__version__ = '1.1'
__all__ = ['Lexer']


from enum import Enum
import re

from exceptions.syntax_error_exception import SyntaxError


class TokenType(Enum):
    """ Enum Representing Token type """
    COMMENT = 1
    CALL = 2
    METHOD = 3
    ELIF = 4
    IF = 5
    ELSE = 6
    FI = 7
    ENDFOR = 8
    ENDWHILE = 9
    BREAK = 10
    CONT = 11
    FOR = 12
    TO = 13
    INCR = 14
    WHILE = 15
    DO = 16
    ECHO = 17
    IDENTIFICATION = 18
    STRING = 19
    NUMBER = 20
    EQUIVALENT = 21
    EQUAL = 22
    NOTEQUIVALENT = 23
    GRATERTHANOREQUAL = 24
    LESSTHANOREQUAL = 25
    GRATERTHAN = 26
    LESSTHAN = 27
    ADD = 28
    SUB = 29
    MULT = 30
    DIV = 31
    MOD = 32
    AND = 33
    OR = 34
    NOT = 35
    TRUE = 36
    FALSE = 37
    NEWLINE = 38
    SPACE = 39
    OPENPARANTHESIS = 40
    CLOSINGPARANTHESIS = 41
    INPUT = 42
    REAL = 43
    IDENTIFICATIONBETWEENBRSCKETS = 44
    UNKNOWN = 45
    CONDITION = 46
    SEMICOLON = 47


class Token:
    """ Token Class """

    def __init__(self, token_type: TokenType, match: str, line_number: int) -> None:
        """Init Token
        Args:
            token_type: type of token
            match: the match string
            line_number: line number
        """
        self.token_type = token_type
        self.match = match
        self.line_number = line_number

    def __repr__(self) -> str:
        return f"{self.line_number} {self.token_type} {self.match}"


class Lexer(object):
    """ Lexer Class """

    def __init__(self) -> None:
        """ init Lexer Class """

        # this list contains all regular expressions that are recognized by
        # the programming language.
        self.regex_list = [
            {'type': TokenType.COMMENT,
                'regex': '(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)'},
            {'type': TokenType.CALL, 'regex': '^call'},
            {'type': TokenType.METHOD, 'regex': '^method'},
            {'type': TokenType.ELIF, 'regex': '^elif'},
            {'type': TokenType.IF, 'regex': '^if'},
            {'type': TokenType.ELSE, 'regex': '^else'},
            {'type': TokenType.FI, 'regex': '^fi'},
            {'type': TokenType.ENDFOR, 'regex': '^endfor'},
            {'type': TokenType.ENDWHILE, 'regex': '^endwhile'},
            {'type': TokenType.BREAK, 'regex': '^break'},
            {'type': TokenType.CONT, 'regex': '^cont'},
            {'type': TokenType.FOR, 'regex': '^for'},
            {'type': TokenType.TO, 'regex': '^to'},
            {'type': TokenType.INCR, 'regex': '^incr'},
            {'type': TokenType.WHILE, 'regex': '^while'},
            {'type': TokenType.DO, 'regex': '^do'},
            {'type': TokenType.ECHO, 'regex': '^echo'},
            {'type': TokenType.INPUT, 'regex': '^input'},
            #{'type': TokenType.CONDITION, 'regex': "\(([^)]+)\)"},
            {'type': TokenType.IDENTIFICATIONBETWEENBRSCKETS, 'regex': "\{.*?\}"},
            {'type': TokenType.IDENTIFICATION,
                'regex': '^[a-zA-Z_$][a-zA-Z_$0-9]*'},
            {'type': TokenType.STRING, 'regex': '^"[^"]*"'},
            {'type': TokenType.REAL, 'regex': '[0-9]+\.[0-9]*'},
            {'type': TokenType.NUMBER, 'regex': '^\d+'},
            {'type': TokenType.EQUIVALENT, 'regex': '^=='},
            {'type': TokenType.EQUAL, 'regex': '^='},
            {'type': TokenType.NOTEQUIVALENT, 'regex': '^!='},
            {'type': TokenType.GRATERTHANOREQUAL, 'regex': '^>='},
            {'type': TokenType.LESSTHANOREQUAL, 'regex': '^<='},
            {'type': TokenType.GRATERTHAN, 'regex': '^>'},
            {'type': TokenType.LESSTHAN, 'regex': '^<'},
            {'type': TokenType.ADD, 'regex': '^\+'},
            {'type': TokenType.SUB, 'regex': '^\-'},
            {'type': TokenType.MULT, 'regex': '^\*'},
            {'type': TokenType.DIV, 'regex': '^\/'},
            {'type': TokenType.MOD, 'regex': '^\%'},
            {'type': TokenType.AND, 'regex': '^&'},
            {'type': TokenType.OR, 'regex': '^\|'},
            {'type': TokenType.NOT, 'regex': '^!'},
            {'type': TokenType.SEMICOLON, 'regex': "^;"},
            {'type': TokenType.TRUE, 'regex': '^true'},
            {'type': TokenType.FALSE, 'regex': '^false'},
            {'type': TokenType.NEWLINE, 'regex': '^\n'},
            {'type': TokenType.SPACE, 'regex': '\s'},
            {'type': TokenType.OPENPARANTHESIS, 'regex': '^\('},
            {'type': TokenType.CLOSINGPARANTHESIS, 'regex': '^\)'}
        ]

    def tokenize(self, text: str, keep_unknown=False, keep_spaces=False) -> list:
        """ Tokenize source file text
        Args:
            text: text file string
            keep_unknown:
            keep_spaces:

        Returns:
            list of tokens
        """

        tokens = []
        line_number = 1

        while text:

            token_type = None
            match = None

            # Find Matching token in regex_list
            for regex in self.regex_list:
                current_match = re.match(regex['regex'], text)
                if current_match:
                    # match found
                    token_type = regex
                    match = current_match
                    break
                pass

            if match:

                # New Token Found, remove token from text.
                text = text.removeprefix(match.group())

                if keep_spaces and token_type['type'] == TokenType.SPACE:
                    token = Token(token_type['type'],
                                  match.group(), line_number)
                    tokens.append(token)

                if token_type['type'] != TokenType.SPACE:
                    token = Token(token_type['type'],
                                  match.group(), line_number)
                    tokens.append(token)

                # Increase line number when finding new line.
                if token_type['type'] == TokenType.NEWLINE:
                    line_number += 1
            else:
                if keep_unknown:
                    token = Token(TokenType.UNKNOWN, text[0], line_number)
                    tokens.append(token)
                    text = text[1:]
                    pass
                else:
                    # Exception, unrecognized char, syntax error
                    raise SyntaxError(
                        f"Syntax Error at line {line_number} \n {text}")

        return tokens
