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

##########################################################################################################################################

My Programming Language Block Diagram:

       -------------        -------------         ----------------        ----------------         ----------------
      |             |      |              |      |                |      |                 |      |                |
------|    Lexer    |------|    Parser    |------|    Compiler    |------|    Generator    |------|    Executor    |------> Program Output
 |    |             |  |   |              |  |   |                |  |   |                 |  |   |                |
 |     -------------   |    -------------    |    ----------------   |    ----------------    |    ----------------
 |                     |                     |                       |                        |
\ /                   \ /                   \ /                     \ /                      \ /
Input               List of               list of                Execution                 List of
File                 tokens              statements                Tree                  Instructions

Classes Description:

    Lexer: Converts code texts into meaningful lexems to tokens

    Parser: Convert list of tokens into statements and extract thier attributes

    Compiler: Compiles list of statements into execution tree

    Generator: Converts execution tree into executable instructions list

    Executor: Contains methods to execute list of instructions to produce program logical output

"""

import argparse

from compiler import Compiler
from enhanced_parser import EnhancedParser
from executor import Executor
from instructions_generator import InstructionsGenerator
from lexer import Lexer


def main():
    """ Main Function, calls modules Arguemnt Parser, File Reader, Lexer,
        Parser, Compiler, Generator, Executor to execute a given source code file
    Args:
        None
    Returns:
        None
    """

    # Parse program argument
    args_parser = argparse.ArgumentParser("My Programming Language Command Line version 1.0")

    # Argument identifier: --filename or -f
    # File name that contails source code to be executed.
    args_parser.add_argument('-f', '--filename',
                        default='asl_files/one_var.asl',
                        help='source file name',
                        nargs=argparse.OPTIONAL,
                        )

    args = args_parser.parse_args()

    filename = args.filename

    # if file name not provided, raise exception
    if not filename:
        raise Exception(f"file {filename} does not exist")

    # Read Text File and store in text string
    text = ""
    with open(filename) as file:
        for line in file:
            text += line

    # Tokenizes Text file into list of meaningful tokens
    lexer = Lexer()
    tokens = lexer.tokenize_text(text)

    # Parses list of tokens into list of statements
    parser = EnhancedParser()
    statements = parser.parse(tokens)

    # Compiles list of statements into execution tree
    compiler = Compiler()
    execution_tree = compiler.compile(statements)

    # Generates Instructions list
    generator = InstructionsGenerator()
    instructions = generator.generate_instructions(execution_tree)

    # Executes Instructions list into meaningful program
    executor = Executor()
    executor.execute(instructions, execution_tree)


if __name__ == "__main__":
    # Main function
    try:
        main()
    except Exception as e:
        print("Unhandled Exception ", e)
        raise e
