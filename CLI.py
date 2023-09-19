import click
import sys
from customer import *
from employee import *
from menu_items import *
from menu import *
from order import *
from table import *
from customer_system import *
from employee_system import *


class MainMenu:
    def __init__(self):
        self.password = "password"
        self.customer_data = DataCustomer("customer_data.csv")
        self.employee_data = EmployeeData("employee_data.csv")
        self.choices = {
            1: self.customer_menu,
            2: self.employee_menu,
            0: self.exit
        }

    def display(self):
        while True:
            click.echo("\nMain Menu")
            click.echo("1. Customer")
            click.echo("2. Employee")
            click.echo("0. Exit")

            choice = click.prompt("Enter your choice", type=int)

            if choice in self.choices:
                if choice == 1:
                    menu_items = MenuItem.load_from_csv('menu_items.csv')
                    MenuItem.display_menu(menu_items)
                self.choices[choice]()
            else:
                click.echo("Invalid choice. Please try again.")

    def customer_menu(self):        
        while True:
            click.echo("\nCustomer Menu")
            click.echo("1. Place Order")
            click.echo("2. Exit")

            choice = click.prompt("Enter your choice", type=int)

            if choice == 1:
                order_system = OrderSystem('customer_orders.csv', menu_items)
                order_system.place_order()
            elif choice == 2:
                break
            else:
                click.echo("Invalid choice. Please try again.")


    def employee_menu(self):
                employee_system = EmployeeSystem('employee_list.csv')
                employee_system.Employee_menu()


    def exit(self):
        click.echo("\nGoodbye maybe next time.\n")
        sys.exit()


if __name__ == "__main__":
    main_menu = MainMenu()
    main_menu.display()
