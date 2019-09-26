
from inventory import Inventory
from params import Params
from consts import BASE_PARAMS


class Being:
    """ TODO Documentation """

    def __init__(self, name):
        print("Creating new being!")
        self.set_name(name)
        self.name = name
        self.inventory = Inventory()
        self.params = Params()

    def set_name(self, name):
        print("New name of character: {}".format(name))
        self.name = name
