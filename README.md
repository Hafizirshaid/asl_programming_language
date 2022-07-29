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
## Remaining features to be implemented:
    - [x] Variable types(number, string)
    - [x] String comparison
    - [ ] functions (methods) calls
    - [ ] Arrays and lists
    - [ ] Signed number comparisons - sign minus
    - [ ] handle ++ and --
    - [ ] Enhanced Syntax Error Checking
    - [ ] Enhance expression evaluator to take priority
    - [ ] Implement ! operation
    - [ ] Implement exec command on shell
        exec "ls -l"
            should execute ls -l command on the shell
    - [ ] Implement Unit Testing.


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

Token Type | Regular Expression
---|:---
COMMENT  | (/\*([^*]|[\n]|(\*+([^*/]|[\n])))*\*+/)|(//.*)
CALL  |  ^call
METHOD  |  ^method
ELIF  |  ^elif
IF  |  ^if
ELSE  |  ^else
FI  |  ^fi
FI  |  ^endif
ENDFOR  |  ^endfor
ENDWHILE  |  ^endwhile
BREAK  |  ^break
CONTINUE  |  ^continue
FOR  |  ^for
WHILE  |  ^while
STRUCT  |  ^struct
ENDSTRUCT  |  ^endstruct
ECHO  |  ^echo
PRINT  |  ^print
INPUT  |  ^input
RETURN  |  ^return
TRUE  |  ^true
FALSE  |  ^false
IDENTIFICATIONBETWEENBRSCKETS  |  \{.*?\}
IDENTIFICATION  |  ^[a-zA-Z_$][a-zA-Z_$0-9]*
STRING  |  ^"[^"]*"
REAL  |  [0-9]+\.[0-9]*
NUMBER  |  ^\d+
EQUIVALENT  |  ^==
PLUSEQUAL  |  ^\+=
SUBEQUAL  |  ^\-=
MULTEQUAL  |  ^\*=
DIVEQUAL  |  ^\/=
INVERT  |  ^=!
EQUAL  |  ^=
NOTEQUIVALENT  |  ^!=
GRATERTHANOREQUAL  |  ^>=
LESSTHANOREQUAL  |  ^<=
GRATERTHAN  |  ^>
LESSTHAN  |  ^<
ADD  |  ^\+
SUB  |  ^\-
MULT  |  ^\*
DIV  |  ^\/
MOD  |  ^\%
AND  |  ^&
OR  |  ^\|
NOT  |  ^!
LEFTBRAKET  |  ^}
RIGHTBRAKET  |  ^{
OPENPARANTHESIS  |  ^\(
CLOSINGPARANTHESIS  |  ^\)
OPENSQUAREBRACKET  |  ^\[
CLOSESQUAREBRACKET  |  ^\]
SEMICOLON  |  ^;
NEWLINE  |  ^\n
SPACE  |  \s
COMMA  |  ^,
DOT  |  ^\.