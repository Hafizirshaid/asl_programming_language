# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

"""

Enhanced Lexer Library

Converts code texts into meaningful lexemes to tokens:

Example:

"""

from lexer.lexer import Lexer, Token, TokenType
from exceptions.language_exception import SyntaxError


class EnhancedLexer(Lexer):
    """ Lexer Class

    Contains method tokenize_text() that converts source file text into meaningful
    tokens

    Class Attributes:
        regex_list: A list that contains token types and their regular expressions

    """

    def __init__(self) -> None:
        """ init Lexer Class """
        super().__init__()
        self.alphabets = "abcdefghijklmnopqrstuvwxyz"
        self.caps_alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.numeric = "1234567890"

    def is_numeric(self, char):
        """ Check if value is a numerical value
        Args:
            char:  Character to be checked
        Returns:
            True:  if char is a numerical value
            False: if char is not a numerical value
        """
        return char in self.numeric

    def is_alphabetical(self, char):
        """ Check if value is an alphabetical value
        Args:
            char:  Character to be checked
        Returns:
            True:  if char is an alphabetical value
            False: if char is not an alphabetical value
        """
        return char in self.alphabets or char in self.caps_alphabets

    def tokenize_text(self,
                      text: str,
                      keep_unknown=False,
                      keep_spaces=False,
                      ignore_new_lines=True) -> list:
        """ Tokenize source file text into meaningful tokens
        Args:
            text:         text file string
            keep_unknown: weather to keep an unknown token or not, a token that
                          doesn't have a type in regex_list
            keep_spaces:  weather white spaces should be added to list of tokens or not
            ignore_new_lines: weather new line tokens should be ignored
        Returns:
            list of meaningful tokens
        """

        idx = 0
        tokens = []
        line_number = 1

        while idx < len(text):
            current_char = text[idx]

            # Numerical value
            if self.is_numeric(current_char):
                number = current_char
                idx += 1
                while (idx < len(text) and (self.is_numeric(text[idx]) or text[idx] == '.')):
                    number += text[idx]
                    idx += 1
                idx -= 1
                # Real number contains dot.
                if '.' in number:
                    tokens.append(Token(TokenType.REAL, number, line_number))
                else:
                    tokens.append(Token(TokenType.NUMBER, number, line_number))
            # Alphabetical value
            elif self.is_alphabetical(current_char):
                identifier = text[idx]
                idx += 1
                # Identifier might contain letters, numbers or underscore.
                while (idx < len(text) and (self.is_alphabetical(text[idx])
                        or self.is_numeric(text[idx])
                        or text[idx] == '_')):
                    identifier += text[idx]
                    idx += 1
                idx -= 1
                # check if the found identifier is a keyword
                if identifier == 'call':
                    tokens.append(Token(TokenType.CALL, identifier, line_number))
                elif identifier == 'method':
                    tokens.append(Token(TokenType.METHOD, identifier, line_number))
                elif identifier == 'elif':
                    tokens.append(Token(TokenType.ELIF, identifier, line_number))
                elif identifier == 'if':
                    tokens.append(Token(TokenType.IF, identifier, line_number))
                elif identifier == 'else':
                    tokens.append(Token(TokenType.ELSE, identifier, line_number))
                elif identifier == 'fi':
                    tokens.append(Token(TokenType.FI, identifier, line_number))
                elif identifier == 'endif':
                    tokens.append(Token(TokenType.FI, identifier, line_number))
                elif identifier == 'endfor':
                    tokens.append(Token(TokenType.ENDFOR, identifier, line_number))
                elif identifier == 'endwhile':
                    tokens.append(Token(TokenType.ENDWHILE, identifier, line_number))
                elif identifier == 'break':
                    tokens.append(Token(TokenType.BREAK, identifier, line_number))
                elif identifier == 'continue':
                    tokens.append(Token(TokenType.CONTINUE, identifier, line_number))
                elif identifier == 'for':
                    tokens.append(Token(TokenType.FOR, identifier, line_number))
                elif identifier == 'while':
                    tokens.append(Token(TokenType.WHILE, identifier, line_number))
                elif identifier == 'struct':
                    tokens.append(Token(TokenType.STRUCT, identifier, line_number))
                elif identifier == 'endstruct':
                    tokens.append(Token(TokenType.ENDSTRUCT, identifier, line_number))
                elif identifier == 'echo':
                    tokens.append(Token(TokenType.ECHO, identifier, line_number))
                elif identifier == 'print':
                    tokens.append(Token(TokenType.PRINT, identifier, line_number))
                elif identifier == 'input':
                    tokens.append(Token(TokenType.INPUT, identifier, line_number))
                elif identifier == 'return':
                    tokens.append(Token(TokenType.RETURN, identifier, line_number))
                elif identifier == 'true':
                    tokens.append(Token(TokenType.TRUE, identifier, line_number))
                elif identifier == 'false':
                    tokens.append(Token(TokenType.FALSE, identifier, line_number))
                else:
                    tokens.append(Token(TokenType.IDENTIFICATION, identifier, line_number))
            # Space
            elif current_char == ' ':
                if keep_spaces:
                    tokens.append(Token(TokenType.SPACE, current_char, line_number))
            # New line
            elif current_char == '\n':
                line_number += 1
                if not ignore_new_lines:
                    tokens.append(Token(TokenType.NEWLINE, current_char, line_number))
            # Equal
            elif current_char == '=':
                # Equivalent
                if idx + 1 < len(text) and text[idx + 1] == '=':
                    tokens.append(Token(TokenType.EQUIVALENT, "==", line_number))
                    idx += 1
                else:
                    tokens.append(Token(TokenType.EQUAL, current_char, line_number))
            # Greater than
            elif current_char == '>':
                # Greater than or equal
                if idx + 1 < len(text) and text[idx + 1] == '=':
                    tokens.append(Token(TokenType.GREATERTHANOREQUAL, ">=", line_number))
                    idx += 1
                else:
                    tokens.append(Token(TokenType.GREATERTHAN, current_char, line_number))
                    # idx += 1
            # Less than
            elif current_char == '<':
                # Less than or equal
                if idx + 1 < len(text) and text[idx + 1] == '=':
                    tokens.append(Token(TokenType.LESSTHANOREQUAL, "<=", line_number))
                    idx += 1
                else:
                    tokens.append(Token(TokenType.LESSTHAN, current_char, line_number))
            # Plus
            elif current_char == '+':
                # Plus Equal
                if idx + 1 < len(text) and text[idx + 1] == '=':
                    tokens.append(Token(TokenType.PLUSEQUAL, "+=", line_number))
                    idx += 1
                else:
                    tokens.append(Token(TokenType.ADD, current_char, line_number))
            # Minus
            elif current_char == '-':
                # Minus Equal
                if idx + 1 < len(text) and text[idx + 1] == '=':
                    tokens.append(Token(TokenType.SUBEQUAL, "-=", line_number))
                    idx += 1
                elif idx + 1 < len(text) and self.is_numeric(text[idx + 1]):
                     # check previous token if it is also number,
                    if tokens and tokens[-1].token_type in [TokenType.NUMBER, TokenType.REAL]:
                        tokens.append(Token(TokenType.SUB, current_char, line_number))
                    else:
                        # Negative number
                        idx += 1
                        number = current_char
                        while (idx < len(text) and (self.is_numeric(text[idx]) or text[idx] == '.')):
                            number += text[idx]
                            idx += 1
                        idx -= 1
                        # Real number contains dot.
                        if '.' in number:
                            tokens.append(Token(TokenType.REAL, number, line_number))
                        else:
                            tokens.append(Token(TokenType.NUMBER, number, line_number))
                else:
                    # Subtract
                    tokens.append(Token(TokenType.SUB, current_char, line_number))
            # Multiply
            elif current_char == '*':
                # Multiply Equal
                if idx + 1 < len(text) and text[idx + 1] == '=':
                    tokens.append(Token(TokenType.MULTEQUAL, "*=", line_number))
                    idx += 1
                else:
                    tokens.append(Token(TokenType.MULT, current_char, line_number))
            # Division
            elif current_char == '/':
                # Division Equal
                if idx + 1 < len(text) and text[idx + 1] == '=':
                    tokens.append(Token(TokenType.DIVEQUAL, "/=", line_number))
                    idx += 1
                # Comment
                elif idx + 1 < len(text) and text[idx + 1] == '/':
                    # handle comment
                    idx += 1
                    comment_content = ""
                    while (idx < len(text) and text[idx] != '\n'):
                        comment_content += text[idx]
                        idx += 1
                    tokens.append(Token(TokenType.COMMENT, comment_content, line_number))
                    line_number += 1
                elif idx + 1 < len(text) and text[idx + 1] == '*':
                    # Multi line comment
                    comment_line_number = line_number
                    comment_content = ""
                    idx += 2
                    while (idx < len(text)
                           and text[idx] != '*'
                           and idx + 1 < len(text)
                           and text[idx + 1] != '/'):
                        comment_content += text[idx]
                        if text[idx] == '\n':
                            line_number += 1
                        idx += 1
                    idx += 1
                    tokens.append(Token(TokenType.COMMENT, comment_content, comment_line_number))
                else:
                    # Division
                    tokens.append(Token(TokenType.DIV, current_char, line_number))
            # Modulus
            elif current_char == '%':
                tokens.append(Token(TokenType.MOD, current_char, line_number))
            # And
            elif current_char == '&':
                tokens.append(Token(TokenType.AND, current_char, line_number))
            # Or
            elif current_char == '|':
                tokens.append(Token(TokenType.OR, current_char, line_number))
            # Not
            elif current_char == '!':
                if idx + 1 < len(text) and text[idx + 1] == '=':
                    tokens.append(Token(TokenType.NOTEQUIVALENT, "!=", line_number))
                    idx += 1
                else:
                    tokens.append(Token(TokenType.NOT, current_char, line_number))
            # Left Bracket
            elif current_char == '}':
                tokens.append(Token(TokenType.LEFTBRACKET, current_char, line_number))
            # Right Bracket
            elif current_char == '{':
                tokens.append(Token(TokenType.RIGHTBRAKET, current_char, line_number))
            # Open Parenthesis
            elif current_char == '(':
                tokens.append(Token(TokenType.OPENPARENTHESIS, current_char, line_number))
            # Close Parenthesis
            elif current_char == ')':
                tokens.append(Token(TokenType.CLOSINGPARENTHESIS, current_char, line_number))
            # Open Square Parenthesis
            elif current_char == '[':
                tokens.append(Token(TokenType.OPENSQUAREBRACKET, current_char, line_number))
            # Close Square Parenthesis
            elif current_char == ']':
                tokens.append(Token(TokenType.CLOSESQUAREBRACKET, current_char, line_number))
            # Semicolon
            elif current_char == ';':
                tokens.append(Token(TokenType.SEMICOLON, current_char, line_number))
            # String value
            elif current_char == '"':
                string_value = '"'
                idx += 1
                while (idx < len(text) and text[idx] != '"'):
                    string_value += text[idx]
                    idx += 1
                string_value += '"'
                tokens.append(Token(TokenType.STRING, string_value, line_number))
            # Dot
            elif current_char == '.':
                tokens.append(Token(TokenType.DOT, ".", line_number))
            # Comma
            elif current_char == ',':
                tokens.append(Token(TokenType.COMMA, ",", line_number))
            # Unknown chat
            else:
                if keep_unknown:
                    tokens.append(Token(TokenType.UNKNOWN, current_char, line_number))
                else:
                    self.handle_syntax_error(Token(TokenType.UNKNOWN, current_char, line_number), f"Syntax Error index: {idx}")
            idx += 1
        return tokens

    def handle_syntax_error(self, token: Token, message):
        """ Handles Syntax Errors
        Args:
            token: token that has caused the issue
            message: message
        Raises:
            SyntaxError
        """
        raise SyntaxError(f"Syntax Error at line {token.line_number} type: {token.token_type} match: {token.match}\n{message} ")
