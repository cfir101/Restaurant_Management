import csv
from dataclasses import dataclass
from typing import List

@dataclass
class Table:
    table_number: int
    seating_capacity: int
    is_available: bool = True

    def __init__(self, table_number: int, seating_capacity: int):
        self.table_number = table_number
        self.seating_capacity = seating_capacity
        self.employee_id = None

    def add_tables(self):
        # Increment the table number by 1
        self.table_number += 1
        return self.table_number
    
    def assign_employee(self, employee_id):
        # Assign an employee to the table by specifying the employee ID
        self.employee_id = employee_id
    
    @staticmethod
    def write_to_csv(file_path: str, tables: List["Table"]) -> None:
        # Write the table data to a CSV file
        fieldnames = ["table_number", "seating_capacity","employee_id"]
        with open(file_path, mode="w", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for table in tables:
                writer.writerow({
                    "table_number": table.table_number,
                    "seating_capacity": table.seating_capacity,
                    "employee_id": table.employee_id
                })

    @staticmethod
    def read_from_csv(file_path: str) -> List["Table"]:
        # Read the table data from a CSV file
        tables = []
        with open(file_path, mode="r") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                table = Table(
                    table_number=int(row["table_number"]),
                    seating_capacity=int(row["seating_capacity"]),
                    employee_id=int(row["employee_id"])
                )
                tables.append(table)
        return tables

    def save(self, file_path: str) -> None:
        # Save the current table object to a CSV file
        tables = Table.read_from_csv(file_path)
        for i, table in enumerate(tables):
            if table.table_number == self.table_number:
                tables[i] = self
                break
        else:
            tables.append(self)
        Table.write_to_csv(file_path, tables)

    @staticmethod
    def load(file_path: str) -> List["Table"]:
        # Load the table data from a CSV file
        return Table.read_from_csv(file_path)
