""" TODO Documentation """


from inventory import Inventory
from params import Params


class Character:
    """ TODO Documentation """

    def __init__(self, name):
        print("Creating new character!")
        self.set_name(name)
        self.name = name
        self.inventory = Inventory()
        self.params = Params()

    def set_name(self, name):
        print("Name of new character: {}".format(name))
        self.name = name

    @staticmethod
    def create_new_character():
        name = input("Your name: ")
        your_class = input("Choose your class (warrior, mage, archer): ".lower())

        return Character(name)


if __name__ == "__main__":
    player = Character.create_new_character()
    print(player.name)
