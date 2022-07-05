# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

from enum import Enum

class StatementType(Enum):

    ECHO = 1
    VAR = 2
    IF = 3
    ELSEIF = 4
    ELSE = 5
    FOR = 6
    ENDFOR = 7
    ENDIF = 8
    CONDITION = 9
    WHILE = 10
    ENDWHILE = 11
    BREAK = 12