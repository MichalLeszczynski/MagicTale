""" TODO Documentation """


from being import Being


class Character(Being):
    """ TODO Documentation """

    def __init__(self, name):
        print("Creating new character!")
        super(Character, self).__init__(name)

    @staticmethod
    def create_new_character(name="", your_class="none"):
        if not name:
            name = input("Your name: ")
        return Character(name)


if __name__ == "__main__":
    player = Character.create_new_character()
    print(player.name)
