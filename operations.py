from enum import Enum
from program_state import Program_state
from typing import Dict


def ASSIGNMENT(program_state: Program_state, name: str, value: int) -> Program_state:
    '''
    This function adds or changes a variable and returns the new program state.
    '''
    new_program_state = Program_state(program_state.program_state, program_state.PC)
    new_program_state.program_state[name] = value

    return new_program_state


'''
Enum containing basic mathematical operations.
'''
class Operations(Enum):
    PLUS    = lambda a, b : a + b,  "PLUS OPERATOR"
    MINUS   = lambda a, b : a - b,  "MINUS OPERATOR"
    TIMES   = lambda a, b : a * b,  "TIMES OPERATOR"
    DIVIDE  = lambda a, b : a / b,  "DIVIDE OPERATOR"
    IS      = ASSIGNMENT         ,  "IS OPERATOR"
    EQUALS  = lambda a, b : a == b, "EQUALS OPERATOR"
    GREATER = lambda a, b : a > b,  "GREATER OPERATOR"
    LESSER  = lambda a, b : a < b,  "LESSER OPERATOR"
    PRINT   = lambda a : print(a),  "PRINT OPERATOR"
    IF      = lambda a : a       ,  "IF OPERATOR"
    WHILE   = lambda a : a       ,  "WHILE OPERATOR"