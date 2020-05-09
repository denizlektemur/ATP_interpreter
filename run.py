from node       import Operator_node, Float_node, Variable_node, Print_node, If_node, Endif_node, While_node, Endwhile_node, Node
from operations import Operations
from program_state import Program_state
from typing import List


def run(nodes: List[List[Node]], program_state: Program_state = Program_state()) -> Program_state:
    '''
    This function runs the AST and returns the program state.
    '''
    if program_state.PC == len(nodes):
        return program_state

    return run(nodes, execute_node(nodes[program_state.PC][0], program_state))
    

def change_pc(program_state: Program_state, new_pc: int) -> Program_state:
    '''
    This function changes the program counter to the given new program counter.
    '''
    return Program_state(program_state.program_state, new_pc)


def execute_node(node, program_state: Program_state) -> Program_state:
    '''
    This function executes the given node by calling the matching operation.
    This function returns the new program state.
    '''
    if type(node) == Float_node:
        return node.value

    elif type(node) == Operator_node:
        if node.operation == Operations.PLUS:
            return Operations.PLUS.value[0](execute_node(node.left, program_state), execute_node(node.right, program_state))
        elif node.operation == Operations.MINUS:
            return Operations.MINUS.value[0](execute_node(node.left, program_state), execute_node(node.right, program_state))
        elif node.operation == Operations.TIMES:
            return Operations.TIMES.value[0](execute_node(node.left, program_state), execute_node(node.right, program_state))
        elif node.operation == Operations.DIVIDE:
            return Operations.DIVIDE.value[0](execute_node(node.left, program_state), execute_node(node.right, program_state))
        elif node.operation == Operations.IS:
            new_program_state = Operations.IS.value[0](program_state, node.left.name, execute_node(node.right, program_state))
            return change_pc(new_program_state, new_program_state.PC + 1)
        elif node.operation == Operations.EQUALS:
            return Operations.EQUALS.value[0](execute_node(node.left, program_state), execute_node(node.right, program_state))
        elif node.operation == Operations.GREATER:
            return Operations.GREATER.value[0](execute_node(node.left, program_state), execute_node(node.right, program_state))
        elif node.operation == Operations.LESSER:
            return Operations.LESSER.value[0](execute_node(node.left, program_state), execute_node(node.right, program_state))

    elif type(node) == Variable_node:
        return program_state.program_state[node.name]

    elif type(node) == Print_node:
        Operations.PRINT.value[0](execute_node(node.text, program_state))
        return change_pc(program_state, program_state.PC + 1)

    elif type(node) == If_node:
        if(Operations.IF.value[0](execute_node(node.condition, program_state))):
            return change_pc(program_state, program_state.PC + 1)
        else:
            return change_pc(program_state, node.row_number + 1)

    elif type(node) == Endif_node:
        return change_pc(program_state, program_state.PC + 1)

    elif type(node) == While_node:
        if(Operations.WHILE.value[0](execute_node(node.condition, program_state))):
            return change_pc(program_state, program_state.PC + 1)
        else:
            return change_pc(program_state, node.row_number + 1)
            
    elif type(node) == Endwhile_node:
        return change_pc(program_state, node.row_number)