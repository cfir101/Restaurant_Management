import csv
from menu_items import *


#a class if we want to add a new meal to the restaurant
class Menu:
    def __init__(self):
        self.menu_items = []

    def add_menu_item(self,item_id, name, price):
        menu_item = MenuItem(item_id,name, price)
        self.menu_items.append(menu_item)

#if we want to remove a course from the menu
    def remove_menu_item(self, menu_item):
        if menu_item in self.menu_items:
            self.menu_items.remove(menu_item)
        else:
            pass

#saving to csv the new menu
    def save_to_csv(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["item_id",'name', 'price'])
            for menu_item in self.menu_items:
                writer.writerow(
                    [menu_item.item_id, menu_item.price, menu_item.name])

#getting the csv file

    @classmethod
    def load_from_csv(cls, file_path):
        menu = cls()
        with open(file_path, "r") as file:
            csv_reader = csv.reader(file)
            # Skip the header row
            next(csv_reader)
            for row in csv_reader:
                item_id = row[0]
                name = row[1]
                price = float(row[2])
                menu_item = MenuItem(item_id,name, price)
                menu.add_menu_item(menu_item)
        return menu

#getting the menu items by writing the item id 
    def get_menu_item_by_id(self, item_id):
        for menu_item in self.menu_items:
            if menu_item.item_id == item_id:
                return menu_item
        return None
