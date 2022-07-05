
from compiler import Compiler
from executor import Executor
from expression_evaluator import Evaluator

from lexer import Lexer
from parser import Parser


def main():
    """ Read File"""
    text = ""
    with open("main.asl") as file:
        for line in file:
            text += line

    """ Tokenize """
    lexer = Lexer()
    lexes = lexer.tokenize(text)

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
