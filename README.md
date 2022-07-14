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

TODO:
    - Variable types(number, string)
    - functions (methods) calls
    - break
    - continue
    - Arrays
    - Signed number comparisons - sign minus
    - handle ++ and --
    - Syntax Error Checking
    - Enhance expression evaluator to take priority
    - Implement ! operation