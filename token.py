from token_types import Token_types
from typing import Union


'''
Token class used to store the token type and value.
'''
class Token:
    def __init__(self, type: Token_types, value: Union[str, int]):
        self.type  = type
        self.value = value

    def __str__(self):
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()