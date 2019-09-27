from src.gameplay.inventory import Inventory
from src.gameplay.params import Params


class Being:
    """ TODO Documentation """

    def __init__(self, name):
        self.name = name
        self.name = name
        self.inventory = Inventory()
        self.params = Params()

    def set_name(self, name):
        print("New name of character: {}".format(name))
        self.name = name


if __name__ == "__main__":
    test_being = Being("test_rat")
