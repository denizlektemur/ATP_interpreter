from lex          import lex, lex_print
from token_parser import parse, parse_print
from run          import run
import sys
from time import time
import threading
from typing import List
from node import Node
import argparse


def remove_comments(lines: List[List[str]]) -> List[List[str]]:
    '''
    This function removes lines that start with a question mark.
    '''
    if len(lines) == 0:
        return []
    
    head, *tail = lines

    if head.startswith('?'):
        return remove_comments(tail)
    
    return [head] + remove_comments(tail)


def open_and_split_file(file_name: str) -> List[List[str]]:
    '''
    This function splits the text file into lines.
    These lines then get divided into seperate words.
    This functions returns a 2d list with every sub list containing the words from a line.
    '''
    text_file = open(file_name, 'r')
    text_list = text_file.read().splitlines()
    text_list = remove_comments(text_list)
    text_list = list(map(str.split, text_list))
    text_list = filter(None, text_list)
    return text_list


class run_all:
    def __init__(self, file_name):
        self.nodes = parse(lex(open_and_split_file(file_name)))

    def __call__(self):
        self.run_program(self.nodes)

    def run_program(self, nodes: List[List[Node]]):
        '''
        This function runs the program.
        '''
        print("\nProgram variables:", run(nodes).program_state)


def increase_stack_recursion():
    '''
    This function sets the recursion limit to 100000 and the stack size to 256mb
    '''
    sys.setrecursionlimit(0x100000)
    threading.stack_size(256000000)


def get_arguments():
    '''
    This function retrieves the command line arguments.
    This function returns a dictionary with the command line arguments and the value of the argument
    '''
    parser = argparse.ArgumentParser(description="Lines interpreter")
    parser.add_argument("File", help="Path to input file")
    parser.add_argument("-l", dest='-l', action='store_true', default='false', help="Print lexer output when running")
    parser.add_argument("-p", dest='-p', action='store_true', default='false', help="Print parser output when running")
    parser.add_argument("-t", dest='-t', action='store_true', default='false', help="Print the amount of time it took to run the program")

    return vars(parser.parse_args())


def main():
    '''
    Main function that gets called when the program starts.
    This function processes the given comand line arguments and calls all the functions to execute the program.
    '''
    global lex
    global parse

    increase_stack_recursion()

    arguments = get_arguments()

    if arguments['-l'] == True:
        lex = lex_print(lex)
    if arguments['-p'] == True:
        parse = parse_print(parse)
    if arguments['-t'] == True:
        start_time = time()
    
    t = threading.Thread(target=run_all(arguments['File']))
    t.start()
    t.join()

    if arguments['-t'] == True:
        print("\nThe program took", round(time() - start_time, 2), "seconds to run")


main()