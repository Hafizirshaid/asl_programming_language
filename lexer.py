# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

"""

Lexer Library

Converts code texts into meaningful lexems to tokens:

Example:
-------------------------------
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
----------------------------

List of tokens:
-------------------
Token(TokenType.IDENTIFICATION, 'x', 1),
Token(TokenType.EQUAL, '=', 1),
Token(TokenType.NUMBER, '10', 1),
Token(TokenType.NEWLINE, '', 1),
Token(TokenType.NEWLINE, '', 2),
Token(TokenType.FOR, 'for', 3),
Token(TokenType.STRING, '"i=0;i<10;i=i+1"', 3),
Token(TokenType.NEWLINE, '', 3),
Token(TokenType.IF, 'if', 4),
Token(TokenType.STRING, '"i==0"', 4),
Token(TokenType.NEWLINE, '', 4),
Token(TokenType.ECHO, 'echo', 5),
Token(TokenType.STRING, '"stmt says i is 0"', 5),
Token(TokenType.NEWLINE, '', 5),
Token(TokenType.ELIF, 'elif', 6),
Token(TokenType.STRING, '"i==1"', 6),
Token(TokenType.NEWLINE, '', 6),
Token(TokenType.ECHO, 'echo', 7),
Token(TokenType.STRING, '"stmt says i is 1"', 7),
Token(TokenType.NEWLINE, '', 7),
Token(TokenType.ELIF, 'elif', 8),
Token(TokenType.STRING, '"i==2"', 8),
Token(TokenType.NEWLINE, '', 8),
Token(TokenType.ECHO, 'echo', 9),
Token(TokenType.STRING, '"stmt says i is 2"', 9),
Token(TokenType.NEWLINE, '', 9),
Token(TokenType.ELIF, 'elif', 10),
Token(TokenType.STRING, '"i==3"', 10),
Token(TokenType.NEWLINE, '', 10),
Token(TokenType.ECHO, 'echo', 11),
Token(TokenType.STRING, '"stmt says i is 3"', 11),
Token(TokenType.NEWLINE, '', 11),
Token(TokenType.ELIF, 'elif', 12),
Token(TokenType.STRING, '"i==4"', 12),
Token(TokenType.NEWLINE, '', 12),
Token(TokenType.ECHO, 'echo', 13),
Token(TokenType.STRING, '"stmt says i is 4"', 13),
Token(TokenType.NEWLINE, '', 13),
Token(TokenType.ELIF, 'elif', 14),
Token(TokenType.STRING, '"i==5"', 14),
Token(TokenType.NEWLINE, '', 14),
Token(TokenType.ECHO, 'echo', 15),
Token(TokenType.STRING, '"stmt says i is 5"', 15),
Token(TokenType.NEWLINE, '', 15),
Token(TokenType.ELSE, 'else', 16),
Token(TokenType.NEWLINE, '', 16),
Token(TokenType.ECHO, 'echo', 17),
Token(TokenType.STRING, '"not checked i is {i}"', 17),
Token(TokenType.NEWLINE, '', 17),
Token(TokenType.FI, 'fi', 18),
Token(TokenType.NEWLINE, '', 18),
Token(TokenType.ENDFOR, 'endfor', 19)
-------------------

"""

from enum import Enum
import re

from exceptions.language_exception import SyntaxError


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
    CONTINUE = 11
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
    PRINT = 48
    LEFTBRAKET = 49
    RIGHTBRAKET = 50


class Token:
    """ Token Class

    Holds information about a token

    Class Variables:
        token_type: the type of the token
        match: token value
        line_number: line number
    """

    def __init__(self, token_type: TokenType, match: str, line_number: int) -> None:
        """ Token Constructor
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

    def __str__(self) -> str:
        return f"{self.line_number} {self.token_type} {self.match}"

class Lexer(object):
    """ Lexer Class

    Contains method tokenize_text() that converts source file text into meaningful
    tokens

    Class Attributes:
        regex_list: A list that contains token types and thier regular expressions

    """

    def __init__(self) -> None:
        """ init Lexer Class """

        # this list contains all regular expressions that are recognized by
        # the programming language.
        self.regex_list = [
            {'type': TokenType.COMMENT, 'regex': '(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)'},
            {'type': TokenType.CALL, 'regex': '^call'},
            {'type': TokenType.METHOD, 'regex': '^method'},
            {'type': TokenType.ELIF, 'regex': '^elif'},
            {'type': TokenType.IF, 'regex': '^if'},
            {'type': TokenType.ELSE, 'regex': '^else'},
            {'type': TokenType.FI, 'regex': '^fi'},
            {'type': TokenType.ENDFOR, 'regex': '^endfor'},
            {'type': TokenType.ENDWHILE, 'regex': '^endwhile'},
            {'type': TokenType.BREAK, 'regex': '^break'},
            {'type': TokenType.CONTINUE, 'regex': '^continue'},
            {'type': TokenType.FOR, 'regex': '^for'},
            {'type': TokenType.TO, 'regex': '^to'},
            {'type': TokenType.INCR, 'regex': '^incr'},
            {'type': TokenType.WHILE, 'regex': '^while'},
            {'type': TokenType.DO, 'regex': '^do'},
            {'type': TokenType.ECHO, 'regex': '^echo'},
            {'type': TokenType.PRINT, 'regex': '^print'},
            {'type': TokenType.INPUT, 'regex': '^input'},
            #{'type': TokenType.CONDITION, 'regex': "\(([^)]+)\)"},
            {'type': TokenType.IDENTIFICATIONBETWEENBRSCKETS, 'regex': "\{.*?\}"},
            {'type': TokenType.IDENTIFICATION, 'regex': '^[a-zA-Z_$][a-zA-Z_$0-9]*'},
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
            {'type': TokenType.LEFTBRAKET, 'regex': '^}'},
            {'type': TokenType.RIGHTBRAKET, 'regex': '^{'},
            {'type': TokenType.SEMICOLON, 'regex': "^;"},
            {'type': TokenType.TRUE, 'regex': '^true'},
            {'type': TokenType.FALSE, 'regex': '^false'},
            {'type': TokenType.NEWLINE, 'regex': '^\n'},
            {'type': TokenType.SPACE, 'regex': '\s'},
            {'type': TokenType.OPENPARANTHESIS, 'regex': '^\('},
            {'type': TokenType.CLOSINGPARANTHESIS, 'regex': '^\)'}
        ]

    def tokenize_text(self, text: str, keep_unknown=False, keep_spaces=False) -> list:
        """ Tokenize source file text
        Args:
            text: text file string
            keep_unknown: weather to keep an unknown token or not, a token that
                          doesn't have a type in regex_list
            keep_spaces: weather white spaces should be added to list of tokens or not

        Returns:
            list of meaningful tokens
        """

        tokens = []
        line_number = 1

        while text:

            token_type = None
            match = None

            # Find a matching token in regex_list
            for regex in self.regex_list:
                current_match = re.match(regex['regex'], text)
                if current_match:
                    # match found
                    token_type = regex
                    match = current_match
                    break

            if match:

                # New Token Found, remove token from text.
                text = text.removeprefix(match.group())

                if keep_spaces and token_type['type'] == TokenType.SPACE:
                    # add white space token to list
                    token = Token(token_type['type'], match.group(), line_number)
                    tokens.append(token)

                if token_type['type'] != TokenType.SPACE:

                    token_value = match.group().strip()
                    token = Token(token_type['type'], token_value, line_number)
                    tokens.append(token)

                # Increase line number when finding new line.
                if token_type['type'] == TokenType.NEWLINE:
                    line_number += 1
            else:

                # Unrecognized token found
                if keep_unknown:
                    token = Token(TokenType.UNKNOWN, text[0], line_number)
                    tokens.append(token)
                    # Remove first unknown char from the text string.
                    text = text[1:]
                else:
                    # Exception, unrecognized token, raise syntax error
                    raise SyntaxError(f"Syntax Error at line {line_number} \n {text}")

        return tokens
