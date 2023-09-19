import click
import csv
from employee import *
from customer_system import *

#This Class if for the command line interface to communiction
class EmployeeSystem(Employee, EmployeeData):
    def __init__(self, file_path):
        EmployeeData.__init__(self, file_path)
        self.employee_list = self.load_data()
        self.table_number = None

    #This is for the Manager Class to add a new employee
    def add_employee(self):
        employee_id = click.prompt("Enter employee ID",type = str)
        
        name = click.prompt("Enter employee name",type= str)
        while not name.isalpha():
                click.echo("Invalid name. Please enter a valid name.")
                name = click.prompt("Enter updated employee name",type= str)
        
        email = click.prompt("Enter employee email",type = EMAIL)
        
        phone = click.prompt("Enter employee phone", type = str)
        while not phone.isdigit() or len(phone) != 10:
            click.echo("Invalid phone number. Please enter a 10-digit phone number.")
            phone = click.prompt("Enter your phone number", type=str)
        
        role = click.prompt("Enter employee role", type = str)
        
        permission = click.prompt("Enter permission", type = str)

        employee = Employee(employee_id, name, email, phone, role, permission)
        self.employee_list.append(employee)
        self.save_data(self.employee_list)
        click.echo("Employee added successfully.")
        

    def edit_employee(self):
        employee_id = click.prompt("Enter employee ID",type = str)
        for employee in self.employee_list:
            if employee.employee_id == employee_id:

                name = click.prompt("Enter a updated employee name",type= str)
                while not name.isalpha():
                    click.echo("Invalid name. Please enter a valid name.")
                    name = click.prompt("Enter employee name ",type= str)

                email = click.prompt("Enter employee email ",type = EMAIL)
                
                phone = click.prompt("Enter new employee phone ", type = str)
                while not phone.isdigit() or len(phone) != 10:
                    click.echo("Invalid phone number. Please enter a 10-digit phone number.")
                    phone = click.prompt("Enter your phone number", type=str)

                role = self.role
                
                    
                employee.edit_employee(employee_id, name, email, phone, role)
                self.save_data(self.employee_list)
                click.echo("Employee edited successfully.")
                break
        else:
            click.echo(f"Employee with ID {employee_id} not found.")

    def delete_employee(self):
        employee_id = click.prompt("Enter employee ID to delete ",type = str)
        for employee in self.employee_list:
            if employee.employee_id == employee_id:
                self.employee_list.remove(employee)
                self.save_data(self.employee_list)
                click.echo("Employee deleted successfully.")
                break
        else:
            click.echo(f"Employee with ID {employee_id} not found.")

    def assign_table(self):
        table_number = click.prompt("Enter table number to assign", type=int)
        employee_id = click.prompt("Enter employee ID to assign", type=str)
        table = self.get_table_by_number(table_number)
        if table is not None:
            table.assign_employee(employee_id)
            self.save_data(self.employee_list, self.table_number)  # Pass both arguments to save_data
            click.echo(f"Table {table_number} assigned to employee with ID {employee_id} successfully.")
        else:
            click.echo(f"Table with number {table_number} not found.")


    # Finding the menu item by it's ID
    def get_menu_item_by_id(self, item_id):
        menu_item_list = []

        for menu_item in menu_item_list:
            if menu_item.item_id == item_id:
                return menu_item
        return None


    # Finding the table by it's number
    def get_table_by_number(self, table_number):
        # Return None if table is not found
        table_list = [
            Table(1, 4),
            Table(2, 2),
            Table(3, 6),
            Table(4, 4),]

        for table in table_list:
            if table.table_number == table_number:
                return table
        return None


    def Employee_menu(self):
        while True:
            click.echo("\n===== Employee Menu =====\n")
            click.echo("1. Add Employee")
            click.echo("2. Edit Employee")
            click.echo("3. Delete Employee")
            click.echo("4. Assign Table")
            click.echo("5. Place Order")
            click.echo("6. Exit")

            choice = click.prompt("\nEnter your choice ")
            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.edit_employee()
            elif choice == "3":
                self.delete_employee()
            elif choice == "4":
                self.assign_table()
            elif choice == "5":
                order_system = OrderSystem('customer_orders.csv', menu_items)
                order_system.place_order()
            elif choice == "6":
                click.echo("\nExiting\n")
                break
            else:
                click.echo("Invalid choice. Please try again.")


if __name__ == "__main__":
    system = EmployeeSystem("employee_data.csv")
    system.Employee_menu()