# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

"""

Symbols Table Library

Contains Symbols table definitions and types

"""

from enum import Enum
from typing import Optional



class SymbolsType(Enum):
    """ Symbol types enum """

    NUMBER = 1
    STRING = 2
    OBJECT = 3
    ANY = 4


class SymbolTableEntry:
    """ Symbol Table Entry Class"""

    def __init__(self, name: str, value: str, type=None) -> None:
        """ Symbol Table Entry Class Constructor
        Desc:
            Initialize Symbol Table Entry (Constrctor)
        Args:
            name: name of entry
            value: value of entry
            type: type of entry
        Returns:
            None
        """

        self.name = name
        self.value = value

        if not type:
            self.type = SymbolsType.ANY
        else:
            self.type = type


class SymbolTable:
    """ Symbol Table Class """

    def __init__(self) -> None:
        """ Initializes Symbol table to empty dictionary """
        self.symbol_table = {}

    def add_entry(self, name: str, value: str, type=None):
        """
        Desc:
            Adds entry to symbols table
        Args:
            name: name of symbol
            value: value of symbol
        Returns:
            None
        """
        self.symbol_table[name] = SymbolTableEntry(name, value, type)

    def get_entry_value(self, name: str):
        """
        Desc:
            Get Entry value from symbols table by name
        Args:
            name: name of symbol
        Returns:
            Symbol value in table
        """
        return self.symbol_table.get(name)

    def modify_entry(self, name, value):
        """
        Desc:
            Modifies an existing value of symbol by name
        Args:
            name: name of symbol
            value: new value of symbol
        Raises:
            Unknown variable exception if symbol does not exist
        Returns:
            None
        """

        # Check each entry in the table if it contains name
        for entry in self.symbol_table:
            if entry == name:
                self.symbol_table[name].value = value
                return
        raise Exception(f"Unknown Variable name {name}")
