# Asl Programming Language
### Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

> I had some free time so I decided to develop my own programming language
for fun only. This programming langauge might have some issues, I will
continue to fix them on my free time.

## keywords:
```
    if, elseif, else, fi, for, while, endfor, endwhile, echo, break, print
```
## Command:

```
    python3 asl.py --filename filename.asl
```

filename.asl is the input source file
asl.py is the main file.

## Sample code:
```asl
echo "while loop"
i = 0
end = 50
while (i <= end)
    if ((i % 2) == 0)
        echo "{i} is even"
    else
        echo "{i} is odd"
    fi
    i = i + 1
endwhile

echo "testing for loop"

for (var = 1; var <= 10; var = var + 1)
    if ((var % 2) == 0)
        echo "{var} is even"
    else
        echo "{var} is odd"
    fi
endfor
```
## Remaining TODO items:
    - Variable types(number, string)
    - String comparison
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
    - Implement Unit Testing.


## My Programming Language Block Diagram:

```

       -------------        --------------        ----------------        -----------------        ----------------
      |             |      |              |      |                |      |                 |      |                |
------|    Lexer    |------|    Parser    |------|    Compiler    |------|    Generator    |------|    Executor    |------> Program Output
 |    |             |  |   |              |  |   |                |  |   |                 |  |   |                |
 |     -------------   |    --------------   |    ----------------   |    -----------------   |    ----------------
 |                     |                     |                       |                        |
\ /                   \ /                   \ /                     \ /                      \ /
Input               List of               list of                Execution                 List of
File                 tokens              statements                Tree                  Instructions

```
## Classes Description:

    Lexer: Converts code texts into meaningful lexems to tokens

    Parser: Convert list of tokens into statements and extract thier attributes

    Compiler: Compiles list of statements into execution tree

    Generator: Converts execution tree into executable instructions list

    Executor: Contains methods to execute list of instructions to produce program logical output

    Expression Evaluator:

## Regex List
```python
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
```
