# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

class SymbolTableEntry:
    def __init__(self, name: str, value: str, type = None) -> None:
        self.name = name
        self.value = value
        self.type = type

class SymbolTable:

    def __init__(self) -> None:
        self.symbol_table = {}

    def add_entry(self, name: str, value: str):
        self.symbol_table[name] = SymbolTableEntry(name, value)

    def get_entry_value(self, name: str):
        return self.symbol_table.get(name)

    def modify_entry(self, name, value):
        for entry in self.symbol_table:
            if entry == name:
                self.symbol_table[name].value = value
                return
        raise Exception(f"Unknown Variable name {name}")

