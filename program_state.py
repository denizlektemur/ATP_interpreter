from typing import Dict


'''
Class containing the program state and program counter.
The program state is used to keep track of all the variables.
The program counter is used to keep track of the line number that needs to be executed.
'''
class Program_state:
    def __init__(self, program_state: Dict[str, float] = {}, PC: int = 0):
        self.program_state = program_state
        self.PC = PC

    def __str__(self):
        return 'Program_state({state}, {pc})'.format(\
            state = self.program_state,
            pc = self.PC
        )

    def __repr__(self):
        return self.__str__()