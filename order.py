from typing import List, Dict
from menu_items import MenuItem
import csv

class Order:
    def __init__(self, order_id, customer_name, phone_number, menu_items):
        # Initialize the Order object with order ID, customer name, phone number, and menu items
        self.order_id = order_id
        self.customer_name = customer_name
        self.phone_number = phone_number
        self.menu_items = menu_items

    def add_order_item(self, menu_item: MenuItem, quantity: int):
        # Add a menu item to the order with the specified quantity
        for item in self.order_items:
            if item["menu_item"] == menu_item:
                item["quantity"] += quantity
                return
        self.order_items.append({"menu_item": menu_item, "quantity": quantity})

    def remove_order_item(self, menu_item: MenuItem):
        # Remove a menu item from the order
        for item in self.order_items:
            if item["menu_item"] == menu_item:
                self.order_items.remove(item)
                return

    def update_order_item_quantity(self, menu_item: MenuItem, quantity: int):
        # Update the quantity of a menu item in the order
        for item in self.order_items:
            if item["menu_item"] == menu_item:
                item["quantity"] = quantity
                return

    def get_total_price(self):
        # Calculate and return the total price of the order
        return sum(menu_item.price for menu_item in self.menu_items)

    def contains(self, menu_item: MenuItem) -> bool:
        # Check if the order contains a specific menu item
        for item in self.order_items:
            if item["menu_item"] == menu_item:
                return True
        return False

    def save_to_csv(self, filename):
        # Save the order details to a CSV file
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["order_id", "customer_name", "phone_number", "menu_item", "quantity"])
            for item in self.order_items:
                writer.writerow([self.order_id, self.customer_name, self.phone_number, item['menu_item'].name, item['quantity']])

    @staticmethod
    def load_from_csv(filename):
        # Load the order details from a CSV file and create an Order object
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            order_id = None
            customer_name = None
            phone_number = None
            order_items = []
            for row in reader:
                if order_id is None:
                    order_id = int(row['order_id'])
                    customer_name = row['customer_name']
                    phone_number = row['phone_number']
                menu_item = MenuItem(row['menu_item'], 0.0, [], "")
                quantity = int(row['quantity'])
                order_items.append({"menu_item": menu_item, "quantity": quantity})
            return Order(order_id, customer_name, phone_number, order_items)
