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
        self.alphabets: list of english language alphabets
        self.caps_alphabets: list of english language alphabets all caps
        self.numeric: list of digits
        self.idx: current id pointing to current character to be tokenized.
        self.line_number: current line number

    """

    def __init__(self) -> None:
        """ init Lexer Class """

        super().__init__()
        self.alphabets = "abcdefghijklmnopqrstuvwxyz"
        self.caps_alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.numerical_values = "1234567890"
        self.idx = 0
        self.line_number = 1

    def is_numeric(self, char):
        """ Check if value is a numerical value
        Args:
            char:  Character to be checked
        Returns:
            True:  if char is a numerical value
            False: if char is not a numerical value
        """
        return char in self.numerical_values

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

        self.idx = 0
        self.line_number = 1
        tokens = []

        while self.idx < len(text):

            current_char = text[self.idx]

            # Numerical value
            if self.is_numeric(current_char):
                self.tokenize_numerical_value(text, tokens, current_char)
            # Alphabetical value
            elif self.is_alphabetical(current_char):
                self.tokenize_alphabetical_value(text, tokens)
            # Space
            elif current_char == ' ':
                self.tokenize_space(keep_spaces, tokens, current_char)
            # New line
            elif current_char == '\n':
                self.tokenize_new_line(ignore_new_lines, tokens, current_char)
            # Equal
            elif current_char == '=':
                # Equivalent
                self.tokenize_equivalent(text, tokens, current_char)
            # Greater than
            elif current_char == '>':
                self.tokenize_greater_than(text, tokens, current_char)
            # Less than
            elif current_char == '<':
                self.tokenize_less_than(text, tokens, current_char)
            # Plus
            elif current_char == '+':
                self.tokenize_plus(text, tokens, current_char)
            # Minus
            elif current_char == '-':
                self.tokenize_minus(text, tokens, current_char)
            # Multiply
            elif current_char == '*':
                self.tokenize_multiply(text, tokens, current_char)
            # Division
            elif current_char == '/':
                self.tokenize_division(text, tokens, current_char)
            # Modulus
            elif current_char == '%':
                tokens.append(Token(TokenType.MOD, current_char, self.line_number))
            # And
            elif current_char == '&':
                tokens.append(Token(TokenType.AND, current_char, self.line_number))
            # Or
            elif current_char == '|':
                tokens.append(Token(TokenType.OR, current_char, self.line_number))
            # Not
            elif current_char == '!':
                self.tokenize_not(text, tokens, current_char)
            # Left Bracket
            elif current_char == '}':
                tokens.append(Token(TokenType.LEFTBRACKET, current_char, self.line_number))
            # Right Bracket
            elif current_char == '{':
                tokens.append(Token(TokenType.RIGHTBRAKET, current_char, self.line_number))
            # Open Parenthesis
            elif current_char == '(':
                tokens.append(Token(TokenType.OPENPARENTHESIS, current_char, self.line_number))
            # Close Parenthesis
            elif current_char == ')':
                tokens.append(Token(TokenType.CLOSINGPARENTHESIS, current_char, self.line_number))
            # Open Square Parenthesis
            elif current_char == '[':
                tokens.append(Token(TokenType.OPENSQUAREBRACKET, current_char, self.line_number))
            # Close Square Parenthesis
            elif current_char == ']':
                tokens.append(Token(TokenType.CLOSESQUAREBRACKET, current_char, self.line_number))
            # Semicolon
            elif current_char == ';':
                tokens.append(Token(TokenType.SEMICOLON, current_char, self.line_number))
            # String value
            elif current_char == '"':
                self.tokenize_string(text, tokens)
            # Dot
            elif current_char == '.':
                tokens.append(Token(TokenType.DOT, ".", self.line_number))
            # Comma
            elif current_char == ',':
                tokens.append(Token(TokenType.COMMA, ",", self.line_number))
            # Unknown chat
            else:
                self.handle_unknown_char(keep_unknown, tokens, current_char)
            self.idx += 1
        return tokens

    def handle_unknown_char(self, keep_unknown, tokens, current_char):
        """ This method determines weather unknown character should be added to tokens list or not.

        Args:
            keep_unknown: weather unknown character should be added to list of tokens or not
            tokens: list of tokens
            current_char: current character to be checked

        Returns:
            None
        """

        if keep_unknown:
            tokens.append(Token(TokenType.UNKNOWN, current_char, self.line_number))
        else:
            self.handle_syntax_error(Token(TokenType.UNKNOWN, current_char, self.line_number), f"Syntax Error index: {self.idx}")

    def tokenize_string(self, text, tokens):
        """ This method will tokenize a string and adds to to list of tokens.

        Args:
            text: code text string
            tokens: list of tokens

        Returns:
            None
        """

        string_value = '"'
        self.idx += 1
        while (self.idx < len(text) and text[self.idx] != '"'):
            string_value += text[self.idx]
            self.idx += 1
        string_value += '"'
        tokens.append(Token(TokenType.STRING, string_value, self.line_number))

    def tokenize_not(self, text, tokens, current_char):
        """ This method will tokenize not "!" operation, and determine if next char is not equal "!="

        Args:
            text: code text string
            tokens: list of tokens
            current_char: current character representing '!' char.

        Returns:
            None
        """

        if self.idx + 1 < len(text) and text[self.idx + 1] == '=':
            tokens.append(Token(TokenType.NOTEQUIVALENT, "!=", self.line_number))
            self.idx += 1
        else:
            tokens.append(Token(TokenType.NOT, current_char, self.line_number))

    def tokenize_division(self, text, tokens, current_char):
        """ This method will tokenize division operation '/', or division equal
            operation '/=' also it checks for next character,
            for one line comment '//' and multi line comments '/*' until '*/'

        Args:
            text: code text string
            tokens: list of tokens
            current_char: current character representing div '/'

        Returns:
            None
        """

        # Division Equal
        if self.idx + 1 < len(text) and text[self.idx + 1] == '=':
            tokens.append(Token(TokenType.DIVEQUAL, "/=", self.line_number))
            self.idx += 1
        # Comment
        elif self.idx + 1 < len(text) and text[self.idx + 1] == '/':
            # handle comment
            self.tokenize_one_line_comment(text, tokens)
        elif self.idx + 1 < len(text) and text[self.idx + 1] == '*':
            # Multi line comment
            self.tokenize_multi_line_comment(text, tokens)
        else:
            # Division
            tokens.append(Token(TokenType.DIV, current_char, self.line_number))

    def tokenize_multi_line_comment(self, text, tokens):
        """ This method will tokenize multi line comment, it searches
        for end of comment '*/'

        Args:
            text: code text string
            tokens: list of tokens

        Returns:
            None
        """

        comment_line_number = self.line_number
        comment_content = ""
        self.idx += 2
        while (self.idx < len(text)
               and text[self.idx] != '*'
               and self.idx + 1 < len(text)
               and text[self.idx + 1] != '/'):

            comment_content += text[self.idx]
            if text[self.idx] == '\n':
                self.line_number += 1
            self.idx += 1

        self.idx += 1
        tokens.append(Token(TokenType.COMMENT, comment_content, comment_line_number))

    def tokenize_one_line_comment(self, text, tokens):
        """ This method will tokenize one line comment, anything comes after //
        Args:
            text: text code string
            tokens: list of tokens

        Returns:
            None
        """

        self.idx += 1
        comment_content = ""
        while (self.idx < len(text) and text[self.idx] != '\n'):
            comment_content += text[self.idx]
            self.idx += 1
        tokens.append(Token(TokenType.COMMENT, comment_content, self.line_number))
        self.line_number += 1

    def tokenize_multiply(self, text, tokens, current_char):
        """ This function will tokenize multiply operation * and if it is followed by =
            so two possible tokens * or *=
        Args:
            text: code text string.
            tokens: list of tokens.
            current_char: current character.

        Returns:
            None
        """

        # Multiply Equal
        if self.idx + 1 < len(text) and text[self.idx + 1] == '=':
            tokens.append(Token(TokenType.MULTEQUAL, "*=", self.line_number))
            self.idx += 1
        else:
            tokens.append(Token(TokenType.MULT, current_char, self.line_number))

    def tokenize_minus(self, text, tokens, current_char):
        """ This method will tokenize minus operation or minus equal or negative number.
        Args:
            text: code text string.
            tokens: list of tokens.
            current_char: current char representing minus sign.

        Returns:
            None
        """

        # Minus Equal
        if self.idx + 1 < len(text) and text[self.idx + 1] == '=':
            tokens.append(Token(TokenType.SUBEQUAL, "-=", self.line_number))
            self.idx += 1
        elif self.idx + 1 < len(text) and self.is_numeric(text[self.idx + 1]):
            # check previous token if it is also number,
            if tokens and tokens[-1].token_type in [TokenType.NUMBER, TokenType.REAL]:
                tokens.append(Token(TokenType.SUB, current_char, self.line_number))
            else:
                # Negative number
                self.idx += 1
                number = current_char
                while (self.idx < len(text)
                       and (self.is_numeric(text[self.idx])
                       or text[self.idx] == '.')):
                    number += text[self.idx]
                    self.idx += 1
                self.idx -= 1
                # Real number contains dot.
                if '.' in number:
                    tokens.append(Token(TokenType.REAL, number, self.line_number))
                else:
                    tokens.append(Token(TokenType.NUMBER, number, self.line_number))
        else:
            # Subtract
            tokens.append(Token(TokenType.SUB, current_char, self.line_number))

    def tokenize_plus(self, text, tokens, current_char):
        """ This function will tokenize plus operation '+' or plus equal '+='
        Args:
            text: code text string.
            tokens: list of tokens.
            current_char: current character representing plus sign

        Returns:
            None
        """

        # Plus Equal
        if self.idx + 1 < len(text) and text[self.idx + 1] == '=':
            tokens.append(Token(TokenType.PLUSEQUAL, "+=", self.line_number))
            self.idx += 1
        else:
            tokens.append(Token(TokenType.ADD, current_char, self.line_number))

    def tokenize_less_than(self, text, tokens, current_char):
        """ This method will tokenize less than '<' or less than or equal '<='
        Args:
            text: code text string.
            tokens: list of tokens.
            current_char: current character representing less than sign

        Returns:
            None
        """

        # Less than or equal
        if self.idx + 1 < len(text) and text[self.idx + 1] == '=':
            tokens.append(Token(TokenType.LESSTHANOREQUAL, "<=", self.line_number))
            self.idx += 1
        else:
            tokens.append(Token(TokenType.LESSTHAN, current_char, self.line_number))

    def tokenize_greater_than(self, text, tokens, current_char):
        """ This method will tokenize greater than '>' or greater than or equal '>='
        Args:
            text: code text string.
            tokens: list of tokens.
            current_char: current character representing greater than sign.

        Returns:
            None
        """

        # Greater than or equal
        if self.idx + 1 < len(text) and text[self.idx + 1] == '=':
            tokens.append(Token(TokenType.GREATERTHANOREQUAL, ">=", self.line_number))
            self.idx += 1
        else:
            tokens.append(Token(TokenType.GREATERTHAN, current_char, self.line_number))

    def tokenize_equivalent(self, text, tokens, current_char):
        """ This method will tokenize equal sign '=' or equal equal sign '=='
        Args:
            text: code text string.
            tokens: list of tokens.
            current_char: current character representing equal sign.

        Returns:
            None
        """

        if self.idx + 1 < len(text) and text[self.idx + 1] == '=':
            tokens.append(Token(TokenType.EQUIVALENT, "==", self.line_number))
            self.idx += 1
        else:
            tokens.append(Token(TokenType.EQUAL, current_char, self.line_number))

    def tokenize_new_line(self, ignore_new_lines, tokens, current_char):
        """ This function will tokenize new line \n and weather this token
            should be added to list of tokens or not based on ignore_new_lines
        Args:
            ignore_new_lines: weather new lines should be ignored or not
            tokens: list of tokens
            current_char: current character representing new line

        Returns:
            None
        """

        self.line_number += 1
        if not ignore_new_lines:
            tokens.append(Token(TokenType.NEWLINE, current_char, self.line_number))

    def tokenize_space(self, keep_spaces, tokens, current_char):
        """ This function will tokenize space ' ' and adds it to list of tokens if
            keep_spaces is set to true
        Args:
            keep_spaces: weather spaces should be added to list of tokens or not
            tokens: list of tokens
            current_char: current character representing space.

        Returns:
            None
        """

        if keep_spaces:
            tokens.append(Token(TokenType.SPACE, current_char, self.line_number))

    def tokenize_alphabetical_value(self, text, tokens):
        """ This function will tokenize alphabetical value and checks if
            the alphabetical string represents a keyword or an identifier.
        Args:
            text: code text string
            tokens: list of tokens

        Returns:
            None
        """

        identifier = text[self.idx]
        self.idx += 1

        # Identifier might contain letters, numbers or underscores.
        while (self.idx < len(text)
                and (self.is_alphabetical(text[self.idx])
                or self.is_numeric(text[self.idx])
                or text[self.idx] == '_')):
            identifier += text[self.idx]
            self.idx += 1
        self.idx -= 1

        # check if the found identifier is a keyword
        self.tokenize_keyword(tokens, identifier)

    def tokenize_keyword(self, tokens, identifier):
        """ This function will tokenize a keyword or identifier and adds it to list of tokens.
        Args:
            tokens: list of tokens
            identifier: identifier string value

        Returns:
            None
        """

        if identifier == 'call':
            tokens.append(Token(TokenType.CALL, identifier, self.line_number))
        elif identifier == 'method':
            tokens.append(Token(TokenType.METHOD, identifier, self.line_number))
        elif identifier == 'elif':
            tokens.append(Token(TokenType.ELIF, identifier, self.line_number))
        elif identifier == 'if':
            tokens.append(Token(TokenType.IF, identifier, self.line_number))
        elif identifier == 'else':
            tokens.append(Token(TokenType.ELSE, identifier, self.line_number))
        elif identifier == 'fi':
            tokens.append(Token(TokenType.FI, identifier, self.line_number))
        elif identifier == 'endif':
            tokens.append(Token(TokenType.FI, identifier, self.line_number))
        elif identifier == 'endfor':
            tokens.append(Token(TokenType.ENDFOR, identifier, self.line_number))
        elif identifier == 'endwhile':
            tokens.append(Token(TokenType.ENDWHILE, identifier, self.line_number))
        elif identifier == 'break':
            tokens.append(Token(TokenType.BREAK, identifier, self.line_number))
        elif identifier == 'continue':
            tokens.append(Token(TokenType.CONTINUE, identifier, self.line_number))
        elif identifier == 'for':
            tokens.append(Token(TokenType.FOR, identifier, self.line_number))
        elif identifier == 'while':
            tokens.append(Token(TokenType.WHILE, identifier, self.line_number))
        elif identifier == 'struct':
            tokens.append(Token(TokenType.STRUCT, identifier, self.line_number))
        elif identifier == 'endstruct':
            tokens.append(Token(TokenType.ENDSTRUCT, identifier, self.line_number))
        elif identifier == 'echo':
            tokens.append(Token(TokenType.ECHO, identifier, self.line_number))
        elif identifier == 'print':
            tokens.append(Token(TokenType.PRINT, identifier, self.line_number))
        elif identifier == 'input':
            tokens.append(Token(TokenType.INPUT, identifier, self.line_number))
        elif identifier == 'return':
            tokens.append(Token(TokenType.RETURN, identifier, self.line_number))
        elif identifier == 'true':
            tokens.append(Token(TokenType.TRUE, identifier, self.line_number))
        elif identifier == 'false':
            tokens.append(Token(TokenType.FALSE, identifier, self.line_number))
        else:
            tokens.append(Token(TokenType.IDENTIFICATION, identifier, self.line_number))

    def tokenize_numerical_value(self, text, tokens, current_char):
        """ tokenize_numerical_value
        Args:
            text: text code string
            tokens: list of tokens
            current_char: current character

        Returns:
            None
        """

        number = current_char
        self.idx += 1
        while (self.idx < len(text) and (self.is_numeric(text[self.idx]) or text[self.idx] == '.')):
            number += text[self.idx]
            self.idx += 1
        self.idx -= 1
        # Real number contains dot.
        if '.' in number:
            tokens.append(Token(TokenType.REAL, number, self.line_number))
        else:
            tokens.append(Token(TokenType.NUMBER, number, self.line_number))

    def handle_syntax_error(self, token: Token, message):
        """ Handles Syntax Errors
        Args:
            token: token that has caused the issue
            message: message
        Raises:
            SyntaxError
        """
        raise SyntaxError(f"Syntax Error at line {token.line_number} type: {token.token_type} match: {token.match}\n{message} ")
