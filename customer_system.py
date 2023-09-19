import click
import random
from customer import *
from order import *
from employee import *
import csv


class OrderSystem:
    def __init__(self, file_path, menu_items):
        self.file_path = file_path
        self.menu = menu_items
        self.customer_list = self.load_data()

    def load_data(self):
        customer_list = []
        try:
            with open(self.file_path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip the header row
                for row in reader:
                    order_id = int(row[0])
                    customer_name = row[1]
                    phone_number = row[2]
                    menu_item_ids = [int(item_id) for item_id in row[3:]]
                    menu_items = [self.get_menu_item_by_id(item_id) for item_id in menu_item_ids]
                    order = Order(order_id, customer_name, phone_number, menu_items)
                    customer = Customer(order_id, customer_name, phone_number)  # Create a new Customer object
                    customer.order = order  # Assign the order to the customer
                    customer_list.append(customer)
        except FileNotFoundError:
            pass
        return customer_list

    def save_data(self):
        with open(self.file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['order_id', 'customer_name', 'phone_number', 'menu_item_ids'])
            for customer in self.customer_list:
                menu_item_ids = [str(menu_item.item_id) for menu_item in customer.order.menu_items]
                writer.writerow([customer.order.order_id, customer.order.customer_name,
                                 customer.order.phone_number] + menu_item_ids)
        
    def generate_order_id(self):
        used_ids = [customer.order_id for customer in self.customer_list]
        order_id = random.randint(1, 9999)
        while order_id in used_ids:
            order_id = random.randint(1, 9999)
        return order_id

    def add_customer(self, customer_name, phone_number, order_items=None):
        order_id = self.generate_order_id()
        customer = Customer(order_id, customer_name, phone_number)
        self.customer_list.append(customer)
        self.save_data()    
    

    def get_menu_item_by_id(self, item_id):
        for menu_item in self.menu:
            if menu_item.item_id == item_id:
                return menu_item
        return None

    def place_order(self):
        order_id = self.generate_order_id()
        customer = self.get_customer_by_id(order_id)

        customer_name = click.prompt("\nEnter your name", type=str)
        while not customer_name.isalpha():
            
            click.echo("Invalid name. Please enter a valid name.")
            customer_name = click.prompt("Enter your name", type=str)

        phone_number = click.prompt("Enter your phone number", type=str)
        while not phone_number.isdigit() or len(phone_number) != 10:
            
            click.echo("Invalid phone number. Please enter a 10-digit phone number.")
            phone_number = click.prompt("Enter your phone number", type=str)

        if customer is None:
            item_ids = click.prompt(
                "Enter menu item IDs to place an order (comma-separated) or 0 to end the order",
                type=str
            )
            item_ids = item_ids.strip().split(",")
            menu_items = []
            total_price = 0

            for item_id in item_ids:
                if item_id == "0":
                    click.echo("Order cancelled.\nBYE")
                    return

                while not item_id.isdigit():
                    click.echo("Invalid menu item ID. Please enter a valid menu item ID.")
                    item_id = click.prompt(
                        "Enter menu item IDs to place an order (comma-separated) or 0 to end the order",
                        type=str
                    )

                menu_item = self.get_menu_item_by_id(int(item_id))
                if menu_item is not None:
                    menu_items.append(menu_item)
                    total_price += menu_item.price
                else:
                    click.echo(f"Invalid menu item ID: {item_id}. Please try again.")
            
            
            click.echo(f"\nHi {customer_name}")
            click.echo("Order details:\n")
            click.echo(f"Order ID: {order_id}")
            click.echo("Menu items:")
            for item in menu_items:
                click.echo(f"- {item.name} (${item.price})")
            click.echo(f"Total price: ${total_price:.2f}")

            order = Order(order_id, customer_name, phone_number, menu_items)
            customer = Customer(order_id, customer_name, phone_number)  # Create a new Customer object
            customer.order = order  # Assign the order to the customer
            self.customer_list.append(customer)
            self.save_data()
            click.echo("\nOrder placed successfully.")
        else:
            click.echo("Unable to place the order. Customer not found.")

    def get_customer_by_id(self, order_id):
        for customer in self.customer_list:
            if customer.order.order_id == order_id:
                return customer
        return None


if __name__ == "__main__":
    file_path = "customers.csv" 
    menu_items = MenuItem.load_from_csv('menu_items.csv')
    order_system = OrderSystem('customer_orders.csv', menu_items)
    order_system.place_order()