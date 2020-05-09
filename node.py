from operations import Operations

'''
Base node class all other nodes are derived from this class.
'''
class Node:
    pass


'''
Node used to store an operation and a left and right node.
'''
class Operator_node(Node):
    def __init__(self, operation: Operations, left: Node, right: Node):
        self.operation = operation
        self.left      = left
        self.right     = right

    def __str__(self):
        return 'Operator_node({operation}, {left}, {right})'.format(\
            operation = self.operation.name,
            left      = self.left,
            right     = self.right
        )

    def __repr__(self):
        return self.__str__()


'''
Node used to store an float.
'''
class Float_node(Node):
    def __init__(self, value: float):
        self.value = value

    def __str__(self):
        return 'Float({value})'.format(\
            value = self.value
        )

    def __repr__(self):
        return self.__str__()


'''
Node used to store a variable name and value.
'''
class Variable_node(Node):
    def __init__(self, name: str, value: float = None):
        self.name  = name
        self.value = value

    def __str__(self):
        return 'Var({name}, {value})'.format(\
            name  = self.name,
            value = self.value
        )

    def __repr__(self):
        return self.__str__()


'''
Node used to start a condition.
The node contains a condition and a row number.
The row number points to the line that contains the end of the condition.
'''
class If_node(Node):
    def __init__(self, condition: Operations, row_number: int = None):
        self.condition  = condition
        self.row_number = row_number

    def __str__(self):
        return 'IF({row}, {condition})'.format(\
            row  = self.row_number,
            condition = self.condition
        )

    def __repr__(self):
        return self.__str__()


'''
Node used to end a condition.
The node contains a row number.
The row number points to the line that contains the start of the condition.
'''
class Endif_node(Node):
    def __init__(self, row_number: int = None):
        self.row_number = row_number

    def __str__(self):
        return 'ENDIF({row})'.format(\
            row  = self.row_number,
        )

    def __repr__(self):
        return self.__str__()


'''
Node used to start a loop based on a condition.
The node contains a condition and a row number.
The row number points to the line that contains the end of the loop.
'''
class While_node(Node):
    def __init__(self, condition: Operations, row_number: int = None):
        self.condition  = condition
        self.row_number = row_number

    def __str__(self):
        return 'WHILE({row}, {condition})'.format(\
            row  = self.row_number,
            condition = self.condition
        )

    def __repr__(self):
        return self.__str__()


'''
Node used to end a loop.
The node contains a row number.
The row number points to the line that contains the start of the loop.
'''
class Endwhile_node(Node):
    def __init__(self, row_number: int = None):
        self.row_number = row_number

    def __str__(self):
        return 'ENDWHILE({row})'.format(\
            row  = self.row_number,
        )

    def __repr__(self):
        return self.__str__()


'''
Node used to print a variable or expression.
'''
class Print_node(Node):
    def __init__(self, text: Node):
        self.text  = text

    def __str__(self):
        return 'Print({text})'.format(\
            text  = self.text,
        )

    def __repr__(self):
        return self.__str__()