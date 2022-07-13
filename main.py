# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

import argparse
import logging
from parser import Parser

from compiler import Compiler
from executor import Executor
from instructions_generator import InstructionsGenerator
from lexer import Lexer


def main():

    parser = argparse.ArgumentParser("Asl Programming Language Command Line")

    parser.add_argument('-f', '--filename',
                        default='asl_files/prime.asl',
                        help='name of source file',
                        nargs=argparse.OPTIONAL,
                        )

    args = parser.parse_args()

    filename = args.filename

    if not filename:
        logging.error(f"file {filename} does not exist")
        exit(1)

    """ Read File"""
    text = ""
    with open(filename) as file:
        for line in file:
            text += line

    """ Tokenize """
    lexer = Lexer()
    tokens = lexer.tokenize(text)

    """ Parse Tokens """
    parser = Parser()
    statements = parser.parse(tokens)

    """ Compile List of statements """
    compiler = Compiler()
    execution_tree = compiler.compile(statements)

    """ Generate Instructions """
    generator = InstructionsGenerator()
    instructions = generator.generate_instructions(execution_tree)

    """ Execute List of Instructions """
    executor = Executor()
    executor.execute(instructions, execution_tree)


if __name__ == "__main__":
    main()
