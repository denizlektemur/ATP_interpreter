from enum import Enum


'''
Enum containing all the token types.
'''
class Token_types(Enum):
    FLOAT    = "FLOAT"
    PLUS     = "HORIZONTAL_AND_VERTICAL_LINES"
    MINUS    = "HORIZONTAL_LINE"
    DIVIDE   = "DIAGONAL_LINE"
    TIMES    = "DIAGONAL_LINES"
    IS       = "HORIZONTAL_LINES"
    VARIABLE = "VARIABLE"
    EQUALS   = "DOUBLE_HORIZONTAL_LINES"
    GREATER  = "BROKEN_LINE_RIGHT"
    LESSER   = "BROKEN_LINE_LEFT"
    IF       = "IF"
    ENDIF    = "!IF"
    WHILE    = "WHILE"
    ENDWHILE = "!WHILE"
    PRINT    = "SHOW"