from statements.statement_types import StatementType

class Statement(object):

    def __init__(self, type : StatementType) -> None:
        self.type = type
        pass
