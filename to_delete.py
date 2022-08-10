
from io import StringIO
import sys
from contextvars import Token
from enhanced_lexer import EnhancedLexer
from lexer import Lexer, TokenType
from parser.enhanced_parser import EnhancedParser

code = """// program that contains all statements

for(i = 0; i < 10; i += 1)

    if (i == 1)
        echo "i is 1"
    elif (i == 9)
        echo "i is 9, breaking"
        break
    else
        echo "i value is {i}"
        continue
    fi

endfor

var = 1

while (var < 10)

    echo "var is {var}"
    if ((var %2 ) == 0)
        echo "var {var} is even"
    else
        echo "var {var} is odd"
    fi

endwhile
"""
tokens = EnhancedLexer().tokenize_text(code)
statements = EnhancedParser().parse(tokens)

for i in statements:
    print(f"Statement({i.type}),")
exit(1)
# old_stdout = sys.stdout
# old_stdin = sys.stdin

# new_stdout = StringIO()
# sys.stdout = new_stdout
# sys.stdin = StringIO("qw\n12\n13\n14")

# x = input()
# y = input()
# z = input()
# w = input()

# print("hello this is hafiz")

# sys.stdout = old_stdout

# print(new_stdout.getvalue())
# print(x)
# print(y)
# print(z)
# print(w)



# Assignment Operators



x = [{'type': TokenType.CALL, 'regex': 'call'},
     {'type': TokenType.METHOD, 'regex': 'method'},
     {'type': TokenType.ELIF, 'regex': 'elif'},
     {'type': TokenType.IF, 'regex': 'if'},
     {'type': TokenType.ELSE, 'regex': 'else'},
     {'type': TokenType.FI, 'regex': 'fi'},
     {'type': TokenType.FI, 'regex': 'endif'},
     {'type': TokenType.ENDFOR, 'regex': 'endfor'},
     {'type': TokenType.ENDWHILE, 'regex': 'endwhile'},
     {'type': TokenType.BREAK, 'regex': 'break'},
     {'type': TokenType.CONTINUE, 'regex': 'continue'},
     {'type': TokenType.FOR, 'regex': 'for'},
     {'type': TokenType.WHILE, 'regex': 'while'},
     {'type': TokenType.STRUCT, 'regex': 'struct'},
     {'type': TokenType.ENDSTRUCT, 'regex': 'endstruct'},
     {'type': TokenType.ECHO, 'regex': 'echo'},
     {'type': TokenType.PRINT, 'regex': 'print'},
     {'type': TokenType.INPUT, 'regex': 'input'},
     {'type': TokenType.RETURN, 'regex': 'return'},
     {'type': TokenType.TRUE, 'regex': 'true'},
     {'type': TokenType.FALSE, 'regex': 'false'}]

# for i in x:
#     print(
#         f"            elif identifier == '{i['regex']}':\n                tokens.append(Token({i['type']}, identifier, line_number))")

file_name = 'asl_files/new_lexer.asl'
code = ""
with open(file_name) as file:
    for line in file:
        code += line
#code = """test_lexer_true_false"""
code = """
        // one line comment
        var = 1
        /* multi
        line
        comment
        */
        var2 = 2
        """

actual_tokens = EnhancedLexer().tokenize_text(code)
tokens_2 = Lexer().tokenize_text(code)
for i in actual_tokens:
    print(f"Token({i.token_type}, '{i.match}', {i.line_number}),")

# expected_tokens = [Token(TokenType.IDENTIFICATION, 'print_value', 1),
#       Token(TokenType.EQUAL, '=', 1),
#       Token(TokenType.NUMBER, '1', 1),
#       Token(TokenType.IDENTIFICATION, 'if_cond', 1),
#       Token(TokenType.EQUAL, '=', 1),
#       Token(TokenType.NUMBER, '2', 1),
#       Token(TokenType.IDENTIFICATION, 'else_cond', 1),
#       Token(TokenType.EQUAL, '=', 1),
#       Token(TokenType.NUMBER, '3', 1),
#       Token(TokenType.IDENTIFICATION, 'echo_var', 1),
#       Token(TokenType.EQUAL, '=', 1),
#       Token(TokenType.NUMBER, '333', 1),
#       Token(TokenType.IDENTIFICATION, 'elif_cond', 1),
#       Token(TokenType.EQUAL, '=', 1),
#       Token(TokenType.NUMBER, '22', 1),
#       Token(TokenType.IDENTIFICATION, 'fi_cond', 1),
#       Token(TokenType.EQUAL, '=', 1),
#       Token(TokenType.NUMBER, '22', 1)]
