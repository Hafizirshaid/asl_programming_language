# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

"""

Lexer Library

Converts code texts into meaningful lexemes to tokens:

Example:

"""

from lexer import Lexer, Token, TokenType


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


    def tokenize_text(self, text: str, keep_unknown=False, keep_spaces=False, ignore_new_lines=True) -> list:
        """ Tokenize source file text
        Args:
            text: text file string
            keep_unknown: weather to keep an unknown token or not, a token that
                          doesn't have a type in regex_list
            keep_spaces: weather white spaces should be added to list of tokens or not

        Returns:
            list of meaningful tokens
        """

        idx = 0
        tokens = []
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        caps_alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numeric = "1234567890"
        line_number = 1

        while idx < len(text):
            current_char = text[idx]
            if current_char in numeric:
                number = current_char
                idx += 1
                while (idx < len(text) and (text[idx] in numeric or text[idx] == '.')):
                    number += text[idx]
                    idx += 1
                idx -= 1
                if '.' in number:
                    tokens.append(Token(TokenType.REAL, number, line_number))
                else:
                    tokens.append(Token(TokenType.NUMBER, number, line_number))
            elif current_char in alphabets or current_char in caps_alphabets:
                identifier = text[idx]
                idx += 1
                while (idx < len(text) and (text[idx] in alphabets
                        or text[idx] in caps_alphabets
                        or text[idx] in numeric
                        or text[idx] == '_')):
                    identifier += text[idx]
                    idx += 1
                idx -= 1
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
            elif current_char == ' ':
                if keep_spaces:
                    tokens.append(Token(TokenType.SPACE, current_char, line_number))
            elif current_char == '\n':
                line_number += 1
                if not ignore_new_lines:
                    tokens.append(Token(TokenType.NEWLINE, current_char, line_number))
            elif current_char == '=':
                if text[idx + 1] == '=':
                    tokens.append(Token(TokenType.EQUIVALENT, "==", line_number))
                    idx += 1
                else:
                    tokens.append(Token(TokenType.EQUAL, current_char, line_number))
            elif current_char == '>':
                if text[idx + 1] == '=':
                    tokens.append(Token(TokenType.GRATERTHANOREQUAL, ">=", line_number))
                    idx += 1
                else:
                    tokens.append(Token(TokenType.GRATERTHAN, current_char, line_number))
                    idx += 1
            elif current_char == '<':
                if text[idx + 1] == '=':
                    tokens.append(Token(TokenType.LESSTHANOREQUAL, "<=", line_number))
                    idx += 1
                else:
                    tokens.append(Token(TokenType.LESSTHAN, current_char, line_number))
            elif current_char == '+':
                if text[idx + 1] == '=':
                    tokens.append(Token(TokenType.PLUSEQUAL, "+=", line_number))
                    idx += 1
                else:
                    tokens.append(Token(TokenType.ADD, current_char, line_number))
            elif current_char == '-':
                if text[idx + 1] == '=':
                    tokens.append(Token(TokenType.SUBEQUAL, "-=", line_number))
                    idx += 1
                else:
                    tokens.append(Token(TokenType.SUB, current_char, line_number))
            elif current_char == '*':
                if text[idx + 1] == '=':
                    tokens.append(Token(TokenType.MULTEQUAL, "*=", line_number))
                    idx += 1
                else:
                    tokens.append(Token(TokenType.MULT, current_char, line_number))
            elif current_char == '/':
                if text[idx + 1] == '=':
                    tokens.append(Token(TokenType.DIVEQUAL, "/=", line_number))
                    idx += 1
                elif text[idx + 1] == '/':
                    # handle comment
                    idx += 1
                    while (idx < len(text) and text[idx] != '\n'):
                        idx += 1
                    pass
                    tokens.append(Token(TokenType.COMMENT, "", line_number))
                else:
                    tokens.append(Token(TokenType.DIV, current_char, line_number))
            elif current_char == '%':
                tokens.append(Token(TokenType.MOD, current_char, line_number))
            elif current_char == '&':
                tokens.append(Token(TokenType.AND, current_char, line_number))
            elif current_char == '|':
                tokens.append(Token(TokenType.OR, current_char, line_number))
            elif current_char == '!':
                tokens.append(Token(TokenType.NOT, current_char, line_number))
            elif current_char == '}':
                tokens.append(Token(TokenType.LEFTBRAKET, current_char, line_number))
            elif current_char == '{':
                tokens.append(Token(TokenType.RIGHTBRAKET, current_char, line_number))
            elif current_char == '(':
                tokens.append(Token(TokenType.OPENPARENTHESIS, current_char, line_number))
            elif current_char == ')':
                tokens.append(Token(TokenType.CLOSINGPARENTHESIS, current_char, line_number))
            elif current_char == '[':
                tokens.append(Token(TokenType.OPENSQUAREBRACKET, current_char, line_number))
            elif current_char == ']':
                tokens.append(Token(TokenType.CLOSESQUAREBRACKET, current_char, line_number))
            elif current_char == ';':
                tokens.append(Token(TokenType.SEMICOLON, current_char, line_number))
            elif current_char == '"':
                string_value = '"'
                idx += 1
                while (idx < len(text) and text[idx] != '"'):
                    string_value += text[idx]
                    idx += 1
                string_value += '"'
                tokens.append(Token(TokenType.STRING, string_value, line_number))
            elif current_char == '.':
                tokens.append(Token(TokenType.DOT, ".", line_number))
            elif current_char == ',':
                tokens.append(Token(TokenType.COMMA, ",", line_number))
            else:
                if keep_unknown:
                    tokens.append(Token(TokenType.UNKNOWN, "", line_number))
                else:
                    raise SyntaxError(f"Syntax Error at line {line_number} \n {current_char}")
            idx += 1
        return tokens

    pass