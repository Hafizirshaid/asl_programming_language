import unittest

from symbols.symbols_table import SymbolTable, SymbolsType

class SymbolsTableUnitTest(unittest.TestCase):
    def setUp(self):
        super(SymbolsTableUnitTest, self).setUp()

    def test_symbols_table(self):
        table = SymbolTable()
        table.add_entry("var1", "1", SymbolsType.NUMBER)
        value = table.get_entry_value("var1")
        self.assertEqual(value.name, "var1")
        self.assertEqual(value.value, "1")
        self.assertEqual(value.type,  SymbolsType.NUMBER)

    def test_symbols_table_2(self):
        table = SymbolTable()
        table.add_entry("var1", "1", SymbolsType.NUMBER)

        table.modify_entry("var1", "2")

        value = table.get_entry_value("var1")
        self.assertEqual(value.name, "var1")
        self.assertEqual(value.value, "2")
        self.assertEqual(value.type,  SymbolsType.NUMBER)

    def test_symbols_table_3(self):
        table = SymbolTable()
        self.assertRaises(Exception, table.modify_entry, "var", "1")

    def tearDown(self):
        super(SymbolsTableUnitTest, self).tearDown()


if __name__ == '__main__':
    unittest.main()
