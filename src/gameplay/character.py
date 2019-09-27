""" TODO Documentation """


from src.gameplay.being import Being


class Character(Being):
    """ TODO Documentation """

    def __init__(self, name):
        print("Creating new character!")
        super(Character, self).__init__(name)


