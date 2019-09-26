"""
Module implementing Item class.
"""
from trait import Trait, Traits
from consts import BASE_PARAMS

class Item:
    """
    Class representing item like from games - it has its name, and other parameters.
    """

    def __init__(self, name, value=1, weight: float = 1, traits=None):
        """
        Creates new Item.
        """

        self.name = name
        self.value = value
        self.weight = weight
        self.traits = traits

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
        if self.traits:
            self.traits.print()

    def apply_traits(self, being):
        self.traits.apply_traits(being)



if __name__ == "__main__":
    sharp = Trait("Sharp", {BASE_PARAMS.get_param("ST"): 20, BASE_PARAMS.get_param("ATT"): 5})
    magical = Trait("Magical", {BASE_PARAMS.get_param("MP"): 20})
    collection = Traits(sharp, magical)
    i1 = Item(name="spear", traits=collection)
    i1.print_full_item()
