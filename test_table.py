import unittest
from table import Table


class TestTable(unittest.TestCase):
    def setUp(self):
        # Set up a Table instance for other test cases
        self.table = Table(1, 4)

    def test_init(self):
        # Test Table initialization
        self.assertEqual(self.table.table_number, 1)
        self.assertEqual(self.table.seating_capacity, 4)
        self.assertEqual(self.table.is_available, True)

    def test_mark_table_available(self):
        # Test marking the table as available
        self.table.mark_table_available()
        self.assertEqual(self.table.is_available, True)

    def test_mark_table_unavailable(self):
        # Test marking the table as unavailable
        self.table.mark_table_unavailable()
        self.assertEqual(self.table.is_available, False)

    def test_update_seating_capacity(self):
        # Test updating the seating capacity of the table
        self.table.update_seating_capacity(6)
        self.assertEqual(self.table.seating_capacity, 6)

    def test_is_table_available(self):
        # Test checking if the table is available
        self.assertEqual(self.table.is_table_available(), True)
        self.table.mark_table_unavailable()
        self.assertEqual(self.table.is_table_available(), False)

    def test_save_and_load_csv(self):
        # Create table instances
        table1 = Table(1, 4)
        table2 = Table(2, 6)
        table3 = Table(3, 2)

        # Save tables to CSV file
        file_path = "test_table.csv"
        Table.write_to_csv(file_path, [table1, table2, table3])

        # Load tables from CSV file
        tables = Table.read_from_csv(file_path)

        # Assert tables are loaded correctly
        self.assertEqual(len(tables), 3)
        self.assertEqual(tables[0].table_number, 1)
        self.assertEqual(tables[0].seating_capacity, 4)
        self.assertEqual(tables[0].is_available, True)
        self.assertEqual(tables[1].table_number, 2)
        self.assertEqual(tables[1].seating_capacity, 6)
        self.assertEqual(tables[1].is_available, True)
        self.assertEqual(tables[2].table_number, 3)
        self.assertEqual(tables[2].seating_capacity, 2)
        self.assertEqual(tables[2].is_available, True)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
