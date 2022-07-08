# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

"""
Lexer Library

"""

__version__ = '1.1'
__all__ = ['Lexer']


import re

from exceptions.syntax_error_exception import SyntaxError


class Lexer(object):
    """ Lexer Class """

    def __init__(self) -> None:
        """ init """

        self.regex_list = [
            {'type': 'comment', 'regex': '(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)'},
            {'type': 'call', 'regex': '^call'},
            {'type': 'method', 'regex': '^method'},
            {'type': 'elif', 'regex': '^elif'},
            {'type': 'if', 'regex': '^if'},
            {'type': 'else', 'regex': '^else'},
            {'type': 'fi', 'regex': '^fi'},
            {'type': 'endfor', 'regex': '^endfor'},
            {'type': 'endwhile', 'regex': '^endwhile'},
            {'type': 'break', 'regex': '^break'},
            {'type': 'cont', 'regex': '^cont'},
            {'type': 'for', 'regex': '^for'},
            {'type': 'to', 'regex': '^to'},
            {'type': 'incr', 'regex': '^incr'},
            {'type': 'while', 'regex': '^while'},
            {'type': 'do', 'regex': '^do'},
            {'type': 'echo', 'regex': '^echo'},
            {'type': 'identification', 'regex': '^[a-zA-Z_$][a-zA-Z_$0-9]*'},
            {'type': 'string', 'regex': '^"[^"]*"'},
            {'type': 'number', 'regex': '^\d+'},
            {'type': 'equivalent', 'regex': '^=='},
            {'type': 'equal', 'regex': '^='},
            {'type': 'notequivalent', 'regex': '^!='},
            {'type': 'graterthanorequal', 'regex': '^>='},
            {'type': 'lessthanorequal', 'regex': '^<='},
            {'type': 'graterthan', 'regex': '^>'},
            {'type': 'lessthan', 'regex': '^<'},
            {'type': 'add', 'regex': '^\+'},
            {'type': 'sub', 'regex': '^\-'},
            {'type': 'mult', 'regex': '^\*'},
            {'type': 'div', 'regex': '^\/'},
            {'type': 'mod', 'regex': '^\%'},
            {'type': 'and', 'regex': '^&'},
            {'type': 'or', 'regex': '^\|'},
            {'type': 'not', 'regex': '^!'},
            {'type': 'true', 'regex': '^true'},
            {'type': 'false', 'regex': '^false'},
            {'type': 'newline', 'regex': '^\n'},
            {'type': 'space', 'regex': '\s'},
            {'type': 'openparanthesis', 'regex': '^\('},
            {'type': 'closingparanthesis', 'regex': '^\)'},
        ]

    def tokenize(self, text: str) -> list:
        """ Tokenize source file
        Args:
            text: text file string

        Returns:
            list of lexes
        """

        tokens = []
        line_number = 1

        while text:

            token_type = None
            match = None

            """ Find Matching token in regex_list """
            for regex in self.regex_list:

                current_match = re.match(regex['regex'], text)
                if current_match is not None:
                    """ match found """
                    token_type = regex
                    match = current_match
                    break
                pass

            if match is not None:
                """ New Token Found, remove token from text """
                text = text.removeprefix(match.group())
                tokens.append(
                    {'match': match, 'token_type': token_type,
                        'line_number': line_number})

                if token_type['type'] == 'newline':
                    line_number += 1
            else:
                """ Exception, unrecognized char, syntax error """
                raise SyntaxError(f"Syntax Error at line {line_number} \n {text}")
            pass
        return tokens
