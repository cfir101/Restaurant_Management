import csv
import os
from order import *
from menu import *


# Customer class
class Customer:
    def __init__(self, order_id, customer_name, phone_number, menu_items=None):
        self.order_id = order_id
        self.customer_name = customer_name
        self.phone_number = phone_number
        self.menu_items = menu_items or []
        self.orders = []

    def place_order(self, order):
        self.orders.append(order)

class DataCustomer(Customer, Order,Menu):
    def __init__(self, file_path):
        self.file_path = file_path
        self.customer_list = []

    def read_data(self):
        if not os.path.exists(self.file_path):
            return []

        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            customer_list = []
            for row in reader:
                order_id, customer_name, phone_number, menu_items = row
                menu_items = eval(menu_items)  # Convert the string representation back to a list
                customer = Customer(int(order_id), customer_name, phone_number, menu_items)
                customer_list.append(customer)
        return customer_list
    
    
    def write_data(self, customer_list):
        with open(self.file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["order_id", "customer_name", "phone_number", "menu_item_ids"])
            for customer in customer_list:
                menu_item_ids = [str(menu_item.item_id) for menu_item in customer.menu_items]
                writer.writerow([customer.order_id, customer.customer_name, customer.phone_number] + menu_item_ids)

    def save_data(self):
        self.write_data(self.customer_list)

    def load_data(self):
        self.customer_list = self.read_data()
        return self.customer_list
