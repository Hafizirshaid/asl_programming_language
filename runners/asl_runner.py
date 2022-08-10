# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

"""

Asl Runner:
    Contains class that runs Asl Language code

"""

from compiler.compiler import Compiler
from lexer.enhanced_lexer import EnhancedLexer
from parser.enhanced_parser import EnhancedParser
from executors.executor import Executor
from instruction_generators.instructions_generator import InstructionsGenerator


class AslRunner:
    """ AslRunner Class """

    def __init__(self,
                lexer = None,
                parser = None,
                compiler = None,
                generator = None,
                executor = None) -> None:
        """ AslRunner Class Constructor
        Args:
            lexer:
            parser:
            compiler:
            generator:
            executor:
        Returns:
            None
        """

        if lexer:
            self.lexer = lexer
        else:
            self.lexer = EnhancedLexer()

        if parser:
            self.parser = parser
        else:
            self.parser = EnhancedParser()

        if compiler:
            self.compiler = compiler
        else:
            self.compiler = Compiler()

        if generator:
            self.generator = generator
        else:
            self.generator = InstructionsGenerator()

        if executor:
            self.executor = executor
        else:
            self.executor = Executor()

    def run(self, code):
        """ Asl Language Code Runner
        Args:
            code: code text to be executed
        Returns:
            None
        """

        # Tokenize Text file into list of meaningful tokens
        tokens = self.lexer.tokenize_text(code)

        # Parses list of tokens into list of statements
        statements = self.parser.parse(tokens)

        # Compiles list of statements into execution tree
        execution_tree = self.compiler.compile(statements)

        # Generates Instructions list
        instructions = self.generator.generate_instructions(execution_tree)

        # Executes Instructions list into meaningful program
        self.executor.execute(instructions, execution_tree)
