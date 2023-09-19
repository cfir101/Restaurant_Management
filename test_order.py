import unittest
from order import Order
from menu_items import MenuItem
import csv


class TestOrder(unittest.TestCase):
    def test_order_init(self):
        # Test Order initialization
        order = Order(1, "John")
        self.assertEqual(order.order_id, 1)
        self.assertEqual(order.customer_name, "John")
        self.assertEqual(order.order_items, [])

    def setUp(self):
        # Set up an Order instance for other test cases
        self.order = Order(1, "Alice", None)

    def test_add_order_item(self):
        # Test adding an order item to the order
        order = Order(1, "John")
        menu_item = MenuItem("Spaghetti", 15.99, ["Pasta", "Tomato Sauce", "Meatballs"], "Entrees")
        order.add_order_item(menu_item, 2)
        self.assertEqual(len(order.order_items), 1)
        self.assertEqual(order.order_items[0]["menu_item"], menu_item)
        self.assertEqual(order.order_items[0]["quantity"], 2)

    def test_remove_order_item(self):
        # Test removing an order item from the order
        order = Order(1, "John")
        menu_item = MenuItem("Spaghetti", 15.99, ["Pasta", "Tomato Sauce", "Meatballs"], "Entrees")
        order.add_order_item(menu_item, 2)
        order.remove_order_item(menu_item)
        self.assertEqual(len(order.order_items), 0)

    def test_update_order_item_quantity(self):
        # Test updating the quantity of an order item in the order
        order = Order(1, "John")
        menu_item = MenuItem("Spaghetti", 15.99, ["Pasta", "Tomato Sauce", "Meatballs"], "Entrees")
        order.add_order_item(menu_item, 2)
        order.update_order_item_quantity(menu_item, 3)
        self.assertEqual(order.order_items[0]["quantity"], 3)

    def test_calculate_total(self):
        # Test calculating the total price of the order
        order = Order(1, "John")
        menu_item1 = MenuItem("Spaghetti", 15.99, ["Pasta", "Tomato Sauce", "Meatballs"], "Entrees")
        menu_item2 = MenuItem("Salad", 10.99, ["Lettuce", "Tomato", "Cucumber"], "Appetizers")
        order.add_order_item(menu_item1, 2)
        order.add_order_item(menu_item2, 1)
        self.assertEqual(order.calculate_total(), 42.97)

    def test_contains(self):
        # Test checking if the order contains a specific menu item
        menu_item1 = MenuItem("Pizza", 10.0, [], "Entrees")
        menu_item2 = MenuItem("Burger", 8.0, [], "Entrees")
        self.order.add_order_item(menu_item1, 2)
        self.assertTrue(self.order.contains(menu_item1))
        self.assertFalse(self.order.contains(menu_item2))

    def test_save_and_load_csv(self):
        # Create a new order
        order = Order(1, "Alice", None)
        order.add_order_item(MenuItem("Pizza", 10.0, [], "Entrees"), 2)
        order.add_order_item(MenuItem("Burger", 8.0, [], "Entrees"), 1)

        # Save the order to a CSV file
        filename = "test_order.csv"
        order.save_to_csv(filename)

        # Load the order from the CSV file
        loaded_order = Order.load_from_csv(filename)

        # Assert that the loaded order is the same as the original order
        self.assertEqual(order.order_id, loaded_order.order_id)
        self.assertEqual(order.customer_name, loaded_order.customer_name)
        self.assertEqual(len(order.order_items), len(loaded_order.order_items))
        for i in range(len(order.order_items)):
            self.assertEqual(order.order_items[i]["menu_item"].name, loaded_order.order_items[i]["menu_item"].name)
            self.assertEqual(order.order_items[i]["quantity"], loaded_order.order_items[i]["quantity"])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
