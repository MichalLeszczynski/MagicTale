""" TODO Documentation """


from being import Being


class Character(Being):
    """ TODO Documentation """

    def __init__(self, name):
        print("Creating new character!")
        super(Character, self).__init__(name)

    @staticmethod
    def create_new_character(name = "", your_class = ""):
        if not name:
            name = input("Your name: ")
        if not your_class:
            your_class = input("Choose your class (warrior, mage, archer): ".lower())
        return Character(name)


if __name__ == "__main__":
    player = Character.create_new_character()
    print(player.name)
