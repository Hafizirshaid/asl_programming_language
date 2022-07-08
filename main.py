# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

import argparse
from compiler import Compiler
from executor import Executor
from expression_evaluator import Evaluator

from lexer import Lexer
from parser import Parser


def main():

    parser = argparse.ArgumentParser("Asl Programming Language Command Line")

    parser.add_argument('-f', '--filename',
        default='main.asl',
        help='name of source file',
        nargs=argparse.OPTIONAL,
    )

    args = parser.parse_args()

    filename = args.filename
    
    if not filename:
        print(f"file {filename} does not exist")
        exit(1)
    """ Read File"""
    text = ""
    with open(filename) as file:
        for line in file:
            text += line
    
    """ Tokenize """
    lexer = Lexer()
    lexes = lexer.tokenize(text)
    print("------ Lexes ---------")
    for i in lexes:
        lex_type = i['token_type']
        line_number = i['line_number']
        
        print(f"{line_number} {lex_type}")

    print("------ Lexes ---------")

    """ Parse Tokens """
    statements = []
    parser = Parser()
    statements = parser.parse(lexes)

    """ Print List of Statements """
    for statement in statements:
        print(statement.type)

    """ Compile List of statements """
    compiler = Compiler()
    execution_tree = compiler.compile(statements)
    print("------------------------")
    instructions = compiler.build_instructions_list(execution_tree)
    print("------------------------")

    """ Execute List of Instructions """
    executor = Executor()
    executor.execute(instructions)


if __name__ == "__main__":
    main()
