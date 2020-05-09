from token_types import Token_types
from token       import Token
from typing import List


def get_token(text: str) -> Token:
    '''
    This function returns a token based on the given string.
    '''
    if text.isdigit() or text.replace('.', '', 1).isdigit() or text.replace('-', '', 1).isdigit():
        return Token(Token_types.FLOAT, float(text))
    elif text == Token_types.PLUS.value:
        return Token(Token_types.PLUS, text)
    elif text == Token_types.MINUS.value:
        return Token(Token_types.MINUS, text)
    elif text == Token_types.DIVIDE.value:
        return Token(Token_types.DIVIDE, text)
    elif text == Token_types.TIMES.value:
        return Token(Token_types.TIMES, text)
    elif text == Token_types.IS.value:
        return Token(Token_types.IS, text)
    elif text == Token_types.EQUALS.value:
        return Token(Token_types.EQUALS, text)
    elif text == Token_types.GREATER.value:
        return Token(Token_types.GREATER, text)
    elif text == Token_types.LESSER.value:
        return Token(Token_types.LESSER, text)
    elif text == Token_types.IF.value:
        return Token(Token_types.IF, text)
    elif text == Token_types.ENDIF.value:
        return Token(Token_types.ENDIF, text)
    elif text == Token_types.WHILE.value:
        return Token(Token_types.WHILE, text)
    elif text == Token_types.ENDWHILE.value:
        return Token(Token_types.ENDWHILE, text)
    elif text == Token_types.PRINT.value:
        return Token(Token_types.PRINT, text)
    else:
        return Token(Token_types.VARIABLE, text)


def lex(text: List[List[str]]) -> List[List[Token]]:
    '''
    This function a 2d list of tokens generated from the string input.
    '''
    return list(map(lambda row: list(map(get_token, row)), text))

def lex_print(f: callable):
    '''
    This is a decorator for the lex function to print the lex output.
    '''
    def inner(text: List[List[str]]):
        print("Lexing started\n")
        tokens = f(text)
        print("Lex Output:")
        list(map(print, tokens))
        print()
        return tokens
    return inner