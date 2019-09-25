"""
Module implementing Inventory class.
"""

from typing import Dict
from item import Item


class Inventory:
    """
    Class being container for Item class objects.
    """

    def __init__(self):
        """
        Initializes dictionary for inventory.
        """
        print("Creating new inventory!")
        self.inventory: Dict[Item, int] = {}

    def display_inventory(self):
        """
        Displays inventory - all items with its quantity.
        """

        print("\nInventory:")
        for item, count in self.inventory.items():
            multiplier = ""
            if count > 1:
                multiplier = "s"
            print(count, item.name + multiplier)
        print("\nTotal value: ", self.get_total_value())
        print("Total weight: ", self.get_total_weight())

    def get_total_weight(self):
        """
        Returns total weight of all items in the inventory.
        """
        total_weight = 0
        for item, count in self.inventory.items():
            total_weight += item.weight * count
        return total_weight

    def get_total_value(self):
        """
        Returns total value of all items in the inventory.
        """
        total_value = 0
        for item, count in self.inventory.items():
            total_value += item.value * count
        return total_value

    def add_item(self, item: Item, count=1):
        """
        Adds Item class object to inventory.
        """
        self.inventory.setdefault(item, 0)
        self.inventory[item] += count

    def add_list_of_items(self, items_list):
        for item in items_list:
            self.add_item(item)

    def __add__(self, other):
        new_inventory = Inventory()
        new_inventory.inventory.update(self.inventory)
        new_inventory.inventory.update(other.inventory)
        return new_inventory