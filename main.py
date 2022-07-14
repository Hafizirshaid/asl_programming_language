# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

"""

The MIT License (MIT)

Copyright (c) 2022 Hafez Irshaid

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import argparse
from parser import Parser

from compiler import Compiler
from executor import Executor
from instructions_generator import InstructionsGenerator
from lexer import Lexer


def main():

    """ Parse Arguments """
    parser = argparse.ArgumentParser("Asl Programming Language Command Line")

    parser.add_argument('-f', '--filename',
                        default='asl_files/continue_statement.asl',
                        help='name of source file',
                        nargs=argparse.OPTIONAL,
                        )

    args = parser.parse_args()

    filename = args.filename

    if not filename:
        raise Exception(f"file {filename} does not exist")

    """ Read File"""
    text = ""
    with open(filename) as file:
        for line in file:
            text += line

    """ Tokenize """
    lexer = Lexer()
    tokens = lexer.tokenize_text(text)

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
    #try:
    main()
    #except Exception as e:
    #    print("Unhandled Exception ", e)
