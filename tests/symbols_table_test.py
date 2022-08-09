# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

"""

Symbols Table Unit Testing

"""

import unittest

from symbols.symbols_table import SymbolTable, SymbolsType


class SymbolsTableUnitTest(unittest.TestCase):
    """ SymbolsTableUnitTest Class """

    def setUp(self):
        """ setUp """
        super(SymbolsTableUnitTest, self).setUp()

    def test_symbols_table(self):
        """ test_symbols_table:
                Test adding an entry and retrieving the same entry
        """

        table = SymbolTable()
        table.add_entry("var1", "1", SymbolsType.NUMBER)
        value = table.get_entry_value("var1")
        self.assertEqual(value.name, "var1")
        self.assertEqual(value.value, "1")
        self.assertEqual(value.type,  SymbolsType.NUMBER)

    def test_symbols_table_2(self):
        """ test_symbols_table_2:
                Test adding entries and modifying entries.
        """

        table = SymbolTable()
        table.add_entry("var1", "1", SymbolsType.NUMBER)

        table.modify_entry("var1", "2")

        value = table.get_entry_value("var1")
        self.assertEqual(value.name, "var1")
        self.assertEqual(value.value, "2")
        self.assertEqual(value.type,  SymbolsType.NUMBER)

    def test_symbols_table_3(self):
        """ test_symbols_table_3:
                symbols table should raise an exception that value does not exist
                if table is empty.
        """

        table = SymbolTable()
        with self.assertRaises(Exception):
            table.modify_entry("var", "1")

    def tearDown(self):
        """ tearDown """
        super(SymbolsTableUnitTest, self).tearDown()


if __name__ == '__main__':
    unittest.main()
