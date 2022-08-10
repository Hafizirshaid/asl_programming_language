# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

"""

Lexer Library

Converts code texts into meaningful lexemes to tokens:

Example:
-------------------------------
echo "Calculate Grades rank between 0 to 100"

for (grade = 0; grade <= 100; grade = grade + 1)

    if ((grade >= 90) & (grade <= 100))
        echo "{grade} Outstanding"
    elif ((grade >= 80) & (grade <= 90))
        echo "{grade} very good"
    elif ((grade >= 70) & (grade <= 80))
        echo "{grade} good"
    elif ((grade >= 60) & (grade <= 70))
        echo "{grade} fair"
    elif ((grade >= 0) & (grade <= 60))
        echo "{grade} failure"
    else
        echo "Invalid Grade"
    fi

endfor
----------------------------

List of tokens:
-------------------
Token(TokenType.ECHO, 'echo', 1),
Token(TokenType.STRING, '"Calculate Grades rank between 0 to 100"', 1),
Token(TokenType.NEWLINE, '', 1),
Token(TokenType.NEWLINE, '', 2),
Token(TokenType.FOR, 'for', 3),
Token(TokenType.OPENPARANTHESIS, '(', 3),
Token(TokenType.IDENTIFICATION, 'grade', 3),
Token(TokenType.EQUAL, '=', 3),
Token(TokenType.NUMBER, '0', 3),
Token(TokenType.SEMICOLON, ';', 3),
Token(TokenType.IDENTIFICATION, 'grade', 3),
Token(TokenType.LESSTHANOREQUAL, '<=', 3),
Token(TokenType.NUMBER, '100', 3),
Token(TokenType.SEMICOLON, ';', 3),
Token(TokenType.IDENTIFICATION, 'grade', 3),
Token(TokenType.EQUAL, '=', 3),
Token(TokenType.IDENTIFICATION, 'grade', 3),
Token(TokenType.ADD, '+', 3),
Token(TokenType.NUMBER, '1', 3),
Token(TokenType.CLOSINGPARANTHESIS, ')', 3),
Token(TokenType.NEWLINE, '', 3),
Token(TokenType.NEWLINE, '', 4),
Token(TokenType.IF, 'if', 5),
Token(TokenType.OPENPARANTHESIS, '(', 5),
Token(TokenType.OPENPARANTHESIS, '(', 5),
Token(TokenType.IDENTIFICATION, 'grade', 5),
Token(TokenType.GRATERTHANOREQUAL, '>=', 5),
Token(TokenType.NUMBER, '90', 5),
Token(TokenType.CLOSINGPARANTHESIS, ')', 5),
Token(TokenType.AND, '&', 5),
Token(TokenType.OPENPARANTHESIS, '(', 5),
Token(TokenType.IDENTIFICATION, 'grade', 5),
Token(TokenType.LESSTHANOREQUAL, '<=', 5),
Token(TokenType.NUMBER, '100', 5),
Token(TokenType.CLOSINGPARANTHESIS, ')', 5),
Token(TokenType.CLOSINGPARANTHESIS, ')', 5),
Token(TokenType.NEWLINE, '', 5),
Token(TokenType.ECHO, 'echo', 6),
Token(TokenType.STRING, '"{grade} Outstanding"', 6),
Token(TokenType.NEWLINE, '', 6),
Token(TokenType.ELIF, 'elif', 7),
Token(TokenType.OPENPARANTHESIS, '(', 7),
Token(TokenType.OPENPARANTHESIS, '(', 7),
Token(TokenType.IDENTIFICATION, 'grade', 7),
Token(TokenType.GRATERTHANOREQUAL, '>=', 7),
Token(TokenType.NUMBER, '80', 7),
Token(TokenType.CLOSINGPARANTHESIS, ')', 7),
Token(TokenType.AND, '&', 7),
Token(TokenType.OPENPARANTHESIS, '(', 7),
Token(TokenType.IDENTIFICATION, 'grade', 7),
Token(TokenType.LESSTHANOREQUAL, '<=', 7),
Token(TokenType.NUMBER, '90', 7),
Token(TokenType.CLOSINGPARANTHESIS, ')', 7),
Token(TokenType.CLOSINGPARANTHESIS, ')', 7),
Token(TokenType.NEWLINE, '', 7),
Token(TokenType.ECHO, 'echo', 8),
Token(TokenType.STRING, '"{grade} very good"', 8),
Token(TokenType.NEWLINE, '', 8),
Token(TokenType.ELIF, 'elif', 9),
Token(TokenType.OPENPARANTHESIS, '(', 9),
Token(TokenType.OPENPARANTHESIS, '(', 9),
Token(TokenType.IDENTIFICATION, 'grade', 9),
Token(TokenType.GRATERTHANOREQUAL, '>=', 9),
Token(TokenType.NUMBER, '70', 9),
Token(TokenType.CLOSINGPARANTHESIS, ')', 9),
Token(TokenType.AND, '&', 9),
Token(TokenType.OPENPARANTHESIS, '(', 9),
Token(TokenType.IDENTIFICATION, 'grade', 9),
Token(TokenType.LESSTHANOREQUAL, '<=', 9),
Token(TokenType.NUMBER, '80', 9),
Token(TokenType.CLOSINGPARANTHESIS, ')', 9),
Token(TokenType.CLOSINGPARANTHESIS, ')', 9),
Token(TokenType.NEWLINE, '', 9),
Token(TokenType.ECHO, 'echo', 10),
Token(TokenType.STRING, '"{grade} good"', 10),
Token(TokenType.NEWLINE, '', 10),
Token(TokenType.ELIF, 'elif', 11),
Token(TokenType.OPENPARANTHESIS, '(', 11),
Token(TokenType.OPENPARANTHESIS, '(', 11),
Token(TokenType.IDENTIFICATION, 'grade', 11),
Token(TokenType.GRATERTHANOREQUAL, '>=', 11),
Token(TokenType.NUMBER, '60', 11),
Token(TokenType.CLOSINGPARANTHESIS, ')', 11),
Token(TokenType.AND, '&', 11),
Token(TokenType.OPENPARANTHESIS, '(', 11),
Token(TokenType.IDENTIFICATION, 'grade', 11),
Token(TokenType.LESSTHANOREQUAL, '<=', 11),
Token(TokenType.NUMBER, '70', 11),
Token(TokenType.CLOSINGPARANTHESIS, ')', 11),
Token(TokenType.CLOSINGPARANTHESIS, ')', 11),
Token(TokenType.NEWLINE, '', 11),
Token(TokenType.ECHO, 'echo', 12),
Token(TokenType.STRING, '"{grade} fair"', 12),
Token(TokenType.NEWLINE, '', 12),
Token(TokenType.ELIF, 'elif', 13),
Token(TokenType.OPENPARANTHESIS, '(', 13),
Token(TokenType.OPENPARANTHESIS, '(', 13),
Token(TokenType.IDENTIFICATION, 'grade', 13),
Token(TokenType.GRATERTHANOREQUAL, '>=', 13),
Token(TokenType.NUMBER, '0', 13),
Token(TokenType.CLOSINGPARANTHESIS, ')', 13),
Token(TokenType.AND, '&', 13),
Token(TokenType.OPENPARANTHESIS, '(', 13),
Token(TokenType.IDENTIFICATION, 'grade', 13),
Token(TokenType.LESSTHANOREQUAL, '<=', 13),
Token(TokenType.NUMBER, '60', 13),
Token(TokenType.CLOSINGPARANTHESIS, ')', 13),
Token(TokenType.CLOSINGPARANTHESIS, ')', 13),
Token(TokenType.NEWLINE, '', 13),
Token(TokenType.ECHO, 'echo', 14),
Token(TokenType.STRING, '"{grade} failure"', 14),
Token(TokenType.NEWLINE, '', 14),
Token(TokenType.ELSE, 'else', 15),
Token(TokenType.NEWLINE, '', 15),
Token(TokenType.ECHO, 'echo', 16),
Token(TokenType.STRING, '"Invalid Grade"', 16),
Token(TokenType.NEWLINE, '', 16),
Token(TokenType.FI, 'fi', 17),
Token(TokenType.NEWLINE, '', 17),
Token(TokenType.NEWLINE, '', 18),
Token(TokenType.ENDFOR, 'endfor', 19),
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
    GREATERTHANOREQUAL = 24
    LESSTHANOREQUAL = 25
    GREATERTHAN = 26
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
    OPENPARENTHESIS = 40
    CLOSINGPARENTHESIS = 41
    INPUT = 42
    REAL = 43
    IDENTIFICATIONBETWEENBRSCKETS = 44
    UNKNOWN = 45
    CONDITION = 46
    SEMICOLON = 47
    PRINT = 48
    LEFTBRACKET = 49
    RIGHTBRAKET = 50
    COMMA = 51
    ENDMETHOD = 52
    OPENSQUAREBRACKET = 53
    CLOSESQUAREBRACKET = 54
    STRUCT = 55
    ENDSTRUCT = 56
    DOT = 57
    RETURN = 58
    PLUSEQUAL = 59
    SUBEQUAL = 60
    MULTEQUAL = 61
    DIVEQUAL = 62
    INVERT = 63


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

    def __eq__(self, __o: object) -> bool:
        return (self.token_type == __o.token_type
                and self.match == __o.match
                and self.line_number == __o.line_number )

class Lexer(object):
    """ Lexer Class

    Contains method tokenize_text() that converts source file text into meaningful
    tokens

    Class Attributes:
        regex_list: A list that contains token types and their regular expressions

    """

    def __init__(self) -> None:
        """ init Lexer Class """

        # this list contains all regular expressions that are recognized by
        # the programming language.
        self.regex_list = [
            # Comment
            {'type': TokenType.COMMENT, 'regex': '(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)'},

            # KeyWords:
            {'type': TokenType.CALL, 'regex': '^call'},
            {'type': TokenType.METHOD, 'regex': '^method'},
            {'type': TokenType.ELIF, 'regex': '^elif'},
            {'type': TokenType.IF, 'regex': '^if'},
            {'type': TokenType.ELSE, 'regex': '^else'},
            {'type': TokenType.FI, 'regex': '^fi'},
            {'type': TokenType.FI, 'regex': '^endif'},
            {'type': TokenType.ENDFOR, 'regex': '^endfor'},
            {'type': TokenType.ENDWHILE, 'regex': '^endwhile'},
            {'type': TokenType.BREAK, 'regex': '^break\n'},
            {'type': TokenType.CONTINUE, 'regex': '^continue\n'},
            {'type': TokenType.FOR, 'regex': '^for'},
            {'type': TokenType.WHILE, 'regex': '^while'},
            {'type': TokenType.STRUCT, 'regex': '^struct'},
            {'type': TokenType.ENDSTRUCT, 'regex': '^endstruct'},
            {'type': TokenType.ECHO, 'regex': '^echo'},
            {'type': TokenType.PRINT, 'regex': '^print'},
            {'type': TokenType.INPUT, 'regex': '^input'},
            {'type': TokenType.RETURN, 'regex': '^return'},
            {'type': TokenType.TRUE, 'regex': '^true'},
            {'type': TokenType.FALSE, 'regex': '^false'},

            # Expressions:
            {'type': TokenType.IDENTIFICATIONBETWEENBRSCKETS, 'regex': "\{.*?\}"},
            {'type': TokenType.IDENTIFICATION, 'regex': '^[a-zA-Z_$][a-zA-Z_$0-9]*'},
            {'type': TokenType.STRING, 'regex': '^"[^"]*"'},
            {'type': TokenType.REAL, 'regex': '[0-9]+\.[0-9]*'},
            {'type': TokenType.NUMBER, 'regex': '^\d+'},

            # Assignment Operators
            {'type': TokenType.EQUIVALENT, 'regex': '^=='},
            {'type': TokenType.PLUSEQUAL, 'regex': '^\+='},
            {'type': TokenType.SUBEQUAL, 'regex': '^\-='},
            {'type': TokenType.MULTEQUAL, 'regex': '^\*='},
            {'type': TokenType.DIVEQUAL, 'regex': '^\/='},
            {'type': TokenType.INVERT, 'regex': '^=!'},
            {'type': TokenType.EQUAL, 'regex': '^='},

            # Logical Compare Operators
            {'type': TokenType.NOTEQUIVALENT, 'regex': '^!='},
            {'type': TokenType.GREATERTHANOREQUAL, 'regex': '^>='},
            {'type': TokenType.LESSTHANOREQUAL, 'regex': '^<='},
            {'type': TokenType.GREATERTHAN, 'regex': '^>'},
            {'type': TokenType.LESSTHAN, 'regex': '^<'},

            # Mathematical Operators
            {'type': TokenType.ADD, 'regex': '^\+'},
            {'type': TokenType.SUB, 'regex': '^\-'},
            {'type': TokenType.MULT, 'regex': '^\*'},
            {'type': TokenType.DIV, 'regex': '^\/'},
            {'type': TokenType.MOD, 'regex': '^\%'},

            # Logical Operators
            {'type': TokenType.AND, 'regex': '^&'},
            {'type': TokenType.OR, 'regex': '^\|'},
            {'type': TokenType.NOT, 'regex': '^!'},

            #brackets and parenthesis
            {'type': TokenType.LEFTBRACKET, 'regex': '^}'},
            {'type': TokenType.RIGHTBRAKET, 'regex': '^{'},
            {'type': TokenType.OPENPARENTHESIS, 'regex': '^\('},
            {'type': TokenType.CLOSINGPARENTHESIS, 'regex': '^\)'},
            {'type': TokenType.OPENSQUAREBRACKET, 'regex': '^\['},
            {'type': TokenType.CLOSESQUAREBRACKET, 'regex': '^\]'},

            # Semicolon
            {'type': TokenType.SEMICOLON, 'regex': "^;"},

            {'type': TokenType.NEWLINE, 'regex': '^\n'},
            {'type': TokenType.SPACE, 'regex': '\s'},
            {'type': TokenType.COMMA, 'regex': '^,'},
            {'type': TokenType.DOT, 'regex': '^\.'},
        ]

    def tokenize_text(self, text: str,
                      keep_unknown=False,
                      keep_spaces=False,
                      ignore_new_lines=True) -> list:
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

                # New Token Found, remove match from text.
                text = text.removeprefix(match.group())

                if ((keep_spaces and token_type['type'] == TokenType.SPACE)
                    or (not ignore_new_lines and token_type['type'] == TokenType.NEWLINE)):
                    # add white space token to list
                    token = Token(token_type['type'], match.group(), line_number)
                    tokens.append(token)

                if token_type['type'] != TokenType.SPACE and token_type['type'] != TokenType.NEWLINE:

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
