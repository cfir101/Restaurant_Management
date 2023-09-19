import unittest
from menu import Menu, MenuItem


class TestMenu(unittest.TestCase):
    def test_init(self):
        # Test Menu initialization
        menu = Menu()
        self.assertIsInstance(menu, Menu)
        self.assertEqual(menu.menu_items, [])

    def setUp(self):
        # Set up a Menu instance and some menu items for other test cases
        self.menu = Menu()
        self.menu_item1 = MenuItem("Pizza", 12.99, ["tomato sauce", "cheese", "pepperoni"], "Main Course")
        self.menu_item2 = MenuItem("Salad", 8.99, ["lettuce", "tomatoes", "cucumbers"], "Appetizer")
        self.menu_item3 = MenuItem("Ice Cream", 5.99, ["milk", "sugar", "vanilla extract"], "Dessert")
        self.menu.add_menu_item(self.menu_item1)
        self.menu.add_menu_item(self.menu_item2)
        self.menu.add_menu_item(self.menu_item3)

    def test_add_menu_item(self):
        # Test adding a menu item to the menu
        self.assertEqual(len(self.menu.menu_items), 3)
        menu_item4 = MenuItem("Burger", 10.99, ["bun", "patty", "lettuce"], "Main Course")
        self.menu.add_menu_item(menu_item4)
        self.assertEqual(len(self.menu.menu_items), 4)
        self.assertEqual(self.menu.menu_items[-1].name, "Burger")

    def test_remove_menu_item(self):
        # Test removing a menu item from the menu
        self.assertEqual(len(self.menu.menu_items), 3)
        self.menu.remove_menu_item(self.menu_item2)
        self.assertEqual(len(self.menu.menu_items), 2)
        self.assertNotIn(self.menu_item2, self.menu.menu_items)

    def test_search_by_name(self):
        # Test searching menu items by name
        result = self.menu.search_by_name("Pizza")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].price, 12.99)
        self.assertEqual(result[0].ingredients, ["tomato sauce", "cheese", "pepperoni"])

    def test_search_by_category(self):
        # Test searching menu items by category
        result = self.menu.search_by_category("Main Course")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Pizza")
        result = self.menu.search_by_category("Dessert")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Ice Cream")

    def test_sort_by_price(self):
        # Test sorting menu items by price
        sorted_menu = self.menu.sort_by_price()
        self.assertEqual(sorted_menu[0].name, "Ice Cream")
        self.assertEqual(sorted_menu[1].name, "Salad")
        self.assertEqual(sorted_menu[2].name, "Pizza")

    def test_sort_by_popularity(self):
        # Test sorting menu items by popularity
        self.menu_item1.popularity = 10
        self.menu_item2.popularity = 20
        self.menu_item3.popularity = 5
        sorted_menu = self.menu.sort_by_popularity()
        self.assertEqual(sorted_menu[0].name, "Salad")
        self.assertEqual(sorted_menu[1].name, "Pizza")
        self.assertEqual(sorted_menu[2].name, "Ice Cream")

    def test_save_and_load_csv(self):
        # Save menu to CSV file
        file_name = "test_menu.csv"
        self.menu.save_to_csv(file_name)

        # Load menu from CSV file
        loaded_menu = Menu.load_from_csv(file_path=file_name)

        # Compare loaded menu to original menu
        self.assertEqual(len(self.menu.menu_items), len(loaded_menu.menu_items))
        for i in range(len(self.menu.menu_items)):
            self.assertEqual(self.menu.menu_items[i].name, loaded_menu.menu_items[i].name)
            self.assertEqual(self.menu.menu_items[i].price, loaded_menu.menu_items[i].price)
            self.assertEqual(self.menu.menu_items[i].ingredients, loaded_menu.menu_items[i].ingredients)
            self.assertEqual(self.menu.menu_items[i].category, loaded_menu.menu_items[i].category)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
