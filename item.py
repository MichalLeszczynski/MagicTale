"""
Module implementing Item class.
"""


class Item:
    """
    Class representing item like from games - it has its name, and other parameters.
    """

    def __init__(self, name, value=1, weight: float = 1):
        """
        Creates new Item.
        """

        self.name = name
        self.value = value
        self.weight = weight

    def print_item(self):
        """
        Print short item description.
        """

        print("Name: ", self.name)

    def print_full_item(self):
        """
        Print long item description.
        """

        print("Name: ", self.name, ", value: ", self.value, ", weight: ", self.weight)
