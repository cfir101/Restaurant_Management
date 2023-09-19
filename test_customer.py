import unittest
from customer import Customer, DataCustomer
import csv
from menu_items import MenuItem
from order import Order

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer(1, "John Doe", "johndoe@example.com", "1234567890", "123 Main St")

    def test_customer_attributes(self):
        # Test customer attribute values
        self.assertEqual(self.customer.customer_id, 1)
        self.assertEqual(self.customer.name, "John Doe")
        self.assertEqual(self.customer.email, "johndoe@example.com")
        self.assertEqual(self.customer.phone, "1234567890")
        self.assertEqual(self.customer.address, "123 Main St")

    def test_find_order_by_id(self):
        # Test finding an order by ID
        order_id = 1
        order = self.customer.find_order_by_id(order_id)
        self.assertIsNone(order)

    def test_place_order(self):
        # Test placing an order
        order_id = 1
        customer_id = 1
        menu_items = [MenuItem("Pizza", 10.99, "Tomato sauce", "Main Course"), MenuItem("Burger", 8.99,"Meat", "Main Course")]
        order = Order(order_id, customer_id, menu_items)
        placed_order = self.customer.place_order(order)
        self.assertIsNotNone(placed_order)
        self.assertEqual(placed_order.order_id, order_id)

    def test_modify_order(self):
        # Test modifying an order
        order_id = 1
        new_items = ["Pizza", "Burger"]
        result = self.customer.modify_order(order_id, new_items)
        self.assertFalse(result)

    def test_cancel_order(self):
        # Test canceling an order
        order_id = 1
        self.customer.cancel_order(order_id)
        order = self.customer.find_order_by_id(order_id)
        self.assertIsNone(order)

class TestDataCustomer(unittest.TestCase):
    def setUp(self):
        self.data_customer = DataCustomer("customers.csv")

    def test_read_data(self):
        # Test reading customer data from CSV
        customer_list = self.data_customer.read_data()
        self.assertIsNotNone(customer_list)
        self.assertEqual(len(customer_list), 2)
        customer = customer_list[0]
        self.assertEqual(customer.customer_id, 1)
        self.assertEqual(customer.name, "John Doe")
        self.assertEqual(customer.email, "johndoe@example.com")
        self.assertEqual(customer.phone, "1234567890")
        self.assertEqual(customer.address, "123 Main St")

    def test_write_data(self):
        # Test writing customer data to CSV
        customer_list = [
            Customer(1, "John Doe", "johndoe@example.com", "1234567890", "123 Main St"),
            Customer(2, "Jane Doe", "janedoe@example.com", "9876543210", "456 Elm St"),
        ]
        self.data_customer.write_data(customer_list)
        with open("customers.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            for i, row in enumerate(reader):
                customer_id, name, email, phone, address = row
                customer = Customer(int(customer_id), name, email, phone, address)
                self.assertEqual(customer.customer_id, customer_list[i].customer_id)
                self.assertEqual(customer.name, customer_list[i].name)
                self.assertEqual(customer.email, customer_list[i].email)
                self.assertEqual(customer.phone, customer_list[i].phone)
                self.assertEqual(customer.address, customer_list[i].address)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
