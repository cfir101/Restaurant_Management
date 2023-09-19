import unittest
import csv
from customer import *
from order import *
from menu_items import *
from employee_system import *


class TestOrderSystem(unittest.TestCase):
    def setUp(self):
        self.menu_items = [
            MenuItem(1, "Pizza", 10.99),
            MenuItem(2, "Burger", 8.99)
        ]
        self.order_system = OrderSystem('customer_orders.csv', self.menu_items)
        self.test_data_file = 'test_customer_orders.csv'

    def tearDown(self):
        # Clean up any test data files created during testing
        self.order_system.customer_list = []
        self.order_system.save_data()

    def test_generate_order_id(self):
        # Test generating a unique order ID
        order_id = self.order_system.generate_order_id()
        self.assertIsInstance(order_id, int)

    def test_place_order(self):
        # Test placing an order
        customer_name = "John Doe"
        phone_number = "1234567890"
        item_ids = ["1", "2"]
        expected_order_id = self.order_system.generate_order_id()

        with open(self.test_data_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['order_id', 'customer_name', 'phone_number', 'menu_item_ids'])
            writer.writerow([expected_order_id, customer_name, phone_number] + item_ids)

        self.order_system.place_order()
        customer = self.order_system.get_customer_by_id(expected_order_id)
        self.assertEqual(customer.order.order_id, expected_order_id)
        self.assertEqual(customer.order.customer_name, customer_name)
        self.assertEqual(customer.order.phone_number, phone_number)
        self.assertEqual(len(customer.order.menu_items), len(item_ids))

    def test_get_menu_item_by_id(self):
        # Test retrieving a menu item by ID
        menu_item = self.order_system.get_menu_item_by_id(1)
        self.assertEqual(menu_item.item_id, 1)
        self.assertEqual(menu_item.name, "Pizza")

    def test_get_customer_by_id(self):
        # Test retrieving a customer by order ID
        customer = Customer(1, "John Doe", "1234567890")
        self.order_system.customer_list.append(customer)
        found_customer = self.order_system.get_customer_by_id(1)
        self.assertEqual(found_customer.order.order_id, 1)
        self.assertEqual(found_customer.order.customer_name, "John Doe")
        self.assertEqual(found_customer.order.phone_number, "1234567890")


if __name__ == '__main__':
    unittest.main()
