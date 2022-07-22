The MIT License (MIT)

Copyright (c) 2022 Hafez Irshaid

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
------------------------------------------------------------------------------

Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

Asl Programming Language

I had some free time so I decided to develop my own programming language
for fun only. This programming langauge might have some issues, I will
continue to fix them on my free time.

keywords:
    if, elseif, else, fi, for, while, endfor, endwhile, echo, break, print

Command:

    python3 asl.py --filename filename.asl

filename.asl is the input source file
asl.py is the main file.

Sample code:
------------------------------------------------------------------
echo "while loop"
i = 0
end = 50
while "i <= end"
    if "(i % 2) == 0"
        echo "{i} is even"
    else
        echo "{i} is odd"
    fi
    i = i + 1
endwhile

echo "testing for loop"

for "var=1;var <= 1000;var = var + 1"
    if "(var % 2) == 0"
        echo "{var} is even"
    else
        echo "{var} is odd"
    fi
endfor
------------------------------------------------------------------

Remaining TODO items:
    - Variable types(number, string)
    - functions (methods) calls
    - Arrays and lists
    - Signed number comparisons - sign minus
    - handle ++ and --
    - Syntax Error Checking
    - Enhance expression evaluator to take priority
    - Implement ! operation
    - Implement exec command on shell
        exec "ls -l"
            should execute ls -l command on the shell
    - For loop, while loop and if statements remove "" and make it C/C++ style for loop
    - Implement Unit Testing.

------------------------------------------------------------
My Programming Language Block Diagram:

       -------------        --------------        ----------------        -----------------        ----------------
      |             |      |              |      |                |      |                 |      |                |
------|    Lexer    |------|    Parser    |------|    Compiler    |------|    Generator    |------|    Executor    |------> Program Output
 |    |             |  |   |              |  |   |                |  |   |                 |  |   |                |
 |     -------------   |    --------------   |    ----------------   |    -----------------   |    ----------------
 |                     |                     |                       |                        |
\ /                   \ /                   \ /                     \ /                      \ /
Input               List of               list of                Execution                 List of
File                 tokens              statements                Tree                  Instructions

Classes Description:

    Lexer: Converts code texts into meaningful lexems to tokens

    Parser: Convert list of tokens into statements and extract thier attributes

    Compiler: Compiles list of statements into execution tree

    Generator: Converts execution tree into executable instructions list

    Executor: Contains methods to execute list of instructions to produce program logical output


######################################## Regex List ##############################
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
{'type': TokenType.CONT, 'regex': '^cont'},
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
{'type': TokenType.IDENTIFICATION,'regex': '^[a-zA-Z_$][a-zA-Z_$0-9]*'},
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
######################################## Regex List ##############################
