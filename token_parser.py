from node import Operator_node, Int_node, Variable_node, Print_node, If_node, Endif_node, While_node, Endwhile_node, Node
from token_types import Token_types
from operations import Operations
from token import Token
from typing import List


def parse(tokens: List[List[Token]]) -> List[List[Node]]:
    '''
    This function is used to parse the given tokens into a 2d list containing nodes.
    This generates a AST.
    The tree is generated in a specific order with specific operators being handled first.
    This is done in order to adhere to mathematical priority rules. 
    '''
    lst = list(map(lambda row: get_nodes(row), tokens))
    lst = list(map(lambda row: nodes_to_tree(row, [Operations.TIMES, Operations.DIVIDE]), lst))
    lst = list(map(lambda row: nodes_to_tree(row, [Operations.PLUS, Operations.MINUS]), lst))
    lst = list(map(lambda row: nodes_to_tree(row, [Operations.EQUALS, Operations.GREATER, Operations.LESSER]), lst))
    lst = list(map(lambda row: nodes_to_tree(row, [Operations.IS, Operations.PRINT, Operations.IF, Operations.WHILE]), lst))
    lst = pair_if_and_while(lst)
    return lst



def parse_print(f: callable):
    '''
    This is a decorator for the parse function to print the parse output.
    '''
    def inner(text: List[List[str]]):
        print("Parsing started\n")
        nodes = f(text)
        print("Parse Output:")
        list(map(print, nodes))
        print()
        return nodes
    return inner



def pair_if_and_while(nodes: List[List[Node]], row: int = 0) -> List[List[Node]]:
    '''
    This function is used to pair all the if-endif while-endwhile nodes.
    Both nodes in the pair receive a line number that points to the other node's location.
    '''
    if row == len(nodes):
        return nodes
    
    if type(nodes[row][0]) == Endif_node or type(nodes[row][0]) == Endwhile_node:
        if nodes[row][0].row_number == None:
            return pair_if_and_while(find_pair(nodes, row, row), row)
    
    return pair_if_and_while(nodes, row+1)


def find_pair(nodes: List[List[Node]], row: int, location: int) -> List[List[Node]]:
    '''
    This function looks for the matching pair to a endif or endwhile node.
    Both nodes in the pair receive a line number that points to the other node's location.
    '''
    if row < 0:
        return nodes

    if (type(nodes[row][0]) == If_node and type(nodes[location][0]) == Endif_node) or (type(nodes[row][0]) == While_node and type(nodes[location][0]) == Endwhile_node):
        if nodes[row][0].row_number == None:
            new_nodes = nodes.copy()
            new_nodes[row][0].row_number = location
            new_nodes[location][0].row_number = row
            return new_nodes
    
    return find_pair(nodes, row-1, location)



def nodes_to_tree(nodes: List[Node], operations: List[Operations]) -> List[Node]:
    '''
    This function transforms the given nodes into a AST.
    This is done by looking for operators and moving the adjacent nodes into the operator node.
    '''
    if len(nodes) < 2:
        return nodes
    
    x, y, *tail = nodes

    if type(x) == Print_node and Operations.PRINT in operations:
        return nodes_to_tree([Print_node(y)] + tail, operations)
    elif type(x) == If_node and Operations.IF in operations:
        return nodes_to_tree([If_node(y)] + tail, operations)
    elif type(x) == While_node and Operations.WHILE in operations:
        return nodes_to_tree([While_node(y)] + tail, operations)

    if len(nodes) < 3:
        return nodes
    
    z, *tail = tail

    if type(y) == Operator_node:
        if y.operation in operations:
            return nodes_to_tree([Operator_node(y.operation, x, z)] + tail, operations)
    
    return [x] + nodes_to_tree(([y] + [z] + tail), operations)


def get_nodes(tokens: List[Token]) -> List[Node]:
    '''
    This function returns a list of nodes based on the given tokens.
    '''
    if len(tokens) == 0:
        return []
    
    head, *tail = tokens

    if head.type == Token_types.INTEGER:
        return [Int_node(head.value)] + get_nodes(tail)
    elif head.type == Token_types.PLUS:
        return [Operator_node(Operations.PLUS, Node, Node)] + get_nodes(tail)
    elif head.type == Token_types.MINUS:
        return [Operator_node(Operations.MINUS, Node, Node)] + get_nodes(tail)
    elif head.type == Token_types.DIVIDE:
        return [Operator_node(Operations.DIVIDE, Node, Node)] + get_nodes(tail)
    elif head.type == Token_types.TIMES:
        return [Operator_node(Operations.TIMES, Node, Node)] + get_nodes(tail)
    elif head.type == Token_types.IS:
        return [Operator_node(Operations.IS, Node, Node)] + get_nodes(tail)
    elif head.type == Token_types.VARIABLE:
        return [Variable_node(head.value)] + get_nodes(tail)
    elif head.type == Token_types.EQUALS:
        return [Operator_node(Operations.EQUALS, Node, Node)] + get_nodes(tail)
    elif head.type == Token_types.GREATER:
        return [Operator_node(Operations.GREATER, Node, Node)] + get_nodes(tail)
    elif head.type == Token_types.LESSER:
        return [Operator_node(Operations.LESSER, Node, Node)] + get_nodes(tail)
    elif head.type == Token_types.PRINT:
        return [Print_node(Node)] + get_nodes(tail)
    elif head.type == Token_types.IF:
        return [If_node(Node)] + get_nodes(tail)
    elif head.type == Token_types.ENDIF:
        return [Endif_node()] + get_nodes(tail)
    elif head.type == Token_types.WHILE:
        return [While_node(Node)] + get_nodes(tail)
    elif head.type == Token_types.ENDWHILE:
        return [Endwhile_node()] + get_nodes(tail)